"""FIBRA — produção 16/11: músculos do supino (s_) e o músculo cresce no descanso (d_). Estilo prancha técnica (build3)."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, panel, conclusao_factory, cta_flex, SFX_CTA
from scenes_fibra_g import bar_pct, _ik
import pauta_1611 as PA

CY = 1080
FLOOR = 1500
SHX, SHY = 380, 1235          # ombro (atleta deitado, cabeça à esquerda)
HIPX, HIPY = 680, 1250
L_ARM = 135


def bench_press(c, t, u, hl, p=1.0, wobble=0.0):
    """supino de perfil. u 0 = barra no peito, 1 = braço estendido. hl: músculo -> 0..1 (peitoral, ombro, triceps, costas)"""
    # banco
    rrect(c, 250, 1290, 560, 44, 12, NAVY2, p); rrect(c, 250, 1290, 560, 44, 12); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    for x in (300, 760):
        cap_line(c, x, 1334, x, FLOOR, MUTED, 10, p)
    cap_line(c, 200, FLOOR, 900, FLOOR, LINE, 4, p)
    # costas/escápulas apoiadas no banco (atrás do tronco)
    ellipse(c, SHX + 40, 1282, 70, 16, 0, mix(NAVY2, PINK, hl.get("costas", 0)), p, CYAN)
    # pernas: quadril -> joelho -> pé no chão
    kx, ky = 820, 1170
    cap_line(c, HIPX, HIPY, kx, ky, CYAN, 30, p); cap_line(c, HIPX, HIPY, kx, ky, NAVY2, 22, p)
    cap_line(c, kx, ky, 860, FLOOR - 10, CYAN, 26, p); cap_line(c, kx, ky, 860, FLOOR - 10, NAVY2, 18, p)
    cap_line(c, 845, FLOOR - 6, 905, FLOOR - 6, INK, 10, p)
    # tronco deitado
    ellipse(c, (SHX + HIPX) / 2 + 10, 1240, 175, 46, 0.02, NAVY2, p, CYAN)
    # peitoral (em cima do tronco, perto do ombro)
    ellipse(c, SHX + 75, 1203, 72, 26, 0.05, mix(NAVY2, PINK, hl.get("peitoral", 0)), p, CYAN)
    # cabeça
    c.new_path(); c.arc(SHX - 120, 1222, 52, 0, 6.3); rgb(c, NAVY2, p); c.fill_preserve(); rgb(c, CYAN, p); c.set_line_width(3); c.stroke()
    cap_line(c, SHX - 70, 1230, SHX - 20, 1232, CYAN, 18, p)  # pescoço
    # braço: mão sobe na vertical acima do peito/ombro (barra nunca sobre o rosto)
    hx = lerp(SHX + 125, SHX + 15, ease(u)) + wobble * 14 * math.sin(t * 18)  # embaixo: antebraço vertical, cotovelo na altura do banco
    hy = lerp(1150, SHY - 2 * L_ARM + 8, ease(u))
    ex, ey = _ik(SHX, SHY, hx, hy, L_ARM, 1)
    ang = math.atan2(ey - SHY, ex - SHX)
    ellipse(c, (SHX + ex) / 2, (SHY + ey) / 2, L_ARM * 0.5, 30, ang, mix(NAVY2, PINK, hl.get("triceps", 0)), p, CYAN)
    ang2 = math.atan2(hy - ey, hx - ex)
    ellipse(c, (ex + hx) / 2, (ey + hy) / 2, L_ARM * 0.48, 22, ang2, NAVY2, p, CYAN)
    ellipse(c, SHX + 4, SHY - 10, 40, 34, 0, mix(NAVY2, PINK, hl.get("ombro", 0)), p, CYAN)  # deltoide
    for j in ((SHX, SHY), (ex, ey)):
        disk(c, j[0], j[1], 8, INK, p)
    # barra vista de ponta (anilha) na mão
    disk(c, hx, hy, 62, (0.16, 0.22, 0.32), 0.35 * p)
    c.new_path(); c.arc(hx, hy, 62, 0, 6.3); rgb(c, INK, p); c.set_line_width(5); c.stroke()
    disk(c, hx, hy, 14, INK, p)
    return dict(hand=(hx, hy), elbow=(ex, ey), sh=(SHX, SHY))


class Big:
    """amplia o supino 1,2× (figura + marcações juntas)"""
    def __init__(self, c): self.c = c
    def __enter__(self):
        self.c.save(); self.c.translate(510, 1300); self.c.scale(1.2, 1.2); self.c.translate(-550, -1300)
    def __exit__(self, *a): self.c.restore()


def _u(t, spd=2.0):
    return 0.5 - 0.5 * math.cos(t * spd)


ANCH = {"peitoral": lambda j: (SHX + 75, 1200), "ombro": lambda j: (SHX + 4, SHY - 12),
        "triceps": lambda j: ((SHX + j["elbow"][0]) / 2, (SHY + j["elbow"][1]) / 2), "costas": lambda j: (SHX + 40, 1285)}


def s_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY), Big(c):
        k = int(3 * clamp(prog(t, 0.2, d * 0.7)) + 0.0001)
        hl = {m: 1.0 for m in ("peitoral", "ombro", "triceps")[:k]}
        bench_press(c, t, _u(t, 2.4), hl, ease_out(prog(t, 0, 0.3)))
        _mono_right(c, f"MÚSCULOS: {k}", 900, 900, 40, PINK if k else MUTED, ease_out(prog(t, 0.1, 0.3)))


def _sfocus(muscle, label, ly=820):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.06, cy=CY), Big(c):
            g = ease_out(prog(t, 0.1, 0.4))
            j = bench_press(c, t, _u(t, 1.9), {muscle: g})
            px, py = ANCH[muscle](j)
            q = ease_out(prog(t, 0.25, 0.5))
            if q > 0:
                c.new_path(); c.arc(px, py, 44 + 8 * math.sin(t * 6), 0, 6.3); rgb(c, PINK, q); c.set_line_width(4); c.stroke()
            callout(c, px + 40, py - 40, 470, ly, label, q, PINK, 32)
    return f


def s_inclina(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, (lab, ang, v_top, v_omb) in enumerate((("BANCO RETO", 0, 0.5, 0.45), ("INCLINADO 30°", 30, 0.85, 0.7))):
            q = ease_out(prog(t, 0.05 + i * 0.4 * d, 0.35))
            if q <= 0:
                continue
            y0 = 740 + i * 390
            panel(c, LEFT + 10, y0, RIGHT - LEFT - 20, 350, q)
            mono(c, lab, LEFT + 50, y0 + 66, 34, INK, q)
            # banco desenhado no ângulo
            bx, by = LEFT + 70, y0 + 280
            a = math.radians(ang)
            cap_line(c, bx, by, bx + 260 * math.cos(a), by - 260 * math.sin(a), CYAN, 14, q)
            cap_line(c, bx + 40, by, bx + 40, by + 40, MUTED, 8, q); cap_line(c, bx + 200, by - 100 * math.sin(a), bx + 200, by + 40, MUTED, 8, q)
            for j, (m, v) in enumerate((("PEITO DE CIMA", v_top), ("OMBRO", v_omb))):
                yy = y0 + 160 + j * 90
                mono(c, m, LEFT + 380, yy, 26, MUTED, q)
                bar_pct(c, LEFT + 600, yy - 26, 200, 32, v * ease(prog(t, 0.2 + i * 0.4 * d, 0.6)), PINK if i == 1 else LINE, q)


def s_escapula(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY), Big(c):
        loose = 1.0 if (t % 3.0) > 1.6 else 0.0
        j = bench_press(c, t, _u(t, 2.0), {"costas": 1.0 - loose}, 1.0, wobble=loose)
        px, py = ANCH["costas"](j)
        q = ease_out(prog(t, 0.2, 0.4))
        callout(c, px, py, 560, 900, "ESCÁPULAS FIRMES", q * (1 - loose), CYAN, 30)
        if loose:
            chip(c, "SEM APOIO: BARRA BALANÇA", 560, 900, PINK, NAVY, 38, 1.0)


# ================================================================ DESCANSO (d_)
def d_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        fiber(c, LEFT + 60, 1000, 760, 150, ease_out(prog(t, 0, 0.4)), tears=prog(t, 0.3, 1.0), t=t)
        mono(c, "DURANTE O TREINO", LEFT + 60, 860, 32, MUTED, ease_out(prog(t, 0.1, 0.3)))
        mono(c, "TAMANHO", LEFT + 60, 1210, 30, MUTED, ease_out(prog(t, 0.2, 0.3)))
        bar_pct(c, LEFT + 260, 1184, 520, 34, 0.5, LINE, ease_out(prog(t, 0.2, 0.3)))
        chip(c, "+0%", LEFT + 870, 1200, PINK, NAVY, 40, ease_out(prog(t, 0.5, 0.3)))


def d_treino(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        fiber(c, LEFT + 60, 930, 760, 150, 1.0, acid=0.3 * prog(t, 0.2, 1.0), tears=prog(t, 0.2, 1.4), t=t)
        for i, (lab, v) in enumerate((("TENSÃO", 0.9), ("ENERGIA", lerp(0.9, 0.25, ease(prog(t, 0.3, d * 0.7)))), ("MICROLESÕES", 0.6 * ease(prog(t, 0.6, 1.0))))):
            q = ease_out(prog(t, 0.15 + i * 0.25, 0.3))
            yy = 1150 + i * 100
            mono(c, lab, LEFT + 60, yy, 30, INK, q)
            bar_pct(c, LEFT + 420, yy - 26, 400, 32, v, PINK if i != 1 else CYAN, q)


def d_sinal(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        fiber(c, LEFT + 60, 1250, 760, 140, 1.0, tears=1.0, t=t)
        cx, cy = W / 2 - 40, 900
        c.new_path(); c.arc(cx, cy, 90, 0, 6.3); rgb(c, NAVY2); c.fill_preserve(); rgb(c, CYAN); c.set_line_width(3); c.stroke()
        mono(c, "CORPO", cx, cy + 12, 32, INK, align="center")
        for k in range(3):
            f = (t * 0.9 + k / 3) % 1
            r = 60 + 220 * f
            c.new_path(); c.arc(cx, 1250, r, math.pi * 1.15, math.pi * 1.85); rgb(c, PINK, 1 - f); c.set_line_width(5); c.stroke()
        chip(c, "AVISO: FOI PESADO", cx, 1450, PINK, NAVY, 40, ease_out(prog(t, 0.5, 0.35)))


def d_obra(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        x0, y0, w, h = LEFT + 90, 1380, 720, 480
        p = ease_out(prog(t, 0, 0.3))
        cap_line(c, x0, y0, x0 + w, y0, INK, 3, p); cap_line(c, x0, y0, x0, y0 - h, INK, 3, p)
        mono(c, "FABRICAÇÃO DE PROTEÍNA", x0, y0 - h - 24, 28, MUTED, p)
        for hh, lab in ((0, "0 H"), (24, "24 H"), (48, "48 H")):
            xx = x0 + w * hh / 48
            cap_line(c, xx, y0, xx, y0 + 14, INK, 3, p)
            mono(c, lab, xx, y0 + 52, 28, INK, p, align="center")
        q = ease_out(prog(t, 0.3, d * 0.6))
        pts = []
        for i in range(int(60 * q) + 1):
            f = i / 60
            hrs = 48 * f
            v = 0.15 + 0.75 * math.exp(-((hrs - 22) / 14) ** 2)
            pts.append((x0 + w * f, y0 - h * v))
        if len(pts) > 1:
            poly(c, pts, PINK, 6)
            disk(c, pts[-1][0], pts[-1][1], 12, PINK)
        dline(c, x0, y0 - h * 0.15, x0 + w, y0 - h * 0.15, MUTED, 2, (6, 8), p)
        mono(c, "REPOUSO", x0 + w - 4, y0 - h * 0.15 - 14, 24, MUTED, p * 0.9, align="right") if False else \
            _mono_right(c, "REPOUSO", x0 + w - 4, y0 - h * 0.15 - 14, 24, MUTED, p * 0.9)


def d_grossa(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        g = ease(prog(t, 0.3, d * 0.6))
        fiber(c, LEFT + 60, 1050, 760, lerp(140, 190, g), 1.0, tears=1 - g, t=t)
        mono(c, "ANTES", LEFT + 60, 860, 30, MUTED)
        dline(c, LEFT + 60, 1050 - 70, LEFT + 820, 1050 - 70, MUTED, 2, (6, 8))
        chip(c, "REFORÇADA", W / 2 - 40, 1300, CYAN, NAVY, 44, ease_out(prog(t, 0.6 * d, 0.3)))


def d_precisa(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i, lab in enumerate(("PROTEÍNA", "SONO")):
            q = ease_out(prog(t, 0.1 + i * 0.4, 0.35))
            if q <= 0:
                continue
            x0 = LEFT + 20 + i * 430
            panel(c, x0, 760, 400, 520, q)
            mono(c, lab, x0 + 200, 830, 36, INK, q, align="center")
            if i == 0:  # cadeia de aminoácidos se encaixando
                for k in range(6):
                    kx = x0 + 70 + k * 52; ky = 1030 + 26 * math.sin(k * 1.3 + t * 2)
                    disk(c, kx, ky, 22, PINK if k % 2 else CYAN, q)
                    if k:
                        cap_line(c, kx - 52, 1030 + 26 * math.sin((k - 1) * 1.3 + t * 2), kx, ky, INK, 4, q * 0.7)
            else:  # lua desenhada
                mx, my = x0 + 200, 1030
                disk(c, mx, my, 90, INK, q); disk(c, mx + 40, my - 30, 82, NAVY2, q)
                for k in range(3):
                    a = 0.4 + 0.6 * abs(math.sin(t * 3 + k * 2))
                    sx, sy = x0 + 80 + k * 110, 1190
                    cap_line(c, sx - 10, sy, sx + 10, sy, CYAN, 4, a * q); cap_line(c, sx, sy - 10, sx, sy + 10, CYAN, 4, a * q)


VIS = dict(
    s_hook=s_hook, s_peitoral=_sfocus("peitoral", "PEITORAL MAIOR"), s_ombro=_sfocus("ombro", "DELTOIDE ANTERIOR", 780),
    s_triceps=_sfocus("triceps", "TRÍCEPS"), s_inclina=s_inclina, s_escapula=s_escapula,
    d_hook=d_hook, d_treino=d_treino, d_sinal=d_sinal, d_obra=d_obra, d_grossa=d_grossa, d_precisa=d_precisa,
)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
for chave, pre in (("fibra_10_supino", "s_"), ("fibra_11_descanso", "d_")):
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
