"""BRIO 23 — braço não cresce: tríceps."""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_23 as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        u = 0.5 + 0.5 * math.sin(t * 4)
        hx, hy = chunky(c, 300, FLOOR_Y, 0.9, pose_mix("curl_down", "curl_up", u), face=1)
        dumbbell(c, hx, hy, 0.8, 0.0)
        pop(c, 300, 1000, back_out(prog(t, 0.5, 0.3))); label(c, "?", 0, 60, YEL, 190); c.restore()
        arm_view(c, 760, 960, 1.0, tri=None, bi=None, bend=1.2)
        x_mark(c, 760, 1500, 0.8, prog(t, 0.9, 0.3))
        tag(c, 760, 1640, "ROSCA TODA SEMANA", CARD, WHITE, 44, back_out(prog(t, 0.3, 0.3)))
        tag(c, 540, 1760, "MÚSCULO ERRADO?", YEL, INK, 60, back_out(prog(t, d * 0.55, 0.3)))

def biceps(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pul = 0.08 * math.sin(t * 6)
        arm_view(c, 440, 900, 1.15, bi=YEL, bend=1.1, pulse=pul)
        ring(c, 520, 1060, 120, t, YEL)
        # espelho
        pm = back_out(prog(t, 0.3, 0.35))
        pop(c, 860, 1150, pm)
        rrect(c, -110, -190, 220, 380, 30, (0.12, 0.14, 0.18)); rrect(c, -90, -170, 180, 340, 22, (0.35, 0.5, 0.6))
        cap_line(c, -70, -140, 20, -60, WHITE, 8, 0.5)
        c.restore()
        mono(c, "ESPELHO", 860, 1400, 26, GREY, pm)
        arrow(c, 600, 1060, 740, 1100, YEL, 12, p=prog(t, 0.6, 0.3))
        tag(c, 620, 1620, "FRENTE = BÍCEPS", YEL, INK, 64, back_out(prog(t, d * 0.35, 0.3)))
        txt(c, "O QUE APARECE", 620, 1730, 44, WHITE, prog(t, d * 0.55, 0.3))

def triceps(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pul = 0.1 * math.sin(t * 6)
        arm_view(c, 280, 900, 1.0, tri=YEL, bend=1.1, pulse=pul)
        # pizza: 2/3 tríceps
        cx, cy, r = 760, 1170, 190
        p = ease_out(prog(t, 0.3, 0.9))
        a_tri = 2 * math.pi * 0.62 * p
        c.new_path(); c.move_to(cx, cy); c.arc(cx, cy, r, -math.pi / 2, -math.pi / 2 + a_tri); c.close_path(); rgb(c, YEL); c.fill()
        c.new_path(); c.move_to(cx, cy); c.arc(cx, cy, r, -math.pi / 2 + a_tri, -math.pi / 2 + 2 * math.pi * p); c.close_path(); rgb(c, GREY); c.fill()
        if p > 0.95:
            txt(c, "TRÍCEPS", cx - 40, cy - 10, 54, INK); 
            txt(c, "BÍCEPS", cx - 95, cy - 80, 32, INK)
        tag(c, 540, 1620, "A MAIOR PARTE", YEL, INK, 66, back_out(prog(t, d * 0.45, 0.3)))
        txt(c, "O MÚSCULO DE TRÁS", 540, 1740, 46, WHITE, prog(t, d * 0.6, 0.3))

def three(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cols = [YEL, BLU, GRN]
        names = ["CABEÇA LONGA", "LATERAL", "MEDIAL"]
        hl = int(t * 1.1) % 3
        hc = tuple(cols[i] if i == hl or t < 0.8 else mix(cols[i], GREY, 0.6) for i in range(3))
        arm_view(c, 300, 880, 1.0, heads=hc, bend=1.1)
        for i, (n, col) in enumerate(zip(names, cols)):
            p = back_out(prog(t, 0.3 + i * 0.35, 0.3))
            y = 1000 + i * 150
            card(c, 790, y, 400, 110, CARD, p)
            if p > 0:
                disk(c, 640, y, 22, col, p); txt(c, n, 810, y + 18, 40, WHITE, p)
        # a longa: braço acima
        if t > d * 0.5:
            p = back_out(prog(t, d * 0.5, 0.3))
            tag(c, 790, 1520, "LONGA: BRAÇO ACIMA", YEL, INK, 42, p)
            arrow(c, 790, 1720, 790, 1580, YEL, 12, p=prog(t, d * 0.55, 0.3))
        tag(c, 300, 1720, "3 PARTES", CARD, WHITE, 52, back_out(prog(t, 0.2, 0.3)))

def overhead(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 + 0.5 * math.sin(t * 3.2)
        pose = pose_mix("point_up", "scratch", u * 0.55)
        hx, hy = chunky(c, 330, FLOOR_Y, 0.9, pose, face=1)
        dumbbell(c, hx, hy - 20, 0.9, 1.57)
        arrow(c, 330, 925, 330, 990, YEL, 10, p=prog(t, 0.3, 0.3))
        txt(c, "FRANCÊS", 330, 900, 44, YEL, prog(t, 0.3, 0.3))
        # polia por trás
        px = 800
        pp = back_out(prog(t, 0.35, 0.35))
        card(c, px, 1250, 190, 620, DARK, pp)
        if pp > 0:
            disk(c, px, 980, 36, GREY)
            sy = 1250 + 120 * u
            cap_line(c, px, 980, px - 140, 1080 + 40 * u, YEL, 8)
            rrect(c, px - 55, sy, 110, 120, 12, IRON)
            cap_line(c, px, 980, px, sy, STEEL, 6)
        mono(c, "POLIA POR TRÁS", px, 1620, 26, WHITE, prog(t, 0.6, 0.3))
        tag(c, 540, 1745, "BRAÇO LÁ EM CIMA", YEL, INK, 62, back_out(prog(t, d * 0.5, 0.3)))

def push(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 + 0.5 * math.sin(t * 3)
        # supino
        card(c, 300, 1230, 430, 700, CARD, back_out(prog(t, 0.1, 0.3)))
        rrect(c, 140, 1500, 320, 40, 10, IRON); cap_line(c, 200, 1540, 200, 1600, IRON, 14); cap_line(c, 400, 1540, 400, 1600, IRON, 14)
        by = lerp(1480, 1180, u)
        cap_line(c, 300, 1480, 300, by, STEEL, 12); barbell(c, 300, by, 0.5, 2)
        disk(c, 300, 1470, 34, L_FRONT, 0.0)
        arrow(c, 300, 1100, 300, 1020, YEL, 10, p=prog(t, 0.3, 0.3))
        txt(c, "SUPINO", 300, 940, 52, WHITE, prog(t, 0.2, 0.3))
        # mergulho
        card(c, 780, 1230, 430, 700, CARD, back_out(prog(t, 0.4, 0.3)))
        for xx in (680, 880): cap_line(c, xx, 1300, xx, 1540, IRON, 16); cap_line(c, xx - 40, 1300, xx + 40, 1300, STEEL, 16)
        dy = lerp(1230, 1330, u)
        disk(c, 780, dy - 60, 44, L_BODY); rrect(c, 745, dy - 20, 70, 130, 30, L_BODY)
        cap_line(c, 745, dy - 5, 680, 1300, L_FRONT, 26); cap_line(c, 815, dy - 5, 880, 1300, L_FRONT, 26)
        txt(c, "MERGULHO", 780, 940, 52, WHITE, prog(t, 0.5, 0.3))
        tag(c, 540, 1745, "TAMBÉM PEGAM O TRÍCEPS", YEL, INK, 50, back_out(prog(t, d * 0.55, 0.3)))

def volume(c, t, d, b):
    with Cam(c, t, punch=0.06):
        n = int(clamp((t - 0.2) / 0.12, 0, 10))
        pc = back_out(prog(t, 0.1, 0.3))
        pop(c, 540, 1060, pc); rrect(c, -230, -120, 460, 240, 36, (0.08, 0.09, 0.11))
        label(c, str(n), -70, 65, YEL, 190); label(c, "SÉRIES", 100, 40, WHITE, 52); c.restore()
        days = ["S", "T", "Q", "Q", "S", "S", "D"]
        for i, dd in enumerate(days):
            x = 130 + i * 136; on = i in (0, 3)
            p = back_out(prog(t, 0.6 + i * 0.07, 0.25))
            card(c, x, 1420, 110, 150, YEL if on else CARD, p, 20)
            if p > 0: txt(c, dd, x, 1475, 70, INK if on else GREY, p)
        for k, x in enumerate((130, 130 + 3 * 136)):
            p = back_out(prog(t, d * 0.5 + k * 0.4, 0.3))
            tag(c, x, 1260, "5 SÉRIES", WHITE, INK, 40, p)
        tag(c, 540, 1700, "DIVIDIDAS EM 2 DIAS", YEL, INK, 58, back_out(prog(t, d * 0.45, 0.3)))

def elbow(c, t, d, b):
    with Cam(c, t, punch=0.06, shake=3 if t < 1.4 else 0):
        arm_view(c, 330, 880, 1.0, bend=1.4)
        ring(c, 330, 1210, 100, t, RED)
        pb = back_out(prog(t, 0.3, 0.3))
        if pb > 0:
            pop(c, 330, 1210, pb); bolt(c, -30, -45, 30, 45, t, RED, 14); c.restore()
        txt(c, "DOEU", 330, 1370, 56, RED, prog(t, 0.4, 0.3))
        # menos peso
        pw = prog(t, d * 0.35, 0.4)
        dumbbell(c, 790, lerp(1000, 1000, pw), 1.4 - 0.5 * pw, 0.0)
        arrow(c, 790, 1100, 790, 1250, YEL, 12, p=pw)
        txt(c, "MENOS PESO", 790, 1340, 46, YEL, pw)
        if t > d * 0.62:
            p = back_out(prog(t, d * 0.62, 0.3))
            tag(c, 540, 1560, "OUTRA VARIAÇÃO", GRN, INK, 56, p)
            check_mark(c, 540, 1690, 0.9, prog(t, d * 0.7, 0.3))

def measure(c, t, d, b):
    with Cam(c, t, punch=0.06):
        arm_view(c, 400, 880, 1.05, bend=1.0)
        # fita ao redor do braço
        p = ease_out(prog(t, 0.3, 0.6))
        c.save(); c.translate(400, 1110); c.scale(1, 0.35)
        c.new_path(); c.arc(0, 0, 118, 0, 6.2832 * p); rgb(c, YEL); c.set_line_width(30); c.stroke(); c.restore()
        tape(c, 540, 1580, 860, t)
        mono(c, "SEMPRE DO MESMO JEITO", 540, 1660, 28, WHITE, prog(t, d * 0.55, 0.3))
        # calendário 1x/mês
        pc = back_out(prog(t, d * 0.3, 0.3))
        card(c, 840, 1050, 250, 270, (0.93, 0.92, 0.89), pc)
        if pc > 0:
            rrect(c, 715, 915, 250, 70, 20, RED, pc); txt(c, "1 VEZ", 840, 1130, 70, INK, pc); txt(c, "MÊS", 840, 970, 44, WHITE, pc)
        tag(c, 540, 1760, "FITA MÉTRICA", YEL, INK, 56, back_out(prog(t, 0.1, 0.3)))

def time(c, t, d, b):
    with Cam(c, t, punch=0.06):
        vals = [0.35, 0.38, 0.42, 0.46]
        bars(c, 540, 1500, 800, 520, vals, t, 0.3)
        for i, m in enumerate(["MÊS 1", "MÊS 2", "MÊS 3", "MÊS 4"]):
            mono(c, m, 540 - 400 + (i + 0.5) * 200, 1550, 24, GREY, prog(t, 0.4 + i * 0.2, 0.3))
        pt = back_out(prog(t, d * 0.4, 0.3))
        tag(c, 540, 1000, "+0,5 CM", GRN, INK, 90, pt)
        arrow(c, 300, 1250, 780, 1050, YEL, 12, p=prog(t, d * 0.4, 0.5))
        tag(c, 540, 1740, "CRESCE DEVAGAR", YEL, INK, 62, back_out(prog(t, 0.2, 0.3)))
        ring(c, 540, 1000, 190, t, GRN) if t > d * 0.5 else None

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="save", app_title="TRÍCEPS FRANCÊS", app_lines=[("S1  12 × 15 KG", None), ("S2  10 × 15 KG", None), ("S3  10 × 15 KG", None)])

VIS = {k: globals()[k] for k in "hook biceps triceps three overhead push volume elbow measure time cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.3, "pop"), (0.5, "pop"), (0.9, "buzz"), ("0.55d", "pop")],
    "biceps": [(0.0, "whoosh"), (0.3, "pop"), (0.6, "swish"), ("0.35d", "pop"), ("0.55d", "pop")],
    "triceps": [(0.0, "whoosh"), (0.3, "swish"), (1.0, "pop"), ("0.45d", "pop"), ("0.6d", "pop")],
    "three": [(0.0, "whoosh"), (0.3, "pop"), (0.65, "pop"), (1.0, "pop"), ("0.5d", "pop")],
    "overhead": [(0.0, "whoosh"), (0.3, "pop"), (0.35, "swish"), ("0.5d", "pop")],
    "push": [(0.0, "whoosh"), (0.1, "pop"), (0.4, "pop"), ("0.55d", "pop")],
    "volume": [(0.0, "whoosh"), (0.2, "tick"), (0.6, "tick"), (1.0, "tick"), (1.4, "tick"), ("0.5d", "pop"), ("0.5d+0.4", "pop")],
    "elbow": [(0.0, "whoosh"), (0.3, "buzz"), ("0.35d", "swish"), ("0.62d", "pop"), ("0.7d", "ding")],
    "measure": [(0.0, "whoosh"), (0.1, "pop"), (0.3, "swish"), ("0.3d", "pop"), ("0.55d", "click")],
    "time": [(0.0, "whoosh"), (0.2, "pop"), (0.3, "tick"), (0.5, "tick"), (0.7, "tick"), (0.9, "tick"), ("0.4d", "pop"), ("0.4d+0.3", "ding")],
    "cta": cta_sfx(BEAT_CTA, "save"),
}
