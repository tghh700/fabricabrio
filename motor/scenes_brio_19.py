"""Cenas do BRIO 19 — travou no supino: 3 saídas."""
import math
from engine2 import *
from scenes_short02 import chip
from scenes_brio_18 import pop_in, tag, card, bench_lifter, calendar, INK, CARD, DARK
import roteiro_brio_19 as R
from cta_brio import cta_brio, cta_sfx

def flat_chart(c, x, y, w, t, st, col=None, jump=None, wk=6):
    """gráfico de carga por semana. jump = índice da semana em que sobe"""
    col = col or YEL
    cap_line(c, x, y, x + w, y, WHITE, 4, 0.25)
    n = int(clamp((t - st) / 0.25)) if False else None
    pts = []
    for k in range(wk):
        h = 0 if jump is None or k < jump else 90 * (k - jump + 1)
        pts.append((x + k * w / (wk - 1), y - 120 - h))
    p = ease_out(prog(t, st, 1.3)) * (wk - 1)
    out = [pts[0]]
    for k in range(1, wk):
        if p >= k: out.append(pts[k])
        elif p > k - 1:
            f = p - (k - 1); out.append((lerp(pts[k - 1][0], pts[k][0], f), lerp(pts[k - 1][1], pts[k][1], f)))
    if len(out) > 1: poly(c, out, col, 12)
    for q in out: disk(c, q[0], q[1], 15, col)
    return out[-1]

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        sh = 4 * math.sin(t * 35) * (0.5 + 0.5 * math.sin(t * 3))
        bench_lifter(c, 120, 1640, 1.1, 0.1, plate=1.25, col=RED, shake=sh)
        # semanas paradas no mesmo peso
        for i in range(4):
            p = back_out(prog(t, 0.2 + i * 0.25, 0.3))
            if p > 0:
                pop_in(c, 190 + i * 235, 960, p); rrect(c, -100, -80, 200, 160, 22, DARK)
                draw_text(c, f"SEM {i + 1}", 0, -35, 24, GREY, "Space Mono", align="center")
                label(c, "60", 0, 55, WHITE, 70); c.restore()
        pt = back_out(prog(t, d * 0.55, 0.3))
        if pt > 0:
            pop_in(c, 760, 1220, pt); label(c, "3 SAÍDAS", 0, 0, YEL, 100); c.restore()
            ring(c, 760, 1200, 190, t, YEL)

def plateau(c, t, d, b):
    with Cam(c, t, punch=0.06):
        end = flat_chart(c, 120, 1450, 840, t, 0.1, RED)
        draw_text(c, "MESMO TREINO", 540, 1000, 70, WHITE, "Anton", prog(t, 0.2, 0.3), align="center")
        draw_text(c, "MESMO RESULTADO", 540, 1100, 70, RED, "Anton", prog(t, 1.0, 0.3), align="center")
        chunky(c, 880, FLOOR_Y + 120, 0.45, pose_mix("idle", "shrug", prog(t, d * 0.5, 0.3)), t=t)
        tag(c, 300, 1640, "COM TODO MUNDO", CARD, WHITE, 52, back_out(prog(t, d * 0.4, 0.3)))

