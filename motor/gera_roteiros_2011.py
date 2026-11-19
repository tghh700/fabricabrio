"""Gera roteiro_<id>.py (BRIO v2 e FIBRA build3) de pauta_2011.py, com o áudio apertado e o início de cada beat."""
import json, re, sys
import pauta_2011 as PA
from apertar import apertar
PRE = {"fibra_22_euforia": "eu_", "fibra_23_folego": "fl_", "fibra_24_cansaco": "ca_", "fibra_25_maos": "ma_"}
import os
out = json.load(open("starts_2011.json")) if os.path.exists("starts_2011.json") else {}
for k, v in PA.P.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
    al = json.load(open(f"audio/{k}.json")); chars = "".join(al["characters"]); st = al["character_start_times_seconds"]
    _, mapa = apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3")
    starts, pos = [], 0
    for vis, t1, t2, text in v['beats']:
        k0 = chars.find(re.sub(r"\[[^\]]*\]", "", text).strip()[:14], pos); k0 = pos if k0 < 0 else k0
        starts.append(round(mapa(st[k0]), 3)); pos = k0 + 1
    if v['perfil'] == 'brio':
        beats = [dict(vis=vis, k='', t1=t1, t2=t2, text=text) for vis, t1, t2, text in v['beats']]
        kc = chars.find('que eu te mando'); kf = chars.find('Link na bio')
        beats[-1]['marks'] = {'ponte': round(mapa(st[kc]) - starts[-1], 3), 'fixa': round(mapa(st[kf]) - starts[-1], 3)}
        src = (f"# {k} — produção 20/11 · {v['tema']}\n# evidência: {v['evid']}\n# fonte: {v['fonte']}\n"
               f"TITLE={v['beats'][0][3]!r}\nVOICE='plASsyS7JE6GCAvx9uIc'\nTHEME='brio'\nBRAND='brio'\nGATILHO_TIPO=2\n"
               f"NARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    else:
        beats = []
        for i, (vis, t1, t2, text) in enumerate(v['beats']):
            bb = dict(vis=PRE[k] + vis, t1=t1, t2=t2, text=text)
            bb['fig'] = f"FIG. {i + 1:02d} — {t1.rstrip(':.,').replace(chr(34), '')}"[:28]
            beats.append(bb)
        src = (f"# {k} — produção 20/11 · {v['tema']}\n# evidência/formato: {v['formato']}\n# fonte: {v['fonte']}\n"
               f"THEME='fibra'\nVOICE=None\nBPM=112\nBED_VOL=0.7\nNARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    open(f"roteiro_{k}.py", "w").write(src); out[k] = starts; print(k, starts)
json.dump(out, open("starts_2011.json", "w"))
