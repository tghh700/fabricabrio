from cenas_1511 import *
import roteiro_brio_48_cinto as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    squat_belt(c, t, HX, 0.95, 2.4)
    draw_text(c, "?", 800, 1500, 240 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", 1.0, align="center")

def oque(c, t, d):
    pr = 0.5 + 0.5 * math.sin(t * 3)
    d = 0.5 * (0.5 - 0.5 * math.cos(t * 2.0))
    squatter(c, HX, 0.95, d, belly=pr)
    from brio_kit2 import _drop
    dr = _drop(pose_mix("bar_back", "squat_deep", d)); belt(c, HX, 0.95, dr)
    by = FLOOR_Y + (dr - 335) * 0.95
    for k in range(2):
        a = ease_out(prog((t * 1.1 + k / 2) % 1, 0, 1))
        arrow(c, HX + 90 + 40 * a, by, HX + 190 + 40 * a, by, YEL, 14, 1.0)
    tag(c, 790, 1100, "PAREDE PRO ABDÔMEN", YEL, INK, 42, back_out(prog(t, 0.4, 0.3)))

def quando(c, t, d):
    squat_belt(c, t, HX, 0.95, 2.4)
    stack_list(c, t, ("AGACHAMENTO", "TERRA"), 790, 1000, 420, 160, -1, num=False)
    for i in range(2):
        icon_ok(c, 1040, 1000 + i * 160, 0.45, prog(t, 0.6 + i * 0.3, 0.3))
    draw_text(c, "PERTO DO MÁXIMO", 790, 1450, 54, YEL, "Anton", back_out(prog(t, 1.2, 0.3)), align="center")

def nao(c, t, d):
    act_curl(c, t, HX, 0.95)
    stack_list(c, t, ("ROSCA", "SUPINO", "SÉRIE LEVE"), 790, 1000, 420, 160, -1, num=False)
    for i in range(3):
        icon_x(c, 1040, 1000 + i * 160, 0.45, prog(t, 0.5 + i * 0.3, 0.3))

def tecnica(c, t, d):
    pr = 0.5 + 0.5 * math.sin(t * 3)
    squatter(c, HX, 0.95, 0.5 * (0.5 - 0.5 * math.cos(t * 2.0)), belly=pr)
    stack_list(c, t, ("1º TRAVAR SEM CINTO", "2º CINTO NO PESADO"), 790, 1050, 470, 170, 0, num=False)

def aperto(c, t, d):
    squat_belt(c, t, HX, 0.95, 2.0, 0.4)
    for k in range(3):  # ar entrando
        f = (t * 0.8 + k / 3) % 1
        cap_line(c, 560 - 120 * f, 1060, 620 - 120 * f, 1060, BLU, 10, 1 - f)
    tag(c, 800, 1200, "FIRME, MAS RESPIRA", GRN, INK, 44, back_out(prog(t, 0.4, 0.3)))
    tag(c, 800, 1360, "SEM AR? APERTADO DEMAIS", RED, WHITE, 36, back_out(prog(t, 1.4, 0.3)))

VIS = {"hook": scene(hook, "CINTO: PRECISA?", YEL), "oque": scene(oque, "O CINTO FIRMA O TRONCO", YEL),
       "quando": scene(quando, "AGACHAMENTO E TERRA", GRN), "nao": scene(nao, "SÉRIE LEVE: SEM CINTO", RED),
       "tecnica": scene(tecnica, "TÉCNICA PRIMEIRO", YEL), "aperto": scene(aperto, "APERTO CERTO", GRN)}
SFX = finish(R, VIS, ("SÓ NA SÉRIE PESADA", "TÉCNICA PRIMEIRO", "FIRME, MAS RESPIRA"), "CINTO", "AGACHAMENTO",
 [("80 KG × 8 SEM CINTO", WHITE), ("100 KG × 3 COM CINTO", WHITE), ("SÓ NO PESADO", None)], ("REGISTRE SUAS SÉRIES", "PESADAS NO BRIO"))
