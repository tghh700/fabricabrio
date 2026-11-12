"""BRIO 14 — treinar em jejum."""
import math
from engine2 import *
from lote_h import *
import roteiro_brio_14 as R
from cta_brio import cta_brio, cta_sfx
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        clock(c, 300, 1000, 120, t * 1.5, hour=6)
        plate(c, 760, 1010, 140)
        pr = back_out(prog(t, 0.3, 0.3))
        if pr > 0: x_mark(c, 760, 1010, 1.1 * pr, 1.0)
        flame(c, 540, 1300, 1.0 + 0.05 * math.sin(t * 6), YEL, t)
        chunky(c, 540, FLOOR_Y, 0.62, pose_mix("idle", "walk1", 0.5 + 0.5 * math.sin(t * 5)), face=1, bob=-6 * abs(math.sin(t * 5)))
        tg(c, 540, 1760, "SEM COMER", YEL, INK, 64, back_out(prog(t, d * 0.45, 0.3)))

def idea(c, t, d, b):
    with Cam(c, t, punch=0.06):
        p1 = back_out(prog(t, 0.2, 0.35))
        pop_in(c, 230, 1100, p1); plate(c, 0, 0, 120); x_mark(c, 0, 0, 0.9, prog(t, 0.45, 0.3)); c.restore()
        draw_text(c, "SEM COMIDA", 230, 1300, 44, WHITE, "Anton", p1, align="center")
        arrow(c, 380, 1100, 640, 1100, YEL, 18, p=ease_out(prog(t, d * 0.3, 0.35)))
        p2 = back_out(prog(t, d * 0.4, 0.4))
        pop_in(c, 820, 1100, p2); flame(c, 0, 0, 1.2, YEL, t); c.restore()
        draw_text(c, "GORDURA", 820, 1330, 52, YEL, "Anton", p2, align="center")
        # tanque de energia
        rrect(c, 200, 1500, 680, 50, 25, (0.2, 0.22, 0.27))
        rrect(c, 200, 1500, 680 * (1 - 0.6 * ease(prog(t, d * 0.4, d * 0.5))) + 1, 50, 25, YEL)
        draw_text(c, "ENERGIA", 540, 1620, 36, GREY, "Space Mono", align="center", spacing=6)
        chunky(c, 880, FLOOR_Y + 130, 0.0001, "idle")

def partial(c, t, d, b):
    with Cam(c, t, punch=0.06):
        base = 1500
        draw_text(c, "GORDURA USADA NO TREINO", 540, 900, 40, GREY, "Space Mono", align="center", spacing=2)
        for x, h, col, lab, dl in ((330, 330, GREY, "COMIDO", 0.2), (750, 430, YEL, "JEJUM", 0.5)):
            pp = ease_out(prog(t, dl, 0.6))
            bar(c, x, base, 230, h, col, pp)
            if pp > 0.1: flame(c, x, base - h * pp - 80, 0.55, col, t)
            draw_text(c, lab, x, base + 70, 48, WHITE, "Anton", align="center")
        pa = back_out(prog(t, d * 0.55, 0.3))
        tg(c, 750, 1000, "UM POUCO MAIS", YEL, INK, 52, pa)
        dumbbell_h(c, 540, 1710, 0.9, ang=math.sin(t * 5) * 0.12)
        ring(c, 750, 1190, 140, t, YEL)

def day(c, t, d, b):
    with Cam(c, t, punch=0.06):
        base = 1500
        groups = [("TREINO", 180, 240, 0.15), ("RESTO DO DIA", 440, 320, 0.2 + d * 0.28), ("TOTAL", 800, 400, 0.2 + d * 0.55)]
        # barras: (x do grupo, altura comido, altura jejum)
        spec = [(250, 300, 360, "TREINO", 0.15), (620, 300, 240, "RESTO", d * 0.3), (910, 330, 330, "TOTAL", d * 0.58)]
        for x, ha, hj, lab, st in spec:
            pp = ease_out(prog(t, st, 0.5))
            w = 80 if lab != "TOTAL" else 90
            bar(c, x - 50, base, w, ha, GREY, pp, 12)
            bar(c, x + 50, base, w, hj, YEL, pp, 12)
            draw_text(c, lab, x, base + 65, 40, WHITE, "Anton", pp, align="center")
        pe = back_out(prog(t, d * 0.62, 0.35))
        if pe > 0:
            pop_in(c, 910, 1000, pe); label(c, "=", 0, 50, GRN, 160); c.restore()
        tg(c, 300, 1000, "MAIS", GRN, INK, 44, back_out(prog(t, 0.6, 0.3)))
        tg(c, 620, 1000, "MENOS", RED, WHITE, 44, back_out(prog(t, d * 0.35, 0.3)))
        draw_text(c, "CINZA = COMEU   CORAL = JEJUM", 540, 1750, 28, GREY, "Space Mono", align="center", spacing=2)

