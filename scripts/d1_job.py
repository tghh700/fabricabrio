"""Pedido ao D1 via wrangler (rodado pelo workflow d1-job).
Lê jobs/d1.json:
  {"nome": "...",
   "videos": [{"id","perfil","tema_canonico","gancho","gatilho_tipo","palavra_chave","arquivo",
               "legenda","hashtags","duracao_s","dm_texto"(opcional),"agendado_para" (UTC 'AAAA-MM-DD HH:MM:SS')}],
   "creditos": [{"video_id","quantidade"}],
   "sql": ["UPDATE ...", ...]   (opcional, comandos extras)
  }
Regras checadas antes de gravar: tema canônico não pode existir em outro perfil; arquivo tem que existir no branch midia.
Sempre grava o estado (posts, métricas, temas, cliques) em saida/estado.json."""
import json, os, re, subprocess, sys, urllib.request

DB = "fabrica-brio"
RAW = "https://raw.githubusercontent.com/tghh700/fabricabrio/midia/"


BRIU = re.compile(r"br[íi]u", re.I)


def escrita(txt):
    """'Bríu' é só pronúncia (narração). Na escrita é sempre 'Brio'."""
    return BRIU.sub(lambda m: "BRIO" if m.group(0).isupper() else "Brio", txt) if isinstance(txt, str) else txt


def q(v):
    if v is None:
        return "NULL"
    if isinstance(v, (int, float)):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


def d1(sql=None, arquivo=None):
    cmd = ["npx", "--yes", "wrangler@4", "d1", "execute", DB, "--remote", "--json"]
    cmd += ["--file", arquivo] if arquivo else ["--command", sql]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:]); raise SystemExit("falha no D1")
    try:
        return json.loads(r.stdout)
    except Exception:
        return r.stdout


def linhas(sql):
    res = d1(sql)
    return res[0]["results"] if isinstance(res, list) and res else []


def existe_midia(arq):
    try:
        req = urllib.request.Request(RAW + arq, method="HEAD")
        return urllib.request.urlopen(req, timeout=20).status == 200
    except Exception:
        return False


def main():
    job = json.load(open("jobs/d1.json"))
    os.makedirs("saida", exist_ok=True)
    rel = {"nome": job.get("nome"), "gravados": [], "recusados": []}
    temas = {(r["tema_canonico"] or "").strip().lower(): r["perfil"] for r in linhas("SELECT tema_canonico, perfil FROM videos")}
    sql = []
    for v in job.get("videos", []):
        tema = (v["tema_canonico"] or "").strip().lower()
        if tema in temas and temas[tema] != v["perfil"]:
            rel["recusados"].append({"id": v["id"], "motivo": f"tema já usado no perfil {temas[tema]}"}); continue
        if not existe_midia(v["arquivo"]):
            rel["recusados"].append({"id": v["id"], "motivo": "arquivo não está no branch midia"}); continue
        for campo in ("legenda", "dm_texto", "gancho", "hashtags"):
            if isinstance(v.get(campo), str) and BRIU.search(v[campo]):
                v[campo] = escrita(v[campo]); rel.setdefault("corrigidos_briu", []).append(f"{v['id']}.{campo}")
        cols = ["id", "perfil", "tema_canonico", "gancho", "gatilho_tipo", "palavra_chave", "arquivo", "legenda", "hashtags", "duracao_s", "dm_texto"]
        sql.append("INSERT OR REPLACE INTO videos (" + ",".join(cols) + ",status) VALUES (" + ",".join(q(v.get(c)) for c in cols) + ",'pronto');")
        if v.get("agendado_para"):
            sql.append(f"DELETE FROM posts WHERE video_id={q(v['id'])} AND status='agendado';")
            sql.append(f"INSERT INTO posts (video_id, perfil, agendado_para) VALUES ({q(v['id'])},{q(v['perfil'])},{q(v['agendado_para'])});")
        rel["gravados"].append(v["id"])
    for c in job.get("creditos", []):
        sql.append(f"INSERT INTO creditos (servico, video_id, quantidade) VALUES ('elevenlabs',{q(c.get('video_id'))},{int(c['quantidade'])});")
    sql += job.get("sql", [])
    if sql:
        open("/tmp/job.sql", "w").write("\n".join(sql))
        d1(arquivo="/tmp/job.sql")
    estado = {
        "posts": linhas("SELECT p.id, p.video_id, p.perfil, p.agendado_para, p.status, p.permalink, p.erro, v.tema_canonico FROM posts p LEFT JOIN videos v ON v.id=p.video_id WHERE p.agendado_para >= datetime('now','-10 days') ORDER BY p.agendado_para"),
        "temas": linhas("SELECT id, perfil, tema_canonico, status FROM videos ORDER BY criado_em"),
        "metricas": linhas("SELECT m.post_id, p.video_id, p.perfil, max(m.views) views, max(m.alcance) alcance, max(m.curtidas) curtidas, max(m.comentarios) comentarios, max(m.salvamentos) salvamentos, max(m.compartilhamentos) compartilhamentos, max(m.tempo_medio_ms) tempo_medio_ms FROM metricas m JOIN posts p ON p.id=m.post_id GROUP BY m.post_id ORDER BY views DESC"),
        "cliques": linhas("SELECT perfil, video_id, origem, count(*) n FROM cliques GROUP BY perfil, video_id, origem ORDER BY n DESC"),
        "dms": linhas("SELECT perfil, status, count(*) n FROM dms GROUP BY perfil, status"),
        "creditos": linhas("SELECT servico, sum(quantidade) total FROM creditos GROUP BY servico"),
        "logs": linhas("SELECT tipo, titulo, criada_em FROM tasks WHERE status='log' ORDER BY id DESC LIMIT 20"),
        "config": linhas("SELECT chave, valor FROM config WHERE chave IN ('cron_ultimo','escala','pausa_global')"),
    }
    json.dump({"relatorio": rel, "estado": estado}, open("saida/estado.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(rel, ensure_ascii=False))
    if rel["recusados"]:
        sys.exit(0)


if __name__ == "__main__":
    main()
