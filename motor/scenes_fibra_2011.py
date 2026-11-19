"""FIBRA — produção 20/11 (prancha técnica, build3): euforia depois do treino (eu_), começo da corrida/fôlego (fl_),
cansaço do treino de perna (ca_), mãos inchadas na caminhada (ma_). Uma figura por cena; nada atravessa o corpo;
só glifos da fonte (sem ✓ ✦ ↑ — marcas desenhadas)."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA, squat
from scenes_fibra_g import bar_pct, ok_mark, no_mark
from scenes_fibra_1811 import counter, heart, ecg, lungs, wave_lines
from scenes_fibra_1911 import runner, treadmill, vessel_wide, thermo, CX, CY, RED, ORANGE
import pauta_2011 as PA

GLY = (0.98, 0.80, 0.30)


# ------------------------------------------------------------------ peças
def rings(c, x, y, r, t, k, p=1.0, col=CYAN):
    for i in range(3):
        f = (t * 0.9 + i / 3) % 1
        c.new_path(); c.arc(x, y, r + 110 * f, 0, 6.3); rgb(c, col, p * k * (1 - f) * 0.8); c.set_line_width(5); c.stroke()


def barrier(c, x0, x1, y, p=1.0):
    """barreira hematoencefálica: parede de células (tijolinhos) com frestas pequenas"""
    n = 9; w = (x1 - x0) / n
    for i in range(n):
        rrect(c, x0 + i * w + 4, y - 22, w - 8, 44, 12, NAVY2, p)
        rrect(c, x0 + i * w + 4, y - 22, w - 8, 44, 12); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()


def hand(c, x, y, s, k=0.0, p=1.0, fill=0.0):
    """mão aberta de frente (palma); k 0..1 = inchaço (dedos engrossam); fill 0..1 = sangue acumulado (rosa)"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s, s)
    body = mix(NAVY2, (0.42, 0.14, 0.24), fill)
    fw = 46 + 22 * k
    for i, (dx, L) in enumerate(((-90, 190), (-30, 220), (30, 210), (90, 170))):
        cap_line(c, dx, -60, dx * 1.08, -60 - L, CYAN, fw + 8, p); cap_line(c, dx, -60, dx * 1.08, -60 - L, body, fw, p)
    cap_line(c, -120, 60, -210, -40, CYAN, fw + 8, p); cap_line(c, -120, 60, -210, -40, body, fw, p)   # polegar
    rrect(c, -130 - 8 * k, -90, 260 + 16 * k, 260, 70, body, p)
    rrect(c, -130 - 8 * k, -90, 260 + 16 * k, 260, 70); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
    cap_line(c, -60, 170, -60, 300, CYAN, 5, p); cap_line(c, 60, 170, 60, 300, CYAN, 5, p)          # punho
    c.restore()


def o2_chart(c, t, x, y, w, h, prog_x, p=1.0, shade=0.0):
    """pedido de oxigênio (degrau, rosa tracejado) x entrega (curva subindo, ciano); shade = déficit preenchido"""
    if p <= 0:
        return
    cap_line(c, x, y + h, x + w, y + h, LINE, 3, p); cap_line(c, x, y, x, y + h, LINE, 3, p)
    top = y + h * 0.2
    dline(c, x, top, x + w, top, PINK, 4, (14, 10), p)
    n = 50; k = max(2, int(n * clamp(prog_x)))
    pts = [(x + w * i / (n - 1), y + h - (h * 0.8) * (1 - math.exp(-(i / (n - 1)) * 5))) for i in range(n)]
    if shade > 0:
        c.new_path(); c.move_to(x, top)
        for (px, py) in pts:
            c.line_to(px, py)
        c.line_to(x + w, top); c.close_path(); rgb(c, PINK, 0.35 * shade * p); c.fill()
    poly(c, pts[:k], CYAN, 8, p)
    mono(c, "PEDIDO", x + w - 160, top - 22, 26, PINK, p)
    mono(c, "ENTREGA", x + 20, y + h - 30, 26, CYAN, p)
    mono(c, "0", x - 10, y + h + 44, 26, MUTED, p)
    _mono_right(c, "3 MIN", x + w + 10, y + h + 44, 26, MUTED, p)


