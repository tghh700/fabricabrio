"""Gera roteiro_<id>.py (FIBRA) de pauta_1811.py, com o áudio apertado e o início de cada beat."""
import json, re, sys
import pauta_1811 as PA
from apertar import apertar
from scenes_fibra_1811 import PRE
out = {}
for k, v in PA.P.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
    al = json.load(open(f"audio/{k}.json")); chars = "".join(al["characters"]); st = al["character_start_times_seconds"]
    _, mapa = apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3")
    starts, pos = [], 0
    for vis, t1, t2, text in v['beats']:
        k0 = chars.find(re.sub(r"\[[^\]]*\]", "", text).strip()[:14], pos); k0 = pos if k0 < 0 else k0
        starts.append(round(mapa(st[k0]), 3)); pos = k0 + 1
    beats = []
    for i, (vis, t1, t2, text) in enumerate(v['beats']):
        bb = dict(vis=PRE[k] + vis, t1=t1, t2=t2, text=text)
        bb['fig'] = f"FIG. {i + 1:02d} — {t1.rstrip(':.,').replace(chr(34), '')}"[:28]
        beats.append(bb)
    src = (f"# {k} — produção 18/11 · {v['tema']}\n# formato: {v['formato']}\n# fonte: {v['fonte']}\n"
           f"THEME='fibra'\nVOICE=None\nBPM=112\nBED_VOL=0.7\nNARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    open(f"roteiro_{k}.py", "w").write(src); out[k] = starts; print(k, starts)
json.dump(out, open("starts_1811.json", "w"))
