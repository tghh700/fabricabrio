"""FIBRA — produção 21/11 (prancha técnica, build3): dor pra sentar depois da perna (se_), veias saltando (ve_),
formigamento do pré-treino (fr_), sem fôlego na escada (es_). Uma figura por cena; nada atravessa o corpo;
só glifos da fonte (sem ✓ ✦ ↑ — marcas desenhadas)."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA, squat, arm
from scenes_fibra_g import bar_pct, ok_mark, no_mark
from scenes_fibra_1811 import counter, heart, lungs, wave_lines
from scenes_fibra_1911 import runner, treadmill, itch_marks, face, CX, CY, RED, ORANGE
import pauta_2111 as PA

MITO = (0.98, 0.62, 0.25)
FAT = (0.95, 0.80, 0.45)
POWDER = (0.95, 0.55, 0.75)


# ------------------------------------------------------------------ peças
def pain_marks(c, x, y, t, k, p=1.0, n=7, r=70):
    """raios curtos em volta de um ponto (dor)"""
    for i in range(n):
        a = i * 2 * math.pi / n + 0.3
        rr = r + 10 * math.sin(t * 10 + i)
        cap_line(c, x + rr * math.cos(a), y + rr * math.sin(a), x + (rr + 34) * math.cos(a), y + (rr + 34) * math.sin(a),
                 PINK, 6, p * k * (0.6 + 0.4 * math.sin(t * 12 + i)))


def box(c, x, y, w, h, p=1.0):
    """caixote/banco técnico (contorno ciano)"""
    rrect(c, x, y, w, h, 14, NAVY2, p)
    rrect(c, x, y, w, h, 14); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()


def pain_chart(c, t, x, y, w, h, prog_x, p=1.0):
    """dor ao longo dos dias: sobe, pico entre o dia 1 e o 3, desce"""
    if p <= 0:
        return
    cap_line(c, x, y + h, x + w, y + h, LINE, 3, p); cap_line(c, x, y, x, y + h, LINE, 3, p)
    rrect(c, x + w * 0.25, y, w * 0.5, h, 10, PINK, 0.12 * p)
    n = 60; k = max(2, int(n * clamp(prog_x)))
    def f(u):
        d = u * 4.0
        return math.exp(-((d - 2.0) / 0.95) ** 2) * (1 if d > 0.15 else d / 0.15)
    pts = [(x + w * i / (n - 1), y + h - h * 0.9 * f(i / (n - 1))) for i in range(n)]
    poly(c, pts[:k], PINK, 8, p)
    for dd in range(5):
        mono(c, f"DIA {dd}", x + w * dd / 4, y + h + 44, 24, MUTED, p, align="center")
    mono(c, "DOR", x - 6, y - 20, 26, PINK, p)


def skin_section(c, t, x, y, w, fat_h, vein_r, p=1.0, title=""):
    """corte da pele: pele (topo), gordura (amarela) e a veia embaixo; quanto mais fina a gordura, mais a veia empurra a pele"""
    if p <= 0:
        return
    top = y
    bump = clamp((90 - fat_h) / 70)
    vy = top + 30 + fat_h + vein_r
    # pele com calombo sobre a veia
    pts = []
    for i in range(41):
        u = i / 40
        xx = x + u * w
        yy = top - 46 * bump * math.exp(-((u - 0.5) / 0.13) ** 2)
        pts.append((xx, yy))
    c.new_path(); c.move_to(*pts[0])
    for q in pts[1:]:
        c.line_to(*q)
    c.line_to(x + w, top + 30 + fat_h); c.line_to(x, top + 30 + fat_h); c.close_path()
    rgb(c, FAT, 0.85 * p); c.fill()
    poly(c, pts, INK, 6, p)
    rrect(c, x, top + 30 + fat_h, w, 160, 0, (0.30, 0.10, 0.18), p)   # músculo
    mono(c, "MÚSCULO", x + 20, top + 30 + fat_h + 120, 22, MUTED, p)
    disk(c, x + w / 2, vy - 46 * bump, vein_r, CYAN, p)
    disk(c, x + w / 2, vy - 46 * bump, vein_r * 0.6, NAVY, p)
    mono(c, title, x + w / 2, top - 90, 26, INK, p, align="center")


def scoop(c, x, y, s, p=1.0, fill=1.0):
    """medidor (scoop) de pré-treino"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s, s)
    cap_line(c, 60, -10, 190, -60, CYAN, 16, p)
    c.new_path(); c.arc(0, 0, 70, 0, math.pi); c.close_path(); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
    if fill > 0:
        c.new_path(); c.arc(0, -4, 64 * fill, math.pi, 2 * math.pi); c.close_path(); rgb(c, POWDER, p); c.fill()
    c.restore()


