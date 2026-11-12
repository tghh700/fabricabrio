"""BRIO 29 — séries de aquecimento: carimbos 50/70/85 %."""
import math
from brio_kit2 import *
import roteiro_brio_29_aquece as R
BEAT_CTA = R.BEATS[-1]


def rep(t, f=2.0):
    return 0.5 - 0.5 * math.cos(t * f)


def ramp(c, t, n_on, hot=None):
    """4 barras: 50, 70, 85, 100 %"""
    labs = ("50%", "70%", "85%", "100%")
    for i, lab in enumerate(labs):
        x = 600 + i * 95; h = (0.5, 0.7, 0.85, 1.0)[i] * 380
        on = i < n_on
        rrect(c, x, 1450 - h, 70, h, 10, (YEL if i == hot else GRN) if on else CARD)
        draw_text(c, lab, x + 35, 1510, 30, WHITE if on else GREY, "Space Mono", 1.0, align="center")


def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        sy = squatter(c, 380, 0.95, rep(t, 2.6))
        ramp(c, t, 4 if t > 0.2 else 0, hot=3)
        x_mark(c, 700, 950, 0.8, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "DIRETO NO PESADO?", RED, WHITE, 62, back_out(prog(t, d * 0.45, 0.3)))


def risco(c, t, d, b):
    with Cam(c, t, punch=0.06):
        squatter(c, 380, 0.95, 0.25 * rep(t, 3))
        for i in range(3):
            a = 0.4 + 0.6 * math.sin(t * 5 + i)
            snowflake(c, 700 + i * 90, 1000 + (i % 2) * 90, 34, a)
        tag(c, 540, 1745, "ARTICULAÇÃO FRIA", BLU, INK, 60, back_out(prog(t, d * 0.4, 0.3)))


def stamp(n, txt):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.07):
            squatter(c, 330, 0.9, rep(t, 2.4 + n * 0.3))
            ramp(c, t, n, hot=n - 1)
            p = back_out(prog(t, 0.15, 0.3))
            c.save(); c.translate(760, 1000); c.rotate(-0.12); s = max(p, .001); c.scale(s, s)
            rrect(c, -170, -70, 340, 140, 18, YEL); label(c, txt, 0, 26, INK, 70)
            c.restore()
            tag(c, 540, 1745, ("LEVE", "MÉDIO", "SEM CANSAR")[n - 1], GRN, INK, 60, back_out(prog(t, d * 0.4, 0.3)))
    return f


def pronto(c, t, d, b):
    with Cam(c, t, punch=0.07):
        squatter(c, 330, 0.95, rep(t, 2.0))
        ramp(c, t, 4, hot=3)
        check_mark(c, 840, 960, 0.9, prog(t, 0.3, 0.3))
        tag(c, 540, 1745, "AGORA SIM", YEL, INK, 66, back_out(prog(t, d * 0.4, 0.3)))


conc = conc_cards(("50% × 10", "70% × 5", "85% × 2", "AÍ A PESADA"))
cta = cta_factory("AQUECE", "AQUECIMENTO · SUPINO", [("30 KG × 10", WHITE), ("42 KG × 5", WHITE), ("51 KG × 2", None)], ("REGISTRE O AQUECIMENTO", "NO BRIO"))
VIS = {"hook": hook, "risco": risco, "s1": stamp(1, "50% × 10"), "s2": stamp(2, "70% × 5"), "s3": stamp(3, "85% × 2"), "pronto": pronto, "conc": conc, "cta": cta}
SFX = sfx_for(VIS, BEAT_CTA)
for k in ("s1", "s2", "s3"):
    SFX[k] = [(0.0, "whoosh"), (0.15, "clack"), ("0.4d", "pop")]
