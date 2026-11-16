from cenas_1711 import *
import roteiro_brio_65_genetica as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0))
        bicep_glow(c, t, cx - 40, by - 300, prog(t, 0.9, 0.3))
    split(c, t, L, Rr, "VOCÊ", "SEU AMIGO", GREY, YEL)

def estudo(c, t, d):
    act_curl(c, t)
    counter(c, t, 790, 1080, 0, 585, "{:.0f}", 190, YEL)
    draw_text(c, "PESSOAS", 790, 1230, 44, GREY, "Space Mono", prog(t, 0.5, 0.3), align="center", spacing=3)
    tag(c, 790, 1400, "MESMO TREINO DE BRAÇO", BLU, INK, 42, back_out(prog(t, 0.9, 0.3)))

def variou(c, t, d):
    act_curl(c, t, spd=2.0)
    vals = (0.04, 0.2, 0.38, 0.6, 1.0)
    bars(c, t, 790, 1470, vals, ("", "", "", "", ""), (RED, YEL, YEL, GRN, GRN), w=70, gap=24, h=420, step=0.18)
    draw_text(c, "0%", 790 - 2 * 94, 1540, 56, RED, "Anton", prog(t, 0.6, 0.3), align="center")
    draw_text(c, "+59%", 790 + 2 * 94, 1540, 56, GRN, "Anton", prog(t, 1.0, 0.3), align="center")

def gen(c, t, d):
    act_pose(c, t, "shrug")
    for k in range(10):  # dupla hélice desenhada
        y = 1000 + k * 48; ph = t * 2.5 + k * 0.6
        x1 = 790 + 110 * math.sin(ph); x2 = 790 - 110 * math.sin(ph)
        cap_line(c, x1, y, x2, y, GREY, 5, 0.6 * prog(t, k * 0.05, 0.2))
        disk(c, x1, y, 16, BLU, prog(t, k * 0.05, 0.2)); disk(c, x2, y, 16, YEL, prog(t, k * 0.05, 0.2))

def mais(c, t, d):
    act_curl(c, t, spd=3.0)
    stack_list(c, t, ("MAIS SÉRIES", "MAIS TEMPO"), 790, 1080, 480, 170, int(t * 1.3) % 2)

def compara(c, t, d):
    act_curl(c, t, heavy=True)
    zigzag(c, t, 580, 1020, 420, 360, (0.2, 0.3, 0.28, 0.45, 0.5, 0.62, 0.7), GRN, trend=True)
    draw_text(c, "VOCÊ × VOCÊ", 790, 1500, 56, YEL, "Anton", back_out(prog(t, 0.8, 0.3)), align="center")

VIS = {"hook": scene(hook, "MESMO TREINO?", YEL, bg=False), "estudo": scene(estudo, "585 PESSOAS", YEL),
       "variou": scene(variou, "DE 0% A 59%", GRN), "gen": scene(gen, "GENÉTICA PESA", YEL),
       "mais": scene(mais, "QUEM RESPONDE POUCO", GRN), "compara": scene(compara, "COMPARA COM VOCÊ", GRN)}
SFX = finish(R, VIS, ("CADA CORPO, UM RITMO", "MAIS SÉRIES AJUDAM", "VOCÊ × VOCÊ"), "GENÉTICA", "SUA EVOLUÇÃO",
 [("JAN: ROSCA 10 KG", WHITE), ("MAR: ROSCA 14 KG", WHITE), ("+4 KG: É VOCÊ", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