def one(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # reps sobem até a meta, depois o peso
        goal = 12
        for i in range(5):
            h = 130 + i * 70; x = 130 + i * 190
            p = back_out(prog(t, 0.2 + i * 0.3, 0.3))
            if p > 0:
                c.save(); c.translate(x, 1600); c.scale(1, max(p, .001))
                rrect(c, 0, -h * 1.5, 160, h * 1.5, 18, YEL if i == 4 else CARD); c.restore()
                draw_text(c, str(8 + i), x + 80, 1670, 46, WHITE, "Anton", p, align="center")
        c.set_dash([20, 14]); cap_line(c, 90, 1180, 990, 1180, GRN, 6, prog(t, 0.3, 0.3)); c.set_dash([])
        draw_text(c, "META", 970, 1150, 36, GRN, "Anton", prog(t, 0.3, 0.3), align="right")
        pk = back_out(prog(t, d * 0.55, 0.3))
        if pk > 0:
            pop_in(c, 540, 960, pk); rrect(c, -250, -80, 500, 150, 28, YEL); label(c, "AGORA SOBE O PESO", 0, 30, INK, 52); c.restore()
        chip(c, "MESMO PESO", 540, 830, CARD, WHITE, 50, t=t, start=0.2) if t < d * 0.5 else None

def two(c, t, d, b):
    with Cam(c, t, punch=0.06):
        n = 3 + (1 if t > d * 0.4 else 0) + (1 if t > d * 0.55 else 0)
        for i in range(5):
            p = back_out(prog(t, 0.1 + i * 0.12, 0.3)) if i < 3 else back_out(prog(t, d * 0.4 + (i - 3) * (d * 0.15), 0.3))
            if p <= 0: continue
            y = 1000 + i * 135
            pop_in(c, 540, y, p)
            new = i >= 3
            rrect(c, -380, -52, 760, 104, 24, YEL if new else CARD)
            draw_text(c, f"SÉRIE {i + 1}", -340, 18, 48, INK if new else WHITE, "Anton")
            for k in range(5): disk(c, 90 + k * 52, 0, 16, INK if new else GREY)
            c.restore()
        if t > d * 0.4:
            draw_text(c, "+1 OU 2", 900, 930, 50, YEL, "Anton", prog(t, d * 0.4, 0.3), align="center")
        chip(c, "FALTA VOLUME", 540, 1790, YEL, INK, 56, t=t, start=d * 0.65)

def battery(c, x, y, lvl, col, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -170, -80, 340, 160, 28, WHITE, 0.9); rrect(c, 170, -30, 28, 60, 8, WHITE, 0.9)
    rrect(c, -150, -60, 300, 120, 16, DARK)
    rrect(c, -150, -60, max(300 * lvl, 1), 120, 16, col)
    c.restore()

def three(c, t, d, b):
    with Cam(c, t, punch=0.06):
        lvl = 0.9 - 0.8 * ease(prog(t, 0.1, 1.2)) + 0.85 * ease(prog(t, d * 0.55, 1.2))
        col = RED if lvl < 0.3 else (GRN if lvl > 0.6 else YEL)
        battery(c, 540, 1150, lvl, col, 1.8)
        draw_text(c, "CANSAÇO", 540, 940, 56, RED, "Anton", prog(t, 0.2, 0.3) * (1 if t < d * 0.55 else 0.3), align="center")
        if t > d * 0.5:
            pa = prog(t, d * 0.5, 0.4)
            snowflake(c, 250, 1500, 70 + 8 * math.sin(t * 4), pa); snowflake(c, 830, 1500, 70 + 8 * math.sin(t * 4 + 2), pa)
            tag(c, 540, 1520, "SEMANA LEVE", YEL, INK, 70, back_out(pa))
        chip(c, "TRAVA A CARGA", 540, 1770, CARD, WHITE, 52, t=t, start=0.5) if t < d * 0.5 else None

def tech(c, t, d, b):
    with Cam(c, t, punch=0.06):
        up = 0.5 + 0.5 * math.sin(t * 2.2)
        bench_lifter(c, 60, 1250, 0.85, up, plate=0.9)
        items = [("PÉS FIRMES", 0.3), ("ESCÁPULAS JUNTAS", d * 0.33), ("BARRA NO PEITO", d * 0.62)]
        for i, (s_, st) in enumerate(items):
            p = back_out(prog(t, st, 0.3))
            if p <= 0: continue
            y = 1420 + i * 120
            pop_in(c, 540, y, p); rrect(c, -400, -48, 800, 96, 24, DARK)
            draw_text(c, s_, -330, 20, 54, WHITE, "Anton"); c.restore()
            check_mark(c, 880, y, 0.8, prog(t, st + 0.2, 0.25))
        draw_text(c, "TÉCNICA", 540, 900, 90, YEL, "Anton", prog(t, 0.0, 0.3), align="center")

def sleep(c, t, d, b):
    with Cam(c, t, punch=0.06):
        bed(c, 340, 1250, 0.62, t)
        draw_text(c, "SONO", 340, 1000, 60, WHITE, "Anton", prog(t, 0.1, 0.3), align="center")
        # prato quase vazio
        pp = back_out(prog(t, d * 0.35, 0.35))
        if pp > 0:
            pop_in(c, 800, 1260, pp)
            disk(c, 0, 0, 190, WHITE); disk(c, 0, 0, 140, (0.85, 0.85, 0.83)); disk(c, 20, 10, 36, YEL)
            c.restore()
            draw_text(c, "COMIDA", 800, 1000, 60, WHITE, "Anton", pp, align="center")
        # barras de nível baixo
        for x, st in ((340, 0.5), (800, d * 0.4 + 0.2)):
            rrect(c, x - 150, 1560, 300, 40, 20, DARK)
            rrect(c, x - 150, 1560, 300 * 0.25 * ease(prog(t, st, 0.5)) + 1, 40, 20, RED)
        x_mark(c, 900, 1700, 0.6, prog(t, d * 0.6, 0.3))
        chip(c, "SEGURAM O SUPINO", 540, 1800, RED, WHITE, 50, t=t, start=d * 0.65)

def change(c, t, d, b):
    with Cam(c, t, punch=0.06):
        names = ["SÉRIES", "CARGA", "EXERCÍCIOS", "DIETA", "HORÁRIO"]
        for i, nm in enumerate(names):
            p = back_out(prog(t, 0.1 + i * 0.2, 0.3))
            if p <= 0: continue
            x = 300 if i % 2 == 0 else 780; y = 930 + (i // 2) * 190
            if i == 4: x = 540
            ang = math.sin(t * 6 + i) * 0.05
            pop_in(c, x, y, p); c.rotate(ang)
            rrect(c, -210, -65, 420, 130, 26, CARD); draw_text(c, nm, 0, 20, 52, WHITE, "Anton", align="center")
            c.restore()
        pq = back_out(prog(t, d * 0.45, 0.3))
        if pq > 0:
            pop_in(c, 540, 1540, pq); label(c, "O QUE FUNCIONOU?", 0, 0, YEL, 80); c.restore()
            for k, xx in enumerate((150, 930)):
                pop_in(c, xx, 1380 + 20 * math.sin(t * 5 + k), pq); label(c, "?", 0, 40, RED, 140); c.restore()
        x_mark(c, 540, 1720, 0.9, prog(t, d * 0.65, 0.3))

def one_thing(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i in range(4):
            on = i == 0
            x = 300 if i % 2 == 0 else 780; y = 930 + (i // 2) * 150
            p = back_out(prog(t, 0.1 + i * 0.1, 0.3))
            pop_in(c, x, y, p); rrect(c, -210, -55, 420, 110, 24, YEL if on else CARD)
            draw_text(c, ["SÉRIES", "CARGA", "DIETA", "SONO"][i], 0, 18, 48, INK if on else GREY, "Anton", align="center"); c.restore()
        calendar(c, 270, 1280, 3, 1, 180, t, 0.6, mark=lambda n: True, gap=30)
        for i in range(3):
            draw_text(c, f"S{i + 1}", 360 + i * 210, 1395, 56, INK, "Anton", prog(t, 0.7 + i * 0.12, 0.2), align="center")
        pa = prog(t, d * 0.6, 0.4)
        chart_up(c, 300, 1500, 480, 200, ease(pa), YEL)
        chip(c, "COMPARA OS NÚMEROS", 540, 1790, YEL, INK, 54, t=t, start=d * 0.65)

def patience(c, t, d, b):
    with Cam(c, t, punch=0.06):
        flat_chart(c, 120, 1500, 840, t, 0.1, YEL, jump=3, wk=6)
        for k in range(6):
            draw_text(c, f"S{k + 1}", 120 + k * 168, 1570, 34, GREY, "Space Mono", align="center")
        draw_text(c, "PARADO", 330, 1090, 60, GREY, "Anton", prog(t, 0.8, 0.3), align="center")
        pu = back_out(prog(t, d * 0.55, 0.3))
        if pu > 0:
            pop_in(c, 760, 1000, pu); label(c, "VOLTA A SUBIR", 0, 0, YEL, 66); c.restore()
            arrow(c, 760, 1060, 800, 1260, YEL, 14, p=prog(t, d * 0.6, 0.4))
        chunky(c, 160, FLOOR_Y + 120, 0.4, "idle", t=t)

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="__ SEMANAS", app_title="SUPINO",
             app_lines=[("SEM 1  60 KG", None), ("SEM 2  60 KG", None), ("SEM 3  62,5 KG", GRN)], chart=True)

VIS = {k: globals()[k] for k in "hook plateau one two three tech sleep change one_thing patience cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.2, "pop"), (0.45, "pop"), (0.7, "pop"), ("0.55d", "pop")],
    "plateau": [(0.0, "whoosh"), (0.2, "pop"), (1.0, "buzz"), ("0.4d", "pop")],
    "one": [(0.0, "whoosh"), (0.2, "tick"), (0.5, "tick"), (0.8, "tick"), (1.1, "tick"), (1.4, "tick"), ("0.55d", "ding")],
    "two": [(0.0, "whoosh"), (0.1, "pop"), (0.22, "pop"), (0.34, "pop"), ("0.4d", "ding"), ("0.55d", "ding")],
    "three": [(0.0, "whoosh"), (0.2, "buzz"), ("0.5d", "swish"), ("0.5d+0.1", "pop")],
    "tech": [(0.0, "whoosh"), (0.3, "pop"), ("0.33d", "pop"), ("0.62d", "pop"), ("0.33d+0.2", "ding")],
    "sleep": [(0.0, "whoosh"), (0.1, "pop"), ("0.35d", "pop"), ("0.6d", "buzz")],
    "change": [(0.0, "whoosh"), (0.1, "pop"), (0.3, "pop"), (0.5, "pop"), (0.7, "pop"), ("0.45d", "pop"), ("0.65d", "buzz")],
    "one_thing": [(0.0, "whoosh"), (0.1, "pop"), (0.6, "click"), (0.9, "click"), ("0.6d", "swish"), ("0.65d", "pop")],
    "patience": [(0.0, "whoosh"), (0.8, "pop"), ("0.55d", "pop"), ("0.55d+0.1", "ding")],
    "cta": cta_sfx(R.BEATS[-1], "bubble"),
}
