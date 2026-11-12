"""Cenas do BRIO 12 — parou 2 semanas: memória muscular."""
import math
from engine2 import *
from scenes_short02 import chip
from scenes_brio_05 import counter, tag, pop_in, CARD, INK
from scenes_brio_10 import card
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_12 as R
BEAT_CTA = R.BEATS[-1]
BLUE = (0.3, 0.6, 1.0)

def meter(c, x, y, w, h, frac, col=None, a=1.0):
    rrect(c, x - w / 2, y - h / 2, w, h, h / 2, (0.2, 0.22, 0.27), a)
    if frac > 0.02: rrect(c, x - w / 2, y - h / 2, w * frac, h, h / 2, col or YEL, a)

def hook(c, t, d, b):
    with Cam(c, t, punch=0.10):
        n = int(clamp((t - 0.3) / 1.8 * 14, 0, 14))
        for i in range(14):
            x = 150 + (i % 7) * 130; y = 900 + (i // 7) * 140
            card(c, x, y, 105, 105, CARD, r=16)
            label(c, str(i + 1), x, y + 22, GREY, 56)
            if i < n: x_mark(c, x, y, 0.7, 1.0)
        chunky(c, 300, FLOOR_Y, 0.7, pose_mix("idle", "shrug", prog(t, 1.2, 0.3)), face=1)
        if t > d * 0.5:
            pop_in(c, 760, 1500, back_out(prog(t, d * 0.5, 0.3))); tag(c, 0, 0, "PERDI TUDO?", YEL, INK, 70); c.restore()

def fear(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, l in enumerate(["VIAGEM", "GRIPE", "TRABALHO"]):
            p = back_out(prog(t, 0.2 + i * 0.5, 0.3))
            if p <= 0: continue
            pop_in(c, 290 + (i % 2) * 150, 960 + i * 150, p); card(c, 0, 0, 380, 110, CARD, r=30); label(c, l, 0, 22, WHITE, 60); c.restore()
        chunky(c, 900, FLOOR_Y, 0.75, "shock", face=-1)
        if t > d * 0.55:
            pop_in(c, 400, 1500, back_out(prog(t, d * 0.55, 0.3))); label(c, "MESES FORA?", 0, 0, RED, 100); c.restore()

def strength(c, t, d, b):
    with Cam(c, t, punch=0.06):
        barbell(c, 540, 1100, 1.2, 2)
        v = 1.0 - 0.04 * ease_out(prog(t, 0.5, 1.5))
        label(c, "FORÇA", 540, 1330, GREY, 56)
        meter(c, 540, 1420, 800, 60, v, GRN)
        label(c, f"{int(v * 100)}%", 540, 1560, WHITE, 100)
        check_mark(c, 860, 1560, 1.4, prog(t, d * 0.6, 0.3))
        if t > d * 0.7: chip(c, "CONTINUA LÁ", 540, 1760, YEL, INK, 62, t=t, start=d * 0.7)

def flat(c, t, d, b):
    with Cam(c, t, punch=0.06):
        k = 1 - 0.2 * ease(prog(t, 0.4, 0.8)) + 0.2 * ease(prog(t, d * 0.6, 0.7))
        c.save(); c.translate(380, 1250); c.scale(k, k); disk(c, 0, 0, 170, (0.9, 0.82, 0.75)); disk(c, 0, 0, 120, (0.85, 0.72, 0.65)); c.restore()
        label(c, "MÚSCULO", 380, 1520, WHITE, 56)
        for i in range(3):
            pp = (t * 0.6 + i / 3) % 1
            if t < d * 0.6: pp_a = 1 - pp
            else: pp_a = 0
            c.save(); c.translate(620 + i * 90, lerp(1150, 1000, pp)); c.scale(0.8, 0.8)
            c.move_to(0, -34); c.curve_to(30, 0, 28, 28, 0, 28); c.curve_to(-28, 28, -30, 0, 0, -34); rgb(c, BLUE, pp_a); c.fill(); c.restore()
        if t > 0.5: label(c, "MENOS ÁGUA", 780, 1260, BLUE, 52, a=prog(t, 0.5, 0.3)); label(c, "MENOS ENERGIA", 780, 1340, YEL, 52, a=prog(t, 0.9, 0.3))
        if t > d * 0.6:
            arrow(c, 380, 1000, 380, 900, GRN, 16, p=prog(t, d * 0.6, 0.3))
            chip(c, "VOLTA RÁPIDO", 540, 1740, GRN, INK, 62, t=t, start=d * 0.65)

def memory(c, t, d, b):
    with Cam(c, t, punch=0.06):
        label(c, "MEMÓRIA MUSCULAR", 540, 900, YEL, 80, a=prog(t, 0.1, 0.3))
        for i, (l, dur, col) in enumerate([("DO ZERO", 3.4, CARD), ("DE NOVO", 1.4, YEL)]):
            y = 1150 + i * 260
            draw_text(c, l, 90, y - 70, 40, WHITE, "Space Mono", spacing=3)
            meter(c, 540, y, 900, 70, clamp((t - 0.5) / dur, 0, 1), col if i else (0.6, 0.62, 0.68))
            if t - 0.5 > dur: check_mark(c, 960, y - 70, 0.7, prog(t, 0.5 + dur, 0.2))

def back(c, t, d, b):
    with Cam(c, t, punch=0.06):
        barbell(c, 540, 1050, 1.0, 2)
        v = 0.7 + 0.3 * ease(prog(t, d * 0.45, d * 0.35))
        pop_in(c, 540, 1280, back_out(prog(t, 0.2, 0.3))); tag(c, 0, 0, f"{int(v * 100)}% DA CARGA", YEL, INK, 72); c.restore()
        meter(c, 540, 1450, 800, 60, v)
        for i in range(3):
            x = 340 + i * 200; on = t > d * 0.45 + i * 0.5
            disk(c, x, 1600, 40, YEL if on else CARD)
            if on: check_mark(c, x, 1605, 0.5, 1.0, INK)
        label(c, "POUCOS TREINOS", 540, 1730, WHITE, 52, a=prog(t, d * 0.5, 0.3))

def ego(c, t, d, b):
    with Cam(c, t, punch=0.06, shake=8 * math.sin(t * 40) if t > d * 0.5 else 0):
        chunky(c, 330, FLOOR_Y, 0.85, "shock" if t > d * 0.5 else "bar_back", face=1)
        barbell(c, 760, 1400, 0.65, 4)
        pop_in(c, 760, 1260, back_out(prog(t, 0.2, 0.3))); tag(c, 0, 0, "TUDO DE NOVO", RED, WHITE, 56); c.restore()
        if t > d * 0.5:
            for i in range(3): ring(c, 330, 1250 + i * 130, 60, t + i * 0.3, RED)
            chip(c, "DOR FORTE", 540, 900, RED, WHITE, 66, t=t, start=d * 0.5)
            x_mark(c, 850, 1000, 1.4, prog(t, d * 0.7, 0.3))

def long_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        label(c, "MAIS DE 1 MÊS", 540, 920, WHITE, 70, a=prog(t, 0.1, 0.3))
        for i, (l, h, col) in enumerate([("1ª VEZ", 520, CARD), ("A VOLTA", 300, YEL)]):
            x = 280 + i * 420; g = ease_out(prog(t, 0.4 + i * 0.7, 0.7))
            rrect(c, x - 120, 1640 - h * g, 240, h * g + 1, 20, col); label(c, l, x, 1710, WHITE, 52)
        label(c, "MAIS LENTA", 280, 1060, GREY, 44, a=prog(t, 0.8, 0.3))
        label(c, "MAIS RÁPIDA", 700, 1260, YEL, 44, a=prog(t, 1.5, 0.3))
        pass  # 11/11: seta removida (ficava atrás da barra)

def know(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 300, FLOOR_Y, 0.85, "scratch", face=1)
        barbell(c, 760, 1500, 0.65, 3)
        pop_in(c, 760, 1260, back_out(prog(t, 0.3, 0.3))); label(c, "?? KG", 0, 0, YEL, 150); c.restore()
        for i in range(3):
            p = back_out(prog(t, 0.8 + i * 0.4, 0.3))
            pop_in(c, 200 + i * 90, 1000 - i * 40 + math.sin(t * 3 + i) * 6, p); label(c, "?", 0, 0, GREY, 100); c.restore()

def plan(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (l, sub, v) in enumerate([("SEMANA 1", "LEVE", 0.5), ("SEMANA 2", "QUASE NORMAL", 0.85), ("SEMANA 3", "SUAS CARGAS", 1.0)]):
            st = 0.2 + i * d * 0.25
            p = ease_out(prog(t, st, 0.35))
            if p <= 0: continue
            y = 1000 + i * 250; x = lerp(1300, 540, p)
            card(c, x, y, 900, 210, YEL if i == 2 else CARD, r=30)
            fg = INK if i == 2 else WHITE
            draw_text(c, l, x - 410, y - 45, 36, fg, "Space Mono", spacing=3)
            label(c, sub, x - 410 + 0, y + 25, fg, 64).__class__ if False else draw_text(c, sub, x - 410, y + 40, 64, fg, "Anton")
            meter(c, x + 200, y + 40, 320, 34, v * ease(prog(t, st + 0.3, 0.6)), INK if i == 2 else YEL)

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="send", text="seuamigo", app_title="SUPINO",
             app_lines=[("ÚLTIMA VEZ", None), ("60 KG × 8", None)], app_big="60 KG", app_big_label="ÚLTIMA CARGA", chart=False)

VIS = {k.rstrip("_"): v for k, v in list(globals().items()) if k.rstrip("_") in "hook fear strength flat memory back ego long know plan cta".split() and callable(v) and k != "meter"}
SFX = {k: [(0.0, "whoosh"), (0.3, "pop"), ("0.55d", "pop")] for k in VIS}
SFX["hook"] = [(0.0, "boom")] + [(0.3 + k * 0.13, "tick") for k in range(0, 14, 2)]
SFX["strength"] = [(0.0, "whoosh"), (0.5, "pop"), ("0.6d", "ding")]
SFX["ego"] = [(0.0, "whoosh"), ("0.5d", "buzz"), ("0.7d", "pop")]
SFX["plan"] = [(0.0, "whoosh"), (0.2, "swish"), ("0.45d", "swish"), ("0.7d", "swish")]
SFX["cta"] = cta_sfx(BEAT_CTA, "send")
