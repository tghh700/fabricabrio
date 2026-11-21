"""FIBRA — produção 22/11 (prancha técnica, build3): barra fixa difícil (ba_), alongar não evita dor (al_),
leg press parece leve (lp_), mais forte na descida (de_). Uma figura por cena; nada atravessa o corpo;
só glifos da fonte (marcas desenhadas)."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam, rgb
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA, squat, arm, leg_calf
from scenes_fibra_g import bar_pct, ok_mark, no_mark, pullup, _pull, BX0, BX1, BARY
from scenes_fibra_1911 import CX, CY, RED, ORANGE
import pauta_2211 as PA


# ------------------------------------------------------------------ peças
def arrow_v(c, x, y1, y2, col, w=8, p=1.0, head=26):
    if p <= 0:
        return
    y2_ = lerp(y1, y2, p)
    cap_line(c, x, y1, x, y2_, col, w)
    sgn = 1 if y2 > y1 else -1
    poly(c, [(x - head * 0.7, y2_ - sgn * head), (x, y2_), (x + head * 0.7, y2_ - sgn * head)], col, w)


def weight_tag(c, x, y, txt, col=PINK, p=1.0, size=40):
    chip(c, txt, x, y, col, NAVY, size, p)


def hbar(c, x, y, w, frac, lab, col, p=1.0, val=None):
    mono(c, lab, x, y - 16, 26, MUTED, p)
    rrect(c, x, y, w, 40, 20, NAVY2, p)
    rrect(c, x, y, max(1, w * clamp(frac) * p), 40, 20, col, p)
    if val:
        _mono_right(c, val, x + w, y - 16, 26, col, p)


# ================================================================ BARRA (ba_)
def ba_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        # sobe até a metade, trava e volta: esforço sem chegar
        ph = (t * 0.7) % 1
        pull = 0.62 * (ease(ph / 0.55) if ph < 0.55 else 1 - ease((ph - 0.55) / 0.45)) + 0.02 * math.sin(t * 30) * (ph > 0.4)
        j = pullup(c, t, pull, {"dorsal": 0.7, "biceps": 0.8}, p)
        chip(c, "TÃO DIFÍCIL?", CX, 1500, PINK, NAVY, 50, ease_out(prog(t, 0.6, 0.3)))


def ba_corpo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        j = pullup(c, t, _pull(t, 1.6), {"dorsal": 0.5, "biceps": 0.5}, p)
        g = ease_out(prog(t, 0.3, 0.6))
        cx = j["cx"]
        arrow_v(c, RIGHT - 10, 1040, 1320, PINK, 8, g)
        _mono_right(c, "SEU PESO", RIGHT + 10, 1370, 26, PINK, g)
        weight_tag(c, CX, 1500, "PESA 80 KG? SOBE UNS 75", PINK, ease_out(prog(t, 0.45 * d, 0.3)), 40)


def ba_quilo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        panel(c, LEFT + 10, 720, RIGHT - LEFT - 20, 620, p)
        mono(c, "MESMA FORÇA DE PUXADA", LEFT + 50, 790, 28, CYAN, p)
        rows = (("PESO 65 KG · SOBE FÁCIL", 0.65, CYAN), ("PESO 80 KG · NO LIMITE", 0.8, ORANGE), ("PESO 95 KG · NÃO SOBE", 0.95, PINK))
        for i, (lab, v, col) in enumerate(rows):
            q = ease_out(prog(t, 0.2 + i * 0.45, 0.35))
            y = 900 + i * 150
            hbar(c, LEFT + 50, y, RIGHT - LEFT - 100, v, lab, col, q)
        # linha da força (igual para todos)
        fx = LEFT + 50 + (RIGHT - LEFT - 100) * 0.82
        dline(c, fx, 860, fx, 1320, INK, 3, (8, 8), ease_out(prog(t, 0.3, 0.3)))
        mono(c, "SUA FORÇA", fx - 80, 1300, 22, INK, ease_out(prog(t, 0.3, 0.3)))
        chip(c, "FORÇA ÷ PESO", CX, 1460, PINK, NAVY, 46, ease_out(prog(t, 0.55 * d, 0.3)))


def ba_braco(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        c.save(); c.translate(530, 740); c.scale(0.8, 0.8); c.translate(-530, -740)
        j = pullup(c, t, _pull(t, 1.8), {"dorsal": 1.0, "biceps": 1.0}, p)
        c.restore()
        q = ease_out(prog(t, 0.35 * d, 0.35))
        y = 1460
        mono(c, "MASSA MUSCULAR", LEFT + 20, y - 70, 24, MUTED, q)
        hbar(c, LEFT + 20, y - 30, 380, 0.42, "COSTAS + BÍCEPS", PINK, q)
        hbar(c, LEFT + 440, y - 30, 380, 1.0, "PERNAS", CYAN, q)


# ================================================================ ALONGAR (al_)
def hamstring_stretch(c, t, x, y, s, k, p=1.0, hl=0.0):
    """perna estendida no banco (vista de lado) e o tronco inclinando para alongar; k 0..1 = quanto inclina"""
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -40, 0, 560, 40, 14, LINE, p)                      # banco
    cap_line(c, 0, 40, 0, 200, LINE, 14, p); cap_line(c, 480, 40, 480, 200, LINE, 14, p)
    hip = (40, -40); knee = (260, -40); ank = (470, -40)
    ellipse(c, 150, -70, 115, 36, 0, mix(NAVY2, PINK, hl), p, CYAN)   # posterior da coxa
    for a_, b_ in ((hip, knee), (knee, ank)):
        cap_line(c, a_[0], a_[1], b_[0], b_[1], INK, 6, p)
    capsule_foot = (ank[0] + 10, -110)
    cap_line(c, ank[0], ank[1], capsule_foot[0], capsule_foot[1], INK, 6, p)
    ang = math.radians(lerp(80, 35, ease(k)))                    # tronco: de vertical para inclinado à frente
    sho = (hip[0] + math.cos(ang) * 300, hip[1] - math.sin(ang) * 300)
    cap_line(c, hip[0], hip[1], sho[0], sho[1], INK, 6, p)
    for j in (hip, knee, ank, sho):
        disk(c, j[0], j[1], 10, INK, p)
    hx, hy = sho[0] + math.cos(ang) * 80, sho[1] - math.sin(ang) * 80
    c.new_path(); c.arc(hx, hy, 50, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    # braço alcançando a canela
    hand = (lerp(sho[0] + 120, knee[0] + 120, ease(k)), lerp(sho[1] + 140, -70, ease(k)))
    cap_line(c, sho[0], sho[1], hand[0], hand[1], INK, 6, p)
    c.restore()


def al_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = 0.5 + 0.5 * math.sin(t * 1.6)
        hamstring_stretch(c, t, LEFT + 80, 1260, 1.25, k, p, 0.5 * k)
        chip(c, "SEM DOR AMANHÃ?", CX, 1480, PINK, NAVY, 48, ease_out(prog(t, 0.6, 0.3)))


def al_estudo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        mono(c, "12 ESTUDOS · DOR DEPOIS DO TREINO", LEFT + 20, 760, 26, CYAN, p)
        for i in range(12):
            q = back_out(prog(t, 0.1 + i * 0.09, 0.25))
            if q <= 0:
                continue
            col_ = i % 4; row = i // 4
            x = LEFT + 30 + col_ * 210; y = 800 + row * 170
            panel(c, x, y, 180, 140, min(q, 1))
            h1 = 70 + 8 * math.sin(i * 1.7); h2 = h1 - 3
            rrect(c, x + 40, y + 120 - h1, 40, h1, 8, MUTED, min(q, 1))
            rrect(c, x + 100, y + 120 - h2, 40, h2, 8, CYAN, min(q, 1))
        q = ease_out(prog(t, 0.55 * d, 0.3))
        mono(c, "SEM ALONGAR", LEFT + 30, 1340, 22, MUTED, q); mono(c, "ALONGANDO", LEFT + 260, 1340, 22, CYAN, q)
        chip(c, "1 A 4 PONTOS EM 100", CX, 1460, PINK, NAVY, 46, q)


def al_fibra(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        fiber(c, LEFT + 30, 1000, RIGHT - LEFT - 60, 180, p, tears=1.0, t=t)
        mono(c, "FIBRA COM PEQUENAS LESÕES", LEFT + 30, 870, 26, PINK, p)
        rnd = random.Random(5)
        for i in range(14):
            f = (t * 0.4 + rnd.random()) % 1
            disk(c, LEFT + 60 + rnd.random() * (RIGHT - LEFT - 120), 1000 + rnd.uniform(-60, 60), 10 + 6 * g, ORANGE, p * g * (0.5 + 0.5 * f))
        mono(c, "CONSERTO EM ANDAMENTO", LEFT + 30, 1150, 26, ORANGE, ease_out(prog(t, 0.3 * d, 0.3)))
        # puxar a fibra (alongar) não muda nada: setas de esticar e X
        q = ease_out(prog(t, 0.5 * d, 0.3))
        stretch = 18 * math.sin(t * 3) * q
        cap_line(c, LEFT + 20 - stretch, 1260, LEFT + 200 - stretch, 1260, CYAN, 6, q)
        cap_line(c, RIGHT - 200 + stretch, 1260, RIGHT - 20 + stretch, 1260, CYAN, 6, q)
        mono(c, "ESTICAR", CX - 70, 1270, 26, CYAN, q)
        no_mark(c, CX, 1400, 40, ease_out(prog(t, 0.65 * d, 0.3)))


def al_serve(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = 0.5 + 0.5 * math.sin(t * 1.4)
        hamstring_stretch(c, t, LEFT + 120, 1050, 0.95, k, p, 0.3)
        g = ease(prog(t, 0.25, d * 0.5))
        q = ease_out(prog(t, 0.2, 0.3))
        hbar(c, LEFT + 20, 1300, 560, lerp(0.3, 0.85, g), "FLEXIBILIDADE", GOOD, q)
        ok_mark(c, RIGHT - 120, 1320, 34, ease_out(prog(t, 0.45 * d, 0.3)), GOOD)
        q2 = ease_out(prog(t, 0.4 * d, 0.3))
        hbar(c, LEFT + 20, 1440, 560, 0.7, "DOR NO DIA SEGUINTE", PINK, q2)
        no_mark(c, RIGHT - 120, 1460, 34, ease_out(prog(t, 0.6 * d, 0.3)))


# ================================================================ LEG PRESS (lp_)
def sled(c, t, x0, y0, L, u, p=1.0, plates=3):
    """trilho a 45° (de baixo-esquerda para cima-direita); u 0..1 posição do trenó"""
    a = math.radians(45)
    x1, y1 = x0 + L * math.cos(a), y0 - L * math.sin(a)
    cap_line(c, x0, y0, x1, y1, LINE, 16, p)
    cap_line(c, x0, y0 + 20, x1 + 20, y1 + 20, LINE, 4, p)
    sx, sy = lerp(x0 + 80, x1 - 140, u) , lerp(y0 - 80, y1 + 140, u)
    c.save(); c.translate(sx, sy); c.rotate(-a)
    rrect(c, -90, -70, 180, 60, 12, NAVY2, p); rrect(c, -90, -70, 180, 60, 12); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    for k in range(plates):
        rrect(c, -60 + k * 34, -150, 26, 80, 6, MUTED, p)
    c.restore()
    return sx, sy


def lp_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = 0.45 + 0.4 * (0.5 - 0.5 * math.cos(t * 2.4))
        squat(c, LEFT + 290, 1420, 0.62, dep, {"quad": 0.6, "gluteo": 0.5}, t, p)
        q = ease_out(prog(t, 0.3, 0.3))
        hbar(c, LEFT + 470, 900, 360, 0.5, "AGACHAMENTO", CYAN, q, "100 KG")
        q2 = ease_out(prog(t, 0.6, 0.3))
        hbar(c, LEFT + 470, 1060, 360, 1.0, "LEG PRESS", PINK, q2, "200 KG")
        chip(c, "POR QUÊ?", LEFT + 650, 1220, PINK, NAVY, 46, ease_out(prog(t, 0.9, 0.3)))


def lp_rampa(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        u = 0.35 + 0.25 * math.sin(t * 1.5)
        sx, sy = sled(c, t, LEFT + 60, 1460, 700, u, p)
        g = ease_out(prog(t, 0.35, 0.5))
        # peso das anilhas (vertical) e a parte que empurra contra a perna (ao longo do trilho)
        arrow_v(c, sx + 150, sy - 40, sy + 200, MUTED, 7, g)
        mono(c, "PESO TOTAL", sx + 170, sy + 160, 24, MUTED, g)
        a = math.radians(45); L = 180 * g
        if g > 0:
            ex, ey = sx - 40 - L * math.cos(a), sy + 40 + L * math.sin(a)
            cap_line(c, sx - 40, sy + 40, ex, ey, PINK, 9)
            poly(c, [(ex + 30, ey - 4), (ex, ey), (ex + 4, ey - 30)], PINK, 9)
        mono(c, "CONTRA A PERNA", sx - 117, sy + 207, 24, PINK, g)
        chip(c, "SÓ PARTE DO PESO", CX + 120, 820, PINK, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


def lp_tronco(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = 0.5 - 0.5 * math.cos(t * 2.0)
        j = squat(c, LEFT + 320, 1440, 0.7, 0.85 * dep, {"quad": 0.8, "gluteo": 0.6, "core": 0.9}, t, p)
        q = ease_out(prog(t, 0.35, 0.4))
        callout(c, j["sho"][0] + 20, (j["sho"][1] + j["hip"][1]) / 2, RIGHT - 280, 880, "+ SEU TRONCO", q, PINK, 40)
        chip(c, "A PERNA LEVANTA TUDO ISSO", CX, 1520, PINK, NAVY, 40, ease_out(prog(t, 0.55 * d, 0.3)))


def lp_equil(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        wob = 0.05 * math.sin(t * 5)
        dep = 0.6
        c.save(); c.translate(LEFT + 320, 1440); c.rotate(wob); c.translate(-(LEFT + 320), -1440)
        j = squat(c, LEFT + 320, 1440, 0.7, dep, {"core": 1.0}, t, p)
        c.restore()
        for k in range(3):                                      # marcas de equilíbrio
            a = 0.6 + 0.4 * abs(math.sin(t * 5 + k))
            c.new_path(); c.arc(LEFT + 320, 1440, 520 + k * 30, -2.0, -1.2); rgb(c, CYAN, 0.35 * a * p); c.set_line_width(3); c.stroke()
        q = ease_out(prog(t, 0.3, 0.3))
        mono(c, "AGACHAMENTO:", RIGHT - 330, 880, 26, CYAN, q)
        mono(c, "CORE SEGURA", RIGHT - 330, 920, 26, INK, q)
        q2 = ease_out(prog(t, 0.45 * d, 0.3))
        mono(c, "LEG PRESS:", RIGHT - 330, 1040, 26, PINK, q2)
        mono(c, "COSTAS APOIADAS", RIGHT - 330, 1080, 26, INK, q2)
        chip(c, "SEM EQUILIBRAR", CX, 1520, PINK, NAVY, 44, ease_out(prog(t, 0.6 * d, 0.3)))


# ================================================================ DESCIDA (de_)
def _dumbbell_at(c, x, y, s, p):
    rrect(c, x - 60 * s, y - 14 * s, 120 * s, 28 * s, 10 * s, MUTED, p)
    for sd in (-1, 1):
        rrect(c, x + sd * 60 * s - 20 * s, y - 50 * s, 40 * s, 100 * s, 10 * s, INK, p)


def _arm_hand(x, y, s, bend):
    ang = math.radians(lerp(10, 125, ease(bend)))
    ex, ey = x + 330 * s, y + 40 * s
    return ex + 300 * s * math.cos(-ang), ey + 300 * s * math.sin(-ang)


def curl_arm(c, t, x, y, s, bend, p, hl=1.0):
    arm(c, x, y, s, bend, p, hl, t)
    hx, hy = _arm_hand(x, y, s, bend)
    _dumbbell_at(c, hx, hy, s * 0.9, p)
    return hx, hy


def de_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        ph = (t * 0.5) % 1                                      # sobe rápido e trava; desce controlado
        bend = 0.9 * (1 - ease(ph / 0.7)) if ph < 0.7 else 0.9 * ease((ph - 0.7) / 0.3)
        curl_arm(c, t, LEFT + 40, 1020, 1.05, bend, p)
        q = ease_out(prog(t, 0.4, 0.3))
        hbar(c, LEFT + 40, 1400, 360, 0.6, "SUBIDA", CYAN, q)
        hbar(c, LEFT + 460, 1400, 360, 0.85, "DESCIDA", PINK, q)


def de_freia(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        ph = (t * 0.4) % 1
        bend = 0.9 * (1 - ease(ph / 0.8)) if ph < 0.8 else 0.9 * ease((ph - 0.8) / 0.2)
        hx, hy = curl_arm(c, t, LEFT + 40, 1000, 1.0, bend, p, 0.6 + 0.4 * (ph < 0.8))
        q = ease_out(prog(t, 0.3, 0.3))
        if ph < 0.8:
            arrow_v(c, RIGHT - 40, 880, 1200, PINK, 8, q)
            _mono_right(c, "PESO PUXA", RIGHT, 1250, 24, PINK, q)
        chip(c, "O MÚSCULO FREIA", CX, 1420, PINK, NAVY, 48, ease_out(prog(t, 0.4 * d, 0.3)))


def sarcomere(c, t, x, y, w, stretch, p=1.0, grip=1.0):
    """miofibrila: filamentos finos (ciano) presos nas linhas Z, grossos (rosa) no meio com 'pontes'; titina em mola"""
    half = w / 2 * (0.78 + 0.22 * stretch)
    for sd in (-1, 1):
        zx = x + sd * half
        cap_line(c, zx, y - 150, zx, y + 150, INK, 6, p)                # linha Z
        for r in (-90, 0, 90):
            cap_line(c, zx, y + r + 30 * (1 if r >= 0 else -1) * 0, x + sd * 40, y + r, CYAN, 8, p)  # filamento fino
        # titina: mola em zigue-zague da linha Z até o meio
        pts = []
        n = 10
        for k in range(n + 1):
            f = k / n
            px = lerp(zx, x + sd * 30, f)
            py = y + 135 + (12 if k % 2 else -12) * (1.2 - 0.8 * stretch)
            pts.append((px, py))
        poly(c, pts, ORANGE, 4, p)
    for r in (-45, 45):
        cap_line(c, x - 150, y + r, x + 150, y + r, PINK, 16, p)        # filamento grosso
        for k in range(-3, 4):                                          # pontes
            bx = x + k * 40
            sgn = -1 if r < 0 else 1
            cap_line(c, bx, y + r + sgn * 6, bx - 10 * math.copysign(1, k or 1) * (1 + stretch), y + r + sgn * 36, PINK, 5, p * grip)


def de_pontes(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        st = 0.5 + 0.5 * math.sin(t * 1.4)
        panel(c, LEFT + 10, 760, RIGHT - LEFT - 20, 520, p)
        sarcomere(c, t, CX, 1010, 640, st, p, ease_out(prog(t, 0.3, 0.4)))
        q = ease_out(prog(t, 0.35 * d, 0.3))
        mono(c, "PONTES SEGURAM", LEFT + 40, 820, 26, PINK, ease_out(prog(t, 0.2, 0.3)))
        mono(c, "TITINA = MOLA", LEFT + 40, 1250, 26, ORANGE, q)
        chip(c, "ESTICADA, SEGURA MAIS", CX, 1420, PINK, NAVY, 44, ease_out(prog(t, 0.6 * d, 0.3)))


def de_terco(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.5))
        base = 1240
        for i, (lab, v, col) in enumerate((("SUBIDA", 0.66, CYAN), ("DESCIDA", 0.88, PINK))):
            x = LEFT + 140 + i * 360
            h = 420 * v * g
            rrect(c, x, base - 420, 200, 420, 24, NAVY2, p)
            rrect(c, x, base - h, 200, h, 24, col, p)
            mono(c, lab, x + 100, base + 50, 30, col, p, align="center")
        q = ease_out(prog(t, 0.5 * d, 0.3))
        if q > 0:
            dline(c, LEFT + 140, base - 420 * 0.66, LEFT + 700, base - 420 * 0.66, INK, 3, (8, 8), q)
        chip(c, "≈ 1/3 A MAIS", CX, 1430, PINK, NAVY, 50, q)


VIS = dict(ba_hook=ba_hook, ba_corpo=ba_corpo, ba_quilo=ba_quilo, ba_braco=ba_braco,
           al_hook=al_hook, al_estudo=al_estudo, al_fibra=al_fibra, al_serve=al_serve,
           lp_hook=lp_hook, lp_rampa=lp_rampa, lp_tronco=lp_tronco, lp_equil=lp_equil,
           de_hook=de_hook, de_freia=de_freia, de_pontes=de_pontes, de_terco=de_terco)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
PRE = {"fibra_30_barra": "ba_", "fibra_31_alonga": "al_", "fibra_32_legpress": "lp_", "fibra_33_descida": "de_"}
for chave, pre in PRE.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
