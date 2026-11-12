"""Tema FIBRA — prancha técnica / raio-x. Tudo dentro da área segura do Reels (y 250–1570, margem direita 140)."""
import math
import cairo
from engine2 import (W, H, clamp, ease, ease_out, back_out, lerp, prog, mix, rgb, cap_line, poly, disk, rrect, font, wrap,
                     draw_text, Cam)

NAVY = (0.027, 0.094, 0.180)      # #07182E
GRID = (0.071, 0.188, 0.310)      # #12304F
NAVY2 = (0.043, 0.137, 0.259)     # #0B2342
CYAN = (0.220, 0.882, 0.824)      # #38E1D2
PINK = (1.0, 0.361, 0.478)        # #FF5C7A
INK = (0.949, 0.969, 0.980)       # #F2F7FA
MUTED = (0.561, 0.659, 0.749)     # #8FA8BF
LINE = (0.114, 0.267, 0.439)      # #1D4470
GOOD = (0.45, 0.92, 0.55)
TOP, BOTTOM, LEFT, RIGHT = 250, 1570, 60, W - 140
TITLE = "Barlow Condensed"
MONO = "JetBrains Mono"


def background(c, t):
    rgb(c, NAVY); c.paint()
    c.set_line_width(2)
    step = 54
    for x in range(0, W + 1, step):
        c.move_to(x, 0); c.line_to(x, H)
    for y in range(0, H + 1, step):
        c.move_to(0, y); c.line_to(W, y)
    rgb(c, GRID, 0.9); c.stroke()
    # varredura de raio-x descendo devagar
    sy = (t * 160) % (H + 400) - 200
    g = cairo.LinearGradient(0, sy - 120, 0, sy + 10)
    g.add_color_stop_rgba(0, *CYAN, 0.0); g.add_color_stop_rgba(1, *CYAN, 0.07)
    c.set_source(g); c.rectangle(0, sy - 120, W, 130); c.fill()
    # vinheta
    v = cairo.RadialGradient(W / 2, H / 2, 300, W / 2, H / 2, 1250)
    v.add_color_stop_rgba(0, 0, 0, 0, 0); v.add_color_stop_rgba(1, 0, 0, 0, 0.45)
    c.set_source(v); c.paint()


def headline(c, t, t1, t2, fig=None):
    """título em Barlow Condensed: linha 1 branca, linha 2 ciano; rótulo de figura em mono acima"""
    y = TOP + 30
    if fig:
        pk = ease_out(prog(t, 0, 0.25))
        draw_text(c, fig, LEFT, y, 30, CYAN, MONO, pk, spacing=3)
    size = 118
    maxw = RIGHT - LEFT
    lines = [(l, INK) for l in wrap(c, t1, size, maxw, TITLE)] + [(l, CYAN) for l in wrap(c, t2, size, maxw, TITLE)]
    if len(lines) > 3:
        size = 92
        lines = [(l, INK) for l in wrap(c, t1, size, maxw, TITLE)] + [(l, CYAN) for l in wrap(c, t2, size, maxw, TITLE)]
    yy = y + 20
    for i, (ln, col) in enumerate(lines):
        p = ease_out(prog(t, 0.04 + i * 0.07, 0.28))
        if p <= 0:
            continue
        font(c, TITLE, size, bold=True)
        draw_text(c, ln, LEFT, yy + size * 0.95 * (i + 1) + (1 - p) * 50, size, col, TITLE, p)
    return yy + size * 0.95 * len(lines)


def fibra_icon(c, x, y, s=1.0, a=1.0, t=0.0, pulse=False):
    c.save(); c.translate(x, y); c.scale(s, s); c.translate(-60, -60)
    w = 4.5
    cap_line(c, 10, 60, 22, 60, CYAN, 5, a); cap_line(c, 98, 60, 110, 60, CYAN, 5, a)
    for k in (-42, -22, 22, 42):
        c.move_to(22, 60); c.curve_to(45, 60 + k * 1.1, 75, 60 + k * 1.1, 98, 60)
        rgb(c, CYAN, a); c.set_line_width(w); c.set_line_cap(cairo.LINE_CAP_ROUND); c.stroke()
    pa = a * (0.75 + 0.25 * math.sin(t * 8)) if pulse else a
    cap_line(c, 22, 60, 98, 60, PINK, 5, pa)
    c.restore()


