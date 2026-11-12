"""Cenas do BRIO 18 — quanto tempo pro supino subir 10 kg (e helpers reaproveitados por 19-21)."""
import math
from engine2 import *
from scenes_short02 import chip
import roteiro_brio_18 as R
from cta_brio import cta_brio, cta_sfx

INK = (0.1, 0.1, 0.1)
CARD = (0.20, 0.22, 0.27)
DARK = (0.08, 0.09, 0.11)

def pop_in(c, x, y, p):
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))

def tag(c, x, y, txt, col=None, fg=INK, size=60, p=1.0):
    col = col or YEL
    if p <= 0: return
    pop_in(c, x, y, p)
    font(c, "Anton", size); w = c.text_extents(txt).x_advance + 50
    rrect(c, -w / 2, -size * 0.8, w, size * 1.45, 20, col)
    label(c, txt, 0, size * 0.4, fg, size)
    c.restore()

def card(c, x, y, w, h, title, val, col=WHITE, p=1.0, vsize=96, bg=DARK):
    if p <= 0: return
    pop_in(c, x, y, p)
    rrect(c, -w / 2, -h / 2, w, h, 30, bg)
    draw_text(c, title, 0, -h / 2 + 52, 28, GREY, "Space Mono", align="center", spacing=4)
    label(c, val, 0, h / 2 - 48, col, vsize)
    c.restore()

def bench_lifter(c, x, y, s, u, plate=1.0, col=None, shake=0.0):
    """supino visto de lado. u: 0 = barra no peito, 1 = braços esticados. y = chão."""
    col = col or YEL
    c.save(); c.translate(x, y); c.scale(s, s)
    shadow(c, 300, 0, 380)
    rrect(c, -90, -230, 700, 60, 18, CARD)
    cap_line(c, 0, -170, 0, 0, (0.3, 0.32, 0.38), 26); cap_line(c, 520, -170, 520, 0, (0.3, 0.32, 0.38), 26)
    # corpo
    cap_line(c, 60, -285, 330, -285, L_BODY, 100)
    poly(c, [(330, -285), (500, -330), (520, -60)], L_FRONT, 52)
    disk(c, -20, -300, 62, L_BODY)
    sh = (90, -290); hy = -290 - 110 - 170 * u
    hand = (90 + shake, hy)
    poly(c, [sh, (90, (sh[1] + hy) / 2), hand], L_FRONT, 44)
    r = 110 * plate
    disk(c, hand[0], hand[1], r, col); disk(c, hand[0], hand[1], r * 0.62, mix(col, INK, 0.35)); disk(c, hand[0], hand[1], r * 0.18, (0.75, 0.76, 0.8))
    c.restore()
    return (x + (90 + shake) * s, y + hy * s)

def steps(c, x0, y0, n, w, hstep, a, col=None, p=1.0, grow=1.0):
    """degraus crescentes"""
    for i in range(n):
        pi = back_out(prog(p, i / n * 0.7, 0.3))
        if pi <= 0: continue
        h = hstep * (i + 1) * grow
        c.save(); c.translate(x0 + i * w, y0); c.scale(1, max(pi, .001))
        rrect(c, 0, -h, w - 14, h, 14, col or (YEL if i == n - 1 else CARD))
        c.restore()

def calendar(c, x, y, cols, rows, cell, t, start=0.0, mark=None, col=None, gap=10):
    n = 0
    for r in range(rows):
        for k in range(cols):
            pc = back_out(prog(t, start + n * 0.04, 0.25)); n += 1
            if pc <= 0: continue
            cx = x + k * (cell + gap); cy = y + r * (cell + gap)
            pop_in(c, cx + cell / 2, cy + cell / 2, pc)
            hit = mark is not None and mark(n - 1)
            rrect(c, -cell / 2, -cell / 2, cell, cell, 14, (col or YEL) if hit else CARD)
            c.restore()

def CTAB(): return R.BEATS[-1]

