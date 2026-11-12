"""BRIO 25 — como saber se está evoluindo (5 sinais)."""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_25 as R
BEAT_CTA = R.BEATS[-1]

def mirror(c, x, y, w, h, p=1.0):
    if p <= 0: return
    pop(c, x, y, p)
    rrect(c, -w / 2 - 14, -h / 2 - 14, w + 28, h + 28, 34, (0.12, 0.14, 0.18)); rrect(c, -w / 2, -h / 2, w, h, 24, (0.30, 0.42, 0.52))
    cap_line(c, -w / 2 + 30, -h / 2 + 50, -w / 2 + 110, -h / 2 + 20, WHITE, 8, 0.4)
    c.restore()

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        chunky(c, 290, FLOOR_Y, 0.9, pose_mix("idle", "shrug", prog(t, 0.4, 0.3)), face=1)
        pop(c, 290, 1000, back_out(prog(t, 0.5, 0.3))); label(c, "?", 0, 60, YEL, 190); c.restore()
        pc = back_out(prog(t, 0.2, 0.35))
        card(c, 780, 1220, 360, 400, CARD, pc)
        chart_up(c, 640, 1100, 280, 220, ease_out(prog(t, 0.5, 1.0)), YEL)
        pq = back_out(prog(t, 1.2, 0.3)); pop(c, 880, 1060, pq); label(c, "?", 0, 40, WHITE, 110); c.restore()
        tag(c, 540, 1745, "SEM ESPELHO, SEM BALANÇA", YEL, INK, 52, back_out(prog(t, d * 0.55, 0.3)))

def mirror_s(c, t, d, b):
    with Cam(c, t, punch=0.06):
        mirror(c, 770, 1250, 330, 640, back_out(prog(t, 0.1, 0.3)))
        chunky(c, 270, FLOOR_Y, 0.85, "idle", face=1)
        chunky(c, 770, 1560, 0.5, "idle", face=-1, bob=0)
        for i in range(3):
            p = ease_out(prog(t, 0.6 + i * 0.5, 0.3))
            if p > 0: ring(c, 270, 1250 + i * 80, 40, t + i * 0.3, WHITE)
        mono(c, "TODO DIA", 270, 900, 30, GREY, prog(t, 0.3, 0.3))
        x_mark(c, 770, 960, 0.8, prog(t, d * 0.5, 0.3))
        tag(c, 540, 1745, "NÃO VÊ A MUDANÇA", RED, WHITE, 56, back_out(prog(t, d * 0.4, 0.3)))

