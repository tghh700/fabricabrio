"""Cenas do BRIO 21 — dá pra ganhar músculo sem peso?"""
import math
from engine2 import *
from scenes_short02 import chip
from scenes_brio_18 import pop_in, tag, card, calendar, INK, CARD, DARK
import roteiro_brio_21 as R
from cta_brio import cta_brio, cta_sfx

def pushup(c, x, y, s, u, feet_up=0.0, col=None):
    """flexão de lado. u 0=em cima 1=embaixo. feet_up = altura do apoio dos pés."""
    c.save(); c.translate(x, y); c.scale(s, s)
    fy = -feet_up
    if feet_up > 0: rrect(c, 470, -feet_up, 150, feet_up, 14, YEL)
    hx, hy = -230, 0
    sy = -150 + 100 * u; fx = 470
    sh = (-190, sy - 20); ft = (fx, fy - 30)
    cap_line(c, sh[0], sh[1], ft[0], ft[1], L_BODY, 90)
    disk(c, sh[0] - 70, sh[1] - 25, 58, L_BODY)
    cap_line(c, sh[0], sh[1], -190, 0, L_FRONT, 38)
    c.restore()

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        chunky(c, 300, FLOOR_Y, 0.9, pose_mix("idle", "flex", prog(t, 0.2, 0.3)), t=t)
        pb = back_out(prog(t, 0.3, 0.3))
        if pb > 0:
            pop_in(c, 780, 1250, pb); barbell(c, 0, 0, 0.7, 2); c.restore()
            x_mark(c, 780, 1250, 1.8, prog(t, 0.5, 0.3))
        pq = back_out(prog(t, d * 0.45, 0.3))
        if pq > 0:
            pop_in(c, 780, 980, pq); label(c, "DÁ?", 0, 0, YEL, 150); c.restore()
            ring(c, 780, 940, 180, t, YEL)

def yes(c, t, d, b):
    with Cam(c, t, punch=0.06):
        p1 = back_out(prog(t, 0.1, 0.3)); p2 = back_out(prog(t, 0.5, 0.3)); p3 = back_out(prog(t, d * 0.45, 0.35))
        if p1 > 0: pop_in(c, 270, 1050, p1); barbell(c, 0, 0, 0.5, 2); label(c, "BARRA", 0, 150, WHITE, 52); c.restore()
        if p2 > 0:
            pop_in(c, 810, 1050, p2); chunky(c, 0, 120, 0.3, "push", t=t); label(c, "SEU CORPO", 0, 190, WHITE, 52); c.restore()
        if p3 > 0:
            pop_in(c, 540, 1180, p3); label(c, "=", 0, 30, YEL, 120); c.restore()
            pop_in(c, 540, 1420, p3)
            disk(c, 0, 0, 150, YEL, 0.9)
            cap_line(c, -70, 40, -20, -50, WHITE, 40); cap_line(c, -20, -50, 50, -30, WHITE, 40); cap_line(c, 50, -30, 70, 30, WHITE, 40)
            c.restore()
            ring(c, 540, 1420, 200, t, YEL)
        chip(c, "O MÚSCULO NÃO SABE", 540, 1760, YEL, INK, 58, t=t, start=d * 0.6)