def watermark(c):
    fibra_icon(c, LEFT + 18, BOTTOM - 46, 0.28, 0.9)
    font(c, TITLE, 30, bold=True)
    draw_text(c, "FIBRA", LEFT + 44, BOTTOM - 36, 30, MUTED, TITLE, 0.9, spacing=4)


def progress(c, T, total):
    y = BOTTOM - 14
    cap_line(c, LEFT, y, RIGHT, y, GRID, 6)
    cap_line(c, LEFT, y, LEFT + (RIGHT - LEFT) * clamp(T / total), y, CYAN, 6)


# ---------------------------------------------------------------- primitivas de prancha
def dline(c, x1, y1, x2, y2, col=LINE, w=2, dash=(8, 10), a=1.0):
    c.set_dash(dash); cap_line(c, x1, y1, x2, y2, col, w, a); c.set_dash([])


def mono(c, s, x, y, size=30, col=INK, a=1.0, align="left"):
    return draw_text(c, s, x, y, size, col, MONO, a, align)


def callout(c, x0, y0, x1, y1, txt, p, col=INK, size=30, side="right"):
    """bolinha no ponto + linha em L + texto mono"""
    if p <= 0:
        return
    disk(c, x0, y0, 7 * min(1, p * 2), col)
    q = clamp(p * 1.4)
    xm = lerp(x0, x1, q)
    cap_line(c, x0, y0, x0, lerp(y0, y1, q), col, 2.5)
    if q > 0.5:
        cap_line(c, x0, y1, lerp(x0, x1, (q - 0.5) * 2), y1, col, 2.5)
    if p > 0.7:
        a = clamp((p - 0.7) / 0.3)
        if side == "right":
            mono(c, txt, x1 + 14, y1 + 10, size, col, a)
        else:
            mono(c, txt, x1 - 14, y1 + 10, size, col, a, align="right") if False else _mono_right(c, txt, x1 - 14, y1 + 10, size, col, a)


def _mono_right(c, s, x, y, size, col, a):
    font(c, MONO, size); w = c.text_extents(s).x_advance
    draw_text(c, s, x - w, y, size, col, MONO, a)


def chip(c, s, x, y, col=CYAN, txt=NAVY, size=44, p=1.0, align="center"):
    if p <= 0:
        return
    font(c, TITLE, size, bold=True); w = c.text_extents(s).x_advance + 44; h = size * 1.35
    x0 = x - w / 2 if align == "center" else x
    c.save(); c.translate(x0 + w / 2, y); s_ = max(back_out(p), 0.001); c.scale(s_, s_)
    rrect(c, -w / 2, -h / 2, w, h, 10, col)
    draw_text(c, s, -w / 2 + 22, size * 0.36, size, txt, TITLE)
    c.restore()


