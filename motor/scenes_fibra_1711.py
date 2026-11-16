"""FIBRA — produção 17/11: fibras rápidas x lentas (f_) e estalo na articulação (e_). Prancha técnica (build3).
Joelho de perfil (fêmur em cima, tíbia embaixo); a bolha nasce no líquido entre as superfícies quando o espaço abre."""
import math
import random
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA
from scenes_fibra_g import bar_pct, ok_mark, no_mark, molecules
import pauta_1711 as PA

CY = 1080
CX = W / 2 - 40


def mosaic(c, t, x, y, r, frac_fast, p=1.0, grow=0.0, seed=5, hl=None):
    """corte transversal do músculo: círculos ciano (lentas) e rosa (rápidas); grow engrossa as rápidas"""
    rnd = random.Random(seed)
    cells = []
    for i in range(-6, 7):
        for j in range(-6, 7):
            cx_ = x + i * 46 + (23 if j % 2 else 0); cy_ = y + j * 40
            if (cx_ - x) ** 2 + (cy_ - y) ** 2 < r * r:
                cells.append((cx_, cy_, rnd.random()))
    c.new_path(); c.arc(x, y, r + 26, 0, 2 * math.pi); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    for k, (cx_, cy_, u) in enumerate(cells):
        q = clamp(p * 1.6 - k / len(cells) * 0.6)
        if q <= 0:
            continue
        fast = u < frac_fast
        rr = (17 if not fast else 17 + 5 * grow) * q
        if hl == "lenta" and fast or hl == "rapida" and not fast:
            a = 0.25
        else:
            a = 1.0
        disk(c, cx_, cy_, rr, PINK if fast else CYAN, a)


def sprint_icon(c, t, x, y, s, fast, p=1.0):
    """pernas correndo desenhadas em traço (sem figura completa: só o ícone da modalidade)"""
    spd = 9 if fast else 4
    for k in (0, 1):
        a = math.sin(t * spd + k * math.pi) * (0.7 if fast else 0.35)
        hx, hy = x, y
        kx, ky = hx + 70 * s * math.sin(a), hy + 70 * s * math.cos(a)
        fx, fy = kx - 20 * s * math.sin(a - 0.6), ky + 70 * s
        cap_line(c, hx, hy, kx, ky, CYAN if k else MUTED, 8, p); cap_line(c, kx, ky, fx, fy, CYAN if k else MUTED, 8, p)


# ================================================================ FIBRAS (f_)
def f_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        for i, (lab, fr) in enumerate((("VELOCISTA", 0.76), ("MARATONISTA", 0.21))):
            q = ease_out(prog(t, 0.05 + i * 0.3, 0.35))
            x0 = LEFT + 20 + i * 430
            panel(c, x0, 740, 400, 600, q)
            mono(c, lab, x0 + 200, 800, 32, INK, q, align="center")
            mosaic(c, t, x0 + 200, 1080, 135, fr, q, seed=11 + i)
            mono(c, f"{int(fr * 100)}% RÁPIDAS", x0 + 200, 1290, 28, PINK, q, align="center")
        chip(c, "POR QUÊ?", CX, 1420, PINK, NAVY, 48, ease_out(prog(t, 0.7 * d, 0.3)))


def f_tipos(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        mosaic(c, t, CX, 1060, 230, 0.5, ease_out(prog(t, 0, 0.5)), seed=21)
        mono(c, "CORTE DO MÚSCULO", CX, 760, 30, MUTED, ease_out(prog(t, 0.1, 0.3)), align="center")
        chip(c, "LENTA", CX - 180, 1390, CYAN, NAVY, 44, ease_out(prog(t, 0.4 * d, 0.3)))
        chip(c, "RÁPIDA", CX + 180, 1390, PINK, NAVY, 44, ease_out(prog(t, 0.55 * d, 0.3)))


def _tipo(kind):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.06, cy=CY):
            lenta = kind == "lenta"
            fiber(c, LEFT + 60, 880, 760, 110 if lenta else 170, ease_out(prog(t, 0, 0.4)), t=t)
            if lenta:
                chip(c, "USA OXIGÊNIO", CX, 1010, CYAN, NAVY, 40, ease_out(prog(t, 0.2, 0.3)))
            bars = (("FORÇA", 0.25 if lenta else 0.92), ("CRESCIMENTO", 0.2 if lenta else 0.85),
                    ("RESISTÊNCIA", 0.9 if lenta else lerp(0.9, 0.12, ease(prog(t, 0.6, 1.4)))))
            for i, (lab, v) in enumerate(bars):
                q = ease_out(prog(t, 0.2 + i * 0.25, 0.3))
                yy = 1130 + i * 100
                mono(c, lab, LEFT + 60, yy, 30, INK, q)
                bar_pct(c, LEFT + 420, yy - 26, 400, 32, v * q, CYAN if lenta else PINK, q)
            if not lenta:
                clock(c, RIGHT - 110, 1420, 50, (t % 8) / 8, ease_out(prog(t, 0.6, 0.3)))
                _mono_right(c, "CANSA EM SEGUNDOS", RIGHT - 180, 1432, 26, PINK, ease_out(prog(t, 0.9, 0.3)))
    return f


