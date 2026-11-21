"""BRIO 84 — crescer treinando 3×/semana (cadeia erro → consequência → volta). Kit cenas_v2 + cenas_2211."""
from cenas_2211 import *
import roteiro_brio_84_tres as R

DAYS3 = (0, 2, 4)


def day_labels(c, t, x, y, labs, cols, cell=96, t0=0.3):
    gap = 14; w = 7 * cell + 6 * gap
    for j, (i, l) in enumerate(zip(DAYS3, labs)):
        cx = x - w / 2 + cell / 2 + i * (cell + gap)
        p = back_out(prog(t, t0 + j * 0.2, 0.3))
        if p > 0:
            tag(c, cx, y + 110, l, cols[j], INK, 30, p)


def e1(c, t, d):
    k = 0.5 * d
    c.save(); shake(c, t, k)
    act_curl(c, t, 300, 0.95, 2.6)
    week(c, t, 700, 900, DAYS3, YEL, cell=70, t0=0.1)
    day_labels(c, t, 700, 870, ("PEITO", "COSTAS", "PERNA"), (YEL, YEL, YEL), cell=70)
    if t > k:
        draw_text(c, "1×", 700, 1240, 170, RED, "Anton", back_out(prog(t, k, 0.3)), align="center")
        draw_text(c, "POR SEMANA", 700, 1300, 32, GREY, "Space Mono", 1.0, align="center", spacing=2)
    c.restore()
    consequence(c, t, "x", 920, 1160, k)
    red_flash(c, t, k)


def f1(c, t, d):
    act_squat(c, t, 300, 0.9)
    week(c, t, 700, 900, DAYS3, GRN, cell=70, t0=0.1)
    day_labels(c, t, 700, 870, ("CORPO", "CORPO", "CORPO"), (GRN, GRN, GRN), cell=70)
    p = back_out(prog(t, d * 0.45, 0.3))
    draw_text(c, "3×", 700, 1240, 170, GRN, "Anton", p, align="center")
    draw_text(c, "CADA MÚSCULO", 700, 1300, 32, GREY, "Space Mono", 1.0, align="center", spacing=2)


EX10 = ("SUPINO", "CRUCIFIXO", "PUXADA", "REMADA", "AGACHAMENTO", "LEG PRESS", "ROSCA", "TRÍCEPS", "OMBRO", "PANTURRILHA")


def e2(c, t, d):
    k = 0.55 * d
    c.save(); shake(c, t, k)
    act_tired(c, t, 300, 0.95) if t > k else act_curl(c, t, 300, 0.95, 2.6)
    n = min(10, int(t / 0.18) + 1)
    for i in range(n):
        p = back_out(prog(t, i * 0.18, 0.2))
        col_ = i // 5; row = i % 5
        card(c, 600 + col_ * 270, 860 + row * 78, 250, 64, CARD, p)
        draw_text(c, EX10[i], 600 + col_ * 270, 874 + row * 78, 26, WHITE, "Anton", p, align="center")
    clock(c, t, 740, 1360, 110, 120 * ease(prog(t, 0.2, k)), RED, prog(t, 0.1, 0.3))
    if t > k:
        tag(c, 740, 1530, "2 HORAS", RED, WHITE, 44, back_out(prog(t, k, 0.3)))
    c.restore()
    red_flash(c, t, k)
    consequence(c, t, "x", 930, 1300, k)


def f2(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6)
    for i in range(5):
        p = back_out(prog(t, 0.1 + i * 0.2, 0.25))
        card(c, 740, 860 + i * 78, 400, 64, CARD, p)
        draw_text(c, ("SUPINO", "REMADA", "AGACHAMENTO", "OMBRO", "ROSCA")[i], 740, 874 + i * 78, 28, WHITE, "Anton", p, align="center")
    clock(c, t, 740, 1360, 110, 45 * ease(prog(t, 0.2, d * 0.6)), GRN, prog(t, 0.1, 0.3))
    tag(c, 740, 1530, "45 MIN", GRN, INK, 44, back_out(prog(t, d * 0.5, 0.3)))


def e3(c, t, d):
    k = 0.5 * d
    c.save(); shake(c, t, k)
    act_pose(c, t, "shrug", 300, 0.95)
    week(c, t, 700, 1000, DAYS3, YEL, cell=70, t0=0.1)
    gap = 14; cell = 70; w = 7 * cell + 6 * gap
    cx = 700 - w / 2 + cell / 2 + 2 * (cell + gap)
    p = prog(t, k, 0.25)
    if p > 0:
        rrect(c, cx - cell / 2, 1000 - cell / 2, cell, cell, 20, RED, p)
        x_mark(c, cx, 1000, 0.3, p, WHITE)
        tag(c, 700, 1200, "-1/3 DA SEMANA", RED, WHITE, 48, back_out(prog(t, k + 0.15, 0.3)))
    c.restore()
    red_flash(c, t, k)


def f3(c, t, d):
    act_walk(c, t, 260, 0.95, 6.0, move=18)
    for r in range(3):
        y = 900 + r * 120
        week(c, t - r * 0.35, 720, y, DAYS3, GRN, cell=62, t0=0.1)
    tag(c, 720, 1340, "SEG · QUA · SEX", GRN, INK, 44, back_out(prog(t, d * 0.45, 0.3)))


def conc(c, t, d):
    act_curl(c, t, 300, 0.95, 2.4, heavy=True)
    pieces(c, t, 760, 1000, ("CORPO", "45 MIN", "FIXOS"), 0.2, 0.45, 170)
    graph(c, t, 600, 1220, 340, 200, [(0, 0.1), (0.33, 0.35), (0.66, 0.6), (1, 0.95)], GRN, 1.4, 1.2, "MÚSCULO")


SCENES = dict(e1=e1, f1=f1, e2=e2, f2=f2, e3=e3, f3=f3, conc=conc)
CYCLES = [("1×", "CORPO"), ("2 H", "45 MIN"), ("FALTA", "FIXOS")]
HOT = [b["k"] for b in R.BEATS]
VIS = chain_vis(R, SCENES, CYCLES, HOT, None)
VIS["cta"] = wipe_in(cta_factory("TREINO", "SEU TREINO", [("SEG · CORPO", WHITE), ("QUA · CORPO", WHITE), ("SEX · CORPO", None)],
                                 ("REGISTRE SEUS TREINOS", "NO BRIO")), slide=0)
SFX = chain_sfx(R, VIS)
SFX["cta"] = sfx_for(["cta"], R.BEATS[-1])["cta"]