def arm(c, x, y, s=1.0, bend=0.0, p=1.0, hl=1.0, t=0.0):
    """braço em vista lateral: ombro em (x,y); bend 0 = estendido, 1 = flexionado. bíceps aceso em rosa."""
    c.save(); c.translate(x, y); c.scale(s, s)
    ang = math.radians(lerp(10, 125, ease(bend)))
    # braço (úmero) horizontal até o cotovelo
    ex, ey = 330, 40
    c.set_line_join(cairo.LINE_JOIN_ROUND)
    # contorno do braço
    c.move_to(0, -55); c.curve_to(120, -70, 230, -45, ex, ey - 50)
    c.line_to(ex + 10, ey + 50); c.curve_to(230, 70, 120, 75, 0, 60); c.close_path()
    rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    # antebraço
    c.save(); c.translate(ex, ey); c.rotate(-ang)
    c.move_to(0, -42); c.curve_to(110, -48, 220, -32, 290, -20); c.line_to(290, 22); c.curve_to(220, 34, 110, 48, 0, 46); c.close_path()
    rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    disk(c, 300, 0, 34, NAVY2, p); c.new_path(); c.arc(300, 0, 34, 0, 2 * math.pi); rgb(c, CYAN, p); c.stroke()
    c.restore()
    # bíceps (incha com a flexão)
    bulge = 30 + 38 * ease(bend)
    c.move_to(70, -40); c.curve_to(140, -40 - bulge, 230, -40 - bulge, 300, -20)
    c.curve_to(230, -6, 140, -6, 70, -40); c.close_path()
    rgb(c, PINK, 0.85 * hl * p); c.fill_preserve(); rgb(c, PINK, p); c.set_line_width(2.5); c.stroke()
    for k in range(3):  # estrias
        yy = -30 - bulge * (0.25 + k * 0.22)
        c.move_to(100, -34 - k * 4); c.curve_to(160, yy, 230, yy, 285, -22)
        rgb(c, NAVY, 0.7 * hl * p); c.set_line_width(1.5); c.stroke()
    c.restore()


def fiber(c, x, y, w, h, p=1.0, acid=0.0, tears=0.0, t=0.0, ions=0):
    """corte de uma fibra muscular (cilindro) com miofibrilas; acid tinge de rosa; ions = nº de íons H+"""
    c.save(); c.translate(x, y)
    w_ = w * ease_out(p)
    rrect(c, 0, -h / 2, w_, h, h / 2, mix(NAVY2, (0.30, 0.10, 0.18), acid))
    rrect(c, 0, -h / 2, w_, h, h / 2); rgb(c, CYAN); c.set_line_width(3); c.stroke()
    for k in range(1, 6):
        yy = -h / 2 + h * k / 6
        c.move_to(h * 0.3, yy); c.line_to(w_ - h * 0.3, yy)
        rgb(c, mix(CYAN, PINK, acid), 0.35); c.set_line_width(2); c.stroke()
    if tears > 0:
        import random
        rnd = random.Random(7)
        for k in range(9):
            tx = rnd.uniform(0.15, 0.85) * w_; ty = rnd.uniform(-0.35, 0.35) * h
            a = clamp(tears * 3 - k * 0.25)
            poly(c, [(tx - 14, ty - 10), (tx, ty + 4), (tx + 12, ty - 8)], PINK, 4, a)
    if ions:
        import random
        rnd = random.Random(3)
        for k in range(ions):
            ix = rnd.uniform(0.08, 0.92) * w_ + math.sin(t * 3 + k) * 8
            iy = rnd.uniform(-0.38, 0.38) * h + math.cos(t * 2.6 + k * 1.7) * 6
            disk(c, ix, iy, 13, PINK, 0.95)
            font(c, MONO, 16, bold=True); draw_text(c, "H+", ix - 11, iy + 6, 16, NAVY, MONO)
    c.restore()


def gauge(c, x, y, r, val, p=1.0, label_="pH", lo="7,1", hi="6,6"):
    """mostrador semicircular: val 0..1 (0 = normal, 1 = ácido)"""
    c.save(); c.translate(x, y)
    c.new_path(); c.arc(0, 0, r, math.pi, 2 * math.pi); rgb(c, LINE); c.set_line_width(22); c.stroke()
    c.new_path(); c.arc(0, 0, r, math.pi, math.pi + math.pi * clamp(val) * p)
    rgb(c, mix(CYAN, PINK, val)); c.set_line_width(22); c.stroke()
    a = math.pi + math.pi * clamp(val) * p
    cap_line(c, 0, 0, (r - 40) * math.cos(a), (r - 40) * math.sin(a), INK, 8)
    disk(c, 0, 0, 16, INK)
    mono(c, label_, 0, 70, 40, INK, align="center")
    mono(c, lo, -r, 60, 28, MUTED, align="center"); mono(c, hi, r, 60, 28, MUTED, align="center")
    c.restore()


