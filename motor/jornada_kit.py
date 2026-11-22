"""Peças reaproveitáveis da 'jornada de erros' do BRIO (23/11). Base: cenas_v2 + peças do v2_75_cresce.
Uma figura por cena (comparação explícita em split é a exceção). Só glifos da fonte; marcas desenhadas."""
from cenas_v2 import *
from v2_75_cresce import mirror, plate, tape_arm, barbell_load, graph, puzzle

# agachamento livre (sem barra): braços à frente para equilibrar
BW_UP = (60, 10, 72, 10, -10, 6, 12, 6)
BW_DOWN = (78, 10, 88, 10, 85, -115, 95, -125)


def act_bwsquat(c, t, x=HX, s=0.95, spd=2.4):
    u = 0.5 - 0.5 * math.cos(t * spd)
    chunky(c, x, FLOOR_Y, s, pose_mix(BW_UP, BW_DOWN, u))


def act_curl_struggle(c, t, x=HX, s=0.95):
    """rosca travando no meio (tremendo) — carga pesada até a falha"""
    ph = (t * 0.55) % 1
    u = 0.55 * (ease(ph / 0.6) if ph < 0.6 else 1 - ease((ph - 0.6) / 0.4))
    u += 0.025 * math.sin(t * 40) * (0.3 < ph < 0.65)
    hx, hy = chunky(c, x, FLOOR_Y, s, pose_mix("curl_down", "curl_up", u))
    dumbbell(c, hx, hy, s * 1.3, 0.0)
    for k in range(2):  # suor
        f = (t * 0.9 + k * 0.5) % 1
        disk(c, x + 60 + k * 30, FLOOR_Y - 640 * s + 140 * f, 10, BLU, 1 - f)


def pain_marks(c, t, x, y, s=1.0, a=1.0):
    """raios vermelhos de dor (desenhados) em volta de um ponto"""
    for k in range(5):
        ang = -2.2 + k * 0.55
        r1 = 46 * s + 8 * math.sin(t * 9 + k)
        x1, y1 = x + r1 * math.cos(ang), y + r1 * math.sin(ang)
        x2, y2 = x + (r1 + 38 * s) * math.cos(ang), y + (r1 + 38 * s) * math.sin(ang)
        cap_line(c, x1, y1, x2, y2, RED, 9 * s, a)


def stairs(c, x, y, n=5, step=80, rise=60, col=(0.30, 0.33, 0.40)):
    """escada descendo para a direita; (x, y) = topo do primeiro degrau"""
    for i in range(n):
        rrect(c, x + i * step, y + i * rise, step + 4, (n - i) * rise + 40, 6, col)


def stair_walker(c, t, x0, y0, step=80, rise=60, n=5, s=0.55):
    """boneco cansado descendo a escada devagar (pés sempre em cima de um degrau)"""
    k = min(n - 1, int((t * 0.6) % n))
    mini(c, x0 + k * step + step / 2, y0 + k * rise, s, lambda xx: act_tired(c, t, xx, 1.0))
    return x0 + k * step + step / 2, y0 + k * rise


def rows(c, t, items, x=770, y=800, w=470, gap=118, t0=0.2, hot=-1, hot_col=None, size=44):
    for i, s in enumerate(items):
        p = back_out(prog(t, t0 + i * 0.45, 0.3))
        card(c, x, y + i * gap, w, 96, CARD, p)
        if p > 0:
            col = (hot_col or GRN) if i == (hot if hot >= 0 else len(items) - 1) else WHITE
            draw_text(c, s, x, y + i * gap + 20, size, col, "Anton", p, align="center")


def caption(c, s, x, y, a=1.0, col=GREY, size=30):
    draw_text(c, s, x, y, size, col, "Space Mono", a, align="center", spacing=2)


def backpack(c, x, y, s=1.0, p=1.0):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -70, -90, 140, 190, 40, (0.35, 0.45, 0.70))
    rrect(c, -50, 10, 100, 70, 20, (0.28, 0.36, 0.58))
    c.new_path(); c.arc(0, -90, 40, math.pi, 2 * math.pi); rgb(c, (0.28, 0.36, 0.58)); c.set_line_width(14); c.stroke()
    c.restore()


def confetti(c, t, x, y, w=420, h=300):
    cols = (YEL, GRN, BLU, RED, LILAC)
    for i in range(18):
        fx = (i * 0.37 + 0.13) % 1; f = (t * 0.5 + i * 0.11) % 1
        disk(c, x - w / 2 + fx * w, y - h / 2 + f * h, 9, cols[i % len(cols)], 1 - f)


def cross_days(c, t, x, y, idx, cell=86, t0=0.4):
    """X vermelho sobre dias da semana desenhada por week()"""
    gap = 14; w = 7 * cell + 6 * gap
    for j, i in enumerate(idx):
        cx = x - w / 2 + cell / 2 + i * (cell + gap)
        x_mark(c, cx, y, 0.32, prog(t, t0 + j * 0.12, 0.2), RED)


def strike(c, x1, y, x2, p, col=None):
    if p > 0:
        cap_line(c, x1, y, lerp(x1, x2, ease(p)), y, col or RED, 10)


def concl(items, pose="flex"):
    def f(c, t, d):
        act_pose(c, t, pose, 300, 0.95)
        stack_list(c, t, items, x=760, y=900, w=520, gap=150, hot=len(items) - 1)
    return f
