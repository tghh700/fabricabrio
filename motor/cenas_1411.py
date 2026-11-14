"""Biblioteca de cenas do lote BRIO 14/11 (32–37): boneco + adereços animados + tag inferior."""
import math
from brio_kit2 import *

PX, PY = 700, 1000   # centro da zona de adereços (direita do boneco)


def fig(c, t, pose="idle", x=330, s=0.85, face=1, bob=14):
    chunky(c, x, FLOOR_Y, s, pose, face=face, bob=bob * math.sin(t * 3.2))


# ---------- adereços (todos animados por t) ----------
def p_q(c, t, x=PX, y=PY, col=YEL):
    pul = 1 + 0.08 * math.sin(t * 5)
    draw_text(c, "?", x, y + 150 * pul, 420 * pul, col, "Anton", 1.0, align="center")

def p_x(c, t, x=PX, y=PY, s=1.3, t0=0.3): x_mark(c, x, y, s, prog(t, t0, 0.3))
def p_ok(c, t, x=PX, y=PY, s=1.3, t0=0.3): check_mark(c, x, y, s, prog(t, t0, 0.3))

def p_pain(c, t, x=PX, y=PY, n=5, col=RED):
    for k in range(n):
        a = k * 2.4 + t * 2
        spark(c, x + 120 * math.cos(a) * (0.6 + 0.4 * math.sin(t * 3 + k)), y + 100 * math.sin(a), 0.7, t + k * 0.3, col)

def p_dumb(c, t, x=PX, y=PY, s=2.0, up=True):
    dumbbell(c, x, y - (40 * math.sin(t * 3) if up else 0), s, 0.0)

def p_chart(c, t, x=PX - 230, y=PY - 230, w=460, h=400, t0=0.2, dur=1.4, col=GRN):
    chart_up(c, x, y, w, h, ease_out(prog(t, t0, dur)), col)

def p_bars(c, t, vals, labels, x=PX, y=PY + 200, w=420, h=420, cols=None, t0=0.15):
    bars(c, x, y, w, h, vals, t, t0, cols)
    n = len(vals)
    for i, lab in enumerate(labels):
        bx = x - w / 2 + (i + 0.5) * w / n
        draw_text(c, lab, bx, y + 48, 28, GREY, "Space Mono", 1.0, align="center")

def p_warn(c, t, x=PX, y=PY, s=1.0, col=RED):
    pul = 1 + 0.05 * math.sin(t * 6)
    c.save(); c.translate(x, y); c.scale(s * pul, s * pul)
    poly(c, [(0, -170), (160, 110), (-160, 110), (0, -170)], col, 22)
    rrect(c, -14, -70, 28, 100, 10, col); disk(c, 0, 64, 15, col)
    c.restore()

def p_clock(c, t, x=PX, y=PY, r=190, spd=1.0): clock(c, x, y, r, t, spd)

def p_bed(c, t, x=PX, y=PY + 120, s=0.9): bed(c, x, y, s, t)

def p_sun(c, t, x=PX - 150, y=PY - 80, r=95):
    for i in range(10):
        a = i * math.pi / 5 + t * 0.6
        cap_line(c, x + (r + 26) * math.cos(a), y + (r + 26) * math.sin(a), x + (r + 62) * math.cos(a), y + (r + 62) * math.sin(a), YEL, 12)
    disk(c, x, y, r, YEL)

def p_moon(c, t, x=PX + 130, y=PY + 110, r=85):
    disk(c, x, y, r, (0.86, 0.87, 0.93))
    for (dx, dy, rr) in ((-25, -20, 18), (20, 15, 24), (-10, 38, 12)):
        disk(c, x + dx, y + dy, rr, (0.72, 0.74, 0.82))
    for k in range(3):
        a = 0.5 + 0.5 * math.sin(t * 4 + k * 2)
        draw_text(c, "✦", x - 120 + k * 140, y - 140 - k * 25, 30, WHITE, "Anton", a, align="center")

