"""Helpers próprios do lote (brio 14-17)."""
import math
from engine2 import *
from scenes_short02 import chip

INK = (0.1, 0.1, 0.1)
CARD = (0.20, 0.22, 0.27)
IRON = (0.42, 0.44, 0.50)
BROWN = (0.62, 0.36, 0.22)

def pop_in(c, x, y, p):
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))

def tg(c, x, y, txt, col=None, fg=INK, size=56, p=1.0):
    col = col or YEL
    if p <= 0: return
    pop_in(c, x, y, p)
    font(c, "Anton", size); w = c.text_extents(txt).x_advance + 50
    rrect(c, -w / 2, -size * 0.8, w, size * 1.45, 20, col)
    label(c, txt, 0, size * 0.4, fg, size)
    c.restore()

def flame(c, x, y, s=1.0, col=None, t=0.0):
    col = col or YEL
    w = 1 + 0.06 * math.sin(t * 9)
    c.save(); c.translate(x, y); c.scale(s * w, s)
    c.move_to(0, -120)
    c.curve_to(30, -70, 70, -40, 62, 10)
    c.curve_to(56, 60, 20, 80, 0, 80)
    c.curve_to(-20, 80, -56, 60, -62, 10)
    c.curve_to(-66, -20, -40, -40, -30, -70)
    c.curve_to(-14, -50, -8, -80, 0, -120)
    c.close_path(); rgb(c, col); c.fill()
    disk(c, 0, 35, 28, WHITE, 0.85)
    c.restore()

def clock(c, x, y, r, tm=0.0, hour=6):
    disk(c, x, y, r, WHITE); disk(c, x, y, r * 0.9, (0.12, 0.13, 0.16))
    for i in range(12):
        a = i * math.pi / 6
        cap_line(c, x + math.sin(a) * r * 0.72, y - math.cos(a) * r * 0.72, x + math.sin(a) * r * 0.82, y - math.cos(a) * r * 0.82, WHITE, 5)
    a = (hour % 12) * math.pi / 6
    cap_line(c, x, y, x + math.sin(a) * r * 0.45, y - math.cos(a) * r * 0.45, WHITE, 9)
    a2 = tm * 2
    cap_line(c, x, y, x + math.sin(a2) * r * 0.7, y - math.cos(a2) * r * 0.7, YEL, 6)
    disk(c, x, y, 8, YEL)

def plate(c, x, y, r=130, food=0.0, empty=False):
    disk(c, x, y + 8, r + 6, (0.0, 0.0, 0.0), 0.25)
    disk(c, x, y, r, (0.9, 0.9, 0.88)); disk(c, x, y, r * 0.72, (0.97, 0.97, 0.95))
    if food > 0:
        s = r / 130
        rrect(c, x - 70 * s, y - 40 * s, 80 * s * food, 70 * s * food, 26 * s, BROWN)
        disk(c, x + 50 * s, y - 20 * s, 38 * s * food, WHITE)
        disk(c, x + 30 * s, y + 35 * s, 30 * s * food, GRN)
        disk(c, x - 20 * s, y + 45 * s, 24 * s * food, (0.95, 0.5, 0.2))

def apple(c, x, y, r=60):
    disk(c, x - r * 0.28, y, r * 0.78, RED); disk(c, x + r * 0.28, y, r * 0.78, RED)
    cap_line(c, x, y - r * 0.7, x + 8, y - r * 1.1, BROWN, 9)
    disk(c, x + 28, y - r * 1.0, 14, GRN)

def battery(c, x, y, w, h, level, col):
    rrect(c, x - w / 2, y - h / 2, w, h, 20, WHITE)
    rrect(c, x - w / 2 + 10, y - h / 2 + 10, w - 20, h - 20, 12, (0.1, 0.11, 0.13))
    rrect(c, x - w / 2 + 14, y - h / 2 + 14, max(1, (w - 28) * level), h - 28, 8, col)
    rrect(c, x + w / 2, y - h * 0.2, 18, h * 0.4, 6, WHITE)

def moon(c, x, y, r, col=None):
    col = col or (0.95, 0.93, 0.7)
    disk(c, x, y, r, col); disk(c, x + r * 0.45, y - r * 0.2, r * 0.85, (0.11, 0.12, 0.15))

def warn(c, x, y, s=1.0, col=None):
    col = col or YEL
    poly(c, [(x - 70 * s, y + 55 * s), (x, y - 65 * s), (x + 70 * s, y + 55 * s), (x - 70 * s, y + 55 * s)], col, 16 * s)
    cap_line(c, x, y - 25 * s, x, y + 12 * s, col, 14 * s); disk(c, x, y + 35 * s, 8 * s, col)

def bar(c, x, base, w, h, col, p=1.0, r=14):
    hh = max(2, h * p)
    rrect(c, x - w / 2, base - hh, w, hh, r, col)

def balance(c, x, y, ang, left_fn, right_fn, plank=300):
    """gangorra: fulcro em (x,y); beam gira ang rad; left_fn/right_fn(cx,cy) desenham sobre as pontas"""
    c.new_path(); poly(c, [(x - 60, y + 170), (x, y), (x + 60, y + 170), (x - 60, y + 170)], IRON, 16)
    lx, ly = x - math.cos(ang) * plank, y - math.sin(ang) * plank
    rx, ry = x + math.cos(ang) * plank, y + math.sin(ang) * plank
    cap_line(c, lx, ly, rx, ry, WHITE, 22); disk(c, x, y, 20, YEL)
    left_fn(lx, ly); right_fn(rx, ry)

def dots(c, x, y, n, on, col, r=26, gap=70):
    for i in range(n):
        disk(c, x + i * gap, y, r, col if i < on else (0.28, 0.3, 0.35))

def calendar(c, x, y, cols, rows, cw, ch, filled, col=None, p=1.0):
    col = col or GRN
    for r_ in range(rows):
        for q in range(cols):
            i = r_ * cols + q
            xx, yy = x + q * cw, y + r_ * ch
            rrect(c, xx, yy, cw - 10, ch - 10, 12, (0.2, 0.22, 0.27))
            if i in filled:
                pp = filled[i]
                if pp > 0:
                    rrect(c, xx, yy, cw - 10, ch - 10, 12, col, pp)
                    check_mark(c, xx + (cw - 10) / 2, yy + (ch - 10) / 2 + 2, 0.32, pp, INK)

def dumbbell_h(c, x, y, s=1.0, col=None, ang=0.0):
    col = col or IRON
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    cap_line(c, -60, 0, 60, 0, (0.75, 0.76, 0.8), 14)
    for sd in (-1, 1): rrect(c, sd * 60 - 16, -36, 32, 72, 9, col)
    c.restore()
