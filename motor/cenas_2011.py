"""Extensões do kit v2 para o lote de 20/11 (BRIO 75–78): supino de lado no padrão v2, camiseta que aperta,
balão de conversa, curva de pico hormonal, medidor de amplitude. Sem glifos fora da fonte (use check_mark/x_mark)."""
from cenas_1711 import *
from scenes_brio_18 import bench_lifter


def act_bench(c, t, x=70, s=0.9, spd=2.2, y=None):
    """supino visto de lado (uma figura). Subida rápida, descida controlada. A barra fica sobre o peito/ombros."""
    ph = (t * spd / (2 * math.pi)) % 1
    u = ease(ph / 0.35) if ph < 0.35 else 1 - ease((ph - 0.35) / 0.65)
    return bench_lifter(c, x, FLOOR_Y if y is None else y, s, u)


def mini_bench(c, t, cx, base_y, s=0.45, spd=2.2):
    act_bench(c, t, cx - 280 * s, s, spd, base_y)


def tshirt(c, t, x, y, s=1.0, k=0.0, p=1.0, col=None):
    """camiseta de frente; k 0..1 = quanto aperta (ombros/braços alargam, linhas de tensão)"""
    if p <= 0:
        return
    col = col or BLU
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    w = 150 + 40 * k; sl = 120 + 30 * k
    pts = [(-w, -150), (-w - sl, -60), (-w - sl + 60, 10), (-w + 10, -40), (-w + 10, 170), (w - 10, 170), (w - 10, -40),
           (w + sl - 60, 10), (w + sl, -60), (w, -150), (50, -150), (0, -110), (-50, -150)]
    c.new_path(); c.move_to(*pts[0])
    for q in pts[1:]:
        c.line_to(*q)
    c.close_path(); rgb(c, col); c.fill_preserve(); rgb(c, INK); c.set_line_width(6); c.stroke()
    for i in range(3):  # linhas de tensão nos ombros e nas mangas
        a = k * (0.6 + 0.4 * math.sin(t * 6 + i))
        for sd in (-1, 1):
            cap_line(c, sd * (w - 30 - i * 26), -120 + i * 22, sd * (w + 30 - i * 10), -70 + i * 26, WHITE, 5, a)
    c.restore()


def bubble(c, x, y, txt, p=1.0, col=WHITE, fg=INK, size=48, tail=-1):
    """balão de conversa com rabinho (tail -1 = esquerda, 1 = direita)"""
    if p <= 0:
        return
    pop(c, x, y, p)
    font(c, "Anton", size); w = c.text_extents(txt).x_advance + 60; h = size * 1.7
    rrect(c, -w / 2, -h / 2, w, h, 30, col)
    poly(c, [(tail * w * 0.25, h / 2 - 2), (tail * w * 0.38, h / 2 + 34), (tail * w * 0.05, h / 2 - 2)], col, 0)
    c.new_path(); c.move_to(tail * w * 0.25, h / 2 - 4); c.line_to(tail * w * 0.38, h / 2 + 34); c.line_to(tail * w * 0.05, h / 2 - 4)
    c.close_path(); rgb(c, col); c.fill()
    label(c, txt, 0, size * 0.38, fg, size)
    c.restore()


def spike(c, t, x, y, w, h, p=1.0, col=None):
    """curva de hormônio: sobe rápido e volta ao normal (eixo em y+h)"""
    if p <= 0:
        return
    col = col or YEL
    n = 40; k = max(2, int(n * ease_out(p)))
    pts = []
    for i in range(k):
        u = i / (n - 1)
        v = (u / 0.18) if u < 0.18 else math.exp(-(u - 0.18) * 7)
        pts.append((x + u * w, y + h - 0.15 * h - 0.8 * h * v))
    cap_line(c, x, y + h, x + w, y + h, WHITE, 4, 0.3)
    poly(c, pts, col, 10)


def angle_gauge(c, t, x, y, r, frac, p=1.0, ok=False):
    """arco de amplitude: frac 0..1 do movimento (0 = em pé, 1 = embaixo)"""
    if p <= 0:
        return
    c.new_path(); c.arc(x, y, r, math.pi, 2 * math.pi); rgb(c, CARD, p); c.set_line_width(34); c.stroke()
    c.new_path(); c.arc(x, y, r, math.pi, math.pi + math.pi * clamp(frac)); rgb(c, GRN if ok else YEL, p); c.set_line_width(34); c.stroke()
    a = math.pi + math.pi * clamp(frac)
    disk(c, x + r * math.cos(a), y + r * math.sin(a), 26, WHITE, p)


def flex_band(c, t, x, y, stretch, w=420):
    """elástico verde (amplitude): quanto mais estica, melhor"""
    L = w * (0.55 + 0.45 * stretch)
    disk(c, x - L / 2, y, 30, STEEL); disk(c, x + L / 2, y, 30, STEEL)
    th = 46 * (1 - 0.5 * stretch)
    rrect(c, x - L / 2, y - th / 2, L, th, th / 2, mix(GREY, GRN, 0.3 + 0.7 * stretch))