def molecule(c, x, y, s, p=1.0, col=POWDER):
    """beta-alanina estilizada: 3 bolinhas ligadas + 'cauda'"""
    if p <= 0:
        return
    pts = [(x - 60 * s, y + 20 * s), (x, y - 20 * s), (x + 60 * s, y + 20 * s), (x + 110 * s, y - 15 * s)]
    poly(c, pts, INK, 4, p)
    for i, (px, py) in enumerate(pts):
        disk(c, px, py, (22 if i < 3 else 14) * s, col if i != 1 else CYAN, p)


def skin_nerves(c, t, x, y, w, k, p=1.0):
    """pele com terminações nervosas; k 0..1 = sensores ativados (rosa, piscando)"""
    rrect(c, x, y, w, 40, 14, (0.45, 0.25, 0.32), p)
    poly(c, [(x, y), (x + w, y)], INK, 5, p)
    for i in range(6):
        nx = x + 70 + i * (w - 140) / 5
        on = k * (0.6 + 0.4 * math.sin(t * 9 + i * 1.7))
        cap_line(c, nx, y + 40, nx, y + 230, mix(CYAN, PINK, on), 5, p)
        poly(c, [(nx, y + 40), (nx - 22, y + 8)], mix(CYAN, PINK, on), 4, p)
        poly(c, [(nx, y + 40), (nx + 22, y + 8)], mix(CYAN, PINK, on), 4, p)
        disk(c, nx, y + 40, 12, mix(CYAN, PINK, on), p)
    cap_line(c, x + 70, y + 230, x + w - 70, y + 230, mix(CYAN, PINK, k), 6, p)


def stairs(c, x0, y0, n, sw, sh, p=1.0):
    """escada subindo para a direita; (x0, y0) = pé do primeiro degrau"""
    pts = [(x0, y0)]
    for i in range(n):
        pts.append((x0 + i * sw, y0 - (i + 1) * sh))
        pts.append((x0 + (i + 1) * sw, y0 - (i + 1) * sh))
    poly(c, pts, CYAN, 5, p)
    cap_line(c, x0 - 40, y0, x0, y0, CYAN, 5, p)


def mito_cell(c, x, y, r, p=1.0, t=0.0):
    """mitocôndria (usina de energia)"""
    if p <= 0:
        return
    ellipse(c, x, y, r * 1.6, r, 0.3, MITO, p, INK)
    pts = [(x - r * 1.1 + i * r * 0.32, y + (r * 0.45 if i % 2 else -r * 0.45)) for i in range(8)]
    poly(c, pts, NAVY, 3, p)


def _ik_knee(h, f, L):
    dx, dy = f[0] - h[0], f[1] - h[1]; D = min(math.hypot(dx, dy), 2 * L - 1)
    mx, my = h[0] + dx / 2, h[1] + dy / 2
    a = math.sqrt(max(L * L - (D / 2) ** 2, 0)); n = math.hypot(dx, dy) or 1
    nx, ny = -dy / n, dx / n
    if nx < 0: nx, ny = -nx, -ny                          # joelho para a frente (direita)
    return (mx + nx * a, my + ny * a)


