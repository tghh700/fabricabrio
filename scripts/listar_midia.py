"""Lista os últimos posts de cada perfil (sem imprimir tokens) e grava em config.midia_<perfil> no D1 via SQL."""
import json, os, urllib.parse, urllib.request
IDS = {"brio": "17841418207775427", "fibra": "17841417348851668", "diaum": "17841456016332755"}
linhas = []
for perfil, ig in IDS.items():
    tok = os.environ.get("IG_TOKEN_" + perfil.upper(), "")
    q = urllib.parse.urlencode({"fields": "id,caption,timestamp,permalink,media_type,thumbnail_url,media_url", "limit": 100, "access_token": tok})
    try:
        with urllib.request.urlopen(f"https://graph.facebook.com/v25.0/{ig}/media?{q}", timeout=30) as r:
            d = json.loads(r.read().decode())
        itens = [{"id": m["id"], "ts": m.get("timestamp"), "link": m.get("permalink"), "cap": (m.get("caption") or "")[:90]} for m in d.get("data", [])]
        # cópia completa + miniaturas para conferir repetição (vai para o branch previas, sem token)
        os.makedirs(f"saida/midia/{perfil}", exist_ok=True)
        completo = []
        for m in d.get("data", []):
            completo.append({"id": m["id"], "ts": m.get("timestamp"), "link": m.get("permalink"), "tipo": m.get("media_type"), "legenda": m.get("caption") or ""})
            thumb = m.get("thumbnail_url") or (m.get("media_url") if m.get("media_type") == "IMAGE" else None)
            if thumb:
                try:
                    urllib.request.urlretrieve(thumb, f"saida/midia/{perfil}/{m['id']}.jpg")
                except Exception:
                    pass
        json.dump(completo, open(f"saida/midia/{perfil}.json", "w"), ensure_ascii=False, indent=1)
    except Exception as e:
        itens = [{"erro": type(e).__name__ + ": " + str(getattr(e, "code", ""))}]
    print(perfil, len(itens))
    v = json.dumps(itens, ensure_ascii=False).replace("'", "''")
    linhas.append(f"INSERT INTO config (chave, valor) VALUES ('midia_{perfil}', '{v}') ON CONFLICT(chave) DO UPDATE SET valor=excluded.valor, atualizado_em=datetime('now');")
open("midia.sql", "w").write("\n".join(linhas) + "\n")
