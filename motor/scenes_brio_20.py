"""Cenas do BRIO 20 — semana leve (deload)."""
import math
from engine2 import *
from scenes_short02 import chip
from scenes_brio_18 import pop_in, tag, card, calendar, INK, CARD, DARK
from scenes_brio_19 import battery
import roteiro_brio_20 as R
from cta_brio import cta_brio, cta_sfx

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        barbell(c, 540, 1330, 0.9, 1)
        # peso leve: halter pequeno sendo levantado devagar
        up = 0.5 + 0.5 * math.sin(t * 2)
        chunky(c, 240, FLOOR_Y, 0.8, pose_mix("idle", "curl_up", up), t=t)
        tag(c, 760, 960, "PEGAR LEVE", CARD, WHITE, 64, back_out(prog(t, 0.2, 0.3)))
        pq = back_out(prog(t, 0.5, 0.3))
        if pq > 0:
            pop_in(c, 800, 1130, pq); label(c, "FRAQUEZA?", 0, 0, RED, 90); c.restore()
        if t > d * 0.5:
            p = prog(t, d * 0.5, 0.5)
            chart_up(c, 520, 1450, 460, 200, ease(p), YEL)
            chip(c, "CARGA VOLTA A SUBIR", 540, 1790, YEL, INK, 52, t=t, start=d * 0.5)

def tired(c, t, d, b):
    with Cam(c, t, punch=0.06):
        n = int(clamp((t - 0.2) / 0.28, 0, 8))
        for k in range(8):
            if k >= n: continue
            p = back_out(prog(t, 0.2 + k * 0.28, 0.25))
            pop_in(c, 540, 1650 - k * 95 - 40, p)
            rrect(c, -230, -40, 460, 80, 18, mix(CARD, RED, k / 9))
            draw_text(c, f"SEMANA {k + 1}", 0, 16, 36, WHITE, "Anton", align="center"); c.restore()
        chunky(c, 880, FLOOR_Y + 40, 0.55, pose_mix("idle", "tired", prog(t, d * 0.5, 0.5)), t=t)
        draw_text(c, "CANSAÇO", 300, 900, 70, RED, "Anton", prog(t, d * 0.45, 0.3), align="center")
        arrow(c, 300, 1230, 300, 960, RED, 14, p=prog(t, d * 0.45, 0.5))

