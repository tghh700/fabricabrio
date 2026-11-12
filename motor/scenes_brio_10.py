"""Cenas do BRIO 10 — 30 dias de treino."""
import math
from engine2 import *
from scenes_short02 import chip
from scenes_brio_05 import counter, tag, pop_in, CARD, INK
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_10 as R
BEAT_CTA = R.BEATS[-1]

def card(c, x, y, w, h, col=CARD, a=1.0, r=24): rrect(c, x - w / 2, y - h / 2, w, h, r, col, a)

def hook(c, t, d, b):
    with Cam(c, t, punch=0.10):
        rgb(c, GREY); c.set_line_width(10); c.move_to(120, 1450); c.line_to(960, 1450); c.stroke()
        days = [1, 3, 7, 14, 30]
        xs = [120 + i * 210 for i in range(5)]
        for i, (dd, x) in enumerate(zip(days, xs)):
            p = back_out(prog(t, 0.3 + i * 0.35, 0.3))
            if p <= 0: continue
            pop_in(c, x, 1450, p)
            disk(c, 0, 0, 34, YEL if dd == 30 else WHITE)
            c.restore()
            label(c, str(dd), x, 1370, YEL if dd == 30 else WHITE, 70, a=min(1, p))
            label(c, "DIA", x, 1560, GREY, 36, a=min(1, p))
        f = ease(prog(t, 0.2, 2.4))
        chunky(c, lerp(120, 960, f), 1440, 0.55, "walk1" if int(t * 4) % 2 else "walk2", face=1)
        if t > d * 0.5:
            pop_in(c, 540, 1000, back_out(prog(t, d * 0.5, 0.3))); label(c, "?", 0, 100, YEL, 280); c.restore()

def d1(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 300, FLOOR_Y, 0.85, pose_mix("idle", "shrug", prog(t, 0.2, 0.3)), face=1)
        for i, (txt, x, y) in enumerate([("CARGA?", 720, 1000), ("ORDEM?", 820, 1200), ("FEZ POUCO?", 640, 1400)]):
            p = back_out(prog(t, 0.4 + i * 0.5, 0.3))
            if p <= 0: continue
            pop_in(c, x, y + math.sin(t * 3 + i) * 8, p)
            font(c, "Anton", 60); w = c.text_extents(txt).x_advance + 70
            card(c, 0, 0, w, 100, CARD, r=30); label(c, txt, 0, 22, YEL if i == 2 else WHITE, 60); c.restore()

def d3(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 540, FLOOR_Y, 0.9, "tired", face=1, bob=math.sin(t * 3) * 6)
        for i, (x, y) in enumerate([(430, 1500), (650, 1500), (330, 1180), (760, 1180)]):
            p = prog(t, 0.3 + i * 0.25, 0.3)
            if p > 0:
                disk(c, x, y, 55 * (1 + 0.2 * math.sin(t * 7 + i)), RED, 0.35 * p)
                ring(c, x, y, 70, t + i * 0.3, RED)
        if t > d * 0.55:
            chip(c, "NORMAL E PASSA", 540, 900, WHITE, INK, 62, t=t, start=d * 0.55)
            check_mark(c, 900, 1000, 1.5, prog(t, d * 0.65, 0.3))

def d7(c, t, d, b):
    with Cam(c, t, punch=0.06):
        ph = (math.sin(t * 3) + 1) / 2
        chunky(c, 330, FLOOR_Y, 0.85, pose_mix("squat_half", "squat_deep", ph), face=1)
        # cérebro -> músculo
        p = back_out(prog(t, 0.3, 0.35))
        pop_in(c, 760, 1050, p)
        disk(c, -40, 0, 70, LILAC); disk(c, 40, 0, 70, LILAC)
        rgb(c, INK); c.set_line_width(8); c.move_to(0, -60); c.line_to(0, 60); c.stroke()
        c.restore()
        label(c, "CÉREBRO", 760, 1200, WHITE, 56, a=prog(t, 0.5, 0.3))
        bolt(c, 760, 1230, 600, 1480, t, YEL) if t > 0.8 else None
        if t > d * 0.55:
            chip(c, "MAIS FIRME", 700, 1730, YEL, INK, 64, t=t, start=d * 0.55)

def d14(c, t, d, b):
    with Cam(c, t, punch=0.06):
        lift = (math.sin(t * 3) + 1) / 2
        chunky(c, 300, FLOOR_Y, 0.85, pose_mix("curl_down", "curl_up", lift), face=1)
        barbell(c, 790, 1560, 0.6, 2)
        p = back_out(prog(t, 0.3, 0.3))
        pop_in(c, 790, 1380, p); tag(c, 0, 0, "ERA PESADO", WHITE, INK, 52); c.restore()
        if t > d * 0.4:
            pop_in(c, 790, 1000, back_out(prog(t, d * 0.4, 0.35)))
            label(c, "FÁCIL", 0, 0, YEL, 170); c.restore()
            ring(c, 790, 960, 200, t, YEL)
        if t > d * 0.7:
            chip(c, "1ª VITÓRIA", 540, 1750, YEL, INK, 64, t=t, start=d * 0.7)