def p_cal(c, t, cols=7, rows=2, marks=2, x=PX, y=PY, cell=70, hot=None, col=None):
    calendar(c, x, y, cols, rows, cell, marks, t, 0.2, 10, hot, col)

def p_list(c, t, items, x=PX, y=PY - 160, w=470, gap=150, hot=0):
    for i, s in enumerate(items):
        p = back_out(prog(t, 0.15 + i * 0.25, 0.3))
        card(c, x, y + i * gap, w, 120, YEL if i == hot else CARD, p)
        if p > 0:
            draw_text(c, f"{i + 1}", x - w / 2 + 40, y + i * gap + 20, 60, INK if i == hot else YEL, "Anton", p)
            draw_text(c, s, x - w / 2 + 100, y + i * gap + 20, 46, INK if i == hot else WHITE, "Anton", p)

def p_gauge(c, t, label_, v0, v1, x=PX, y=PY, w=70, h=430, col=GRN, t0=0.2, dur=1.6):
    """barra vertical que muda de v0 para v1"""
    rrect(c, x - w / 2, y - h / 2, w, h, 22, CARD)
    v = lerp(v0, v1, ease(prog(t, t0, dur)))
    rrect(c, x - w / 2 + 8, y + h / 2 - 8 - (h - 16) * v, w - 16, (h - 16) * v, 16, mix(RED, col, v) if v1 < v0 else col)
    draw_text(c, label_, x, y + h / 2 + 60, 34, GREY, "Space Mono", 1.0, align="center")

def p_notebook(c, t, x=PX, y=PY, lines=(), w=470, h=560):
    notebook(c, x, y, w, h, back_out(prog(t, 0.1, 0.3)))
    for i, s in enumerate(lines):
        p = prog(t, 0.4 + i * 0.3, 0.3)
        draw_text(c, s, x - w / 2 + 100, y - h / 2 + 110 + i * 90, 44, (0.12, 0.12, 0.14), "Anton", p)

def p_arrow(c, t, x1, y1, x2, y2, col=YEL, t0=0.25): arrow(c, x1, y1, x2, y2, col, 16, ease_out(prog(t, t0, 0.4)))

def p_big(c, t, s, x=PX, y=PY, size=190, col=YEL):
    pul = 1 + 0.04 * math.sin(t * 4)
    p = back_out(prog(t, 0.15, 0.3))
    draw_text(c, s, x, y + size * 0.35, size * pul, col, "Anton", p, align="center")


def breathe(fn, amp=0.018):
    """respiração lenta de câmera (zoom +-1,8%): evita quadro congelado em cena parada"""
    def f(c, t, d, b):
        c.save(); c.translate(540, 1250); z = 1 + amp * math.sin(t * 1.7); c.scale(z, z)
        c.translate(-540 + 14 * math.sin(t * 1.1), -1250 + 9 * math.sin(t * 1.3))
        fn(c, t, d, b); c.restore()
    return f


def scene(pose, props, tagtxt, tagcol=None, tagfg=None, face=1, fx=330, fs=0.85, punch=0.06, fig_on=True):
    tagcol = tagcol or YEL; tagfg = tagfg or INK
    def f(c, t, d, b):
        with Cam(c, t, punch=punch):
            if fig_on:
                fig(c, t, pose, fx, fs, face)
            for p in props:
                p(c, t)
            tag(c, 540, 1745, tagtxt, tagcol, tagfg, 58, back_out(prog(t, d * 0.4, 0.3)))
    return breathe(f)

def W(fn, *a, **k):
    return lambda c, t: fn(c, t, *a, **k)

def finish(R, VIS, conc_items, cta_word, cta_title, cta_lines, cta_text):
    VIS["conc"] = breathe(conc_cards(conc_items))
    VIS["cta"] = breathe(cta_factory(cta_word, cta_title, cta_lines, cta_text))
    SFX = sfx_for(VIS, R.BEATS[-1])
    return SFX
