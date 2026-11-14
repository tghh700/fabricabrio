from cenas_1511 import *
import roteiro_brio_42_biset as R
BEAT_CTA = R.BEATS[-1]

def alt(c, t, x=HX, s=0.95, per=2.4):
    """mesma pessoa alternando os dois exercícios do bi-set"""
    if (t % (2 * per)) < per:
        act_curl(c, t, x, s, 2.8)
        return "ROSCA"
    act_press(c, t, x + 20, s * 0.82, 2.6)
    return "DESENVOLVIMENTO"

def hook(c, t, d):
    act_walk(c, t, HX, 0.95)
    clock(c, 780, 1150, 160, t, 3.0)
    p = ease_out(prog(t, 0.3, 1.2))
    rrect(c, 560, 1400, 440, 60, 20, CARD); rrect(c, 560, 1400, 440 * lerp(1, 0.55, p), 60, 20, GRN)
    draw_text(c, "MENOS MINUTOS", 780, 1540, 52, GRN, "Anton", back_out(prog(t, 1.0, 0.3)), align="center")

def oque(c, t, d):
    nm = alt(c, t, per=d / 2)
    for i, txt in enumerate(("1. ROSCA", "2. DESENVOLVIMENTO", "DEPOIS: DESCANSO")):
        p = back_out(prog(t, 0.2 + i * 0.35, 0.3))
        hot = (i == 0 and nm == "ROSCA") or (i == 1 and nm != "ROSCA")
        card(c, 780, 1000 + i * 170, 480, 130, YEL if hot else CARD, p)
        draw_text(c, txt, 780, 1000 + i * 170 + 20, 44, INK if hot else WHITE, "Anton", p, align="center")

def par(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_press(c, t, x + 15, 0.72))
    split(c, t, L, Rr, "PUXA", "EMPURRA", BLU, YEL)

def descansa(c, t, d):
    nm = alt(c, t, per=d / 2)
    a = nm == "ROSCA"
    battery(c, 690, 1150, 0.4 + 0.3 * math.sin(t * 2) if a else 0.95, "BÍCEPS", 140, 260)
    battery(c, 900, 1150, 0.95 if a else 0.4 + 0.3 * math.sin(t * 2), "OMBRO", 140, 260)

def tempo(c, t, d):
    p = ease_out(prog(t, 0.3, 1.2))
    for i, (lab, w, col) in enumerate((("NORMAL", 1.0, BLU), ("BI-SET", 0.62, GRN))):
        y = 1020 + i * 260
        draw_text(c, lab, 140, y - 30, 48, GREY, "Anton", 1.0)
        rrect(c, 140, y, 800 * w * p, 90, 24, col)
        draw_text(c, "8 SÉRIES", 170, y + 66, 46, INK, "Anton", prog(t, 1.2, 0.3))
    clock(c, 540, 1560, 100, t, 2.0)

def evita(c, t, d):
    act_squat(c, t, HX, 0.95, 2.4)
    stack_list(c, t, ("AGACHAMENTO", "+ LEG PRESS"), 790, 1050, 440, 170, -1, num=False)
    icon_x(c, 790, 1450, 0.9, prog(t, 1.0, 0.3))

VIS = {"hook": scene(hook, "TREINO MAIS CURTO", GRN), "oque": scene(oque, "BI-SET", YEL),
       "par": scene(par, "MÚSCULOS QUE NÃO COMPETEM", YEL, bg=False), "descansa": scene(descansa, "UM DESCANSA", GRN),
       "tempo": scene(tempo, "MESMAS SÉRIES", GRN, bg=False), "evita": scene(evita, "2 PESADOS DE PERNA: NÃO", RED)}
SFX = finish(R, VIS, ("PARES QUE NÃO COMPETEM", "MESMAS SÉRIES", "MENOS ESPERA"), "BISET", "BI-SET",
 [("ROSCA 12 KG × 10", WHITE), ("DESENV. 20 KG × 10", WHITE), ("3 RODADAS", None)], ("REGISTRE SEUS PARES", "NO BRIO"))