# ------------------------------------------------------------ cenas
def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        per = 2.0; u = (t % per) / per
        up = ease(math.sin(clamp(u / 0.9) * math.pi)) if u < 0.9 else 0
        bench_lifter(c, 120, 1640, 1.15, up, plate=1.0 + 0.25 * prog(t, 0.5, 1.0))
        pr = back_out(prog(t, 0.3, 0.3))
        if pr > 0:
            pop_in(c, 800, 1000, pr); label(c, "+10 KG", 0, 0, YEL, 150); c.restore()
            pop_in(c, 800, 1160, pr); label(c, "?", 0, 60, WHITE, 190); c.restore()
        # régua que ninguém mede
        if t > d * 0.5:
            p = prog(t, d * 0.5, 0.3)
            tag(c, 540, 1770, "QUASE NINGUÉM MEDE", CARD, WHITE, 52, back_out(p))
            ring(c, 800, 1090, 220, t, YEL)

def beginner(c, t, d, b):
    with Cam(c, t, punch=0.06):
        p = prog(t, 0.1, 1.6)
        steps(c, 90, 1560, 5, 180, 150, 1, p=p)
        # boneco subindo
        k = min(4, int(p * 5)); hx = 90 + k * 180 + 80
        chunky(c, 220 + p * 560, 1560 - 150 * (p * 5) - 0, 0.0001, "idle")
        chunky(c, hx, 1560 - 150 * (k + 1) , 0.5, pose_mix("idle", "cheer", prog(t, 1.7, 0.3)), t=t)
        card(c, 270, 960, 380, 220, "EM POUCOS MESES", "+10 KG", YEL, back_out(prog(t, 0.4, 0.3)), 90)
        arrow(c, 480, 1040, 760, 1180, YEL, 14, p=prog(t, 0.8, 0.5))
        chip(c, "SOBE RÁPIDO", 540, 1745, YEL, INK, 62, t=t, start=d * 0.5)

