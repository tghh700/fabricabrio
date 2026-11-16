from cenas_1711 import *
import roteiro_brio_70_bcaa as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    pill(c, 760, 1150, 1.4, back_out(prog(t, 0.05, 0.3)), YEL)
    coin_stack(c, t, 940, 1450, 1 + int(clamp(prog(t, 0.3, d * 0.6)) * 5.99))
    draw_text(c, "BCAA", 760, 1380, 70, YEL, "Anton", back_out(prog(t, 0.3, 0.3)), align="center")

def oque(c, t, d):
    act_curl(c, t, spd=2.0)
    draw_text(c, "BCAA: 3", 790, 1050, 70, YEL, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    amino_chain(c, t, 790, 1150, 3, 9, 52, prog(t, 0.1, 1.0))
    draw_text(c, "O MÚSCULO PRECISA: 9", 790, 1330, 48, WHITE, "Anton", back_out(prog(t, 0.6, 0.3)), align="center")
    amino_chain(c, t, 790, 1430, 9, 9, 52, prog(t, 0.7, 1.0))

def falta(c, t, d):
    act_tired(c, t)
    amino_chain(c, t, 790, 1200, 3, 9, 60)
    q = prog(t, 0.5, 0.3)
    if q > 0:
        x_mark(c, 790 + 60 * 1.5, 1200, 0.9, q, RED)
    tag(c, 790, 1400, "FALTAM 6 PEÇAS", RED, WHITE, 46, back_out(prog(t, 0.8, 0.3)))

def comida(c, t, d):
    act_walk(c, t, spd=4.0)
    for i, (fn, lab) in enumerate(((chicken, "FRANGO"), (egg, "OVO"), (shaker, "WHEY"))):
        x = 590 + i * 200
        p = back_out(prog(t, 0.1 + i * 0.3, 0.3))
        if fn is shaker:
            fn(c, x, 1150, 0.6, p)
        else:
            fn(c, x, 1150, 0.65, p)
        draw_text(c, lab, x, 1340, 48, YEL, "Anton", p, align="center")
    tag(c, 790, 1470, "JÁ TÊM BCAA", GRN, INK, 46, back_out(prog(t, 1.0, 0.3)))

def quem(c, t, d):
    def L(c, t, cx, by):
        muscle_fiber(c, t, cx, by - 250, 280, 100, 1.0)
        draw_text(c, "PROTEÍNA", cx, by - 400, 60, GRN, "Anton", 1.0, align="center")
    def Rr(c, t, cx, by):
        muscle_fiber(c, t, cx, by - 250, 280, 100, 1.0)
        draw_text(c, "+ BCAA", cx, by - 400, 60, YEL, "Anton", 1.0, align="center")
        draw_text(c, "= IGUAL", cx, by - 90, 60, WHITE, "Anton", prog(t, 1.3, 0.3), align="center")
    split(c, t, L, Rr, "SÓ COMIDA", "COM BCAA", GRN, YEL)

def troca(c, t, d):
    act_walk(c, t, spd=4.0)
    coin_stack(c, t, 640, 1450, 5)
    arrow(c, 720, 1300, 840, 1300, YEL, 14, ease_out(prog(t, 0.3, 0.3)))
    plate_food(c, 920, 1300, 0.85, back_out(prog(t, 0.6, 0.3)))

VIS = {"hook": scene(hook, "VALE O DINHEIRO?", YEL), "oque": scene(oque, "SÓ 3 DE 9", YEL),
       "falta": scene(falta, "A OBRA PARA", RED), "comida": scene(comida, "A COMIDA JÁ TEM", GRN),
       "quem": scene(quem, "NÃO SOMA NADA", RED, bg=False), "troca": scene(troca, "GASTA NA COMIDA", GRN)}
SFX = finish(R, VIS, ("BCAA = 3 DE 9", "A COMIDA JÁ TEM", "BATE A PROTEÍNA"), "BCAA", "SUAS SÉRIES",
 [("ROSCA: 12 KG × 10", WHITE), ("4 SEMANAS: 14 KG", WHITE), ("SEM BCAA", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
