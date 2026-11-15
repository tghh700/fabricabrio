from cenas_1611 import *
import roteiro_brio_59_confunde as R
BEAT_CTA = R.BEATS[-1]
EX = ("SUPINO", "CRUCIFIXO", "FLEXÃO", "CROSSOVER", "PECK DECK")

def hook(c, t, d):
    act_tired(c, t)
    i = int(t * 4) % len(EX)
    card(c, 790, 1150, 440, 150, CARD, back_out(prog(t, 0.05, 0.3)))
    draw_text(c, EX[i], 790, 1175, 70, YEL, "Anton", 1.0, align="center")
    draw_text(c, "SEMANA " + str(i + 1), 790, 1300, 40, GREY, "Space Mono", 1.0, align="center", spacing=2)

def mito(c, t, d):
    act_curl(c, t)
    tag(c, 790, 1120, "SURPREENDER O MÚSCULO", YEL, INK, 46, back_out(prog(t, 0.1, 0.3)))
    icon_x(c, 790, 1340, 1.3, prog(t, 0.6, 0.3))

def sinal(c, t, d):
    act_curl(c, t, heavy=True)
    zigzag(c, t, 580, 1040, 420, 400, (0.2, 0.3, 0.38, 0.45, 0.55, 0.62, 0.72, 0.82), GRN, trend=False, dur=1.4)
    draw_text(c, "CARGA × SEMANAS", 790, 1500, 38, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center", spacing=1)

def perde(c, t, d):
    act_tired(c, t)
    vals = (0.3, 0.25, 0.32, 0.22, 0.3, 0.27)
    bars(c, t, 790, 1460, vals, ("S1", "S2", "S3", "S4", "S5", "S6"), (RED,) * 6, w=56, gap=18, h=380, step=0.15)
    tag(c, 790, 1060, "SEMPRE DO ZERO", RED, WHITE, 52, back_out(prog(t, 1.0, 0.3)))

def quando(c, t, d):
    act_press(c, t)
    vals = (0.3, 0.38, 0.45, 0.52, 0.6, 0.68, 0.76, 0.85)
    bars(c, t, 800, 1460, vals, tuple(f"S{i + 1}" for i in range(8)), (GRN,) * 8, w=44, gap=12, h=420, step=0.1)

def varia(c, t, d):
    act_curl(c, t)
    stack_list(c, t, ("TRAVOU", "DÓI", "ENJOOU DE VERDADE"), 790, 1000, 480, 160, -1, num=False)

VIS = {"hook": scene(hook, "TROCA TODA SEMANA?", RED), "mito": scene(mito, "MITO ANTIGO", RED),
       "sinal": scene(sinal, "O SINAL É A CARGA", GRN), "perde": scene(perde, "TROCOU TUDO? PERDEU A CONTA", RED),
       "quando": scene(quando, "MANTÉM 4 A 8 SEMANAS", GRN), "varia": scene(varia, "TROCA COM MOTIVO", YEL)}
SFX = finish(R, VIS, ("NÃO CONFUNDE", "MESMO EXERCÍCIO", "CARGA SUBINDO"), "TROCA", "SUPINO",
 [("SEMANA 1: 40 KG × 8", WHITE), ("SEMANA 4: 45 KG × 8", WHITE), ("+5 KG EM 4 SEMANAS", None)], ("REGISTRE CADA EXERCÍCIO", "NO BRIO"))
