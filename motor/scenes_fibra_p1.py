"""FIBRA — piloto 1: a queimação no fim da série."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *

CY = 1060  # centro vertical do conteúdo (entre ~640 e ~1480)


def hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        bend = 0.5 + 0.5 * math.sin(t * 5)
        heat = 0.5 + 0.5 * math.sin(t * 9)
        arm(c, 140, 1080, 1.35, bend, ease_out(prog(t, 0, 0.3)), 0.6 + 0.4 * heat, t)
        # ondas de calor
        for k in range(3):
            a = clamp(prog(t, 0.3 + k * 0.15, 0.3)) * (0.5 + 0.5 * math.sin(t * 6 + k))
            yy = 830 - k * 34 - (t * 40 % 30)
            poly(c, [(360 + k * 40, yy), (385 + k * 40, yy - 18), (410 + k * 40, yy), (435 + k * 40, yy - 18)], PINK, 4, a)
        callout(c, 520, 900, 760, 760, "QUEIMAÇÃO?", ease_out(prog(t, 0.45, 0.5)), PINK, 40)
        dline(c, LEFT, 1420, RIGHT, 1420)
        mono(c, "ESC. 1:4 · VISTA LATERAL", LEFT, 1460, 26, MUTED, ease_out(prog(t, 0.3, 0.4)))


def mito(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        # "ácido lático" riscado
        rrect(c, LEFT + 20, 700, 820, 150, 18, NAVY2, p)
        rrect(c, LEFT + 20, 700, 820, 150, 18); rgb(c, LINE, p); c.set_line_width(3); c.stroke()
        draw_text(c, "ÁCIDO LÁTICO", LEFT + 70, 805, 84, INK, TITLE, p)
        x = ease_out(prog(t, 0.35, 0.3))
        if x > 0:
            cap_line(c, LEFT + 40, 778, LEFT + 40 + 780 * x, 778, PINK, 12)
        # lactato -> combustível
        q = ease_out(prog(t, 0.45 * d, 0.4))
        if q > 0:
            disk(c, 300, 1150, 90 * back_out(q), NAVY2)
            c.new_path(); c.arc(300, 1150, 90 * back_out(q), 0, 6.3); rgb(c, CYAN); c.set_line_width(4); c.stroke()
            mono(c, "LACTATO", 300, 1162, 30, INK, q, align="center")
            arrow_p = ease_out(prog(t, 0.55 * d, 0.35))
            cap_line(c, 410, 1150, 410 + 200 * arrow_p, 1150, CYAN, 6)
            if arrow_p > 0.95:
                poly(c, [(590, 1130), (612, 1150), (590, 1170)], CYAN, 6)
            r = ease_out(prog(t, 0.65 * d, 0.35))
            if r > 0:
                # bateria/combustível
                rrect(c, 650, 1080, 200, 140, 16, NAVY2, r); rrect(c, 650, 1080, 200, 140, 16); rgb(c, GOOD, r); c.set_line_width(5); c.stroke()
                rrect(c, 850, 1125, 18, 50, 4, GOOD, r)
                for k in range(3):
                    rrect(c, 668 + k * 60, 1098, 48, 104, 6, GOOD, r * clamp(prog(t, 0.7 * d + k * 0.12, 0.2)))
                mono(c, "COMBUSTÍVEL", 750, 1290, 32, GOOD, r, align="center")


def ions(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        n = int(4 + 22 * ease(prog(t, 0.2, d * 0.7)))
        fiber(c, LEFT + 20, 1040, RIGHT - LEFT - 40, 300, ease_out(prog(t, 0, 0.4)), acid=0.25 * prog(t, 0.2, d), ions=n, t=t)
        callout(c, 700, 960, 820, 760, "ÍONS H+", ease_out(prog(t, 0.35 * d, 0.5)), PINK, 36, "right") if False else None
        callout(c, 560, 930, 700, 760, "ÍONS DE HIDROGÊNIO", ease_out(prog(t, 0.35 * d, 0.5)), PINK, 32)
        mono(c, f"H+ ACUMULADOS: {n:02d}", LEFT + 20, 1290, 34, MUTED, ease_out(prog(t, 0.2, 0.3)))


def acido(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        v = ease(prog(t, 0.15, d * 0.6))
        gauge(c, 330, 1100, 210, v, ease_out(prog(t, 0, 0.3)))
        brain(c, 790, 860, 1.05, glow=v)
        nerve(c, 520, 1060, 760, 930, t, ease_out(prog(t, 0.35 * d, 0.4)))
        if prog(t, 0.55 * d, 0.2) > 0:
            chip(c, "TÁ PESADO!", 790, 1250, PINK, NAVY, 52, ease_out(prog(t, 0.55 * d, 0.3)))


def some(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        f = ease(prog(t, 0.1, d * 0.75))
        clock(c, 300, 1050, 190, f, ease_out(prog(t, 0, 0.3)))
        mono(c, "~ POUCOS MINUTOS", 300, 1310, 34, CYAN, ease_out(prog(t, 0.2, 0.3)), align="center")
        gauge(c, 770, 1110, 150, 1 - f, ease_out(prog(t, 0, 0.3)))
        if f > 0.9:
            chip(c, "NORMAL", 770, 1280, GOOD, NAVY, 44, ease_out(prog(t, 0.85 * d, 0.3)))


def doms(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        fiber(c, LEFT + 20, 1000, RIGHT - LEFT - 40, 260, ease_out(prog(t, 0, 0.4)), tears=prog(t, 0.25 * d, d * 0.5), t=t)
        callout(c, 420, 980, 560, 770, "MICROLESÕES", ease_out(prog(t, 0.4 * d, 0.5)), PINK, 34)
        q = ease_out(prog(t, 0.15, 0.4))
        rrect(c, LEFT + 20, 1210, 300, 110, 14, NAVY2, q); rrect(c, LEFT + 20, 1210, 300, 110, 14); rgb(c, LINE, q); c.set_line_width(3); c.stroke()
        draw_text(c, "+24 A 72 H", LEFT + 46, 1286, 60, INK, TITLE, q)
        if prog(t, 0.6 * d, 0.2) > 0:
            a = ease_out(prog(t, 0.6 * d, 0.3))
            draw_text(c, "NÃO É ÁCIDO", 520, 1290, 64, PINK, TITLE, a)


def segredo(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        plates = 1 + int(3 * ease(prog(t, 0.45 * d, d * 0.4)))
        lift = math.sin(t * 4) * 18
        barbell_line(c, W / 2 - 40, 840 + lift, 1.05, plates)
        mini_chart(c, LEFT + 20, 1000, RIGHT - LEFT - 40, 360, prog(t, 0.2 * d, d * 0.6))
        mono(c, "CARGA / SEMANA", LEFT + 50, 1050, 28, MUTED, ease_out(prog(t, 0.2, 0.3)))
        fibra_icon(c, RIGHT - 70, 1060, 0.6, ease_out(prog(t, 0.5 * d, 0.3)), t, pulse=True)


def cta(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        fibra_icon(c, W / 2 - 40, 790, 2.2 * back_out(p) if p > 0 else 0.01, 1.0, t, pulse=True)
        chip(c, "COMENTA  CARGA", W / 2 - 40, 1010, PINK, NAVY, 64, ease_out(prog(t, 0.15, 0.35)))
        q = ease_out(prog(t, 0.35 * d, 0.4))
        mono(c, "REGISTRE E ACOMPANHE SEUS", W / 2 - 40, 1150, 32, INK, q, align="center")
        mono(c, "TREINOS GRATUITAMENTE", W / 2 - 40, 1196, 32, INK, q, align="center")
        chip(c, "LINK NA BIO", W / 2 - 40, 1310, CYAN, NAVY, 56, ease_out(prog(t, 0.55 * d, 0.35)))


VIS = dict(hook=hook, mito=mito, ions=ions, acido=acido, some=some, doms=doms, segredo=segredo, cta=cta)
SFX = {
    "hook": [(0.0, "boom"), ("0.45", "pop")],
    "mito": [(0.0, "whoosh"), ("0.35", "clack"), ("0.65d", "ding")],
    "ions": [(0.0, "whoosh"), ("0.35d", "pop")],
    "acido": [(0.0, "whoosh"), ("0.35d", "zip"), ("0.55d", "buzz")],
    "some": [(0.0, "whoosh"), ("0.85d", "ding")],
    "doms": [(0.0, "whoosh"), ("0.6d", "clack")],
    "segredo": [(0.0, "whoosh"), ("0.45d", "clack"), ("0.6d", "clack")],
    "cta": [(0.0, "whoosh"), ("0.15", "pop"), ("0.55d", "ding")],
}
