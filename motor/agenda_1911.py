"""Agenda de 19/11: FIBRA 18–21 (novos). BRIO 19/11 já agendado do estoque (59, 56, 36, 47). BRT -> UTC +3h."""
import json, re, subprocess
import pauta_1911 as PA

CRED = {g["id"]: g["caracteres"] for g in json.load(open("audio/creditos_1911.json"))["gastos"]}


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
    gancho = re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][3])
    vids.append(dict(id=vid, perfil=v['perfil'], tema_canonico=v['tema'], gancho=gancho, gatilho_tipo="2", palavra_chave=kw,
                     arquivo=f"{v['perfil']}/{vid}.mp4", legenda=leg, hashtags=v['tags'], duracao_s=dur(f"out/roteiro_{k}.mp4"),
                     dm_texto=DM, agendado_para=utc(v['hora'], 19)))
    cred.append(dict(video_id=vid, quantidade=CRED[k]))
json.dump({"nome": "agenda-20261119", "videos": vids, "creditos": cred}, open("../jobs/d1.json", "w"), ensure_ascii=False, indent=1)
for x in vids: print(x['id'], x['agendado_para'], x['duracao_s'], len(x['legenda']))
