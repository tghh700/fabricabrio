"""Extensões do kit v2 para o lote de 15/11: barra fixa (IK do braço), máquina de placas, fone, cinto,
pegada com strap, rosca com descida controlada, notas musicais e gráfico oscilando. Sem glifos fora da fonte."""
from cenas_v2 import *
from brio_kit2 import _drop

SH_LOCAL = (10, -510)  # ombro (braço da frente) no sistema local do chunky
L1, L2 = 120, 110


def _ik(dx, dy, front=True):
    """ângulos (graus, convenção do chunky) para a mão chegar em (dx, dy) a partir do ombro"""
    d = max(1e-3, min(L1 + L2 - 0.5, math.hypot(dx, dy)))
    a = math.atan2(dx, dy)
    al = math.acos(clamp((L1 * L1 + d * d - L2 * L2) / (2 * L1 * d), -1, 1))
    a1 = a - al if front else a + al
    ex, ey = L1 * math.sin(a1), L1 * math.cos(a1)
    b = math.atan2(dx - ex, dy - ey)
    return math.degrees(a1), math.degrees(b - a1)


def pullup_bar(c, x, by, w=520):
    col = (0.55, 0.57, 0.63)
    cap_line(c, x - w / 2, by, x + w / 2, by, STEEL, 20)
    for sd in (-1, 1):
        cap_line(c, x + sd * w / 2, by, x + sd * w / 2, FLOOR_Y, col, 22, 0.8)


def hanger(c, x, by, s, u, box=False):
    """boneco na barra fixa, de perfil. u 0 = pendurado, braço esticado; 1 = queixo acima da barra"""
    legs = (-4, 18, 10, 22)
    lift = lerp(0, 175, ease(u))                      # quanto o ombro sobe (unidades locais)
    shy_local = SH_LOCAL[1]
    hand_local_y = shy_local - (L1 + L2 - 4) + lift  # mão fica fixa na barra; o corpo sobe
    a1, a2 = _ik(2, hand_local_y - shy_local)
    pose = (a1, a2, a1, a2) + legs
    dr = _drop(pose)
    # pés no mundo: a mão (local hand_local_y + drop) tem que ficar em by
    fy = by - (hand_local_y + dr) * s
    if box:
        rrect(c, x - 110, FLOOR_Y - 230, 220, 230, 18, (0.30, 0.32, 0.38))
    pullup_bar(c, x + 10 * s, by, 520 * s)
    chunky(c, x, fy, s, pose)
    disk(c, x + 12 * s, by, 26 * s, L_BODY)  # mão fechada na barra (desenhada por cima)
    return fy


def stack_machine(c, x, y, s, u, n=8, sel=4, hi=None):
    """máquina de placas (vista de frente): u 0..1 sobe as placas selecionadas"""
    c.save(); c.translate(x, y); c.scale(s, s)
    frame = (0.42, 0.44, 0.50)
    cap_line(c, -170, 0, -170, -760, frame, 26); cap_line(c, 170, 0, 170, -760, frame, 26)
    cap_line(c, -170, -760, 170, -760, frame, 26)
    disk(c, 0, -760, 46, STEEL); disk(c, 0, -760, 16, frame)
    cap_line(c, -100, -10, -100, -700, STEEL, 8, 0.8); cap_line(c, 100, -10, 100, -700, STEEL, 8, 0.8)
    rise = 220 * ease(u)
    top = -30 - n * 46
    for i in range(n):
        yy = -30 - i * 46 - 40
        up = rise if i >= n - sel else 0
        rrect(c, -125, yy - up, 250, 40, 8, hi if (hi and i >= n - sel) else (0.30, 0.32, 0.38))
    pin_y = -30 - (n - sel) * 46 - 20
    cap_line(c, 120, pin_y - rise, 175, pin_y - rise, YEL, 12)
    cap_line(c, 0, -760, 0, top - rise - 30, (0.85, 0.85, 0.82), 6)  # cabo
    c.restore()


def head_pos(x, s, pose, bob=0.0):
    p = POSES[pose] if isinstance(pose, str) else pose
    return x, FLOOR_Y + (_drop(p) + bob - 615) * s


def headphones(c, hx, hy, s):
    c.new_path(); c.arc(hx - 8 * s, hy - 4 * s, 80 * s, math.pi * 1.05, math.pi * 1.95)
    rgb(c, BLU); c.set_line_width(18 * s); c.stroke()
    rrect(c, hx - 52 * s, hy - 34 * s, 46 * s, 80 * s, 20 * s, BLU)
    rrect(c, hx - 44 * s, hy - 24 * s, 30 * s, 60 * s, 14 * s, (0.15, 0.16, 0.2))


def note(c, x, y, s, col, a=1.0):
    """nota musical desenhada (sem glifo)"""
    c.save(); c.translate(x, y); c.rotate(-0.35)
    c.new_path(); c.save(); c.scale(1.3, 1); c.arc(0, 0, 18 * s, 0, 2 * math.pi); c.restore(); rgb(c, col, a); c.fill()
    c.restore()
    cap_line(c, x + 20 * s, y - 4 * s, x + 20 * s, y - 90 * s, col, 7 * s, a)
    cap_line(c, x + 20 * s, y - 90 * s, x + 50 * s, y - 70 * s, col, 9 * s, a)


