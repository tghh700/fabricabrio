from cenas_1711 import *
import roteiro_brio_66_balanca as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    v = lerp(70.0, 71.6, ease(prog(t, 0.3, 1.2)))
    bath_scale(c, 790, 1460, f"{v:.1f}".replace(".", ","), back_out(prog(t, 0.05, 0.3)), YEL)
    arrow(c, 990, 1330, 990, 1150, RED, 14, ease_out(prog(t, 0.8, 0.3)))

def calma(c, t, d):
    act_pose(c, t, "thumb")
    fat_blob(c, t, 790, 1180, 80, back_out(prog(t, 0.05, 0.3)))
    x_mark(c, 790, 1180, 1.3, prog(t, 0.5, 0.3), RED)
    draw_text(c, "NÃO É GORDURA", 790, 1420, 56, WHITE, "Anton", back_out(prog(t, 0.7, 0.3)), align="center")

def estoque(c, t, d):
    act_curl(c, t)
    muscle_fiber(c, t, 790, 1200, 420, 150, prog(t, 0.05, 0.3))
    for k in range(6):
        p = back_out(prog(t, 0.4 + k * 0.15, 0.25))
        if p > 0:
            disk(c, 640 + k * 60, 1200, 30 * p, INK); disk(c, 640 + k * 60, 1200, 24 * p, YEL)
    draw_text(c, "GLICOGÊNIO", 790, 1380, 48, YEL, "Anton", prog(t, 0.6, 0.3), align="center")

def agua(c, t, d):
    act_curl(c, t, spd=2.0)
    disk(c, 640, 1200, 50 * back_out(prog(t, 0.05, 0.3)), YEL)
    draw_text(c, "1 G", 640, 1320, 48, YEL, "Anton", prog(t, 0.1, 0.3), align="center")
    draw_text(c, "+", 750, 1225, 90, WHITE, "Anton", prog(t, 0.4, 0.3), align="center")
    for k in range(3):
        droplet(c, 840 + k * 70, 1200, 1.2 * back_out(prog(t, 0.5 + k * 0.25, 0.3)), 1.0)
    draw_text(c, "3 G DE ÁGUA", 910, 1320, 48, BLU, "Anton", prog(t, 1.0, 0.3), align="center")

def reparo(c, t, d):
    act_tired(c, t)
    k = 1.0 + 0.18 * ease(prog(t, 0.3, 1.0))
    muscle_fiber(c, t, 790, 1200, 400, 140, prog(t, 0.05, 0.3), k)
    for i in range(4):
        f = (t * 0.7 + i / 4) % 1
        droplet(c, 640 + i * 100, 1060 - 40 * f, 0.7, 0.9 * (1 - f))
    tag(c, 790, 1420, "LÍQUIDO DO REPARO", BLU, INK, 44, back_out(prog(t, 0.6, 0.3)))

def quilos(c, t, d):
    act_walk(c, t, spd=4.0)
    zigzag(c, t, 580, 1020, 420, 380, (0.2, 0.55, 0.75, 0.8, 0.78, 0.8, 0.79), YEL, trend=False)
    draw_text(c, "+1 A 2 KG", 790, 1500, 60, YEL, "Anton", back_out(prog(t, 0.6, 0.3)), align="center")
    draw_text(c, "DEPOIS ESTABILIZA", 790, 980, 34, GREY, "Space Mono", prog(t, 1.4, 0.3), align="center", spacing=1)

VIS = {"hook": scene(hook, "A BALANÇA SUBIU?", RED), "calma": scene(calma, "CALMA, É NORMAL", GRN),
       "estoque": scene(estoque, "O MÚSCULO GUARDA ENERGIA", YEL), "agua": scene(agua, "CADA GRAMA PUXA ÁGUA", BLU),
       "reparo": scene(reparo, "O REPARO INCHA", BLU), "quilos": scene(quilos, "1 A 2 KG A MAIS", YEL)}
SFX = finish(R, VIS, ("É ÁGUA, NÃO GORDURA", "1 A 2 KG NO COMEÇO", "OLHA A CARGA"), "BALANÇA", "SUA EVOLUÇÃO",
 [("SEMANA 1: 20 KG × 10", WHITE), ("SEMANA 3: 26 KG × 10", WHITE), ("+6 KG DE FORÇA", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
