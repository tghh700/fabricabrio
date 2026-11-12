"""Gera roteiro_<id>.py a partir de pauta_1311.py. Uso: python3 gera_roteiros_1311.py [starts.json]"""
import json, os, sys
import pauta_1311 as PA
PRE = {'fibra_07_gordura': 'g_', 'fibra_08_barra': 'b_', 'fibra_09_enjoo': 'e_', 'diaum_06_prancha': 'pr_', 'diaum_04_aparelhos': 'ap_',
       'diaum_07_preguica': 'pg_', 'diaum_05_magro': 'mg_', 'diaum_08_semana2': 's2_', 'brio_27_rosca': ''}
starts = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else {}
for k, v in PA.P.items():
    if v['perfil'] == 'brio':
        continue
    beats = []
    for i, (vis, t1, t2, text) in enumerate(v['beats']):
        bb = dict(vis=PRE[k] + vis, t1=t1, t2=t2, text=text)
        if v['perfil'] == 'fibra':
            bb['fig'] = f"FIG. {i + 1:02d} — {t1.rstrip(':.').replace('\"', '')}"[:28]
        beats.append(bb)
    nar = f"NARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts[k]}}}\n" if k in starts else ""
    src = (f"# {k} — produção 13/11 · {v['tema']}\n# formato: {v['formato']}\n" + (f"# fonte: {v['fonte']}\n" if v.get('fonte') else "") +
           f"THEME='{v['perfil']}'\nVOICE=None\nBPM=112\nBED_VOL=0.7\n{nar}BEATS={beats!r}\n")
    open(f"roteiro_{k}.py", "w").write(src)
print("ok")
