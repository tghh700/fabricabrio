"""BRIO 28 — desenvolvimento com a lombar arqueada: erro e correção."""
import math
from brio_kit2 import *
import roteiro_brio_28_desenv as R
BEAT_CTA = R.BEATS[-1]


def rep(t, f=2.2):
    return 0.5 - 0.5 * math.cos(t * f)


def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        u = rep(t); presser(c, 420, 0.95, u, 0.30 * u, u)
        x_mark(c, 820, 1150, 1.0, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "PARA!", RED, WHITE, 72, back_out(prog(t, d * 0.45, 0.3)))


def erro(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t); presser(c, 420, 0.95, u, 0.32 * u, u)
        a = ease_out(prog(t, 0.3, 0.4))
        c.new_path(); c.arc(330, FLOOR_Y - 330, 150, 2.2, 2.2 + 1.4 * a); rgb(c, RED); c.set_line_width(12); c.stroke()
        tag(c, 760, 1100, "LOMBAR ARQUEADA", RED, WHITE, 46, back_out(prog(t, 0.4, 0.3)))
        tag(c, 540, 1745, "QUADRIL PRA FRENTE", YEL, INK, 56, back_out(prog(t, d * 0.45, 0.3)))


def vira(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t); presser(c, 330, 0.85, u, 0.34 * u, u)
        p = ease_out(prog(t, 0.2, 0.4))
        card(c, 770, 1150, 360, 300, CARD, p)
        if p > 0:
            draw_text(c, "SUPINO", 770, 1120, 56, WHITE, "Anton", p, align="center")
            draw_text(c, "INCLINADO?", 770, 1190, 56, YEL, "Anton", p, align="center")
        tag(c, 540, 1745, "A LOMBAR SEGURA O PESO", RED, WHITE, 50, back_out(prog(t, d * 0.45, 0.3)))


def fix1(c, t, d, b):
    with Cam(c, t, punch=0.06):
        presser(c, 420, 0.95, 0.0)
        g = 0.5 + 0.5 * math.sin(t * 6)
        c.new_path(); c.arc(440, FLOOR_Y - 370, 90 + 10 * g, 0, 2 * math.pi); rgb(c, GRN, 0.9); c.set_line_width(10); c.stroke()
        check_mark(c, 800, 1150, 1.0, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "TRAVA E APERTA O GLÚTEO", GRN, INK, 52, back_out(prog(t, d * 0.4, 0.3)))


def fix2(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t, 2.0); presser(c, 420, 0.95, u)
        c.set_dash([20, 16]); cap_line(c, 470, 820, 470, 1250, GRN, 8, 0.9); c.set_dash([])
        check_mark(c, 820, 1150, 1.0, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "SOBE RETA, CORPO PARADO", GRN, INK, 52, back_out(prog(t, d * 0.4, 0.3)))


def menos(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = rep(t, 2.0); presser(c, 300, 0.85, u)
        p = back_out(prog(t, 0.2, 0.35))
        card(c, 760, 1050, 320, 150, CARD, p)
        if p > 0:
            draw_text(c, "−5 KG", 760, 1075, 72, YEL, "Anton", p, align="center")
        p2 = back_out(prog(t, d * 0.45, 0.35))
        card(c, 760, 1260, 320, 150, CARD, p2)
        if p2 > 0:
            draw_text(c, "SENTADO", 760, 1285, 60, WHITE, "Anton", p2, align="center")
        tag(c, 540, 1745, "MAIS OMBRO", GRN, INK, 60, back_out(prog(t, d * 0.6, 0.3)))


conc = conc_cards(("TRONCO PARADO", "ABDÔMEN TRAVADO", "BARRA SOBE RETA", "ARQUEOU? TIRA PESO"))
cta = cta_factory("OMBRO", "CARGA · DESENVOLVIMENTO", [("20 KG × 10", None), ("22 KG × 10", None)], ("ANOTE SUA CARGA NO BRIO", "E SUBA SEM ARQUEAR"))
VIS = {"hook": hook, "erro": erro, "vira": vira, "fix1": fix1, "fix2": fix2, "menos": menos, "conc": conc, "cta": cta}
SFX = sfx_for(VIS, BEAT_CTA)
