"""Extensões do kit v2 para o lote de 17/11: copo de cerveja, ovo, coxa de frango, cadeia de aminoácidos, tronco com
abdômen sob a gordura, cubos de volume (músculo x gordura), gota d'água, anel do ciclo de 28 dias, núcleos na fibra.
Sem glifos fora da fonte (nada de ✓ ✦ — use check_mark/x_mark)."""
from cenas_1611 import *

BEER = (0.98, 0.72, 0.18)
FOAM = (0.98, 0.97, 0.93)
SKIN = (0.93, 0.76, 0.62)
AMINO = ((0.93, 0.27, 0.29), (0.98, 0.73, 0.10), (0.24, 0.75, 0.42), (0.35, 0.72, 1.0), (0.75, 0.5, 0.95),
         (0.98, 0.5, 0.2), (0.4, 0.9, 0.85), (0.95, 0.45, 0.7), (0.7, 0.75, 0.3))


def beer(c, t, x, y, s=1.0, p=1.0, level=1.0):
    """copo de cerveja (caneca) com espuma e bolhas subindo"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    c.new_path(); c.arc(105, -10, 50, -1.3, 1.3); rgb(c, (0.85, 0.88, 0.92)); c.set_line_width(20); c.stroke()
    rrect(c, -100, -150, 200, 260, 26, (0.85, 0.88, 0.92), 0.35)
    h = 230 * level
    rrect(c, -88, 98 - h, 176, h, 18, BEER)
    for k in range(4):
        f = (t * 0.8 + k / 4) % 1
        disk(c, -50 + k * 32, 90 - (h - 30) * f, 7, FOAM, 0.7 * (1 - f))
    if level > 0.2:
        for k in range(5):
            disk(c, -76 + k * 38, 98 - h, 30, FOAM)
    c.restore()


def egg(c, x, y, s=1.0, p=1.0):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001) * 0.82, s * max(p, .001)); disk(c, 0, 0, 60, FOAM); c.restore()


def chicken(c, x, y, s=1.0, p=1.0):
    """filé de frango (forma oval dourada com marcas de grelha)"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -110, -55, 220, 110, 55, (0.86, 0.62, 0.36))
    for k in range(3):
        cap_line(c, -60 + k * 50, -40, -20 + k * 50, 40, (0.55, 0.35, 0.18), 8)
    c.restore()


def amino_chain(c, t, x, y, n, total=9, gap=70, p=1.0, broken_at=None):
    """cadeia de aminoácidos (bolinhas coloridas ligadas); mostra n de total, as que faltam ficam como encaixe vazio"""
    x0 = x - (total - 1) * gap / 2
    for i in range(total):
        q = back_out(prog(p, i / total * 0.6, 0.4)) if p < 1 else 1.0
        xx = x0 + i * gap; yy = y + 14 * math.sin(i * 1.1 + t * 2.4)
        if i and i < n:
            px_ = x0 + (i - 1) * gap; py_ = y + 14 * math.sin((i - 1) * 1.1 + t * 2.4)
            cap_line(c, px_, py_, xx, yy, WHITE, 6, 0.7 * q)
        if i < n:
            disk(c, xx, yy, 26 * q, AMINO[i % len(AMINO)])
        else:
            c.new_path(); c.arc(xx, yy, 24, 0, 2 * math.pi); rgb(c, GREY, 0.7); c.set_line_width(4); c.stroke()


