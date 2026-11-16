from cenas_1711 import *
import roteiro_brio_63_proteina as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    draw_text(c, "? G", 780, 1220, 220 * (1 + 0.06 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.1, 0.3)), align="center")
    draw_text(c, "DE PROTEÍNA POR DIA", 780, 1330, 40, GREY, "Space Mono", prog(t, 0.4, 0.3), align="center", spacing=2)

def conta(c, t, d):
    act_curl(c, t, spd=2.2)
    counter(c, t, 780, 1080, 0, 1.6, "{:.1f}", 170, GRN, suffix=" G")
    draw_text(c, "POR KG DE PESO", 780, 1230, 40, GREY, "Space Mono", prog(t, 0.6, 0.3), align="center", spacing=2)
    # curva que achata depois de 1,6
    x0, y0, w, h = 600, 1470, 380, 170
    q = ease_out(prog(t, 0.6, 1.2))
    pts = [(x0 + w * f, y0 - h * min(1, f / 0.6) ** 0.7) for f in [i / 40 * q for i in range(41)]]
    poly(c, pts, YEL, 8); cap_line(c, x0, y0, x0 + w, y0, GREY, 4, prog(t, 0.6, 0.2))

def exemplo(c, t, d):
    act_walk(c, t, spd=4.0)
    bath_scale(c, 790, 1460, "70,0", back_out(prog(t, 0.05, 0.3)), WHITE)
    arrow(c, 790, 1340, 790, 1230, YEL, 14, ease_out(prog(t, 0.4, 0.3)))
    counter(c, t, 790, 1080, 0, 112, "{:.0f}", 170, YEL, t0=0.5, suffix=" G")

def prato(c, t, d):
    act_walk(c, t, spd=4.0)
    items = ((chicken, 640, 1080, "30 G"), (egg, 940, 1080, "6 G"), (None, 640, 1350, "8 G"), (None, 940, 1350, "7 G"))
    labs = ("FRANGO", "OVO", "LEITE", "FEIJÃO")
    for i, (fn, x, y, g) in enumerate(items):
        p = back_out(prog(t, 0.1 + i * 0.3, 0.3))
        if p <= 0:
            continue
        card(c, x, y, 260, 230, CARD, p)
        if fn:
            fn(c, x, y - 30, 0.7, p)
        elif i == 2:
            rrect(c, x - 40, y - 100, 80, 130, 18, FOAM, p)
        else:
            for k in range(5):
                disk(c, x - 50 + k * 25, y - 40 + 12 * (k % 2), 16 * p, (0.45, 0.25, 0.2))
        draw_text(c, labs[i] + " " + g, x, y + 82, 42, YEL, "Anton", p, align="center")

def divide(c, t, d):
    act_curl(c, t)
    for i in range(4):
        plate_food(c, 620 + (i % 2) * 300, 1060 + (i // 2) * 300, 0.75, back_out(prog(t, 0.1 + i * 0.25, 0.3)))
        draw_text(c, "30 G", 620 + (i % 2) * 300, 1200 + (i // 2) * 300, 38, GRN, "Anton", prog(t, 0.3 + i * 0.25, 0.3), align="center")

def mais(c, t, d):
    def L(c, t, cx, by):
        draw_text(c, "112 G", cx, by - 330, 120, GRN, "Anton", 1.0, align="center")
        muscle_fiber(c, t, cx, by - 160, 280, 90, 1.0, 1.0)
    def Rr(c, t, cx, by):
        draw_text(c, "224 G", cx, by - 330, 120, YEL, "Anton", 1.0, align="center")
        muscle_fiber(c, t, cx, by - 160, 280, 90, 1.0, 1.0)
        draw_text(c, "=", cx - 250, by - 140, 90, WHITE, "Anton", prog(t, 1.2, 0.3), align="center")
    split(c, t, L, Rr, "1,6 G/KG", "O DOBRO", GRN, YEL)

VIS = {"hook": scene(hook, "QUANTA PROTEÍNA?", YEL), "conta": scene(conta, "1,6 G POR QUILO", GRN),
       "exemplo": scene(exemplo, "70 KG = 112 G", YEL), "prato": scene(prato, "A COMIDA SOMA", GRN),
       "divide": scene(divide, "3 OU 4 REFEIÇÕES", YEL), "mais": scene(mais, "O DOBRO NÃO CRESCE MAIS", RED, bg=False)}
SFX = finish(R, VIS, ("1,6 G POR QUILO", "3 OU 4 REFEIÇÕES", "CARGA SUBINDO"), "PROTEÍNA", "SUAS CARGAS",
 [("SEMANA 1: 40 KG × 10", WHITE), ("SEMANA 4: 44 KG × 10", WHITE), ("+4 KG NO MÊS", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
