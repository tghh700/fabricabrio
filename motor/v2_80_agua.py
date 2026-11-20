from cenas_2111 import *
import roteiro_brio_80_agua as R
BEAT_CTA = R.BEATS[-1]

def drinker(c, t, x=HX, s=0.95, lvl=0.8):
    u = 0.5 + 0.5 * math.sin(t * 1.6)
    hx, hy = chunky(c, x, FLOOR_Y, s, pose_mix("curl_down", "curl_up", 0.55 + 0.45 * u))
    bottle(c, hx + 6, hy - 40, 0.55, 1.0, 1.0, lvl)

def hook(c, t, d):
    drinker(c, t)
    for k in range(3):
        ice_cube(c, 700 + k * 110, 980 + 12 * math.sin(t * 3 + k), 38, back_out(prog(t, 0.1 + k * 0.1, 0.3)), 0.3 * k)
    draw_text(c, "FAZ MAL?", 800, 1250, 120 * (1 + 0.03 * math.sin(t * 5)), YEL, "Anton", back_out(prog(t, 0.3, 0.3)), align="center")

def mito(c, t, d):
    drinker(c, t)
    sh = 5 * math.sin(t * 30) * prog(t, 0.2, 0.3) * (1 - prog(t, 0.6, 0.2))
    draw_text(c, "CHOQUE", 800 + sh, 980, 90, WHITE, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    draw_text(c, "TÉRMICO", 800 + sh, 1080, 90, WHITE, "Anton", back_out(prog(t, 0.1, 0.3)), align="center")
    p = ease_out(prog(t, 0.5, 0.3))
    cap_line(c, 600, 1060, 600 + 400 * p, 940, RED, 18)
    tag(c, 800, 1260, "MITO", RED, WHITE, 90, back_out(prog(t, 0.7, 0.3)))

def estudo(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_walk(c, t, x, 1.0, 5.0))
        bottle(c, cx + 150, by - 360, 0.35, 1.0, 0.0, 0.7)
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_walk(c, t, x, 1.0, 5.0))
        bottle(c, cx + 150, by - 360, 0.35, 1.0, 1.0, 0.7)
        ice_cube(c, cx + 150, by - 470, 22, 1.0, 0.4)
    split(c, t, L, Rr, "NATURAL", "GELADA", GREY, BLU)
    q = ease_out(prog(t, 1.0, 1.0))
    rrect(c, 120, 1022, 340, 26, 13, (0.12, 0.13, 0.17)); rrect(c, 120, 1022, 340 * 0.68 * q, 26, 13, GREY)
    rrect(c, 620, 1022, 340, 26, 13, (0.12, 0.13, 0.17)); rrect(c, 620, 1022, 340 * 0.82 * q, 26, 13, BLU)
    tag(c, 790, 860, "+10 MIN", GRN, INK, 54, back_out(prog(t, 1.6, 0.3)))
    draw_text(c, "NO CALOR", 290, 875, 40, GREY, "Space Mono", prog(t, 1.0, 0.3), align="center", spacing=2)

def esfria(c, t, d):
    drinker(c, t)
    k = ease(prog(t, 0.2, 2.2))
    thermo_b(c, 700, 1380, lerp(0.15, 0.45, k), 1.0, h=380)
    thermo_b(c, 880, 1380, lerp(0.15, 0.8, k), 1.0, h=380)
    draw_text(c, "GELADA", 700, 1480, 30, BLU, "Space Mono", 1.0, align="center", spacing=1)
    draw_text(c, "SEM", 880, 1480, 30, GREY, "Space Mono", 1.0, align="center", spacing=1)
    tag(c, 790, 900, "SOBE MAIS DEVAGAR", BLU, INK, 44, back_out(prog(t, 0.6, 0.3)))

VIS = {"hook": scene(hook, "ÁGUA GELADA FAZ MAL?", YEL), "mito": scene(mito, "NÃO. É MITO.", RED),
       "estudo": scene(estudo, "QUEM BEBEU GELADA", BLU, bg=False), "esfria": scene(esfria, "ESFRIA POR DENTRO", BLU)}
SFX = finish(R, VIS, ("NÃO FAZ MAL", "GELADA OU NATURAL", "BEBE NO TREINO"), "ÁGUA", "SEUS TREINOS",
 [("SUPINO: 4 × 10", WHITE), ("REMADA: 3 × 12", WHITE), ("TREINO REGISTRADO", None)], ("REGISTRE SEUS TREINOS", "NO BRIO"))
