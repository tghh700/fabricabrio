from cenas_1511 import *
import roteiro_brio_50_puxar as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_press(c, t, HX + 20, 0.8, 2.6)
    scale_beam(c, t, 820, 1150, -ease(prog(t, 0.3, 0.8)), "SUPINO", "REMADA", L=230)

def espelho(c, t, d):
    act_pose(c, t, "flex")
    # espelho
    rrect(c, 640, 930, 300, 560, 30, (0.30, 0.42, 0.55), 0.5)
    cap_line(c, 690, 1000, 760, 960, WHITE, 10, 0.5); cap_line(c, 690, 1060, 820, 980, WHITE, 8, 0.35)
    tag(c, 790, 1580, "PEITO E OMBRO DA FRENTE", YEL, INK, 38, back_out(prog(t, 0.5, 0.3)))

def desequilibrio(c, t, d):
    act_press(c, t, HX + 20, 0.8, 2.4)
    bars(c, 790, 1480, 400, 460, (0.95, 0.35), t, 0.15, (BLU, RED))
    for i, l in enumerate(("FRENTE", "COSTAS")):
        draw_text(c, l, 790 - 200 + (i + 0.5) * 200, 1530, 30, GREY, "Space Mono", 1.0, align="center")

def regra(c, t, d):
    k = ease(prog(t, 0.6, 1.0))
    scale_beam(c, t, 540, 1080, lerp(-1, 0, k), "EMPURRAR", "PUXAR")
    for i in range(2):
        p = back_out(prog(t, 0.2 + i * 0.6, 0.3))
        draw_text(c, "1 SÉRIE", 240 + i * 600, 1550, 70, YEL, "Anton", p, align="center")

def pares(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_press(c, t, x + 15, 0.72))
    def Rr(c, t, cx, by):
        c.save(); c.translate(cx, by); c.scale(0.62, 0.62); c.translate(-cx, -FLOOR_Y)
        hanger(c, cx, FLOOR_Y - 760, 0.8, 0.5 - 0.5 * math.cos(t * 2.4)); c.restore()
    split(c, t, L, Rr, "EMPURRA", "PUXA", YEL, BLU)

def supino(c, t, d):
    act_curl(c, t, HX, 0.95)
    battery(c, 790, 1150, lerp(0.4, 0.95, ease(prog(t, 0.2, d * 0.6))), "COSTAS", 170, 300, GRN)
    tag(c, 790, 1460, "BARRA MAIS ESTÁVEL", GRN, INK, 44, back_out(prog(t, 0.9, 0.3)))

VIS = {"hook": scene(hook, "DESEQUILÍBRIO", RED), "espelho": scene(espelho, "SÓ O QUE O ESPELHO MOSTRA", RED),
       "desequilibrio": scene(desequilibrio, "COSTAS ATRASADAS", RED), "regra": scene(regra, "EMPURROU, PUXA", GRN, bg=False),
       "pares": scene(pares, "OS PARES", YEL, bg=False), "supino": scene(supino, "COSTAS AJUDAM O SUPINO", GRN)}
SFX = finish(R, VIS, ("EMPURROU, PUXA", "CONTA AS SÉRIES", "DEIXA EMPATADO"), "PUXAR", "SEU TREINO",
 [("EMPURRAR: 9 SÉRIES", WHITE), ("PUXAR: 9 SÉRIES", WHITE), ("EMPATADO", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
