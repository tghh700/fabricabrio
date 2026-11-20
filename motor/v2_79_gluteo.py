from cenas_2111 import *
import roteiro_brio_79_gluteo as R
BEAT_CTA = R.BEATS[-1]
TX = 150

def hook(c, t, d):
    hx, hy = act_thrust(c, t, TX)
    glute_glow(c, hx - 40, hy + 40, 70, 0.6 + 0.4 * math.sin(t * 4))
    draw_text(c, "A MELHOR?", 800, 960, 92 * (1 + 0.03 * math.sin(t * 5)), YEL, "Anton", back_out(prog(t, 0.2, 0.3)), align="center")
    draw_text(c, "PRO GLÚTEO", 800, 1060, 46, GREY, "Space Mono", prog(t, 0.4, 0.3), align="center", spacing=2)

def estudo(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.55, lambda x: act_squat(c, t, x, 1.0, 2.4, 0.9))
    def Rr(c, t, cx, by):
        mini_thrust(c, t, cx + 10, by, 0.42)
    split(c, t, L, Rr, "AGACHAMENTO", "ELEVAÇÃO", BLU, YEL)
    draw_text(c, "9 SEMANAS", 540, 860, 48, WHITE, "Anton", back_out(prog(t, 0.9, 0.3)), align="center")

def igual(c, t, d):
    act_squat(c, t)
    draw_text(c, "GLÚTEO", 790, 820, 40, GREY, "Space Mono", prog(t, 0.05, 0.3), align="center", spacing=2)
    bars(c, t, 790, 1220, (0.85, 0.85), ("AGACH.", "ELEV."), (BLU, YEL), w=130, gap=90, h=300, step=0.2)
    draw_text(c, "=", 790, 1130, 110, WHITE, "Anton", prog(t, 0.8, 0.3), align="center")
    tag(c, 790, 1400, "+ COXA NO AGACHAMENTO", GRN, INK, 38, back_out(prog(t, 0.55 * d, 0.3)))

def carga(c, t, d):
    hx, hy = act_thrust(c, t, TX, spd=2.0)
    v = lerp(40, 60, ease_out(prog(t, 0.3, 1.6)))
    draw_text(c, f"{v:.0f} KG", 800, 1090, 140 * (1 + 0.03 * math.sin(t * 5)), GRN, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    arrow(c, 800, 1300, 800, 1180, GRN, 14, ease_out(prog(t, 0.8, 0.3)))
    tag(c, 800, 870, "SÉRIE PUXADA", YEL, INK, 46, back_out(prog(t, 0.5, 0.3)))

VIS = {"hook": scene(hook, "ELEVAÇÃO PÉLVICA É A MELHOR?", YEL), "estudo": scene(estudo, "UM GRUPO DE CADA JEITO", BLU, bg=False),
       "igual": scene(igual, "CRESCEU IGUAL", GRN), "carga": scene(carga, "CARGA SUBINDO", GRN)}
SFX = finish(R, VIS, ("OS DOIS FUNCIONAM", "ESCOLHE O QUE GOSTA", "SOBE A CARGA"), "GLÚTEO", "SUAS SÉRIES",
 [("ELEVAÇÃO: 4 × 10", WHITE), ("AGACHAMENTO: 3 × 8", WHITE), ("CARGA SUBINDO", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
