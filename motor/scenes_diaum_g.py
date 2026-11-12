"""DIA UM — produção 13/11: prancha (pr_), aparelhos (ap_), preguiça (pg_), magro (mg_), semana 2 (s2_)."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, disk, rrect, draw_text, Cam, pose_mix
from tema_diaum import *
from scenes_diaum_p1 import chip, bubble, FLOOR
from scenes_diaum_l1 import pushup
import pauta_1311 as PA

CY = 1100


def floor_line(c, t, seed=1):
    hline(c, seg(LEFT, FLOOR + 6, RIGHT, FLOOR + 6, 10), INK, 6, t, seed)


def xmark(c, x, y, r, p, t=0.0, seed=0):
    if p <= 0:
        return
    hline(c, seg(x - r, y - r, x - r + 2 * r * p, y - r + 2 * r * p, 3), MARGIN, 9, t, seed)
    if p > 0.5:
        q = (p - 0.5) * 2
        hline(c, seg(x + r, y - r, x + r - 2 * r * q, y - r + 2 * r * q, 3), MARGIN, 9, t, seed + 1)


def strike(c, x, y, w, p, t=0.0, seed=0):
    if p > 0:
        hline(c, seg(x - 10, y - 22, x - 10 + (w + 20) * p, y - 26, 6), MARGIN, 8, t, seed)


def rows(c, t, d, items, x=None, y0=820, dy=130, size=64, seed=100, delay=0.12):
    x = LEFT + 20 if x is None else x
    for i, it in enumerate(items):
        txt, col = (it if isinstance(it, tuple) else (it, INK))
        p = ease_out(prog(t, delay + i * 0.22, 0.35))
        hand(c, txt, x, y0 + i * dy, size, col, p)


def plank(c, t, kind, seed, shake=0.0):
    """prancha alta de perfil. kind: joelho | completa | um_pe"""
    wob = shake * 2.5 * math.sin(t * 30)
    if kind == "joelho":
        L, ax = 420, 330
        ang = math.degrees(math.asin(clamp(212 * 0.97 / L))) + wob
        pushup(c, ax, FLOOR, L, ang, (ax + L * math.cos(math.radians(ang)) + 8, FLOOR), t, seed, "happy", knees=True)
        return ax, ang, L
    L, ax = 600, 150
    ang = math.degrees(math.asin(clamp(212 * 0.97 / L))) + wob
    if kind == "um_pe":
        up = 0.5 + 0.5 * math.sin(t * 2.2)
        hline(c, seg(ax + 170, FLOOR - 75, ax - 20, FLOOR - 110 - 110 * up, 3), INK, 9, t, seed + 50)
    pushup(c, ax, FLOOR, L, ang, (ax + L * math.cos(math.radians(ang)) + 8, FLOOR), t, seed, "happy" if not shake else None)
    return ax, ang, L


def cta_flex(word, lines):
    def cta(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=CY):
            p = ease_out(prog(t, 0, 0.35))
            hcircle(c, W / 2, 840, 130, INK, 9, t, 800, p, fill=LIME if p >= 1 else None)
            if p > 0.6:
                marker(c, "1", W / 2 - 34, 905, 180, INK)
            chip(c, "COMENTA " + word, W / 2, 1060, 62, ease_out(prog(t, 0.15, 0.35)), t=t, seed=810)
            q = ease_out(prog(t, 0.35 * d, 0.4))
            for i, ln in enumerate(lines):
                hand(c, ln, W / 2, 1180 + i * 56, 52, INK, q, align="center")
            chip(c, "LINK NA BIO", W / 2, 1360, 56, ease_out(prog(t, 0.55 * d, 0.35)), col=(1, 1, 1), t=t, seed=820)
    return cta


def conc_factory(items):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=CY):
            n = len(items)
            for i, txt in enumerate(items):
                y = 820 + i * 150
                checkbox(c, LEFT + 10, y - 50, 64, ease_out(prog(t, 0.2 + i * (d * 0.55 / n), 0.3)), t, 700 + i)
                hand(c, txt, LEFT + 110, y, 64, INK, ease_out(prog(t, 0.1 + i * (d * 0.55 / n), 0.3)))
    return f


# ================================================================ PRANCHA
def pr_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        plank(c, t, "completa", 2000, shake=1.0)
        floor_line(c, t)
        sec = min(9, int(t * 3))
        clock(c, 780, 860, 90, sec / 60 * 6, t, 2010)
        marker(c, f"{sec} s", 720, 1040, 80, MARGIN, ease_out(prog(t, 0.1, 0.3)))
        bubble(c, "não aguento!", 380, 830, 400, ease_out(prog(t, 0.35 * d, 0.3)), t, 2020, 54)


def pr_niveis(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i in range(3):
            p = ease_out(prog(t, 0.1 + i * 0.25, 0.35))
            x0, y0 = LEFT + 40 + i * 250, FLOOR - (i + 1) * 150
            hline(c, [(x0, FLOOR), (x0, y0), (x0 + 250, y0)], INK, 8, t, 2100 + i, p=p)
            marker(c, str(i + 1), x0 + 100, y0 + 110, 90, MARGIN if i == 2 else INK, p)
        k = clamp(prog(t, 0.3 * d, 0.5 * d))
        step = min(2, int(k * 3))
        stick(c, LEFT + 165 + step * 250, FLOOR - (step + 1) * 150, 0.42, "cheer" if step == 2 else "idle", t, 2110, mood="happy")


def _nivel(kind, label, note):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=CY):
            ax, ang, L = plank(c, t, kind, 2200)
            floor_line(c, t)
            p = ease_out(prog(t, 0.2, 0.35))
            hand(c, label, LEFT + 10, 820, 64, MARGIN, p)
            q = ease_out(prog(t, 0.45 * d, 0.35))
            if q > 0:
                a = math.radians(ang)
                hline(c, seg(ax - 20, FLOOR - 70, ax + (L + 130) * math.cos(a), FLOOR - 70 - (L + 130) * math.sin(a), 6), BLUEPEN, 5, t, 2210, p=q)
                hand(c, note, LEFT + 430, 960, 56, BLUEPEN, q)
    return f


def pr_regra(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i in range(3):
            y = 820 + i * 140
            hand(c, f"série {i + 1}", LEFT + 20, y + 50, 64, INK, ease_out(prog(t, 0.1 + i * 0.2, 0.3)))
            checkbox(c, LEFT + 300, y, 64, ease_out(prog(t, 0.3 + i * 0.35, 0.3)), t, 2300 + i)
            hand(c, "30 s", LEFT + 400, y + 50, 64, BLUEPEN, ease_out(prog(t, 0.3 + i * 0.35, 0.3)))
        p2 = ease_out(prog(t, 0.55 * d, 0.35))
        if p2 > 0.05:
            harrow(c, LEFT + 20, 1330, LEFT + 330, 1330, p2, t, 2350, MARGIN, 8)
        if p2 > 0.6:
            chip(c, "PRÓXIMO NÍVEL", 650, 1330, 50, p2, t=t, seed=2360)


# ================================================================ APARELHOS
def machine(c, x, t, seed, p=1.0, stack_pin=0.0, sticker=False):
    """aparelho de polia rabiscado: torre, pilha de placas, banco"""
    hline(c, [(x, FLOOR), (x, 760), (x + 260, 760), (x + 260, FLOOR)], INK, 8, t, seed, p=p)
    for k in range(8):
        y = 1050 + k * 45
        hline(c, [(x + 40, y), (x + 140, y), (x + 140, y + 36), (x + 40, y + 36), (x + 40, y)], INK, 4, t, seed + 1 + k, 1.5, p=p)
    py = lerp(1050 + 7 * 45, 1050, stack_pin) + 18
    disk(c, x + 160, py, 10, MARGIN, p)
    hline(c, seg(x + 90, 760, x + 90, 1050, 3), MUTED, 4, t, seed + 20, p=p)
    hline(c, [(x + 330, 1260), (x + 520, 1260)], INK, 9, t, seed + 21, p=p)
    hline(c, seg(x + 425, 1260, x + 425, FLOOR, 2), INK, 8, t, seed + 22, p=p)
    if sticker:
        hline(c, [(x + 160, 800), (x + 250, 800), (x + 250, 960), (x + 160, 960), (x + 160, 800)], BLUEPEN, 5, t, seed + 30, p=p)


def ap_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        machine(c, LEFT + 30, t, 3000)
        stick(c, 820, FLOOR, 0.8, "scratch", t, 3050, face=-1, mood="sad", blush=True)
        floor_line(c, t)
        for k in range(3):
            marker(c, "?", 700 + k * 70, 820 - 30 * math.sin(t * 3 + k), 80, MARGIN, ease_out(prog(t, 0.3 + k * 0.15, 0.3)))
        if prog(t, 0.55 * d, 0.2) > 0:
            chip(c, "NORMAL!", W / 2, 1510, 60, ease_out(prog(t, 0.55 * d, 0.3)), t=t, seed=3060)


def ap_desenho(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        machine(c, LEFT + 30, t, 3100, sticker=True)
        floor_line(c, t)
        p = ease_out(prog(t, 0.2, 0.4))
        # adesivo ampliado
        hline(c, [(560, 780), (RIGHT, 780), (RIGHT, 1200), (560, 1200), (560, 780)], BLUEPEN, 6, t, 3110, p=p)
        if p > 0.3:
            up = 0.5 + 0.5 * math.sin(t * 3)
            stick(c, 700, 1150, 0.5, pose_mix("curl_down", "curl_up", up), t, 3120, face=1)
            highlight(c, 760, 900, 120, 40, p, col=MARGIN, a=0.5)
            hand(c, "músculo", 770, 1000, 46, MARGIN, p)
        harrow(c, LEFT + 280, 880, 550, 880, ease_out(prog(t, 0.1, 0.3)), t, 3130, BLUEPEN, 6)


def ap_banco(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        k = ease(prog(t, 0.2, 0.5 * d))
        sy = lerp(1330, 1140, k)
        hline(c, [(LEFT + 60, sy), (LEFT + 360, sy)], INK, 10, t, 3200)
        hline(c, seg(LEFT + 210, sy, LEFT + 210, FLOOR, 3), INK, 8, t, 3201)
        harrow(c, LEFT + 420, 1350, LEFT + 420, 1180, 0.4 + 0.6 * abs(math.sin(t * 2)), t, 3202, BLUEPEN, 6)
        px, py = 690, 1040
        hcircle(c, px, py, 44, INK, 7, t, 3210)
        hand(c, "eixo", px + 70, py + 20, 56, INK)
        jy = lerp(1230, py, k)
        hcircle(c, px, jy, 30, MARGIN, 7, t, 3211)
        hand(c, "joelho", px - 230, jy + 20, 52, MARGIN, ease_out(prog(t, 0.1, 0.3)))
        if k > 0.95:
            chip(c, "NA MESMA LINHA", W / 2, 1420, 50, ease_out(prog(t, 0.65 * d, 0.3)), t=t, seed=3220)


def ap_leve(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        machine(c, LEFT + 30, t, 3300, stack_pin=1.0)
        floor_line(c, t)
        hand(c, "a 1ª placa", LEFT + 310, 1110, 50, MARGIN, ease_out(prog(t, 0.15, 0.3)))
        hand(c, "repetições", 600, 840, 56, INK, ease_out(prog(t, 0.2, 0.3)))
        tally(c, 600, 900, 10, t, 3310, prog(t, 0.3, 0.7 * d), 80)


def ap_professor(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        stick(c, 280, FLOOR, 0.85, "idle", t, 3400, face=1, mood="neutral")
        stick(c, 760, FLOOR, 0.85, "point_up" if int(t * 2) % 2 else "idle", t, 3410, face=-1, mood="happy")
        floor_line(c, t)
        bubble(c, "me ajuda?", 120, 770, 330, ease_out(prog(t, 0.1, 0.35)), t, 3420, 54)
        bubble(c, "claro!", 600, 860, 260, ease_out(prog(t, 0.4 * d, 0.35)), t, 3430, 54)


def ap_tres(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        dias = ["seg", "qua", "sex"]
        for j, s in enumerate(dias):
            hand(c, s, LEFT + 470 + j * 130, 800, 48, MUTED, ease_out(prog(t, 0.05, 0.3)))
        for i, m in enumerate(("leg press", "puxada", "supino máq.")):
            y = 900 + i * 150
            hand(c, m, LEFT + 10, y + 50, 60, INK, ease_out(prog(t, 0.1 + i * 0.15, 0.3)))
            for j in range(3):
                checkbox(c, LEFT + 475 + j * 130, y, 60, ease_out(prog(t, 0.3 * d + (i * 3 + j) * 0.08 * d / 1.0 * 0.6, 0.25)), t, 3500 + i * 3 + j)


# ================================================================ PREGUIÇA
def door(c, x, t, seed, open_=0.0, p=1.0):
    hline(c, [(x, FLOOR), (x, 800), (x + 230, 800), (x + 230, FLOOR)], INK, 8, t, seed, p=p)
    w = 230 * (1 - 0.6 * open_)
    hline(c, [(x, 800), (x + w, 830), (x + w, FLOOR - 10)], INK, 6, t, seed + 1, p=p)
    disk(c, x + w - 30, 1130, 10, INK, p)


def sofa(c, x, t, seed):
    hline(c, [(x, 1300), (x + 380, 1300), (x + 380, FLOOR), (x, FLOOR), (x, 1300)], INK, 8, t, seed)
    hline(c, [(x, 1300), (x, 1150), (x + 380, 1150), (x + 380, 1300)], INK, 8, t, seed + 1)


def pg_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        sofa(c, LEFT, t, 4000)
        stick(c, LEFT + 500, FLOOR, 0.8, "tired", t, 4010, mood="sad", face=-1)
        door(c, RIGHT - 240, t, 4020)
        floor_line(c, t)
        bubble(c, "hoje não...", 330, 820, 380, ease_out(prog(t, 0.25, 0.4)), t, 4030, 56)


def pg_sair(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        door(c, RIGHT - 240, t, 4100, open_=ease(prog(t, 0.5 * d, 0.3)))
        x = lerp(LEFT + 100, RIGHT - 340, ease(prog(t, 0.1, 0.6 * d)))
        stick(c, x, FLOOR, 0.75, "push" if t > 0.2 else "idle", t, 4110, face=1)
        floor_line(c, t)
        hand(c, "a parte difícil", LEFT + 10, 830, 60, MARGIN, ease_out(prog(t, 0.2, 0.3)))
        harrow(c, LEFT + 60, 900, RIGHT - 300, 900, ease_out(prog(t, 0.3, 0.5 * d)), t, 4120, MARGIN, 7)


def backpack(c, x, y, s, t, seed, p=1.0):
    pts = [(x - 90 * s, y), (x - 90 * s, y - 200 * s), (x + 90 * s, y - 200 * s), (x + 90 * s, y), (x - 90 * s, y)]
    hline(c, pts, INK, 8, t, seed, p=p)
    hline(c, [(x - 50 * s, y - 200 * s), (x - 40 * s, y - 250 * s), (x + 40 * s, y - 250 * s), (x + 50 * s, y - 200 * s)], INK, 7, t, seed + 1, p=p)
    hline(c, [(x - 60 * s, y - 90 * s), (x + 60 * s, y - 90 * s)], MARGIN, 6, t, seed + 2, p=p)


def pg_mochila(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        door(c, RIGHT - 240, t, 4200)
        backpack(c, RIGHT - 340, FLOOR, 1.0, t, 4210, ease_out(prog(t, 0.15, 0.4)))
        floor_line(c, t)
        p = ease_out(prog(t, 0.05, 0.3))
        hcircle(c, LEFT + 110, 880, 70, INK, 7, t, 4220, p)
        hcircle(c, LEFT + 140, 860, 60, PAPER, 2, t, 4221, p, fill=PAPER)
        hand(c, "noite anterior", LEFT + 10, 1030, 56, INK, p)
        chip(c, "-1 DECISÃO", 300, 1240, 52, ease_out(prog(t, 0.55 * d, 0.3)), t=t, seed=4230)


def pg_dez(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        clock(c, 300, 1000, 150, (10 / 60) * ease(prog(t, 0.1, 0.6 * d)), t, 4300)
        marker(c, "10 min", 190, 1260, 84, MARGIN, ease_out(prog(t, 0.2, 0.3)))
        up = int(t * 2) % 2
        stick(c, 760, FLOOR, 0.8, "curl_up" if up else "curl_down", t, 4310, face=-1, mood="happy")
        dumbbell(c, 748, FLOOR - 400 if up else FLOOR - 268, 0.34, t, 4320)
        floor_line(c, t)


def pg_ficou(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        m = int(lerp(10, 45, ease(prog(t, 0.1, 0.6 * d))))
        clock(c, 300, 1000, 150, m / 60, t, 4400)
        marker(c, f"{m} min", 170, 1260, 84, INK, 1.0)
        stick(c, 760, FLOOR, 0.8, "cheer" if t > 0.6 * d else "idle", t, 4410, face=-1, mood="happy")
        floor_line(c, t)
        if t > 0.6 * d:
            chip(c, "TERMINOU!", 330, 1390, 56, ease_out(prog(t, 0.6 * d, 0.3)), t=t, seed=4420)


def pg_agenda(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        hline(c, [(LEFT, 780), (RIGHT, 780), (RIGHT, 1480), (LEFT, 1480), (LEFT, 780)], INK, 7, t, 4500, p=p)
        for i, (h_, txt) in enumerate((("07:00", "trabalho"), ("12:00", "almoço"), ("19:00", "TREINO"), ("21:00", "jantar"))):
            y = 900 + i * 150
            q = ease_out(prog(t, 0.1 + i * 0.12, 0.3))
            hand(c, h_, LEFT + 30, y, 56, MUTED, q)
            if txt == "TREINO":
                highlight(c, LEFT + 220, y - 44, 300, 50, prog(t, 0.4 * d, 0.35))
                marker(c, txt, LEFT + 230, y, 62, INK, ease_out(prog(t, 0.35 * d, 0.3)))
            else:
                hand(c, txt, LEFT + 230, y, 56, INK, q)


# ================================================================ MAGRO
def mg_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        stick(c, 300, FLOOR, 0.95, "idle", t, 5000, face=1, mood="neutral", w=6)
        floor_line(c, t)
        bubble(c, "tenho 19...", 560, 780, 380, ease_out(prog(t, 0.2, 0.4)), t, 5010, 56)
        if prog(t, 0.5 * d, 0.2) > 0:
            hand(c, "meta:", 520, 1080, 58, MUTED, ease_out(prog(t, 0.5 * d, 0.3)))
            marker(c, "+ MASSA", 520, 1180, 76, MARGIN, ease_out(prog(t, 0.55 * d, 0.3)))


def mg_muda(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        k = ease(prog(t, 0.2, 0.6 * d))
        stick(c, 250, FLOOR, 0.85, "idle", t, 5100, face=1, mood="neutral", w=6)
        harrow(c, 420, 1150, 600, 1150, ease_out(prog(t, 0.2, 0.4)), t, 5110, MARGIN, 8)
        if k > 0:
            stick(c, 780, FLOOR, 0.85, "flex", t, 5120, face=-1, mood="happy", w=lerp(6, 16, k))
        floor_line(c, t)
        hand(c, "dá pra mudar", LEFT + 10, 830, 64, INK, ease_out(prog(t, 0.1, 0.3)))


def week_boxes(c, t, d, marked, seed, y=820):
    dias = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
    for i, s in enumerate(dias):
        x = LEFT + i * 115
        hand(c, s.lower(), x + 4, y, 44, INK, ease_out(prog(t, 0.05 + i * 0.04, 0.3)))
        v = marked.get(i)
        if v == "x":
            hline(c, [(x + 6, y + 30), (x + 70, y + 30), (x + 70, y + 94), (x + 6, y + 94), (x + 6, y + 30)], INK, 5, t, seed + i, 1.8)
            xmark(c, x + 38, y + 62, 24, ease_out(prog(t, 0.4 * d, 0.3)), t, seed + 20 + i)
        else:
            checkbox(c, x + 6, y + 30, 64, ease_out(prog(t, v * d + 0.2, 0.3)) if v is not None else 0.0, t, seed + i)


def mg_tres(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        week_boxes(c, t, d, {0: 0.15, 2: 0.3, 4: 0.45}, 5200)
        rows(c, t, d, ["agachamento", "supino", "remada"], y0=1110, dy=120, size=62, seed=5210, delay=0.3 * d)


def mg_amais(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, (s, a_, b_) in enumerate((("sem 1", "20 kg", "× 10"), ("sem 2", "22 kg", "× 10"), ("sem 3", "22 kg", "× 11"))):
            y = 860 + i * 150
            p = ease_out(prog(t, 0.1 + i * 0.3, 0.35))
            hand(c, s, LEFT + 10, y, 60, MUTED, p)
            hand(c, a_, LEFT + 230, y, 64, BLUEPEN if i == 1 else INK, p)
            hand(c, b_, LEFT + 470, y, 64, BLUEPEN if i == 2 else INK, p)
        if prog(t, 0.6 * d, 0.2) > 0:
            harrow(c, RIGHT - 60, 1220, RIGHT - 60, 840, ease_out(prog(t, 0.6 * d, 0.4)), t, 5310, MARGIN, 8)
            chip(c, "UM POUCO A MAIS", W / 2, 1420, 52, ease_out(prog(t, 0.65 * d, 0.3)), t=t, seed=5320)


def mg_prato(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        hcircle(c, 330, 1100, 210, INK, 8, t, 5400, p, fill=PAPER)
        hline(c, seg(330, 890, 330, 1310, 3), INK, 5, t, 5401, p=p)
        hline(c, seg(330, 1100, 540, 1100, 3), INK, 5, t, 5402, p=p)
        hand(c, "proteína", 250, 1080, 46, MARGIN, p, align="center")
        hand(c, "arroz", 440, 1060, 44, INK, p, align="center")
        hand(c, "salada", 440, 1190, 44, INK, p, align="center")
        q = ease_out(prog(t, 0.45 * d, 0.35))
        if q > 0:
            hcircle(c, 760, 1000, 90, INK, 6, t, 5410, q, fill=LIME)
            marker(c, "+1", 720, 1030, 70, INK, q)
            hand(c, "lanche", 700, 1160, 56, INK, q)


def scale_draw(c, x, y, t, seed, val, p=1.0):
    hline(c, [(x - 120, y), (x + 120, y), (x + 120, y + 70), (x - 120, y + 70), (x - 120, y)], INK, 8, t, seed, p=p)
    hline(c, [(x - 80, y + 15), (x + 80, y + 15), (x + 80, y + 55), (x - 80, y + 55), (x - 80, y + 15)], INK, 5, t, seed + 1, p=p)
    hand(c, val, x, y + 52, 44, BLUEPEN, p, align="center")


def mg_balanca(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, (s, v) in enumerate((("sem 1", "62,0"), ("sem 2", "62,3"), ("sem 3", "62,7"))):
            p = ease_out(prog(t, 0.1 + i * 0.35, 0.35))
            x = LEFT + 130 + i * 270
            scale_draw(c, x, 1180 - i * 140, t, 5500 + i * 3, v, p)
            hand(c, s, x, 1310 - i * 140, 50, MUTED, p, align="center")
        if prog(t, 0.6 * d, 0.2) > 0:
            hand(c, "parou? come mais um pouco", W / 2 - 20, 1430, 52, MARGIN, ease_out(prog(t, 0.6 * d, 0.3)), align="center")


# ================================================================ SEMANA 2
def curves(c, t, d, p, emp=True, res=True):
    x0, y0, w, h = LEFT + 30, 1420, RIGHT - LEFT - 60, 560
    hline(c, [(x0, y0 - h), (x0, y0), (x0 + w, y0)], INK, 6, t, 6000, p=p)
    for j, s in enumerate(("sem 1", "sem 2", "sem 3")):
        hand(c, s, x0 + 60 + j * 260, y0 + 60, 44, MUTED, p)
    k = ease(prog(t, 0.2, 0.6 * d))
    n = int(40 * k) + 1
    if emp:
        pts = [(x0 + w * i / 40, y0 - h * (0.9 - 0.75 * (i / 40) ** 0.7)) for i in range(n)]
        if len(pts) > 1:
            hline(c, pts, MARGIN, 8, t, 6010)
        hand(c, "empolgação", x0 + 40, y0 - h + 20, 50, MARGIN, p)
    if res:
        pts = [(x0 + w * i / 40, y0 - h * (0.05 + 0.6 * (i / 40) ** 2.2)) for i in range(n)]
        if len(pts) > 1:
            hline(c, pts, BLUEPEN, 8, t, 6020)
        hand(c, "resultado", x0 + w - 230, y0 - h * 0.75, 50, BLUEPEN, p * k)
    return x0, y0, w, h


def s2_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        x0, y0, w, h = curves(c, t, d, ease_out(prog(t, 0, 0.3)), res=False)
        q = ease_out(prog(t, 0.45 * d, 0.3))
        if q > 0:
            hcircle(c, x0 + w * 0.42, y0 - h * 0.35, 90, INK, 6, t, 6030, q)
            stick(c, x0 + w * 0.42, y0 - 20, 0.35, "tired", t, 6040, mood="sad")


def s2_empolga(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        x0, y0, w, h = curves(c, t, d, ease_out(prog(t, 0, 0.3)))
        q = ease_out(prog(t, 0.55 * d, 0.3))
        if q > 0:
            hline(c, seg(x0 + w * 0.42, y0 - h * 0.37, x0 + w * 0.42, y0 - h * 0.12, 4), INK, 5, t, 6050, p=q)
            hand(c, "o buraco", x0 + w * 0.46, y0 - h * 0.2, 52, INK, q)


def s2_grande(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        its = ["5 dias por semana", "1 hora por treino", "dieta perfeita"]
        rows(c, t, d, its, y0=860, dy=150, size=64)
        for i, s in enumerate(its):
            font(c, HAND, 64); w = c.text_extents(s).x_advance
            strike(c, LEFT + 20, 860 + i * 150, w, ease_out(prog(t, 0.5 * d + i * 0.2, 0.3)), t, 6100 + i)
        chip(c, "GRANDE DEMAIS", W / 2, 1360, 54, ease_out(prog(t, 0.75 * d, 0.3)), t=t, seed=6110)


def s2_pequeno(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        week_boxes(c, t, d, {0: 0.2, 3: 0.35}, 6200)
        p = ease_out(prog(t, 0.3 * d, 0.3))
        clock(c, 300, 1230, 110, (40 / 60) * ease(prog(t, 0.3 * d, 0.4 * d)), t, 6210)
        marker(c, "40 min", 470, 1260, 80, BLUEPEN, p)
        hand(c, "até em semana ruim", W / 2 - 20, 1460, 52, MARGIN, ease_out(prog(t, 0.6 * d, 0.3)), align="center")


def s2_meta(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        hand(c, "meta:", LEFT + 10, 840, 56, MUTED, ease_out(prog(t, 0.05, 0.3)))
        hand(c, "perder 10 kg", LEFT + 20, 980, 72, INK, ease_out(prog(t, 0.1, 0.3)))
        font(c, HAND, 72); w = c.text_extents("perder 10 kg").x_advance
        strike(c, LEFT + 20, 980, w, ease_out(prog(t, 0.35 * d, 0.3)), t, 6300)
        q = ease_out(prog(t, 0.5 * d, 0.3))
        font(c, TITLE, 96); w2 = c.text_extents("NÃO FALTAR").x_advance
        highlight(c, LEFT + 10, 1110, w2 + 20, 70, prog(t, 0.55 * d, 0.3))
        marker(c, "NÃO FALTAR", LEFT + 20, 1180, 96, INK, q)


def s2_seguidos(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        week_boxes(c, t, d, {0: 0.1, 1: "x", 2: 0.55, 4: 0.7}, 6400)
        q = ease_out(prog(t, 0.45 * d, 0.3))
        hand(c, "faltou 1? segue o jogo", LEFT + 10, 1100, 58, INK, q)
        chip(c, "NUNCA 2 SEGUIDOS", W / 2, 1300, 56, ease_out(prog(t, 0.65 * d, 0.3)), t=t, seed=6410)


# ================================================================ registro
VIS = dict(
    pr_hook=pr_hook, pr_niveis=pr_niveis, pr_n1=_nivel("joelho", "joelhos no chão", "corpo reto"),
    pr_n2=_nivel("completa", "nos pés", "quadril firme"), pr_n3=_nivel("um_pe", "tira um pé", "e troca"), pr_regra=pr_regra,
    ap_hook=ap_hook, ap_desenho=ap_desenho, ap_banco=ap_banco, ap_leve=ap_leve, ap_professor=ap_professor, ap_tres=ap_tres,
    pg_hook=pg_hook, pg_sair=pg_sair, pg_mochila=pg_mochila, pg_dez=pg_dez, pg_ficou=pg_ficou, pg_agenda=pg_agenda,
    mg_hook=mg_hook, mg_muda=mg_muda, mg_tres=mg_tres, mg_amais=mg_amais, mg_prato=mg_prato, mg_balanca=mg_balanca,
    s2_hook=s2_hook, s2_empolga=s2_empolga, s2_grande=s2_grande, s2_pequeno=s2_pequeno, s2_meta=s2_meta, s2_seguidos=s2_seguidos,
)
CONC = {'diaum_06_prancha': ('pr_', ["começa no joelho", "3 × 30 s = sobe", "sem vergonha"]),
        'diaum_04_aparelhos': ('ap_', ["olha o desenho", "regula o banco", "peso leve + pergunta"]),
        'diaum_07_preguica': ('pg_', ["deixa tudo pronto", "só 10 minutos", "quem começa, termina"]),
        'diaum_05_magro': ('mg_', ["força 3x por semana", "comida a mais", "paciência"]),
        'diaum_08_semana2': ('s2_', ["começa pequeno", "meta: não faltar", "nunca 2 seguidos"])}
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "swish"), ("0.5d", "pop")]) for k in VIS}
for chave, (pre, items) in CONC.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conc_factory(items)
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "swish"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = [(0.0, "swish"), ("0.15", "pop"), ("0.55d", "ding")]


# respiro de câmera contínuo (evita quadro parado > 3 s depois que os elementos terminam de entrar)
def _respira(f):
    def g(c, t, d, b):
        c.save(); k = 1 + 0.012 * math.sin(t * 1.7)
        c.translate(W / 2, CY); c.scale(k, k); c.rotate(0.004 * math.sin(t * 1.1)); c.translate(-W / 2, -CY)
        f(c, t, d, b); c.restore()
    return g


VIS = {k: _respira(v) for k, v in VIS.items()}
