"""DIA UM — piloto 1: vergonha de ir pra academia."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, disk, rrect, draw_text, Cam, pose_mix
from tema_diaum import *

FLOOR = 1430


def chip(c, s, x, y, size=56, p=1.0, col=LIME, t=0.0, seed=0):
    if p <= 0:
        return
    font(c, TITLE, size); w = c.text_extents(s).x_advance + 50; h = size * 1.4
    c.save(); c.translate(x, y); k = max(back_out(p), 0.001); c.scale(k, k)
    highlight(c, -w / 2, -h / 2, w, h, 1.0, col)
    hline(c, [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2), (-w / 2, -h / 2)], INK, 5, t, seed, 2)
    draw_text(c, s, -w / 2 + 25, size * 0.36, size, INK, TITLE)
    c.restore()


def bubble(c, s, x, y, w, p=1.0, t=0.0, seed=0, size=54):
    if p <= 0:
        return
    h = 120
    c.save(); c.translate(x, y); k = max(back_out(p), 0.001); c.scale(k, k)
    pts = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2 + 120, h / 2), (-w / 2 + 70, h / 2 + 50), (-w / 2 + 80, h / 2),
           (-w / 2, h / 2), (-w / 2, -h / 2)]
    c.move_to(*pts[0])
    for q in pts[1:]:
        c.line_to(*q)
    rgb(c, PAPER); c.fill()
    hline(c, pts, INK, 6, t, seed, 2)
    hand(c, s, 0, 18, size, INK, align="center")
    c.restore()


def hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=1100):
        # porta da academia
        hline(c, [(560, FLOOR), (560, 760), (900, 760), (900, FLOOR)], INK, 8, t, 1)
        marker(c, "ACADEMIA", 600, 830, 54, INK, ease_out(prog(t, 0, 0.3)))
        peek = ease_out(prog(t, 0.1, 0.5))
        stick(c, lerp(380, 470, peek), FLOOR, 1.0, "guard", t, 10, face=1, blush=True, mood="sad")
        bubble(c, "e se rirem de mim?", 330, 680, 470, ease_out(prog(t, 0.45 * d, 0.4)), t, 30, 50)


def ninguem(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        stick(c, 540, FLOOR, 0.9, "idle", t, 10, mood="neutral")
        # outros, cada um na sua
        stick(c, 230, FLOOR, 0.72, "phone_up", t, 20, face=-1)
        stick(c, 860, FLOOR, 0.72, "curl_up" if int(t * 2) % 2 else "curl_down", t, 30, face=1)
        dumbbell(c, 905, FLOOR - 420 if int(t * 2) % 2 else FLOOR - 250, 0.35, t, 40)
        p = ease_out(prog(t, 0.35 * d, 0.4))
        if p > 0:
            hand(c, "no celular", 140, 760, 50, MUTED, p)
            hand(c, "na série", 820, 760, 50, MUTED, p)
            harrow(c, 230, 780, 230, 850, p, t, 50, MUTED, 5)
            harrow(c, 880, 780, 880, 850, p, t, 51, MUTED, 5)


def pequeno(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        dias = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
        treino = {0, 2, 4}
        for i, dd in enumerate(dias):
            x = LEFT + 30 + i * 118; y = 800
            a = ease_out(prog(t, 0.05 * i, 0.25))
            hand(c, dd, x + 10, y, 42, INK, a)
            checkbox(c, x + 14, y + 30, 70, ease(prog(t, 0.35 * d + (i // 2) * 0.25, 0.3)) if i in treino else 0.0, t, 100 + i)
        clock(c, 330, 1210, 150, 0.66 * ease(prog(t, 0.3 * d, 0.6 * d)), t, 200)
        marker(c, "40 MIN", 560, 1240, 96, INK, ease_out(prog(t, 0.5 * d, 0.3)))


def quatro(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        itens = ["agachamento", "supino", "remada", "prancha"]
        for i, it in enumerate(itens):
            y = 780 + i * 140
            a = ease_out(prog(t, 0.1 + i * 0.18, 0.3))
            checkbox(c, LEFT + 20, y - 46, 60, ease(prog(t, 0.6 * d + i * 0.1, 0.25)), t, 300 + i)
            hand(c, f"{i + 1}. {it}", LEFT + 110, y, 66, INK, a)
        p = ease_out(prog(t, 0.45 * d, 0.3))
        if p > 0:
            hcircle(c, 820, 900, 110, MARGIN, 6, t, 400, p)
            marker(c, "x4", 770, 930, 80, MARGIN, p)
            hand(c, "semanas", 745, 1050, 48, MARGIN, p)


def horario(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        clock(c, 260, 980, 150, 0.27, t, 500)
        hand(c, "ex: 14h ou 21h", 140, 1210, 48, MUTED, ease_out(prog(t, 0.2, 0.3)))
        # academia vazia: só 1 boneco tranquilo
        hline(c, [(470, FLOOR), (470, 780), (980, 780), (980, FLOOR)], INK, 7, t, 510)
        stick(c, 720, FLOOR, 0.62, "curl_up" if int(t * 2) % 2 else "curl_down", t, 520, mood="happy")
        chip(c, "VAZIO = TRANQUILO", 720, 700, 40, ease_out(prog(t, 0.5 * d, 0.3)), t=t, seed=530)


def anota(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        linhas = [("supino", "30 kg × 8"), ("agachamento", "20 kg × 10"), ("como foi:", "cansei, mas fui!")]
        for i, (a_, b_) in enumerate(linhas):
            y = 830 + i * 150
            p = ease_out(prog(t, 0.1 + i * 0.25 * d / 1.5, 0.35))
            hand(c, a_, LEFT + 20, y, 70, INK, p)
            hand(c, b_, LEFT + 420, y, 70, BLUEPEN, ease_out(prog(t, 0.2 + i * 0.25 * d / 1.5, 0.35)))
        # lápis
        px = LEFT + 420 + 300 * ((t * 0.8) % 1); py = 830 + 150 * min(2, int(t / max(d, 0.1) * 3)) - 20
        hline(c, [(px, py), (px + 90, py - 90)], (0.85, 0.65, 0.2), 18, t, 600, 0.5)
        hline(c, [(px, py), (px + 14, py - 14)], INK, 8, t, 601, 0.3)


def dia30(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=1100):
        stick(c, 270, FLOOR, 0.85, "tired", t, 700, mood="sad")
        hand(c, "dia 1", 210, 790, 64, INK, ease_out(prog(t, 0, 0.3)))
        p = ease_out(prog(t, 0.3 * d, 0.4))
        harrow(c, 420, 1150, 600, 1150, p, t, 710, MARGIN, 8)
        if p > 0.5:
            stick(c, 800, FLOOR, 0.92, "flex", t, 720, mood="happy")
            highlight(c, 715, 745, 220, 60, prog(t, 0.45 * d, 0.3))
            hand(c, "dia 30", 730, 790, 64, INK, p)
        tally(c, LEFT + 20, 620, 30, t, 730, prog(t, 0.2, d * 0.7), 60)


def cta(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        p = ease_out(prog(t, 0, 0.35))
        hcircle(c, W / 2, 840, 130, INK, 9, t, 800, p, fill=LIME if p >= 1 else None)
        if p > 0.6:
            marker(c, "1", W / 2 - 34, 905, 180, INK)
        chip(c, "COMENTA DIA UM", W / 2, 1060, 62, ease_out(prog(t, 0.15, 0.35)), t=t, seed=810)
        q = ease_out(prog(t, 0.35 * d, 0.4))
        hand(c, "registre e acompanhe seus", W / 2, 1180, 52, INK, q, align="center")
        hand(c, "treinos gratuitamente", W / 2, 1236, 52, INK, q, align="center")
        chip(c, "LINK NA BIO", W / 2, 1360, 56, ease_out(prog(t, 0.55 * d, 0.35)), col=(1, 1, 1), t=t, seed=820)


VIS = dict(hook=hook, ninguem=ninguem, pequeno=pequeno, quatro=quatro, horario=horario, anota=anota, dia30=dia30, cta=cta)
SFX = {
    "hook": [(0.0, "boom"), ("0.45d", "pop")],
    "ninguem": [(0.0, "swish"), ("0.6d", "pop")],
    "pequeno": [(0.0, "swish"), ("0.35d", "tick"), ("0.35d+0.25", "tick"), ("0.35d+0.5", "tick")],
    "quatro": [(0.0, "swish"), ("0.6d", "tick"), ("0.6d+0.1", "tick"), ("0.6d+0.2", "tick"), ("0.6d+0.3", "tick")],
    "horario": [(0.0, "swish"), ("0.5d", "pop")],
    "anota": [(0.0, "swish"), ("0.1", "zip")],
    "dia30": [(0.0, "swish"), ("0.3d", "whoosh"), ("0.55d", "ding")],
    "cta": [(0.0, "swish"), ("0.15", "pop"), ("0.55d", "ding")],
}