def mirror(c, t, d, b):
    with Cam(c, t, punch=0.06):
        card(c, 540, 1280, 560, 800, (0.14, 0.16, 0.2), r=40)
        rgb(c, LILAC); c.set_line_width(10)
        rrect(c, 260, 880, 560, 800, 40, (0.14, 0.16, 0.2), 0.0)
        chunky(c, 540, 1620, 0.8, "idle", face=1, bob=math.sin(t * 3) * 3)
        sh = (int(t * 10) % 2) * 0.12
        c.save(); c.translate(0, 0); c.restore()
        label(c, "= IGUAL", 540, 960, WHITE, 70, a=prog(t, 0.4, 0.3))
        x_mark(c, 860, 1000, 1.4, prog(t, d * 0.4, 0.3))
        if t > d * 0.6:
            chip(c, "NÃO DESISTE", 540, 1760, YEL, INK, 64, t=t, start=d * 0.6)

def d30(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (lab, h, col) in enumerate([("DIA 1", 260, CARD), ("DIA 30", 560, YEL)]):
            x = 200 + i * 330
            g = ease_out(prog(t, 0.2 + i * 0.5, 0.7))
            rrect(c, x - 110, 1560 - h * g, 220, h * g + 1, 20, col)
            label(c, lab, x, 1620, WHITE if i == 0 else YEL, 56)
        arrow(c, 220, 1180, 415, 985, YEL, 14, p=prog(t, d * 0.45, 0.4))  # 11/11: fora da barra
        chunky(c, 880, FLOOR_Y - 20, 0.5, "flex", face=-1)
        if t > d * 0.6:
            chip(c, "HÁBITO", 540, 900, WHITE, INK, 62, t=t, start=d * 0.6)

def muscle(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for m in range(6):
            x = 150 + m * 155; p = back_out(prog(t, 0.2 + m * 0.4, 0.3))
            if p <= 0: continue
            pop_in(c, x, 930, p)
            card(c, 0, 0, 130, 130, YEL if m == 5 else CARD, r=20)
            label(c, str(m + 1), 0, 25, INK if m == 5 else WHITE, 80); c.restore()
        label(c, "MESES", 540, 1060, GREY, 60, a=prog(t, 0.3, 0.3))
        chunky(c, 540, FLOOR_Y, 0.72, pose_mix("idle", "flex", prog(t, d * 0.55, 0.4)), face=1)
        if t > d * 0.55: spark(c, 760, 1350, 1.3, t)
        if t > d * 0.75: chip(c, "NÃO PARA", 540, 1780, YEL, INK, 60, t=t, start=d * 0.75)

def proof(c, t, d, b):
    with Cam(c, t, punch=0.06):
        vals = ["40", "42,5", "45", "47,5"]
        for i, v in enumerate(vals):
            p = ease_out(prog(t, 0.2 + i * 0.45, 0.4))
            if p <= 0: continue
            w = 260; h = 160 + i * 110
            x = 200 + i * 230
            rrect(c, x - w / 2 + 40, 1600 - h * p, w - 60, h * p + 1, 18, YEL if i == 3 else CARD)
            label(c, v, x + 40, 1600 - h * p - 20, WHITE, 52, a=p)
            label(c, f"SEM {i+1}", x + 40, 1660, GREY, 36)
        label(c, "KG", 130, 930, GREY, 46)
        arrow(c, 240, 1340, 920, 1010, YEL, 12, p=prog(t, d * 0.55, 0.45))  # acima das barras, depois que elas sobem

def habit(c, t, d, b):
    with Cam(c, t, punch=0.06):
        n = int(clamp((t - 0.2) / (d * 0.7) * 30, 0, 30))
        for i in range(30):
            x = 160 + (i % 6) * 150; y = 920 + (i // 6) * 130
            on = i < n
            card(c, x, y, 110, 100, YEL if on else CARD, r=18)
            if on: check_mark(c, x, y + 8, 0.5, 1.0, INK)
        if t > d * 0.75:
            chip(c, "MESMO SEM VONTADE", 540, 1700, WHITE, INK, 58, t=t, start=d * 0.75)
            ring(c, 540, 1180, 420, t, YEL)

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="DIA UM", app_title="SUPINO",
             app_lines=[("SEM 1 · 40 KG", None), ("SEM 2 · 42,5 KG", None)], app_big="COMPARAR", app_big_label="DIA 1 x DIA 30", chart=True)

VIS = {k: globals()[k] for k in "hook d1 d3 d7 d14 mirror d30 muscle proof habit cta".split()}
def _w(): return [(0.0, "whoosh")]
SFX = {k: [(0.0, "whoosh"), (0.4, "pop"), ("0.5d", "pop")] for k in VIS}
SFX["hook"] = [(0.0, "boom")] + [(0.3 + i * 0.35, "pop") for i in range(5)]
SFX["d7"] = [(0.0, "whoosh"), (0.8, "zip")]
SFX["proof"] = [(0.0, "whoosh")] + [(0.2 + i * 0.45, "tick") for i in range(4)]
SFX["habit"] = [(0.0, "whoosh"), ("0.75d", "ding")]
SFX["cta"] = cta_sfx(BEAT_CTA, "bubble")
