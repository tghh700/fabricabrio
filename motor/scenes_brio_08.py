"""Cenas do BRIO 08 — cardio atrapalha a hipertrofia?"""
import math
from engine2 import *
from fixtext import draw_text
from scenes_short02 import chip

CARD = (0.20, 0.22, 0.27)
INK = (0.1, 0.1, 0.1)
METAL = (0.55, 0.57, 0.62)
DECK = (0.13, 0.14, 0.17)
HEART = (0.93, 0.27, 0.35)


def pop_in(c, x, y, p):
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))


# ------------------------------------------------------------ objetos novos
def treadmill(c, x, y, s=1.0, t=0.0, speed=1.0, incline=0.0, face=1):
    """esteira de lado; (x,y) = centro da base no chão. face=1 console à direita.
    Retorna (x_meio_esteira, y_topo_esteira) para pôr o boneco."""
    c.save(); c.translate(x, y); c.scale(s * face, s)
    ang = -math.radians(incline)
    # pés
    cap_line(c, -230, 0, -230, -20, METAL, 22)
    c.save(); c.translate(-240, -40); c.rotate(ang)
    # deck
    rrect(c, 0, -30, 480, 56, 26, DECK)
    rrect(c, 10, -38, 460, 18, 9, (0.30, 0.32, 0.38))
    # listras da lona andando
    off = (t * 260 * speed) % 60
    c.save(); rrect(c, 10, -38, 460, 18, 9); c.clip()
    for i in range(-1, 10):
        xx = 470 - (i * 60 + off)
        cap_line(c, xx, -38, xx - 10, -20, (0.5, 0.52, 0.58), 5)
    c.restore()
    disk(c, 26, -2, 22, METAL); disk(c, 454, -2, 22, METAL)
    # coluna + console
    cap_line(c, 450, -20, 500, -330, METAL, 22)
    cap_line(c, 500, -300, 360, -300, METAL, 16)
    rrect(c, 455, -380, 110, 70, 16, (0.2, 0.22, 0.27))
    rrect(c, 470, -368, 80, 40, 8, YEL, 0.85 + 0.15 * math.sin(t * 6))
    c.restore()
    fx = -240 + 440 * math.cos(ang); fy = -40 + 440 * math.sin(ang)
    cap_line(c, fx, 0, fx, fy, METAL, 22)
    c.restore()
    # posição do boneco (meio da lona)
    mx = x + face * s * (-240 + 220 * math.cos(ang))
    my = y + s * (-40 + 220 * math.sin(ang) - 30)
    return mx, my


def bike(c, x, y, s=1.0, t=0.0, face=1):
    """bike ergométrica; (x,y) = chão sob o pedal. Retorna (pedal_frente, pedal_trás, selim, guidão)."""
    c.save(); c.translate(x, y); c.scale(s * face, s)
    cap_line(c, -200, 0, 220, 0, METAL, 26)
    cap_line(c, -60, -10, -90, -300, (0.30, 0.32, 0.38), 30)            # tubo do selim
    rrect(c, -150, -330, 130, 34, 16, DECK)                             # selim
    cap_line(c, 0, -170, 150, -10, (0.30, 0.32, 0.38), 30)
    cap_line(c, -60, -170, 150, -170, (0.30, 0.32, 0.38), 26)
    cap_line(c, 150, -10, 170, -380, (0.30, 0.32, 0.38), 28)          # coluna guidão
    cap_line(c, 170, -380, 110, -400, METAL, 18)
    disk(c, 150, -150, 70, YEL); disk(c, 150, -150, 40, (0.3, 0.32, 0.38))  # volante
    a = t * 6
    for k in range(4):
        r = a + k * math.pi / 2
        cap_line(c, 150, -150, 150 + 55 * math.cos(r), -150 + 55 * math.sin(r), DECK, 6)
    disk(c, -20, -150, 34, METAL)
    c.restore()
    cx, cy = x - 20 * s * face, y - 150 * s
    p1 = (cx + face * 70 * s * math.cos(a), cy + 70 * s * math.sin(a))
    p2 = (cx - face * 70 * s * math.cos(a), cy - 70 * s * math.sin(a))
    seat = (x + face * (-85) * s, y - 330 * s)
    bar = (x + face * 115 * s, y - 400 * s)
    return p1, p2, seat, bar