def torso_abs(c, t, x, y, fat=1.0, p=1.0, thick=1.0):
    """tronco de frente: gomos do abdômen (sempre lá) e a camada de gordura por cima (fat 0..1 = opacidade/volume)"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))
    w = 300 + 70 * fat
    rrect(c, -40, -330, 80, 90, 30, SKIN)                      # pescoço
    rrect(c, -w / 2 - 70, -290, w + 140, 120, 60, SKIN)          # ombros
    rrect(c, -w / 2, -260, w, 520, 120, SKIN)
    for sd in (-1, 1):                                          # peitoral
        rrect(c, sd * 75 - 70, -245, 140, 70, 30, mix(SKIN, (0.72, 0.5, 0.38), 0.35))
    for r in range(3):
        for sd in (-1, 1):
            bw, bh = 86 * thick, 96 * thick
            rrect(c, sd * 52 - bw / 2, -170 + r * 118 - bh / 2 + 40, bw, bh, 30, mix(SKIN, (0.72, 0.5, 0.38), 0.6))
    cap_line(c, 0, -190, 0, 170, (0.72, 0.5, 0.38), 6)
    if fat > 0:
        rrect(c, -w / 2 - 4, -264, w + 8, 528, 124, (0.96, 0.82, 0.68), fat)
        c.new_path(); c.arc(0, 200, 10, 0, 2 * math.pi); rgb(c, (0.6, 0.42, 0.32), fat); c.fill()
    c.restore()


def cube(c, x, y, a, col, txt, p=1.0, sub=None):
    """cubo em perspectiva simples (lado a), base em y"""
    if p <= 0:
        return
    a = a * ease_out(p)
    d = a * 0.32
    rrect(c, x - a / 2, y - a, a, a, 10, col)
    c.new_path(); c.move_to(x - a / 2, y - a); c.line_to(x - a / 2 + d, y - a - d); c.line_to(x + a / 2 + d, y - a - d); c.line_to(x + a / 2, y - a); c.close_path()
    rgb(c, mix(col, WHITE, 0.3)); c.fill()
    c.new_path(); c.move_to(x + a / 2, y - a); c.line_to(x + a / 2 + d, y - a - d); c.line_to(x + a / 2 + d, y - d); c.line_to(x + a / 2, y); c.close_path()
    rgb(c, mix(col, INK, 0.3)); c.fill()
    if p > 0.6:
        draw_text(c, txt, x, y - a / 2 + 22, 56, INK, "Anton", min(1, (p - 0.6) * 3), align="center")
    if sub and p > 0.6:
        draw_text(c, sub, x + d / 2, y + 56, 36, GREY, "Space Mono", min(1, (p - 0.6) * 3), align="center", spacing=1)


def droplet(c, x, y, s=1.0, a=1.0, col=None):
    col = col or BLU
    c.new_path(); c.move_to(x, y - 40 * s); c.curve_to(x + 30 * s, y - 5 * s, x + 30 * s, y + 25 * s, x, y + 28 * s)
    c.curve_to(x - 30 * s, y + 25 * s, x - 30 * s, y - 5 * s, x, y - 40 * s); rgb(c, col, a); c.fill()


def cycle_ring(c, t, x, y, r, hot=None, p=1.0, bars_=None):
    """anel de 28 dias (4 semanas); hot = (início, fim) destacado; bars_ = força relativa por semana"""
    for i in range(28):
        q = prog(p, i / 28 * 0.7, 0.3) if p < 1 else 1.0
        if q <= 0:
            continue
        a = -math.pi / 2 + i * 2 * math.pi / 28
        on = hot and hot[0] <= i <= hot[1]
        disk(c, x + r * math.cos(a), y + r * math.sin(a), (16 if on else 12) * q, RED if on else (CARD if not bars_ else GREY))
    if bars_:
        for k, v in enumerate(bars_):
            a = -math.pi / 2 + (k * 7 + 3) * 2 * math.pi / 28
            draw_text(c, f"S{k + 1}", x + (r + 70) * math.cos(a), y + (r + 70) * math.sin(a) + 14, 34, GREY, "Space Mono", p, align="center")


def nuclei_fiber(c, t, x, y, w, h, k=1.0, n=6, p=1.0, glow=0.0):
    """fibra com núcleos (pontos) que ficam mesmo quando ela afina"""
    muscle_fiber(c, t, x, y, w, h, p, k)
    if p <= 0:
        return
    for i in range(n):
        xx = x - w * 0.38 + i * w * 0.76 / max(1, n - 1)
        yy = y + (h * k * 0.18) * (1 if i % 2 else -1)
        disk(c, xx, yy, 13, (0.35, 0.2, 0.55))
        if glow > 0:
            c.new_path(); c.arc(xx, yy, 22 + 4 * math.sin(t * 6 + i), 0, 2 * math.pi); rgb(c, YEL, glow); c.set_line_width(4); c.stroke()


def pill(c, x, y, s=1.0, p=1.0, col=None, txt=None):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001)); c.rotate(-0.4)
    rrect(c, -90, -36, 180, 72, 36, WHITE); rrect(c, 0, -36, 90, 72, 36, col or BLU); rrect(c, 0, -36, 40, 72, 0, col or BLU)
    c.restore()
    if txt:
        draw_text(c, txt, x, y + 100 * s, 40, GREY, "Space Mono", p, align="center", spacing=2)


def coin_stack(c, t, x, y, n, p=1.0):
    for i in range(n):
        q = back_out(prog(p, i / max(n, 1) * 0.7, 0.3)) if p < 1 else 1.0
        if q <= 0:
            continue
        rrect(c, x - 70 * q, y - i * 30 - 24, 140 * q, 28, 14, YEL)
        cap_line(c, x - 50 * q, y - i * 30 - 10, x + 50 * q, y - i * 30 - 10, (0.8, 0.55, 0.05), 3)


def counter(c, t, x, y, a, b, fmt="{:.0f}", size=150, col=YEL, t0=0.15, dur=1.2, suffix=""):
    """igual ao do kit v2, com vírgula decimal (padrão BR)"""
    v = lerp(a, b, ease_out(prog(t, t0, dur)))
    pul = 1 + 0.05 * math.sin(t * 5) * prog(t, t0 + dur, 0.2)
    draw_text(c, (fmt.format(v) + suffix).replace(".", ","), x, y + size * 0.35, size * pul, col, "Anton", back_out(prog(t, 0.05, 0.25)), align="center")
