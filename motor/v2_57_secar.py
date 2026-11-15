from cenas_1611 import *
import roteiro_brio_57_secar as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_squat(c, t, spd=2.4)
    fat_blob(c, t, 790, 1200, lerp(110, 55, ease(prog(t, 0.3, 1.4))), prog(t, 0.05, 0.3))
    arrow(c, 990, 1100, 990, 1280, GRN, 14, ease_out(prog(t, 0.5, 0.4)))

def mito(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_walk(c, t, x, 1.0, spd=10.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0))
    split(c, t, L, Rr, "SÓ ESTEIRA?", "SÓ CRESCER?", BLU, BLU)

def gasto(c, t, d):
    act_squat(c, t, spd=2.6)
    battery(c, 790, 1150, lerp(1.0, 0.45, ease(prog(t, 0.2, 1.6))), "ENERGIA")
    draw_text(c, "PARECIDO COM", 790, 1470, 38, GREY, "Space Mono", prog(t, 0.6, 0.3), align="center", spacing=2)
    draw_text(c, "CAMINHADA RÁPIDA", 790, 1535, 54, WHITE, "Anton", prog(t, 0.7, 0.3), align="center")

def musculo(c, t, d):
    act_walk(c, t, spd=3.5)
    muscle_fiber(c, t, 790, 1220, 380, 150, prog(t, 0.05, 0.3), lerp(0.8, 1.15, ease(prog(t, 0.2, 1.0))))
    for k in range(6):
        f = (t * 0.8 + k / 6) % 1
        disk(c, 640 + k * 60, 1120 - 220 * f, 10, YEL, (1 - f) * 0.9)
    draw_text(c, "GASTA ATÉ PARADO", 790, 1420, 46, YEL, "Anton", prog(t, 0.5, 0.3), align="center")

def prato(c, t, d):
    act_curl(c, t)
    plate_food(c, 790, 1160, 1.3 + 0.03 * math.sin(t * 4), back_out(prog(t, 0.05, 0.3)))
    tag(c, 790, 1490, "QUEM DECIDE É O PRATO", RED, WHITE, 44, back_out(prog(t, 0.5, 0.3)))

def junto(c, t, d):
    act_squat(c, t, spd=2.4)
    stack_list(c, t, ("COMER MENOS", "TREINAR FORÇA", "CAMINHAR: BÔNUS"), 790, 990, 480, 160, int(t * 1.4) % 3)

VIS = {"hook": scene(hook, "EMAGRECE, SIM", GRN), "mito": scene(mito, "SÓ CARDIO EMAGRECE?", YEL, bg=False),
       "gasto": scene(gasto, "O TREINO GASTA", YEL), "musculo": scene(musculo, "MAIS MÚSCULO, MAIS GASTO", GRN),
       "prato": scene(prato, "O PRATO DECIDE", RED), "junto": scene(junto, "FORÇA + DIETA", GRN)}
SFX = finish(R, VIS, ("TREINO GASTA", "PRATO DECIDE", "FORÇA MUDA O CORPO"), "SECAR", "SEUS TREINOS",
 [("SEG: TREINO A", WHITE), ("QUA: TREINO B", WHITE), ("3 TREINOS NA SEMANA", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
