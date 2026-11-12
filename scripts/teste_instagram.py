"""Confere os tokens do Instagram (IG_TOKEN_BRIO/FIBRA/DIAUM) sem nunca imprimir o token.

Testa os dois hosts possíveis (Instagram Login e Facebook Login / Unified login),
descobre o ID e o @ de cada perfil, consulta o limite de publicação e gera um
arquivo SQL que grava o resultado (sem tokens) na tabela config do D1.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

V = "v25.0"
PERFIS = {"brio": "IG_TOKEN_BRIO", "fibra": "IG_TOKEN_FIBRA", "diaum": "IG_TOKEN_DIAUM"}
USERNAMES = {"brio": "briotreino", "fibra": "fibratreino", "diaum": "diaumtreino"}


def get(host, path, params, token):
    q = urllib.parse.urlencode({**params, "access_token": token})
    url = f"https://{host}/{V}/{path}?{q}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            body = json.loads(e.read().decode())
        except Exception:
            body = {"erro": str(e.code)}
        return e.code, body
    except Exception as e:  # rede
        return 0, {"erro": type(e).__name__}


def limpa(obj, token):
    s = json.dumps(obj, ensure_ascii=False)
    return json.loads(s.replace(token, "***")) if token else obj


def testar(perfil, token):
    res = {"perfil": perfil, "tipo_token": None, "ig_user_id": None, "username": None, "limite": None, "erros": []}
    # 1) Token de Instagram Login
    st, b = get("graph.instagram.com", "me", {"fields": "user_id,username,account_type"}, token)
    if st == 200 and b.get("username"):
        res.update(tipo_token="instagram", ig_user_id=str(b.get("user_id") or b.get("id")), username=b["username"])
        host = "graph.instagram.com"
    else:
        res["erros"].append({"graph.instagram.com/me": b.get("error", b)})
        # 2) Token de Facebook Login / usuário de sistema
        st2, b2 = get("graph.facebook.com", "me", {"fields": "id,name"}, token)
        if st2 != 200:
            res["erros"].append({"graph.facebook.com/me": b2.get("error", b2)})
            return limpa(res, token)
        res["tipo_token"] = "facebook"
        host = "graph.facebook.com"
        # Procura as contas do Instagram acessíveis ao token
        achou = None
        st3, b3 = get(host, "me/accounts", {"fields": "instagram_business_account{id,username}"}, token)
        for p in (b3.get("data") or []) if st3 == 200 else []:
            iba = p.get("instagram_business_account")
            if iba and iba.get("username") == USERNAMES[perfil]:
                achou = iba
        if not achou:
            res["erros"].append({"me/accounts": b3.get("error", "sem conta correspondente") if isinstance(b3, dict) else b3})
            # tenta pelo ID conhecido salvo no D1 (passado via env)
            known = os.environ.get(f"IG_ID_{perfil.upper()}")
            if known:
                st4, b4 = get(host, known, {"fields": "id,username"}, token)
                if st4 == 200:
                    achou = b4
                else:
                    res["erros"].append({"ig_id_conhecido": b4.get("error", b4)})
        if achou:
            res["ig_user_id"] = str(achou["id"])
            res["username"] = achou.get("username")
    if res["ig_user_id"]:
        st5, b5 = get(host, f"{res['ig_user_id']}/content_publishing_limit", {"fields": "quota_usage,config"}, token)
        res["limite"] = b5 if st5 == 200 else {"erro": b5.get("error", b5)}
    return limpa(res, token)


def sql_str(s):
    return "'" + s.replace("'", "''") + "'"


def main():
    linhas, resumo, falhas = [], [], 0
    for perfil, var in PERFIS.items():
        token = os.environ.get(var, "").strip()
        if not token:
            r = {"perfil": perfil, "erros": [f"segredo {var} vazio"]}
        else:
            r = testar(perfil, token)
        ok = bool(r.get("ig_user_id"))
        falhas += 0 if ok else 1
        resumo.append(f"{perfil}: {'OK' if ok else 'FALHOU'} @{r.get('username')} id={r.get('ig_user_id')} tipo={r.get('tipo_token')}")
        linhas.append(
            "INSERT INTO config (chave, valor) VALUES (%s, %s) ON CONFLICT(chave) DO UPDATE SET valor=excluded.valor, atualizado_em=datetime('now');"
            % (sql_str(f"teste_ig_{perfil}"), sql_str(json.dumps(r, ensure_ascii=False)))
        )
        if ok:
            linhas.append(
                "UPDATE contas SET ig_user_id=%s WHERE perfil=%s;" % (sql_str(r["ig_user_id"]), sql_str(perfil))
            )
            if r.get("tipo_token"):
                linhas.append(
                    "INSERT INTO config (chave, valor) VALUES (%s, %s) ON CONFLICT(chave) DO UPDATE SET valor=excluded.valor, atualizado_em=datetime('now');"
                    % (sql_str(f"ig_host_{perfil}"), sql_str("graph.instagram.com" if r["tipo_token"] == "instagram" else "graph.facebook.com"))
                )
    with open("resultado_teste.sql", "w") as f:
        f.write("\n".join(linhas) + "\n")
    print("\n".join(resumo))
    sys.exit(0)  # o resultado vai para o D1; falha não derruba o job


if __name__ == "__main__":
    main()
