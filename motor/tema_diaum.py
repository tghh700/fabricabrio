"""Tema DIA UM — caderno: papel pautado, margem vermelha, letra à mão, marca-texto limão e bonecos rabiscados.
Traço "fervendo" (muda a cada 1/8 s) para parecer animação desenhada à mão. Área segura do Reels: y 250–1570."""
import math
import random
import cairo
from engine2 import (W, H, clamp, ease, ease_out, back_out, lerp, prog, mix, rgb, cap_line, disk, rrect, font, wrap,
                     draw_text, Cam, POSES)

PAPER = (0.953, 0.929, 0.878)   # #F3EDE0
RULE = (0.851, 0.812, 0.733)    # #D9CFBB
INK = (0.122, 0.114, 0.102)     # #1F1D1A
LIME = (0.831, 0.961, 0.235)    # #D4F53C
MARGIN = (0.886, 0.447, 0.357)  # #E2725B
MUTED = (0.42, 0.388, 0.345)    # #6B6358
BLUEPEN = (0.20, 0.33, 0.70)
TOP, BOTTOM, LEFT, RIGHT = 250, 1570, 110, W - 140
TITLE = "Permanent Marker"
HAND = "Caveat"


def boil(t):
    return int(t * 8)


def jit(seed, amt=3.0):
    r = random.Random(seed)
    return lambda: r.uniform(-amt, amt)


def background(c, t):
    rgb(c, PAPER); c.paint()
    c.set_line_width(2)
    for y in range(140, H, 64):
        c.move_to(0, y); c.line_to(W, y)
    rgb(c, RULE); c.stroke()
    cap_line(c, 86, 0, 86, H, MARGIN, 3, 0.8)
    # textura leve de papel
    r = random.Random(11)
    for _ in range(140):
        x, y = r.uniform(0, W), r.uniform(0, H)
        disk(c, x, y, r.uniform(0.6, 1.6), INK, 0.035)


def hline(c, pts, col=INK, w=7, t=0.0, seed=0, amt=2.5, a=1.0, p=1.0):
    """linha à mão: pontos com tremidinha que 'ferve'"""
    j = jit(seed * 1000 + boil(t), amt)
    pts = [(x + j(), y + j()) for x, y in pts]
    if p < 1:
        n = max(2, int(len(pts) * p) + 1); pts = pts[:n]
    c.move_to(*pts[0])
    for q in pts[1:]:
        c.line_to(*q)
    rgb(c, col, a); c.set_line_width(w); c.set_line_cap(cairo.LINE_CAP_ROUND); c.set_line_join(cairo.LINE_JOIN_ROUND); c.stroke()


def seg(x1, y1, x2, y2, n=8):
    return [(lerp(x1, x2, i / n), lerp(y1, y2, i / n)) for i in range(n + 1)]


def hcircle(c, x, y, r, col=INK, w=7, t=0.0, seed=0, p=1.0, fill=None):
    j = jit(seed * 1000 + boil(t), 2.5)
    n = 28; pts = []
    for i in range(int(n * p) + 1):
        a = -math.pi / 2 + 2 * math.pi * i / n * 1.04
        pts.append((x + (r + j()) * math.cos(a), y + (r + j()) * math.sin(a)))
    if fill is not None and p >= 1:
        c.move_to(*pts[0])
        for q in pts[1:]:
            c.line_to(*q)
        c.close_path(); rgb(c, fill); c.fill()
    hline(c, pts, col, w, t, seed + 1, 0.0)


def highlight(c, x, y, w, h=46, p=1.0, col=LIME, a=0.95):
    """passada de marca-texto"""
    if p <= 0:
        return
    w_ = w * ease_out(p)
    c.move_to(x, y + 6); c.line_to(x + w_, y); c.line_to(x + w_ - 4, y + h); c.line_to(x + 4, y + h + 5); c.close_path()
    rgb(c, col, a); c.fill()


def headline(c, t, t1, t2):
    """linha 1 em tinta; linha 2 em tinta sobre marca-texto"""
    size = 104
    maxw = RIGHT - LEFT
    l1 = wrap(c, t1, size, maxw, TITLE); l2 = wrap(c, t2, size, maxw, TITLE)
    if len(l1) + len(l2) > 3:
        size = 84; l1 = wrap(c, t1, size, maxw, TITLE); l2 = wrap(c, t2, size, maxw, TITLE)
    y = TOP + 20
    i = 0
    for ln in l1:
        p = ease_out(prog(t, 0.04 + i * 0.07, 0.28))
        if p > 0:
            draw_text(c, ln, LEFT, y + size * 1.0 * (i + 1) + (1 - p) * 40, size, INK, TITLE, p)
        i += 1
    for ln in l2:
        p = ease_out(prog(t, 0.04 + i * 0.07, 0.28))
        yy = y + size * 1.0 * (i + 1)
        font(c, TITLE, size); w = c.text_extents(ln).x_advance
        highlight(c, LEFT - 10, yy - size * 0.62, w + 20, size * 0.62, prog(t, 0.12 + i * 0.07, 0.35))
        if p > 0:
            draw_text(c, ln, LEFT, yy + (1 - p) * 40, size, INK, TITLE, p)
        i += 1
    return y + size * (i + 0.3)


def watermark(c):
    hcircle(c, LEFT + 6, BOTTOM - 48, 22, INK, 4, 0, 5)
    draw_text(c, "1", LEFT - 2, BOTTOM - 36, 34, INK, TITLE)
    draw_text(c, "DIA UM", LEFT + 40, BOTTOM - 34, 34, MUTED, TITLE, 0.9)


