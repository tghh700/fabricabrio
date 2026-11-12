"""Narração via ElevenLabs com cache: cada trecho é gerado uma única vez (economia de créditos)."""
import hashlib, json, os, subprocess, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "audio_cache")
VOICE = "wHnxjlY53t8X9Oi14Awz"   # Juliano Magalhães (PT-BR, narrativa)
MODEL = "eleven_multilingual_v2"
SETTINGS = {"stability": 0.45, "similarity_boost": 0.8, "style": 0.15, "use_speaker_boost": True, "speed": 1.05}

def keys():
    """chaves do ElevenLabs: .xi_keys (uma por linha, em ordem de uso) ou .xi_key"""
    p = os.path.join(HERE, ".xi_keys")
    if os.path.exists(p):
        ks = [l.strip() for l in open(p) if l.strip() and not l.startswith("#")]
        if ks: return ks
    return [open(os.path.join(HERE, ".xi_key")).read().strip()]

def key():
    return keys()[0]

def _post(url, body):
    """tenta cada chave; pula para a próxima quando a chave não tem crédito ou é inválida"""
    import urllib.error
    last = None
    for k in keys():
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"xi-api-key": k, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="ignore")[:300]; last = f"{e.code} {msg}"
            if e.code in (401, 402, 403, 429) or "quota" in msg.lower() or "credit" in msg.lower():
                print("chave sem crédito/permissão, tentando a próxima:", e.code, flush=True); continue
            raise
    raise RuntimeError("nenhuma chave do ElevenLabs funcionou: " + str(last))

def path_for(text, voice=VOICE, settings=None):
    settings = settings or SETTINGS
    h = hashlib.sha1(json.dumps([text, voice, MODEL, settings]).encode()).hexdigest()[:16]
    return os.path.join(CACHE, h + ".mp3")

def tts(text, prev="", nxt="", voice=VOICE, settings=None):
    settings = settings or SETTINGS
    os.makedirs(CACHE, exist_ok=True)
    p = path_for(text, voice, settings)
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        return p, False
    body = {"text": text, "model_id": MODEL, "voice_settings": settings}
    if prev: body["previous_text"] = prev
    if nxt: body["next_text"] = nxt
    data = _post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128", body)
    open(p, "wb").write(data)
    return p, True

def duration(p):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p])
    return float(out.strip())

if __name__ == "__main__":
    import importlib
    mod = importlib.import_module(sys.argv[1])
    beats = mod.BEATS
    only = int(sys.argv[2]) if len(sys.argv) > 2 else len(beats)
    spent = 0
    for i, b in enumerate(beats[:only]):
        prev = beats[i - 1]["text"] if i > 0 else ""
        nxt = beats[i + 1]["text"] if i + 1 < len(beats) else ""
        p, new = tts(b["text"], prev, nxt, getattr(mod, "VOICE", VOICE), getattr(mod, "SETTINGS", None))
        if new: spent += len(b["text"])
        print(i, round(duration(p), 2), "NOVO" if new else "cache", b["text"][:50])
    print("caracteres gastos agora:", spent)

def full(mod):
    """Gera o roteiro inteiro numa chamada só (ritmo contínuo) e devolve (audio, inícios de cada beat em s, duração)."""
    import base64
    voice = getattr(mod, "VOICE", VOICE); settings = getattr(mod, "SETTINGS", None) or SETTINGS
    texts = [b["text"].strip() for b in mod.BEATS]
    full_text = " ".join(texts)
    os.makedirs(CACHE, exist_ok=True)
    h = hashlib.sha1(json.dumps([full_text, voice, MODEL, settings, "full"]).encode()).hexdigest()[:16]
    mp3 = os.path.join(CACHE, h + "_full.mp3"); js = os.path.join(CACHE, h + "_full.json")
    if not (os.path.exists(mp3) and os.path.exists(js)):
        body = {"text": full_text, "model_id": MODEL, "voice_settings": settings}
        d = json.loads(_post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128", body))
        open(mp3, "wb").write(base64.b64decode(d["audio_base64"]))
        json.dump(d["alignment"], open(js, "w"))
        print("caracteres gastos agora:", len(full_text))
    al = json.load(open(js))
    st = al["character_start_times_seconds"]
    starts = []; pos = 0
    for tx in texts:
        starts.append(st[min(pos, len(st) - 1)]); pos += len(tx) + 1
    return mp3, starts, duration(mp3)