def nerve(c, x1, y1, x2, y2, t, p=1.0, col=PINK):
    """impulso nervoso em zigue-zague correndo da fibra ao cérebro"""
    n = 18; pts = []
    for i in range(n + 1):
        f = i / n
        if f > p:
            break
        xx = lerp(x1, x2, f); yy = lerp(y1, y2, f)
        off = (14 if i % 2 else -14) if 0 < i < n else 0
        nx, ny = -(y2 - y1), (x2 - x1); L = math.hypot(nx, ny) or 1
        pts.append((xx + nx / L * off, yy + ny / L * off))
    if len(pts) > 1:
        poly(c, pts, col, 5)
    # pulso viajando
    f = (t * 1.4) % 1
    if f < p:
        disk(c, lerp(x1, x2, f), lerp(y1, y2, f), 12, INK)


def brain(c, x, y, s=1.0, glow=0.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-90, 20)
    c.curve_to(-120, -40, -70, -100, -10, -90); c.curve_to(40, -120, 110, -80, 100, -20)
    c.curve_to(130, 20, 90, 70, 40, 60); c.curve_to(10, 90, -50, 80, -60, 50); c.curve_to(-100, 60, -110, 40, -90, 20)
    c.close_path(); rgb(c, mix(NAVY2, (0.35, 0.12, 0.2), glow)); c.fill_preserve(); rgb(c, CYAN); c.set_line_width(3); c.stroke()
    for (a, b, cc, d) in ((-60, -40, -20, -60), (0, -70, 20, -20), (40, -50, 70, -10), (-40, 10, 0, 30)):
        c.move_to(a, b); c.curve_to(cc, d, cc + 10, d + 20, a + 40, b + 30); rgb(c, CYAN, 0.6); c.set_line_width(2); c.stroke()
    c.restore()


def clock(c, x, y, r, frac, p=1.0):
    c.new_path(); c.arc(x, y, r, 0, 2 * math.pi); rgb(c, NAVY2); c.fill_preserve(); rgb(c, CYAN); c.set_line_width(4); c.stroke()
    c.move_to(x, y); c.arc(x, y, r - 10, -math.pi / 2, -math.pi / 2 + 2 * math.pi * frac * p); c.close_path()
    rgb(c, CYAN, 0.25); c.fill()
    a = -math.pi / 2 + 2 * math.pi * frac * p
    cap_line(c, x, y, x + (r - 24) * math.cos(a), y + (r - 24) * math.sin(a), INK, 6)
    disk(c, x, y, 9, INK)


def barbell_line(c, x, y, s=1.0, plates=2, col=CYAN):
    c.save(); c.translate(x, y); c.scale(s, s)
    cap_line(c, -260, 0, 260, 0, col, 8)
    for side in (-1, 1):
        for k in range(plates):
            px = side * (170 + k * 36)
            rrect(c, px - 14, -80 + k * 8, 28, 160 - k * 16, 6, NAVY2)
            rrect(c, px - 14, -80 + k * 8, 28, 160 - k * 16, 6); rgb(c, col); c.set_line_width(3); c.stroke()
    c.restore()


def mini_chart(c, x, y, w, h, p, col=CYAN):
    rrect(c, x, y, w, h, 14, NAVY2); rrect(c, x, y, w, h, 14); rgb(c, LINE); c.set_line_width(2); c.stroke()
    vals = [0.2, 0.32, 0.3, 0.45, 0.52, 0.66, 0.8]
    n = len(vals); bw = (w - 60) / n
    for i, v in enumerate(vals):
        q = clamp(p * n - i)
        bh = (h - 70) * v * ease_out(q)
        rrect(c, x + 30 + i * bw + 8, y + h - 30 - bh, bw - 16, bh, 6, mix(LINE, col, 0.4 + 0.6 * (i == n - 1)))
