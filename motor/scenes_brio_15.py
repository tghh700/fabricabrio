"""BRIO 15 — treina pesado e não cresce: erros fora da academia."""
import math
from engine2 import *
from lote_h import *
from scenes_brio_05 import counter
import roteiro_brio_15 as R
from cta_brio import cta_brio, cta_sfx
BEAT_CTA = R.BEATS[-1]

def pie(c, x, y, r, frac, col, a0=-math.pi / 2):
    c.new_path(); c.move_to(x, y); c.arc(x, y, r, a0, a0 + 2 * math.pi * frac); c.close_path(); rgb(c, col); c.fill()

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        chunky(c, 330, FLOOR_Y, 0.85, pose_mix("flex", "idle", 0.5 + 0.5 * math.sin(t * 2.5)), face=1)
        barbell(c, 760, 1560, 0.5, plates=3)
        pr = back_out(prog(t, 0.3, 0.3))
        pop_in(c, 760, 1100, pr * (1 + 0.05 * math.sin(t * 6))); label(c, "?", 0, 120, YEL, 340); c.restore()
        # músculo estacionado
        rrect(c, 620, 1330, 280, 24, 12, (0.2, 0.22, 0.27))
        rrect(c, 620, 1330, 40 + 8 * math.sin(t * 3), 24, 12, RED)
        draw_text(c, "MÚSCULO", 760, 1300, 30, GREY, "Space Mono", align="center", spacing=4)
        tg(c, 540, 1760, "FORA DA ACADEMIA", YEL, INK, 58, back_out(prog(t, d * 0.5, 0.3)))

def gym(c, t, d, b):
    with Cam(c, t, punch=0.06):
        g = ease_out(prog(t, 0.2, 1.0))
        pie(c, 540, 1230, 270, 1.0 * g, (0.3, 0.32, 0.38))
        pie(c, 540, 1230, 270, (1 / 24) * g, YEL)
        disk(c, 540, 1230, 120, (0.11, 0.12, 0.15))
        label(c, "24H", 540, 1262, WHITE, 90)
        tg(c, 250, 880, "1H ACADEMIA", YEL, INK, 46, back_out(prog(t, 0.6, 0.3)))
        tg(c, 760, 1620, "23H FORA", (0.45, 0.47, 0.55), WHITE, 56, back_out(prog(t, d * 0.45, 0.3)))
        dumbbell_h(c, 770, 960, 0.9, ang=math.sin(t * 5) * 0.15)
        arrow(c, 640, 1700, 540, 1520, YEL, 12, p=prog(t, d * 0.5, 0.3)) if False else None

def sleep(c, t, d, b):
    with Cam(c, t, punch=0.06):
        bed(c, 520, 1330, 0.95, t=t)
        pm = back_out(prog(t, 0.2, 0.3)); pop_in(c, 880, 960, pm); moon(c, 0, 0, 70); c.restore()
        clock(c, 190, 980, 90, t * 0.0 + 1.0, hour=5)
        tg(c, 190, 1130, "5 HORAS", RED, WHITE, 44, back_out(prog(t, 0.4, 0.3)))
        lv = 0.9 - 0.6 * ease(prog(t, d * 0.35, 0.6))
        battery(c, 540, 1660, 380, 150, lv, mix(GRN, RED, ease(prog(t, d * 0.35, 0.6))))
        draw_text(c, "PRÓXIMO TREINO", 540, 1580, 28, GREY, "Space Mono", align="center", spacing=4)

