"""Cenas do BRIO 05 — dupla progressão: quando subir a carga."""
import math, random
from engine2 import *
from scenes_short02 import chip

CARD = (0.20, 0.22, 0.27)
INK = (0.1, 0.1, 0.1)

def pop_in(c, x, y, p):
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))

def die(c, x, y, size, n, ang=0.0):
    PIPS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)],
            4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
            6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}
    c.save(); c.translate(x, y); c.rotate(ang)
    rrect(c, -size / 2, -size / 2, size, size, size * 0.18, WHITE)
    for px, py in PIPS[n]: disk(c, px * size * 0.27, py * size * 0.27, size * 0.09, INK)
    c.restore()

def counter(c, x, y, n, s=1.0, col=None, a=1.0, title="REPS"):
    col = col or WHITE
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -150, -170, 300, 300, 36, (0.08, 0.09, 0.11))
    draw_text(c, title, 0, -115, 30, GREY, "Space Mono", align="center", spacing=6)
    label(c, str(n), 0, 95, col, 200, a)
    c.restore()

def tag(c, x, y, txt, col=None, fg=INK, size=64):
    col = col or YEL
    font(c, "Anton", size); w = c.text_extents(txt).x_advance + 60
    rrect(c, x - w / 2, y - size * 0.8, w, size * 1.45, 22, col)
    label(c, txt, x, y + size * 0.4, fg, size)

# ------------------------------------------------------------ cenas
def hook(c, t, d, b):
    with Cam(c, t, punch=0.10):
        barbell(c, 640, 1560, 0.75, 2)
        label(c, "?? KG", 640, 1440, GREY, 70, a=prog(t, 0.3, 0.3))
        hx, hy = chunky(c, 230, FLOOR_Y, 0.85, pose_mix("idle", "reach", prog(t, 0.05, 0.25)), face=1)
        # dado rolando
        f = ease_out(prog(t, 0.3, 1.1))
        if t < 0.3:
            die(c, hx + 30, hy - 20, 90, 3)
        else:
            x = lerp(hx + 30, 760, f); y = lerp(hy - 20, 1000, f) - math.sin(f * math.pi) * 180
            n = 1 + int(t * 14) % 6 if f < 1 else 5
            die(c, x, y, 140, n, ang=(1 - f) * 8)
            if f >= 1: ring(c, 760, 1000, 130, t, YEL)
        if t > d * 0.45:
            p = back_out(prog(t, d * 0.45, 0.3))
            pop_in(c, 330, 940, p); label(c, "?", 0, 60, YEL, 200); c.restore()

