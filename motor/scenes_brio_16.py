"""BRIO 16 — abdominal todo dia não tira barriga."""
import math
from engine2 import *
from lote_h import *
from scenes_brio_05 import counter
import roteiro_brio_16 as R
from cta_brio import cta_brio, cta_sfx
BEAT_CTA = R.BEATS[-1]
SKIN = (0.93, 0.78, 0.55)

def abs_grid(c, x, y, w, h, col=None, a=1.0):
    col = col or L_FRONT
    for r_ in range(3):
        for q in range(2):
            rrect(c, x - w / 2 + q * (w / 2) + 6, y - h / 2 + r_ * (h / 3) + 6, w / 2 - 12, h / 3 - 12, 18, col, a)

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        chunky(c, 330, FLOOR_Y, 0.85, pose_mix("idle", "reach_low", 0.5 + 0.5 * math.sin(t * 3)), face=1)
        ring(c, 330, FLOOR_Y - 330 * 0.85, 120, t, YEL)
        for i in range(7):
            pp = back_out(prog(t, 0.2 + i * 0.22, 0.3))
            if pp <= 0: continue
            pop_in(c, 660 + (i % 4) * 110, 1000 + (i // 4) * 110, pp); disk(c, 0, 0, 42, GRN); check_mark(c, 0, 2, 0.35, 1.0, INK); c.restore()
        draw_text(c, "TODO DIA", 800, 920, 40, WHITE, "Anton", align="center")
        rrect(c, 620, 1400, 360, 40, 20, (0.2, 0.22, 0.27)); rrect(c, 620, 1400, 350, 40, 20, YEL)
        draw_text(c, "GORDURA DA BARRIGA", 800, 1380, 26, GREY, "Space Mono", align="center", spacing=2)
        draw_text(c, "QUASE IGUAL", 800, 1500, 44, RED, "Anton", prog(t, d * 0.5, 0.3), align="center")

def spot(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 540, FLOOR_Y, 0.9, "idle", face=1, dark=False)
        by = FLOOR_Y - 400 * 0.9
        flame(c, 540, by, 0.7 + 0.04 * math.sin(t * 8), YEL, t)
        ring(c, 540, by, 150, t, YEL)
        pp = prog(t, d * 0.4, 0.35)
        if pp > 0: x_mark(c, 540, by, 1.9, pp)
        tg(c, 540, 930, "QUEIMAR NO LUGAR", YEL, INK, 56, back_out(prog(t, 0.2, 0.3)))
        tg(c, 860, 1700, "MITO", RED, WHITE, 70, back_out(prog(t, d * 0.55, 0.3)))

def body(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 540, FLOOR_Y, 0.9, pose_mix("idle", "flex", 0.4 + 0.4 * math.sin(t * 2)), face=1)
        spots = [(300, 1290, "2"), (780, 1130, "1"), (540, 1250, "4"), (780, 1450, "3")]
        spots = [(380, 1290, "2", 0.3), (700, 1110, "1", 0.0), (540, 1230, "4", 0.9), (700, 1460, "3", 0.6)]
        for x, y, n, dl in spots:
            pp = back_out(prog(t, 0.3 + dl, 0.3))
            if pp <= 0: continue
            pop_in(c, x, y, pp); flame(c, 0, 0, 0.45, YEL, t + dl); disk(c, 0, 70, 28, INK); label(c, n, 0, 90, WHITE, 40); c.restore()
        tg(c, 540, 900, "ORDEM DELE", YEL, INK, 60, back_out(prog(t, 0.1, 0.3)))
        draw_text(c, "VOCÊ NÃO ESCOLHE", 540, 1760, 48, WHITE, "Anton", prog(t, d * 0.55, 0.3), align="center")

def abs_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cx, cy = 540, 1250
        rrect(c, cx - 230, cy - 270, 460, 540, 90, (0.2, 0.22, 0.27))
        abs_grid(c, cx, cy, 380, 480, L_FRONT)
        fat = 0.92 - 0.0 * t
        pul = 1 + 0.015 * math.sin(t * 4)
        c.save(); c.translate(cx, cy); c.scale(pul, pul)
        rrect(c, -245, -290, 490, 580, 110, SKIN, fat * (0.6 + 0.3 * math.sin(t * 2) ** 2) if t < d * 0.5 else 0.8)
        c.restore()
        draw_text(c, "GORDURA", cx, cy + 10, 80, WHITE, "Anton", 0.9, align="center")
        tg(c, 300, 900, "JÁ EXISTE", GRN, INK, 54, back_out(prog(t, 0.2, 0.3)))
        tg(c, 780, 1660, "ESCONDIDO", YEL, INK, 54, back_out(prog(t, d * 0.5, 0.3)))
        arrow(c, 780, 1580, 650, 1390, YEL, 12, p=prog(t, d * 0.55, 0.3))

def what(c, t, d, b):
    with Cam(c, t, punch=0.06):
        draw_text(c, "GASTA", 80, 1000, 50, YEL, "Anton"); draw_text(c, "COME", 80, 1220, 50, WHITE, "Anton")
        g1 = ease_out(prog(t, 0.2, 0.6)); g2 = ease_out(prog(t, 0.5, 0.6))
        rrect(c, 80, 1030, 880 * g1, 70, 35, YEL); rrect(c, 80, 1250, 780 * g2, 70, 35, WHITE)
        pd = back_out(prog(t, d * 0.4, 0.3))
        if pd > 0:
            rrect(c, 860, 1150, 100, 150, 20, RED, 0.35 * pd)
            tg(c, 700, 1390, "UM POUCO MENOS", RED, WHITE, 50, pd)
        for i in range(7):
            pp = back_out(prog(t, d * 0.5 + i * 0.18, 0.25))
            if pp > 0:
                pop_in(c, 130 + i * 140, 1620, pp); disk(c, 0, 0, 44, GRN); check_mark(c, 0, 2, 0.35, 1.0, INK); c.restore()
            else: disk(c, 130 + i * 140, 1620, 44, (0.28, 0.3, 0.35))
        draw_text(c, "COM CONSTÂNCIA", 540, 1740, 40, WHITE, "Anton", prog(t, d * 0.6, 0.3), align="center")

def lift(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 + 0.5 * math.sin(t * 3.2)
        h = chunky(c, 330, FLOOR_Y, 0.85, pose_mix("curl_down", "curl_up", u), face=1)
        dumbbell_h(c, h[0], h[1], 0.8)
        items = [("GASTA ENERGIA", 1000, 0.3, flame), ("MANTÉM MÚSCULO", 1190, 0.7, None)]
        for lab, y, st, fn in items:
            pp = back_out(prog(t, st, 0.35))
            if pp <= 0: continue
            pop_in(c, 760, y, pp); rrect(c, -230, -80, 460, 160, 26, (0.2, 0.22, 0.27))
            if fn: flame(c, -160, 10, 0.5, YEL, t)
            else: rrect(c, -190, -20, 60, 60, 20, L_FRONT); disk(c, -160, 10, 30, L_FRONT)
            draw_text(c, lab, -100, 18, 40, WHITE, "Anton"); c.restore()
        g = ease(prog(t, d * 0.4, d * 0.5))
        rrect(c, 540, 1420, 420, 44, 22, (0.2, 0.22, 0.27)); rrect(c, 540, 1420, 420 * (1 - 0.6 * g), 44, 22, YEL)
        draw_text(c, "GORDURA", 750, 1400, 28, GREY, "Space Mono", align="center", spacing=4)
        tg(c, 760, 1560, "MUSCULAÇÃO", YEL, INK, 60, back_out(prog(t, d * 0.55, 0.3)))

def walk(c, t, d, b):
    with Cam(c, t, punch=0.06):
        ph = (t * 2.2) % 2
        pose = "walk1" if ph < 1 else "walk2"
        x = 240 + 600 * ((t / d) % 1.0) * 0 + 70 * math.sin(t * 1.5)
        # chão em movimento
        for i in range(8):
            xx = (i * 190 - t * 260) % 1520 - 220
            cap_line(c, xx, FLOOR_Y + 24, xx + 90, FLOOR_Y + 24, (0.3, 0.32, 0.38), 8)
        chunky(c, 360, FLOOR_Y, 0.85, pose, face=1, bob=-8 * abs(math.sin(t * 6.9)))
        km = 5.0 * ease(prog(t, 0.2, d * 0.7))
        counter(c, 790, 1130, int(km), 1.0, YEL, title="KM")
        tg(c, 790, 1380, "SOMAR PASSOS", GRN, INK, 54, back_out(prog(t, 0.4, 0.3)))
        pf = prog(t, d * 0.55, 0.3)
        if pf > 0:
            draw_text(c, "SIMPLES", 790, 1500, 44, WHITE, "Anton", pf, align="center")
            draw_text(c, "CONTA NA SEMANA", 790, 1560, 40, GREY, "Anton", pf, align="center")

def core(c, t, d, b):
    with Cam(c, t, punch=0.06):
        days = "SEG TER QUA QUI SEX SAB DOM".split()
        on = {0: 0.2, 2: 0.55, 4: 0.9}
        for i, dn in enumerate(days):
            x = 70 + i * 135
            rrect(c, x, 960, 125, 170, 18, (0.2, 0.22, 0.27))
            draw_text(c, dn, x + 62, 1000, 30, GREY, "Space Mono", align="center")
            if i in on:
                pp = back_out(prog(t, on[i], 0.3))
                if pp > 0:
                    pop_in(c, x + 62, 1070, pp); abs_grid(c, 0, 0, 60, 70, YEL); c.restore()
        tg(c, 540, 880, "3X NA SEMANA", YEL, INK, 50, back_out(prog(t, 0.1, 0.3)))
        pc = back_out(prog(t, d * 0.4, 0.35))
        pop_in(c, 540, 1480, pc * (1 + 0.03 * math.sin(t * 5)))
        rrect(c, -90, -180, 180, 360, 70, (0.2, 0.22, 0.27)); abs_grid(c, 0, 0, 140, 300, L_FRONT)
        c.restore()
        ring(c, 540, 1480, 230, t, GRN)
        tg(c, 540, 1760, "FORTALECE O TRONCO", GRN, INK, 52, back_out(prog(t, d * 0.55, 0.3)))

def time_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        rows = [("BRAÇOS", 1.0, 0.2), ("PERNAS", 0.9, 0.2), ("BARRIGA", 0.5, 0.2)]
        for i, (lab, full, st) in enumerate(rows):
            y = 1010 + i * 190
            draw_text(c, lab, 70, y - 20, 40, WHITE, "Anton")
            rrect(c, 70, y, 940, 60, 30, (0.2, 0.22, 0.27))
            sp = 1.0 - 0.45 * i
            f = full * ease_out(prog(t, st, 1.2 / sp + i * 0.4 - 0.3 * 0)) if i < 2 else 0.0
            if i == 2:
                grow = prog(t, 0.4, d * 0.5)
                back = prog(t, d * 0.72, 0.5)
                f = 0.85 * ease(grow) * (1 - 0.8 * ease(back))
            rrect(c, 70, y, 940 * f + 1, 60, 30, GRN if i < 2 else YEL)
        tg(c, 300, 1650, "ÚLTIMA A SAIR", YEL, INK, 46, back_out(prog(t, d * 0.35, 0.3)))
        tg(c, 780, 1740, "PRIMEIRA A VOLTAR", RED, WHITE, 46, back_out(prog(t, d * 0.72, 0.3)))
        clock(c, 900, 900, 55, t * 2, hour=3)

def proof(c, t, d, b):
    with Cam(c, t, punch=0.06):
        s = 0.9
        chunky(c, 360, FLOOR_Y, s, "idle", face=1)
        wy = FLOOR_Y - 405 * s
        pp = ease_out(prog(t, 0.2, 0.5))
        c.save(); c.translate(360, wy)
        rrect(c, -96 * pp, -14, 192 * pp, 28, 6, YEL)
        for k in range(-4, 5):
            cap_line(c, k * 20 * pp, -14, k * 20 * pp, -2 + (4 if k % 2 == 0 else 0), INK, 3)
        c.restore()
        ring(c, 360, wy, 130, t, YEL)
        tg(c, 800, 960, "FITA NA CINTURA", YEL, INK, 50, back_out(prog(t, 0.3, 0.3)))
        v = 92 - 2 * ease(prog(t, d * 0.45, 0.8))
        pq = back_out(prog(t, d * 0.4, 0.3))
        if pq > 0:
            pop_in(c, 790, 1180, pq); rrect(c, -170, -110, 340, 220, 30, (0.08, 0.09, 0.11))
            label(c, f"{v:.0f} CM", 0, 40, WHITE, 100); c.restore()
        calendar(c, 640, 1380, 4, 1, 85, 85, {0: back_out(prog(t, d * 0.6, 0.3)), 1: back_out(prog(t, d * 0.7, 0.3))}, GRN)
        draw_text(c, "1X POR SEMANA", 790, 1520, 36, WHITE, "Anton", prog(t, d * 0.6, 0.3), align="center")
        clock(c, 700, 1650, 48, t * 2, hour=7)
        draw_text(c, "MESMO HORÁRIO", 880, 1665, 34, GREY, "Anton", prog(t, d * 0.8, 0.3), align="center")

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="poll", text=("ABDOMINAL", "TREINO COMPLETO"), app_title="TREINO DE 30 MIN",
             app_lines=[("PEITO 3X10", None), ("COSTAS 3X10", None), ("PERNAS 3X10", None)], app_big="30 MIN", app_big_label="TEMPO LIVRE")

VIS = {"hook": hook, "spot": spot, "body": body, "abs": abs_, "what": what, "lift": lift, "walk": walk, "core": core, "time": time_, "proof": proof, "cta": cta}
SFX = {k: [(0.0, "whoosh"), (0.25, "pop"), ("0.5d", "pop")] for k in VIS}
SFX["hook"] = [(0.0, "boom"), (0.2, "pop"), ("0.5d", "buzz")]
SFX["spot"] += [("0.4d", "buzz")]
SFX["body"] += [(0.6, "pop"), (0.9, "pop"), (1.2, "pop")]
SFX["time"] += [("0.72d", "buzz")]
SFX["proof"] += [("0.6d", "ding")]
SFX["cta"] = cta_sfx(BEAT_CTA, "poll")