def rule(c, t, d, b):
    with Cam(c, t, punch=0.06):
        ang = 0.25 * math.sin(t * 2.2) * (1 - 0.7 * prog(t, d * 0.6, 0.6))
        def L(x, y):
            plate(c, x, y - 90, 90, food=1.0)
        def Rr(x, y):
            flame(c, x, y - 80, 0.75, YEL, t)
        balance(c, 540, 1330, ang, L, Rr, 330)
        draw_text(c, "COME", 215, 1570, 44, WHITE, "Anton", align="center")
        draw_text(c, "GASTA", 865, 1570, 44, YEL, "Anton", align="center")
        tg(c, 540, 900, "TOTAL DO DIA", YEL, INK, 68, back_out(prog(t, 0.2, 0.35)))
        pe = back_out(prog(t, d * 0.65, 0.35))
        if pe > 0: check_mark(c, 540, 1740, 1.2 * pe, 1.0)

def perf(c, t, d, b):
    with Cam(c, t, punch=0.06):
        draw_text(c, "SÉRIES BOAS", 540, 880, 40, GREY, "Space Mono", align="center", spacing=6)
        for i, (lab, on, col, st) in enumerate((("COMIDO", 5, GRN, 0.2), ("JEJUM", 2, YEL, 0.6))):
            y = 1000 + i * 190
            draw_text(c, lab, 70, y + 16, 44, WHITE, "Anton")
            for k in range(5):
                pp = back_out(prog(t, st + k * 0.12, 0.3))
                if pp <= 0: continue
                pop_in(c, 420 + k * 120, y, pp); disk(c, 0, 0, 40, col if k < on else (0.28, 0.3, 0.35)); c.restore()
        pb = prog(t, d * 0.4, 0.5)
        battery(c, 340, 1470, 360, 170, 0.75 - 0.6 * ease(pb), mix(GRN, RED, ease(pb)))
        chunky(c, 800, FLOOR_Y + 20, 0.55, pose_mix("idle", "tired", prog(t, d * 0.4, 0.4)), face=-1, bob=4 * math.sin(t * 3))
        tg(c, 540, 1760, "RENDE MENOS", RED, WHITE, 58, back_out(prog(t, d * 0.5, 0.3)))

def who(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 360, FLOOR_Y, 0.85, pose_mix("flex", "thumb", 0.5 + 0.5 * math.sin(t * 2)), face=1)
        disk(c, 800, 1060, 140, (0.12, 0.13, 0.16)); ring(c, 800, 1060, 150, t, GRN)
        check_mark(c, 800, 1060, 1.6, prog(t, 0.3, 0.4))
        tg(c, 760, 1330, "SE SENTE BEM", GRN, INK, 54, back_out(prog(t, d * 0.3, 0.3)))
        tg(c, 760, 1480, "PREFERÊNCIA", YEL, INK, 54, back_out(prog(t, d * 0.6, 0.3)))

def dizzy(c, t, d, b):
    with Cam(c, t, punch=0.06, shake=3 if t > 0.3 else 0):
        hx, hy = 330, FLOOR_Y - 520 * 0.8 - 90 * 0.8 - 70
        chunky(c, 330, FLOOR_Y, 0.8, "tired", face=1, bob=5 * math.sin(t * 4))
        for i in range(4):
            a = t * 5 + i * math.pi / 2
            disk(c, hx + 110 * math.cos(a), hy - 40 + 28 * math.sin(a), 13, YEL)
        warn(c, 790, 1000, 1.4 * back_out(prog(t, 0.2, 0.3)) + .01, YEL)
        for i, tx in enumerate(("TONTURA", "FRAQUEZA", "ENJOO")):
            tg(c, 790, 1190 + i * 90, tx, RED, WHITE, 44, back_out(prog(t, 0.4 + i * 0.3, 0.3)))
        pa = back_out(prog(t, d * 0.6, 0.35))
        if pa > 0:
            pop_in(c, 790, 1560, pa); apple(c, -110, 0, 60); c.restore()
            tg(c, 830, 1560, "COME", GRN, INK, 56, pa)