def name(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # degraus
        p1 = back_out(prog(t, 0.1, 0.35)); p2 = back_out(prog(t, d * 0.45, 0.35))
        if p1 > 0:
            c.save(); c.translate(320, FLOOR_Y); c.scale(1, max(p1, .001))
            rrect(c, -220, -200, 440, 200, 24, CARD); c.restore()
            if p1 > 0.9:
                label(c, "1", 320, FLOOR_Y - 65, GREY, 90)
                label(c, "REPETIÇÕES ↑", 320, FLOOR_Y + 90, WHITE, 60)
        if p2 > 0:
            c.save(); c.translate(760, FLOOR_Y); c.scale(1, max(p2, .001))
            rrect(c, -220, -420, 440, 420, 24, YEL); c.restore()
            if p2 > 0.9:
                label(c, "2", 760, FLOOR_Y - 160, INK, 120)
                label(c, "PESO ↑", 760, FLOOR_Y + 90, YEL, 60)
        # boneco sobe os degraus
        jump = ease(prog(t, d * 0.6, 0.5))
        if p1 > 0.9:
            bx = lerp(300, 760, jump)
            by = lerp(FLOOR_Y - 200, FLOOR_Y - 420, jump) - math.sin(jump * math.pi) * 120
            pose = "cheer" if jump >= 1 else ("walk1" if 0 < jump < 1 else "idle")
            chunky(c, bx, by, 0.55, pose, face=1)
        if t > d * 0.3:
            c.new_path(); c.move_to(440, 1360); c.curve_to(470, 1200, 540, 1150, 620, 1170)
            rgb(c, YEL); c.set_line_width(14); c.set_line_cap(cairo.LINE_CAP_ROUND)
            pa = prog(t, d * 0.3, 0.4)
            if pa > 0: c.stroke()
            arrow(c, 580, 1160, 630, 1175, YEL, 14, p=1) if pa >= 1 else None

def example(c, t, d, b):
    with Cam(c, t, punch=0.06):
        reps = clamp(int((t - 0.4) / max(0.01, (d * 0.75 - 0.4) / 6)) + 1, 0, 6) if t > 0.4 else 0
        reps = int(reps)
        ph = ((t - 0.4) / max(0.01, (d * 0.75 - 0.4) / 6)) % 1 if 0 < reps < 6 else 0
        lift = math.sin(ph * math.pi) * 90
        barbell(c, 540, 1080 - lift, 1.15, 2)
        p = back_out(prog(t, 0.1, 0.3))
        pop_in(c, 540, 900, p); tag(c, 0, 0, "60 KG"); c.restore()
        counter(c, 540, 1460, reps, 1.0, YEL if reps == 6 else WHITE)
        if reps == 6: ring(c, 540, 1420, 200, t, YEL)
        label(c, "SUPINO", 540, 1720, GREY, 56)

def weeks(c, t, d, b):
    with Cam(c, t, punch=0.06):
        starts = [0.1, d * 0.35, d * 0.65]
        for i, (r, st) in enumerate(zip([6, 7, 8], starts)):
            p = ease_out(prog(t, st, 0.35))
            if p <= 0: continue
            y = 1000 + i * 250
            x = lerp(1300, 540, p)
            last = i == 2
            rrect(c, x - 450, y - 100, 900, 200, 30, YEL if last else CARD)
            fg = INK if last else WHITE
            draw_text(c, f"SEM {i + 1}", x - 400, y + 30, 46, fg, "Space Mono", spacing=4)
            label(c, "60 KG", x + 20, y + 32, fg, 72)
            label(c, str(r), x + 330, y + 52, fg if last else YEL, 130)
        if t > d * 0.8:
            chip(c, "MESMO PESO", 540, 1750, WHITE, INK, 58, t=t, start=d * 0.8)

def rule(c, t, d, b):
    flash_end = d * 0.35
    add = d * 0.45
    reset = d * 0.62
    with Cam(c, t, punch=0.06, shake=10 * (1 - prog(t, add, 0.25)) if t > add else 0):
        plates = 3 if t > add else 2
        barbell(c, 540, 1090, 1.15, plates)
        if t > add:
            pp = back_out(prog(t, add, 0.3))
            for side in (-1, 1):
                disk(c, 540 + side * (215 + 2 * 34) * 1.15, 1090, 130 * (1 - prog(t, add, 0.5)), WHITE, 0.25)
        txt = "62,5 KG" if t > add else "60 KG"
        pt = back_out(prog(t, add, 0.3)) if t > add else 1.0
        pop_in(c, 540, 900, pt); tag(c, 0, 0, txt); c.restore()
        if t < reset:
            on = 1.0 if t > flash_end else (0.35 + 0.65 * (int(t * 8) % 2))
            counter(c, 540, 1470, 8, 1.0, YEL, a=on)
        else:
            pc = back_out(prog(t, reset, 0.3))
            pop_in(c, 540, 1470, pc); counter(c, 0, 0, 6, 1.0, WHITE); c.restore()
            label(c, "RECOMEÇA", 540, 1700, GREY, 50)
        check_mark(c, 850, 1440, 1.3, prog(t, d * 0.75, 0.3))

def _bubble(c, x, y, w, h, a=1.0):
    """balão de comentário flat com rabinho embaixo à esquerda"""
    rrect(c, x - w / 2, y - h / 2, w, h, 34, (0.93, 0.92, 0.89), a)
    c.move_to(x - w / 2 + 60, y + h / 2 - 2); c.line_to(x - w / 2 + 40, y + h / 2 + 50); c.line_to(x - w / 2 + 120, y + h / 2 - 2)
    c.close_path(); rgb(c, (0.93, 0.92, 0.89), a); c.fill()

def cta(c, t, d, b):
    """gatilho (comenta suas repetições) -> não lembra? -> Bríu guarda/avisa -> frase fixa + link"""
    mk = b.get("marks", {}); off = 0.08
    t_nl, t_app, t_fix = mk.get("nao_lembra", 3.0) + off, mk.get("app", 5.7) + off, mk.get("fixa", 8.4) + off
    with Cam(c, t, punch=0.10, shake=10 if t_nl < t < t_nl + 0.25 else 0):
        if t < t_app:
            # 1) balão de comentário digitando
            p = back_out(prog(t, 0.05, 0.35))
            if p > 0:
                c.save(); c.translate(600, 1010); c.scale(max(p, .001), max(p, .001)); c.translate(-600, -1010)
                _bubble(c, 600, 1010, 700, 230)
                disk(c, 330, 1010, 46, (0.31, 0.33, 0.39)); disk(c, 330, 995, 18, (0.6, 0.62, 0.66)); rrect(c, 302, 1020, 56, 26, 13, (0.6, 0.62, 0.66))
                if t < t_nl:
                    txt = "SUPINO: __ REPETIÇÕES"
                    n = int(clamp((t - 0.4) * 14, 0, len(txt)))
                    draw_text(c, txt[:n], 400, 1032, 52, INK, "Anton")
                    if int(t * 3) % 2 == 0: cap_line(c, 400 + 14 + c.text_extents(txt[:n]).x_advance if n else 410, 990, 400 + 14 + c.text_extents(txt[:n]).x_advance if n else 410, 1045, INK, 5)
                else:
                    jig = math.sin(t * 40) * 6 * (1 - prog(t, t_nl, 0.6))
                    draw_text(c, "SUPINO: ?? REPETIÇÕES", 400 + jig, 1032, 52, RED, "Anton")
                c.restore()
            pose = "point_up" if t < t_nl else "scratch"
            chunky(c, 300, FLOOR_Y + 40, 0.72, pose, face=1)
            if t > t_nl:
                pq = back_out(prog(t, t_nl, 0.3))
                c.save(); c.translate(760, 1420); c.scale(max(pq, .001), max(pq, .001))
                label(c, "NÃO LEMBRA?", 0, 0, YEL, 92); c.restore()
        else:
            # 2) o app guarda a última carga e avisa a hora de subir
            tt = t - t_app
            px, py, s = 540, 1200, 1.0
            pp = back_out(prog(tt, 0.0, 0.35))
            c.save(); c.translate(px, py); c.scale(max(pp, .001), max(pp, .001)); c.translate(-px, -py)
            ring(c, px, py, 330, t, YEL)
            phone_screen(c, px, py, s, glow=0.6 + 0.4 * math.sin(t * 5))
            brio_mark(c, px - 85, py - 245, 0.5, trail=True, t=t)
            brio_wordmark(c, px - 40, py - 228, 46, LILAC, align="left")
            p1 = ease_out(prog(tt, 0.2, 0.35))
            if p1 > 0:
                rrect(c, px - 145, py - 170, 290, 150, 18, (0.2, 0.22, 0.26), p1)
                draw_text(c, "ÚLTIMA VEZ", px - 120, py - 125, 24, GREY, "Space Mono", p1, spacing=2)
                draw_text(c, "SUPINO", px - 120, py - 80, 40, WHITE, "Anton", p1)
                draw_text(c, "60 KG × 8", px - 120, py - 34, 40, WHITE, "Anton", p1)
            p2 = back_out(prog(tt, 1.1, 0.35))
            if p2 > 0:
                pul = 1 + 0.04 * math.sin(t * 8)
                c.save(); c.translate(px, py + 120); c.scale(max(p2 * pul, .001), max(p2 * pul, .001))
                rrect(c, -155, -110, 310, 220, 24, YEL)
                draw_text(c, "HORA DE SUBIR", 0, -40, 26, INK, "Space Mono", align="center", spacing=1)
                label(c, "62,5 KG", 0, 70, INK, 92)
                c.restore()
            c.restore()
            # 3) frase fixa + link
            if t > t_fix:
                pf = prog(t, t_fix, 0.35)
                draw_text(c, "REGISTRE E ACOMPANHE SEUS", 540, 1630, 34, WHITE, "Space Mono", pf, align="center", spacing=2)
                draw_text(c, "TREINOS GRATUITAMENTE", 540, 1675, 34, WHITE, "Space Mono", pf, align="center", spacing=2)
                chip(c, "LINK NA BIO", 540, 1775, YEL, INK, 66, t=t, start=t_fix + 0.6)

VIS = {k: globals()[k] for k in "hook name example weeks rule cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.3, "swish"), (0.6, "clack"), (1.0, "clack"), (1.4, "click"), ("0.45d", "pop")],
    "name": [(0.0, "whoosh"), (0.1, "pop"), ("0.45d", "pop"), ("0.6d", "swish"), ("0.6d+0.5", "ding")],
    "example": [(0.0, "whoosh"), (0.1, "pop")] + [(f"0.4+{k}*(0.75d-0.4)/6", "tick") for k in range(5)] + [("0.75d", "ding")],
    "weeks": [(0.0, "whoosh"), (0.1, "swish"), ("0.35d", "swish"), ("0.65d", "swish"), ("0.8d", "pop")],
    "rule": [(0.0, "whoosh"), (0.2, "tick"), (0.45, "tick"), ("0.45d", "clack"), ("0.45d+0.05", "pop"), ("0.62d", "pop"), ("0.75d", "ding")],
    "cta": [(0.0, "whoosh"), (0.05, "pop"), (0.5, "tick"), (0.9, "tick"), (1.3, "tick"), (3.1, "buzz"), (5.8, "whoosh"), (6.9, "ding"), (9.1, "pop")],
}
