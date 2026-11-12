"""FIBRA — produção 13/11: gordura sai pelo pulmão (g_), barra fixa 5 músculos (b_), enjoo no treino de perna (e_)."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, squat, conclusao_factory, cta_flex, SFX_CTA, arm
import pauta_1311 as PA

CY = 1060
FAT = (1.0, 0.78, 0.35)


def ok_mark(c, x, y, r, p, col=CYAN):
    if p <= 0:
        return
    c.new_path(); c.arc(x, y, r, 0, 6.3); rgb(c, col, p); c.set_line_width(4); c.stroke()
    poly(c, [(x - r * 0.5, y), (x - r * 0.1, y + r * 0.4), (x + r * 0.55, y - r * 0.45)], col, 5, p)


def no_mark(c, x, y, r, p, col=PINK):
    if p <= 0:
        return
    k = r * 0.8 * p
    cap_line(c, x - k, y - k, x + k, y + k, col, 10); cap_line(c, x + k, y - k, x - k, y + k, col, 10)


def bar_pct(c, x, y, w, h, frac, col, p=1.0, bg=NAVY2):
    rrect(c, x, y, w, h, h / 2, bg, p)
    if frac > 0.01:
        rrect(c, x, y, max(h, w * frac), h, h / 2, col, p)


# ================================================================ GORDURA (g_)
def fat_cell(c, x, y, r, t, p=1.0, shrink=0.0):
    rr = r * (1 - 0.45 * shrink)
    c.new_path(); c.arc(x, y, rr, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    disk(c, x, y, rr * 0.78, FAT, 0.85 * p)
    disk(c, x - rr * 0.25, y - rr * 0.3, rr * 0.18, INK, 0.25 * p)
    disk(c, x + rr * 0.72, y + rr * 0.1, 12, CYAN, p)  # núcleo espremido na borda


def molecules(c, x, y, t, n, p, label="CO2", col=PINK, spread=260, rise=520, seed=3):
    rnd = random.Random(seed)
    for k in range(n):
        f = (t * 0.45 + rnd.random()) % 1
        xx = x + rnd.uniform(-spread, spread) * (0.3 + 0.7 * f)
        yy = y - rise * f
        a = p * (1 - f) * 1.2
        mono(c, label, xx, yy, 28, col, clamp(a), align="center")


def g_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        sh = 0.5 + 0.5 * math.sin(t * 2.2)
        fat_cell(c, 380, 1230, 190, t, p, sh * 0.6)
        molecules(c, 380, 1050, t, 10, p, spread=200, rise=330)
        callout(c, 470, 1300, 640, 1420, "CÉLULA DE GORDURA", ease_out(prog(t, 0.3, 0.5)), FAT, 28)
        _mono_right(c, "SAÍDA: AR EXPIRADO", RIGHT - 10, 760, 32, PINK, ease_out(prog(t, 0.4 * d, 0.3)))


def drop(c, x, y, s, p=1.0, col=CYAN):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(0, -150); c.curve_to(40, -80, 110, -10, 110, 50); c.curve_to(110, 120, 55, 160, 0, 160)
    c.curve_to(-55, 160, -110, 120, -110, 50); c.curve_to(-110, -10, -40, -80, 0, -150); c.close_path()
    rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, col, p); c.set_line_width(4 / s); c.stroke()
    c.restore()


def g_suor(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        bob = 12 * math.sin(t * 3)
        drop(c, 300, 1040 + bob, 1.5, p)
        mono(c, "H2O", 300, 1090 + bob, 44, CYAN, p, align="center")
        mono(c, "+ SAL", 300, 1140 + bob, 30, MUTED, p, align="center")
        q = ease_out(prog(t, 0.3 * d, 0.3))
        panel(c, 560, 820, 360, 130, q)
        mono(c, "GORDURA?", 600, 900, 40, INK, q)
        no_mark(c, 860, 885, 36, q)
        r = ease_out(prog(t, 0.55 * d, 0.3))
        panel(c, 560, 1060, 360, 130, r, CYAN)
        mono(c, "RESFRIA O", 740, 1115, 32, CYAN, r, align="center")
        mono(c, "CORPO", 740, 1160, 32, CYAN, r, align="center")
        ok_mark(c, 740, 1290, 40, ease_out(prog(t, 0.65 * d, 0.3)))


def chain(c, x, y, n, t, p, brk=0.0, col=FAT):
    for i in range(n):
        dx = (i - n / 2) * 70
        sep = brk * (i - n / 2) * 30
        yy = y + math.sin(t * 3 + i) * 6 + brk * (i % 2) * 40
        if i < n - 1 and brk < 0.3:
            cap_line(c, x + dx, yy, x + dx + 70, y + math.sin(t * 3 + i + 1) * 6, col, 6, p)
        disk(c, x + dx + sep, yy, 22, col, p)


def g_quebra(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        brk = ease(prog(t, 0.45 * d, 0.35 * d))
        chain(c, 500, 1050, 7, t, p, brk)
        mono(c, "TRIGLICERÍDEO", 500, 960, 30, FAT, p * (1 - brk), align="center")
        for k in range(5):
            f = ease(prog(t, 0.1 + k * 0.12, 0.5 * d))
            disk(c, lerp(LEFT + 40 + k * 60, 300 + k * 90, f), lerp(1400, 1120, f), 16, CYAN, p)
            mono(c, "O2", lerp(LEFT + 40 + k * 60, 300 + k * 90, f), lerp(1400, 1120, f) + 46, 22, CYAN, p * (1 - f), align="center")
        q = ease_out(prog(t, 0.6 * d, 0.3))
        mono(c, "+ O2  →  CO2 + H2O", W / 2 - 40, 1360, 40, INK, q, align="center")


def g_co2(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        f = 0.84 * ease(prog(t, 0.15, 0.6 * d))
        mono(c, "SAÍDA DA GORDURA", LEFT + 20, 760, 30, MUTED, p)
        bar_pct(c, LEFT + 20, 790, RIGHT - LEFT - 40, 70, f, PINK, p)
        draw_text(c, f"{int(round(f * 100))}%", LEFT + 20, 1010, 150, PINK, TITLE, p)
        mono(c, "CO2 · AR QUE VOCÊ SOLTA", LEFT + 20, 1070, 32, INK, ease_out(prog(t, 0.4 * d, 0.3)))
        molecules(c, 640, 1460, t, 12, ease_out(prog(t, 0.2, 0.4)), spread=200, rise=330, seed=7)
        mono(c, "FONTE: BMJ 2014", LEFT + 20, 1500, 24, MUTED, ease_out(prog(t, 0.5 * d, 0.3)))


def g_agua(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        f = 0.16 * ease(prog(t, 0.15, 0.4 * d))
        mono(c, "SAÍDA DA GORDURA", LEFT + 20, 760, 30, MUTED, p)
        rrect(c, LEFT + 20, 790, RIGHT - LEFT - 40, 70, 35, NAVY2, p)
        rrect(c, LEFT + 20, 790, (RIGHT - LEFT - 40) * 0.84, 70, 35, PINK, 0.35 * p)
        rrect(c, LEFT + 20 + (RIGHT - LEFT - 40) * (1 - f), 790, max(1, (RIGHT - LEFT - 40) * f), 70, 35, CYAN, p)
        draw_text(c, f"{int(round(f * 100))}%", LEFT + 20, 1010, 150, CYAN, TITLE, p)
        mono(c, "ÁGUA", LEFT + 260, 1000, 44, CYAN, p)
        for i, lab in enumerate(("URINA", "SUOR", "RESPIRAÇÃO")):
            q = ease_out(prog(t, 0.3 * d + i * 0.25, 0.3))
            drop(c, LEFT + 110 + i * 270, 1240 + 6 * math.sin(t * 3 + i), 0.45, q)
            mono(c, lab, LEFT + 110 + i * 270, 1380, 28, INK, q, align="center")


def g_gasto(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        panel(c, LEFT + 10, 740, RIGHT - LEFT - 20, 220, p)
        mono(c, "RESPIRAR RÁPIDO", LEFT + 50, 820, 34, INK, p)
        wave(c, LEFT + 50, 890, RIGHT - LEFT - 220, 22, t * 2.4, p)
        no_mark(c, RIGHT - 90, 850, 50, ease_out(prog(t, 0.3 * d, 0.3)))
        q = ease_out(prog(t, 0.4 * d, 0.35))
        if q > 0:
            bend = 0.5 + 0.5 * math.sin(t * 3.5)
            arm(c, LEFT + 40, 1240, 0.95, bend, q, 0.6 + 0.4 * bend, t)
            mono(c, "MÚSCULO TRABALHANDO", LEFT + 40, 1460, 34, CYAN, q)
            ok_mark(c, RIGHT - 90, 1130, 50, ease_out(prog(t, 0.6 * d, 0.3)))


def wave(c, x, y, w, amp, t, p, col=CYAN):
    pts = [(x + w * i / 80, y + math.sin(i / 80 * 30 + t * 6) * amp) for i in range(81)]
    poly(c, pts, col, 4, p)


# ================================================================ BARRA (b_)
BX0, BX1, BARY = 300, 760, 760


def _ik(sx, sy, hx, hy, L, out):
    D = math.hypot(hx - sx, hy - sy); mx, my = (sx + hx) / 2, (sy + hy) / 2
    if D >= 2 * L:
        return mx, my
    k = math.sqrt(L * L - (D / 2) ** 2); nx, ny = -(hy - sy) / D, (hx - sx) / D
    if nx * out < 0:
        nx, ny = -nx, -ny
    return mx + nx * k, my + ny * k


def pullup(c, t, pull, hl, p=1.0):
    """atleta de costas pendurado na barra (vista técnica). pull 0 = braço estendido, 1 = queixo na barra. hl: músculo -> 0..1"""
    cx = (BX0 + BX1) / 2 + 0
    cap_line(c, BX0 - 120, BARY, BX1 + 120, BARY, INK, 12, p)
    for x in (BX0 - 120, BX1 + 120):
        cap_line(c, x, BARY - 40, x, BARY + 40, MUTED, 8, p)
    sy = lerp(BARY + 260, BARY + 120, pull)  # altura dos ombros
    shL, shR = (cx - 120, sy), (cx + 120, sy)
    hL, hR = (BX0, BARY), (BX1, BARY)
    eL = _ik(*shL, *hL, 165, -1); eR = _ik(*shR, *hR, 165, 1)
    # tronco (V) com dorsais
    hipy = sy + 320
    torso = [(cx - 150, sy - 10), (cx + 150, sy - 10), (cx + 85, hipy), (cx - 85, hipy)]
    c.new_path(); c.move_to(*torso[0])
    for pt in torso[1:]:
        c.line_to(*pt)
    c.close_path(); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    for sd in (-1, 1):  # dorsal
        c.new_path(); c.move_to(cx + sd * 140, sy + 20); c.curve_to(cx + sd * 150, sy + 160, cx + sd * 110, sy + 280, cx + sd * 30, hipy - 30)
        c.line_to(cx + sd * 20, sy + 150); c.close_path()
        rgb(c, mix(NAVY2, PINK, hl.get("dorsal", 0)), p); c.fill_preserve(); rgb(c, CYAN, p * 0.8); c.set_line_width(2); c.stroke()
        ellipse(c, cx + sd * 55, sy + 80, 40, 70, sd * 0.25, mix(NAVY2, PINK, hl.get("romboide", 0)), p, CYAN)  # romboide/trapézio
    # trapézio superior (losango) + cabeça
    ellipse(c, cx, sy - 30, 70, 30, 0, mix(NAVY2, PINK, hl.get("romboide", 0) * 0.6), p, CYAN)
    c.new_path(); c.arc(cx, sy - 110, 62, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    # braços
    for sh, el, hd in ((shL, eL, hL), (shR, eR, hR)):
        ang = math.atan2(el[1] - sh[1], el[0] - sh[0])
        mx, my = (sh[0] + el[0]) / 2, (sh[1] + el[1]) / 2
        ellipse(c, mx, my, 92, 34, ang, mix(NAVY2, PINK, hl.get("biceps", 0)), p, CYAN)
        ang2 = math.atan2(hd[1] - el[1], hd[0] - el[0])
        ellipse(c, (el[0] + hd[0]) / 2, (el[1] + hd[1]) / 2, 88, 26, ang2, mix(NAVY2, PINK, hl.get("antebraco", 0)), p, CYAN)
        for j in (sh, el):
            disk(c, j[0], j[1], 9, INK, p)
        disk(c, hd[0], hd[1], 20, mix(INK, PINK, hl.get("antebraco", 0)), p)
    # pernas
    for sd in (-1, 1):
        cap_line(c, cx + sd * 50, hipy, cx + sd * 60, hipy + 170, CYAN, 26, p); cap_line(c, cx + sd * 50, hipy, cx + sd * 60, hipy + 170, NAVY2, 18, p)
    return dict(sy=sy, cx=cx, eL=eL, eR=eR, hipy=hipy)


def _pull(t, speed=2.0):
    return 0.5 - 0.5 * math.cos(t * speed)


def b_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        k = int(5 * clamp(prog(t, 0.2, d * 0.7)) + 0.0001)
        order = ("dorsal", "biceps", "biceps", "romboide", "antebraco")
        hl = {}
        for i in range(k):
            hl[order[i]] = 1.0
        pullup(c, t, _pull(t), hl, ease_out(prog(t, 0, 0.3)))
        _mono_right(c, f"MÚSCULOS: {k}", RIGHT - 10, 1520, 40, PINK if k else MUTED, ease_out(prog(t, 0.1, 0.3)))


def _bfocus(muscle, label, anchor):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.06, cy=CY):
            g = ease_out(prog(t, 0.1, 0.4))
            j = pullup(c, t, _pull(t, 1.8), {muscle: g})
            px, py = anchor(j)
            q = ease_out(prog(t, 0.25, 0.4))
            if q > 0:
                c.new_path(); c.arc(px, py, 46 + 8 * math.sin(t * 6), 0, 6.3); rgb(c, PINK, q); c.set_line_width(4); c.stroke()
            chip(c, label, W / 2 - 40, 660, PINK, NAVY, 40, q)
    return f


def b_pegada(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, (lab, foco, v_b, v_c) in enumerate((("PALMA PRA VOCÊ", "+ BÍCEPS", 0.85, 0.55), ("PALMA PRA FRENTE", "+ COSTAS", 0.5, 0.85))):
            q = ease_out(prog(t, 0.05 + i * 0.4 * d, 0.35))
            if q <= 0:
                continue
            y0 = 740 + i * 390
            panel(c, LEFT + 10, y0, RIGHT - LEFT - 20, 350, q)
            mono(c, lab, LEFT + 50, y0 + 70, 34, INK, q)
            # mão na barra
            cap_line(c, LEFT + 60, y0 + 150, LEFT + 330, y0 + 150, INK, 10, q)
            disk(c, LEFT + 195, y0 + 165, 34, NAVY2, q)
            c.new_path(); c.arc(LEFT + 195, y0 + 165, 34, 0, 6.3); rgb(c, CYAN, q); c.set_line_width(3); c.stroke()
            for k in range(4):
                fy = y0 + 132 if i == 0 else y0 + 196
                cap_line(c, LEFT + 168 + k * 18, y0 + 165, LEFT + 168 + k * 18, fy, CYAN, 6, q)
            for j, (m, v) in enumerate((("BÍCEPS", v_b), ("COSTAS", v_c))):
                yy = y0 + 150 + j * 90
                mono(c, m, LEFT + 380, yy, 26, MUTED, q)
                bar_pct(c, LEFT + 540, yy - 26, 260, 32, v * ease(prog(t, 0.2 + i * 0.4 * d, 0.6)), PINK if j == i else LINE, q)
            chip(c, foco, LEFT + 530, y0 + 310, PINK, NAVY, 40, ease_out(prog(t, 0.3 + i * 0.4 * d, 0.3)))


# ================================================================ ENJOO (e_)
def stomach(c, x, y, s, t, p=1.0, queasy=0.0, food=0, flow=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    wob = queasy * 6 * math.sin(t * 9)
    c.new_path(); c.move_to(-40, -170); c.curve_to(-30, -90, -140, -60, -130, 40); c.curve_to(-120, 150, 40, 190, 130, 110)
    c.curve_to(190, 60, 160, -20, 90, -10); c.curve_to(30, 0, 30, -100, 40, -170); c.close_path()
    c.translate(wob, 0)
    rgb(c, mix(NAVY2, PINK, 0.25 * flow), p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(4 / s); c.stroke()
    rnd = random.Random(5)
    for k in range(food):
        rrect(c, -80 + rnd.uniform(0, 130), -10 + rnd.uniform(0, 110), 44, 34, 8, FAT, 0.85 * p)
    c.restore()
    if queasy > 0:
        for k in range(3):
            yy = y - 220 * s - k * 30
            pts = [(x - 90 + i * 9, yy + math.sin(i * 0.8 + t * 6 + k) * 10) for i in range(21)]
            poly(c, pts, GOOD, 4, p * queasy)


def e_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        dep = 0.5 + 0.5 * math.sin(t * 2.4 - 1.5)
        squat(c, 300, 1440, 0.62, dep, {"quad": 1.0, "gluteo": 0.8}, t, ease_out(prog(t, 0, 0.3)))
        q = ease_out(prog(t, 0.25, 0.4))
        stomach(c, 740, 1060, 1.1, t, q, queasy=ease(prog(t, 0.5, 0.6)), food=4)
        callout(c, 760, 1180, 640, 1480, "ENJOO", ease_out(prog(t, 0.45 * d, 0.4)), GOOD, 36, side="left")


def e_sangue(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        dep = 0.55 + 0.45 * math.sin(t * 2.2 - 1.5)
        g = ease_out(prog(t, 0.1, 0.4))
        j = squat(c, 380, 1440, 0.72, dep, {"quad": g, "gluteo": g, "adutor": g}, t)
        rnd = random.Random(2)
        for k in range(14):
            f = (t * 0.7 + rnd.random()) % 1
            x0, y0 = RIGHT - 40, 760 + rnd.uniform(0, 120)
            disk(c, lerp(x0, j["quad"][0], f), lerp(y0, j["quad"][1], f), 9, PINK, g * (1 - f * 0.5))
        _mono_right(c, "MAIOR GRUPO MUSCULAR", RIGHT - 10, 1520, 30, PINK, ease_out(prog(t, 0.4 * d, 0.3)))


def splitter(c, t, p, leg_share):
    """coração -> divide para INTESTINO (esquerda) e PERNAS (direita); leg_share 0..1 muda a espessura e o fluxo"""
    hx, hy = W / 2 - 40, 780
    c.new_path(); c.arc(hx - 28, hy, 34, 0, 6.3); c.arc(hx + 28, hy, 34, 0, 6.3); rgb(c, PINK, p); c.fill()
    mono(c, "CORAÇÃO", hx + 90, hy + 10, 26, MUTED, p)
    gl, gr = (LEFT + 140, 990), (RIGHT - 140, 990)
    wl = lerp(30, 8, leg_share); wr = lerp(12, 34, leg_share)
    for (tx, ty), w_, share, seed in ((gl, wl, 1 - leg_share, 1), (gr, wr, leg_share, 2)):
        cap_line(c, hx, hy + 30, tx, ty, PINK, w_ + 8, p); cap_line(c, hx, hy + 30, tx, ty, NAVY, w_, p)
        n = max(1, int(2 + 8 * share))
        for k in range(n):
            f = (t * 0.9 + k / n) % 1
            disk(c, lerp(hx, tx, f), lerp(hy + 30, ty, f), 9, INK, p)
    stomach(c, gl[0], gl[1] + 210, 0.6, t, p, flow=1 - leg_share)
    mono(c, "DIGESTÃO", gl[0], gl[1] + 390, 30, INK, p, align="center")
    squat(c, gr[0] - 40, 1440, 0.38, 0.5 + 0.5 * math.sin(t * 2.5), {"quad": leg_share, "gluteo": leg_share}, t, p)
    mono(c, "PERNAS", gr[0] - 40, 1520, 30, INK, p, align="center")


def e_desvio(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        splitter(c, t, ease_out(prog(t, 0, 0.3)), ease(prog(t, 0.25 * d, 0.5 * d)))


def e_oitenta(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        f = 1 - 0.8 * ease(prog(t, 0.2, 0.6 * d))
        mono(c, "FLUXO NA DIGESTÃO", LEFT + 20, 760, 30, MUTED, p)
        x0, y0, hh = LEFT + 60, 1460, 600
        rrect(c, x0, y0 - hh, 200, hh, 20, NAVY2, p)
        rrect(c, x0, y0 - hh * f, 200, hh * f, 20, PINK, p)
        dline(c, x0 - 20, y0 - hh, x0 + 240, y0 - hh, LINE, 2, (6, 8), p)
        draw_text(c, f"−{int(round((1 - f) * 100))}%", x0 + 290, 1180, 150, PINK, TITLE, p)
        mono(c, "EM TREINO INTENSO", x0 + 300, 1240, 30, INK, ease_out(prog(t, 0.4 * d, 0.3)))
        stomach(c, x0 + 480, 1470, 0.45, t, ease_out(prog(t, 0.3 * d, 0.3)), queasy=1 - f)


def e_parada(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        stomach(c, 420, 1120, 1.5, t, p, queasy=ease(prog(t, 0.3 * d, 0.4)), food=7, flow=0.2)
        q = ease_out(prog(t, 0.2, 0.3))
        # ícone de pausa
        rrect(c, 700, 860, 36, 120, 10, PINK, q); rrect(c, 760, 860, 36, 120, 10, PINK, q)
        mono(c, "DIGESTÃO", 748, 1030, 30, INK, q, align="center")
        mono(c, "EM ESPERA", 748, 1070, 30, PINK, q, align="center")
        chip(c, "ENJOO", 740, 1420, GOOD, NAVY, 52, ease_out(prog(t, 0.45 * d, 0.3)))


def e_evita(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        rows = (("COMIDA LEVE 1–2 H ANTES", CYAN), ("MAIS DESCANSO NAS SÉRIES", CYAN), ("ÁGUA AOS GOLES", CYAN), ("FREQUENTE? MÉDICO", PINK))
        n = len(rows)
        for i, (lab, col) in enumerate(rows):
            q = ease_out(prog(t, 0.05 + i * (d * 0.7 / n), 0.35))
            if q <= 0:
                continue
            y = 780 + i * 170
            panel(c, LEFT + 10, y, RIGHT - LEFT - 20, 130, q, col)
            if i == 0:
                clock(c, LEFT + 80, y + 65, 40, (t * 0.2) % 1, q)
            elif i == 1:
                for k in range(3):
                    rrect(c, LEFT + 50 + k * 30, y + 45 + (k % 2) * 6, 18, 40, 4, CYAN, q)
            elif i == 2:
                drop(c, LEFT + 80, y + 60 + 4 * math.sin(t * 3), 0.28, q)
            else:
                c.new_path(); c.arc(LEFT + 80, y + 65, 36, 0, 6.3); rgb(c, PINK, q); c.set_line_width(4); c.stroke()
                cap_line(c, LEFT + 80, y + 45, LEFT + 80, y + 85, PINK, 8, q); cap_line(c, LEFT + 60, y + 65, LEFT + 100, y + 65, PINK, 8, q)
            mono(c, lab, LEFT + 150, y + 76, 32, INK, q)


# ================================================================ registro
VIS = dict(
    g_hook=g_hook, g_suor=g_suor, g_quebra=g_quebra, g_co2=g_co2, g_agua=g_agua, g_gasto=g_gasto,
    b_hook=b_hook, b_pegada=b_pegada,
    b_dorsal=_bfocus("dorsal", "GRANDE DORSAL", lambda j: (j["cx"] + 120, j["sy"] + 180)),
    b_biceps=_bfocus("biceps", "BÍCEPS + BRAQUIAL", lambda j: ((j["cx"] + 120 + j["eR"][0]) / 2, (j["sy"] + j["eR"][1]) / 2)),
    b_romboide=_bfocus("romboide", "ROMBOIDES + TRAPÉZIO", lambda j: (j["cx"] - 55, j["sy"] + 80)),
    b_antebraco=_bfocus("antebraco", "ANTEBRAÇO", lambda j: ((j["eR"][0] + BX1) / 2, (j["eR"][1] + BARY) / 2)),
    e_hook=e_hook, e_sangue=e_sangue, e_desvio=e_desvio, e_oitenta=e_oitenta, e_parada=e_parada, e_evita=e_evita,
)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
for chave, pre in (("fibra_07_gordura", "g_"), ("fibra_08_barra", "b_"), ("fibra_09_enjoo", "e_")):
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
