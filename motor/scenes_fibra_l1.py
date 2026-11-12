"""FIBRA — lote extra 12/11: pump, tremor, adaptação neural, músculos do agachamento."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right

CY = 1060


# ----------------------------------------------------------------- helpers
def ellipse(c, x, y, rx, ry, ang, col, a=1.0, stroke=None):
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(max(rx, 0.1), max(ry, 0.1))
    c.new_path(); c.arc(0, 0, 1, 0, 2 * math.pi); c.restore()
    rgb(c, col, a); c.fill_preserve() if stroke else c.fill()
    if stroke:
        rgb(c, stroke, a); c.set_line_width(2.5); c.stroke()


def capsule(c, x1, y1, x2, y2, w, a=1.0):
    cap_line(c, x1, y1, x2, y2, CYAN, w + 6, a)
    cap_line(c, x1, y1, x2, y2, NAVY2, w, a)


def panel(c, x, y, w, h, p=1.0, col=LINE):
    rrect(c, x, y, w, h, 16, NAVY2, p); rrect(c, x, y, w, h, 16); rgb(c, col, p); c.set_line_width(3); c.stroke()


def wave(c, x, y, w, amp, t, p, irregular=0.0, col=CYAN, seed=1):
    """traço tipo eletromiografia; irregular 0 = senoide lisa, 1 = liga/desliga desencontrado"""
    rnd = random.Random(seed + int(t * 12))
    pts = []
    n = 90
    for i in range(int(n * clamp(p)) + 1):
        f = i / n
        xx = x + w * f
        base = math.sin(f * 22 + t * 7) * amp
        jit = (rnd.uniform(-1, 1) * amp * 1.3) * irregular
        if irregular > 0 and rnd.random() < 0.18 * irregular:
            jit *= 0.1  # buracos de sinal (unidade desligando)
        pts.append((xx, y + base * (1 - 0.6 * irregular) + jit))
    if len(pts) > 1:
        poly(c, pts, col, 4)


def cta_factory(word):
    def cta(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=CY):
            p = ease_out(prog(t, 0, 0.35))
            fibra_icon(c, W / 2 - 40, 790, 2.2 * back_out(p) if p > 0 else 0.01, 1.0, t, pulse=True)
            chip(c, "COMENTA  " + word, W / 2 - 40, 1010, PINK, NAVY, 64, ease_out(prog(t, 0.15, 0.35)))
            q = ease_out(prog(t, 0.35 * d, 0.4))
            mono(c, "REGISTRE E ACOMPANHE SEUS", W / 2 - 40, 1150, 32, INK, q, align="center")
            mono(c, "TREINOS GRATUITAMENTE", W / 2 - 40, 1196, 32, INK, q, align="center")
            chip(c, "LINK NA BIO", W / 2 - 40, 1310, CYAN, NAVY, 56, ease_out(prog(t, 0.55 * d, 0.35)))
    return cta


SFX_CTA = [(0.0, "whoosh"), ("0.15", "pop"), ("0.55d", "ding")]


# ----------------------------------------------------------------- PUMP
def vessel(c, x, y, w, t, p, squeeze=0.0):
    """artéria chegando (esquerda) -> músculo (centro) -> veia saindo (direita), veia apertada pela contração"""
    mx = x + w * 0.5
    panel(c, mx - 200, y - 150, 400, 300, p)
    mono(c, "MÚSCULO", mx, y + 125, 26, MUTED, p, align="center")
    # artéria
    cap_line(c, x, y - 40, mx - 200, y - 40, PINK, 34, p); cap_line(c, x, y - 40, mx - 200, y - 40, NAVY, 18, p)
    # veia (afina com o aperto)
    vw = lerp(34, 12, squeeze)
    cap_line(c, mx + 200, y + 40, x + w, y + 40, CYAN, vw, p); cap_line(c, mx + 200, y + 40, x + w, y + 40, NAVY, vw * 0.5, p)
    # fluxo: entra rápido, sai devagar
    for k in range(6):
        f = (t * 0.9 + k / 6) % 1
        disk(c, lerp(x, mx - 200, f), y - 40, 8, INK, p)
    slow = lerp(0.9, 0.25, squeeze)
    for k in range(4):
        f = (t * slow + k / 4) % 1
        disk(c, lerp(mx + 200, x + w, f), y + 40, 6, INK, p)
    # gotas acumulando dentro
    n = int(18 * squeeze)
    rnd = random.Random(4)
    for k in range(n):
        disk(c, mx + rnd.uniform(-160, 160), y + rnd.uniform(-110, 90), 10, CYAN, 0.7 * p)
    # "pinça" da contração sobre a veia
    if squeeze > 0.05:
        cx = mx + 330
        cap_line(c, cx - 34, y + 40 - 60 + 30 * squeeze, cx + 34, y + 40 - 60 + 30 * squeeze, PINK, 8, p)
        cap_line(c, cx - 34, y + 40 + 60 - 30 * squeeze, cx + 34, y + 40 + 60 - 30 * squeeze, PINK, 8, p)


def p_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        pump = 0.5 + 0.5 * math.sin(t * 6)
        arm(c, 140, 1080, 1.35, 0.9 + 0.1 * pump, ease_out(prog(t, 0, 0.3)), 0.7 + 0.3 * pump, t)
        callout(c, 520, 880, 720, 740, "PUMP", ease_out(prog(t, 0.35, 0.5)), PINK, 40)
        if prog(t, 0.55 * d, 0.2) > 0:
            chip(c, "NÃO É MÚSCULO NOVO", W / 2 - 40, 1380, PINK, NAVY, 48, ease_out(prog(t, 0.55 * d, 0.3)))


def p_veia(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        sq = ease(prog(t, 0.25 * d, 0.5 * d))
        vessel(c, LEFT + 10, 1050, RIGHT - LEFT - 20, t, ease_out(prog(t, 0, 0.35)), sq)
        mono(c, "ARTÉRIA · CHEGA", LEFT + 10, 950, 26, PINK, ease_out(prog(t, 0.15, 0.3)))
        _mono_right(c, "VEIA · SAI DEVAGAR", RIGHT - 10, 1230, 26, CYAN, ease_out(prog(t, 0.35 * d, 0.3)))
        if sq > 0.6:
            chip(c, "CONTRAÇÃO APERTA A SAÍDA", W / 2 - 40, 1340, PINK, NAVY, 44, ease_out(prog(t, 0.65 * d, 0.3)))


def p_plasma(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        sw = ease(prog(t, 0.2 * d, 0.6 * d))
        h = lerp(220, 320, sw)
        fiber(c, LEFT + 20, 1060, RIGHT - LEFT - 40, h, ease_out(prog(t, 0, 0.4)), t=t)
        rnd = random.Random(9)
        for k in range(16):
            f = (t * 0.6 + rnd.random()) % 1
            x0 = LEFT + 60 + rnd.random() * (RIGHT - LEFT - 120)
            yy = lerp(760, 1060 + rnd.uniform(-0.3, 0.3) * h, ease(f))
            disk(c, x0, yy, 11, CYAN, 0.85 * clamp(prog(t, 0.15 * d, 0.3)) * (1 - 0.6 * f))
        callout(c, 300, 1060 - h / 2, 380, 760, "PLASMA ENTRANDO", ease_out(prog(t, 0.35 * d, 0.5)), CYAN, 30)
        mono(c, f"VOLUME DA FIBRA +{int(sw * 25):02d}%", LEFT + 20, 1330, 34, MUTED, ease_out(prog(t, 0.2, 0.3)))


def p_agua(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        fiber(c, LEFT + 20, 1050, RIGHT - LEFT - 40, 300, ease_out(prog(t, 0, 0.4)), acid=0.2, t=t)
        labels = ["LACTATO", "FOSFATO", "H+"]
        for i, s in enumerate(labels):
            x = LEFT + 160 + i * 270
            q = ease_out(prog(t, 0.15 + i * 0.15 * d, 0.35))
            chip(c, s, x, 1050, PINK, NAVY, 36, q)
            for k in range(3):  # água sendo puxada
                f = (t * 0.8 + k / 3) % 1
                ang = -math.pi / 2 + (k - 1) * 0.7
                disk(c, x + math.cos(ang) * lerp(200, 50, f), 1050 + math.sin(ang) * lerp(200, 50, f), 9, CYAN, q * (0.3 + 0.7 * f))
        mono(c, "METABÓLITOS PUXAM ÁGUA", LEFT + 20, 1290, 34, CYAN, ease_out(prog(t, 0.45 * d, 0.3)))


def p_some(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        f = ease(prog(t, 0.1, d * 0.75))
        clock(c, 290, 1040, 180, f, ease_out(prog(t, 0, 0.3)))
        mono(c, "1 A 2 HORAS", 290, 1290, 36, CYAN, ease_out(prog(t, 0.2, 0.3)), align="center")
        arm(c, 540, 1060, 0.62, 0.95, ease_out(prog(t, 0, 0.3)), lerp(1.0, 0.25, f), t)
        if f > 0.85:
            chip(c, "VOLTOU AO NORMAL", 730, 1300, GOOD, NAVY, 40, ease_out(prog(t, 0.8 * d, 0.3)))


def p_fica(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        plates = 1 + int(3 * ease(prog(t, 0.45 * d, d * 0.4)))
        barbell_line(c, W / 2 - 40, 830 + math.sin(t * 4) * 18, 1.05, plates)
        mini_chart(c, LEFT + 20, 990, RIGHT - LEFT - 40, 360, prog(t, 0.2 * d, d * 0.6))
        mono(c, "CARGA / SEMANA", LEFT + 50, 1040, 28, MUTED, ease_out(prog(t, 0.2, 0.3)))


# ----------------------------------------------------------------- TREMOR
def units(c, x, y, t, active, tired=0, p=1.0):
    """3 unidades motoras: nervo do cérebro até um feixe de fibras; active = quantas acesas; tired = quantas cansadas"""
    for i in range(3):
        ux = x + i * 270
        on = i < active; cansada = i < tired
        col = PINK if cansada else (CYAN if on else LINE)
        cap_line(c, W / 2 - 40, 720, ux, y - 120, col, 3, p)
        for k in range(5):
            rrect(c, ux - 80, y - 90 + k * 40, 160, 26, 13, NAVY2, p)
            rrect(c, ux - 80, y - 90 + k * 40, 160, 26, 13); rgb(c, col, p); c.set_line_width(2.5); c.stroke()
        if on and not cansada:
            f = (t * 1.6 + i * 0.3) % 1
            disk(c, lerp(W / 2 - 40, ux, f), lerp(720, y - 120, f), 9, INK, p)
        if not cansada:
            mono(c, f"GRUPO {i + 1}", ux, y + 150, 26, col if on else MUTED, p, align="center")


def t_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        sh = math.sin(t * 40) * 6 * clamp(prog(t, 0.2, 0.3))
        c.save(); c.translate(sh, 0)
        fiber(c, LEFT + 20, 960, RIGHT - LEFT - 40, 240, ease_out(prog(t, 0, 0.35)), t=t)
        c.restore()
        panel(c, LEFT + 20, 1170, RIGHT - LEFT - 40, 220, ease_out(prog(t, 0.1, 0.35)))
        wave(c, LEFT + 50, 1280, RIGHT - LEFT - 100, 40, t, prog(t, 0.15, 0.5), irregular=0.9, col=PINK)
        mono(c, "SINAL DO NERVO", LEFT + 50, 1210, 24, MUTED, ease_out(prog(t, 0.2, 0.3)))


def t_equipes(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        brain(c, W / 2 - 40, 690, 0.7, glow=0.3)
        units(c, 230, 1120, t, int(1 + 2.99 * ease(prog(t, 0.15, d * 0.6))), p=ease_out(prog(t, 0, 0.35)))
        mono(c, "1 NERVO = 1 GRUPO DE FIBRAS", W / 2 - 40, 1400, 30, CYAN, ease_out(prog(t, 0.5 * d, 0.3)), align="center")


def t_liso(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        brain(c, W / 2 - 40, 690, 0.7)
        units(c, 230, 1050, t, 2, p=1.0)
        panel(c, LEFT + 20, 1250, RIGHT - LEFT - 40, 180, ease_out(prog(t, 0, 0.3)))
        wave(c, LEFT + 50, 1340, RIGHT - LEFT - 100, 34, t, prog(t, 0.1, 0.6), 0.0, CYAN)


def t_reforco(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        brain(c, W / 2 - 40, 690, 0.7, glow=0.6)
        tired = 2 if prog(t, 0.2 * d, 0.1) > 0 else 0
        units(c, 230, 1050, t, 3, tired=tired)
        panel(c, LEFT + 20, 1250, RIGHT - LEFT - 40, 180)
        wave(c, LEFT + 50, 1340, RIGHT - LEFT - 100, 34, t, 1.0, ease(prog(t, 0.3 * d, 0.5 * d)), mix(CYAN, PINK, prog(t, 0.3 * d, 0.5 * d)))
        if tired:
            chip(c, "CANSADOS", 365, 1180, PINK, NAVY, 30, ease_out(prog(t, 0.2 * d, 0.3)))


def t_treme(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        panel(c, LEFT + 20, 760, RIGHT - LEFT - 40, 420, ease_out(prog(t, 0, 0.3)))
        wave(c, LEFT + 50, 970, RIGHT - LEFT - 100, 90, t, prog(t, 0.05, 0.4), 1.0, PINK, seed=5)
        for i, (s, x) in enumerate((("LIGA", 280), ("DESLIGA", 560), ("LIGA", 820))):
            chip(c, s, x, 1270, CYAN if s == "LIGA" else PINK, NAVY, 40, ease_out(prog(t, 0.2 + i * 0.18, 0.3)))
        mono(c, "FORA DE RITMO = TREMOR", W / 2 - 40, 1400, 32, INK, ease_out(prog(t, 0.5 * d, 0.3)), align="center")


def t_limite(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        v = ease(prog(t, 0.1, d * 0.5)) * 0.92
        gauge(c, W / 2 - 40, 1120, 230, v, ease_out(prog(t, 0, 0.3)), "ESFORÇO", "LEVE", "LIMITE")
        if v > 0.8:
            chip(c, "ESTÍMULO MÁXIMO", W / 2 - 40, 1330, PINK, NAVY, 48, ease_out(prog(t, 0.55 * d, 0.3)))


# ----------------------------------------------------------------- NEURAL
def two_bars(c, x, y, h, fa, ta, p=1.0):
    for i, (lab, v, col) in enumerate((("FORÇA", fa, CYAN), ("TAMANHO", ta, PINK))):
        bx = x + i * 300
        rrect(c, bx, y - h, 180, h, 14, NAVY2, p); rrect(c, bx, y - h, 180, h, 14); rgb(c, LINE, p); c.set_line_width(2); c.stroke()
        bh = (h - 20) * v
        rrect(c, bx + 10, y - 10 - bh, 160, bh, 10, col, p)
        mono(c, lab, bx + 90, y + 50, 30, col, p, align="center")


def n_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        f = ease(prog(t, 0.15, d * 0.6))
        two_bars(c, 260, 1300, 520, 0.25 + 0.6 * f, 0.25 + 0.03 * f, ease_out(prog(t, 0, 0.3)))
        mono(c, f"SEMANA {1 + int(3 * f)}", W / 2 - 40, 1440, 30, MUTED, ease_out(prog(t, 0.1, 0.3)), align="center")
        if f > 0.6:
            mono(c, "?", 920, 900, 90, PINK, ease_out(prog(t, 0.6 * d, 0.3)))


def n_cerebro(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        g = ease(prog(t, 0.1, d * 0.5))
        brain(c, 300, 860, 1.25, glow=g)
        nerve(c, 380, 960, 700, 1180, t, ease_out(prog(t, 0.3 * d, 0.4)), CYAN)
        fiber(c, 640, 1240, 340, 160, ease_out(prog(t, 0.25 * d, 0.4)), t=t)
        if g > 0.7:
            chip(c, "EVOLUI PRIMEIRO", 300, 1100, CYAN, NAVY, 40, ease_out(prog(t, 0.5 * d, 0.3)))


def n_ativa(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        frac = lerp(0.3, 0.85, ease(prog(t, 0.2 * d, 0.6 * d)))
        cols, rows = 7, 5
        rnd = random.Random(11); order = list(range(cols * rows)); rnd.shuffle(order)
        lit = set(order[:int(frac * cols * rows)])
        for i in range(cols * rows):
            cx = LEFT + 100 + (i % cols) * 125; cy = 820 + (i // cols) * 115
            on = i in lit
            disk(c, cx, cy, 44, CYAN if on else NAVY2, 0.95)
            c.new_path(); c.arc(cx, cy, 44, 0, 6.3); rgb(c, CYAN if on else LINE); c.set_line_width(3); c.stroke()
        mono(c, f"FIBRAS ATIVAS: {int(frac * 100)}%", W / 2 - 40, 1420, 36, INK, ease_out(prog(t, 0.1, 0.3)), align="center")


def n_sinal(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        sp = lerp(1.0, 3.0, ease(prog(t, 0.2 * d, 0.5 * d)))
        brain(c, 220, 900, 0.8, glow=0.5)
        cap_line(c, 300, 900, RIGHT - 60, 900, CYAN, 5)
        for k in range(3):
            f = (t * sp * 0.6 + k / 3) % 1
            disk(c, lerp(300, RIGHT - 60, f), 900, 13, INK)
        panel(c, LEFT + 20, 1080, RIGHT - LEFT - 40, 260, ease_out(prog(t, 0.1, 0.3)))
        for k in range(int(4 + 8 * (sp - 1) / 2)):
            x = LEFT + 70 + k * 72
            cap_line(c, x, 1300, x, 1140, CYAN, 6, ease_out(prog(t, 0.15 + k * 0.05, 0.2)))
        mono(c, "MAIS RÁPIDO, MAIS SINCRONIZADO", W / 2 - 40, 1400, 30, CYAN, ease_out(prog(t, 0.4 * d, 0.3)), align="center")


def n_espelho(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        x0, y0, w, h = LEFT + 40, 1340, RIGHT - LEFT - 80, 560
        cap_line(c, x0, y0, x0 + w, y0, LINE, 3); cap_line(c, x0, y0, x0, y0 - h, LINE, 3)
        p = ease(prog(t, 0.1, d * 0.75))
        fp, tp = [], []
        for i in range(int(40 * p) + 1):
            f = i / 40
            fp.append((x0 + w * f, y0 - h * (0.15 + 0.7 * (1 - math.exp(-4 * f)))))
            tp.append((x0 + w * f, y0 - h * (0.12 + 0.55 * clamp((f - 0.35) / 0.65) ** 1.3)))
        if len(fp) > 1:
            poly(c, fp, CYAN, 6); poly(c, tp, PINK, 6)
        mono(c, "FORÇA", x0 + 20, y0 - h + 30, 30, CYAN, ease_out(prog(t, 0.2, 0.3)))
        mono(c, "TAMANHO", x0 + w - 200, y0 - 60, 30, PINK, ease_out(prog(t, 0.5 * d, 0.3)))
        mono(c, "SEMANAS →", x0 + w - 180, y0 + 50, 26, MUTED, ease_out(prog(t, 0.1, 0.3)))


def n_tamanho(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        g = ease(prog(t, 0.15, d * 0.6))
        fiber(c, LEFT + 20, 1000, RIGHT - LEFT - 40, lerp(170, 330, g), ease_out(prog(t, 0, 0.35)), t=t)
        tally_x = LEFT + 20
        for k in range(int(12 * g)):
            rrect(c, tally_x + k * 70, 1290, 50, 50, 8, CYAN, 0.9)
        mono(c, "TREINOS SEGUIDOS", LEFT + 20, 1400, 30, MUTED, ease_out(prog(t, 0.1, 0.3)))


# ----------------------------------------------------------------- AGACHAMENTO
def squat(c, x, y, s, depth, hl, t, p=1.0):
    """boneco técnico de perfil (olhando para a direita); tornozelo em (x,y). hl: dict músculo -> brilho 0..1"""
    Ls, Lt, Lb = 300 * s, 320 * s, 380 * s
    a_s = math.radians(lerp(4, 34, depth)); a_t = math.radians(lerp(8, 92, depth)); a_b = math.radians(lerp(6, 42, depth))
    ank = (x, y)
    kne = (x + math.sin(a_s) * Ls, y - math.cos(a_s) * Ls)
    hip = (kne[0] - math.sin(a_t) * Lt, kne[1] - math.cos(a_t) * Lt)
    sho = (hip[0] + math.sin(a_b) * Lb, hip[1] - math.cos(a_b) * Lb)
    cap_line(c, ank[0] - 30 * s, y + 20 * s, ank[0] + 110 * s, y + 20 * s, CYAN, 8, p)
    # músculos (atrás dos ossos)
    tx, ty = hip[0] - kne[0], hip[1] - kne[1]; ang_t = math.atan2(ty, tx); L = math.hypot(tx, ty)
    nx, ny = -ty / L, tx / L
    if ny > 0: nx, ny = -nx, -ny  # normal para cima = frente da coxa
    mx, my = (hip[0] + kne[0]) / 2, (hip[1] + kne[1]) / 2
    ellipse(c, mx + nx * 42 * s, my + ny * 42 * s, Lt * 0.42, 46 * s, ang_t, mix(NAVY2, PINK, hl.get("quad", 0)), p, CYAN)
    ellipse(c, hip[0] - 20 * s - 30 * s * math.cos(a_b), hip[1] + 10 * s, 78 * s, 66 * s, 0, mix(NAVY2, PINK, hl.get("gluteo", 0)), p, CYAN)
    ellipse(c, mx - nx * 30 * s + (hip[0] - mx) * 0.3, my - ny * 30 * s + (hip[1] - my) * 0.3, Lt * 0.28, 30 * s, ang_t,
            mix(NAVY2, PINK, hl.get("adutor", 0)), p, CYAN)
    bx, by = sho[0] - hip[0], sho[1] - hip[1]; ang_b = math.atan2(by, bx)
    ellipse(c, (hip[0] + sho[0]) / 2, (hip[1] + sho[1]) / 2, Lb * 0.42, 52 * s, ang_b, mix(NAVY2, PINK, hl.get("core", 0)), p, CYAN)
    # ossos
    for a_, b_ in ((ank, kne), (kne, hip), (hip, sho)):
        cap_line(c, a_[0], a_[1], b_[0], b_[1], INK, 6, p)
    for j in (ank, kne, hip, sho):
        disk(c, j[0], j[1], 11, INK, p)
    hx, hy = sho[0] + math.sin(a_b) * 90 * s, sho[1] - math.cos(a_b) * 90 * s
    c.new_path(); c.arc(hx, hy, 58 * s, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    # braços estendidos à frente (contrapeso)
    cap_line(c, sho[0], sho[1], sho[0] + 230 * s, sho[1] + 20 * s, INK, 6, p)
    return dict(ank=ank, kne=kne, hip=hip, sho=sho, quad=(mx + nx * 42 * s, my + ny * 42 * s))


SQX, SQY, SQS = 500, 1420, 0.7


def a_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        dep = 0.6 + 0.4 * math.sin(t * 2.6 - 1.5)
        k = int(4 * clamp(prog(t, 0.15, d * 0.7)) + 0.0001)
        hl = {m: (1.0 if i < k else 0.0) for i, m in enumerate(("quad", "gluteo", "adutor", "core"))}
        squat(c, SQX, SQY, SQS, dep, hl, t, ease_out(prog(t, 0, 0.3)))
        mono(c, f"MÚSCULOS: {k}", RIGHT - 20, 760, 40, PINK if k else MUTED, ease_out(prog(t, 0.1, 0.3)), align="right") if False else \
            _mono_right(c, f"MÚSCULOS: {k}", RIGHT - 20, 760, 40, PINK if k else MUTED, ease_out(prog(t, 0.1, 0.3)))


def _focus(muscle, label, call_dy=-120):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.06, cy=CY):
            dep = 0.62 + 0.38 * math.sin(t * 2.2 - 1.5)
            g = ease_out(prog(t, 0.1, 0.4))
            j = squat(c, SQX, SQY, SQS, dep, {muscle: g}, t)
            px, py = {"quad": j["quad"], "gluteo": (j["hip"][0] - 60, j["hip"][1]), "adutor": ((j["hip"][0] + j["kne"][0]) / 2, (j["hip"][1] + j["kne"][1]) / 2 + 20),
                      "core": ((j["hip"][0] + j["sho"][0]) / 2, (j["hip"][1] + j["sho"][1]) / 2)}[muscle]
            callout(c, px, py, 760, 720 if muscle != "gluteo" else 760, label, ease_out(prog(t, 0.25, 0.5)), PINK, 30)
    return f


def a_fundo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        dep = lerp(0.35, 1.0, 0.5 + 0.5 * math.sin(t * 1.8 - 1.5))
        squat(c, 460, SQY, 0.72, dep, {"gluteo": dep, "adutor": dep, "quad": 0.5}, t)
        rrect(c, RIGHT - 60, 760, 36, 560, 18, NAVY2); rrect(c, RIGHT - 60, 760, 36, 560, 18); rgb(c, LINE); c.set_line_width(2); c.stroke()
        rrect(c, RIGHT - 54, 1314 - 548 * dep, 24, 548 * dep, 12, PINK)
        _mono_right(c, "AMPLITUDE", RIGHT - 80, 790, 28, PINK, ease_out(prog(t, 0.1, 0.3)))
        if prog(t, 0.5 * d, 0.2) > 0:
            chip(c, "COM CONTROLE", 760, 1330, CYAN, NAVY, 40, ease_out(prog(t, 0.5 * d, 0.3)))


VIS = dict(
    p_hook=p_hook, p_veia=p_veia, p_plasma=p_plasma, p_agua=p_agua, p_some=p_some, p_fica=p_fica, p_cta=cta_factory("PUMP"),
    t_hook=t_hook, t_equipes=t_equipes, t_liso=t_liso, t_reforco=t_reforco, t_treme=t_treme, t_limite=t_limite, t_cta=cta_factory("TREMI"),
    n_hook=n_hook, n_cerebro=n_cerebro, n_ativa=n_ativa, n_sinal=n_sinal, n_espelho=n_espelho, n_tamanho=n_tamanho, n_cta=cta_factory("FORÇA"),
    a_hook=a_hook, a_quad=_focus("quad", "QUADRÍCEPS"), a_gluteo=_focus("gluteo", "GLÚTEO MÁXIMO"), a_adutor=_focus("adutor", "ADUTORES"),
    a_tronco=_focus("core", "ABDÔMEN + LOMBAR"), a_fundo=a_fundo, a_cta=cta_factory("AGACHO"),
)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else SFX_CTA if k.endswith("cta") else [(0.0, "whoosh"), ("0.5d", "pop")])
       for k in VIS}


# ----------------------------------------------------------------- CÃIBRA
def leg_calf(c, x, y, s, cramp, t, p=1.0):
    """panturrilha de perfil (canela + pé); cramp 0..1 contrai a panturrilha e aponta o pé"""
    c.save(); c.translate(x, y); c.scale(s, s)
    capsule(c, 0, -420, 0, 0, 70, p)  # canela
    foot = math.radians(lerp(0, 35, cramp))
    fx, fy = 220 * math.cos(foot), 220 * math.sin(foot)
    capsule(c, 0, 0, fx, fy, 56, p)  # pé
    bulge = lerp(1.0, 1.35, cramp)
    shake = math.sin(t * 45) * 5 * cramp
    ellipse(c, -52 + shake, -260, 50 * bulge, 150, 0, mix(NAVY2, PINK, 0.25 + 0.75 * cramp), p, CYAN)
    c.restore()


def c_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        cr = clamp(prog(t, 0.2, 0.4))
        leg_calf(c, 420, 1300, 1.2, cr, t, ease_out(prog(t, 0, 0.3)))
        callout(c, 360, 970, 560, 760, "CÃIBRA", ease_out(prog(t, 0.35, 0.5)), PINK, 40)


def c_mito(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        panel(c, LEFT + 20, 720, RIGHT - LEFT - 40, 170, p)
        draw_text(c, "SÓ POTÁSSIO?", LEFT + 70, 840, 92, INK, TITLE, p)
        x = ease_out(prog(t, 0.35, 0.3))
        if x > 0:
            cap_line(c, LEFT + 50, 808, LEFT + 50 + 640 * x, 808, PINK, 12)
        q = ease_out(prog(t, 0.4 * d, 0.4))
        if q > 0:
            for i, (lab, v) in enumerate((("ELETRÓLITOS", 0.25), ("FADIGA DO NERVO", 0.85))):
                y = 1060 + i * 150
                mono(c, lab, LEFT + 20, y, 30, MUTED, q)
                rrect(c, LEFT + 20, y + 20, RIGHT - LEFT - 40, 34, 17, NAVY2, q)
                rrect(c, LEFT + 20, y + 20, (RIGHT - LEFT - 40) * v * q, 34, 17, PINK if i else LINE, q)
            mono(c, "PESO DA EVIDÊNCIA", LEFT + 20, 1400, 26, MUTED, q)


def c_nervo(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        brain(c, 250, 820, 0.8, glow=0.4)
        n = 1 + int(5 * ease(prog(t, 0.2 * d, 0.5 * d)))
        cap_line(c, 320, 880, 760, 1150, CYAN, 4)
        for k in range(n):
            f = (t * 1.8 + k / n) % 1
            disk(c, lerp(320, 760, f), lerp(880, 1150, f), 11, PINK)
        fiber(c, 560, 1250, 400, 170, ease_out(prog(t, 0, 0.35)), acid=0.3, t=t)
        mono(c, f"DISPAROS/S: {n * 12}", LEFT + 20, 1420, 32, PINK, ease_out(prog(t, 0.2, 0.3)))


def c_trava(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        leg_calf(c, 420, 1300, 1.2, 1.0, t)
        if prog(t, 0.3 * d, 0.2) > 0:
            chip(c, "CONTRAÇÃO TRAVADA", 700, 900, PINK, NAVY, 40, ease_out(prog(t, 0.3 * d, 0.3)))


def c_alonga(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        cr = 1 - ease(prog(t, 0.15, d * 0.6))
        c.save(); c.translate(420, 1300); c.restore()
        leg_calf(c, 420, 1300, 1.2, cr * 0.9 - 0.25 * (1 - cr), t)
        harc = ease_out(prog(t, 0.1, 0.4))
        c.new_path(); c.arc(680, 1300, 150, -1.2, -1.2 + 1.0 * harc); rgb(c, CYAN); c.set_line_width(6); c.stroke()
        mono(c, "PÉ PRA CIMA, DEVAGAR", 600, 1120, 28, CYAN, ease_out(prog(t, 0.2, 0.3)))
        if cr < 0.15:
            chip(c, "SOLTOU", 760, 1420, GOOD, NAVY, 40, ease_out(prog(t, 0.75 * d, 0.3)))


def c_evita(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        mono(c, "SÉRIES POR SEMANA", LEFT + 20, 780, 30, MUTED, p)
        vals = [3, 4, 5, 6]
        for i, v in enumerate(vals):
            q = ease_out(prog(t, 0.15 + i * 0.15, 0.3))
            bh = 70 * v * q
            rrect(c, LEFT + 40 + i * 120, 1250 - bh, 80, bh, 8, CYAN, q)
        mono(c, "AOS POUCOS", LEFT + 40, 1310, 30, CYAN, ease_out(prog(t, 0.6, 0.3)))
        q2 = ease_out(prog(t, 0.35 * d, 0.3))
        rrect(c, 640, 1250 - 70 * 8 * q2, 110, 70 * 8 * q2, 8, PINK, q2)
        rrect(c, 640, 1250 - 70 * 3 * q2, 110, 70 * 3 * q2, 8, LINE, q2)
        if q2 > 0.5:
            cap_line(c, 600, 700, 800, 1260, PINK, 10)
            cap_line(c, 800, 700, 600, 1260, PINK, 10)
            mono(c, "3 → 8", 695, 1310, 30, PINK, q2, align="center")


VIS.update(c_hook=c_hook, c_mito=c_mito, c_nervo=c_nervo, c_trava=c_trava, c_alonga=c_alonga, c_evita=c_evita, c_cta=cta_factory("CÃIBRA"))
SFX.update({k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else SFX_CTA if k.endswith("cta") else [(0.0, "whoosh"), ("0.5d", "pop")])
            for k in VIS if k.startswith("c_")})
