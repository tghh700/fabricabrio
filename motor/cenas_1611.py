"""Extensões do kit v2 para o lote de 16/11: barras por ano, balança de banheiro, osso com placa de crescimento,
xícara, coqueteleira, prato, régua, fita métrica, moldura de foto com luz, tecido (músculo x gordura).
Sem glifos fora da fonte (nada de ✓ ✦ — use check_mark/x_mark)."""
from cenas_1511 import *

FAT = (0.98, 0.80, 0.42)
MEAT = (0.86, 0.33, 0.36)
COFFEE = (0.42, 0.26, 0.16)


def bars(c, t, x, y, vals, labels, cols=None, w=110, gap=40, h=420, t0=0.15, step=0.25, fmt=None):
    """barras verticais crescendo (base em y). vals 0..1"""
    n = len(vals); tot = n * w + (n - 1) * gap
    for i, v in enumerate(vals):
        p = ease_out(prog(t, t0 + i * step, 0.5))
        bx = x - tot / 2 + i * (w + gap)
        col = (cols[i] if cols else GRN)
        hh = max(1, h * v * p)
        rrect(c, bx, y - hh, w, hh, 18, col)
        draw_text(c, labels[i], bx + w / 2, y + 52, 36, GREY, "Space Mono", 1.0, align="center", spacing=1)
        if fmt and p > 0.6:
            draw_text(c, fmt[i], bx + w / 2, y - hh - 22, 44, WHITE, "Anton", min(1, (p - 0.6) * 3), align="center")


def bath_scale(c, x, y, txt, p=1.0, col=None, shake=0.0):
    """balança de banheiro vista de cima-frente"""
    if p <= 0:
        return
    c.save(); c.translate(x + shake, y); c.scale(max(p, .001), max(p, .001))
    rrect(c, -190, -70, 380, 150, 40, (0.85, 0.86, 0.9))
    rrect(c, -110, -50, 220, 70, 14, (0.12, 0.14, 0.17))
    draw_text(c, txt, 0, 4, 52, col or GRN, "Anton", 1.0, align="center")
    for sd in (-1, 1):
        rrect(c, sd * 120 - 40, 30, 80, 34, 12, (0.7, 0.72, 0.77))
    c.restore()


def bone(c, x, y, w=460, th=70, glow=0.0, p=1.0, thick=0.0):
    """osso longo na horizontal; glow acende as placas de crescimento perto das pontas"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))
    th = th * (1 + 0.35 * thick)
    col = (0.93, 0.90, 0.82)
    rrect(c, -w / 2 + 40, -th / 2, w - 80, th, th / 2, col)
    for sd in (-1, 1):
        disk(c, sd * (w / 2 - 30), -th * 0.45, th * 0.62, col); disk(c, sd * (w / 2 - 30), th * 0.45, th * 0.62, col)
        if glow > 0:
            gx = sd * (w / 2 - 95)
            rrect(c, gx - 9, -th * 0.75, 18, th * 1.5, 8, YEL, glow)
    c.restore()


def cup(c, t, x, y, s=1.0, p=1.0):
    """xícara de café com vapor"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    c.new_path(); c.arc(95, -20, 42, -1.4, 1.4); rgb(c, WHITE); c.set_line_width(18); c.stroke()
    c.new_path(); c.move_to(-110, -90); c.line_to(110, -90); c.line_to(85, 60); c.line_to(-85, 60); c.close_path(); rgb(c, WHITE); c.fill()
    rrect(c, -100, -92, 200, 26, 12, COFFEE)
    rrect(c, -150, 60, 300, 26, 12, (0.8, 0.8, 0.84))
    for k in range(3):
        f = (t * 0.7 + k / 3) % 1
        xx = -50 + k * 50 + 14 * math.sin(f * 7 + k)
        cap_line(c, xx, -110 - 140 * f, xx + 10 * math.sin(f * 9), -150 - 140 * f, WHITE, 10, (1 - f) * 0.7)
    c.restore()


def shaker(c, x, y, s=1.0, p=1.0, col=None):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -70, -150, 140, 260, 30, (0.88, 0.9, 0.95), 0.9)
    rrect(c, -66, -20, 132, 126, 26, col or (0.85, 0.72, 0.55))
    rrect(c, -80, -200, 160, 60, 18, BLU)
    rrect(c, -20, -240, 40, 44, 10, BLU)
    c.restore()


