"""Kit próprio do lote BRIO 22-26 (primitivas extras)."""
import math
from engine2 import *
from scenes_short02 import chip
INK = (0.1, 0.1, 0.1); CARD = (0.20, 0.22, 0.27); IRON = (0.42, 0.44, 0.50); STEEL = (0.75, 0.76, 0.8)

def pop(c, x, y, p):
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))

def tag(c, x, y, txt, col=None, fg=INK, size=60, p=1.0):
    col = col or YEL
    if p <= 0: return
    pop(c, x, y, p)
    font(c, "Anton", size); w = c.text_extents(txt).x_advance + 50
    rrect(c, -w / 2, -size * 0.8, w, size * 1.45, 20, col)
    label(c, txt, 0, size * 0.4, fg, size)
    c.restore()

def card(c, x, y, w, h, col=CARD, p=1.0, r=26):
    if p <= 0: return
    pop(c, x, y, p); rrect(c, -w / 2, -h / 2, w, h, r, col); c.restore()

def txt(c, s, x, y, size=50, col=WHITE, a=1.0):
    draw_text(c, s, x, y, size, col, "Anton", a, align="center")

def mono(c, s, x, y, size=26, col=GREY, a=1.0):
    draw_text(c, s, x, y, size, col, "Space Mono", a, align="center", spacing=3)

def dumbbell(c, x, y, s=1.0, ang=0.0, col=None):
    col = col or IRON
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    cap_line(c, -44, 0, 44, 0, STEEL, 14)
    for sd in (-1, 1): rrect(c, sd * 44 - 15, -32, 30, 64, 9, col)
    c.restore()

def clock(c, x, y, r, t, spd=1.0, col=None, hand_col=None):
    col = col or WHITE
    disk(c, x, y, r, (0.08, 0.09, 0.11)); c.new_path(); c.arc(x, y, r, 0, 6.2832); rgb(c, col); c.set_line_width(10); c.stroke()
    for i in range(12):
        a = i * math.pi / 6
        cap_line(c, x + (r - 8) * math.sin(a), y - (r - 8) * math.cos(a), x + (r - 26) * math.sin(a), y - (r - 26) * math.cos(a), GREY, 5)
    a = t * spd * 2 * math.pi / 3
    cap_line(c, x, y, x + r * 0.78 * math.sin(a), y - r * 0.78 * math.cos(a), hand_col or YEL, 10)
    a2 = a / 12
    cap_line(c, x, y, x + r * 0.5 * math.sin(a2), y - r * 0.5 * math.cos(a2), col, 12)
    disk(c, x, y, 12, hand_col or YEL)

def calendar(c, x, y, cols, rows, cell, marks, t, t0=0.0, gap=10, hot=None, mark_col=None):
    """grade de dias; marks = nº de células marcadas até agora (progressivo em t)"""
    w = cols * cell + (cols - 1) * gap; h = rows * cell + (rows - 1) * gap
    n = 0
    for r in range(rows):
        for k in range(cols):
            cx = x - w / 2 + cell / 2 + k * (cell + gap); cy = y - h / 2 + cell / 2 + r * (cell + gap)
            rrect(c, cx - cell / 2, cy - cell / 2, cell, cell, 14, CARD)
            if n < marks:
                ts = t0 + n * 0.16
                p = back_out(prog(t, ts, 0.25))
                if p > 0:
                    rrect(c, cx - cell / 2, cy - cell / 2, cell, cell, 14, mark_col or YEL, min(p, 1))
                    check_mark(c, cx, cy, cell / 130, prog(t, ts + 0.1, 0.2), INK)
            n += 1

def notebook(c, x, y, w, h, p=1.0):
    if p <= 0: return
    pop(c, x, y, p)
    rrect(c, -w / 2, -h / 2, w, h, 24, (0.93, 0.92, 0.89))
    rrect(c, -w / 2, -h / 2, 60, h, 24, (0.8, 0.78, 0.72))
    for i in range(1, 6): cap_line(c, -w / 2 + 90, -h / 2 + i * h / 6.5, w / 2 - 30, -h / 2 + i * h / 6.5, (0.7, 0.72, 0.78), 3)
    c.restore()

def tape(c, x, y, w, t):
    """fita métrica horizontal com marcas"""
    rrect(c, x - w / 2, y - 30, w, 60, 8, YEL)
    for i in range(0, 21):
        xx = x - w / 2 + 20 + i * (w - 40) / 20
        cap_line(c, xx, y - 30, xx, y - (6 if i % 5 else -6), INK, 3)

def bars(c, x, y, w, h, vals, t, t0=0.0, cols=None):
    n = len(vals); bw = w / (n * 1.5)
    cap_line(c, x - w / 2, y, x + w / 2, y, (1, 1, 1), 4, 0.3)
    for i, v in enumerate(vals):
        p = ease_out(prog(t, t0 + i * 0.2, 0.5))
        col = (cols[i] if cols else YEL)
        bx = x - w / 2 + (i + 0.5) * w / n
        rrect(c, bx - bw / 2, y - h * v * p, bw, h * v * p + 1, 10, col)

def thought(c, x, y, w, h, p=1.0, col=None):
    col = col or (0.93, 0.92, 0.89)
    if p <= 0: return
    pop(c, x, y, p)
    rrect(c, -w / 2, -h / 2, w, h, 40, col)
    c.restore()

def torso_arm(c, x, y, s, ang, col=None):
    """braço de perfil estilizado (só um músculo): útil p/ cenas de bíceps/tríceps"""
    pass

def ell(c, x, y, rx, ry, col, a=1.0, ang=0.0):
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(rx, ry); c.new_path(); c.arc(0, 0, 1, 0, 6.2832); c.restore()
    rgb(c, col, a); c.fill()

def arm_view(c, x, y, s=1.0, bi=None, tri=None, bend=0.9, heads=None, pulse=0.0):
    """braço de perfil (frente = direita). (x,y) = ombro. bi/tri = cor de destaque ou None.
    heads: None ou (long, lat, med) cores dos 3 feixes do tríceps."""
    c.save(); c.translate(x, y); c.scale(s, s)
    skin = L_FRONT
    # antebraço (sai do cotovelo em (0,330))
    ex, ey = 0, 330
    fx, fy = 300 * math.sin(bend), 330 - 300 * math.cos(bend)
    cap_line(c, ex, ey, ex + fx, fy + 0, skin, 90)
    disk(c, ex + fx, fy, 48, skin)
    # braço
    cap_line(c, 0, 0, 0, 330, skin, 150)
    disk(c, 0, 0, 82, L_BACK)
    # tríceps (atrás = esquerda)
    k = 1 + pulse
    tcol = tri or L_BACK
    if heads:
        ell(c, -62, 150, 58 * k, 150, heads[0], 1)
        ell(c, -30, 215, 52 * k, 100, heads[1], 1)
        ell(c, 5, 245, 50, 70, heads[2], 0.9)
    else:
        ell(c, -58, 150, 56 * k, 160, tcol, 1)
    bcol = bi or L_BACK
    ell(c, 62, 130, 52 * (1 + (pulse if bi else 0)), 100, bcol, 1)
    disk(c, 0, 330, 62, skin)
    c.restore()
    return (x + 0, y + 330 * s)