def climber(c, t, x0, y0, sw, sh, s, p=1.0, rate=1.1):
    """figura técnica subindo a escada: pé de apoio sempre em cima de um degrau, o outro passa por cima do degrau."""
    L = 190 * s; H = 250 * s
    u = t * rate; n = int(u); f = u - n
    F = lambda k: (x0 + (k + 0.5) * sw, y0 - (k + 1) * sh)
    stance = F(n)
    a, b = F(n - 1), F(n + 1)
    ff = ease(f)
    swing = (lerp(a[0], b[0], ff), lerp(a[1], b[1], ff) - math.sin(math.pi * ff) * (sh + 40 * s))
    hip = (x0 + (n + f + 0.3) * sw, y0 - (n + f + 1) * sh - H)
    lean = 0.28
    Lb = 300 * s
    sho = (hip[0] + math.sin(lean) * Lb, hip[1] - math.cos(lean) * Lb)
    dim = mix(INK, MUTED, 0.5)
    back, front = (swing, stance) if n % 2 else (stance, swing)
    kb = _ik_knee(hip, back, L)
    cap_line(c, hip[0], hip[1], kb[0], kb[1], dim, 7, p); cap_line(c, kb[0], kb[1], back[0], back[1], dim, 7, p)
    cap_line(c, back[0], back[1], back[0] + 36 * s, back[1], dim, 7, p)
    sw_a = 0.5 * math.sin(math.pi * u)
    el = (sho[0] + 140 * s * math.sin(sw_a), sho[1] + 140 * s * math.cos(sw_a))
    cap_line(c, sho[0], sho[1], el[0], el[1], dim, 6, p); cap_line(c, el[0], el[1], el[0] + 110 * s, el[1] - 40 * s, dim, 6, p)
    mx, my = (hip[0] + sho[0]) / 2, (hip[1] + sho[1]) / 2
    ellipse(c, mx, my, Lb * 0.5, 62 * s, math.atan2(sho[1] - hip[1], sho[0] - hip[0]), NAVY2, p, CYAN)
    cap_line(c, hip[0], hip[1], sho[0], sho[1], INK, 6, p)
    hx, hy = sho[0] + math.sin(lean) * 80 * s, sho[1] - math.cos(lean) * 80 * s
    c.new_path(); c.arc(hx, hy, 52 * s, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    kf = _ik_knee(hip, front, L)
    cap_line(c, hip[0], hip[1], kf[0], kf[1], INK, 7, p); cap_line(c, kf[0], kf[1], front[0], front[1], INK, 7, p)
    cap_line(c, front[0], front[1], front[0] + 36 * s, front[1], INK, 7, p)
    el2 = (sho[0] - 140 * s * math.sin(sw_a), sho[1] + 140 * s * math.cos(sw_a))
    cap_line(c, sho[0], sho[1], el2[0], el2[1], INK, 6, p); cap_line(c, el2[0], el2[1], el2[0] + 110 * s, el2[1] - 40 * s, INK, 6, p)
    for j in (hip, sho, kf):
        disk(c, j[0], j[1], 9, INK, p)
    return dict(head=(hx, hy), hip=hip)


# ================================================================ SENTAR (se_)
def se_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = lerp(0.15, 0.82, ease(prog(t, 0.2, 1.4))) + 0.02 * math.sin(t * 24) * prog(t, 1.0, 0.3)
        box(c, 140, 1285, 260, 110, p)                          # banco atrás
        j = squat(c, 470, 1450, 0.62, dep, {"quad": 0.9, "gluteo": 0.6}, t, p)
        k = ease(prog(t, 0.8, 0.4))
        pain_marks(c, j["quad"][0], j["quad"][1], t, k, p)
        chip(c, "DÓI PRA SENTAR", 690, 860, PINK, NAVY, 50, ease_out(prog(t, 0.9, 0.3)))


def se_dia2(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.15, d * 0.7))
        pain_chart(c, t, LEFT + 60, 860, RIGHT - LEFT - 120, 460, g, p)
        chip(c, "PICO: 1 A 3 DIAS", CX, 1480, PINK, NAVY, 46, ease_out(prog(t, 0.55 * d, 0.3)))


