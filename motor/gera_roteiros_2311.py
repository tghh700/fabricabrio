"""Gera roteiro_<id>.py de pauta_2311.py (BRIO jornada no padrão do brio_75; FIBRA build3), com áudio apertado e início de cada beat."""
import json, re, sys, os
import pauta_2311 as PA
from apertar import apertar

PRE = {"fibra_34_joelho": "jo_", "fibra_35_primeiro": "pr_", "fibra_36_falha": "fa_", "fibra_37_segundos": "sg_"}
ANALISE = {
    'brio': "# ANALISE_10: melhores = seis meses 1.580 (wt 12,8 s) · jornada brio-75 1.406 (wt 17,2 s, 18 salvos) · força parou 1.364 (wt 12,6 s);\n"
            "#   piores = flexibilidade 137 (wt 5,2 s) · peito não cresce 146 (wt 5,1 s) · água gelada 231 (wt 6,2 s).\n"
            "#   separa: situação de resultado/tempo que a pessoa vive + história longa seguram 12–17 s; mito pontual e músculo isolado caem em 5–6 s.\n",
    'fibra': "# ANALISE_10: melhores = treino de perna cansa 2.220 (wt 13,7 s, 9 compart.) · veias 871 (wt 8,0 s) · escada 676 (wt 10,5 s);\n"
             "#   piores = formigamento do pré-treino 14 · começo da corrida 53 · sensação boa 115.\n"
             "#   separa: perna/academia e 'por que' de algo que todo mundo sente na série vencem; sensação rara/de corrida/suplemento morre.\n",
}
out = json.load(open("starts_2311.json")) if os.path.exists("starts_2311.json") else {}
for k, v in PA.P.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]:
        continue
    al = json.load(open(f"audio/{k}.json")); chars = "".join(al["characters"]); st = al["character_start_times_seconds"]
    if v["perfil"] == "brio":
        _, mapa = apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3", max_pausa=0.45, tempo=1.0)
    else:
        _, mapa = apertar(f"audio/{k}.mp3", f"audio/{k}_tight.mp3")
    starts, pos = [], 0
    for b in v['beats']:
        text = b[-1]
        k0 = chars.find(re.sub(r"\[[^\]]*\]", "", text).strip()[:14], pos); k0 = pos if k0 < 0 else k0
        starts.append(round(mapa(st[k0]), 3)); pos = k0 + 1
    head = (f"# {k} — produção 23/11 · {v['tema']}\n{ANALISE[v['perfil']]}# modelo: {v['formato']}\n"
            f"# evidência: {v.get('evid') or v['formato']}\n# fonte: {v['fonte']}\n")
    if v['perfil'] == 'brio':
        beats = [dict(vis=vis, k='', t1=t1, t2=t2, text=text) for (vis, t1, t2, text) in v['beats']]
        kc = chars.find('que eu te mando'); kf = chars.find('Link na bio')
        beats[-1]['marks'] = {'ponte': round(mapa(st[kc]) - starts[-1], 3), 'fixa': round(mapa(st[kf]) - starts[-1], 3)}
        src = (head + f"TITLE={v['beats'][0][3]!r}\nVOICE='plASsyS7JE6GCAvx9uIc'\nTHEME='brio'\nBRAND='brio'\nGATILHO_TIPO=2\n"
               f"NARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    else:
        beats = []
        for i, (vis, t1, t2, text) in enumerate(v['beats']):
            bb = dict(vis=PRE[k] + vis, t1=t1, t2=t2, text=text)
            bb['fig'] = f"FIG. {i + 1:02d} — {t1.rstrip(':.,')}"[:28]
            beats.append(bb)
        src = head + (f"THEME='fibra'\nVOICE=None\nBPM=112\nBED_VOL=0.7\nNARRATION={{'file':'audio/{k}_tight.mp3','starts':{starts}}}\nBEATS={beats!r}\n")
    open(f"roteiro_{k}.py", "w").write(src); out[k] = starts
    from tts import duration
    print(k, round(duration(f"audio/{k}_tight.mp3"), 1), starts)
json.dump(out, open("starts_2311.json", "w"))
