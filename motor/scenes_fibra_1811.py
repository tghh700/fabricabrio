"""FIBRA — produção 18/11 (prancha técnica, build3): tontura ao levantar (to_), gosto de sangue (sg_), fome que some e volta (fo_),
coração acelera antes da série (co_). Uma figura por cena; nada atravessa o corpo; só glifos da fonte (sem ✓ ✦ ↑)."""
import math
import random
import cairo
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA, squat
from scenes_fibra_g import bar_pct, molecules, stomach
import pauta_1811 as PA

CY = 1080
CX = W / 2 - 40
RED = (0.86, 0.18, 0.26)


# ------------------------------------------------------------------ peças
def heart(c, x, y, s, t=0.0, bpm=70, p=1.0, col=PINK):
    """coração estilizado que pulsa no ritmo de 'bpm'"""
    if p <= 0:
        return 1.0
    ph = (t * bpm / 60.0) % 1
    k = 1 + 0.12 * math.exp(-ph * 10)
    c.save(); c.translate(x, y); c.scale(s * k * p, s * k * p)
    c.new_path(); c.move_to(0, 40)
    c.curve_to(-70, -10, -60, -70, -20, -60); c.curve_to(-5, -56, 0, -45, 0, -38)
    c.curve_to(0, -45, 5, -56, 20, -60); c.curve_to(60, -70, 70, -10, 0, 40); c.close_path()
    rgb(c, col); c.fill_preserve(); rgb(c, INK, 0.6); c.set_line_width(2 / max(s, 0.1)); c.stroke()
    c.restore()
    return k


def ecg(c, x, y, w, h, t, bpm, p=1.0, col=PINK):
    """traçado de eletrocardiograma rolando; mais bpm = picos mais juntos"""
    if p <= 0:
        return
    per = 60.0 / bpm * 160
    pts = []
    for i in range(0, int(w) + 1, 4):
        u = ((i + t * 260) % per) / per
        v = 0
        if 0.40 < u < 0.44: v = -0.25
        elif 0.44 < u < 0.48: v = 1.0
        elif 0.48 < u < 0.52: v = -0.45
        elif 0.62 < u < 0.72: v = 0.2 * math.sin((u - 0.62) / 0.1 * math.pi)
        pts.append((x + i, y - v * h))
    poly(c, pts, col, 4, p)


def counter(c, x, y, val, unit, col, p=1.0, size=150):
    if p <= 0:
        return
    draw_text(c, f"{int(round(val))}", x, y, size, col, TITLE, p)
    font(c, TITLE, size, bold=True); w = c.text_extents(f"{int(round(val))}").x_advance
    mono(c, unit, x + w + 16, y - 10, 30, INK, p)


def tunnel(c, x, y, k):
    """visão escurecendo: tudo fora de um círculo em torno da cabeça fica preto (k 0..1)"""
    if k <= 0:
        return
    r = lerp(1400, 170, k)
    g = cairo.RadialGradient(x, y, r * 0.55, x, y, r)
    g.add_color_stop_rgba(0, 0, 0, 0, 0); g.add_color_stop_rgba(1, 0, 0, 0, 0.92 * k)
    c.save(); c.set_source(g); c.rectangle(0, 0, W, H); c.fill(); c.restore()


