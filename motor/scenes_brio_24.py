"""BRIO 24 — quanto tempo de treino por dia basta."""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_24 as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        clock(c, 330, 1180, 210, t * 3, 1.0)
        pop(c, 330, 1470, back_out(prog(t, 0.3, 0.3))); label(c, "2 HORAS?", 0, 30, WHITE, 76); c.restore()
        chunky(c, 800, FLOOR_Y, 0.85, pose_mix("idle", "shrug", prog(t, 0.6, 0.3)), face=-1)
        pop(c, 800, 1000, back_out(prog(t, 0.5, 0.3))); label(c, "?", 0, 60, YEL, 190); c.restore()
        if t > d * 0.5:
            x_mark(c, 330, 1180, 1.6, prog(t, d * 0.5, 0.3))
            tag(c, 540, 1760, "NÃO PRECISA", YEL, INK, 66, back_out(prog(t, d * 0.6, 0.3)))

def myth(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # tempo sobe, músculo não
        p = ease_out(prog(t, 0.2, 1.4))
        clock(c, 280, 1050, 110, t * 4)
        txt(c, "TEMPO", 280, 1220, 44, WHITE, prog(t, 0.2, 0.3))
        rrect(c, 180, 1650 - 400 * p, 200, 400 * p + 1, 14, YEL)
        txt(c, "MAIS TEMPO", 280, 1720, 36, GREY)
        arrow(c, 280, 1600, 280, 1340, YEL, 14, p=prog(t, 0.3, 0.6))
        # músculo parado
        arm_view(c, 760, 900, 0.7, bend=1.1)
        rrect(c, 680, 1560, 160, 90, 14, GREY)
        txt(c, "MÚSCULO", 760, 1720, 36, GREY)
        cap_line(c, 600, 1500, 940, 1500, RED, 8, 0.0)
        x_mark(c, 640, 1380, 0.8, prog(t, d * 0.5, 0.3))
        tag(c, 760, 1300, "QUASE IGUAL", RED, WHITE, 44, back_out(prog(t, d * 0.5, 0.3)))

def truth(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 + 0.5 * math.sin(t * 3.5)
        hx, hy = chunky(c, 270, FLOOR_Y, 0.85, pose_mix("curl_down", "curl_up", u), face=1, bob=-4 * u)
        dumbbell(c, hx, hy, 0.8)
        # medidor perto do limite
        cx, cy = 760, 1250
        pa = back_out(prog(t, 0.2, 0.4))
        pop(c, cx, cy, pa)
        c.new_path(); c.arc(0, 0, 190, math.pi, 2 * math.pi); rgb(c, CARD); c.set_line_width(46); c.stroke()
        c.new_path(); c.arc(0, 0, 190, math.pi * 1.72, 2 * math.pi); rgb(c, YEL); c.set_line_width(46); c.stroke()
        ang = math.pi + math.pi * (0.78 + 0.1 * math.sin(t * 6)) * prog(t, 0.4, 0.6)
        cap_line(c, 0, 0, 150 * math.cos(ang), 150 * math.sin(ang), WHITE, 14)
        disk(c, 0, 0, 24, WHITE); c.restore()
        txt(c, "LIMITE", 760, 1330, 44, WHITE, prog(t, 0.4, 0.3))
        check_mark(c, 760, 1470, 0.8, prog(t, d * 0.4, 0.3))
        tag(c, 540, 1745, "SÉRIES BOAS", YEL, INK, 66, back_out(prog(t, d * 0.35, 0.3)))
        if t > d * 0.65:
            clock(c, 860, 960, 60, t)
            x_mark(c, 860, 960, 0.9, prog(t, d * 0.65, 0.3))

def enough(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cx, cy, r = 540, 1130, 200
        disk(c, cx, cy, r, (0.08, 0.09, 0.11))
        p = ease_out(prog(t, 0.2, 0.9))
        c.new_path(); c.move_to(cx, cy); c.arc(cx, cy, r, -math.pi / 2, -math.pi / 2 + 2 * math.pi * (40 / 60) * p); c.close_path(); rgb(c, YEL); c.fill()
        c.new_path(); c.arc(cx, cy, r, 0, 6.2832); rgb(c, WHITE); c.set_line_width(10); c.stroke()
        disk(c, cx, cy, 120, (0.08, 0.09, 0.11)); label(c, "40", cx, cy + 25, WHITE, 120); label(c, "MIN", cx, cy + 85, YEL, 44)
        days = ["S", "T", "Q", "Q", "S", "S", "D"]
        for i, dd in enumerate(days):
            x = 130 + i * 136; on = i in (0, 2, 4)
            pp = back_out(prog(t, 0.6 + i * 0.07, 0.25))
            card(c, x, 1560, 110, 150, YEL if on and t > d * 0.35 + i * 0.1 else CARD, pp, 20)
            if pp > 0: txt(c, dd, x, 1615, 70, INK if on and t > d * 0.35 + i * 0.1 else GREY, pp)
        tag(c, 540, 1740 - 40, "3 A 4 VEZES NA SEMANA", WHITE, INK, 42, back_out(prog(t, d * 0.5, 0.3)))
        chip(c, "BEM FEITOS", 540, 1000 - 0, YEL, INK, 0, t=t) if False else None

def waste(c, t, d, b):
    with Cam(c, t, punch=0.06):
        items = [("CELULAR", 300), ("CONVERSA", 540), ("FILA", 780)]
        for i, (n, x) in enumerate(items):
            p = back_out(prog(t, 0.15 + i * 0.55, 0.3))
            card(c, x, 1220, 220, 420, CARD, p)
            if p <= 0: continue
            pop(c, x, 1170, p)
            if i == 0:
                rrect(c, -50, -90, 100, 180, 16, (0.07, 0.08, 0.1)); rrect(c, -40, -75, 80, 140, 10, BLU, 0.5 + 0.3 * math.sin(t * 6))
            elif i == 1:
                rrect(c, -85, -70, 120, 70, 24, WHITE); rrect(c, -35, 10, 120, 70, 24, YEL)
                for k in range(3): disk(c, -50 + k * 30, -35, 7, GREY)
            else:
                rrect(c, -60, -40, 120, 24, 8, IRON); cap_line(c, -90, -28, 90, -28, STEEL, 8)
                cap_line(c, 0, -16, 0, 80, IRON, 22)
                c.restore(); pop(c, x, 1170, p)
                label(c, "?", 70, -60, YEL, 70)
            c.restore()
            txt(c, n, x, 1380, 34, WHITE, p)
        clock(c, 540, 1620, 80, t * 6)
        tag(c, 540, 1000, "TEMPO PERDIDO", RED, WHITE, 58, back_out(prog(t, d * 0.45, 0.3)))
        arrow(c, 540, 1470, 540, 1500, RED, 8, p=0)

def secret(c, t, d, b):
    with Cam(c, t, punch=0.06):
        notebook(c, 540, 1230, 760, 640, back_out(prog(t, 0.1, 0.3)))
        rows = [("SUPINO", "4 × 8 · 60 KG"), ("REMADA", "4 × 10 · 45 KG"), ("AGACHAR", "4 × 8 · 80 KG")]
        for i, (a, bb) in enumerate(rows):
            p = prog(t, 0.5 + i * 0.5, 0.3)
            y = 1090 + i * 130
            txt(c, a, 400, y + 12, 44, INK, p)
            mono(c, bb, 650, y + 8, 26, (0.3, 0.3, 0.35), p)
            check_mark(c, 860, y, 0.5, prog(t, 0.75 + i * 0.5, 0.25))
        chunky(c, 180, FLOOR_Y, 0.55, pose_mix("idle", "point_up", prog(t, 0.2, 0.3)), face=1)
        tag(c, 560, 1720, "CHEGA COM PLANO", YEL, INK, 62, back_out(prog(t, d * 0.45, 0.3)))

def rest(c, t, d, b):
    with Cam(c, t, punch=0.06):
        def mmss(sec): sec = max(0, int(sec)); return f"{sec // 60}:{sec % 60:02d}"
        for i, (lab, start, col) in enumerate([("GRANDES", 120, YEL), ("PEQUENOS", 60, WHITE)]):
            x = 300 + i * 480
            p = back_out(prog(t, 0.1 + i * 0.35, 0.3))
            card(c, x, 1180, 420, 380, (0.08, 0.09, 0.11), p)
            if p > 0:
                mono(c, lab, x, 1050, 30, GREY, p)
                rem = start - ((t * 12) % (start + 4))
                label(c, mmss(rem), x, 1230, col, 150, p)
                rrect(c, x - 160, 1300, 320, 20, 10, CARD, p)
                rrect(c, x - 160, 1300, 320 * clamp(rem / start), 20, 10, col, p)
        tag(c, 540, 1560, "CRONÔMETRO", YEL, INK, 64, back_out(prog(t, d * 0.3, 0.3)))
        txt(c, "SEM SUMIR", 540, 1700, 56, WHITE, prog(t, d * 0.65, 0.3))

def short(c, t, d, b):
    with Cam(c, t, punch=0.06):
        p = back_out(prog(t, 0.2, 0.4))
        card(c, 540, 1010, 860, 120, CARD, p)
        rrect(c, 110, 960, 860 * 0.3 * ease_out(prog(t, 0.4, 0.6)) + 1, 100, 24, YEL)
        txt(c, "TREINO CURTO", 540, 1030, 52, WHITE, prog(t, 0.5, 0.3))
        for i, n in enumerate(["PRINCIPAIS", "SÓ OS GRANDES"]):
            pass
        for i, (lab) in enumerate(["AGACHAR", "SUPINO", "REMADA"]):
            pp = back_out(prog(t, 0.8 + i * 0.35, 0.3))
            card(c, 250 + i * 290, 1230, 260, 130, DARK, pp)
            if pp > 0: txt(c, lab, 250 + i * 290, 1245, 38, WHITE, pp)
            check_mark(c, 250 + i * 290, 1340, 0.45, prog(t, 1.0 + i * 0.35, 0.25))
        chunky(c, 240, FLOOR_Y, 0.55, "walk1" if int(t * 3) % 2 else "walk2", face=1)
        if t > d * 0.5:
            card(c, 740, 1520, 500, 110, (0.08, 0.09, 0.11), back_out(prog(t, d * 0.5, 0.3)))
            txt(c, "NENHUM = 0", 740, 1550, 52, RED, prog(t, d * 0.5, 0.3))
        tag(c, 540, 1760, "CURTO > NENHUM", YEL, INK, 62, back_out(prog(t, d * 0.65, 0.3)))

def const(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # semanas regulares vs um treino gigante
        card(c, 300, 1250, 440, 640, CARD, back_out(prog(t, 0.1, 0.3)))
        bars(c, 300, 1480, 360, 300, [0.8, 0.8, 0.8, 0.8], t, 0.3, [GRN] * 4)
        txt(c, "TODA SEMANA", 300, 1000, 40, GRN, prog(t, 0.3, 0.3))
        check_mark(c, 300, 1590, 0.6, prog(t, 1.3, 0.3))
        card(c, 780, 1250, 440, 640, CARD, back_out(prog(t, 0.3, 0.3)))
        vals = [0.05, 0.05, 0.05, 1.0]
        bars(c, 780, 1480, 360, 400, vals, t, 0.5, [GREY, GREY, GREY, RED])
        txt(c, "1 GIGANTE", 780, 1000, 40, RED, prog(t, 0.5, 0.3))
        x_mark(c, 780, 1590, 0.55, prog(t, d * 0.55, 0.3))
        tag(c, 540, 1760, "CONSTÂNCIA MANDA", YEL, INK, 62, back_out(prog(t, d * 0.4, 0.3)))

def order(c, t, d, b):
    with Cam(c, t, punch=0.06):
        items = [("AGACHAMENTO", 700, YEL), ("SUPINO", 560, YEL), ("ROSCA", 380, GREY), ("PANTURRILHA", 300, GREY)]
        for i, (n, w, col) in enumerate(items):
            p = back_out(prog(t, 0.15 + i * 0.4, 0.3))
            y = 960 + i * 140
            card(c, 400, y, w, 110, col, p)
            if p > 0: txt(c, n, 400, y + 16, 42, INK if col == YEL else WHITE, p)
            pn = back_out(prog(t, 0.3 + i * 0.4, 0.3))
            if pn > 0:
                pop(c, 80, y, pn); disk(c, 0, 0, 34, WHITE); label(c, str(i + 1), 0, 16, INK, 44); c.restore()
        # energia caindo
        card(c, 900, 1170, 110, 450, CARD, back_out(prog(t, 0.2, 0.3)))
        lv = 1 - 0.75 * ease(prog(t, 0.4, 1.8))
        rrect(c, 868, 1370 - 400 * lv + 30, 64, 400 * lv + 1, 12, GRN if lv > 0.5 else YEL)
        mono(c, "ENERGIA", 900, 1440, 20, GREY)
        tag(c, 300, 1590, "GRANDES PRIMEIRO", YEL, INK, 56, back_out(prog(t, d * 0.4, 0.3)))
        txt(c, "PEQUENOS NO FINAL", 380, 1710, 48, WHITE, prog(t, d * 0.6, 0.3))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="__ MINUTOS", app_title="TREINO DE HOJE", app_lines=[("SUPINO", None), ("REMADA", None), ("AGACHAR", None)], app_big="40 MIN", app_big_label="CABE NO SEU TEMPO")

VIS = {k: globals()[k] for k in "hook myth truth enough waste secret rest short const order cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.3, "pop"), (0.5, "pop"), ("0.5d", "buzz"), ("0.6d", "pop")],
    "myth": [(0.0, "whoosh"), (0.2, "swish"), (0.6, "tick"), ("0.5d", "buzz"), ("0.5d+0.1", "pop")],
    "truth": [(0.0, "whoosh"), (0.2, "pop"), (0.5, "swish"), ("0.35d", "pop"), ("0.4d", "ding"), ("0.65d", "buzz")],
    "enough": [(0.0, "whoosh"), (0.2, "swish"), (0.6, "pop"), (1.1, "pop"), ("0.35d", "click"), ("0.5d", "pop")],
    "waste": [(0.0, "whoosh"), (0.15, "pop"), (0.7, "pop"), (1.25, "pop"), ("0.45d", "buzz")],
    "secret": [(0.0, "whoosh"), (0.1, "pop"), (0.75, "tick"), (1.25, "tick"), (1.75, "tick"), ("0.45d", "pop")],
    "rest": [(0.0, "whoosh"), (0.1, "pop"), (0.45, "pop"), ("0.3d", "pop"), ("0.65d", "click")],
    "short": [(0.0, "whoosh"), (0.2, "pop"), (0.8, "pop"), (1.15, "pop"), (1.5, "pop"), ("0.5d", "buzz"), ("0.65d", "pop")],
    "const": [(0.0, "whoosh"), (0.1, "pop"), (0.3, "pop"), ("0.4d", "pop"), ("0.55d", "buzz")],
    "order": [(0.0, "whoosh"), (0.15, "pop"), (0.55, "pop"), (0.95, "pop"), (1.35, "pop"), ("0.4d", "pop"), ("0.6d", "pop")],
    "cta": cta_sfx(BEAT_CTA, "bubble"),
}
