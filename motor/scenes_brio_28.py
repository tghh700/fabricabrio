"""BRIO 28 — desenvolvimento com a lombar arqueada. Vista frontal (movimento) + quadro com a vista lateral (coluna)."""
import math
from brio_kit2 import *
import roteiro_brio_28_desenv as R
BEAT_CTA = R.BEATS[-1]
FX, IX, IY = 340, 800, 1230


def rep(t, f=2.2):
    return 0.5 - 0.5 * math.cos(t * f)


def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        u = rep(t); front_presser(c, FX, 0.9, u, hip=u)
        spine_inset(c, IX, IY, u, t, ease_out(prog(t, 0.1, 0.3)))
        x_mark(c, IX + 130, IY - 190, 0.6, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "PARA!", RED, WHITE, 72, back_out(prog(t, d * 0.45, 0.3)))


def erro(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t); front_presser(c, FX, 0.9, u, hip=u)
        spine_inset(c, IX, IY, 0.4 + 0.6 * u, t)
        a = ease_out(prog(t, 0.3, 0.4))
        arrow(c, IX - 60, IY + 60, IX + 60, IY + 60, RED, 10, a)
        tag(c, IX, IY + 320, "LOMBAR ARQUEADA", RED, WHITE, 40, back_out(prog(t, 0.4, 0.3)))
        tag(c, 540, 1745, "QUADRIL PRA FRENTE", YEL, INK, 56, back_out(prog(t, d * 0.45, 0.3)))


def vira(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t); front_presser(c, FX, 0.9, u, hip=1.0)
        spine_inset(c, IX, IY, 1.0, t)
        p = back_out(prog(t, 0.3, 0.35))
        card(c, IX, IY + 330, 340, 110, CARD, p)
        if p > 0:
            draw_text(c, "SUPINO INCLINADO?", IX, IY + 345, 34, YEL, "Anton", p, align="center")
        tag(c, 540, 1745, "A LOMBAR SEGURA O PESO", RED, WHITE, 50, back_out(prog(t, d * 0.45, 0.3)))


def fix1(c, t, d, b):
    with Cam(c, t, punch=0.06):
        g = 0.5 + 0.5 * math.sin(t * 6)
        front_presser(c, FX, 0.9, 0.0, ring=GRN)
        spine_inset(c, IX, IY, 1 - ease(prog(t, 0.2, d * 0.5)), t)
        check_mark(c, IX + 130, IY - 190, 0.6, prog(t, 0.5 * d, 0.3))
        tag(c, 540, 1745, "TRAVA E APERTA O GLÚTEO", GRN, INK, 52, back_out(prog(t, d * 0.4, 0.3)))


def fix2(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t, 2.0); bx, hy = front_presser(c, FX, 0.9, u)
        c.set_dash([20, 16]); cap_line(c, FX, 760, FX, 1180, GRN, 8, 0.9); c.set_dash([])
        spine_inset(c, IX, IY, 0.0, t, ok=GRN)
        check_mark(c, IX + 130, IY - 190, 0.6, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "SOBE RETA, CORPO PARADO", GRN, INK, 52, back_out(prog(t, d * 0.4, 0.3)))


def menos(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t, 2.0); front_presser(c, FX, 0.9, u)
        p = back_out(prog(t, 0.2, 0.35))
        card(c, IX, 1050, 300, 150, CARD, p)
        if p > 0:
            draw_text(c, "−5 KG", IX, 1075, 72, YEL, "Anton", p, align="center")
        p2 = back_out(prog(t, d * 0.45, 0.35))
        card(c, IX, 1260, 300, 150, CARD, p2)
        if p2 > 0:
            draw_text(c, "SENTADO", IX, 1285, 60, WHITE, "Anton", p2, align="center")
        tag(c, 540, 1745, "MAIS OMBRO", GRN, INK, 60, back_out(prog(t, d * 0.6, 0.3)))


conc = conc_cards(("TRONCO PARADO", "ABDÔMEN TRAVADO", "BARRA SOBE RETA", "ARQUEOU? TIRA PESO"))
cta = cta_factory("OMBRO", "DESENVOLVIMENTO", [("20 KG × 10", None), ("22 KG × 10", None)], ("ANOTE SUA CARGA NO BRIO", "E SUBA SEM ARQUEAR"))
VIS = {"hook": hook, "erro": erro, "vira": vira, "fix1": fix1, "fix2": fix2, "menos": menos, "conc": conc, "cta": cta}
SFX = sfx_for(VIS, BEAT_CTA)