def signs(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cells = [("CARGA PARADA", 300, 1010), ("ARTICULAÇÃO", 780, 1010), ("SONO PIOR", 300, 1400), ("SEM VONTADE", 780, 1400)]
        for i, (nm, x, y) in enumerate(cells):
            p = back_out(prog(t, 0.1 + i * (d * 0.2), 0.3))
            if p <= 0: continue
            pop_in(c, x, y, p)
            rrect(c, -220, -170, 440, 340, 30, DARK)
            draw_text(c, nm, 0, 135, 40, YEL, "Anton", align="center")
            if i == 0:
                cap_line(c, -140, -20, 140, -20, WHITE, 10); disk(c, 140, -20, 14, WHITE)
                x_mark(c, 0, -90, 0.5, 1.0)
            elif i == 1:
                cap_line(c, -90, -90, 0, -10, L_FRONT, 40); cap_line(c, 0, -10, 90, -90, L_FRONT, 40)
                ring(c, 0, -10, 70, t, RED)
            elif i == 2:
                for k in range(3):
                    ph = (t * 0.6 + k / 3) % 1; draw_text(c, "Z", -60 + ph * 120, -10 - ph * 90, 50 + ph * 30, WHITE, "Anton", 1 - ph)
                disk(c, 0, -30, 60, (0.8, 0.8, 0.9)); disk(c, 25, -45, 55, DARK)
            else:
                disk(c, 0, -40, 66, L_BODY); cap_line(c, -30, -30, 30, -30, INK, 6); cap_line(c, -30, -55, -10, -48, INK, 6); cap_line(c, 30, -55, 10, -48, INK, 6)
            c.restore()

def what(c, t, d, b):
    with Cam(c, t, punch=0.06):
        base = 1560
        data = [("SÉRIES", 560, 280, 280), ("PESO", 440, 300, 800)]
        for i, (nm, normal, leve, x) in enumerate(data):
            p = ease_out(prog(t, 0.15 + i * 0.1, 0.6))
            rrect(c, x - 110, base - normal * p, 100, normal * p, 16, CARD)
            q = ease_out(prog(t, d * 0.4, 0.6))
            rrect(c, x + 10, base - leve * q, 100, leve * q, 16, YEL)
            draw_text(c, nm, x, base + 62, 50, WHITE, "Anton", align="center")
        draw_text(c, "NORMAL", 170, 880, 40, GREY, "Space Mono", prog(t, 0.3, 0.3), align="center")
        draw_text(c, "LEVE", 400, 880, 40, YEL, "Space Mono", prog(t, d * 0.4, 0.3), align="center")
        tag(c, 540, 1760, "TREINA, MAS MENOS", YEL, INK, 60, back_out(prog(t, d * 0.45, 0.3)))

def how(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # 6 séries -> 3 séries
        for i in range(6):
            x = 130 + i * 155
            cut = i >= 3 and t > d * 0.35 + (i - 3) * 0.15
            p = back_out(prog(t, 0.1 + i * 0.1, 0.25))
            if p <= 0: continue
            pop_in(c, x + 55, 1050, p)
            rrect(c, -55, -110, 110, 220, 20, CARD if cut else YEL, 0.35 if cut else 1)
            if cut: x_mark(c, 0, 0, 0.7, 1.0)
            c.restore()
        draw_text(c, "METADE DAS SÉRIES", 540, 880, 56, WHITE, "Anton", prog(t, 0.2, 0.3), align="center")
        # peso levemente menor
        pw = back_out(prog(t, d * 0.5, 0.3))
        if pw > 0:
            pop_in(c, 540, 1380, pw); rrect(c, -340, -75, 680, 150, 28, DARK)
            label(c, "PESO", -190, 28, GREY, 56); label(c, "−10%", 130, 36, YEL, 100); c.restore()
        pn = back_out(prog(t, d * 0.72, 0.3))
        if pn > 0:
            pop_in(c, 540, 1660, pn); rrect(c, -330, -70, 660, 140, 26, RED); label(c, "NADA DE LIMITE", 0, 25, WHITE, 62); c.restore()

def when(c, t, d, b):
    with Cam(c, t, punch=0.06):
        calendar(c, 110, 940, 4, 2, 190, t, 0.1, mark=lambda n: n in (3, 7), col=YEL, gap=20)
        for i in range(8):
            x = 110 + (i % 4) * 210 + 95; y = 940 + (i // 4) * 210 + 120
            draw_text(c, f"S{i + 1}", x, y - 40, 40, WHITE if i in (3, 7) else GREY, "Anton", prog(t, 0.1 + i * 0.04, 0.2), align="center")
            if i in (3, 7) and t > d * 0.35:
                snowflake(c, x, y + 10, 38 + 4 * math.sin(t * 4 + i), prog(t, d * 0.35 + (i - 3) * 0.12, 0.3))
        chip(c, "A CADA 4 A 8 SEMANAS", 540, 1560, YEL, INK, 56, t=t, start=d * 0.5)
        pw = back_out(prog(t, d * 0.7, 0.3))
        tag(c, 540, 1730, "OU QUANDO OS SINAIS APARECEM", CARD, WHITE, 40, pw)

def after(c, t, d, b):
    with Cam(c, t, punch=0.06):
        battery(c, 540, 1000, 0.3 + 0.7 * ease(prog(t, 0.1, 1.0)), GRN, 1.4)
        chart_up(c, 200, 1250, 680, 360, ease(prog(t, d * 0.35, 1.6)), YEL)
        draw_text(c, "DESCANSADO", 540, 1700, 60, GRN, "Anton", prog(t, 0.8, 0.3), align="center")
        pu = back_out(prog(t, d * 0.6, 0.3))
        if pu > 0:
            pop_in(c, 830, 1330, pu); label(c, "CARGA ↑", 0, 0, YEL, 70); c.restore()

def lose(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 330, FLOOR_Y, 0.85, pose_mix("idle", "flex", prog(t, 0.2, 0.3)), t=t)
        # escudo
        pp = back_out(prog(t, 0.5, 0.35))
        if pp > 0:
            pop_in(c, 790, 1130, pp)
            c.move_to(-160, -190); c.line_to(160, -190); c.line_to(160, 20); c.curve_to(160, 130, 60, 190, 0, 230)
            c.curve_to(-60, 190, -160, 130, -160, 20); c.close_path(); rgb(c, GRN); c.fill()
            label(c, "MÚSCULO", 0, 10, INK, 50); label(c, "OK", 0, 90, INK, 76); c.restore()
            ring(c, 790, 1130, 260, t, GRN)
        tag(c, 540, 1760, "SÓ RECUPERA", YEL, INK, 64, back_out(prog(t, d * 0.5, 0.3)))
        if t > d * 0.3: x_mark(c, 900, 880, 0.6, prog(t, d * 0.3, 0.3))
        draw_text(c, "PERDER", 900, 960, 36, RED, "Anton", prog(t, d * 0.3, 0.3), align="center")

def beginner(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # poucos dias vs meses de treino pesado
        for i, (lab, n, x, col) in enumerate((("POUCO TEMPO", 2, 300, GREY), ("MESES", 8, 780, YEL))):
            p = back_out(prog(t, 0.15 + i * (d * 0.3), 0.3))
            if p <= 0: continue
            draw_text(c, lab, x, 900, 44, col, "Anton", p, align="center")
            for k in range(n):
                pk = back_out(prog(t, 0.3 + i * (d * 0.3) + k * 0.08, 0.25))
                if pk <= 0: continue
                cx = x - 110 + (k % 2) * 220 if n > 2 else x - 110 + k * 220
                cy = 1000 + (k // 2) * 120 if n > 2 else 1030
                pop_in(c, cx if n > 2 else x - 80 + k * 160, cy, pk)
                rrect(c, -50, -45, 100, 90, 14, col); c.restore()
        chunky(c, 270, FLOOR_Y + 100, 0.45, pose_mix("idle", "reach", 0.3), t=t) if False else None
        pt = back_out(prog(t, d * 0.55, 0.3))
        if pt > 0:
            tag(c, 300, 1330, "NEM PRECISA", GRN, INK, 60, pt)
            check_mark(c, 300, 1450, 1.0, prog(t, d * 0.6, 0.3))
        tag(c, 780, 1470, "PRA QUEM TREINA PESADO", CARD, WHITE, 36, back_out(prog(t, d * 0.7, 0.3)))

def feel(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 330, FLOOR_Y, 0.85, pose_mix("idle", "shrug", prog(t, 0.2, 0.3)), t=t)
        pb = back_out(prog(t, 0.4, 0.35))
        if pb > 0:
            pop_in(c, 770, 1000, pb)
            rrect(c, -240, -120, 480, 240, 50, WHITE)
            disk(c, -150, 160, 18, WHITE); disk(c, -200, 210, 10, WHITE)
            label(c, "FIZ", 0, -5, INK, 80); label(c, "POUCO?", 0, 85, INK, 80); c.restore()
        pi = back_out(prog(t, d * 0.5, 0.3))
        if pi > 0:
            pop_in(c, 770, 1400, pi); rrect(c, -300, -90, 600, 180, 34, YEL)
            label(c, "É A IDEIA", 0, 30, INK, 90); c.restore()
            ring(c, 770, 1400, 260, t, YEL)
            check_mark(c, 960, 1260, 0.8, prog(t, d * 0.55, 0.3))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="LEVE", app_title="SUPINO · CARGA",
             app_lines=[("ANTES  60 KG", None), ("DEPOIS  65 KG", GRN)], app_big="+5 KG", app_big_label="ANTES × DEPOIS")

VIS = {k: globals()[k] for k in "hook tired signs what how when after lose beginner feel cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.2, "pop"), (0.5, "pop"), ("0.5d", "ding")],
    "tired": [(0.0, "whoosh")] + [(0.2 + k * 0.28, "tick") for k in range(8)] + [("0.45d", "buzz")],
    "signs": [(0.0, "whoosh"), (0.1, "pop"), ("0.2d+0.1", "pop"), ("0.4d+0.1", "pop"), ("0.6d+0.1", "pop")],
    "what": [(0.0, "whoosh"), (0.15, "swish"), ("0.4d", "swish"), ("0.45d", "pop")],
    "how": [(0.0, "whoosh"), (0.1, "tick"), ("0.35d", "clack"), ("0.35d+0.3", "clack"), ("0.5d", "pop"), ("0.72d", "buzz")],
    "when": [(0.0, "whoosh"), (0.1, "tick"), ("0.35d", "pop"), ("0.5d", "pop"), ("0.7d", "pop")],
    "after": [(0.0, "whoosh"), (0.1, "swish"), ("0.35d", "swish"), ("0.6d", "ding")],
    "lose": [(0.0, "whoosh"), (0.5, "pop"), ("0.3d", "buzz"), ("0.5d", "pop")],
    "beginner": [(0.0, "whoosh"), (0.2, "pop"), ("0.3d", "pop"), ("0.55d", "ding"), ("0.7d", "pop")],
    "feel": [(0.0, "whoosh"), (0.4, "pop"), ("0.5d", "pop"), ("0.55d", "ding")],
    "cta": cta_sfx(R.BEATS[-1], "bubble"),
}