def protein(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # parede de músculo em construção
        cols, rows, bw, bh = 4, 3, 190, 110
        x0, y0 = 540 - cols * bw / 2, 1400
        k = 0
        for r_ in range(rows):
            for q in range(cols):
                xx, yy = x0 + q * bw, y0 - (r_ + 1) * bh
                filled = (r_ == 0 and q in (0, 1, 3)) or (r_ == 1 and q == 1)
                if filled:
                    pp = ease_out(prog(t, 0.2 + k * 0.25, 0.3)); k += 1
                    rrect(c, xx + 4, yy + 4 - (1 - pp) * 200, bw - 8, bh - 8, 10, BROWN, pp)
                else:
                    c.set_dash([14, 10]); rgb(c, GREY, 0.5); c.set_line_width(4)
                    c.rectangle(xx + 6, yy + 6, bw - 12, bh - 12); c.stroke(); c.set_dash([])
        pq = back_out(prog(t, d * 0.5, 0.35))
        pop_in(c, x0 + 2.5 * bw, y0 - 2.5 * bh, pq); label(c, "?", 0, 40, YEL, 120); c.restore()
        tg(c, 540, 930, "PROTEÍNA = TIJOLO", YEL, INK, 54, back_out(prog(t, 0.1, 0.3)))
        tg(c, 540, 1600, "SEM MATÉRIA-PRIMA", RED, WHITE, 52, back_out(prog(t, d * 0.4, 0.3)))
        draw_text(c, "MÚSCULO NÃO CRESCE", 540, 1700, 32, GREY, "Space Mono", prog(t, d * 0.6, 0.3), align="center", spacing=2)

def food(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pl = back_out(prog(t, 0.1, 0.35))
        pop_in(c, 300, 1150, pl); plate(c, 0, 0, 120, food=0.5); c.restore()
        # tanque vazio
        rrect(c, 460, 1100, 500, 60, 30, (0.2, 0.22, 0.27))
        rrect(c, 460, 1100, 40 + 20 * math.sin(t * 5) ** 2, 60, 30, RED)
        draw_text(c, "COMBUSTÍVEL", 710, 1080, 30, GREY, "Space Mono", align="center", spacing=4)
        # linha de carga travada
        pts = [(80, 1650), (250, 1560), (400, 1480), (520, 1420), (640, 1415), (780, 1415), (960, 1415)]
        n = prog(t, d * 0.3, d * 0.5) * (len(pts) - 1)
        i = int(n); seg = [pts[j] for j in range(0, i + 1)]
        if i < len(pts) - 1:
            f = n - i; seg.append((lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f)))
        if len(seg) > 1: poly(c, seg, YEL, 14)
        draw_text(c, "CARGA NA BARRA", 80, 1330, 28, GREY, "Space Mono", spacing=3)
        tg(c, 800, 1530, "TRAVA", RED, WHITE, 64, back_out(prog(t, d * 0.7, 0.3)))
        draw_text(c, "COMER POUCO", 540, 1780, 40, WHITE, "Anton", prog(t, 0.4, 0.3), align="center")

def weekend(c, t, d, b):
    with Cam(c, t, punch=0.06):
        days = "SEG TER QUA QUI SEX SAB DOM".split()
        for i, dn in enumerate(days):
            x = 70 + i * 135
            wk = i < 5
            pp = back_out(prog(t, 0.2 + i * 0.12, 0.3))
            rrect(c, x, 1000, 125, 200, 18, (0.2, 0.22, 0.27))
            draw_text(c, dn, x + 62, 1040, 30, GREY, "Space Mono", align="center")
            if wk:
                if pp > 0: check_mark(c, x + 62, 1130, 0.6 * pp, min(1, pp), GRN)
            else:
                q = prog(t, d * 0.45 + (i - 5) * 0.2, 0.3)
                if q > 0:
                    rgb(c, RED, 0.25 * q); c.rectangle(x, 1000, 125, 200); c.fill()
                    x_mark(c, x + 62, 1130, 0.6, q)
        # festa
        pq = back_out(prog(t, d * 0.45, 0.3))
        if pq > 0:
            pop_in(c, 800, 1480, pq)
            moon(c, -170, -30, 60)
            rrect(c, -20, -50, 70, 110, 12, BLU, 0.9); disk(c, 15, -60, 20, WHITE)
            for k in range(8):
                a = k * 0.8 + t * 3
                disk(c, 110 + 90 * math.cos(a), -20 + 60 * math.sin(a * 1.3), 8, [YEL, RED, GRN, BLU][k % 4])
            c.restore()
        # desfaz: barra de progresso encolhe
        g = 1 - 0.7 * ease(prog(t, d * 0.55, 0.8))
        rrect(c, 70, 1450, 500, 50, 25, (0.2, 0.22, 0.27)); rrect(c, 70, 1450, 500 * 0.95 * g, 50, 25, GRN if g > .5 else RED)
        draw_text(c, "PROGRESSO", 70, 1430, 28, GREY, "Space Mono", spacing=4)
        tg(c, 540, 1740, "DESFAZ TUDO", RED, WHITE, 62, back_out(prog(t, d * 0.7, 0.3)))

def stress(c, t, d, b):
    with Cam(c, t, punch=0.06, shake=4 * prog(t, 0.3, 0.2)):
        # termômetro
        rrect(c, 130, 900, 70, 560, 35, (0.2, 0.22, 0.27))
        lv = 0.35 + 0.6 * ease(prog(t, 0.2, 1.2))
        rrect(c, 140, 1450 - 540 * lv, 50, 540 * lv + 0, 25, RED)
        disk(c, 165, 1500, 60, RED)
        draw_text(c, "ESTRESSE", 165, 1620, 30, WHITE, "Space Mono", align="center", spacing=2)
        items = [("SONO", 0.5), ("FOME", 1.0), ("VONTADE", 1.5)]
        for i, (lab, st) in enumerate(items):
            y = 1000 + i * 250
            pp = back_out(prog(t, st, 0.35))
            if pp <= 0: continue
            pop_in(c, 620, y, pp)
            rrect(c, -290, -90, 580, 180, 30, (0.2, 0.22, 0.27))
            if i == 0: moon(c, -200, 0, 48)
            elif i == 1: plate(c, -200, 0, 55, food=0.4)
            else: dumbbell_h(c, -200, 0, 0.6)
            draw_text(c, lab, -110, 22, 62, WHITE, "Anton")
            arrow(c, 215, -40, 215, 50, RED, 12, p=1.0)
            c.restore()
        bolt(c, 330, 900, 280, 980, t, YEL, 10)

def secret(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (lab, fn) in enumerate((("SONO", lambda x, y: moon(c, x, y, 50)), ("COMIDA", lambda x, y: plate(c, x, y, 55, food=1.0)), ("TREINO", lambda x, y: dumbbell_h(c, x, y, 0.7)))):
            x = 200 + i * 340
            pp = back_out(prog(t, 0.15 + i * 0.25, 0.35))
            if pp <= 0: continue
            pop_in(c, x, 1010, pp)
            rrect(c, -140, -100, 280, 260, 30, (0.2, 0.22, 0.27)); fn(0, -20)
            draw_text(c, lab, 0, 125, 46, WHITE, "Anton", align="center")
            check_mark(c, 95, -75, 0.4, prog(t, 0.5 + i * 0.25, 0.25))
            c.restore()
        n = 1 + int(5 * ease(prog(t, d * 0.35, d * 0.55)))
        counter(c, 540, 1520, n, 1.0, YEL, title="MESES")
        tg(c, 540, 1760, "O BÁSICO BEM FEITO", YEL, INK, 52, back_out(prog(t, d * 0.6, 0.3)))

def check(c, t, d, b):
    with Cam(c, t, punch=0.06):
        base = 1560
        for x, h, col, lab, ic, dl in ((300, 520, GRN, "NOITE BOA", 0, 0.2), (780, 320, RED, "NOITE RUIM", 1, 0.6)):
            pp = ease_out(prog(t, dl, 0.6))
            bar(c, x, base, 250, h, col, pp)
            label(c, f"{int(100 * h / 520 * pp)}%", x, base - h * pp + 80, INK, 70) if pp > 0.4 else None
            draw_text(c, lab, x, base + 70, 44, WHITE, "Anton", align="center")
            if ic == 0: moon(c, x, 960, 55)
            else:
                moon(c, x, 960, 55, (0.5, 0.5, 0.55)); 
        draw_text(c, "RENDIMENTO NO TREINO", 540, 880, 30, GREY, "Space Mono", align="center", spacing=3)
        pv = back_out(prog(t, d * 0.55, 0.3))
        pop_in(c, 540, 1230, pv); label(c, "VS", 0, 30, YEL, 80); c.restore()
        chip(c, "COMPARA", 540, 1745, YEL, INK, 58, t=t, start=d * 0.65)

def fix(c, t, d, b):
    with Cam(c, t, punch=0.06):
        g = ease(prog(t, 0.3, 1.4))
        clock(c, 330, 1150, 170, 0.0, hour=11)
        pie(c, 330, 1150, 150, (0.5 / 12) * g * 1.0, YEL, a0=-math.pi / 2 + 11 * math.pi / 6 * 0 )
        pm = back_out(prog(t, 0.2, 0.3)); pop_in(c, 780, 1000, pm); moon(c, 0, 0, 80); c.restore()
        tg(c, 780, 1180, "+30 MIN", YEL, INK, 76, back_out(prog(t, 0.5, 0.3)))
        draw_text(c, "POR NOITE", 780, 1260, 36, WHITE, "Anton", prog(t, 0.7, 0.3), align="center")
        arrow(c, 540, 1480, 540, 1330, GRN, 16, p=prog(t, d * 0.5, 0.35))
        pb = ease_out(prog(t, d * 0.5, 0.6))
        bar(c, 330, 1760, 160, 150, GREY, 1, 12); bar(c, 540, 1760, 160, 150 + 120 * pb, GRN, 1, 12)
        draw_text(c, "PRÓXIMO TREINO", 800, 1720, 30, GREY, "Space Mono", align="center", spacing=1)
        tg(c, 540, 870, "COMEÇA PELO SONO", GRN, INK, 52, back_out(prog(t, d * 0.7, 0.3)))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="SONO", app_title="TREINO DE HOJE",
             app_lines=[("SONO  8H", None), ("SUPINO 60 KG", None), ("RENDEU BEM", GRN)], app_big="NOTA 9", app_big_label="NOITE BOA")

VIS = {k: globals()[k] for k in "hook gym sleep protein food weekend stress secret check fix cta".split()}
SFX = {k: [(0.0, "whoosh"), (0.25, "pop"), ("0.5d", "pop")] for k in VIS}
SFX["hook"] = [(0.0, "boom"), (0.3, "pop"), ("0.5d", "buzz")]
SFX["sleep"] += [("0.35d", "buzz")]
SFX["weekend"] += [("0.45d", "buzz"), ("0.7d", "buzz")]
SFX["stress"] += [(0.5, "pop"), (1.0, "pop"), (1.5, "pop"), (0.3, "buzz")]
SFX["secret"] += [(0.4, "tick"), ("0.6d", "ding")]
SFX["cta"] = cta_sfx(BEAT_CTA, "bubble")
