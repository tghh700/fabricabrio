"""Cenas do BRIO 13 — quantas repetições: 6 a 30."""
import math
from engine2 import *
from scenes_short02 import chip
from scenes_brio_05 import counter, tag, pop_in, CARD, INK
from scenes_brio_10 import card
from scenes_brio_12 import meter
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_13 as R
BEAT_CTA = R.BEATS[-1]
SKIN = (0.9, 0.82, 0.75)

def dumbbell(c, x, y, s=1.0, col=None):
    col = col or YEL
    c.save(); c.translate(x, y); c.scale(s, s)
    cap_line(c, -70, 0, 70, 0, (0.75, 0.76, 0.8), 16)
    for sx in (-1, 1): rrect(c, sx * 80 - 22, -50, 44, 100, 12, col)
    c.restore()

def hook(c, t, d, b):
    with Cam(c, t, punch=0.10):
        pop_in(c, 540, 1050, back_out(prog(t, 0.1, 0.35))); label(c, "8 A 12", 0, 90, WHITE, 280); c.restore()
        if t > d * 0.4: pop_in(c, 540, 1050, back_out(prog(t, d * 0.4, 0.3))); label(c, "?", 380, -90, YEL, 220); c.restore()
        g = ease_out(prog(t, d * 0.55, 0.6))
        rrect(c, 140, 1360, 800, 60, 30, (0.2, 0.22, 0.27))
        rrect(c, 140 + 800 * (6 - 6) / 24 * 1.0, 1360, 800 * g, 60, 30, YEL)
        label(c, "6", 140, 1500, WHITE, 70, a=g); label(c, "30", 940, 1500, WHITE, 70, a=g)
        chunky(c, 540, FLOOR_Y + 60, 0.3, "flex", face=1)