def se_descida(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        ph = (t * 0.55) % 1                                 # desce devagar (70%), sobe rápido (30%)
        dep = ease(ph / 0.7) if ph < 0.7 else 1 - ease((ph - 0.7) / 0.3)
        j = squat(c, 300, 1480, 0.5, 0.9 * dep, {"quad": 0.4 + 0.5 * (ph < 0.7)}, t, p)
        mono(c, "DESCENDO: O MÚSCULO FREIA", 600, 830, 26, PINK, ease_out(prog(t, 0.2, 0.3)), align="center")
        g = ease(prog(t, 0.4, d * 0.6))
        fiber(c, 560, 1050, 360, 150, p, tears=g, t=t)
        mono(c, "FIBRA", 560, 1170, 24, MUTED, p)
        chip(c, "PEQUENAS LESÕES", 680, 1300, PINK, NAVY, 40, ease_out(prog(t, 0.6 * d, 0.3)))


def se_nervo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        fiber(c, LEFT + 30, 1320, RIGHT - LEFT - 60, 170, p, tears=1.0, t=t)
        rnd = random.Random(5)
        for i in range(14):                                 # inflamação: células de conserto chegando
            f = (t * 0.4 + rnd.random()) % 1
            disk(c, LEFT + 60 + rnd.random() * (RIGHT - LEFT - 120), 1320 + rnd.uniform(-60, 60), 10 + 6 * g, ORANGE, p * g * (0.5 + 0.5 * f))
        mono(c, "INFLAMAÇÃO PRA CONSERTAR", LEFT + 30, 1460, 26, ORANGE, ease_out(prog(t, 0.25 * d, 0.3)))
        nerve(c, CX, 1240, CX, 900, t, ease_out(prog(t, 0.4 * d, 0.4)))
        brain(c, CX, 820, 0.55, glow=0.6 * g)
        chip(c, "NERVO SENSÍVEL", 690, 1080, PINK, NAVY, 44, ease_out(prog(t, 0.55 * d, 0.3)))


# ================================================================ VEIAS (ve_)
def _arm_veins(c, t, k, p, x=120, y=1100, s=1.3):
    pts = [(x + 70 * s, y + 38 * s), (x + 150 * s, y + 30 * s), (x + 210 * s, y + 44 * s), (x + 280 * s, y + 34 * s), (x + 320 * s, y + 42 * s)]
    poly(c, pts, CYAN, 6 + 12 * k, p)
    poly(c, pts, (0.10, 0.45, 0.55), 2 + 6 * k, p)
    poly(c, [(x + 150 * s, y + 30 * s), (x + 190 * s, y + 6 * s), (x + 250 * s, y + 0 * s)], CYAN, 4 + 8 * k, p * 0.9)


def ve_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.2, 1.2))
        bend = 0.5 + 0.5 * math.sin(t * 3)
        arm(c, 120, 1100, 1.3, 0.2 + 0.45 * bend, p, 0.5 + 0.4 * k, t)
        _arm_veins(c, t, k * (0.8 + 0.2 * bend), p)
        chip(c, "VEIAS SALTANDO", 640, 860, CYAN, NAVY, 48, ease_out(prog(t, 0.7, 0.3)))


