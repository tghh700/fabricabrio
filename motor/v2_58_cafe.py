from cenas_1611 import *
import roteiro_brio_58_cafe as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    cup(c, t, 790, 1300, 1.1, back_out(prog(t, 0.05, 0.3)))
    draw_text(c, "?", 990, 1080, 140, YEL, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def sim(c, t, d):
    act_curl(c, t, heavy=True)
    tag(c, 790, 1100, "CAFEÍNA", YEL, INK, 80, back_out(prog(t, 0.1, 0.3)))
    icon_ok(c, 790, 1320, 1.3, prog(t, 0.5, 0.3))

def rende(c, t, d):
    act_curl(c, t, spd=3.0)
    counter(c, t, 790, 1150, 8, 9, "{:.0f}", 170, GRN, 0.3, 1.0, " REP")
    draw_text(c, "MAIS FÔLEGO", 790, 1420, 56, YEL, "Anton", prog(t, 0.8, 0.3), align="center")

def quando(c, t, d):
    act_walk(c, t, spd=4.0)
    cup(c, t, 700, 1350, 0.75, back_out(prog(t, 0.05, 0.3)))
    draw_text(c, "30 A 60", 860, 1150, 120, YEL, "Anton", back_out(prog(t, 0.3, 0.3)), align="center")
    draw_text(c, "MIN ANTES", 860, 1230, 46, GREY, "Space Mono", prog(t, 0.5, 0.3), align="center", spacing=2)

def dose(c, t, d):
    act_walk(c, t, spd=4.0)
    for i in range(3):
        cup(c, t, 610 + i * 180, 1300, 0.55, back_out(prog(t, 0.1 + i * 0.3, 0.3)))
    q = prog(t, 1.1, 0.3)
    if q > 0:
        x_mark(c, 970, 1250, 0.9, q, RED)
    draw_text(c, "MAIS NÃO AJUDA", 790, 1480, 64, YEL, "Anton", prog(t, 0.8, 0.3), align="center")

def noite(c, t, d):
    moon(c, t, 680, 990)
    sleeper(c, t, 540, 1430, 1.0, restless=1.0)
    cup(c, t, 950, 1170, 0.5, back_out(prog(t, 0.2, 0.3)))
    q = prog(t, 0.6, 0.3)
    if q > 0:
        x_mark(c, 950, 1130, 0.8, q, RED)

VIS = {"hook": scene(hook, "CAFÉ ANTES?", YEL), "sim": scene(sim, "FUNCIONA", GRN),
       "rende": scene(rende, "RENDE MAIS", GRN), "quando": scene(quando, "30 A 60 MIN ANTES", YEL),
       "dose": scene(dose, "2 XÍCARAS BASTAM", YEL), "noite": scene(noite, "CUIDADO COM O SONO", RED, bg=False)}
SFX = finish(R, VIS, ("AJUDA, SIM", "30 A 60 MIN ANTES", "LONGE DO SONO"), "CAFÉ", "SUAS SÉRIES",
 [("SEM CAFÉ: 40 KG × 8", WHITE), ("COM CAFÉ: 40 KG × 9", WHITE), ("+1 REPETIÇÃO", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
