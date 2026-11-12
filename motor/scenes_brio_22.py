"""BRIO 22 — 5 erros de iniciante."""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_22 as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        chunky(c, 280, FLOOR_Y, 0.9, pose_mix("idle", "shrug", prog(t, 0.3, 0.3)), face=1)
        pop(c, 280, 1040, back_out(prog(t, 0.5, 0.3))); label(c, "?", 0, 60, YEL, 190); c.restore()
        for i in range(5):
            p = back_out(prog(t, 0.3 + i * 0.28, 0.3))
            x = 620 + (i % 2) * 220; y = 1000 + (i // 2) * 230
            if i == 4: x = 730
            if p > 0:
                pop(c, x, y, p); disk(c, 0, 0, 90, RED); label(c, str(i + 1), 0, 38, WHITE, 110); c.restore()
        txt(c, "ERROS", 730, 1610, 70, YEL, prog(t, 1.9, 0.3))

def e1(c, t, d, b):
    with Cam(c, t, punch=0.06):
        names = ["SEMANA 1", "SEMANA 2", "SEMANA 3", "SEMANA 4"]
        cols = [BLU, GRN, RED, YEL]
        for i in range(4):
            x = 300 + (i % 2) * 480; y = 1000 + (i // 2) * 330
            p = back_out(prog(t, 0.1 + i * 0.3, 0.3))
            card(c, x, y, 420, 270, CARD, p)
            if p > 0:
                mono(c, names[i], x, y - 85, 26, GREY, p)
                k = (i + int(t * 1.2)) % 4
                if k == 0: barbell(c, x, y + 20, 0.42, 1, cols[i])
                elif k == 1: dumbbell(c, x, y + 20, 1.5, 0.0, cols[i])
                elif k == 2: disk(c, x, y + 20, 60, cols[i]); disk(c, x, y + 20, 22, CARD)
                else: bolt(c, x - 50, y - 30, x + 50, y + 70, t, cols[i], 14)
        x_mark(c, 540, 1500, 0.9, prog(t, d * 0.4, 0.3))
        tag(c, 540, 1690, "NUNCA SABE", RED, WHITE, 62, back_out(prog(t, d * 0.5, 0.3)))
        txt(c, "?", 800, 1560, 150, YEL, prog(t, d * 0.6, 0.3))

def e2(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 760, FLOOR_Y, 0.95, pose_mix("flex", "idle", 0.5 + 0.5 * math.sin(t * 3)), dark=True, face=-1, bob=-6 * abs(math.sin(t * 3)))
        barbell(c, 760, 1000, 0.4, 3)
        card(c, 760, 900, 300, 80, DARK, back_out(prog(t, 0.2, 0.3)))
        mono(c, "MAIS FORTE", 760, 910, 26, WHITE, prog(t, 0.3, 0.3))
        hx, hy = chunky(c, 270, FLOOR_Y, 0.7, pose_mix("idle", "reach", prog(t, d * 0.2, 0.3)), face=1)
        thought(c, 290, 1130, 300, 110, back_out(prog(t, 0.5, 0.35)))
        txt(c, "COPIAR?", 290, 1150, 58, INK, prog(t, 0.6, 0.3))
        arrow(c, 440, 1290, 600, 1290, YEL, 14, p=prog(t, 0.7, 0.4))
        if t > d * 0.5:
            tag(c, 540, 1745, "OUTRA FASE", YEL, INK, 64, back_out(prog(t, d * 0.5, 0.3)))
            x_mark(c, 270, 940, 0.8, prog(t, d * 0.6, 0.3))

def e3(c, t, d, b):
    shk = 5 * (0.5 + 0.5 * math.sin(t * 9)) if t > 0.4 else 0
    with Cam(c, t, punch=0.06, shake=shk):
        sag = prog(t, 0.2, 0.8)
        pose = pose_mix("bar_back", "squat_half", sag * 0.5)
        chunky(c, 400, FLOOR_Y, 0.85, pose, face=1, bob=sag * 20)
        barbell(c, 400, 1640 - 460 * 0.85 + sag * 70, 0.5, 4)
        x_mark(c, 400, 900, 0.7, prog(t, 0.5, 0.3))
        # balança: peso vs técnica
        card(c, 830, 1250, 340, 560, CARD, back_out(prog(t, 0.2, 0.3)))
        order = [("1", "TÉCNICA", GRN), ("2", "CARGA", YEL)]
        for i, (n, s, col) in enumerate(order):
            p = back_out(prog(t, d * 0.45 + i * 0.5, 0.3))
            if p > 0:
                pop(c, 830, 1130 + i * 250, p); disk(c, 0, -20, 62, col); label(c, n, 0, 22, INK, 80); label(c, s, 0, 130, WHITE, 52); c.restore()
        arrow(c, 955, 1190, 955, 1330, WHITE, 8, p=prog(t, d * 0.45 + 0.3, 0.3))
        tag(c, 400, 1745, "PESO DEMAIS", RED, WHITE, 60, back_out(prog(t, 0.3, 0.3)))

def e4(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 260, FLOOR_Y, 0.85, "idle", face=1)
        # perna destacada
        ring(c, 260, 1400, 140, t, YEL)
        names = ["PERNA", "PEITO", "BRAÇO"]
        bars(c, 700, 1560, 470, 560, [1.0, 0.42, 0.28], t, 0.2, [YEL, GREY, GREY])
        for i, n in enumerate(names):
            mono(c, n, 700 - 235 + (i + 0.5) * 470 / 3, 1605, 24, WHITE if i == 0 else GREY, prog(t, 0.4 + i * 0.2, 0.3))
        # energia
        p = back_out(prog(t, d * 0.55, 0.3))
        if p > 0:
            pop(c, 700, 920, p); bolt(c, -40, -60, 30, 40, t, YEL, 16); c.restore()
            txt(c, "ENERGIA", 700, 1010, 50, YEL, p)
        x_mark(c, 260, 900, 0.7, prog(t, 0.3, 0.3))
        tag(c, 260, 1745, "PULAR PERNA", RED, WHITE, 56, back_out(prog(t, 0.2, 0.3)))

def e5(c, t, d, b):
    with Cam(c, t, punch=0.06):
        notebook(c, 640, 1250, 620, 620, back_out(prog(t, 0.1, 0.35)))
        for i, s in enumerate(["CARGA ?", "REPS ?"]):
            p = back_out(prog(t, 0.6 + i * 0.5, 0.3))
            if p > 0:
                pop(c, 690, 1160 + i * 160, p); label(c, s, 0, 20, RED, 90); c.restore()
        chunky(c, 190, FLOOR_Y, 0.75, pose_mix("idle", "scratch", 0.5 + 0.5 * math.sin(t * 5)), face=1)
        x_mark(c, 640, 920, 0.7, prog(t, 0.3, 0.3))
        if t > d * 0.45:
            card(c, 640, 1500, 420, 90, DARK, back_out(prog(t, d * 0.45, 0.3)))
            mono(c, "SEMANA SEGUINTE", 640, 1512, 26, WHITE, prog(t, d * 0.5, 0.3))
        tag(c, 540, 1745, "NÃO ANOTOU", RED, WHITE, 58, back_out(prog(t, d * 0.3, 0.3)))

def secret(c, t, d, b):
    with Cam(c, t, punch=0.06):
        items = ["POUCOS EXERCÍCIOS", "BEM FEITOS", "POR SEMANAS"]
        for i, s in enumerate(items):
            p = back_out(prog(t, 0.15 + i * 0.7, 0.3))
            y = 1000 + i * 190
            card(c, 540, y, 860, 150, CARD, p)
            if p > 0:
                txt(c, s, 500, y + 20, 64, WHITE, p)
                check_mark(c, 900, y, 0.7, prog(t, 0.35 + i * 0.7, 0.25))
        # ciclo repetindo
        ang = t * 2
        cx, cy = 540, 1630
        c.new_path(); c.arc(cx, cy, 70, ang, ang + 4.6); rgb(c, YEL); c.set_line_width(16); c.set_line_cap(1); c.stroke()
        a = ang + 4.6; poly(c, [(cx + 70 * math.cos(a) - 30, cy + 70 * math.sin(a) - 15), (cx + 70 * math.cos(a) + 15, cy + 70 * math.sin(a) + 10), (cx + 70 * math.cos(a) - 10, cy + 70 * math.sin(a) + 40)], YEL, 10)
        tag(c, 780, 1640, "REPETE", YEL, INK, 54, back_out(prog(t, d * 0.6, 0.3)))

def first(c, t, d, b):
    with Cam(c, t, punch=0.06):
        calendar(c, 540, 1230, 7, 4, 108, 12, t, 0.3, 10)
        txt(c, "PRIMEIRO MÊS", 540, 880, 54, YEL, prog(t, 0.1, 0.3))
        chunky(c, 240, FLOOR_Y, 0.6, "walk1" if int(t * 3) % 2 else "walk2", face=1, bob=-8 * abs(math.sin(t * 6)))
        tag(c, 700, 1590, "APRENDER", YEL, INK, 56, back_out(prog(t, d * 0.35, 0.3)))
        tag(c, 760, 1730, "CRIAR O HÁBITO", GRN, INK, 52, back_out(prog(t, d * 0.6, 0.3)))

def help(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 800, FLOOR_Y, 0.9, pose_mix("idle", "thumb", prog(t, d * 0.45, 0.3)), dark=True, face=-1)
        chunky(c, 270, FLOOR_Y, 0.85, pose_mix("idle", "point_up", prog(t, 0.2, 0.3)), face=1)
        card(c, 270, 1010, 200, 150, (0.93, 0.92, 0.89), back_out(prog(t, 0.3, 0.3)))
        txt(c, "?", 270, 1080, 130, INK, prog(t, 0.4, 0.3))
        tag(c, 800, 960, "PROFESSOR", DARK, WHITE, 48, back_out(prog(t, 0.2, 0.3)))
        if t > d * 0.45:
            p = back_out(prog(t, d * 0.45, 0.3)); pop(c, 800, 1130, p)
            rrect(c, -90, -70, 180, 140, 30, GRN); c.restore()
            check_mark(c, 800, 1135, 1.0, prog(t, d * 0.45 + 0.1, 0.3), WHITE)
        arrow(c, 440, 1250, 640, 1250, YEL, 14, p=prog(t, 0.6, 0.4))
        tag(c, 540, 1745, "PEDE AJUDA", YEL, INK, 62, back_out(prog(t, d * 0.55, 0.3)))

def bonus(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 780, FLOOR_Y, 0.95, "flex", dark=True, face=-1, bob=-5 * abs(math.sin(t * 3)))
        mono(c, "QUEM TREINA HÁ ANOS", 780, 930, 24, GREY)
        x_mark(c, 780, 1060, 0.9, prog(t, 0.3, 0.3))
        chunky(c, 250, FLOOR_Y, 0.6, "idle", face=1)
        if t > d * 0.45:
            p = back_out(prog(t, d * 0.45, 0.3))
            # ontem vs hoje
            pop(c, 250, 1050, p); rrect(c, -200, -50, 400, 100, 24, GRN); c.restore()
            txt(c, "VOCÊ DO MÊS PASSADO", 250, 1075, 34, INK, p)
            arrow(c, 250, 1420, 250, 1250, GRN, 14, p=prog(t, d * 0.55, 0.4))
            ring(c, 250, 1300, 150, t, GRN)
        tag(c, 540, 1745, "BÔNUS: NÃO COMPARA", YEL, INK, 56, back_out(prog(t, 0.2, 0.3)))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="send", text="amigo", app_title="SÉRIES", app_lines=[("SUPINO  3×10", None), ("AGACHAR  3×12", None), ("REMADA  3×10", None)])

VIS = {k: globals()[k] for k in "hook e1 e2 e3 e4 e5 secret first help bonus cta".split()}
W_ = lambda: [(0.0, "whoosh")]
SFX = {
    "hook": [(0.0, "boom"), (0.3, "pop"), (0.58, "pop"), (0.86, "pop"), (1.14, "pop"), (1.42, "pop")],
    "e1": [(0.0, "whoosh"), (0.1, "pop"), (0.4, "pop"), (0.7, "pop"), (1.0, "pop"), ("0.4d", "buzz")],
    "e2": [(0.0, "whoosh"), (0.5, "pop"), ("0.5d", "pop"), ("0.6d", "buzz")],
    "e3": [(0.0, "whoosh"), (0.3, "pop"), (0.5, "buzz"), ("0.45d", "pop"), ("0.45d+0.5", "pop")],
    "e4": [(0.0, "whoosh"), (0.2, "pop"), (0.4, "pop"), ("0.55d", "zip")],
    "e5": [(0.0, "whoosh"), (0.3, "buzz"), (0.6, "pop"), (1.1, "pop")],
    "secret": [(0.0, "whoosh"), (0.15, "pop"), (0.85, "pop"), (1.55, "pop"), ("0.6d", "pop")],
    "first": [(0.0, "whoosh"), (0.3, "tick"), (0.9, "tick"), (1.5, "tick"), ("0.35d", "pop"), ("0.6d", "pop")],
    "help": [(0.0, "whoosh"), (0.3, "pop"), ("0.45d", "ding"), ("0.55d", "pop")],
    "bonus": [(0.0, "whoosh"), (0.2, "pop"), (0.3, "buzz"), ("0.45d", "pop"), ("0.55d", "swish")],
    "cta": cta_sfx(BEAT_CTA, "send"),
}