def scale_s(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # balança
        rrect(c, 290, 1500, 500, 90, 30, (0.85, 0.84, 0.8)); rrect(c, 440, 1510, 200, 50, 14, (0.08, 0.09, 0.11))
        label(c, "??,? KG", 540, 1550, YEL, 40)
        items = [("ÁGUA", BLU, 340), ("COMIDA", RED, 480), ("MÚSCULO", GRN, 620), ("GORDURA", YEL, 760)]
        for i, (n, col, x) in enumerate(items):
            t0 = 0.3 + i * 0.5
            f = ease(prog(t, t0, 0.5))
            if f <= 0: continue
            sx = lerp(100 + i * 260, 540, f); sy = lerp(1000, 1430, f) - math.sin(f * math.pi) * 120
            pop(c, sx, sy, 1)
            rrect(c, -90, -36, 180, 72, 22, col); label(c, n, 0, 16, INK if col in (YEL, GRN) else WHITE, 34); c.restore()
        tag(c, 540, 1000, "TUDO NO MESMO NÚMERO", WHITE, INK, 52, back_out(prog(t, d * 0.55, 0.3)))
        ring(c, 540, 1550, 140, t, YEL) if t > d * 0.55 else None

def counter_card(c, x, y, lab, big, sub, p, col=WHITE):
    card(c, x, y, 420, 330, (0.08, 0.09, 0.11), p)
    if p > 0:
        mono(c, lab, x, y - 110, 26, GREY, p); txt(c, big, x, y + 20, 100, col, p); txt(c, sub, x, y + 110, 44, GREY, p)

def sign1(c, t, d, b):
    with Cam(c, t, punch=0.06):
        counter_card(c, 300, 1100, "MÊS PASSADO", "40 KG", "10 REPS", back_out(prog(t, 0.1, 0.3)))
        pk = back_out(prog(t, 0.7, 0.3))
        counter_card(c, 780, 1100, "ESTE MÊS", "45 KG", "10 REPS", pk, YEL)
        arrow(c, 480, 1100, 580, 1100, YEL, 14, p=prog(t, 0.6, 0.3))
        barbell(c, 300, 1540, 0.45, 1); barbell(c, 780, 1540, 0.45, 3 if t > 1.0 else 2)
        arrow(c, 780, 1420, 780, 1330, GRN, 12, p=prog(t, 1.2, 0.3))
        tag(c, 540, 1745, "A CARGA SOBE", YEL, INK, 64, back_out(prog(t, d * 0.45, 0.3)))

def sign2(c, t, d, b):
    with Cam(c, t, punch=0.06):
        counter_card(c, 300, 1100, "MÊS PASSADO", "40 KG", "10 REPS", back_out(prog(t, 0.1, 0.3)))
        counter_card(c, 780, 1100, "ESTE MÊS", "40 KG", "12 REPS", back_out(prog(t, 0.7, 0.3)), YEL)
        arrow(c, 480, 1100, 580, 1100, YEL, 14, p=prog(t, 0.6, 0.3))
        # bolinhas de repetição
        for i in range(12):
            on = i < 10 or t > 1.4 + (i - 10) * 0.3
            p = back_out(prog(t, 0.9 + i * 0.07, 0.2)) if i < 10 else back_out(prog(t, 1.4 + (i - 10) * 0.3, 0.2))
            if p > 0:
                pop(c, 170 + i * 67, 1500, p); disk(c, 0, 0, 24, YEL if i >= 10 else WHITE); c.restore()
        txt(c, "+2", 780, 1630, 90, GRN, prog(t, 1.5, 0.3))
        tag(c, 300, 1745, "MAIS REPETIÇÕES", YEL, INK, 56, back_out(prog(t, d * 0.45, 0.3)))

def sign3(c, t, d, b):
    with Cam(c, t, punch=0.06):
        rows = [("BRAÇO", "36 CM"), ("COXA", "56 CM"), ("CINTURA", "82 CM")]
        for i, (n, v) in enumerate(rows):
            p = back_out(prog(t, 0.15 + i * 0.5, 0.3))
            y = 970 + i * 190
            card(c, 540, y, 860, 150, CARD, p)
            if p > 0:
                txt(c, n, 270, y + 18, 56, WHITE, p)
                tape(c, 700, y + 5, 330, t) if False else None
                rrect(c, 560, y - 30, 290, 60, 8, YEL, p)
                for k in range(10):
                    xx = 575 + k * 28; cap_line(c, xx, y - 30, xx, y - (8 if k % 5 else -6), INK, 3, p)
                txt(c, v, 860 - 0, y + 70, 0, WHITE, 0)
        for i, (n, v) in enumerate(rows):
            txt(c, v, 960 - 60 - 40, 970 + i * 190 - 50, 36, YEL, prog(t, 0.6 + i * 0.5, 0.3)) if False else None
            mono(c, v, 705, 970 + i * 190 + 55, 26, WHITE, prog(t, 0.6 + i * 0.5, 0.3))
        pc = back_out(prog(t, d * 0.45, 0.3))
        card(c, 540, 1600, 360, 150, (0.93, 0.92, 0.89), pc)
        if pc > 0: txt(c, "1 VEZ POR MÊS", 540, 1612, 44, INK, pc)
        tag(c, 540, 1770, "A FITA MÉTRICA", YEL, INK, 56, back_out(prog(t, 0.1, 0.3)))

def sign4(c, t, d, b):
    with Cam(c, t, punch=0.06):
        for i, (lab, flex) in enumerate((("MÊS 1", 0.0), ("MÊS 2", 1.0))):
            x = 290 + i * 500
            p = back_out(prog(t, 0.15 + i * 0.5, 0.3))
            card(c, x, 1250, 440, 700, (0.16, 0.18, 0.22), p)
            if p > 0:
                sun = 1 if True else 0
                disk(c, x + 150, 1000, 30, YEL, p)
                chunky(c, x, 1560, 0.6, pose_mix("idle", "flex", flex * ease(prog(t, 0.8, 0.4))), face=1)
                mono(c, lab, x, 940, 28, WHITE, p)
        # linhas de alinhamento
        for yy in (1010, 1560):
            c.set_dash([14, 12]); cap_line(c, 80, yy, 1000, yy, YEL, 3, 0.5 * prog(t, 0.9, 0.3)); c.set_dash([])
        pc = back_out(prog(t, d * 0.5, 0.3))
        tag(c, 540, 1745, "MESMA LUZ, MESMA POSIÇÃO", YEL, INK, 48, pc)
        arrow(c, 500, 1250, 580, 1250, WHITE, 10, p=prog(t, 1.0, 0.3))

def secret(c, t, d, b):
    with Cam(c, t, punch=0.06):
        notebook(c, 300, 1230, 420, 520, back_out(prog(t, 0.1, 0.3)))
        mono(c, "ANTES", 330, 1050, 28, INK, prog(t, 0.3, 0.3))
        for i in range(3):
            cap_line(c, 280, 1130 + i * 90, 340 + 40 * (i % 2), 1130 + i * 90, (0.3, 0.3, 0.35), 8, prog(t, 0.5 + i * 0.3, 0.3))
        card(c, 780, 1230, 420, 520, CARD, back_out(prog(t, 0.5, 0.3)))
        mono(c, "AGORA", 780, 1050, 28, WHITE, prog(t, 0.6, 0.3))
        for i in range(3):
            cap_line(c, 640, 1130 + i * 90, 760 + 40 * (i % 2), 1130 + i * 90, YEL, 8, prog(t, 0.8 + i * 0.3, 0.3))
        # setas de comparação
        for i in range(3):
            arrow(c, 510, 1130 + i * 90, 600, 1130 + i * 90, GRN, 8, p=prog(t, 1.2 + i * 0.2, 0.3))
        tag(c, 540, 1600, "COMPARAR", YEL, INK, 78, back_out(prog(t, d * 0.4, 0.3)))
        txt(c, "TEM QUE TER ANOTADO ANTES", 540, 1720, 38, WHITE, prog(t, d * 0.65, 0.3))

def stuck(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 250, FLOOR_Y, 0.8, pose_mix("tired", "thumb", prog(t, d * 0.55, 0.3)), face=1)
        # regulador (1 ajuste)
        card(c, 740, 1100, 520, 220, CARD, back_out(prog(t, 0.1, 0.3)))
        cap_line(c, 540, 1100, 940, 1100, GREY, 12)
        k = 540 + 400 * (0.3 + 0.35 * ease(prog(t, 0.6, 0.7)))
        disk(c, k, 1100, 34, YEL)
        mono(c, "UM AJUSTE", 740, 1040, 28, WHITE)
        # fita de novo
        p = back_out(prog(t, d * 0.45, 0.3))
        card(c, 740, 1380, 520, 160, DARK, p)
        if p > 0: rrect(c, 520, 1355, 440, 52, 8, YEL, p); [cap_line(c, 540 + k2 * 40, 1355, 540 + k2 * 40, 1375 if k2 % 5 else 1390, INK, 3) for k2 in range(11)]
        tag(c, 740, 1560, "MEDE DE NOVO", YEL, INK, 52, back_out(prog(t, d * 0.5, 0.3)))
        tag(c, 540, 1745, "NÃO DESISTE", GRN, INK, 66, back_out(prog(t, 0.2, 0.3)))

def sign5(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # camiseta apertando no braço
        pul = 0.06 * math.sin(t * 6)
        arm_view(c, 280, 900, 0.85, bi=YEL, bend=1.1, pulse=pul)
        c.save(); c.translate(280, 900 + 150 * 0.85); c.scale(1, 0.32)
        c.new_path(); c.arc(0, 0, 100 * (1 + pul), 0, 6.2832); rgb(c, CORAL if 'CORAL' in globals() else RED, 0.9); c.set_line_width(46); c.stroke(); c.restore()
        txt(c, "CAMISETA APERTA", 280, 1380, 38, WHITE, prog(t, 0.4, 0.3))
        # calça folgando
        cx = 780
        pw = back_out(prog(t, 0.2, 0.3))
        pop(c, cx, 1120, pw)
        rrect(c, -110, -90, 220, 60, 12, GREY)
        poly(c, [(-110, -45), (-120, 260), (-20, 260), (0, 20), (20, 260), (120, 260), (110, -45)], (0.3, 0.4, 0.65), 36)
        c.restore()
        gap = 40 * ease(prog(t, 0.8, 0.6))
        for sd in (-1, 1):
            arrow(c, cx + sd * 150, 1130, cx + sd * (150 - gap), 1130, GRN, 10, p=prog(t, 0.8, 0.5))
        txt(c, "CALÇA FOLGADA", cx, 1480, 38, WHITE, prog(t, 0.7, 0.3))
        tag(c, 540, 1700, "A ROUPA MUDA", YEL, INK, 66, back_out(prog(t, d * 0.5, 0.3)))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="bubble", text="SUBIU", app_title="CARGA · SUPINO", app_lines=[], app_big="CARGA", chart=True)

VIS = {"hook": hook, "mirror": mirror_s, "scale": scale_s, "sign1": sign1, "sign2": sign2, "sign3": sign3, "sign4": sign4,
       "secret": secret, "stuck": stuck, "sign5": sign5, "cta": cta}
SFX = {
    "hook": [(0.0, "boom"), (0.3, "pop"), (0.5, "pop"), (1.2, "pop")],
    "mirror": [(0.0, "whoosh"), (0.1, "pop"), (0.6, "pop"), ("0.5d", "buzz")],
    "scale": [(0.0, "whoosh"), (0.3, "swish"), (0.8, "swish"), (1.3, "swish"), (1.8, "swish"), ("0.55d", "pop")],
    "sign1": [(0.0, "whoosh"), (0.1, "pop"), (0.7, "pop"), (1.2, "ding"), ("0.45d", "pop")],
    "sign2": [(0.0, "whoosh"), (0.1, "pop"), (0.7, "pop"), (1.4, "tick"), (1.7, "tick"), ("0.45d", "pop")],
    "sign3": [(0.0, "whoosh"), (0.15, "pop"), (0.65, "pop"), (1.15, "pop"), ("0.45d", "pop")],
    "sign4": [(0.0, "whoosh"), (0.15, "pop"), (0.65, "pop"), (0.8, "shutter"), ("0.5d", "pop")],
    "secret": [(0.0, "whoosh"), (0.1, "pop"), (0.5, "pop"), (1.2, "tick"), (1.4, "tick"), (1.6, "tick"), ("0.4d", "pop")],
    "stuck": [(0.0, "whoosh"), (0.2, "pop"), (0.7, "swish"), ("0.45d", "pop"), ("0.5d", "click")],
    "sign5": [(0.0, "whoosh"), (0.2, "pop"), (0.4, "pop"), (0.8, "swish"), ("0.5d", "pop")],
    "cta": cta_sfx(BEAT_CTA, "bubble"),
}
