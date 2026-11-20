"""Extensões do kit v2 para o lote de 21/11 (BRIO 79–82): elevação pélvica de lado (uma figura, barra sobre o quadril),
garrafa d'água, cubos de gelo, banheira de gelo, termômetro, barras de sono. Sem glifos fora da fonte (use check_mark/x_mark)."""
from cenas_2011 import *

ICE = (0.78, 0.92, 1.0)
WATER = (0.35, 0.72, 1.0)


def thruster(c, x, y, s, u, col=None):
    """elevação pélvica vista de lado (olhando para a direita). u: 0 = quadril embaixo, 1 = quadril no alto.
    Costas apoiadas no banco, pés no chão, canela vertical em cima, barra (anilha) sobre o quadril. y = chão."""
    col = col or YEL
    c.save(); c.translate(x, y); c.scale(s, s)
    shadow(c, 260, 0, 360)
    # banco (atrás das costas)
    rrect(c, -170, -250, 190, 56, 18, CARD)
    cap_line(c, -140, -200, -140, 0, (0.3, 0.32, 0.38), 24); cap_line(c, -10, -200, -10, 0, (0.3, 0.32, 0.38), 24)
    u = clamp(u)
    sh = (-20, -285)                          # ombro apoiado na borda do banco
    knee = (430, -250)
    foot = (450, -12)
    th = math.radians(lerp(-48, -2, ease(u)))  # ângulo coxa (do joelho ao quadril)
    hip = (knee[0] - 200 * math.cos(th), knee[1] - 200 * math.sin(th))
    # perna de trás (mais escura), levemente deslocada
    poly(c, [(hip[0] - 6, hip[1] + 6), (knee[0] - 14, knee[1] + 6), (foot[0] - 20, foot[1])], L_BACK, 50)
    cap_line(c, foot[0] - 28, foot[1], foot[0] + 26, foot[1], L_BACK, 40)
    # tronco: do ombro ao quadril
    cap_line(c, sh[0], sh[1], hip[0], hip[1], L_BODY, 100)
    # cabeça (apoiada na altura do banco, queixo para o peito)
    ang = math.atan2(hip[1] - sh[1], hip[0] - sh[0])
    disk(c, sh[0] - 95 * math.cos(ang) - 10, sh[1] - 95 * math.sin(ang) - 22, 62, L_BODY)
    # perna da frente
    poly(c, [hip, knee, foot], L_FRONT, 52)
    cap_line(c, foot[0] - 10, foot[1], foot[0] + 46, foot[1], L_FRONT, 42)
    # barra sobre o quadril (anilha de lado) e braço segurando
    bx, by = hip[0] + 8, hip[1] - 108
    poly(c, [(sh[0] + 30, sh[1] - 10), ((sh[0] + bx) / 2, by + 40), (bx - 30, by + 30)], L_FRONT, 40)
    r = 92
    disk(c, bx, by, r, col); disk(c, bx, by, r * 0.62, mix(col, INK, 0.35)); disk(c, bx, by, r * 0.18, (0.75, 0.76, 0.8))
    c.restore()
    return (x + hip[0] * s, y + hip[1] * s)


def act_thrust(c, t, x=40, s=0.85, spd=2.2, y=None):
    """subida rápida, pausa curta em cima, descida controlada"""
    ph = (t * spd / (2 * math.pi)) % 1
    u = ease(ph / 0.3) if ph < 0.3 else (1.0 if ph < 0.42 else 1 - ease((ph - 0.42) / 0.58))
    return thruster(c, x, FLOOR_Y if y is None else y, s, u)


def mini_thrust(c, t, cx, base_y, s=0.42, spd=2.2):
    act_thrust(c, t, cx - 240 * s, s, spd, base_y)


def glute_glow(c, x, y, r, a):
    if a <= 0:
        return
    c.new_path(); c.arc(x, y, r, 0, 2 * math.pi); rgb(c, YEL, 0.22 * a); c.fill_preserve(); rgb(c, YEL, 0.9 * a); c.set_line_width(8); c.stroke()


def bottle(c, x, y, s=1.0, p=1.0, cold=1.0, level=0.8):
    """garrafa d'água; cold 0..1 = gotinhas de condensação"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -60, -170, 120, 300, 40, (0.86, 0.92, 1.0), 0.55)
    h = 270 * level
    rrect(c, -50, 120 - h, 100, h, 32, WATER, 0.9)
    rrect(c, -34, -220, 68, 56, 14, BLU)
    for k in range(5):
        disk(c, -40 + (k * 23) % 80, -110 + k * 46, 7, WHITE, 0.8 * cold)
    c.restore()


def ice_cube(c, x, y, r, a=1.0, rot=0.0):
    c.save(); c.translate(x, y); c.rotate(rot)
    rrect(c, -r, -r, 2 * r, 2 * r, r * 0.3, ICE, a)
    rrect(c, -r * 0.6, -r * 0.7, r * 0.5, r * 0.3, r * 0.12, WHITE, 0.8 * a)
    c.restore()


def ice_tub(c, t, x, y, s=1.0, p=1.0):
    """banheira com água gelada e cubos boiando (sem pessoa)"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -230, -40, 460, 200, 70, (0.88, 0.9, 0.95))
    rrect(c, -205, -20, 410, 60, 30, WATER, 0.85)
    for k in range(5):
        ice_cube(c, -150 + k * 75, -14 + 6 * math.sin(t * 2 + k), 26, 1.0, 0.3 * math.sin(k * 1.7))
    cap_line(c, -170, 160, -170, 200, (0.6, 0.62, 0.68), 22); cap_line(c, 170, 160, 170, 200, (0.6, 0.62, 0.68), 22)
    for k in range(3):
        snowflake(c, -120 + k * 120, -120 - 14 * math.sin(t * 2 + k), 26, 0.7)
    c.restore()


def thermo_b(c, x, y, frac, p=1.0, col=None, h=320):
    """termômetro vertical do kit BRIO; frac 0..1"""
    if p <= 0:
        return
    col = col or mix(BLU, RED, frac)
    rrect(c, x - 26, y - h, 52, h, 26, CARD, p)
    hh = 40 + (h - 70) * clamp(frac)
    rrect(c, x - 14, y - hh, 28, hh, 14, col, p)
    disk(c, x, y + 16, 46, col, p)


def sparks_up(c, t, x, y, n=5, col=None, a=1.0, spread=120):
    """sinais de crescimento subindo (bolinhas amarelas)"""
    for i in range(n):
        f = (t * 0.8 + i / n) % 1
        disk(c, x - spread / 2 + spread * i / max(n - 1, 1), y - 240 * f, 16, col or YEL, a * (1 - f))