# ================================================================ EUFORIA (eu_)
def eu_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.3, 0.9))
        treadmill(c, 110, 620, 1500, t, p)
        j = runner(c, 330, 1120, 1.0, t, p, lerp(7.0, 4.5, k))
        rings(c, j["head"][0], j["head"][1], 60, t, k, p)
        chip(c, "SENSAÇÃO BOA", 790, 1000, CYAN, NAVY, 46, ease_out(prog(t, 0.9, 0.3)))


def _bbb(c, t, p):
    panel(c, LEFT + 10, 730, RIGHT - LEFT - 20, 760, p)
    vessel_wide(c, LEFT + 50, RIGHT - 50, 1390, 60, t, 0.5, p)
    mono(c, "SANGUE", LEFT + 50, 1470, 26, MUTED, p)
    barrier(c, LEFT + 40, RIGHT - 40, 1200, p)
    _mono_right(c, "BARREIRA", RIGHT - 40, 1160, 26, CYAN, p)


def eu_barreira(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        _bbb(c, t, p)
        brain(c, CX, 900, 0.9, glow=0.1)
        for i in range(4):                               # endorfina: grande, bate e volta
            f = (t * 0.8 + i / 4) % 1
            yy = 1350 - 110 * math.sin(f * math.pi)
            disk(c, LEFT + 150 + i * 190, yy, 34, PINK, p * 0.9)
            mono(c, "END", LEFT + 150 + i * 190, yy + 10, 22, NAVY, p, align="center")
        chip(c, "NÃO PASSA", 790, 1060, PINK, NAVY, 44, ease_out(prog(t, 0.5 * d, 0.3)))


def eu_endo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.3, d * 0.6))
        _bbb(c, t, p)
        brain(c, CX, 900, 0.9, glow=0.75 * g * (0.8 + 0.2 * math.sin(t * 5)))
        rnd = random.Random(4)
        for i in range(8):                               # endocanabinoides: pequenos, atravessam até o cérebro
            f = (t * 0.55 + rnd.random()) % 1
            x0 = LEFT + 110 + i * 95
            disk(c, lerp(x0, CX + rnd.uniform(-80, 80), f * f), lerp(1370, 920, f), 13, GOOD, p * (1 - 0.6 * f))
        chip(c, "ENDOCANABINOIDES", 650, 1060, GOOD, NAVY, 38, ease_out(prog(t, 0.45 * d, 0.3)))


def eu_estudo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.45))
        mono(c, "NUM ESTUDO", LEFT + 20, 790, 30, MUTED, p)
        mono(c, "ENDORFINA", LEFT + 20, 900, 32, PINK, p)
        bar_pct(c, LEFT + 20, 930, RIGHT - LEFT - 140, 54, lerp(0.85, 0.05, g), PINK, p)
        no_mark(c, RIGHT - 50, 957, 26, ease_out(prog(t, 0.5 * d, 0.3)))
        mono(c, "EUFORIA", LEFT + 20, 1090, 32, GOOD, p)
        bar_pct(c, LEFT + 20, 1120, RIGHT - LEFT - 140, 54, 0.85 + 0.03 * math.sin(t * 4), GOOD, p)
        ok_mark(c, RIGHT - 50, 1147, 26, ease_out(prog(t, 0.65 * d, 0.3)), GOOD)
        chip(c, "BLOQUEADA", CX, 1330, PINK, NAVY, 44, ease_out(prog(t, 0.35 * d, 0.3)))
        chip(c, "E A EUFORIA FICOU", CX, 1450, GOOD, NAVY, 44, ease_out(prog(t, 0.6 * d, 0.3)))


# ================================================================ FÔLEGO (fl_)
def fl_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.3, 0.8))
        treadmill(c, 110, 620, 1500, t, p)
        j = runner(c, 330, 1120, 1.0, t, p, 7.0)
        wave_lines(c, j["head"][0] + 120, j["head"][1] - 10, t, p * k, PINK, 3, 120)
        s = int(lerp(0, 59, prog(t, 0.2, max(d - 0.3, 0.5))))
        draw_text(c, f"0:{s:02d}", 790, 900, 110, INK, TITLE, p, align="center")
        chip(c, "OFEGANTE", 790, 1030, PINK, NAVY, 48, ease_out(prog(t, 0.9, 0.3)))


