from cenas_2011 import *
import roteiro_brio_78_flexivel as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_squat(c, t, depth=0.5)
    sh = 6 * math.sin(t * 30) * prog(t, 0.6, 0.2)
    draw_text(c, "TRAVADO?", 790 + sh, 1180, 130, YEL, "Anton", back_out(prog(t, 0.1, 0.3)), align="center")
    flex_band(c, t, 790, 1360, 0.05 + 0.04 * math.sin(t * 3), 380)

def contra(c, t, d):
    act_squat(c, t, depth=1.0)
    k = ease(prog(t, 0.2, 1.2))
    flex_band(c, t, 790, 1200, 0.15 + 0.8 * k * (0.75 + 0.25 * math.sin(t * 2.4)), 400)
    tag(c, 790, 1000, "MAIS FLEXÍVEL", GRN, INK, 52, back_out(prog(t, 0.6, 0.3)))
    icon_ok(c, 790, 1400, 0.8, prog(t, 0.9, 0.3))

def estudo(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_squat(c, t, x, 1.0, 2.4, 1.0))
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: chunky(c, x, FLOOR_Y, 1.0, pose_mix("idle", "cheer", 0.5 + 0.5 * math.sin(t * 1.6)), bob=0))
    split(c, t, L, Rr, "MUSCULAÇÃO", "ALONGAMENTO", BLU, YEL)
    q = ease_out(prog(t, 1.0, 0.8))
    for i in range(2):
        rrect(c, 120 + i * 500, 1022, 340, 26, 13, (0.12, 0.13, 0.17))
        rrect(c, 120 + i * 500, 1022, 340 * 0.8 * q, 26, 13, GRN)
    draw_text(c, "=", 540, 1300, 110, WHITE, "Anton", prog(t, 1.1, 0.3), align="center")

def desce(c, t, d):
    ph = 0.5 - 0.5 * math.cos(t * 1.8)
    squatter(c, HX, 0.95, ph)
    angle_gauge(c, t, 790, 1250, 170, ph, prog(t, 0.05, 0.3), ok=ph > 0.85)
    draw_text(c, "AMPLITUDE", 790, 1330, 40, GREY, "Space Mono", prog(t, 0.1, 0.3), align="center", spacing=2)
    tag(c, 790, 980, "ATÉ O FIM", GRN, INK, 54, back_out(prog(t, 0.6, 0.3)))

VIS = {"hook": scene(hook, "MUSCULAÇÃO TRAVA?", YEL), "contra": scene(contra, "PELO CONTRÁRIO", GRN),
       "estudo": scene(estudo, "AMPLITUDE PARECIDA", BLU, bg=False), "desce": scene(desce, "DESCE ATÉ O FIM", GRN)}
SFX = finish(R, VIS, ("MAIS FORTE", "MAIS SOLTO", "MOVIMENTO COMPLETO"), "FLEXÍVEL", "SEUS TREINOS",
 [("AGACHAMENTO: 4 × 10", WHITE), ("STIFF: 3 × 10", WHITE), ("TREINO REGISTRADO", None)], ("REGISTRE SEUS TREINOS", "NO BRIO"))
