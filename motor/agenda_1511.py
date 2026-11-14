"""Monta jobs/d1.json com a agenda BRIO de 15/11 (horários BRT -> UTC +3h). Uso: python3 agenda_1511.py <ids aprovados...>"""
import json, sys, re, subprocess
import pauta_1511 as PA

LEG = {
 'brio_39_descida': ("Deixar o peso cair joga fora metade da repetição. 👇\nSobe firme, desce em 2 segundos, sempre controlado. Sem controle? O peso está alto demais.",
                     "#brio #musculacao #tecnica #academia #hipertrofia"),
 'brio_40_maquina': ("Máquina dá músculo, sim. 👇\nUma revisão de 2023 comparou máquina e peso livre: o ganho de músculo foi parecido. Usa os dois e faz a carga subir.",
                     "#brio #musculacao #academia #hipertrofia #treino"),
 'brio_41_dropset': ("Drop set economiza tempo de treino. 👇\nAté perto da falha, tira peso e continua. Funciona melhor na última série, em máquina ou isolado.",
                     "#brio #dropset #musculacao #academia #hipertrofia"),
 'brio_42_biset': ("Dá pra treinar o mesmo em menos tempo. 👇\nBi-set: dois exercícios seguidos de músculos que não competem, e só depois o descanso.",
                   "#brio #biset #treinorapido #musculacao #academia"),
 'brio_43_lado': ("Um braço mais forte que o outro? É normal. 👇\nExercício de um lado só, começando pelo lado fraco, e o forte faz as mesmas repetições.",
                  "#brio #musculacao #unilateral #academia #treino"),
 'brio_44_menos': ("Cinco exercícios de bíceps no mesmo treino é exagero. 👇\nDepois de algumas séries duras, cada série a mais rende menos. O resto vai pra outro dia.",
                   "#brio #biceps #musculacao #academia #hipertrofia"),
 'brio_45_barra': ("Não consegue fazer nem uma barra? 👇\nComeça pela negativa: sobe com um banco e desce em 5 segundos. A primeira barra vem.",
                   "#brio #barrafixa #calistenia #academia #treino"),
 'brio_46_musica': ("Treinar com fone te deixa mais forte? 👇\nMais de 100 estudos: a música melhora o desempenho e o esforço parece menor. Mas quem faz o resultado é a carga.",
                    "#brio #musica #treino #academia #musculacao"),
 'brio_47_oscila': ("Um treino fraco não é regressão. 👇\nA força varia de um dia pro outro. Compara as últimas 4 semanas com as 4 anteriores.",
                    "#brio #evolucao #musculacao #academia #treino"),
 'brio_48_cinto': ("Cinto na academia: precisa? 👇\nSó na série pesada de agachamento e terra. Primeiro aprende a travar o abdômen sem ele.",
                   "#brio #cinto #agachamento #musculacao #academia"),
 'brio_49_pegada': ("Sua mão cansa antes das costas? 👇\nNa remada e no terra pesado, o strap segura a barra e as costas trabalham até o fim.",
                    "#brio #costas #remada #musculacao #academia"),
 'brio_50_puxar': ("Muito supino e pouca remada é erro. 👇\nPra cada série de empurrar, uma de puxar: supino com remada, desenvolvimento com puxada.",
                   "#brio #costas #supino #musculacao #academia"),
}
GATILHO = {  # linha do gatilho (escrita: Brio)
 'brio_39_descida': "como registrar suas séries no Brio e ver a carga subir",
 'brio_40_maquina': "como registrar a carga de cada aparelho no Brio",
 'brio_41_dropset': "como registrar cada etapa do seu drop set no Brio",
 'brio_42_biset': "como registrar seus pares de exercício no Brio, série por série",
 'brio_43_lado': "como registrar as repetições de cada lado no Brio",
 'brio_44_menos': "como registrar suas séries no Brio e acompanhar sua evolução",
 'brio_45_barra': "como registrar suas descidas no Brio até a primeira barra",
 'brio_46_musica': "como registrar suas séries no Brio e ver se a carga está subindo",
 'brio_47_oscila': "como acompanhar sua evolução no Brio, semana a semana",
 'brio_48_cinto': "como registrar suas séries pesadas no Brio",
 'brio_49_pegada': "como registrar sua remada no Brio e ver a carga subir",
 'brio_50_puxar': "como registrar suas séries no Brio e conferir se empurrar e puxar estão empatados",
}
CRED = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and sys.argv[1].endswith('.json') else {}


def utc(hhmm):
    h, m = map(int, hhmm.split(':')); h += 3
    d = 15
    if h >= 24: h -= 24; d = 16
    return f"2026-11-{d:02d} {h:02d}:{m:02d}:00"


def dur(path):
    return round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout), 2)


ids = [a for a in sys.argv[1:] if not a.endswith('.json')]
vids, cred = [], []
for k in ids:
    v = PA.P[k]; vid = k.replace('_', '-')
    g, tags = LEG[k]
    kw = v['palavra']
    leg = f"{g}\n📲 Comenta {kw} que eu te mando no direct {GATILHO[k]}.\n\n{tags}"
    assert not re.search(r"br[íi]u", leg, re.I), k
    gancho = re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][3])
    vids.append(dict(id=vid, perfil='brio', tema_canonico=v['tema'], gancho=gancho, gatilho_tipo=str(v['gat']), palavra_chave=kw,
                     arquivo=f"brio/{vid}.mp4", legenda=leg, hashtags=tags, duracao_s=dur(f"out/roteiro_{k}.mp4"),
                     dm_texto="Aqui está o link do Brio, onde você registra suas séries e acompanha sua evolução de graça: {link}",
                     agendado_para=utc(v['hora'])))
    cred.append(dict(video_id=vid, quantidade=CRED.get(k, 0)))
json.dump({"nome": "agenda-20261115-brio", "videos": vids, "creditos": cred}, open("../jobs/d1.json", "w"), ensure_ascii=False, indent=1)
print(len(vids), "vídeos na agenda")
