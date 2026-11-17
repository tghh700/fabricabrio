"""Agenda de 18/11 (BRIO 4 do estoque pausado + FIBRA 4 novos) e adiantamento de 19/11 (BRIO 4 do estoque). BRT -> UTC +3h."""
import json, re, subprocess
import pauta_1811 as PA

CRED = json.load(open("audio/creditos_1811.json"))
CRED = {g["id"]: g["caracteres"] for g in CRED["gastos"]}


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
                     dm_texto=DM, agendado_para=utc(v['hora'], 18)))
    cred.append(dict(video_id=vid, quantidade=CRED[k]))
# estoque pausado do BRIO (post id -> horário): reativa o mesmo post com novo horário
ESTOQUE = [(61, 'brio-55-altura', '11:30', 18), (68, 'brio-62-rapido', '14:00', 18), (42, 'brio-37-semana', '18:00', 18), (59, 'brio-53-pesado', '21:00', 18),
           (65, 'brio-59-confunde', '11:30', 19), (62, 'brio-56-junto', '14:00', 19), (41, 'brio-36-horario', '18:00', 19), (53, 'brio-47-oscila', '21:00', 19)]
sql = [f"UPDATE posts SET status='agendado', agendado_para='{utc(h, d)}', erro=NULL WHERE id={i} AND video_id='{v}' AND status='pausado';" for i, v, h, d in ESTOQUE]
json.dump({"nome": "agenda-20261118", "videos": vids, "creditos": cred, "sql": sql}, open("../jobs/d1.json", "w"), ensure_ascii=False, indent=1)
print(len(vids), "novos +", len(sql), "do estoque")