def myth(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pop_in(c, 540, 1180, back_out(prog(t, 0.15, 0.35)))
        card(c, 0, 0, 820, 460, (0.93, 0.92, 0.89), r=40)
        label(c, "8 A 12", 0, 50, INK, 230); draw_text(c, "REGRA DA ACADEMIA", 0, -160, 36, INK, "Space Mono", align="center", spacing=3)
        c.restore()
        if t > d * 0.5:
            pop_in(c, 540, 1620, back_out(prog(t, d * 0.5, 0.3))); tag(c, 0, 0, "FUNCIONA, MAS NÃO É A ÚNICA", YEL, INK, 50); c.restore()
        check_mark(c, 880, 980, 1.4, prog(t, d * 0.35, 0.3))

def science(c, t, d, b):
    with Cam(c, t, punch=0.06):
        label(c, "6 A 30 REPS", 540, 960, YEL, 90, a=prog(t, 0.1, 0.3))
        for i, r in enumerate([6, 15, 30]):
            x = 210 + i * 330; p = back_out(prog(t, 0.4 + i * 0.5, 0.35))
            if p <= 0: continue
            pop_in(c, x, 1300, p); disk(c, 0, 0, 130, SKIN); disk(c, 0, 0, 90, (0.85, 0.72, 0.65)); c.restore()
            label(c, f"{r}", x, 1520, WHITE, 90, a=min(1, p))
        label(c, "=", 375, 1330, GREY, 90, a=prog(t, 1.2, 0.3)); label(c, "=", 705, 1330, GREY, 90, a=prog(t, 1.6, 0.3))
        if t > d * 0.7: chip(c, "CRESCE PARECIDO", 540, 1740, WHITE, INK, 62, t=t, start=d * 0.7)

def catch(c, t, d, b):
    with Cam(c, t, punch=0.06):
        n = int(clamp((t - 0.3) / (d * 0.5) * 10, 0, 10))
        for i in range(10):
            x = 150 + i * 87; last = i >= 7
            disk(c, x, 1100, 34, (YEL if not last else (0.35, 0.37, 0.42)) if i < n else CARD)
        label(c, "SÉRIE", 540, 980, GREY, 56)
        if t > d * 0.55:
            pop_in(c, 800, 1300, back_out(prog(t, d * 0.55, 0.3))); label(c, "SOBRAM 3", 0, 0, WHITE, 70); c.restore()
            arrow(c, 800, 1250, 800, 1180, YEL, 10, p=1)
        chunky(c, 330, FLOOR_Y, 0.7, pose_mix("curl_up", "tired", prog(t, d * 0.5, 0.4)), face=1)
        pop_in(c, 760, 1500, back_out(prog(t, d * 0.65, 0.3))); tag(c, 0, 0, "PERTO DO LIMITE", YEL, INK, 60); c.restore()

def light(c, t, d, b):
    with Cam(c, t, punch=0.06):
        lift = (math.sin(t * 4) + 1) / 2
        chunky(c, 300, FLOOR_Y, 0.85, pose_mix("curl_down", "curl_up", lift), face=1)
        n = clamp(int(t / (d * 0.8) * 25) + 1, 1, 25)
        counter(c, 760, 1180, int(n), 0.9, YEL if n > 20 else WHITE)
        dumbbell(c, 760, 1500, 1.0, (0.6, 0.62, 0.68)); label(c, "LEVE", 760, 1620, GREY, 52)
        if t > d * 0.5:
            for i in range(3): spark(c, 600 + i * 160, 960 - (i % 2) * 40, 1.0, t + i)
            chip(c, "QUEIMA MAIS", 540, 1780, YEL, INK, 60, t=t, start=d * 0.5)

def heavy(c, t, d, b):
    with Cam(c, t, punch=0.06):
        lift = (math.sin(t * 2.2) + 1) / 2
        barbell(c, 540, 1480 - lift * 140, 1.0, 4)
        counter(c, 540, 1050, clamp(int(t / (d * 0.8) * 6) + 1, 1, 6), 0.8, WHITE)
        if t > d * 0.45:
            ring(c, 540, 1480, 120, t, RED)
            pop_in(c, 540, 1700, back_out(prog(t, d * 0.45, 0.3))); tag(c, 0, 0, "ARTICULAÇÃO CANSA", RED, WHITE, 56); c.restore()
        label(c, "PESADO", 840, 1000, GREY, 52)

def mix(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (l, r, big) in enumerate([("GRANDES", "6 A 10", True), ("PEQUENOS", "15 A 20", False)]):
            st = 0.2 + i * d * 0.35
            p = back_out(prog(t, st, 0.35))
            if p <= 0: continue
            y = 1070 + i * 330
            pop_in(c, 540, y, p); card(c, 0, 0, 900, 290, YEL if big else CARD, r=36)
            fg = INK if big else WHITE
            label(c, l, -250, -20, fg, 70); label(c, r, -250, 80, fg, 100)
            if big: barbell(c, 250, 0, 0.45, 2, INK)
            else: dumbbell(c, 250, 0, 1.0, YEL)
            c.restore()

def example(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (l, r) in enumerate([("AGACHAMENTO", "6 A 10"), ("ELEVAÇÃO LATERAL", "15 A 20")]):
            st = 0.2 + i * d * 0.3
            p = ease_out(prog(t, st, 0.35))
            if p <= 0: continue
            y = 1020 + i * 260; x = lerp(1300, 540, p)
            card(c, x, y, 900, 220, CARD, r=30)
            draw_text(c, l, x - 410, y - 30, 56, WHITE, "Anton"); draw_text(c, r + " REPS", x - 410, y + 60, 56, YEL, "Anton")
        if t > d * 0.6:
            p = ease_out(prog(t, d * 0.6, 0.5))
            meter(c, 540, 1620, 800 * p + 1, 50, 1.0, YEL)
            label(c, "TUDO PERTO DO LIMITE", 540, 1720, WHITE, 56, a=p)

def track(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pop_in(c, 300, 1150, back_out(prog(t, 0.2, 0.3))); counter(c, 0, 0, 10 + (1 if t > d * 0.45 else 0), 0.85, YEL if t > d * 0.45 else WHITE); c.restore()
        label(c, "+1 REP", 300, 1400, WHITE, 60, a=prog(t, d * 0.45, 0.3))
        pop_in(c, 790, 1150, back_out(prog(t, d * 0.4, 0.3))); barbell(c, 0, 0, 0.55, 2); tag(c, 0, -170, "20 → 22,5 KG", YEL, INK, 46); c.restore()
        label(c, "OU", 540, 1180, GREY, 56)
        arrow(c, 540, 1700, 540, 1460, YEL, 16, p=prog(t, d * 0.55, 0.4))
        label(c, "PROGREDIR", 540, 1780, YEL, 70, a=prog(t, d * 0.6, 0.3))

def rest(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (l, tm, w, col) in enumerate([("PESADA", "3 MIN", 760, YEL), ("LEVE", "1 MIN", 260, CARD)]):
            y = 1060 + i * 330
            draw_text(c, f"SÉRIE {l}", 90, y - 90, 44, WHITE, "Space Mono", spacing=3)
            g = ease(prog(t, 0.3 + i * 0.8, 1.2))
            rrect(c, 90, y - 40, 900, 80, 40, (0.2, 0.22, 0.27))
            rrect(c, 90, y - 40, w * g + 1, 80, 40, col if i == 0 else (0.6, 0.62, 0.7))
            label(c, tm, 900, y + 125, WHITE, 70, a=prog(t, 0.3 + i * 0.8, 0.3))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="save", text="", app_title="SÉRIES",
             app_lines=[("S1 · 20 KG × 15", None), ("S2 · 20 KG × 14", None)], app_big="ANOTADO", app_big_label="CADA SÉRIE", chart=False)

VIS = {k: globals()[k] for k in "hook myth science catch light heavy mix example track rest cta".split()}
SFX = {k: [(0.0, "whoosh"), (0.3, "pop"), ("0.55d", "pop")] for k in VIS}
SFX["hook"] = [(0.0, "boom"), (0.1, "pop"), ("0.4d", "pop"), ("0.55d", "swish")]
SFX["science"] = [(0.0, "whoosh"), (0.4, "pop"), (0.9, "pop"), (1.4, "pop"), ("0.7d", "ding")]
SFX["light"] = [(0.0, "whoosh")] + [(0.4 + k * 0.7, "tick") for k in range(5)] + [("0.5d", "ding")]
SFX["heavy"] = [(0.0, "whoosh"), (0.5, "clack"), ("0.45d", "buzz")]
SFX["mix"] = [(0.0, "whoosh"), (0.2, "pop"), ("0.35d", "pop")]
SFX["track"] = [(0.0, "whoosh"), (0.2, "pop"), ("0.45d", "ding"), ("0.4d", "pop"), ("0.55d", "swish")]
SFX["cta"] = cta_sfx(BEAT_CTA, "save")