def fl_motor(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        mono(c, "OXIGÊNIO NO MÚSCULO", LEFT + 20, 790, 30, INK, p)
        o2_chart(c, t, LEFT + 60, 880, RIGHT - LEFT - 120, 420, prog(t, 0.2, d * 0.7), p)
        chip(c, "DEMORA A LIGAR", CX, 1450, CYAN, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


def fl_deficit(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        mono(c, "OXIGÊNIO NO MÚSCULO", LEFT + 20, 790, 30, INK, p)
        o2_chart(c, t, LEFT + 60, 880, RIGHT - LEFT - 120, 420, 1.0, p, ease(prog(t, 0.2, d * 0.5)))
        chip(c, "FALTA OXIGÊNIO", CX, 1390, PINK, NAVY, 40, ease_out(prog(t, 0.4 * d, 0.3)))
        chip(c, "2 A 3 MIN", CX, 1490, PINK, NAVY, 52, ease_out(prog(t, 0.55 * d, 0.3)))


def fl_reserva(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        mono(c, "RESERVA RÁPIDA", LEFT + 20, 790, 30, GLY, p)
        bar_pct(c, LEFT + 20, 820, 420, 54, lerp(0.95, 0.25, g), GLY, p)
        lungs(c, 330, 1260, 0.95, p, glow=g, t=t * (1 + 2 * g))
        mono(c, "RESPIRAÇÃO", 760, 1080, 28, MUTED, p, align="center")
        counter(c, 640, 1240, lerp(14, 40, g), "/MIN", PINK, p, 150)
        chip(c, "CANSA", 760, 1420, PINK, NAVY, 50, ease_out(prog(t, 0.5 * d, 0.3)))


# ================================================================ CANSAÇO (ca_)
def ca_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.2, 1.2))
        dep = 0.5 + 0.5 * math.sin(t * lerp(2.4, 1.4, k) - 1.5)
        j = squat(c, 330, 1440, 0.72, dep, {"quad": 0.8, "gluteo": 0.8}, t, p)
        mono(c, "ENERGIA", 780, 840, 28, MUTED, p, align="center")
        bar_pct(c, 640, 870, 280, 50, lerp(0.95, 0.15, k), mix(GOOD, PINK, k), p)
        chip(c, "EXAUSTO", 780, 1060, PINK, NAVY, 54, ease_out(prog(t, 0.9, 0.3)))


def ca_metade(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.15, d * 0.5))
        mono(c, "MÚSCULO DO CORPO", LEFT + 20, 790, 30, INK, p)
        x0, w0 = LEFT + 20, RIGHT - LEFT - 40
        rrect(c, x0, 830, w0, 70, 35, NAVY2, p)
        rrect(c, x0, 830, max(70, w0 * 0.55 * g), 70, 35, PINK, p)
        mono(c, "PERNA + GLÚTEO", x0, 950, 28, PINK, p)
        _mono_right(c, "RESTO", x0 + w0, 950, 28, MUTED, p)
        counter(c, x0, 1150, 55 * g, "%", PINK, p, 170)
        squat(c, 760, 1470, 0.42, 0.5 + 0.5 * math.sin(t * 2.4), {"quad": g, "gluteo": g, "adutor": g}, t, p)


def ca_coracao(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.15, d * 0.6))
        bpm = lerp(80, 160, g)
        heart(c, LEFT + 170, 960, 2.2, t, bpm, p)
        counter(c, LEFT + 330, 1010, bpm, "BPM", PINK, p, 140)
        ecg(c, LEFT + 20, 1220, RIGHT - LEFT - 40, 80, t, bpm, p)
        for i in range(10):                              # sangue indo para as pernas (para baixo)
            f = (t * 0.9 + i / 10) % 1
            disk(c, LEFT + 60 + i * 80, lerp(1300, 1470, f), 10, PINK, p * (1 - f))
        mono(c, "MAIS SANGUE PRA PERNA", LEFT + 20, 1520, 28, MUTED, p)


