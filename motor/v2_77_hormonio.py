from cenas_2011 import *
import roteiro_brio_77_hormonio as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_squat(c, t)
    draw_text(c, "PERNA", 790, 960, 90, WHITE, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    arrow(c, 790, 1010, 790, 1150, YEL, 16, ease_out(prog(t, 0.4, 0.3)))
    draw_text(c, "BRAÇO?", 790, 1290, 130 * (1 + 0.04 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.6, 0.3)), align="center")

def mito(c, t, d):
    act_squat(c, t, spd=2.6)
    for i in range(6):  # moléculas de hormônio subindo
        f = (t * 0.5 + i / 6) % 1
        disk(c, 640 + (i % 3) * 110, 1420 - 420 * f, 26, BLU, 0.9 * (1 - f))
    draw_text(c, "HORMÔNIO", 790, 1480, 40, BLU, "Space Mono", prog(t, 0.1, 0.3), align="center", spacing=2)
    tag(c, 790, 1000, "MITO", RED, WHITE, 90, back_out(prog(t, 0.6, 0.3)))
    icon_x(c, 960, 900, 0.7, prog(t, 0.8, 0.3))

def estudo(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_squat(c, t, x, 1.0, 2.4, 0.8))
    split(c, t, L, Rr, "SÓ BRAÇO", "+ PERNA", BLU, YEL)
    draw_text(c, "15 SEMANAS", 540, 860, 44, GREY, "Space Mono", prog(t, 0.9, 0.3), align="center", spacing=2)

def igual(c, t, d):
    act_curl(c, t)
    bars(c, t, 790, 1180, (0.8, 0.8), ("SÓ BRAÇO", "+ PERNA"), (BLU, YEL), w=130, gap=90, h=300, step=0.2)
    draw_text(c, "=", 790, 1110, 110, WHITE, "Anton", prog(t, 0.8, 0.3), align="center")
    draw_text(c, "PICO DE HORMÔNIO", 790, 1320, 30, GREY, "Space Mono", prog(t, 1.0, 0.3), align="center", spacing=1)
    spike(c, t, 600, 1350, 380, 150, prog(t, 1.1, 1.0), BLU)

VIS = {"hook": scene(hook, "PERNA FAZ O BRAÇO CRESCER?", YEL), "mito": scene(mito, "NÃO. É MITO.", RED),
       "estudo": scene(estudo, "UM BRAÇO DE CADA JEITO", BLU, bg=False), "igual": scene(igual, "CRESCERAM IGUAL", GRN)}
SFX = finish(R, VIS, ("HORMÔNIO PASSA RÁPIDO", "PERNA PELA PERNA", "BRAÇO COM BRAÇO"), "PERNA", "SUAS SÉRIES",
 [("ROSCA: 3 × 10", WHITE), ("TRÍCEPS: 3 × 12", WHITE), ("CARGA SUBINDO", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
