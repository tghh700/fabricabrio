"""BRIO 27 — rosca com embalo: erro encenado e correção."""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_27_rosca as R
BEAT_CTA = R.BEATS[-1]


def lifter(c, x, s, u, lean=0.0, hip=0.0, face=1):
    """boneco fazendo rosca; u 0..1 = subida; lean = inclinação do tronco para trás (rad); hip = quadril empurrando à frente"""
    c.save(); c.translate(x + hip * 40 * face, FLOOR_Y); c.rotate(-lean * face); c.translate(-x, -FLOOR_Y)
    hx, hy = chunky(c, x, FLOOR_Y, s, pose_mix("curl_down", "curl_up", u), face=face)
    dumbbell(c, hx, hy, 0.8 * s / 0.9, 0.0)
    c.restore()
    return x + 20 * s * face, FLOOR_Y - 390 * s  # cotovelo (sem a inclinação)


def swing(t, f=2.4):
    ph = (t * f) % (2 * math.pi)
    u = 0.5 - 0.5 * math.cos(ph)
    return u, 0.28 * math.sin(ph) ** 2 if math.sin(ph) > 0 else 0.0


def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        u, ln = swing(t)
        lifter(c, 400, 0.95, u, ln, ln * 2)
        x_mark(c, 800, 1150, 1.0, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "PARA!", RED, WHITE, 72, back_out(prog(t, d * 0.45, 0.3)))


def erro(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u, ln = swing(t)
        lifter(c, 420, 0.95, u, ln, ln * 2)
        for i in range(3):
            a = ease_out(prog(t, 0.3 + i * 0.2, 0.3))
            c.new_path(); c.arc(420, FLOOR_Y - 300, 230 + i * 40, -2.6, -2.6 + 0.9 * a); rgb(c, YEL, 0.8 - i * 0.2); c.set_line_width(10); c.stroke()
        tag(c, 540, 1745, "SOBE NO EMBALO", YEL, INK, 60, back_out(prog(t, d * 0.45, 0.3)))


def carona(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u, ln = swing(t)
        lifter(c, 270, 0.8, u, ln, ln * 2)
        for i, (lab, v, col) in enumerate((("LOMBAR + OMBRO", 0.85, RED), ("BÍCEPS", 0.25, GRN))):
            p = back_out(prog(t, 0.2 + i * 0.5, 0.3))
            y = 1080 + i * 260
            card(c, 760, y, 470, 210, CARD, p)
            if p > 0:
                mono(c, lab, 760, y - 40, 28, WHITE, p)
                rrect(c, 560, y + 10, 400, 40, 20, (0.14, 0.15, 0.18))
                rrect(c, 560, y + 10, max(40, 400 * v * ease(prog(t, 0.4 + i * 0.5, 0.6))), 40, 20, col)
        tag(c, 540, 1745, "BÍCEPS DE CARONA", RED, WHITE, 58, back_out(prog(t, d * 0.5, 0.3)))


def cotovelo(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 - 0.5 * math.cos(t * 2.4)
        ex, ey = lifter(c, 420, 0.95, u)
        pk = ease_out(prog(t, 0.3, 0.3))
        if pk > 0:
            c.new_path(); c.arc(ex, ey, 70, 0, 6.3); rgb(c, YEL, pk); c.set_line_width(10); c.stroke()
            arrow(c, ex + 330, ey - 40, ex + 110, ey, YEL, 14, p=pk)
        check_mark(c, 820, 1100, 0.9, prog(t, d * 0.4, 0.3))
        tag(c, 540, 1745, "COTOVELO PARADO", YEL, INK, 60, back_out(prog(t, d * 0.45, 0.3)))


def desce(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cyc = t % 4.0
        u = ease(cyc / 1.0) if cyc < 1.0 else 1 - (cyc - 1.0) / 3.0
        lifter(c, 360, 0.95, u)
        up = cyc < 1.0
        n = 1 if up else min(3, int(cyc - 1.0) + 1)
        card(c, 790, 1150, 330, 330, CARD, back_out(prog(t, 0.1, 0.3)))
        mono(c, "SOBE" if up else "DESCE", 790, 1040, 30, GREY, prog(t, 0.1, 0.3))
        txt(c, str(n), 790, 1240, 190, GRN if up else YEL, prog(t, 0.1, 0.3))
        tag(c, 540, 1745, "1 SOBE · 3 DESCE", YEL, INK, 60, back_out(prog(t, d * 0.4, 0.3)))


def menos(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pa = back_out(prog(t, 0.1, 0.3)); pb = back_out(prog(t, 0.6, 0.3))
        card(c, 300, 1150, 400, 420, CARD, pa)
        card(c, 780, 1150, 400, 420, CARD, pb)
        if pa > 0:
            dumbbell(c, 300, 1130, 2.2 * pa, 0.0); txt(c, "16 KG", 300, 1300, 70, WHITE, pa)
            x_mark(c, 300, 1130, 0.9, prog(t, 0.5, 0.3))
        if pb > 0:
            dumbbell(c, 780, 1130, 1.6 * pb, 0.0); txt(c, "10 KG", 780, 1300, 70, YEL, pb)
            check_mark(c, 780, 1130, 0.8, prog(t, 1.0, 0.3))
        tag(c, 540, 1745, "MENOS PESO, MAIS BÍCEPS", GRN, INK, 54, back_out(prog(t, d * 0.5, 0.3)))


def conc(c, t, d, b):
    with Cam(c, t, punch=0.06):
        its = ("SEM EMBALO", "COTOVELO PARADO", "DESCE EM 3 S", "AÍ SOBE A CARGA")
        for i, s in enumerate(its):
            p = back_out(prog(t, 0.15 + i * d * 0.15, 0.3))
            y = 960 + i * 175
            card(c, 540, y, 760, 140, CARD, p)
            if p > 0:
                check_mark(c, 220, y, 0.5, prog(t, 0.3 + i * d * 0.15, 0.3))
                draw_text(c, s, 300, y + 22, 60, WHITE if i < 3 else YEL, "Anton", p)
        u = 0.5 - 0.5 * math.cos(t * 2.4)


def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="ROSCA", app_title="CARGA · ROSCA", app_lines=[("10 KG × 10", WHITE), ("12 KG × 10", YEL)],
             chart=False, lines=("REGISTRE A CARGA DA ROSCA", "E VEJA ELA SUBIR"))


VIS = {"hook": hook, "erro": erro, "carona": carona, "cotovelo": cotovelo, "desce": desce, "menos": menos, "conc": conc, "cta": cta}
SFX = {
    "hook": [(0.0, "boom"), (0.35, "buzz"), ("0.45d", "pop")],
    "erro": [(0.0, "whoosh"), (0.3, "swish"), (0.5, "swish"), ("0.45d", "pop")],
    "carona": [(0.0, "whoosh"), (0.2, "pop"), (0.7, "pop"), ("0.5d", "pop")],
    "cotovelo": [(0.0, "whoosh"), (0.3, "pop"), ("0.4d", "ding"), ("0.45d", "pop")],
    "desce": [(0.0, "whoosh"), (1.0, "tick"), (2.0, "tick"), (3.0, "tick"), ("0.4d", "pop")],
    "menos": [(0.0, "whoosh"), (0.1, "pop"), (0.5, "buzz"), (0.6, "pop"), (1.0, "ding"), ("0.5d", "pop")],
    "conc": [(0.0, "whoosh"), (0.3, "tick"), ("0.3d", "tick"), ("0.45d", "tick"), ("0.6d", "tick")],
    "cta": cta_sfx(BEAT_CTA, "bubble"),
}