def body_column(c, x, t, p, down=0.0, head_n=8):
    """silhueta frontal simplificada (cabeça, tronco, pernas) com 'sangue' — down 0..1 desloca o sangue para as pernas"""
    hy, ty0, ty1, ly1 = 800, 870, 1180, 1500
    c.new_path(); c.arc(x, hy, 52, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    rrect(c, x - 85, ty0, 170, ty1 - ty0, 40, NAVY2, p); rrect(c, x - 85, ty0, 170, ty1 - ty0, 40); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    for sd in (-1, 1):
        rrect(c, x + sd * 45 - 32, ty1 + 10, 64, ly1 - ty1 - 10, 30, NAVY2, p)
        rrect(c, x + sd * 45 - 32, ty1 + 10, 64, ly1 - ty1 - 10, 30); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    heart(c, x, 950, 0.55, t, 80, p)
    rnd = random.Random(9)
    nh = int(round(head_n * (1 - 0.8 * down)))
    for k in range(nh):
        a = rnd.uniform(0, 6.28); r = rnd.uniform(0, 34)
        disk(c, x + r * math.cos(a), hy + r * math.sin(a) + 3 * math.sin(t * 3 + k), 7, PINK, p)
    nl = int(8 + 22 * down)
    for k in range(nl):
        sd = -1 if k % 2 else 1
        yy = lerp(ly1 - 30, ty1 + 40, ((k * 0.37) % 1) * (0.5 + 0.5 * (1 - down)))
        disk(c, x + sd * 45 + 8 * math.sin(k * 2.1 + t * 2), yy, 7, PINK, p)


def lungs(c, x, y, s, p=1.0, glow=0.0, t=0.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    cap_line(c, 0, -230, 0, -120, CYAN, 22, p)                       # traqueia
    cap_line(c, 0, -120, -60, -70, CYAN, 16, p); cap_line(c, 0, -120, 60, -70, CYAN, 16, p)
    br = 1 + 0.04 * math.sin(t * 5)
    for sd in (-1, 1):
        c.save(); c.translate(sd * 120, 20); c.scale(br, br)
        c.new_path(); c.move_to(sd * -40, -150)
        c.curve_to(sd * 90, -170, sd * 120, 60, sd * 90, 140); c.curve_to(sd * 40, 170, sd * -50, 150, sd * -60, 80)
        c.curve_to(sd * -70, 0, sd * -60, -120, sd * -40, -150); c.close_path()
        rgb(c, mix(NAVY2, PINK, 0.35 * glow), p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3 / s); c.stroke()
        rnd = random.Random(3 + sd)
        for k in range(10):
            disk(c, sd * rnd.uniform(-20, 70), rnd.uniform(-100, 120), 9, mix(CYAN, PINK, glow), 0.6 * p)
        c.restore()
    c.restore()


def wave_lines(c, x, y, t, p, col=PINK, n=3, w=180):
    for k in range(n):
        yy = y - k * 28
        pts = [(x - w / 2 + i * w / 20, yy + math.sin(i * 0.9 + t * 7 + k) * 9) for i in range(21)]
        poly(c, pts, col, 4, p)


# ================================================================ TONTURA (to_)
def to_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        u = ease(prog(t, 0.15, 0.9))                      # levanta do agachamento uma vez
        dep = lerp(1.0, 0.0, u)
        j = squat(c, 360, 1440, 0.74, dep, {"quad": 0.6 * (1 - u)}, t, ease_out(prog(t, 0, 0.3)))
        hx = j["sho"][0] + 40; hy = j["sho"][1] - 70
        k = ease(prog(t, 0.9, 0.8)) * (0.85 + 0.1 * math.sin(t * 4))
        tunnel(c, hx, hy, k)
        chip(c, "VISTA ESCURECE", 700, 1420, PINK, NAVY, 46, ease_out(prog(t, 1.1, 0.3)))


def to_pressao(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.35))
        down = ease(prog(t, 0.3, d * 0.6))
        body_column(c, 300, t, p, down)
        gauge(c, 720, 1080, 140, down, ease_out(prog(t, 0.15, 0.3)), "", "OK", "BAIXA")
        mono(c, "PRESSÃO", 720, 1190, 34, INK, ease_out(prog(t, 0.15, 0.3)), align="center")
        callout(c, 340, 800, 600, 1300, "MENOS NA CABEÇA", ease_out(prog(t, 0.45 * d, 0.35)), PINK, 30)
        mono(c, "SANGUE NAS PERNAS", 300, 1555, 26, MUTED, ease_out(prog(t, 0.3 * d, 0.3)), align="center")


def to_ar(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        hold = ease(prog(t, 0.3, 0.6))
        panel(c, LEFT + 10, 720, RIGHT - LEFT - 20, 640, p)
        mono(c, "AR PRESO NA SÉRIE", LEFT + 50, 790, 30, PINK, p)
        lungs(c, CX - 40, 1090, 0.9 + 0.12 * hold, p, glow=hold, t=0)
        k = heart(c, CX - 40, 1140, 0.55 * (1 - 0.3 * hold), t, 90, p)
        # veia que devolve o sangue ao coração: o fluxo fica mais lento quando o peito aperta
        vx = RIGHT - 70
        cap_line(c, vx, 1330, vx, 1000, CYAN, 26, p); cap_line(c, vx, 1330, vx, 1000, NAVY, 14 - 8 * hold, p)
        n = 6
        for i in range(n):
            f = (t * lerp(0.9, 0.2, hold) + i / n) % 1
            disk(c, vx, lerp(1330, 1000, f), 7, INK, p)
        _mono_right(c, "VOLTA MENOS", vx - 40, 1300, 26, CYAN, ease_out(prog(t, 0.5 * d, 0.3)))


def to_corrige(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        bpm = lerp(70, 105, g)
        heart(c, LEFT + 140, 860, 0.9, t, bpm, p)
        counter(c, LEFT + 260, 900, bpm, "BPM", PINK, p, 130)
        ecg(c, LEFT + 20, 1030, RIGHT - LEFT - 40, 50, t, bpm, p)
        # vaso apertando
        y0 = 1260
        mono(c, "VEIAS APERTAM", LEFT + 20, y0 - 70, 28, MUTED, ease_out(prog(t, 0.3, 0.3)))
        wv = lerp(70, 38, g)
        cap_line(c, LEFT + 40, y0, RIGHT - 40, y0, CYAN, wv + 10, p); cap_line(c, LEFT + 40, y0, RIGHT - 40, y0, NAVY, wv, p)
        for i in range(8):
            f = (t * lerp(0.4, 0.9, g) + i / 8) % 1
            disk(c, lerp(LEFT + 40, RIGHT - 40, f), y0, 8, PINK, p)
        chip(c, "PRESSÃO VOLTA", CX, 1430, CYAN, NAVY, 46, ease_out(prog(t, 0.55 * d, 0.3)))


# ================================================================ SANGUE (sg_)
def sg_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        dep = 0.5 + 0.5 * math.sin(t * 4.2 - 1.5)
        j = squat(c, 330, 1440, 0.72, dep, {"quad": 0.9, "gluteo": 0.7}, t, ease_out(prog(t, 0, 0.3)))
        hx = j["sho"][0] + 60; hy = j["sho"][1] - 70
        for k in range(3):                               # respiração ofegante saindo da boca
            f = (t * 1.6 + k / 3) % 1
            cap_line(c, hx + 40 + 90 * f, hy + 10 - 10 * k, hx + 80 + 90 * f, hy + 10 - 10 * k, INK, 4, 0.7 * (1 - f))
        q = back_out(prog(t, 0.5, 0.4))
        if q > 0:
            c.save(); c.translate(760, 1000); c.scale(max(q, 0.01), max(q, 0.01))
            c.new_path(); c.move_to(0, -90); c.curve_to(60, -10, 70, 40, 0, 70); c.curve_to(-70, 40, -60, -10, 0, -90)
            rgb(c, RED); c.fill(); c.restore()
        chip(c, "GOSTO DE SANGUE", 700, 1420, PINK, NAVY, 46, ease_out(prog(t, 0.9, 0.3)))


def sg_pulmao(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        g = ease(prog(t, 0.3, d * 0.6))
        lungs(c, 330, 1130, 1.05, ease_out(prog(t, 0, 0.35)), glow=g, t=t * 1.5)
        gauge(c, 740, 1060, 140, g, ease_out(prog(t, 0.15, 0.3)), "", "BAIXA", "ALTA")
        mono(c, "PRESSÃO", 740, 1170, 34, INK, ease_out(prog(t, 0.15, 0.3)), align="center")
        chip(c, "ESFORÇO MÁXIMO", 740, 1300, PINK, NAVY, 40, ease_out(prog(t, 0.45 * d, 0.3)))


def sg_vaza(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        ax, ay = CX - 60, 1080
        c.new_path(); c.arc(ax, ay, 220, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
        mono(c, "ALVÉOLO", ax, ay - 250, 30, CYAN, p, align="center")
        # capilar contornando por baixo
        cy_ = 1350
        cap_line(c, LEFT + 20, cy_, RIGHT - 20, cy_, PINK, 60, p); cap_line(c, LEFT + 20, cy_, RIGHT - 20, cy_, (0.30, 0.08, 0.14), 44, p)
        for i in range(10):
            f = (t * 0.5 + i / 10) % 1
            ellipse(c, lerp(LEFT + 30, RIGHT - 30, f), cy_, 16, 10, 0, RED, p)
        _mono_right(c, "CAPILAR", RIGHT - 20, cy_ + 70, 26, MUTED, p)
        # algumas hemácias escapam e sobem
        for i in range(4):
            t0 = 0.4 + i * 0.35
            f = clamp((t - t0) / 1.8)
            if f <= 0:
                continue
            x = ax - 90 + i * 60
            y = lerp(cy_ - 30, ay - 120 - (60 * i) % 90, ease(f))
            ellipse(c, x + 10 * math.sin(t * 3 + i), y, 15, 10, 0.3, RED, p)
        chip(c, "SOBE ATÉ A BOCA", CX, 760, PINK, NAVY, 40, ease_out(prog(t, 0.6 * d, 0.3)))


def sg_seca(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        # cabeça de perfil (olhando para a direita) com a boca aberta e o ar entrando rápido
        hx, hy = 330, 1000
        c.new_path(); c.arc(hx, hy, 150, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
        op = 0.35 + 0.1 * math.sin(t * 8)
        c.new_path(); c.move_to(hx + 40, hy + 60); c.line_to(hx + 160, hy + 60 - 70 * op); c.line_to(hx + 160, hy + 60 + 70 * op); c.close_path()
        rgb(c, mix(NAVY, PINK, 0.45), p); c.fill()
        cap_line(c, hx + 40, hy + 60, hx + 40, hy + 220, CYAN, 26, p); cap_line(c, hx + 40, hy + 60, hx + 40, hy + 220, mix(NAVY2, PINK, ease(prog(t, 0.3, d * 0.6))), 16, p)
        mono(c, "GARGANTA", hx + 80, hy + 210, 26, MUTED, p)
        disk(c, hx + 70, hy - 40, 12, CYAN, p)
        for k in range(5):
            f = (t * 2.2 + k / 5) % 1
            yy = hy + 30 + k * 14
            cap_line(c, lerp(RIGHT - 20, hx + 190, f), yy, lerp(RIGHT - 80, hx + 150, f), yy, INK, 4, p * (1 - f))
        _mono_right(c, "AR RÁPIDO PELA BOCA", RIGHT - 20, 860, 28, MUTED, p)
        hum = lerp(0.9, 0.25, ease(prog(t, 0.3, d * 0.6)))
        mono(c, "UMIDADE DA GARGANTA", LEFT + 20, 1340, 28, INK, ease_out(prog(t, 0.2, 0.3)))
        bar_pct(c, LEFT + 20, 1370, RIGHT - LEFT - 40, 44, hum, mix(PINK, CYAN, hum), ease_out(prog(t, 0.2, 0.3)))
        _mono_right(c, f"{int(hum * 100)}%", RIGHT - 20, 1480, 40, mix(PINK, CYAN, hum), ease_out(prog(t, 0.25, 0.3)))


# ================================================================ FOME (fo_)
def fome_meter(c, x, y, val, p, label="FOME"):
    mono(c, label, x, y, 30, INK, p)
    bar_pct(c, x, y + 20, 380, 40, val, PINK, p)
    mono(c, f"{int(val * 100)}%", x + 400, y + 52, 30, PINK, p)


def fo_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        dep = 0.5 + 0.5 * math.sin(t * 3.0 - 1.5)
        squat(c, 260, 1440, 0.66, dep, {"quad": 0.8, "gluteo": 0.6}, t, ease_out(prog(t, 0, 0.3)))
        q = ease_out(prog(t, 0.3, 0.4))
        stomach(c, 760, 960, 0.75, t, q, food=0)
        fome_meter(c, 520, 1240, lerp(0.7, 0.08, ease(prog(t, 0.5, 1.0))), q)
        chip(c, "SUMIU?", 760, 1440, PINK, NAVY, 50, ease_out(prog(t, 1.0, 0.3)))


def fo_grelina(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        stomach(c, 300, 1120, 1.0, t, p)
        n = int(round(10 - 8 * g))
        for k in range(n):
            f = (t * 0.45 + k / 10) % 1
            disk(c, 200 + (k * 53) % 200, 990 - 200 * f, 11, PINK, p * (1 - f))
        mono(c, "GRELINA", 300, 760, 30, PINK, p, align="center")
        mono(c, "HORMÔNIO DA FOME", 560, 900, 28, MUTED, p)
        bar_pct(c, 560, 930, 320, 44, lerp(0.85, 0.2, g), PINK, p)
        draw_text(c, "CAI", 560, 1080, 90, PINK, TITLE, ease_out(prog(t, 0.5 * d, 0.3)))
        # sangue indo para os músculos (seta de pontos para a direita/baixo)
        for i in range(6):
            f = (t * 0.8 + i / 6) % 1
            disk(c, lerp(560, 880, f), lerp(1250, 1400, f), 9, PINK, p)
        _mono_right(c, "SANGUE PROS MÚSCULOS", RIGHT - 10, 1470, 26, INK, ease_out(prog(t, 0.4 * d, 0.3)))


def fo_volta(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.7))
        clock(c, LEFT + 150, 900, 100, g, p)
        mono(c, f"{lerp(0, 2, g):.1f} H".replace(".", ","), LEFT + 300, 915, 44, INK, p)
        stomach(c, 640, 1140, 0.7, t, p)
        if g > 0.5:
            wave_lines(c, 640, 980, t, p * ease(prog(g, 0.5, 0.3)), PINK)
        fome_meter(c, LEFT + 20, 1380, lerp(0.1, 0.9, g), p)


def fo_repoe(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.3, d * 0.6))
        fiber(c, LEFT + 40, 950, 800, 150, p, t=t)
        for i in range(7):
            f = (t * 0.7 + i / 7) % 1
            disk(c, lerp(RIGHT - 30, CX, f), lerp(1400, 1030, f), 10, (0.98, 0.73, 0.10), p * (1 - 0.4 * f))
        mono(c, "ESTOQUE DE ENERGIA", LEFT + 40, 1150, 28, INK, ease_out(prog(t, 0.2, 0.3)))
        bar_pct(c, LEFT + 40, 1180, 520, 50, lerp(0.15, 0.85, g), (0.98, 0.73, 0.10), ease_out(prog(t, 0.2, 0.3)))
        mono(c, "GLICOGÊNIO", LEFT + 40, 1290, 26, MUTED, ease_out(prog(t, 0.3, 0.3)))


# ================================================================ CORAÇÃO (co_)
def co_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        j = squat(c, 280, 1440, 0.74, 0.0, {}, t, p)
        barbell_line(c, 700, 1430, 0.55)
        bpm = lerp(70, 112, ease(prog(t, 0.3, 1.2)))
        heart(c, j["sho"][0] - 10, j["sho"][1] + 60, 0.42, t, bpm, p)
        counter(c, 560, 980, bpm, "BPM", PINK, ease_out(prog(t, 0.2, 0.3)), 140)
        ecg(c, 540, 1080, RIGHT - 560, 40, t, bpm, ease_out(prog(t, 0.3, 0.3)))
        chip(c, "AINDA PARADO", 700, 1180, CYAN, NAVY, 42, ease_out(prog(t, 0.9, 0.3)))


def co_cerebro(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        brain(c, 260, 860, 1.1, glow=0.5 + 0.5 * math.sin(t * 4))
        gx, gy = 700, 1300
        nerve(c, 330, 930, gx - 60, gy - 50, t, ease(prog(t, 0.2, 0.6)))
        ellipse(c, gx, gy, 110, 60, -0.2, NAVY2, p, CYAN)
        ellipse(c, gx - 10, gy - 52, 60, 26, -0.2, mix(NAVY2, PINK, 0.7), p, PINK)
        mono(c, "GLÂNDULA ADRENAL", gx, gy + 110, 26, MUTED, p, align="center")
        q = ease(prog(t, 0.5, 0.6))
        for k in range(8):
            f = (t * 0.5 + k / 8) % 1
            xx = gx - 80 + (k * 37) % 170; yy = gy - 90 - 330 * f
            rrect(c, xx - 9, yy - 9, 18, 18, 4, PINK, q * (1 - f))
        chip(c, "ADRENALINA", gx, 860, PINK, NAVY, 40, ease_out(prog(t, 0.6, 0.3)))
        mono(c, "SABE QUE VEM ESFORÇO", LEFT + 20, 1500, 28, CYAN, ease_out(prog(t, 0.3, 0.3)))


def co_bomba(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.1, d * 0.6))
        bpm = lerp(85, 120, g)
        heart(c, 300, 900, 1.6 + 0.3 * g, t, bpm, p)
        ecg(c, LEFT + 20, 1130, RIGHT - LEFT - 40, 60, t, bpm, p)
        fiber(c, 500, 1340, 380, 110, p, t=t)
        for i in range(8):
            f = (t * lerp(0.5, 1.1, g) + i / 8) % 1
            disk(c, lerp(380, 560, f), lerp(980, 1300, f), 9, PINK, p)
        mono(c, "MÚSCULOS", 690, 1450, 26, MUTED, p, align="center")


def co_prova(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, lab in enumerate(("PROVA", "SÉRIE")):
            q = ease_out(prog(t, 0.05 + i * 0.35, 0.35))
            if q <= 0:
                continue
            x0 = LEFT + 20 + i * 440
            panel(c, x0, 740, 400, 640, q)
            mono(c, lab, x0 + 200, 800, 32, INK, q, align="center")
            if i == 0:                                   # folha de prova com linhas
                rrect(c, x0 + 110, 860, 180, 230, 10, INK, q)
                for k in range(5):
                    cap_line(c, x0 + 135, 900 + k * 38, x0 + 265 - (k % 2) * 40, 900 + k * 38, LINE, 6, q)
            else:
                barbell_line(c, x0 + 200, 980, 0.62)
            heart(c, x0 + 200, 1200, 0.6, t, 110, q)
            mono(c, "110 BPM", x0 + 200, 1330, 30, PINK, q, align="center")
        chip(c, "MESMA RESPOSTA", CX, 1440, PINK, NAVY, 44, ease_out(prog(t, 0.7 * d, 0.3)))


VIS = dict(to_hook=to_hook, to_pressao=to_pressao, to_ar=to_ar, to_corrige=to_corrige,
           sg_hook=sg_hook, sg_pulmao=sg_pulmao, sg_vaza=sg_vaza, sg_seca=sg_seca,
           fo_hook=fo_hook, fo_grelina=fo_grelina, fo_volta=fo_volta, fo_repoe=fo_repoe,
           co_hook=co_hook, co_cerebro=co_cerebro, co_bomba=co_bomba, co_prova=co_prova)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
PRE = {"fibra_14_tontura": "to_", "fibra_15_sangue": "sg_", "fibra_16_fome": "fo_", "fibra_17_coracao": "co_"}
for chave, pre in PRE.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