def rider(c, bx, by, s, t, face=1):
    """boneco pedalando: tronco no selim, pernas até os pedais."""
    p1, p2, seat, bar = bike(c, bx, by, s, t, face)
    sc = s * 0.75
    hip = (seat[0] + face * 10 * s, seat[1] - 6 * s)
    LW = 50 * sc
    for (px, py), col in ((p2, L_BACK), (p1, L_FRONT)):
        # joelho: ponto acima entre quadril e pedal
        mx, my = (hip[0] + px) / 2, (hip[1] + py) / 2
        L = math.hypot(px - hip[0], py - hip[1]); half = 150 * sc
        h = math.sqrt(max(0, half * half - (L / 2) ** 2))
        nx, ny = -(py - hip[1]) / (L or 1), (px - hip[0]) / (L or 1)
        if ny > 0: nx, ny = -nx, -ny
        if face * nx < 0: nx, ny = -nx, -ny
        k = (mx + nx * h, my + ny * h)
        poly(c, [hip, k, (px, py)], col, LW)
        cap_line(c, px - 8 * sc * face, py, px + 40 * sc * face, py, col, LW * 0.8)
    # tronco inclinado
    sh = (hip[0] + face * 90 * sc, hip[1] - 210 * sc)
    cap_line(c, hip[0], hip[1], sh[0], sh[1], L_BODY, 136 * sc)
    poly(c, [(sh[0], sh[1] + 10 * sc), bar], L_FRONT, LW)
    disk(c, sh[0] + face * 30 * sc, sh[1] - 95 * sc, 68 * sc, L_BODY)


def heart(c, x, y, r, col=HEART, a=1.0):
    c.save(); c.translate(x, y); c.scale(r / 100, r / 100)
    c.new_path(); c.move_to(0, 90)
    c.curve_to(-140, -10, -100, -120, 0, -55)
    c.curve_to(100, -120, 140, -10, 0, 90)
    c.close_path(); rgb(c, col, a); c.fill()
    c.restore()


def paper(c, x, y, s, ang, a=1.0):
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    rrect(c, -90, -115, 180, 230, 14, WHITE, a)
    rrect(c, -65, -85, 90, 16, 8, YEL, a)
    for i in range(5):
        rrect(c, -65, -45 + i * 30, 130 - (i % 2) * 30, 12, 6, (0.75, 0.75, 0.78), a)
    c.restore()


def clock(c, x, y, r, t, col=WHITE, h=0.0):
    disk(c, x, y, r, col); disk(c, x, y, r * 0.84, (0.12, 0.13, 0.16))
    a1 = h * math.tau / 12 - math.pi / 2; a2 = t * 3 - math.pi / 2
    cap_line(c, x, y, x + r * 0.45 * math.cos(a1), y + r * 0.45 * math.sin(a1), col, r * 0.12)
    cap_line(c, x, y, x + r * 0.7 * math.cos(a2), y + r * 0.7 * math.sin(a2), YEL, r * 0.08)
    disk(c, x, y, r * 0.09, col)


def walker(c, x, y, s, t, face=1, dark=False):
    pose = pose_mix("walk1", "walk2", (math.sin(t * 7) + 1) / 2)
    return chunky(c, x, y, s, pose, face=face, dark=dark, bob=-abs(math.sin(t * 7)) * 8)