def why(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # a mesma trajetória fica mais limpa a cada semana
        for i in range(4):
            y = 940 + i * 190
            pi = ease_out(prog(t, 0.2 + i * 0.35, 0.4))
            draw_text(c, f"SEM {i + 1}", 90, y + 22, 40, GREY, "Anton", pi)
            wob = (3 - i) * 22
            c.set_dash([]); c.new_path()
            for k in range(41):
                xx = 320 + k * 16 * pi * 1.0
                yy = y + math.sin(k * 0.9 + i) * wob * (k / 40) + 0
                (c.move_to if k == 0 else c.line_to)(xx, yy)
            rgb(c, YEL if i == 3 else WHITE, 0.9 if pi > 0 else 0); c.set_line_width(9); c.set_line_cap(1); c.stroke()
        ps = back_out(prog(t, d * 0.55, 0.3))
        tag(c, 540, 1745, "MAIS EFICIENTE", YEL, INK, 62, ps)
        if ps > 0: check_mark(c, 920, 1130, 1.0, prog(t, d * 0.6, 0.3))

def inter(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cols = 4
        calendar(c, 130, 880, cols, 3, 190, t, 0.1, mark=lambda n: n == 11, gap=18)
        draw_text(c, "12 MESES", 540, 1530, 70, WHITE, "Anton", prog(t, 0.6, 0.3), align="center")
        card(c, 540, 1640, 300, 150, "", "+10 KG", YEL, back_out(prog(t, d * 0.55, 0.3)), 76)
        chunky(c, 920, FLOOR_Y + 30, 0.5, "tired", dark=True, t=t)

def normal(c, t, d, b):
    with Cam(c, t, punch=0.06):
        p = prog(t, 0.1, 1.8)
        # curva achatando e passos diminuindo
        c.new_path(); n = int(60 * p)
        pts = []
        for k in range(n + 1):
            x = 100 + k * 14; y = 1620 - 650 * (1 - math.exp(-k / 14.0))
            pts.append((x, y))
        if len(pts) > 1: poly(c, pts, YEL, 14)
        for i, kk in enumerate((6, 20, 40, 58)):
            if kk <= n:
                x, y = pts[kk]; disk(c, x, y, 18, WHITE)
        draw_text(c, "LIMITE", 880, 930, 44, RED, "Anton", prog(t, 0.8, 0.3), align="center")
        c.set_dash([18, 14]); cap_line(c, 100, 985, 980, 985, RED, 5, 0.8 * prog(t, 0.8, 0.3)); c.set_dash([])
        tag(c, 540, 1745, "PASSO MENOR", CARD, WHITE, 60, back_out(prog(t, d * 0.45, 0.3)))
        if t > d * 0.55: check_mark(c, 900, 1500, 1.2, prog(t, d * 0.55, 0.3))

def small(c, t, d, b):
    with Cam(c, t, punch=0.06):
        barbell(c, 540, 1380, 1.0, 2)
        # anilhas pequenas entrando de cada lado
        for sd in (-1, 1):
            pp = back_out(prog(t, 0.3, 0.35))
            if pp > 0:
                pop_in(c, 540 + sd * 345, 1380, pp); rrect(c, -10, -55, 20, 110, 6, WHITE); c.restore()
                draw_text(c, "+1 KG", 540 + sd * 345, 1250, 40, WHITE, "Anton", pp, align="center")
        n = 8 + (1 if t > d * 0.55 else 0)
        counter_y = 960
        pop_in(c, 540, counter_y, back_out(prog(t, 0.1, 0.3)))
        rrect(c, -300, -90, 600, 180, 30, DARK)
        label(c, f"{n}", -150, 55, WHITE if n == 8 else YEL, 130)
        draw_text(c, "REPS", 30, 30, 50, GREY, "Space Mono")
        c.restore()
        if t > d * 0.55: ring(c, 540 - 150, counter_y, 110, t, YEL)
        chip(c, "OU +1 REPETIÇÃO", 540, 1700, YEL, INK, 60, t=t, start=d * 0.5)

def stall(c, t, d, b):
    with Cam(c, t, punch=0.06, shake=4):
        sh = 5 * math.sin(t * 40) * prog(t, 0.6, 0.2)
        bench_lifter(c, 120, 1640, 1.15, 0.12 + 0.05 * math.sin(t * 3), plate=1.35, col=RED, shake=sh)
        tag(c, 760, 960, "PESADO DEMAIS", RED, WHITE, 52, back_out(prog(t, 0.1, 0.3)))
        pc = back_out(prog(t, d * 0.4, 0.3))
        if pc > 0:
            pop_in(c, 800, 1160, pc); rrect(c, -200, -80, 400, 160, 28, DARK); label(c, "5/10", 0, 45, RED, 110); c.restore()
        x_mark(c, 930, 1380, 1.0, prog(t, d * 0.6, 0.3))
        chip(c, "TRAVOU", 540, 1770, RED, WHITE, 66, t=t, start=d * 0.65)

def math_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        items = [("0,5 KG", WHITE, 0.1), ("× 52 SEMANAS", GREY, 0.7), ("= 26 KG", YEL, 1.5)]
        for i, (s_, col, st) in enumerate(items):
            p = back_out(prog(t, st, 0.3))
            if p > 0:
                pop_in(c, 540, 960 + i * 150, p); label(c, s_, 0, 0, col, 100 if i < 2 else 130); c.restore()
        # barras de semana enchendo
        n = int(52 * ease(prog(t, 0.7, 1.8)))
        for k in range(52):
            x = 70 + (k % 26) * 36; y = 1480 + (k // 26) * 70
            on = k < n
            rrect(c, x, y, 28, 52, 8, YEL if on else CARD)
        chart_up(c, 220, 1600, 640, 170, ease(prog(t, 1.0, 2.0)), YEL)

def measure(c, t, d, b):
    with Cam(c, t, punch=0.06):
        card(c, 300, 1050, 440, 300, "HOJE", "60 KG", WHITE, back_out(prog(t, 0.1, 0.3)), 100)
        pq = back_out(prog(t, d * 0.4, 0.3))
        card(c, 780, 1050, 440, 300, "SEMANA PASSADA", "?? KG", GREY, pq, 100)
        if pq > 0: ring(c, 780, 1050, 250, t, YEL)
        pp = prog(t, d * 0.55, 0.4)
        arrow(c, 540, 1300, 540, 1480, YEL, 16, p=pp)
        phone(c, 540, 1620, 0.5) if False else None
        tag(c, 540, 1640, "ANOTA TUDO", YEL, INK, 64, back_out(prog(t, d * 0.6, 0.3)))
        chunky(c, 160, FLOOR_Y + 80, 0.35, pose_mix("idle", "scratch", prog(t, 0.2, 0.3)), t=t)

def lower(c, t, d, b):
    with Cam(c, t, punch=0.06):
        base = 1620
        for i, (nm, hh, col, x) in enumerate((("SUPINO", 420, CARD, 330), ("PERNA", 720, YEL, 750))):
            p = ease_out(prog(t, 0.15 + i * 0.35, 0.7))
            rrect(c, x - 140, base - hh * p, 280, hh * p, 24, col)
            draw_text(c, nm, x, base + 64, 52, WHITE if i == 0 else YEL, "Anton", align="center")
        pa = prog(t, 1.2, 0.5)
        arrow(c, 750, 900, 750, 880 - 0, YEL, 0.1, p=0) if False else None
        draw_text(c, "+ CARGA", 750, 880, 56, YEL, "Anton", prog(t, 1.2, 0.3), align="center")
        draw_text(c, "MÚSCULO MAIOR", 540, 800, 0 + 1, YEL, "Anton", 0) if False else None
        chip(c, "MÚSCULOS MAIORES", 540, 1780, YEL, INK, 56, t=t, start=d * 0.55)

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="save", app_title="SUPINO",
             app_lines=[("HOJE  60 KG", None), ("SEM. PASSADA 57,5", None)], app_big="+2,5 KG", app_big_label="EVOLUÇÃO", chart=True)

VIS = {"hook": hook, "beginner": beginner, "why": why, "inter": inter, "normal": normal, "small": small,
       "stall": stall, "math": math_, "measure": measure, "lower": lower, "cta": cta}
_BC = R.BEATS[-1]
SFX = {
    "hook": [(0.0, "boom"), (0.3, "pop"), ("0.5d", "pop")],
    "beginner": [(0.0, "whoosh"), (0.4, "pop"), (0.8, "swish"), (1.7, "ding")],
    "why": [(0.0, "whoosh"), (0.2, "tick"), (0.55, "tick"), (0.9, "tick"), (1.25, "tick"), ("0.55d", "pop")],
    "inter": [(0.0, "whoosh"), (0.6, "pop"), ("0.55d", "pop")],
    "normal": [(0.0, "whoosh"), (0.8, "pop"), ("0.45d", "pop"), ("0.55d", "ding")],
    "small": [(0.0, "whoosh"), (0.3, "pop"), ("0.5d", "click"), ("0.5d+0.1", "pop")],
    "stall": [(0.0, "whoosh"), (0.1, "pop"), ("0.4d", "pop"), ("0.6d", "buzz"), ("0.65d", "pop")],
    "math": [(0.0, "whoosh"), (0.1, "pop"), (0.7, "pop"), (1.5, "ding")],
    "measure": [(0.0, "whoosh"), (0.1, "pop"), ("0.4d", "pop"), ("0.6d", "pop")],
    "lower": [(0.0, "whoosh"), (0.15, "swish"), (0.5, "swish"), (1.2, "pop"), ("0.55d", "pop")],
    "cta": cta_sfx(_BC, "save"),
}
