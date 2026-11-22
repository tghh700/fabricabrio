"""Agenda de 23/11: BRIO 86–89 e FIBRA 34–37. BRT -> UTC +3h. formato (jornada / teste:<modelo>) via sql extra."""
import json, re, subprocess
import pauta_2311 as PA

CRED = {g["id"]: g["caracteres"] for g in json.load(open("audio/creditos_2311.json"))["gastos"]}


def utc(hhmm, dia):
    h, m = map(int, hhmm.split(':')); h += 3
    if h >= 24: h -= 24; dia += 1
    return f"2026-11-{dia:02d} {h:02d}:{m:02d}:00"


def dur(path):
    return round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout), 2)


DM = "Aqui está o link do Brio, onde você registra suas séries e acompanha sua evolução de graça: {link}"
vids, cred = [], []
for k, v in PA.P.items():
    vid = k.replace('_', '-'); kw = v['palavra']
    leg = f"{v['leg']}\n📲 Comenta {kw} que eu te mando no direct {v['gat']}.\n\n{v['tags']}"
    assert not re.search(r"br[íi]u", leg, re.I), k
    gancho = re.split(r"(?<=[.?!])\s", re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][-1]))[0]
    vids.append(dict(id=vid, perfil=v['perfil'], tema_canonico=v['tema'], gancho=gancho, gatilho_tipo="2", palavra_chave=kw,
                     arquivo=f"{v['perfil']}/{vid}.mp4", legenda=leg, hashtags=v['tags'], duracao_s=dur(f"out/roteiro_{k}.mp4"),
                     dm_texto=DM, agendado_para=utc(v["hora"], 23)))
    cred.append(dict(video_id=vid, quantidade=CRED[k]))
sqlx = [f"UPDATE videos SET formato='{PA.P[k]['formato'].split(' — ')[0] if PA.P[k]['formato'].startswith('teste:') else ('jornada' if PA.P[k]['perfil']=='brio' else 'fibra-padrao')}' WHERE id='{k.replace('_', '-')}';" for k in PA.P]
json.dump({"nome": "agenda-20261123", "videos": vids, "creditos": cred, "sql": sqlx}, open("../jobs/d1.json", "w"), ensure_ascii=False, indent=1)
for x in vids: print(x['id'], x['agendado_para'], x['duracao_s'], len(x['legenda']), x['gancho'])