# ------------------------------------------------------------ cenas
def hook(c, t, d, b):
    with Cam(c, t, punch=0.10, shake=8 * (1 - prog(t, 0, 0.4))):
        mx, my = treadmill(c, 780, FLOOR_Y, 0.95, t, speed=1.4, incline=0)
        ring(c, 790, 1300, 260, t, YEL) if t < d * 0.45 else None
        flee = ease(prog(t, d * 0.45, d * 0.5))
        if flee <= 0:
            pose = pose_mix("flex", "shock", prog(t, d * 0.3, 0.25))
            chunky(c, 260, FLOOR_Y, 0.8, pose, face=1, bob=-abs(math.sin(t * 4)) * 6)
        else:
            walker(c, lerp(260, -60, flee), FLOOR_Y, 0.8, t * 1.6, face=-1)
            for i in range(3):
                cap_line(c, lerp(300, -60, flee) + 120 + i * 40, FLOOR_Y - 380 + i * 70,
                         lerp(300, -60, flee) + 200 + i * 40, FLOOR_Y - 380 + i * 70, WHITE, 10, 0.5)
        # bíceps "derretendo" com ? em cima
        p = back_out(prog(t, 0.25, 0.35))
        if p > 0:
            pop_in(c, 470, 880, p)
            rrect(c, -130, -90, 260, 180, 30, CARD)
            draw_text(c, "MÚSCULO", 0, -30, 30, GREY, "Space Mono", align="center", spacing=4)
            fall = ease(prog(t, 0.6, 1.0))
            rrect(c, -100, 10, 200, 40, 20, (0.3, 0.32, 0.38))
            rrect(c, -100, 10, 200 * (1 - 0.6 * fall), 40, 20, YEL)
            arrow(c, 145, -40, 145, 50, RED, 12, p=fall)
            c.restore()
        if t > d * 0.35:
            pq = back_out(prog(t, d * 0.35, 0.3))
            pop_in(c, 820, 1010, pq * (1 + 0.05 * math.sin(t * 8))); label(c, "?", 0, 70, YEL, 220); c.restore()