def secret(c, t, d, b):
    with Cam(c, t, punch=0.06):
        filled = {}
        sched = [0, 2, 4, 7, 9, 11, 14, 16, 18, 21, 23, 25]
        for k, i in enumerate(sched):
            filled[i] = back_out(prog(t, 0.3 + k * (d * 0.8 / len(sched)), 0.25))
        for q, dn in enumerate("SEG TER QUA QUI SEX SAB DOM".split()):
            draw_text(c, dn, 70 + q * 135 + 55, 930, 28, GREY, "Space Mono", align="center")
        calendar(c, 70, 960, 7, 4, 135, 120, filled, GRN)
        tg(c, 540, 1600, "TODA SEMANA", YEL, INK, 66, back_out(prog(t, d * 0.45, 0.3)))
        draw_text(c, "VÁRIAS VEZES", 540, 1700, 40, WHITE, "Anton", prog(t, d * 0.6, 0.3), align="center")

def eat(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pl = back_out(prog(t, 0.1, 0.4))
        pop_in(c, 330, 1130, pl); plate(c, 0, 0, 170, food=1.0); c.restore()
        pr = back_out(prog(t, 0.5, 0.35))
        tg(c, 330, 940, "PROTEÍNA", YEL, INK, 54, pr)
        arrow(c, 520, 1130, 700, 1130, YEL, 16, p=prog(t, d * 0.4, 0.3))
        # músculo cresce
        g = ease(prog(t, d * 0.45, d * 0.5))
        hh = 200 + 300 * g
        rrect(c, 760, 1500 - hh, 200, hh, 40, L_FRONT)
        rrect(c, 760, 1500 - hh, 200, hh, 40, YEL, 0.2 + 0.2 * math.sin(t * 5))
        draw_text(c, "MÚSCULO", 860, 1580, 40, WHITE, "Anton", align="center")
        chunky(c, 330, FLOOR_Y, 0.0001, "idle")
        draw_text(c, "DEPOIS DO TREINO", 330, 1400, 34, GREY, "Space Mono", prog(t, 0.6, 0.3), align="center", spacing=1)
        tg(c, 540, 1740, "RECUPERA", GRN, INK, 60, back_out(prog(t, d * 0.7, 0.3)))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="__ VEZES", app_title="TREINOS DA SEMANA",
             app_lines=[("SEG  PEITO", None), ("QUA  COSTAS", None), ("SEX  PERNAS", None)], app_big="3 TREINOS", app_big_label="ESTA SEMANA")

VIS = {k: globals()[k] for k in "hook idea partial day rule perf who dizzy secret eat cta".split()}
SFX = {k: [(0.0, "whoosh")] for k in VIS}
SFX["hook"] = [(0.0, "boom"), (0.3, "pop"), ("0.45d", "pop")]
SFX["idea"] += [(0.2, "pop"), ("0.4d", "pop")]
SFX["partial"] += [(0.2, "pop"), (0.5, "pop"), ("0.55d", "pop")]
SFX["day"] += [(0.15, "pop"), ("0.3d", "pop"), ("0.62d", "ding")]
SFX["rule"] += [(0.2, "pop"), ("0.65d", "ding")]
SFX["perf"] += [(0.2, "pop"), ("0.5d", "buzz")]
SFX["who"] += [(0.3, "pop"), ("0.3d", "pop"), ("0.6d", "pop")]
SFX["dizzy"] += [(0.2, "pop"), (0.4, "buzz"), ("0.6d", "pop")]
SFX["secret"] += [(0.3, "tick"), ("0.45d", "pop")]
SFX["eat"] += [(0.1, "pop"), (0.5, "pop"), ("0.7d", "ding")]
SFX["cta"] = cta_sfx(BEAT_CTA, "bubble")