def ve_sangue(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        bpm = lerp(75, 150, g)
        heart(c, LEFT + 170, 960, 2.0, t, bpm, p)
        mono(c, "FLUXO NO MÚSCULO", LEFT + 380, 880, 26, MUTED, p)
        mono(c, "REPOUSO", LEFT + 380, 960, 24, MUTED, p)
        bar_pct(c, LEFT + 380, 980, 400, 40, 0.15, CYAN, p)
        mono(c, "TREINO", LEFT + 380, 1080, 24, PINK, p)
        bar_pct(c, LEFT + 380, 1100, 400, 40, lerp(0.15, 1.0, g), PINK, p)
        for i in range(10):                                 # sangue correndo
            f = (t * lerp(0.4, 1.4, g) + i / 10) % 1
            ellipse(c, lerp(LEFT + 40, RIGHT - 40, f), 1330 + (i % 3 - 1) * 14, 15, 10, 0, RED, p)
        cap_line(c, LEFT + 20, 1290, RIGHT - 20, 1290, PINK, 5, p); cap_line(c, LEFT + 20, 1370, RIGHT - 20, 1370, PINK, 5, p)
        chip(c, "MUITO MAIS SANGUE", CX, 1480, PINK, NAVY, 44, ease_out(prog(t, 0.5 * d, 0.3)))


def ve_volta(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        mx = CX
        panel(c, mx - 170, 900, 340, 300, p)
        mono(c, "MÚSCULO", mx, 1170, 24, MUTED, p, align="center")
        cap_line(c, LEFT + 10, 980, mx - 170, 980, PINK, 34, p); cap_line(c, LEFT + 10, 980, mx - 170, 980, NAVY, 18, p)
        vw = lerp(26, 70, g)
        cap_line(c, mx + 170, 1120, RIGHT - 10, 1120, CYAN, vw, p); cap_line(c, mx + 170, 1120, RIGHT - 10, 1120, (0.10, 0.40, 0.50), vw * 0.65, p)
        for k in range(7):
            f = (t * 1.1 + k / 7) % 1
            disk(c, lerp(LEFT + 10, mx - 170, f), 980, 8, INK, p)
        for k in range(int(4 + 8 * g)):
            f = (t * 0.5 + k / (4 + 8 * g)) % 1
            disk(c, lerp(mx + 170, RIGHT - 10, f), 1120 + ((k % 3) - 1) * vw * 0.2, 8, INK, p)
        mono(c, "ARTÉRIA · CHEGA", LEFT + 10, 920, 24, PINK, p)
        _mono_right(c, "VEIA · VOLTA", RIGHT - 10, 1220, 24, CYAN, p)
        chip(c, "A VEIA ENCHE E ESTUFA", CX, 1400, CYAN, NAVY, 44, ease_out(prog(t, 0.5 * d, 0.3)))


def ve_gordura(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p1 = ease_out(prog(t, 0, 0.3)); p2 = ease_out(prog(t, 0.35 * d, 0.35))
        skin_section(c, t, LEFT + 10, 1000, 380, 150, 26, p1, "MAIS GORDURA")
        skin_section(c, t, RIGHT - 390, 1000, 380, 30, 30, p2, "MENOS GORDURA")
        chip(c, "VEIA PERTO DA PELE", CX, 1480, CYAN, NAVY, 44, ease_out(prog(t, 0.6 * d, 0.3)))


# ================================================================ FORMIGAMENTO (fr_)
def fr_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.3, 1.0))
        face(c, CX - 120, 1100, 200, 0.15, t, p)
        itch_marks(c, CX - 120, 1100, t, k, p, n=10, r=230)
        scoop(c, 740, 1340, 0.9, ease_out(prog(t, 0.2, 0.3)))
        chip(c, "FORMIGANDO", 700, 860, PINK, NAVY, 50, ease_out(prog(t, 0.8, 0.3)))


def fr_beta(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        scoop(c, 300, 1250, 1.2, p)
        for i in range(8):                                   # pó subindo do medidor e virando molécula
            f = (t * 0.6 + i / 8) % 1
            disk(c, 300 + 40 * math.sin(i * 2.1 + f * 4), 1220 - 200 * f, 7, POWDER, p * (1 - f))
        g = back_out(prog(t, 0.4, 0.4))
        molecule(c, 680, 1080, 1.6 * max(g, 0.001), ease_out(prog(t, 0.4, 0.3)))
        chip(c, "BETA-ALANINA", 680, 1300, POWDER, NAVY, 50, ease_out(prog(t, 0.5 * d, 0.3)))


def fr_nervo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.3, d * 0.5))
        rnd = random.Random(9)
        for i in range(6):                                   # moléculas descendo até os sensores
            f = clamp(g * 1.2 - i * 0.05)
            nx = LEFT + 140 + i * (RIGHT - LEFT - 280) / 5
            molecule(c, nx, lerp(840, 1000, f), 0.45, p * (1 - 0.5 * f))
        skin_nerves(c, t, LEFT + 30, 1040, RIGHT - LEFT - 60, g, p)
        mono(c, "SENSORES DE COCEIRA DA PELE", LEFT + 30, 1330, 26, MUTED, p)
        chip(c, "PINICA", CX, 1440, PINK, NAVY, 54, ease_out(prog(t, 0.55 * d, 0.3)))


