"""Executa um pedido ao ElevenLabs descrito em jobs/eleven.json, sem nunca imprimir as chaves.

Operações (lista "ops"):
  {"op": "search_shared", "id": "...", "params": {...}}            -> saida/<id>.json  (grátis)
  {"op": "add_shared", "public_user_id": "...", "voice_id": "...", "name": "..."}
  {"op": "list_voices", "id": "..."}                                -> saida/<id>.json
  {"op": "tts", "id": "...", "voice_id": "...", "model_id": "eleven_v4",
   "text": "...", "voice_settings": {...}, "timestamps": true}     -> saida/<id>.mp3 (+ .json com alinhamento)
As chaves vêm de ELEVENLABS_API_KEY, ELEVENLABS_API_KEY_2, ELEVENLABS_API_KEY_3 (nessa ordem);
quando uma fica sem crédito, passa para a próxima.
Grava saida/creditos.json com os caracteres gastos por item.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.elevenlabs.io"
KEYS = [os.environ.get(k, "").strip() for k in ("ELEVENLABS_API_KEY", "ELEVENLABS_API_KEY_2", "ELEVENLABS_API_KEY_3")]
KEYS = [k for k in KEYS if k]
OUT = "saida"


def limpa(s):
    for k in KEYS:
        s = s.replace(k, "***")
    return s


def call(method, path, body=None, params=None):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    last = None
    for i, k in enumerate(KEYS):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method,
                                     headers={"xi-api-key": k, "Content-Type": "application/json", "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read(), i + 1
        except urllib.error.HTTPError as e:
            msg = limpa(e.read().decode(errors="ignore")[:400])
            last = f"{e.code} {msg}"
            low = msg.lower()
            if (e.code in (401, 402, 403, 429) or "quota" in low or "credit" in low
                    or "invalid_api_key" in low or "authentication_error" in low):
                print(f"chave {i + 1}: sem crédito/permissão ({e.code}), tentando a próxima", flush=True)
                continue
            raise RuntimeError(last)
    raise RuntimeError("nenhuma chave funcionou: " + str(last))


def main():
    job = json.load(open("jobs/eleven.json"))
    os.makedirs(OUT, exist_ok=True)
    gastos, erros = [], []
    for op in job.get("ops", []):
        try:
            if op["op"] == "search_shared":
                raw, _ = call("GET", "/v1/shared-voices", params=op.get("params", {}))
                d = json.loads(raw)
                slim = [{k: v.get(k) for k in ("voice_id", "public_owner_id", "name", "accent", "gender", "age",
                                                  "descriptive", "use_case", "language", "description", "preview_url",
                                                  "cloned_by_count", "usage_character_count_1y", "category")}
                        for v in d.get("voices", [])]
                json.dump(slim, open(f"{OUT}/{op['id']}.json", "w"), ensure_ascii=False, indent=1)
                print(op["id"], "vozes:", len(slim))
            elif op["op"] == "add_shared":
                raw, _ = call("POST", f"/v1/voices/add/{op['public_user_id']}/{op['voice_id']}", {"new_name": op["name"]})
                print("adicionada:", op["name"], raw.decode(errors="ignore")[:120])
            elif op["op"] == "list_voices":
                raw, _ = call("GET", "/v1/voices")
                d = json.loads(raw)
                slim = [{"voice_id": v["voice_id"], "name": v["name"], "category": v.get("category")} for v in d.get("voices", [])]
                json.dump(slim, open(f"{OUT}/{op['id']}.json", "w"), ensure_ascii=False, indent=1)
                print("minhas vozes:", len(slim))
            elif op["op"] == "tts":
                body = {"text": op["text"], "model_id": op.get("model_id", "eleven_v4")}
                if op.get("voice_settings"):
                    body["voice_settings"] = op["voice_settings"]
                if op.get("seed") is not None:
                    body["seed"] = op["seed"]
                if op.get("timestamps"):
                    raw, kidx = call("POST", f"/v1/text-to-speech/{op['voice_id']}/with-timestamps", body,
                                     params={"output_format": "mp3_44100_128"})
                    d = json.loads(raw)
                    open(f"{OUT}/{op['id']}.mp3", "wb").write(base64.b64decode(d["audio_base64"]))
                    json.dump(d.get("alignment"), open(f"{OUT}/{op['id']}.json", "w"))
                else:
                    raw, kidx = call("POST", f"/v1/text-to-speech/{op['voice_id']}", body,
                                     params={"output_format": "mp3_44100_128"})
                    open(f"{OUT}/{op['id']}.mp3", "wb").write(raw)
                gastos.append({"id": op["id"], "caracteres": len(op["text"]), "chave": kidx, "modelo": body["model_id"]})
                print("tts ok:", op["id"], len(op["text"]), "caracteres, chave", kidx)
        except Exception as e:  # registra e segue para o próximo item
            erros.append({"op": op.get("op"), "id": op.get("id") or op.get("name"), "erro": limpa(str(e))[:400]})
            print("ERRO", op.get("id") or op.get("name"), limpa(str(e))[:300])
    json.dump({"gastos": gastos, "erros": erros, "total": sum(g["caracteres"] for g in gastos)},
              open(f"{OUT}/creditos.json", "w"), ensure_ascii=False, indent=1)
    print("caracteres gastos:", sum(g["caracteres"] for g in gastos), "| erros:", len(erros))


if __name__ == "__main__":
    if not KEYS:
        print("nenhuma chave do ElevenLabs configurada")
        sys.exit(1)
    main()
