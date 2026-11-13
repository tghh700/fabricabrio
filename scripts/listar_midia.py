"""Lista os últimos posts de cada perfil (sem imprimir tokens) e grava em config.midia_<perfil> no D1 via SQL."""
import json, os, urllib.error, urllib.parse, urllib.request
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
            item = {"id": m["id"], "ts": m.get("timestamp"), "link": m.get("permalink"), "tipo": m.get("media_type"), "legenda": m.get("caption") or ""}
            # métricas (precisa da permissão de insights no token; sem ela, registra o erro sem expor o token)
            mets = "views,reach,likes,comments,saved,shares,total_interactions"
            if m.get("media_type") == "VIDEO":
                mets += ",ig_reels_avg_watch_time,ig_reels_video_view_total_time"
            for tentativa in (mets, "views,reach,likes,comments,saved,shares"):
                try:
                    qi = urllib.parse.urlencode({"metric": tentativa, "access_token": tok})
                    with urllib.request.urlopen(f"https://graph.facebook.com/v25.0/{m['id']}/insights?{qi}", timeout=30) as r2:
                        di = json.loads(r2.read().decode())
                    item["metricas"] = {x["name"]: (x.get("values") or [{}])[0].get("value", x.get("total_value", {}).get("value")) for x in di.get("data", [])}
                    item.pop("metricas_erro", None)
                    break
                except urllib.error.HTTPError as e:
                    try:
                        item["metricas_erro"] = json.loads(e.read().decode()).get("error", {}).get("message", "")[:200]
                    except Exception:
                        item["metricas_erro"] = f"HTTP {e.code}"
                except Exception as e:
                    item["metricas_erro"] = type(e).__name__
            completo.append(item)
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


def _diagnostico():
    """Mostra o tipo do token e as permissões concedidas (nunca imprime o token)."""
    for perfil in IDS:
        tok = os.environ.get("IG_TOKEN_" + perfil.upper(), "")
        if not tok:
            print("diag", perfil, "sem token"); continue
        q = urllib.parse.urlencode({"input_token": tok, "access_token": tok})
        try:
            with urllib.request.urlopen("https://graph.facebook.com/v25.0/debug_token?" + q, timeout=30) as r:
                d = json.loads(r.read().decode()).get("data", {})
            print("diag", perfil, "tipo=", d.get("type"), "app=", d.get("application"), "valido=", d.get("is_valid"),
                  "expira=", d.get("expires_at"), "scopes=", d.get("scopes"))
        except urllib.error.HTTPError as e:
            try:
                msg = json.loads(e.read().decode()).get("error", {}).get("message", "")[:160]
            except Exception:
                msg = f"HTTP {e.code}"
            print("diag", perfil, "erro:", msg)
        except Exception as e:
            print("diag", perfil, "erro:", type(e).__name__)


_diagnostico()