def science(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # pilha de estudos
        for i in range(4):
            st = 0.05 + i * 0.18
            p = back_out(prog(t, st, 0.3))
            if p <= 0: continue
            paper(c, 220 + i * 12, 1080 - i * 14, 0.95 * max(p, .001), -0.12 + i * 0.07)
        if t > 0.8:
            pl = ease_out(prog(t, 0.8, 0.4))
            c.save(); c.translate(250, 1080)
            c.new_path(); c.arc(30, -20, 60, 0, math.tau); rgb(c, WHITE, pl); c.set_line_width(14); c.stroke()
            cap_line(c, 72, 22, 120, 70, WHITE, 18, pl)
            c.restore()
        draw_text(c, "REVISÕES", 230, 1290, 34, GREY, "Space Mono", prog(t, 0.6, 0.3), align="center", spacing=4)
        # barras: só musculação x musculação + cardio
        base = 1520; H = 520
        g = ease_out(prog(t, d * 0.25, d * 0.35))
        bars = [("SÓ\nMUSC.", 1.0, WHITE, 620), ("MUSC.\n+CARDIO", 0.94, YEL, 870)]
        for name, v, col, x in bars:
            h = H * v * g
            rrect(c, x - 90, base - h, 180, max(h, 1), 22, col)
            for j, ln in enumerate(name.split("\n")):
                draw_text(c, ln, x, base + 50 + j * 40, 32, WHITE, "Space Mono", align="center", spacing=1)
        cap_line(c, 480, base, 1000, base, (1, 1, 1), 6, 0.3)
        if g >= 1:
            pa = prog(t, d * 0.6, 0.3)
            draw_text(c, "≈", 745, base - 260, 120, WHITE, "Anton", pa, align="center")
        chip(c, "QUASE NÃO ATRAPALHA", 540, 1745, YEL, INK, 58, t=t, start=d * 0.55)


def heart_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        beat = (t * 1.6) % 1
        pul = 1 + 0.12 * math.exp(-beat * 9) + 0.06 * math.exp(-max(0, beat - 0.2) * 9) * (beat > 0.2)
        p = back_out(prog(t, 0.05, 0.35))
        r = 150 * max(p, .001) * pul
        disk(c, 540, 1020, 230, HEART, 0.10 + 0.06 * math.exp(-beat * 6))
        heart(c, 540, 1030, r)
        # ECG
        y0 = 1290; x0, x1 = 100, 980
        n = 120; pts = []
        head = (t * 500) % (x1 - x0)
        for i in range(n + 1):
            xx = x0 + (x1 - x0) * i / n
            ph = ((xx - x0) % 220) / 220
            yy = y0
            if 0.40 < ph < 0.45: yy -= 40
            elif 0.45 < ph < 0.50: yy += 110 * (1 - abs(ph - 0.475) / 0.025) * 0 - 140 * (1 - abs(ph - 0.475) / 0.025)
            elif 0.50 < ph < 0.55: yy += 60
            if xx - x0 <= head: pts.append((xx, yy))
        if len(pts) > 1: poly(c, pts, YEL, 8)
        if pts: disk(c, pts[-1][0], pts[-1][1], 12, WHITE)
        # 3 benefícios
        items = [("CORAÇÃO", 0.2), ("FÔLEGO", 0.42), ("RECUPERAÇÃO", 0.62)]
        for i, (txt, f) in enumerate(items):
            st = d * f; pp = back_out(prog(t, st, 0.3))
            if pp <= 0: continue
            y = 1460 + i * 115
            pop_in(c, 540, y, pp)
            rrect(c, -330, -48, 660, 96, 28, CARD)
            draw_text(c, txt, -260, 26, 58, WHITE, "Anton")
            c.restore()
            check_mark(c, 800, y, 0.8, prog(t, st + 0.15, 0.3))


def order(c, t, d, b):
    with Cam(c, t, punch=0.06):
        sep = d * 0.6
        # etapa 1: musculação
        p1 = back_out(prog(t, 0.05, 0.35))
        if p1 > 0:
            pop_in(c, 280, 1080, p1)
            rrect(c, -210, -200, 420, 400, 36, CARD)
            disk(c, -170, -160, 44, YEL); label(c, "1", -170, -136, INK, 60)
            lift = math.sin(t * 5) * 30
            barbell(c, 0, -20 - abs(lift), 0.5, 2)
            label(c, "MUSCULAÇÃO", 0, 150, WHITE, 54)
            c.restore()
        arrow(c, 510, 1080, 580, 1080, YEL, 16, p=prog(t, d * 0.2, 0.3))
        p2 = back_out(prog(t, d * 0.28, 0.35))
        if p2 > 0:
            pop_in(c, 800, 1080, p2)
            rrect(c, -210, -200, 420, 400, 36, CARD)
            disk(c, -170, -160, 44, (0.3, 0.32, 0.38)); label(c, "2", -170, -136, WHITE, 60)
            c.save(); c.translate(0, 90); c.scale(0.5, 0.5)
            mx, my = treadmill(c, 0, 0, 1.0, t, 1.5)
            walker(c, mx + 10, my, 0.45 / 0.5 * 0.5 * 1.6, t)
            c.restore()
            label(c, "CARDIO", 0, 150, WHITE, 54)
            c.restore()
        # ou horários separados
        if t > sep:
            for i, (h, txt, x) in enumerate([(7, "MANHÃ", 330), (19, "NOITE", 750)]):
                pp = back_out(prog(t, sep + i * 0.2, 0.3))
                pop_in(c, x, 1440, pp)
                clock(c, 0, 0, 90, t + i, WHITE, h)
                draw_text(c, txt, 0, 150, 40, GREY, "Space Mono", align="center", spacing=4)
                c.restore()
            label(c, "OU", 540, 1465, YEL, 80, a=prog(t, sep, 0.3))
            chip(c, "HORÁRIOS SEPARADOS", 540, 1760, YEL, INK, 56, t=t, start=sep + 0.4)


def type_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # bike
        p1 = ease_out(prog(t, 0.05, 0.35))
        c.save(); c.translate(lerp(-400, 0, p1), 0)
        rider(c, 270, 1360, 0.85, t * 1.4, face=1)
        draw_text(c, "BIKE", 270, 1440, 46, WHITE, "Anton", align="center")
        c.restore()
        # caminhada inclinada
        p2 = ease_out(prog(t, d * 0.18, 0.35))
        c.save(); c.translate(lerp(500, 0, p2), 0)
        mx, my = treadmill(c, 790, 1360, 0.72, t, speed=0.7, incline=12)
        walker(c, mx + 10, my, 0.55, t * 0.8, face=1)
        draw_text(c, "INCLINADA", 790, 1440, 46, WHITE, "Anton", align="center")
        c.restore()
        check_mark(c, 110, 900, 1.0, prog(t, d * 0.2, 0.3))
        check_mark(c, 640, 900, 1.0, prog(t, d * 0.32, 0.3))
        # medidor de volume
        sv = d * 0.55
        if t > sv:
            a = ease_out(prog(t, sv, 0.3))
            x0, w, y = 160, 760, 1590
            draw_text(c, "VOLUME DE CARDIO", 540, y - 40, 30, GREY, "Space Mono", a, align="center", spacing=4)
            for i, col in enumerate([GRN, YEL, RED]):
                rrect(c, x0 + i * w / 3 + 4, y, w / 3 - 8, 34, 17, col, a)
            m = ease(prog(t, sv + 0.2, 0.9))
            mk = x0 + w * lerp(0.95, 0.2, m) + (math.sin(t * 6) * 6 if m >= 1 else 0)
            c.new_path(); c.move_to(mk, y - 4); c.line_to(mk - 18, y - 34); c.line_to(mk + 18, y - 34); c.close_path()
            rgb(c, WHITE, a); c.fill()
            chip(c, "SEM EXAGERO", 540, 1755, WHITE, INK, 50, t=t, start=sv + 0.9)


def cta(c, t, d, b):
    with Cam(c, t, punch=0.10):
        PX, PY = 540, 1200
        ring(c, PX, PY, 300, t, YEL)
        phone_screen(c, PX, PY, 1.0, glow=0.6 + 0.4 * math.sin(t * 5))
        pm = back_out(prog(t, 0.1, 0.35))
        if pm > 0:
            brio_mark(c, PX, 970, 0.9 * max(pm, .001), t=t)
            brio_wordmark(c, PX, 1080, 60)
        rrect(c, PX - 150, 1130, 300, 340, 20, (0.18, 0.2, 0.24))
        draw_text(c, "CARGA", PX - 128, 1168, 22, GREY, "Space Mono", spacing=3)
        gp = ease(prog(t, 0.4, d * 0.45))
        chart_up(c, PX - 125, 1200, 250, 220, gp)
        if gp >= 1:
            pass  # 10/11: seta extra removida (sobrepunha o gráfico)
            check_mark(c, PX + 95, 1440, 0.6, prog(t, 0.4 + d * 0.45, 0.3))
        chunky(c, 120, FLOOR_Y + 60, 0.6, "point_up", face=1)
        rider(c, 945, FLOOR_Y + 40, 0.5, t * 1.4, face=-1)
        if t > d * 0.4:
            draw_text(c, "GRÁTIS PRA REGISTRAR", 540, 1625, 30, WHITE, "Space Mono", prog(t, d * 0.4, 0.3), align="center", spacing=4)
        chip(c, "LINK NA BIO", 540, 1745, YEL, INK, 66, t=t, start=d * 0.55)


VIS = {"hook": hook, "science": science, "heart": heart_, "order": order, "type": type_, "cta": cta}
SFX = {
    "hook": [(0.0, "boom"), (0.25, "pop"), (0.6, "zip"), ("0.35d", "pop"), ("0.45d", "swish")],
    "science": [(0.0, "whoosh"), (0.05, "clack"), (0.23, "clack"), (0.41, "clack"), (0.59, "clack"), ("0.25d", "zip"), ("0.55d", "pop")],
    "heart": [(0.0, "whoosh"), (0.05, "pop"), ("0.2d", "pop"), ("0.42d", "pop"), ("0.62d", "pop"), ("0.62d+0.2", "ding")],
    "order": [(0.0, "whoosh"), (0.05, "pop"), ("0.2d", "swish"), ("0.28d", "pop"), ("0.6d", "tick"), ("0.6d+0.2", "tick"), ("0.6d+0.4", "pop")],
    "type": [(0.0, "whoosh"), ("0.18d", "swish"), ("0.2d", "ding"), ("0.55d", "zip"), ("0.55d+0.9", "pop")],
    "cta": [(0.0, "whoosh"), (0.1, "pop"), ("0.4+0.45d", "ding"), ("0.55d", "pop")],
}