def notes_float(c, t, x, y, n=3, col=YEL):
    for k in range(n):
        f = (t * 0.55 + k / n) % 1
        note(c, x + 60 * math.sin(f * 6 + k) + k * 40, y - 260 * f, 1.0, col, (1 - f) * min(1, f * 5))


def curl_u(c, x, s, u, heavy=False, trail=0.0):
    hx, hy = chunky(c, x, FLOOR_Y, s, pose_mix("curl_down", "curl_up", u))
    if trail > 0:
        for k in range(3):
            cap_line(c, hx + 60, hy - 30 - k * 40, hx + 60, hy - 90 - k * 40, WHITE, 6, trail * (0.6 - k * 0.15))
    dumbbell(c, hx, hy, s * (1.25 if heavy else 1.0), 0.0)
    return hx, hy


def curl_cycle(t, up=0.7, down=0.7, hold=0.15):
    """u(t) de uma rosca: sobe em `up` s, desce em `down` s"""
    T = up + hold + down + hold
    f = t % T
    if f < up: return ease(f / up), 0
    if f < up + hold: return 1.0, 0
    if f < up + hold + down: return 1 - (f - up - hold) / down if down < 0.3 else 1 - ease((f - up - hold) / down), 1
    return 0.0, 0


def act_curl_tempo(c, t, x=HX, s=0.95, down=2.0, up=0.7, heavy=False):
    u, ph = curl_cycle(t, up, down)
    fast = down < 0.3
    return curl_u(c, x, s, u, heavy, trail=(0.9 if (fast and ph) else 0.0))


def belt(c, x, s, dr, col=(0.45, 0.28, 0.16)):
    """cinto na cintura do chunky (pés em FLOOR_Y). dr = drop da pose"""
    y = FLOOR_Y + (dr - 335) * s
    rrect(c, x - 74 * s, y - 26 * s, 148 * s, 56 * s, 14 * s, col)
    rrect(c, x + 30 * s, y - 18 * s, 34 * s, 40 * s, 6 * s, STEEL)


def squat_belt(c, t, x=HX, s=0.95, spd=2.4, depth=0.9, press=0.0):
    d = depth * (0.5 - 0.5 * math.cos(t * spd))
    squatter(c, x, s, d, belly=press)
    belt(c, x, s, _drop(pose_mix("bar_back", "squat_deep", d)))


def holder(c, t, x=HX, s=0.95, slip=0.0, strap=False, shake=0.0):
    """boneco em pé segurando a barra (fim do terra), vista de lado; slip 0..1 = barra escorregando da mão"""
    hx, hy = chunky(c, x + shake * 6 * math.sin(t * 40), FLOOR_Y, s, "curl_down")
    by = hy + slip * 160
    plate_end(c, hx, by, 70 * s)
    if strap:
        c.new_path(); c.arc(hx, by, 34 * s, 0, 2 * math.pi); rgb(c, YEL); c.set_line_width(14 * s); c.stroke()
        cap_line(c, hx, by - 34 * s, hx - 6, hy - 70 * s, YEL, 14 * s)
    disk(c, hx, hy, 24 * s, L_BODY)  # mão
    return hx, hy


def zigzag(c, t, x, y, w, h, vals, col=BLU, trend=True, t0=0.15, dur=1.6, tcol=GRN):
    p = ease_out(prog(t, t0, dur))
    n = len(vals)
    pts = [(x + i * w / (n - 1), y + h - v * h) for i, v in enumerate(vals)]
    k = max(2, int(n * p + 0.999))
    cap_line(c, x, y + h, x + w, y + h, (1, 1, 1), 4, 0.25)
    poly(c, pts[:k], col, 10)
    for px, py in pts[:k]:
        disk(c, px, py, 12, col)
    if trend:
        q = ease_out(prog(t, t0 + dur, 0.6))
        if q > 0:
            x2 = lerp(pts[0][0], pts[-1][0], q)
            y2 = lerp(y + h - 0.25 * h, y + h - 0.85 * h, q)
            cap_line(c, pts[0][0], y + h - 0.25 * h, x2, y2, tcol, 16)


def scale_beam(c, t, x, y, tilt, lt="EMPURRAR", rt="PUXAR", L=300):
    """balança: tilt -1 (pesa à esquerda) .. 1 (pesa à direita)"""
    cap_line(c, x, y, x, y + 330, STEEL, 18)
    rrect(c, x - 120, y + 320, 240, 30, 12, STEEL)
    a = math.radians(14 * tilt)
    lx, ly = x - L * math.cos(a), y - L * math.sin(a)
    rx, ry = x + L * math.cos(a), y + L * math.sin(a)
    cap_line(c, lx, ly, rx, ry, STEEL, 14); disk(c, x, y, 18, YEL)
    for (px, py, txt, col) in ((lx, ly, lt, RED if tilt < -0.2 else BLU), (rx, ry, rt, RED if tilt > 0.2 else BLU)):
        cap_line(c, px, py, px, py + 110, GREY, 5)
        rrect(c, px - 120, py + 110, 240, 70, 18, col)
        draw_text(c, txt, px, py + 162, 40, INK, "Anton", 1.0, align="center")
