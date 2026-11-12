"""BRIO 30 — respiração e abdômen travado no agachamento."""
import math
from brio_kit2 import *
import roteiro_brio_30_respira as R
BEAT_CTA = R.BEATS[-1]


def rep(t, f=2.0):
    return 0.5 - 0.5 * math.cos(t * f)


def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        dd = 0.55 + 0.35 * math.sin(t * 2.4)
        squatter(c, 420, 0.95, dd)
        x_mark(c, 820, 1100, 0.9, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "PERDE FORÇA?", RED, WHITE, 66, back_out(prog(t, d * 0.45, 0.3)))


def erro(c, t, d, b):
    with Cam(c, t, punch=0.06):
        dd = rep(t, 2.2)
        sy = squatter(c, 400, 0.95, dd)
        for k in range(3):  # ar escapando
            f = (t * 1.3 + k / 3) % 1
            disk(c, 470 + 160 * f, sy + 40 - 60 * f, 16 * (1 - f) + 4, WHITE, 0.6 * (1 - f))
        tag(c, 780, 1050, "TRONCO AMOLECE", RED, WHITE, 46, back_out(prog(t, 0.35, 0.3)))
        tag(c, 540, 1745, "SOLTOU O AR NA DESCIDA", RED, WHITE, 52, back_out(prog(t, d * 0.45, 0.3)))


def puxa(c, t, d, b):
    with Cam(c, t, punch=0.06):
        bel = ease(prog(t, 0.2, d * 0.5))
        squatter(c, 420, 0.95, 0.04 + 0.04 * math.sin(t * 3), belly=bel)
        arrow(c, 760, 1000, 520, 1240, YEL, 14, ease_out(prog(t, 0.2, 0.4)))
        tag(c, 540, 1745, "AR PRA BARRIGA", YEL, INK, 62, back_out(prog(t, d * 0.4, 0.3)))


def trava(c, t, d, b):
    with Cam(c, t, punch=0.07):
        squatter(c, 420, 0.95, 0.06 + 0.05 * math.sin(t * 3), belly=0.9 + 0.1 * math.sin(t * 6))
        p = back_out(prog(t, 0.3, 0.3))
        c.save(); c.translate(780, 1150); s = max(p, .001); c.scale(s, s)
        rrect(c, -150, -60, 300, 120, 30, GRN); label(c, "CINTO", 0, 26, INK, 64)
        c.restore()
        tag(c, 540, 1745, "TRAVA O ABDÔMEN", GRN, INK, 60, back_out(prog(t, d * 0.4, 0.3)))


def solta(c, t, d, b):
    with Cam(c, t, punch=0.06):
        dd = rep(t, 1.8)
        squatter(c, 400, 0.95, dd, belly=1.0 if dd > 0.08 or (t % 3.5) < 1.7 else 0.3)
        tag(c, 790, 1050, "SEGURA…", YEL, INK, 50, back_out(prog(t, 0.2, 0.3)))
        tag(c, 540, 1745, "SOLTA PERTO DO FINAL", GRN, INK, 56, back_out(prog(t, d * 0.45, 0.3)))


def longa(c, t, d, b):
    with Cam(c, t, punch=0.06):
        dd = rep(t, 2.2)
        squatter(c, 360, 0.9, dd, belly=0.4 + 0.6 * dd)
        for i in range(4):
            q = back_out(prog(t, 0.2 + i * 0.25, 0.3))
            card(c, 790, 930 + i * 120, 260, 92, CARD, q)
            if q > 0:
                draw_text(c, f"REP {i + 1} · AR", 790, 945 + i * 120, 34, WHITE, "Space Mono", q, align="center")
        tag(c, 540, 1745, "RESPIRA EM CIMA", YEL, INK, 60, back_out(prog(t, d * 0.45, 0.3)))


conc = conc_cards(("AR PRA BARRIGA", "ABDÔMEN TRAVADO", "DESCE E SOBE FIRME", "SOLTA NO FINAL"))
cta = cta_factory("FIRME", "AGACHAMENTO", [("60 KG × 8", WHITE), ("65 KG × 8", None)], ("REGISTRE SEU AGACHAMENTO", "E VEJA A CARGA SUBIR"))
VIS = {"hook": hook, "erro": erro, "puxa": puxa, "trava": trava, "solta": solta, "longa": longa, "conc": conc, "cta": cta}
SFX = sfx_for(VIS, BEAT_CTA)
