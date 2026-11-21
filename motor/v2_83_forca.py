"""BRIO 83 — por que a força para de subir (cadeia erro → consequência → volta). Kit cenas_v2 + cenas_2211."""
from cenas_2211 import *
import roteiro_brio_83_forca as R


def e1(c, t, d):
    k = 0.45 * d
    c.save(); shake(c, t, k)
    act_curl(c, t, 300, 0.95, 3.4)                     # rosca rápida, halter leve
    counter(c, t, 330, 900, 1, 15, size=120, col=WHITE, t0=0.1, dur=d * 0.8, suffix=" REP")
    graph(c, t, 590, 980, 360, 280, [(0, 0.3), (0.33, 0.32), (0.66, 0.31), (1, 0.32)], RED, 0.2, 1.4, "FORÇA · 4 SEMANAS")
    c.restore()
    consequence(c, t, "x", 900, 900, k)
    red_flash(c, t, k)


def f1(c, t, d):
    act_curl(c, t, 300, 0.95, 1.7, heavy=True)          # rosca lenta, halter pesado
    counter(c, t, 330, 900, 1, 6, size=120, col=GRN, t0=0.1, dur=d * 0.7, suffix=" REP")
    graph(c, t, 590, 980, 360, 280, [(0, 0.2), (0.33, 0.4), (0.66, 0.62), (1, 0.85)], GRN, 0.2, 1.4, "FORÇA · 4 SEMANAS")
    icon_ok(c, 930, 900, 0.8, prog(t, d * 0.6, 0.3))


def e2(c, t, d):
    k = 0.5 * d
    fr = clamp(t / max(k, 0.1))
    c.save(); shake(c, t, k)
    if t < k:
        act_pose(c, t, "tired", 300, 0.95)
        timer(c, t, 760, 1060, 150, fr, f"0:{int(30 * fr):02d}", RED, prog(t, 0.05, 0.3))
    else:
        act_tired(c, t, 300, 0.95)
        bars(c, 760, 1300, 380, 400, (0.9, 0.42), t - k + 0.6, 0.15, (GRN, RED))
        for i, l in enumerate(("1ª SÉRIE", "2ª SÉRIE")):
            draw_text(c, l, 760 - 190 + (i + 0.5) * 190, 1350, 28, GREY, "Space Mono", 1.0, align="center")
    c.restore()
    if t >= k:
        consequence(c, t, "drop", 940, 1000, k + 0.1)
    red_flash(c, t, k)


def f2(c, t, d):
    fr = ease(prog(t, 0.1, d * 0.7))
    act_pose(c, t, "idle", 300, 0.95)
    timer(c, t, 760, 1000, 150, fr, f"{int(1 + 2 * fr)}:00", GRN, prog(t, 0.05, 0.3))
    battery(c, 760, 1340, lerp(0.25, 1.0, fr), None, 150, 190, None)
    icon_ok(c, 960, 1260, 0.7, prog(t, d * 0.65, 0.3))


EX = ("ROSCA", "MARTELO", "SCOTT", "CABO")


def e3(c, t, d):
    k = 0.55 * d
    c.save(); shake(c, t, k)
    act_pose(c, t, "shrug", 300, 0.95)
    i = min(int(t / 0.55), len(EX) - 1)
    pc = back_out(prog(t - i * 0.55, 0, 0.25))
    card(c, 760, 960, 420, 130, CARD, pc)
    draw_text(c, EX[i], 760, 985, 64, WHITE, "Anton", pc, align="center")
    draw_text(c, f"MÊS {i + 1}", 760, 880, 30, GREY, "Space Mono", 1.0, align="center", spacing=2)
    graph(c, t, 590, 1100, 360, 240, [(0, 0.3), (0.25, 0.5), (0.5, 0.25), (0.75, 0.48), (1, 0.28)], RED, 0.2, 1.5, "FORÇA")
    c.restore()
    consequence(c, t, "x", 960, 1150, k)
    red_flash(c, t, k)


def f3(c, t, d):
    act_curl(c, t, 300, 0.95, 2.2, heavy=True)
    rows = ("SEM 1 · 20 KG", "SEM 4 · 22 KG", "SEM 8 · 25 KG")
    for i, s in enumerate(rows):
        p = back_out(prog(t, 0.2 + i * 0.5, 0.3))
        card(c, 770, 900 + i * 125, 440, 100, CARD, p)
        if p > 0:
            draw_text(c, s, 770, 922 + i * 125, 48, GRN if i == 2 else WHITE, "Anton", p, align="center")
    graph(c, t, 590, 1300, 360, 160, [(0, 0.1), (0.5, 0.45), (1, 0.9)], GRN, 1.4, 1.0)


def conc(c, t, d):
    act_curl(c, t, 300, 0.95, 2.4, heavy=True)
    pieces(c, t, 760, 1000, ("PESO", "DESCANSO", "MESMOS"), 0.2, 0.45, 170)
    graph(c, t, 600, 1220, 340, 200, [(0, 0.1), (0.33, 0.35), (0.66, 0.6), (1, 0.95)], GRN, 1.4, 1.2, "FORÇA")


SCENES = dict(e1=e1, f1=f1, e2=e2, f2=f2, e3=e3, f3=f3, conc=conc)
CYCLES = [("LEVE", "PESADO"), ("30 S", "2-3 MIN"), ("TROCA", "MESMOS")]
HOT = [b["k"] for b in R.BEATS]
VIS = chain_vis(R, SCENES, CYCLES, HOT, None)
VIS["cta"] = wipe_in(cta_factory("FORÇA", "SUA FORÇA", [("ROSCA 20 KG", WHITE), ("ROSCA 22 KG", WHITE), ("ROSCA 25 KG", None)],
                                 ("REGISTRE SUAS SÉRIES", "NO BRIO")), slide=0)
SFX = chain_sfx(R, VIS)
SFX["cta"] = sfx_for(["cta"], R.BEATS[-1])["cta"]