def fr_dose(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.15, d * 0.5))
        scoop(c, LEFT + 140, 980, 0.6, p, 0.5)
        scoop(c, LEFT + 140, 1180, 0.9, p, 1.0)
        mono(c, "FORMIGA", LEFT + 330, 900, 24, MUTED, p)
        bar_pct(c, LEFT + 330, 950, 440, 46, 0.3 * g, PINK, p)
        bar_pct(c, LEFT + 330, 1150, 440, 46, 0.95 * g, PINK, p)
        fr = ease(prog(t, 0.5 * d, 0.45 * d))
        clock(c, CX, 1420, 90, fr, p)
        _mono_right(c, "~1 HORA", CX - 120, 1430, 30, CYAN, ease_out(prog(t, 0.5 * d, 0.3)))
        chip(c, "PASSA", CX + 200, 1420, CYAN, NAVY, 44, ease_out(prog(t, 0.8 * d, 0.3)))


# ================================================================ ESCADA (es_)
def es_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        sw, sh = 120, 72
        stairs(c, 120, 1540, 6, sw, sh, p)
        j = climber(c, t, 120, 1540, sw, sh, 0.72, p, 1.1)
        wave_lines(c, j["head"][0] + 80, j["head"][1] + 10, t, p * ease(prog(t, 0.5, 0.5)), PINK, 3, 90)
        chip(c, "SEM FÔLEGO", 760, 1470, PINK, NAVY, 50, ease_out(prog(t, 0.8, 0.3)))


def es_especifico(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        pa = ease_out(prog(t, 0, 0.3)); pb = ease_out(prog(t, 0.3 * d, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        panel(c, LEFT + 10, 820, 400, 560, pa)
        barbell_line(c, LEFT + 210, 1050, 0.55)
        mono(c, "FORÇA", LEFT + 210, 960, 30, INK, pa, align="center")
        bar_pct(c, LEFT + 50, 1250, 320, 44, 0.9 * g, GOOD, pa)
        panel(c, RIGHT - 410, 820, 400, 560, pb)
        lungs(c, RIGHT - 210, 1110, 0.45, pb, 0.3, t)
        mono(c, "FÔLEGO", RIGHT - 210, 960, 30, INK, pb, align="center")
        bar_pct(c, RIGHT - 370, 1250, 320, 44, 0.3 * g, PINK, pb)
        chip(c, "MELHORA NO QUE TREINA", CX, 1470, CYAN, NAVY, 42, ease_out(prog(t, 0.55 * d, 0.3)))


def es_usinas(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        fiber(c, LEFT + 30, 1080, RIGHT - LEFT - 60, 300, p, t=t)
        rnd = random.Random(2)
        n = 14
        for i in range(n):
            q = back_out(prog(g, i / n * 0.85, 0.15))
            mito_cell(c, LEFT + 110 + rnd.random() * (RIGHT - LEFT - 220), 1080 + rnd.uniform(-90, 90), 26 * max(q, 0.001), p * min(1, q * 3), t)
        mono(c, "MITOCÔNDRIAS = USINAS DE ENERGIA", LEFT + 30, 1300, 26, MITO, p)
        chip(c, "MAIS USINAS", CX, 1440, MITO, NAVY, 50, ease_out(prog(t, 0.5 * d, 0.3)))


def es_cardio(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        treadmill(c, 90, 520, 1450, t, p)
        runner(c, 290, 1270, 0.75, t, p, 6.5)
        k = heart(c, 760, 960, lerp(1.4, 1.9, g), t, 110, p)
        mono(c, "SANGUE POR BATIDA", 760, 1110, 24, MUTED, p, align="center")
        bar_pct(c, 590, 1140, 340, 40, lerp(0.4, 0.95, g), PINK, p)
        chip(c, "O CARDIO CRIA", 760, 1300, CYAN, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


VIS = dict(se_hook=se_hook, se_dia2=se_dia2, se_descida=se_descida, se_nervo=se_nervo,
           ve_hook=ve_hook, ve_sangue=ve_sangue, ve_volta=ve_volta, ve_gordura=ve_gordura,
           fr_hook=fr_hook, fr_beta=fr_beta, fr_nervo=fr_nervo, fr_dose=fr_dose,
           es_hook=es_hook, es_especifico=es_especifico, es_usinas=es_usinas, es_cardio=es_cardio)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
PRE = {"fibra_26_sentar": "se_", "fibra_27_veias": "ve_", "fibra_28_formiga": "fr_", "fibra_29_escada": "es_"}
for chave, pre in PRE.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