def ca_estoque(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        fiber(c, LEFT + 20, 1000, RIGHT - LEFT - 40, 200, p, t=t)
        n = 12
        for i in range(n):                               # grãos de glicogênio sumindo
            q = 1 - ease(prog(g, i / n * 0.9, 0.12))
            disk(c, LEFT + 90 + i * 66, 1000 + (24 if i % 2 else -24), 20 * q, GLY, p)
        mono(c, "ENERGIA GUARDADA", LEFT + 20, 1180, 28, GLY, p)
        bar_pct(c, LEFT + 20, 1210, RIGHT - LEFT - 40, 50, lerp(0.95, 0.2, g), GLY, p)
        chip(c, "ENERGIA BAIXA", CX, 1420, PINK, NAVY, 48, ease_out(prog(t, 0.55 * d, 0.3)))


# ================================================================ MÃOS (ma_)
def ma_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        k = ease(prog(t, 0.3, 1.2))
        hand(c, CX, 1180, 1.25, k, p, 0.5 * k)
        rings(c, CX, 1050, 220, t, k, p, PINK)
        chip(c, "INCHOU?", CX, 1500, PINK, NAVY, 54, ease_out(prog(t, 0.9, 0.3)))


def ma_comum(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        cap_line(c, 110, 1500, 640, 1500, LINE, 6, p)
        j = runner(c, 330, 1130, 1.0, t, p, 3.6, lean=0.03)
        chip(c, "É COMUM", 790, 900, CYAN, NAVY, 50, ease_out(prog(t, 0.3, 0.3)))
        chip(c, "BALANÇO DO BRAÇO", 760, 1040, PINK, NAVY, 40, ease_out(prog(t, 0.45 * d, 0.3)))


def ma_balanco(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.7))
        sx, sy, L = 340, 820, 500
        a = 0.42 * math.sin(t * 3.2)
        hx, hy = sx + L * math.sin(a), sy + L * math.cos(a)
        c.new_path(); c.arc(sx, sy, L, math.pi / 2 - 0.45, math.pi / 2 + 0.45); rgb(c, LINE, p); c.set_line_width(3); c.stroke()
        disk(c, sx, sy, 22, INK, p)
        cap_line(c, sx, sy, hx, hy, INK, 26, p)
        for i in range(6):                               # sangue jogado para a ponta
            f = (t * 1.3 + i / 6) % 1
            disk(c, lerp(sx, hx, f), lerp(sy, hy, f), 10, PINK, p)
        disk(c, hx, hy, lerp(40, 62, g), mix(NAVY2, PINK, g), p)
        c.new_path(); c.arc(hx, hy, lerp(40, 62, g), 0, 6.3); rgb(c, CYAN, p); c.set_line_width(4); c.stroke()
        for i in range(3):                               # volta devagar
            f = (t * 0.25 + i / 3) % 1
            disk(c, 760, lerp(1380, 900, f), 10, CYAN, p * (1 - f))
        cap_line(c, 760, 1400, 760, 880, LINE, 3, p)
        mono(c, "VOLTA DEVAGAR", 760, 1460, 28, CYAN, p, align="center")
        mono(c, "PONTA DOS DEDOS", sx, 1470, 28, PINK, ease_out(prog(t, 0.3 * d, 0.3)), align="center")


def ma_calor(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        g = ease(prog(t, 0.2, d * 0.6))
        thermo(c, LEFT + 90, 1300, lerp(0.3, 0.9, g), p)
        mono(c, "CALOR", LEFT + 45, 1410, 28, ORANGE, p)
        hand(c, 660, 1180, 0.95, 0.3 + 0.6 * g, p, 0.3 + 0.5 * g)
        chip(c, "VASOS SE ABREM", 650, 800, PINK, NAVY, 40, ease_out(prog(t, 0.3 * d, 0.3)))
        chip(c, "INCHA MAIS", 650, 1520, PINK, NAVY, 46, ease_out(prog(t, 0.55 * d, 0.3)))


VIS = dict(eu_hook=eu_hook, eu_barreira=eu_barreira, eu_endo=eu_endo, eu_estudo=eu_estudo,
           fl_hook=fl_hook, fl_motor=fl_motor, fl_deficit=fl_deficit, fl_reserva=fl_reserva,
           ca_hook=ca_hook, ca_metade=ca_metade, ca_coracao=ca_coracao, ca_estoque=ca_estoque,
           ma_hook=ma_hook, ma_comum=ma_comum, ma_balanco=ma_balanco, ma_calor=ma_calor)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
PRE = {"fibra_22_euforia": "eu_", "fibra_23_folego": "fl_", "fibra_24_cansaco": "ca_", "fibra_25_maos": "ma_"}
for chave, pre in PRE.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