def rule(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # medidor de esforço
        cx, cy, r = 540, 1350, 330
        c.new_path(); c.arc(cx, cy, r, math.pi, 2 * math.pi); rgb(c, CARD); c.set_line_width(60); c.set_line_cap(1); c.stroke()
        for i, col in enumerate((GRN, YEL, RED)):
            c.new_path(); c.arc(cx, cy, r, math.pi + i * math.pi / 3 + 0.03, math.pi + (i + 1) * math.pi / 3 - 0.03)
            rgb(c, col); c.set_line_width(60); c.stroke()
        ang = math.pi + math.pi * (0.1 + 0.8 * ease(prog(t, 0.2, 1.4))) + (0.02 * math.sin(t * 12) if t > 1.6 else 0)
        cap_line(c, cx, cy, cx + (r - 40) * math.cos(ang), cy + (r - 40) * math.sin(ang), WHITE, 16); disk(c, cx, cy, 30, WHITE)
        draw_text(c, "LIMITE", cx + 300, cy + 70, 40, RED, "Anton", align="center")
        draw_text(c, "FÁCIL", cx - 300, cy + 70, 40, GRN, "Anton", align="center")
        pt = back_out(prog(t, d * 0.5, 0.3))
        tag(c, 540, 1620, "PERTO DO LIMITE", YEL, INK, 64, pt)
        chip(c, "SEM SOBRAR REPETIÇÃO", 540, 1770, CARD, WHITE, 46, t=t, start=d * 0.65)

def problem(c, t, d, b):
    with Cam(c, t, punch=0.06):
        n = int(20 * ease(prog(t, 0.1, 1.5)))
        pop_in(c, 540, 1050, back_out(prog(t, 0.05, 0.3)))
        rrect(c, -300, -150, 600, 300, 36, DARK); draw_text(c, "FLEXÕES", 0, -85, 30, GREY, "Space Mono", align="center", spacing=6)
        label(c, str(n), 0, 90, WHITE if n < 20 else GRN, 190); c.restore()
        pf = back_out(prog(t, d * 0.5, 0.3))
        if pf > 0:
            pop_in(c, 540, 1420, pf); rrect(c, -260, -90, 520, 180, 34, GRN); label(c, "FÁCIL", 0, 40, INK, 120); c.restore()
            ring(c, 540, 1420, 300, t, GRN)
        chunky(c, 920, FLOOR_Y + 120, 0.4, pose_mix("idle", "laugh", prog(t, d * 0.5, 0.3)), t=t)

def harder(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # flexão com pé no alto
        draw_text(c, "PÉ NO ALTO", 540, 900, 52, YEL, "Anton", prog(t, 0.1, 0.3), align="center")
        u = 0.5 + 0.5 * math.sin(t * 2.4)
        pushup(c, 280, 1130, 0.85, u, feet_up=90 * prog(t, 0.1, 0.4))
        # agachamento 1 perna
        draw_text(c, "UMA PERNA SÓ", 540, 1290, 52, YEL, "Anton", prog(t, d * 0.45, 0.3), align="center")
        if t > d * 0.45:
            pose = pose_mix("idle", "squat_deep", 0.5 + 0.5 * math.sin((t - d * 0.45) * 2.4))
            chunky(c, 540, 1800, 0.6, pose, t=t)
            tag(c, 840, 1500, "1 PERNA", CARD, WHITE, 44, back_out(prog(t, d * 0.55, 0.3)))

def slow(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cx, cy = 540, 1150
        per = 4.0; u = (t % per) / per
        disk(c, cx, cy, 250, DARK)
        c.new_path(); c.arc(cx, cy, 250, -math.pi / 2, -math.pi / 2 + 2 * math.pi * u); rgb(c, YEL); c.set_line_width(26); c.set_line_cap(1); c.stroke()
        label(c, f"{int(u * 4) + 1}s" if u < 1 else "4s", cx, cy + 50, WHITE, 150)
        pa = prog(t, 0.2, 0.5)
        arrow(c, 180, 950, 180, 1450, YEL, 18, p=pa)
        draw_text(c, "DESCE", 180, 1520, 44, YEL, "Anton", pa, align="center")
        if t > d * 0.5:
            ph = back_out(prog(t, d * 0.5, 0.3))
            pop_in(c, 560, 1660, ph); rrect(c, -330, -80, 660, 160, 30, YEL); label(c, "SEGURA EMBAIXO", 0, 28, INK, 66); c.restore()
            ring(c, 560, 1660, 200, t, YEL)
        chip(c, "DEVAGAR", 540, 1780, CARD, WHITE, 54, t=t, start=0.3) if t < d * 0.5 else None

def limit(c, t, d, b):
    with Cam(c, t, punch=0.06):
        draw_text(c, "PERNA", 300, 900, 56, RED, "Anton", prog(t, 0.1, 0.3), align="center")
        draw_text(c, "COSTAS", 780, 900, 56, RED, "Anton", prog(t, 0.1, 0.3), align="center")
        # mochila nas costas (perna)
        pm = back_out(prog(t, d * 0.35, 0.35))
        sq = 0.5 + 0.5 * math.sin(t * 2.4)
        chunky(c, 300, FLOOR_Y, 0.75, pose_mix("idle", "squat_half", sq), face=-1, t=t)
        if pm > 0:
            pop_in(c, 395, 1230 + 60 * sq, pm); rrect(c, -50, -80, 100, 150, 30, GRN); rrect(c, -30, -20, 60, 40, 10, INK, 0.5); c.restore()
        # barra fixa
        pb = back_out(prog(t, d * 0.5, 0.35))
        if pb > 0:
            cap_line(c, 600, 1000, 960, 1000, (0.75, 0.76, 0.8), 18)
            cap_line(c, 600, 1000, 600, 1100, GREY, 12); cap_line(c, 960, 1000, 960, 1100, GREY, 12)
            ph = 0.5 + 0.5 * math.sin(t * 2.4)
            by = 1330 - 200 * ph
            cap_line(c, 700, 1000, 740, by - 40, L_FRONT, 36); cap_line(c, 860, 1000, 820, by - 40, L_FRONT, 36)
            rrect(c, 690, by - 70, 180, 260, 70, L_BODY); disk(c, 780, by - 100, 58, L_BODY)
        chip(c, "MOCHILA CHEIA", 300, 1780, GRN, INK, 46, t=t, start=d * 0.35)
        chip(c, "BARRA FIXA", 780, 1780, YEL, INK, 46, t=t, start=d * 0.5)

def gym(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pl = int(clamp((t - 0.2) / 0.3, 0, 4))
        barbell(c, 540, 1250, 0.95, pl)
        draw_text(c, "É SÓ COLOCAR PESO", 540, 1000, 60, WHITE, "Anton", prog(t, 0.1, 0.3), align="center")
        for k in range(pl):
            pass
        arrow(c, 540, 1520, 540, 1420, YEL, 14, p=prog(t, 0.2, 0.3))
        pn = back_out(prog(t, d * 0.5, 0.3))
        if pn > 0:
            pop_in(c, 540, 1630, pn); rrect(c, -370, -80, 740, 160, 30, CARD); label(c, "NÃO É OBRIGATÓRIA", 0, 28, WHITE, 64); c.restore()
            check_mark(c, 900, 1470, 0.9, prog(t, d * 0.55, 0.3))
        chip(c, "MAIS FÁCIL", 540, 1790, YEL, INK, 52, t=t, start=0.5)

def count(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i in range(4):
            h = 170 + i * 80; x = 120 + i * 220
            p = back_out(prog(t, 0.2 + i * 0.35, 0.3))
            if p <= 0: continue
            c.save(); c.translate(x, 1560); c.scale(1, max(p, .001))
            rrect(c, 0, -h, 190, h, 20, YEL if i == 3 else CARD); c.restore()
            draw_text(c, f"SEM {i + 1}", x + 95, 1620, 34, GREY, "Space Mono", p, align="center")
            draw_text(c, str(10 + i), x + 95, 1560 - h + 80, 80, INK if i == 3 else WHITE, "Anton", p, align="center")
        arrow(c, 150, 1300, 900, 1000, YEL, 14, p=prog(t, 0.6, 1.0))
        pt = back_out(prog(t, d * 0.5, 0.3))
        tag(c, 540, 900, "CASA = ACADEMIA", YEL, INK, 62, pt) if False else None
        pu = back_out(prog(t, d * 0.45, 0.3))
        if pu > 0:
            pop_in(c, 330, 940, pu); label(c, "CASA", 0, 0, WHITE, 90); c.restore()
            pop_in(c, 540, 940, pu); label(c, "=", 0, 0, YEL, 90); c.restore()
            pop_in(c, 760, 940, pu); label(c, "ACADEMIA", 0, 0, WHITE, 90); c.restore()
        chip(c, "UM POUCO A CADA SEMANA", 540, 1790, YEL, INK, 50, t=t, start=d * 0.6)

def start(c, t, d, b):
    with Cam(c, t, punch=0.06):
        items = [("FLEXÃO", 0.1), ("AGACHAMENTO", d * 0.28), ("REMADA COM MOCHILA", d * 0.5)]
        for i, (nm, st) in enumerate(items):
            p = back_out(prog(t, st, 0.3))
            if p <= 0: continue
            y = 1000 + i * 210
            pop_in(c, 540, y, p); rrect(c, -440, -85, 880, 170, 30, DARK)
            disk(c, -360, 0, 44, YEL); label(c, str(i + 1), -360, 20, INK, 56)
            draw_text(c, nm, -290, 18, 52 if i < 2 else 44, WHITE, "Anton")
            for k in range(3):
                dp = prog(t, st + 0.3 + k * 0.15, 0.2)
                disk(c, 270 + k * 52, 0, 18, YEL if dp > 0.5 else CARD)
            c.restore()
        chip(c, "3 SÉRIES · PERTO DO LIMITE", 540, 1700, YEL, INK, 52, t=t, start=d * 0.7)

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="poll", text=("ACADEMIA", "EM CASA"), app_title="REGISTRO DE SÉRIES",
             app_lines=[("FLEXÃO  3 × 15", None), ("AGACHAM.  3 × 12", None), ("REMADA  3 × 10", None)], chart=False,
             app_big="15 REPS", app_big_label="ÚLTIMA SÉRIE")

VIS = {k: globals()[k] for k in "hook yes rule problem harder slow limit gym count start cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.3, "pop"), (0.5, "buzz"), ("0.45d", "pop")],
    "yes": [(0.0, "whoosh"), (0.1, "pop"), (0.5, "pop"), ("0.45d", "ding"), ("0.6d", "pop")],
    "rule": [(0.0, "whoosh"), (0.2, "swish"), ("0.5d", "pop"), ("0.65d", "pop")],
    "problem": [(0.0, "whoosh"), (0.1, "tick"), (0.5, "tick"), (0.9, "tick"), ("0.5d", "ding")],
    "harder": [(0.0, "whoosh"), (0.1, "pop"), ("0.45d", "pop"), ("0.55d", "pop")],
    "slow": [(0.0, "whoosh"), (0.2, "swish"), (1.0, "tick"), (2.0, "tick"), ("0.5d", "pop")],
    "limit": [(0.0, "whoosh"), (0.1, "pop"), ("0.35d", "pop"), ("0.5d", "pop")],
    "gym": [(0.0, "whoosh"), (0.2, "clack"), (0.5, "clack"), (0.8, "clack"), ("0.5d", "pop"), ("0.55d", "ding")],
    "count": [(0.0, "whoosh"), (0.2, "pop"), (0.55, "pop"), (0.9, "pop"), (1.25, "pop"), ("0.45d", "pop")],
    "start": [(0.0, "whoosh"), (0.1, "pop"), ("0.28d", "pop"), ("0.5d", "pop"), ("0.7d", "pop")],
    "cta": cta_sfx(R.BEATS[-1], "poll"),
}