def progress(c, T, total, t=0.0):
    y = BOTTOM - 10
    f = clamp(T / total)
    hline(c, seg(LEFT, y, RIGHT, y, 16), RULE, 8, 0, 9, 1.2)
    if f > 0.005:
        hline(c, seg(LEFT, y, LEFT + (RIGHT - LEFT) * f, y, max(2, int(16 * f))), INK, 8, t, 10, 1.2)


def hand(c, s, x, y, size=64, col=INK, a=1.0, align="left"):
    return draw_text(c, s, x, y, size, col, HAND, a, align)


def marker(c, s, x, y, size=80, col=INK, a=1.0, align="left"):
    return draw_text(c, s, x, y, size, col, TITLE, a, align)


def stick(c, x, y, s=1.0, pose="idle", t=0.0, seed=0, face=1, col=INK, w=9, blush=False, mood=None):
    """boneco palito rabiscado usando os ângulos de POSES do motor. pés em (x,y)."""
    p = POSES[pose] if isinstance(pose, str) else pose
    c.save(); c.translate(x, y); c.scale(s * face, s)
    hip = (0, -300); sh = (0, -520)
    lh = 155 * math.cos(math.radians(p[6])) + 150 * math.cos(math.radians(p[6] + p[7]))
    drop = max(0.0, 305 - lh)
    c.translate(0, drop)

    def limb(base, a1, a2, L1, L2, sd):
        r1 = math.radians(a1); j_ = (base[0] + L1 * math.sin(r1), base[1] + L1 * math.cos(r1))
        r2 = math.radians(a1 + a2); e = (j_[0] + L2 * math.sin(r2), j_[1] + L2 * math.cos(r2))
        hline(c, seg(*base, *j_, 4) + seg(*j_, *e, 4)[1:], col, w / s, t, seed + sd, 2.5 / s)
        return e
    limb(hip, p[4], p[5], 155, 150, 1)
    limb(hip, p[6], p[7], 155, 150, 2)
    hline(c, seg(*hip, *sh, 6), col, w / s, t, seed + 3, 2.5 / s)
    limb(sh, p[0], p[1], 120, 110, 4)
    hand_ = limb(sh, p[2], p[3], 120, 110, 5)
    hcircle(c, 0, sh[1] - 85, 62, col, w / s, t, seed + 6, fill=PAPER)
    if mood == "happy":
        c.new_path(); c.arc(0, sh[1] - 80, 30, 0.3, math.pi - 0.3); rgb(c, col); c.set_line_width(6 / s); c.stroke()
    elif mood == "sad":
        c.new_path(); c.arc(0, sh[1] - 50, 26, math.pi + 0.4, 2 * math.pi - 0.4); rgb(c, col); c.set_line_width(6 / s); c.stroke()
    if mood in ("happy", "sad", "neutral"):
        disk(c, -20, sh[1] - 100, 6, col); disk(c, 20, sh[1] - 100, 6, col)
    if blush:
        disk(c, -36, sh[1] - 72, 12, MARGIN, 0.5); disk(c, 36, sh[1] - 72, 12, MARGIN, 0.5)
    c.restore()
    return (x + hand_[0] * s * face, y + (hand_[1] + drop) * s)


def checkbox(c, x, y, size=54, checked=0.0, t=0.0, seed=0):
    pts = [(x, y), (x + size, y), (x + size, y + size), (x, y + size), (x, y)]
    hline(c, pts, INK, 5, t, seed, 1.8)
    if checked > 0:
        hline(c, [(x + 10, y + size * 0.5), (x + size * 0.42, y + size - 10), (x + size + 14, y - 12)], MARGIN, 9, t, seed + 1, 1.5,
              p=checked)


def harrow(c, x1, y1, x2, y2, p=1.0, t=0.0, seed=0, col=INK, w=7):
    xe, ye = lerp(x1, x2, p), lerp(y1, y2, p)
    hline(c, seg(x1, y1, xe, ye, 8), col, w, t, seed)
    if p > 0.2:
        a = math.atan2(ye - y1, xe - x1); hd = 34
        hline(c, [(xe - hd * math.cos(a - .5), ye - hd * math.sin(a - .5)), (xe, ye), (xe - hd * math.cos(a + .5), ye - hd * math.sin(a + .5))],
              col, w, t, seed + 1)


def tally(c, x, y, n, t=0.0, seed=0, p=1.0, h=90):
    """marcas de contagem (||||/)"""
    shown = int(n * p + 0.999)
    for i in range(shown):
        g, k = divmod(i, 5)
        gx = x + g * 120
        if k < 4:
            hline(c, seg(gx + k * 22, y, gx + k * 22 + 4, y + h, 3), INK, 6, t, seed + i)
        else:
            hline(c, seg(gx - 12, y + h * 0.8, gx + 84, y + h * 0.15, 3), MARGIN, 6, t, seed + i)


def dumbbell(c, x, y, s=1.0, t=0.0, seed=0, ang=0.0):
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    hline(c, seg(-80, 0, 80, 0, 4), INK, 9, t, seed)
    for side in (-1, 1):
        rr = [(side * 70, -38), (side * 104, -38), (side * 104, 38), (side * 70, 38), (side * 70, -38)]
        hline(c, rr, INK, 8, t, seed + side + 3)
    c.restore()


def clock(c, x, y, r, frac, t=0.0, seed=0):
    hcircle(c, x, y, r, INK, 7, t, seed, fill=PAPER)
    a = -math.pi / 2 + 2 * math.pi * frac
    hline(c, seg(x, y, x + (r - 24) * math.cos(a), y + (r - 24) * math.sin(a), 3), MARGIN, 7, t, seed + 2)
    hline(c, seg(x, y, x, y - r * 0.5, 3), INK, 7, t, seed + 3)
