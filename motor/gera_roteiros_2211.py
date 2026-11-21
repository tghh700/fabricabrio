"""Gera roteiro_<id>.py (BRIO cadeia com WORDS e FIBRA build3) de pauta_2211.py, com o áudio apertado e o início de cada beat."""
import json, re, sys, os
import pauta_2211 as PA
from apertar import apertar
from cenas_2211 import words_from_alignment
PRE = {"fibra_30_barra": "ba_", "fibra_31_alonga": "al_", "fibra_32_legpress": "lp_", "fibra_33_descida": "de_"}
out = json.load(open("starts_2211.json")) if os.path.exists("starts_2211.json") else {}
for k, v in PA.P.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
    al = json.load(open(f"audio/{k}.json")); chars = "".join(al["characters"]); st = al["character_start_times_seconds"]
    _, mapa = (apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3", max_pausa=0.34, tempo=1.0) if v["perfil"] == "brio" else apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3"))
    starts, pos = [], 0
    for b in v['beats']:
        text = b[-1]
        k0 = chars.find(re.sub(r"\[[^\]]*\]", "", text).strip()[:14], pos); k0 = pos if k0 < 0 else k0
        starts.append(round(mapa(st[k0]), 3)); pos = k0 + 1
    if v['perfil'] == 'brio':
        beats = []
        for i, (vis, kw, text) in enumerate(v['beats']):
            t1, t2 = (v['titulo'] if vis == 'e1' else ('', ''))
            if vis == 'cta': t1, t2 = 'COMENTA', v['palavra'] + '.'
            beats.append(dict(vis=vis, k=kw, t1=t1, t2=t2, text=text))
        kc = chars.find('que eu te mando'); kf = chars.find('Link na bio')
        beats[-1]['marks'] = {'ponte': round(mapa(st[kc]) - starts[-1], 3), 'fixa': round(mapa(st[kf]) - starts[-1], 3)}
        words = words_from_alignment(al, mapa)
        src = (f"# {k} — produção 22/11 · {v['tema']}\n# evidência: {v['evid']}\n# fonte: {v['fonte']}\n"
               f"TITLE={v['beats'][0][2]!r}\nVOICE='plASsyS7JE6GCAvx9uIc'\nTHEME='brio'\nBRAND='brio'\nGATILHO_TIPO=2\n"
               f"NARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\nWORDS={words!r}\n")
    else:
        beats = []
        for i, (vis, t1, t2, text) in enumerate(v['beats']):
            bb = dict(vis=PRE[k] + vis, t1=t1, t2=t2, text=text)
            bb['fig'] = f"FIG. {i + 1:02d} — {t1.rstrip(':.,').replace(chr(34), '')}"[:28]
            beats.append(bb)
        src = (f"# {k} — produção 22/11 · {v['tema']}\n# evidência/formato: {v['formato']}\n# fonte: {v['fonte']}\n"
               f"THEME='fibra'\nVOICE=None\nBPM=112\nBED_VOL=0.7\nNARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    open(f"roteiro_{k}.py", "w").write(src); out[k] = starts; print(k, starts)
json.dump(out, open("starts_2211.json", "w"))
