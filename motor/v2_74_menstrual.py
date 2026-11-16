from cenas_1711 import *
import roteiro_brio_74_menstrual as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    cycle_ring(c, t, 790, 1200, 200, hot=(0, 4), p=prog(t, 0.05, 1.0))
    draw_text(c, "?", 790, 1260, 160, YEL, "Anton", back_out(prog(t, 0.8, 0.3)), align="center")

def pode(c, t, d):
    act_squat(c, t, spd=2.2)
    icon_ok(c, 790, 1150, 1.6, back_out(prog(t, 0.1, 0.35)))
    tag(c, 790, 1400, "PODE TREINAR", GRN, INK, 50, back_out(prog(t, 0.5, 0.3)))

def forca(c, t, d):
    act_curl(c, t, heavy=True)
    cycle_ring(c, t, 790, 1180, 190, hot=(0, 4), bars_=(1, 1, 1, 1))
    for k, v in enumerate((0.93, 0.97, 0.98, 0.96)):
        a = -math.pi / 2 + (k * 7 + 3) * 2 * math.pi / 28
        draw_text(c, f"{int(v * 100)}%", 790 + 95 * math.cos(a), 1180 + 95 * math.sin(a) + 14, 40, WHITE, "Anton", prog(t, 0.6 + k * 0.2, 0.3), align="center")

def cada(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0, heavy=True))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_tired(c, t, x, 1.0))
    split(c, t, L, Rr, "RENDE IGUAL", "DIA RUIM", GRN, YEL)

def ajusta(c, t, d):
    act_curl(c, t, spd=2.0)
    stack_list(c, t, ("MENOS SÉRIES", "MENOS CARGA", "MAS VAI"), 790, 980, 460, 160, 2 if t > 1.2 else -1)

def anota(c, t, d):
    act_walk(c, t, spd=4.0)
    for m in range(3):
        for k in range(4):
            v = (0.86, 0.95, 0.97, 0.93)[k] - 0.02 * m
            p = back_out(prog(t, 0.1 + (m * 4 + k) * 0.07, 0.25))
            if p > 0:
                rrect(c, 600 + k * 95, 1460 - m * 150 - 110 * v * p, 70, 110 * v * p, 12, (RED if k == 0 else GRN))
    for m in range(3):
        draw_text(c, f"MÊS {m + 1}", 1010, 1440 - m * 150, 30, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center")

VIS = {"hook": scene(hook, "TREINAR MENSTRUADA?", YEL), "pode": scene(pode, "PODE, SIM", GRN),
       "forca": scene(forca, "DIFERENÇA PEQUENA", YEL), "cada": scene(cada, "CADA MULHER É UMA", YEL, bg=False),
       "ajusta": scene(ajusta, "NO DIA RUIM, AJUSTA", YEL), "anota": scene(anota, "ANOTA O SEU PADRÃO", GRN)}
SFX = finish(R, VIS, ("PODE TREINAR", "DIFERENÇA PEQUENA", "AJUSTA E VAI"), "CICLO", "SUAS SÉRIES",
 [("SEMANA 1: 30 KG × 8", WHITE), ("SEMANA 2: 32 KG × 8", WHITE), ("SEU PADRÃO", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
