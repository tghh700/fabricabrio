import json, re, os
import pauta_1411 as PA
from apertar import apertar
out = {}
import sys
for k, v in PA.P.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]: continue
    al = json.load(open(f"audio/{k}.json")); chars = "".join(al["characters"]); st = al["character_start_times_seconds"]
    _, mapa = apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3")
    starts, pos = [], 0
    for vis, t1, t2, text in v['beats']:
        k0 = chars.find(re.sub(r"\[[^\]]*\]", "", text).strip()[:14], pos); k0 = pos if k0 < 0 else k0
        starts.append(round(mapa(st[k0]), 3)); pos = k0 + 1
    beats = [dict(vis=vis, k='', t1=t1, t2=t2, text=text) for vis, t1, t2, text in v['beats']]
    kc = chars.find('que eu te mando'); kf = chars.find('Link na bio')
    base = starts[-1]
    beats[-1]['marks'] = {'ponte': round(mapa(st[kc]) - base, 3), 'fixa': round(mapa(st[kf]) - base, 3)}
    src = (f"# {k} — extra 14/11 · {v['tema']}\nTITLE={v['beats'][0][3]!r}\nVOICE='plASsyS7JE6GCAvx9uIc'\nTHEME='brio'\nBRAND='brio'\nGATILHO_TIPO={v['gat']}\n"
           f"NARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    open(f"roteiro_{k}.py", "w").write(src); out[k] = starts; print(k, starts)
_o = json.load(open("starts_1411.json")); _o.update(out); json.dump(_o, open("starts_1411.json", "w"))