def plate_food(c, x, y, s=1.0, p=1.0):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    disk(c, 0, 0, 130, WHITE); disk(c, 0, 0, 100, (0.88, 0.88, 0.85))
    disk(c, -38, -24, 46, (0.96, 0.95, 0.88))   # arroz
    disk(c, 40, -20, 40, (0.45, 0.25, 0.2))     # feijão
    rrect(c, -50, 20, 110, 52, 20, MEAT)        # carne
    disk(c, 60, 50, 22, GRN)
    c.restore()


def ruler(c, t, x, y_top, y_bot, p=1.0, mark=None):
    """régua vertical na parede (altura)"""
    if p <= 0:
        return
    h = (y_bot - y_top) * ease_out(p)
    rrect(c, x - 34, y_bot - h, 68, h, 10, (0.86, 0.75, 0.45))
    n = int((y_bot - y_top) / 40)
    for i in range(n + 1):
        yy = y_bot - i * 40
        if yy < y_bot - h:
            break
        cap_line(c, x - 34, yy, x - (0 if i % 5 == 0 else 14), yy, (0.25, 0.2, 0.12), 4)
    if mark is not None:
        cap_line(c, x - 70, mark, x + 70, mark, RED, 10)


def tape(c, t, x, y, w, v, p=1.0, col=YEL):
    """fita métrica horizontal; v 0..1 = comprimento (cintura)"""
    if p <= 0:
        return
    L = w * v * ease_out(p)
    rrect(c, x - w / 2, y - 26, L, 52, 12, col)
    for i in range(int(L / 30)):
        xx = x - w / 2 + i * 30
        cap_line(c, xx, y - 26, xx, y - (6 if i % 5 == 0 else 14), INK, 3)
    rrect(c, x - w / 2 - 50, y - 46, 70, 92, 16, (0.35, 0.36, 0.42))


def frame(c, x, y, w, h, title, col, p=1.0):
    """moldura de foto com rótulo no topo"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))
    rrect(c, -w / 2 - 10, -h / 2 - 10, w + 20, h + 20, 24, WHITE)
    rrect(c, -w / 2, -h / 2, w, h, 18, (0.12, 0.13, 0.17))
    rrect(c, -w / 2, -h / 2, w, 70, 18, col)
    draw_text(c, title, 0, -h / 2 + 52, 46, INK if col != RED else WHITE, "Anton", 1.0, align="center")
    c.restore()


def lamp(c, t, x, y, on=1.0, down=True):
    """luminária com raios (de cima para baixo, ou de frente)"""
    rrect(c, x - 70, y - 30, 140, 50, 20, STEEL)
    for k in range(5):
        a = (math.pi / 2 if down else 0) + (k - 2) * 0.22
        L = 200 + 20 * math.sin(t * 4 + k)
        cap_line(c, x + 60 * math.cos(a), y + 60 * math.sin(a), x + L * math.cos(a), y + L * math.sin(a), YEL, 8, 0.6 * on)


def fat_blob(c, t, x, y, r, p=1.0):
    if p <= 0:
        return
    for k, (dx, dy, rr) in enumerate(((0, 0, 1), (-0.6, 0.35, 0.6), (0.62, 0.3, 0.55), (0.1, -0.6, 0.5))):
        disk(c, x + dx * r, y + dy * r + 4 * math.sin(t * 3 + k), r * rr * ease_out(p), FAT)


def muscle_fiber(c, t, x, y, w, h, p=1.0, k=1.0):
    """feixe de músculo (cápsula vermelha listrada); k = espessura relativa"""
    if p <= 0:
        return
    hh = h * k
    w_ = w * ease_out(p)
    rrect(c, x - w_ / 2, y - hh / 2, w_, hh, hh / 2, MEAT)
    for i in range(1, 4):
        yy = y - hh / 2 + hh * i / 4
        cap_line(c, x - w_ / 2 + hh * 0.4, yy, x + w_ / 2 - hh * 0.4, yy, (0.98, 0.6, 0.6), 4, 0.6)


def bicep_glow(c, t, hx, hy, a=1.0):
    """brilho pulsante no bíceps do boneco (perto do ombro-cotovelo da frente)"""
    r = 70 + 10 * math.sin(t * 6)
    c.new_path(); c.arc(hx, hy, r, 0, 2 * math.pi); rgb(c, YEL, 0.25 * a); c.fill()
    c.new_path(); c.arc(hx, hy, r, 0, 2 * math.pi); rgb(c, YEL, 0.9 * a); c.set_line_width(8); c.stroke()


def scene(fn, txt, col=YEL, fg=None, bg=True):
    """igual ao scene() do kit v2"""
    from cenas_v2 import scene as _s
    return _s(fn, txt, col, fg, bg)
