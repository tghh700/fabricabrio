"""FIBRA — produção 19/11 (prancha técnica, build3): coceira no cardio (cc_), dor de cabeça na série (cb_),
rosto vermelho (vm_), pontada na barriga (pd_). Uma figura por cena; nada atravessa o corpo; só glifos da fonte (sem ✓ ✦ ↑)."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA, squat
from scenes_fibra_g import bar_pct, stomach, drop
from scenes_fibra_1811 import counter, heart
import pauta_1911 as PA

CY = 1080
CX = W / 2 - 40
RED = (0.86, 0.18, 0.26)
ORANGE = (0.98, 0.60, 0.20)


# ------------------------------------------------------------------ peças
def runner(c, x, y, s, t, p=1.0, spd=7.0, hl_leg=0.0, hl_belly=0.0, lean=0.12):
    """corredor técnico de perfil (olhando para a direita); quadril em (x,y). Braço e perna de trás desenhados
    antes do tronco, os da frente depois — nada atravessa o corpo."""
    if p <= 0:
        p = 0.0
    Lt, Ls, Lb, La = 190 * s, 190 * s, 300 * s, 140 * s
    bob = 10 * s * abs(math.sin(t * spd))
    hip = (x, y - bob)
    sho = (hip[0] + math.sin(lean) * Lb, hip[1] - math.cos(lean) * Lb)

    def leg(ph):
        a = 0.75 * math.sin(ph)                      # coxa: + = para a frente
        kn = (hip[0] + Lt * math.sin(a), hip[1] + Lt * math.cos(a))
        flex = 0.25 + 0.9 * max(0.0, -math.cos(ph))   # joelho dobra mais na volta
        b = a - flex
        an = (kn[0] + Ls * math.sin(b), kn[1] + Ls * math.cos(b))
        return kn, an

    def arm(ph):
        a = -0.7 * math.sin(ph)                          # braço oposto à perna; + = para a frente
        el = (sho[0] + La * math.sin(a), sho[1] + La * math.cos(a))
        wr = (el[0] + La * 0.9 * math.sin(a + 1.4), el[1] + La * 0.9 * math.cos(a + 1.4))   # cotovelo dobrado ~80°, mão à frente
        return el, wr

    ph = t * spd
    back_leg, front_leg = leg(ph + math.pi), leg(ph)
    back_arm, front_arm = arm(ph), arm(ph + math.pi)
    dim = mix(INK, MUTED, 0.5)
    # trás
    el, wr = back_arm
    cap_line(c, sho[0], sho[1], el[0], el[1], dim, 6, p); cap_line(c, el[0], el[1], wr[0], wr[1], dim, 6, p)
    kn, an = back_leg
    cap_line(c, hip[0], hip[1], kn[0], kn[1], dim, 7, p); cap_line(c, kn[0], kn[1], an[0], an[1], dim, 7, p)
    el, wr = front_arm                                   # braços atrás do tronco: o que cruza o tronco fica escondido
    cap_line(c, sho[0], sho[1], el[0], el[1], INK, 6, p); cap_line(c, el[0], el[1], wr[0], wr[1], INK, 6, p)
    # tronco (barriga destacada)
    mx, my = (hip[0] + sho[0]) / 2, (hip[1] + sho[1]) / 2
    ellipse(c, mx, my, Lb * 0.5, 62 * s, math.atan2(sho[1] - hip[1], sho[0] - hip[0]), NAVY2, p, CYAN)
    bx, by = lerp(hip[0], sho[0], 0.3) + 18 * s, lerp(hip[1], sho[1], 0.3)
    if hl_belly > 0:
        ellipse(c, bx, by, 34 * s, 30 * s, 0, PINK, p * hl_belly)
    cap_line(c, hip[0], hip[1], sho[0], sho[1], INK, 6, p)
    hx, hy = sho[0] + math.sin(lean) * 80 * s, sho[1] - math.cos(lean) * 80 * s
    c.new_path(); c.arc(hx, hy, 52 * s, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    # frente
    kn, an = front_leg
    if hl_leg > 0:
        ellipse(c, (kn[0] + an[0]) / 2, (kn[1] + an[1]) / 2, Ls * 0.45, 22 * s, math.atan2(an[1] - kn[1], an[0] - kn[0]), PINK, p * hl_leg)
    cap_line(c, hip[0], hip[1], kn[0], kn[1], INK, 7, p); cap_line(c, kn[0], kn[1], an[0], an[1], INK, 7, p)
    cap_line(c, an[0], an[1], an[0] + 40 * s, an[1] + 4 * s, INK, 7, p)
    for j in (hip, sho, kn):
        disk(c, j[0], j[1], 9, INK, p)
    return dict(hip=hip, sho=sho, head=(hx, hy), belly=(bx, by), shin=((kn[0] + an[0]) / 2, (kn[1] + an[1]) / 2))


def treadmill(c, x0, x1, y, t, p=1.0):
    rrect(c, x0, y, x1 - x0, 26, 13, NAVY2, p); rrect(c, x0, y, x1 - x0, 26, 13); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    for i in range(8):
        f = ((i / 8) - t * 0.9) % 1
        cap_line(c, lerp(x0 + 20, x1 - 20, f), y + 13, lerp(x0 + 20, x1 - 20, f) + 14, y + 13, LINE, 4, p)


def itch_marks(c, x, y, t, k, p=1.0, n=6, r=80):
    """riscos em zigue-zague em volta de um ponto (sinal de coceira)"""
    rnd = random.Random(11)
    for i in range(n):
        a = rnd.uniform(0, 6.28); rr = r + 14 * math.sin(t * 9 + i)
        px, py = x + rr * math.cos(a), y + rr * math.sin(a)
        pts = [(px + j * 9, py + (6 if j % 2 else -6)) for j in range(4)]
        poly(c, pts, PINK, 4, p * k * (0.6 + 0.4 * math.sin(t * 12 + i * 2)))


def vessel_wide(c, x0, x1, y, wv, t, speed, p=1.0, label=True):
    cap_line(c, x0, y, x1, y, PINK, wv + 14, p); cap_line(c, x0, y, x1, y, (0.30, 0.08, 0.14), wv, p)
    n = 9
    for i in range(n):
        f = (t * speed + i / n) % 1
        ellipse(c, lerp(x0 + 20, x1 - 20, f), y + (i % 3 - 1) * wv * 0.22, 15, 10, 0, RED, p)


def thermo(c, x, y, frac, p=1.0):
    rrect(c, x - 22, y - 300, 44, 300, 22, NAVY2, p); rrect(c, x - 22, y - 300, 44, 300, 22); rgb(c, INK, p); c.set_line_width(3); c.stroke()
    h = 40 + 230 * frac
    rrect(c, x - 12, y - h, 24, h, 12, mix(ORANGE, RED, frac), p)
    disk(c, x, y + 10, 40, mix(ORANGE, RED, frac), p)
    c.new_path(); c.arc(x, y + 10, 40, 0, 6.3); rgb(c, INK, p); c.set_line_width(3); c.stroke()


def heat_waves(c, x, y, t, p, w=160, n=3, col=ORANGE):
    for k in range(n):
        f = (t * 0.8 + k / n) % 1
        yy = y - 140 * f
        pts = [(x - w / 2 + i * w / 16, yy + math.sin(i * 0.9 + t * 6 + k) * 8) for i in range(17)]
        poly(c, pts, col, 4, p * (1 - f))


def face(c, x, y, r, red, t, p=1.0):
    """rosto de frente (sem traços de expressão além de olhos/boca) que fica vermelho com 'red' 0..1"""
    c.new_path(); c.arc(x, y, r, 0, 6.3); rgb(c, mix(NAVY2, RED, 0.75 * red), p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
    for sd in (-1, 1):
        ellipse(c, x + sd * r * 0.55, y + r * 0.25, r * 0.22, r * 0.14, 0, mix(NAVY2, PINK, red), p * red)
        disk(c, x + sd * r * 0.35, y - r * 0.12, r * 0.07, INK, p)
    c.new_path(); c.arc(x, y + r * 0.35, r * 0.22, 0.2, math.pi - 0.2); rgb(c, INK, p); c.set_line_width(5); c.stroke()
    # gotas de suor na testa
    for k in range(3):
        f = (t * 0.6 + k / 3) % 1
        disk(c, x - r * 0.5 + k * r * 0.5, y - r * 0.6 + 40 * f, 8, CYAN, p * red * (1 - f))


def abdomen(c, x, y, w, h, t, bounce=0.0, irrit=0.0, full=0.0, p=1.0):
    """corte do abdômen: membrana (peritônio) por dentro da parede, órgãos que sacodem com 'bounce'"""
    rrect(c, x, y, w, h, 60, NAVY2, p); rrect(c, x, y, w, h, 60); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
    col = mix(CYAN, PINK, irrit)
    rrect(c, x + 22, y + 22, w - 44, h - 44, 44); rgb(c, col, p * (0.5 + 0.5 * irrit)); c.set_line_width(4 + 6 * irrit)
    c.set_dash([14, 10]); c.stroke(); c.set_dash([])
    dy = bounce * 26 * math.sin(t * 9)
    # órgãos (fígado, estômago, alças)
    ellipse(c, x + w * 0.32, y + h * 0.28 + dy, w * 0.2, h * 0.12, -0.2, mix(NAVY, (0.45, 0.20, 0.25), 0.8), p, MUTED)
    ellipse(c, x + w * 0.66, y + h * 0.30 + dy * 1.2, w * (0.15 + 0.07 * full), h * (0.11 + 0.05 * full), 0.3, mix(NAVY, PINK, 0.25 + 0.3 * full), p, MUTED)
    for i in range(3):
        for j in range(2):
            ellipse(c, x + w * (0.3 + 0.2 * i), y + h * (0.58 + 0.17 * j) + dy * 0.8, w * 0.09, h * 0.06, 0, mix(NAVY, CYAN, 0.18), p, MUTED)
    # ligamentos que puxam a membrana
    for sd in (0.32, 0.66):
        cap_line(c, x + w * sd, y + 24, x + w * sd, y + h * 0.18 + dy, mix(MUTED, PINK, irrit), 4, p)


# ================================================================ COCEIRA (cc_)
def cc_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.4, 1.0))
        treadmill(c, 110, 620, 1500, t, p)
        j = runner(c, 330, 1120, 1.0, t, p, 7.0, hl_leg=0.6 * k)
        itch_marks(c, j["shin"][0], j["shin"][1], t, k, p, 7, 70)
        chip(c, "COÇA!", 790, 1100, PINK, NAVY, 56, ease_out(prog(t, 0.9, 0.3)))


def cc_vasos(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        panel(c, LEFT + 10, 730, RIGHT - LEFT - 20, 600, p)
        mono(c, "VASINHO DA PERNA", LEFT + 50, 800, 30, CYAN, p)
        vessel_wide(c, LEFT + 60, RIGHT - 60, 1010, lerp(24, 80, g), t, lerp(0.3, 1.1, g), p)
        mono(c, "PARADO", LEFT + 50, 1150, 26, MUTED, p)
        mono(c, "CORRENDO", RIGHT - 230, 1150, 26, PINK, p * g)
        bar_pct(c, LEFT + 50, 1180, RIGHT - LEFT - 100, 40, lerp(0.25, 0.95, g), PINK, p)
        chip(c, "SE ABRE", CX, 1440, PINK, NAVY, 52, ease_out(prog(t, 0.5 * d, 0.3)))


def cc_nervo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.5))
        vessel_wide(c, LEFT + 20, RIGHT - 20, 1340, lerp(50, 80, g), t, 1.0, p)
        # terminações nervosas em volta do vaso, acendendo
        for i in range(5):
            x = LEFT + 110 + i * 170
            q = ease_out(prog(t, 0.2 + i * 0.12, 0.3))
            nerve(c, x, 1290, x + 40, 1180, t, q, mix(CYAN, PINK, g))
        brain(c, 760, 840, 0.75, glow=g * (0.6 + 0.4 * math.sin(t * 6)))
        nerve(c, 420, 1150, 700, 900, t, ease(prog(t, 0.5, 0.5)))
        mono(c, "NERVOS", LEFT + 20, 1460, 28, MUTED, p)
        chip(c, "SINAL: COCEIRA", 380, 860, PINK, NAVY, 42, ease_out(prog(t, 0.55 * d, 0.3)))


def cc_parado(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, (lab, cheio, coc) in enumerate((("TREINA SEMPRE", 6, 0.15), ("DIAS PARADO", 1, 0.85))):
            q = ease_out(prog(t, 0.05 + i * 0.4, 0.35))
            if q <= 0:
                continue
            x0 = LEFT + 10 + i * 450
            panel(c, x0, 730, 410, 680, q, PINK if i else CYAN)
            mono(c, lab, x0 + 205, 800, 30, INK, q, align="center")
            for k in range(7):                           # semana: quadrado cheio = dia de treino
                xx = x0 + 40 + (k % 4) * 85; yy = 860 + (k // 4) * 85
                rrect(c, xx, yy, 66, 66, 10, CYAN if k < cheio else NAVY, q)
                rrect(c, xx, yy, 66, 66, 10); rgb(c, LINE, q); c.set_line_width(2); c.stroke()
            mono(c, "COCEIRA", x0 + 40, 1120, 28, MUTED, q)
            v = coc * ease(prog(t, 0.3 + i * 0.4, 0.8))
            bar_pct(c, x0 + 40, 1145, 330, 44, v, PINK, q)
            draw_text(c, f"{int(v * 100)}%", x0 + 40, 1300, 90, PINK if i else CYAN, TITLE, q)


# ================================================================ CABEÇA (cb_)
def throb(c, x, y, r, t, k, p=1.0):
    for i in range(3):
        f = (t * 1.6 + i / 3) % 1
        c.new_path(); c.arc(x, y, r + 90 * f, -2.4, -0.7); rgb(c, PINK, p * k * (1 - f)); c.set_line_width(6); c.stroke()


def cb_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = 0.5 + 0.5 * math.sin(t * 2.4 - 1.5)
        j = squat(c, 330, 1440, 0.72, dep, {"quad": 0.7, "gluteo": 0.5}, t, p)
        hx = j["sho"][0] + 40; hy = j["sho"][1] - 70
        dx, dy = j["sho"][0] + 230 * 0.72, j["sho"][1] + 20 * 0.72          # halter na mão (fora do corpo)
        cap_line(c, dx, dy - 34, dx, dy + 34, INK, 10, p)
        for e in (-1, 1):
            rrect(c, dx - 26, dy + e * 40 - 14, 52, 28, 8, CYAN, p)
        throb(c, hx, hy, 50, t, ease(prog(t, 0.5, 0.6)), p)
        chip(c, "LATEJA", 780, 1000, PINK, NAVY, 54, ease_out(prog(t, 0.9, 0.3)))


def cb_pressao(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        val = lerp(120, 320, g)
        mono(c, "PRESSÃO NA SÉRIE", LEFT + 20, 790, 30, INK, p)
        counter(c, LEFT + 20, 980, val, "mmHg", PINK, p, 170)
        bar_pct(c, LEFT + 20, 1040, RIGHT - LEFT - 40, 50, val / 340, mix(CYAN, PINK, g), p)
        mono(c, "REPOUSO 120", LEFT + 20, 1150, 28, CYAN, p)
        chip(c, "QUASE O TRIPLO", CX, 1330, PINK, NAVY, 52, ease_out(prog(t, 0.55 * d, 0.3)))


def cb_vasos(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        hx, hy, r = CX - 40, 1080, 300
        c.new_path(); c.arc(hx, hy, r, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
        brain(c, hx, hy - 40, 1.3, glow=0.2)
        # vasos da cabeça engrossando
        for i, (a0, a1) in enumerate(((-2.6, -1.9), (-1.6, -0.9), (-0.6, 0.1))):
            pts = [(hx + (r - 40) * math.cos(lerp(a0, a1, u)), hy + (r - 40) * math.sin(lerp(a0, a1, u))) for u in [k / 12 for k in range(13)]]
            poly(c, pts, PINK, lerp(6, 18, g) + 2 * math.sin(t * 7 + i), p)
        throb(c, hx, hy, r - 60, t, g, p)
        _mono_right(c, "VASOS DILATAM", RIGHT - 10, 1470, 32, PINK, ease_out(prog(t, 0.45 * d, 0.3)))


def cb_agua(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        thermo(c, LEFT + 110, 1230, lerp(0.3, 0.9, g), p)
        mono(c, "CALOR", LEFT + 60, 1340, 28, ORANGE, p)
        drop(c, 640, 1060, 1.2, p)
        lvl = lerp(0.85, 0.3, g)
        c.save(); c.translate(640, 1060); c.scale(1.2, 1.2)
        c.new_path(); c.move_to(0, -150); c.curve_to(40, -80, 110, -10, 110, 50); c.curve_to(110, 120, 55, 160, 0, 160)
        c.curve_to(-55, 160, -110, 120, -110, 50); c.curve_to(-110, -10, -40, -80, 0, -150); c.close_path(); c.clip()
        c.rectangle(-120, 160 - 310 * lvl, 240, 310 * lvl); rgb(c, CYAN, 0.55 * p); c.fill(); c.restore()
        mono(c, "ÁGUA NO CORPO", 640, 1330, 28, CYAN, p, align="center")
        chip(c, "PIORA A DOR", CX, 1460, PINK, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


# ================================================================ VERMELHO (vm_)
def vm_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        red = ease(prog(t, 0.3, 1.2))
        face(c, CX, 1080, 260, red, t, p)
        heat_waves(c, CX, 780, t, p * red, 260)
        chip(c, "VERMELHO", CX, 1440, RED, INK, 54, ease_out(prog(t, 0.9, 0.3)))


def vm_motor(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        fiber(c, LEFT + 20, 1180, 560, 160, p, t=t)
        for i in range(8):
            f = (t * 0.7 + i / 8) % 1
            disk(c, LEFT + 60 + (i * 71) % 500, 1160 - 260 * f, 10, ORANGE, p * (1 - f))
        mono(c, "MÚSCULO TRABALHANDO", LEFT + 20, 1420, 28, MUTED, p)
        thermo(c, RIGHT - 90, 1300, lerp(0.3, 0.85, g), p)
        tv = lerp(37.0, 38.5, g)
        draw_text(c, f"{tv:.1f}".replace(".", ","), RIGHT - 330, 900, 110, ORANGE, TITLE, p)
        mono(c, "°C", RIGHT - 140, 890, 34, INK, p)


def vm_pele(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        # camadas da pele (corte)
        rrect(c, LEFT + 10, 900, RIGHT - LEFT - 20, 90, 10, mix(NAVY2, RED, 0.45 * g), p)
        mono(c, "PELE", LEFT + 30, 960, 30, INK, p)
        rrect(c, LEFT + 10, 990, RIGHT - LEFT - 20, 440, 10, NAVY2, p)
        vessel_wide(c, LEFT + 40, RIGHT - 40, 1260, lerp(26, 70, g), t, 0.8, p)
        for i in range(7):                               # sangue quente subindo para a superfície
            f = (t * 0.7 + i / 7) % 1
            ellipse(c, LEFT + 100 + i * 120, lerp(1220, 1000, f), 13, 9, 0, RED, p * g)
        heat_waves(c, CX, 860, t, p * g, 520)
        chip(c, "SOLTA CALOR", CX, 1500, ORANGE, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


def vm_dez(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.25, d * 0.55))
        mono(c, "SANGUE NA PELE", LEFT + 20, 790, 30, INK, p)
        mono(c, "REPOUSO", LEFT + 20, 880, 28, CYAN, p)
        bar_pct(c, LEFT + 20, 905, RIGHT - LEFT - 40, 50, 0.08, CYAN, p)
        mono(c, "TREINO NO CALOR", LEFT + 20, 1030, 28, RED, p)
        bar_pct(c, LEFT + 20, 1055, RIGHT - LEFT - 40, 50, lerp(0.08, 0.95, g), RED, p)
        counter(c, LEFT + 20, 1330, lerp(1, 10, g), "VEZES MAIS", RED, ease_out(prog(t, 0.2, 0.3)), 190)


# ================================================================ PONTADA (pd_)
def pd_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.4, 0.6))
        treadmill(c, 110, 620, 1500, t, p)
        j = runner(c, 330, 1120, 1.0, t, p, lerp(7.0, 4.0, k), hl_belly=k, lean=lerp(0.12, 0.3, k))
        bx, by = j["belly"]
        for i in range(6):                               # pontada: raios curtos saindo do lado da barriga
            a = i * 1.05 + 0.3
            r0 = 40 + 6 * math.sin(t * 12)
            cap_line(c, bx + r0 * math.cos(a), by + r0 * math.sin(a), bx + (r0 + 36) * math.cos(a), by + (r0 + 36) * math.sin(a), PINK, 5, p * k)
        chip(c, "PONTADA", 790, 1080, PINK, NAVY, 54, ease_out(prog(t, 0.9, 0.3)))


def pd_membrana(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.3, d * 0.5))
        abdomen(c, LEFT + 20, 760, 620, 660, t, 0.0, g, 0, p)
        callout(c, LEFT + 618, 1000, 760, 900, "MEMBRANA", ease_out(prog(t, 0.3 * d, 0.35)), PINK, 30)
        _mono_right(c, "PERITÔNIO", RIGHT - 10, 1470, 28, MUTED, ease_out(prog(t, 0.4 * d, 0.3)))
        chip(c, "IRRITADA", 830, 1200, PINK, NAVY, 40, ease_out(prog(t, 0.55 * d, 0.3)))


def pd_sacode(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        ph = (t * 9 / (2 * math.pi)) % 1
        irr = 0.35 + 0.65 * math.exp(-ph * 6)
        abdomen(c, LEFT + 20, 760, 620, 660, t, 1.0, irr, 0, p)
        n = int(t * 9 / (2 * math.pi)) + 1
        mono(c, "PASSADAS", 830, 900, 28, MUTED, p, align="center")
        draw_text(c, f"{n}", 830, 1060, 130, PINK, TITLE, p, align="center")
        chip(c, "ROÇA E PUXA", CX, 1500, PINK, NAVY, 44, ease_out(prog(t, 0.45 * d, 0.3)))


def pd_cheia(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        stomach(c, 330, 1060, 1.0 + 0.3 * g, t, p, food=int(round(2 + 7 * g)))
        mono(c, "ESTÔMAGO", 330, 820, 30, INK, p, align="center")
        mono(c, "CHEIO", 640, 900, 28, MUTED, p)
        bar_pct(c, 640, 925, 240, 44, lerp(0.2, 0.95, g), PINK, p)
        chip(c, "ESTICA TUDO", CX, 1440, PINK, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


VIS = dict(cc_hook=cc_hook, cc_vasos=cc_vasos, cc_nervo=cc_nervo, cc_parado=cc_parado,
           cb_hook=cb_hook, cb_pressao=cb_pressao, cb_vasos=cb_vasos, cb_agua=cb_agua,
           vm_hook=vm_hook, vm_motor=vm_motor, vm_pele=vm_pele, vm_dez=vm_dez,
           pd_hook=pd_hook, pd_membrana=pd_membrana, pd_sacode=pd_sacode, pd_cheia=pd_cheia)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
PRE = {"fibra_18_coceira": "cc_", "fibra_19_cabeca": "cb_", "fibra_20_vermelho": "vm_", "fibra_21_pontada": "pd_"}
for chave, pre in PRE.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