def f_mistura(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, (lab, slow) in enumerate((("VELOCISTA", 0.24), ("MARATONISTA", 0.79))):
            q = ease_out(prog(t, 0.1 + i * 0.4 * d, 0.35))
            if q <= 0:
                continue
            y0 = 800 + i * 300
            mono(c, lab, LEFT + 40, y0, 34, INK, q)
            k = ease(prog(t, 0.2 + i * 0.4 * d, 0.8))
            w = RIGHT - LEFT - 80
            rrect(c, LEFT + 40, y0 + 30, w, 70, 14, PINK, q)
            rrect(c, LEFT + 40, y0 + 30, max(1, w * slow * k), 70, 14, CYAN, q)
            mono(c, f"{int(slow * 100 * k)}% LENTAS", LEFT + 40, y0 + 150, 30, CYAN, q)
            _mono_right(c, f"{int((1 - slow) * 100 * k)}% RÁPIDAS", RIGHT - 40, y0 + 150, 30, PINK, q)
        mono(c, "COSTILL ET AL., 1976", LEFT + 40, 1420, 24, MUTED, ease_out(prog(t, 0.7 * d, 0.3)))


def f_treino(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        g = ease(prog(t, 0.4, d * 0.6))
        mosaic(c, t, CX, 1080, 230, 0.5, 1.0, grow=g, seed=21, hl="rapida")
        mono(c, "TREINO PESADO", CX, 760, 30, MUTED, 1.0, align="center")
        chip(c, "RÁPIDAS CRESCEM", CX, 1400, PINK, NAVY, 44, ease_out(prog(t, 0.5 * d, 0.3)))


# ================================================================ ESTALO (e_)
def knee(c, t, bend, p=1.0, gap=0.0, glow=0.0, x=CX, y=1080):
    """joelho de perfil: fêmur vem de cima, tíbia sai para baixo com o ângulo de flexão 'bend' (graus)"""
    ft = (x - 40, y - 380)
    fk = (x, y)
    a = math.radians(bend)
    tib_dir = (math.sin(a) * -1, math.cos(a))
    tk = (x + tib_dir[0] * (14 + gap), y + 40 + gap)
    tb = (tk[0] + tib_dir[0] * 380, tk[1] + tib_dir[1] * 380)
    # cápsula com líquido
    ellipse(c, x, y + 20 + gap / 2, 110, 70 + gap / 2, 0, mix(NAVY2, CYAN, 0.25 + 0.3 * glow), p, CYAN)
    # fêmur
    cap_line(c, *ft, *fk, INK, 64, p); disk(c, x - 22, y - 6, 48, INK, p); disk(c, x + 26, y - 4, 44, INK, p)
    # tíbia
    cap_line(c, *tk, *tb, INK, 58, p)
    rrect(c, tk[0] - 60, tk[1] - 8, 120, 30, 12, INK, p)
    # patela
    ellipse(c, x + 78, y - 10, 22, 34, 0.3, mix(INK, CYAN, 0.2), p)
    mono(c, "FÊMUR", x + 70, ft[1] + 40, 26, MUTED, p)
    mono(c, "TÍBIA", tb[0] + 70, tb[1] - 30, 26, MUTED, p)
    return (x, y + 20 + gap / 2)


def pop_rings(c, t, x, y, t0, p=1.0):
    for k in range(3):
        f = clamp((t - t0) * 1.6 - k * 0.2)
        if 0 < f < 1:
            c.new_path(); c.arc(x, y, 30 + 160 * f, 0, 2 * math.pi); rgb(c, PINK, (1 - f) * p); c.set_line_width(5); c.stroke()


def e_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        bend = 10 + 70 * (0.5 - 0.5 * math.cos(t * 2.4))
        jx, jy = knee(c, t, bend, ease_out(prog(t, 0, 0.3)))
        ph = (t * 2.4) % (2 * math.pi)
        tc = t - (ph - math.pi) / 2.4 if ph > math.pi else -9
        pop_rings(c, t, jx, jy, tc)
        if 0 < t - tc < 0.5:
            chip(c, "CREC", jx + 230, jy - 160, PINK, NAVY, 54, 1.0)


def e_liquido(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        jx, jy = knee(c, t, 20, 1.0, gap=30, glow=ease(prog(t, 0.2, 0.6)))
        for k in range(5):
            xx = jx - 80 + k * 40 + 6 * math.sin(t * 3 + k)
            disk(c, xx, jy + 4 * math.cos(t * 2 + k), 7, CYAN, 0.8)
        callout(c, jx + 90, jy + 30, CX + 110, 830, "LÍQUIDO SINOVIAL", ease_out(prog(t, 0.3, 0.4)), CYAN, 30)


def e_bolha(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        g = ease(prog(t, 0.2, d * 0.45))
        jx, jy = knee(c, t, 20, 1.0, gap=30 + 40 * g, glow=0.4)
        gauge(c, RIGHT - 170, 1440, 130, g, ease_out(prog(t, 0.1, 0.3)), "PRESSÃO", "ALTA", "BAIXA")
        tb = 0.2 + d * 0.45
        r = 34 * ease_out(prog(t, tb, 0.5))
        popped = t > tb + 0.9
        if r > 0 and not popped:
            c.new_path(); c.arc(jx, jy, r, 0, 2 * math.pi); rgb(c, INK, 0.9); c.set_line_width(4); c.stroke()
        if popped:
            pop_rings(c, t, jx, jy, tb + 0.9)
            chip(c, "POP: É GÁS", jx + 230, jy - 170, PINK, NAVY, 48, ease_out(prog(t, tb + 0.9, 0.3)))


def e_tendao(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        # osso com saliência e tendão (elástico) passando por cima
        bx0, by = LEFT + 80, 1130
        cap_line(c, bx0, by + 60, RIGHT - 80, by + 60, INK, 70)
        disk(c, CX, by + 20, 70, INK)
        u = 0.5 - 0.5 * math.cos(t * 2.2)
        sx = lerp(CX - 120, CX + 120, u)
        snap = abs(sx - CX) < 12
        pts = [(bx0, by - 40), (sx, by - 60 - (40 if abs(sx - CX) < 70 else 0)), (RIGHT - 80, by - 40)]
        poly(c, pts, PINK, 16)
        disk(c, pts[1][0], pts[1][1], 14, PINK)
        mono(c, "TENDÃO", bx0, by - 110, 28, PINK)
        mono(c, "OSSO", bx0, by + 160, 28, MUTED)
        if snap:
            pop_rings(c, t, CX, by - 60, t - 0.05)


def e_normal(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        bend = 8 + 30 * (0.5 - 0.5 * math.cos(t * 2.0))
        knee(c, t, bend, 1.0, x=CX - 120, y=1130)
        ok_mark(c, CX + 260, 900, 70, ease_out(prog(t, 0.3, 0.4)))
        chip(c, "SEM DOR", CX + 260, 1040, CYAN, NAVY, 44, ease_out(prog(t, 0.4, 0.3)))
        chip(c, "COMUM", CX + 260, 1140, CYAN, NAVY, 44, ease_out(prog(t, 0.6, 0.3)))


def e_alerta(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        panel(c, LEFT + 10, 760, RIGHT - LEFT - 20, 560, ease_out(prog(t, 0, 0.3)), PINK)
        mono(c, "SINAIS DE ALERTA", LEFT + 50, 830, 30, PINK, ease_out(prog(t, 0.05, 0.3)))
        for i, s in enumerate(("ESTALO + DOR", "INCHAÇO", "JOELHO TRAVANDO")):
            q = ease_out(prog(t, 0.2 + i * 0.3, 0.3))
            y = 940 + i * 120
            no_mark(c, LEFT + 80, y - 12, 26, q)
            mono(c, s, LEFT + 130, y, 34, INK, q)
        chip(c, "PROCURA AVALIAÇÃO", CX, 1420, PINK, NAVY, 44, ease_out(prog(t, 0.6 * d, 0.3)))


VIS = dict(f_hook=f_hook, f_tipos=f_tipos, f_lenta=_tipo("lenta"), f_rapida=_tipo("rapida"), f_mistura=f_mistura, f_treino=f_treino,
           e_hook=e_hook, e_liquido=e_liquido, e_bolha=e_bolha, e_tendao=e_tendao, e_normal=e_normal, e_alerta=e_alerta)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
for chave, pre in (("fibra_12_fibras", "f_"), ("fibra_13_estalo", "e_")):
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
