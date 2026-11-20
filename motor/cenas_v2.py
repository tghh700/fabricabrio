"""Kit v2 do BRIO (14/11): cenas mais ricas — boneco executando, painéis comparativos, contadores,
cenário de academia e transição entre beats. Sem caracteres fora da fonte (✓ ✦ viram desenho)."""
import math
from brio_kit2 import *

HX = 320            # x do boneco principal
RX, RY = 740, 1180  # centro da área de adereços


# ------------------------------------------------------------------ base
def wipe_in(fn, slide=150, dur=0.32, amp=0.015):
    """entrada da cena (desliza + aparece) e respiração leve de câmera depois"""
    def f(c, t, d, b):
        p = ease_out(prog(t, 0, dur))
        c.push_group()
        c.save(); c.translate(540, 1250); z = 1 + amp * math.sin(t * 1.7); c.scale(z, z)
        c.translate(-540 + (1 - p) * slide + 10 * math.sin(t * 1.1), -1250 + 8 * math.sin(t * 1.3))
        fn(c, t, d, b)
        c.restore()
        c.pop_group_to_source(); c.paint_with_alpha(0.25 + 0.75 * p)
    return f


def gym(c, t, a=0.16):
    """cenário de academia ao fundo: rack com anilhas e banco (bem apagado)"""
    col = (0.55, 0.57, 0.63)
    cap_line(c, 70, 1640, 70, 960, col, 16, a); cap_line(c, 200, 1640, 200, 960, col, 16, a)
    cap_line(c, 50, 1060, 220, 1060, col, 12, a)
    for i in range(3):
        disk(c, 135, 1250 + i * 110, 46 - i * 6, col, a)
    rrect(c, 840, 1520, 200, 26, 10, col, a); cap_line(c, 870, 1546, 870, 1640, col, 12, a); cap_line(c, 1010, 1546, 1010, 1640, col, 12, a)
    for i in range(2):
        disk(c, 980 - i * 70, 1600, 40, col, a)


def mini(c, cx, base_y, s, draw_fn):
    """desenha uma figura de cena (que usa FLOOR_Y) em escala reduzida com os pés em (cx, base_y)"""
    c.save(); c.translate(cx, base_y); c.scale(s, s); c.translate(-cx, -FLOOR_Y)
    draw_fn(cx)
    c.restore()


# ------------------------------------------------------------------ ações do boneco
def act_curl(c, t, x=HX, s=0.95, spd=2.6, heavy=False):
    u = 0.5 - 0.5 * math.cos(t * spd)
    hx, hy = chunky(c, x, FLOOR_Y, s, pose_mix("curl_down", "curl_up", u))
    dumbbell(c, hx, hy, s * (1.25 if heavy else 1.0), 0.0)


def act_squat(c, t, x=HX, s=0.95, spd=2.4, depth=0.9):
    return squatter(c, x, s, depth * (0.5 - 0.5 * math.cos(t * spd)))


def act_walk(c, t, x=HX, s=0.95, spd=6.0, move=0.0):
    u = 0.5 + 0.5 * math.sin(t * spd)
    chunky(c, x + move * t, FLOOR_Y, s, pose_mix("walk1", "walk2", u), bob=-8 * abs(math.sin(t * spd)))


def act_press(c, t, x=HX + 20, s=0.95, spd=2.2):
    front_presser(c, x, s, 0.5 - 0.5 * math.cos(t * spd))


def act_tired(c, t, x=HX, s=0.95):
    chunky(c, x, FLOOR_Y, s, "tired", squash=0.04 + 0.02 * math.sin(t * 2))
    for k in range(2):  # gotas de suor
        f = (t * 0.9 + k * 0.5) % 1
        disk(c, x + 60 + k * 30, FLOOR_Y - 640 * s + 140 * f, 10, BLU, 1 - f)


def act_pose(c, t, pose, x=HX, s=0.95):
    chunky(c, x, FLOOR_Y, s, pose, bob=10 * math.sin(t * 3.2))


# ------------------------------------------------------------------ adereços
def icon_ok(c, x, y, s, p):
    disk(c, x, y, 70 * s * max(p, 0.001), GRN, min(p, 1)); check_mark(c, x, y, 0.55 * s, p, INK)


def icon_x(c, x, y, s, p):
    disk(c, x, y, 70 * s * max(p, 0.001), RED, min(p, 1)); x_mark(c, x, y, 0.5 * s, p, WHITE)


def counter(c, t, x, y, a, b, fmt="{:.0f}", size=150, col=YEL, t0=0.15, dur=1.2, suffix=""):
    v = lerp(a, b, ease_out(prog(t, t0, dur)))
    pul = 1 + 0.05 * math.sin(t * 5) * prog(t, t0 + dur, 0.2)
    draw_text(c, fmt.format(v) + suffix, x, y + size * 0.35, size * pul, col, "Anton", back_out(prog(t, 0.05, 0.25)), align="center")


def battery(c, x, y, v, label_=None, w=170, h=300, col=None):
    """bateria vertical desenhada; v 0..1"""
    rrect(c, x - w / 2, y - h / 2, w, h, 24, CARD); rrect(c, x - 30, y - h / 2 - 22, 60, 26, 8, CARD)
    col = col or (GRN if v > 0.55 else YEL if v > 0.3 else RED)
    hh = (h - 24) * clamp(v)
    rrect(c, x - w / 2 + 12, y + h / 2 - 12 - hh, w - 24, hh, 16, col)
    if label_:
        draw_text(c, label_, x, y + h / 2 + 50, 30, GREY, "Space Mono", 1.0, align="center", spacing=2)


def split(c, t, left_fn, right_fn, ltxt="ERRADO", rtxt="CERTO", lcol=None, rcol=None, y=1240, h=640):
    """dois quadros lado a lado; cada fn(c, t, cx, base_y) desenha o conteúdo"""
    lcol = lcol or RED; rcol = rcol or GRN
    for i, (fn, txt, col) in enumerate(((left_fn, ltxt, lcol), (right_fn, rtxt, rcol))):
        cx = 290 + i * 500
        p = back_out(prog(t, 0.1 + i * 0.35, 0.35))
        if p <= 0:
            continue
        card(c, cx, y, 460, h, CARD, p)
        c.save(); c.translate(cx, y); c.scale(max(p, .001), max(p, .001)); c.translate(-cx, -y)
        rrect(c, cx - 230, y - h / 2, 460, 84, 26, col)
        rrect(c, cx - 230, y - h / 2 + 50, 460, 34, 0, col)
        label(c, txt, cx, y - h / 2 + 62, INK if col != RED else WHITE, 50)
        fn(c, t, cx, y + h / 2 - 40)
        c.restore()


def week(c, t, x, y, on, cols=None, labels=("S", "T", "Q", "Q", "S", "S", "D"), cell=96, t0=0.2):
    """semana com dias marcados (on = índices)"""
    gap = 14; w = 7 * cell + 6 * gap
    for i, l in enumerate(labels):
        cx = x - w / 2 + cell / 2 + i * (cell + gap)
        hot = i in on
        p = back_out(prog(t, t0 + i * 0.08, 0.25))
        rrect(c, cx - cell / 2, y - cell / 2, cell, cell, 20, (cols or YEL) if hot and p > 0.5 else CARD)
        draw_text(c, l, cx, y + 18, 46, INK if hot and p > 0.5 else GREY, "Anton", 1.0, align="center")
        if hot and cell >= 90:
            check_mark(c, cx + 30, y - cell / 2 - 26, 0.3, prog(t, t0 + 0.3 + i * 0.08, 0.2), GRN)


def stack_list(c, t, items, x=RX, y=960, w=560, gap=150, hot=-1, t0=0.15, num=True):
    for i, s in enumerate(items):
        p = back_out(prog(t, t0 + i * 0.3, 0.3))
        if p <= 0:
            continue
        isel = (i == hot)
        card(c, x, y + i * gap, w, 118, YEL if isel else CARD, p)
        xx = x - w / 2 + 34
        if num:
            draw_text(c, str(i + 1), xx + 10, y + i * gap + 24, 64, INK if isel else YEL, "Anton", p)
            xx += 70
        draw_text(c, s, xx, y + i * gap + 22, 50, INK if isel else WHITE, "Anton", p)


def sun(c, t, x, y, r=90):
    for i in range(10):
        a = i * math.pi / 5 + t * 0.6
        cap_line(c, x + (r + 24) * math.cos(a), y + (r + 24) * math.sin(a), x + (r + 58) * math.cos(a), y + (r + 58) * math.sin(a), YEL, 12)
    disk(c, x, y, r, YEL)


def moon(c, t, x, y, r=80):
    disk(c, x, y, r, (0.86, 0.87, 0.93))
    for (dx, dy, rr) in ((-25, -20, 16), (20, 15, 22), (-8, 36, 11)):
        disk(c, x + dx, y + dy, rr, (0.72, 0.74, 0.82))
    for k in range(3):  # estrelas desenhadas (sem caractere)
        a = 0.4 + 0.6 * abs(math.sin(t * 3 + k * 2))
        sx, sy = x - 130 + k * 120, y - 120 + (k % 2) * 40
        cap_line(c, sx - 12, sy, sx + 12, sy, WHITE, 5, a); cap_line(c, sx, sy - 12, sx, sy + 12, WHITE, 5, a)


def band(c, t, x, y, stretch, w=420):
    """elástico entre dois pinos (representa o músculo alongado)"""
    L = w * (0.55 + 0.45 * stretch)
    disk(c, x - L / 2, y, 30, STEEL); disk(c, x + L / 2, y, 30, STEEL)
    th = 46 * (1 - 0.6 * stretch)
    rrect(c, x - L / 2, y - th / 2, L, th, th / 2, mix(GRN, RED, stretch))


def sleeper(c, t, x, y, s=1.0, restless=0.0):
    """pessoa deitada na cama (só uma figura: a da cama)"""
    c.save(); c.translate(x, y); c.scale(s, s)
    jig = restless * 8 * math.sin(t * 7)
    c.translate(jig, 0)
    bed(c, 0, 0, 1.0, t)
    c.restore()


def tag_b(c, t, d, txt, col=YEL, fg=INK):
    tag(c, 540, 1745, txt, col, fg, 58, back_out(prog(t, d * 0.35, 0.3)))


def scene(fn, txt, col=YEL, fg=None, bg=True):
    fg = fg or (WHITE if col in (RED,) else INK)

    def f(c, t, d, b):
        if bg:
            gym(c, t)
        fn(c, t, d)
        tag_b(c, t, d, txt, col, fg)
    return wipe_in(f)


def finish(R, VIS, conc_items, cta_word, cta_title, cta_lines, cta_text):
    VIS["conc"] = wipe_in(conc_cards(conc_items))
    VIS["cta"] = wipe_in(cta_factory(cta_word, cta_title, cta_lines, cta_text), slide=0)
    return sfx_for(VIS, R.BEATS[-1])


# ------------------------------------------------------------------ fórmula "erro → consequência → volta" (usuário, 20/11)
def rewind_marks(c, x, y, s=1.0, a=1.0, fwd=False):
    """◀◀ (ou ▶▶) desenhado com triângulos — nunca como caractere de fonte"""
    d = 1 if fwd else -1
    for k in range(2):
        cx = x + d * k * 46 * s
        c.new_path(); c.move_to(cx + d * 40 * s, y); c.line_to(cx - d * 4 * s, y - 30 * s); c.line_to(cx - d * 4 * s, y + 30 * s); c.close_path()
        rgb(c, WHITE, a); c.fill()


def rewind_in(fn, prev_fn, prev_dur=3.0, dur=0.55):
    """entrada da cena 'Então...': primeiros `dur` s mostram a cena anterior voltando rápido (scanlines + ◀◀), depois a cena nova"""
    def f(c, t, d, b):
        if t < dur:
            k = t / dur
            prev_fn(c, max(0.0, prev_dur * (1 - k)), prev_dur, b)
            for i in range(0, 1920, 28):  # linhas horizontais de fita voltando
                y = (i + t * 2600) % 1920
                cap_line(c, 0, y, 1080, y, WHITE, 3, 0.18)
            rgb(c, (1, 1, 1), 0.06); c.paint()
            rewind_marks(c, 820, 360, 1.3, 0.95)
        else:
            fn(c, t - dur, d - dur, b)
    return f


def consequence(c, t, kind="x", x=740, y=1100, t0=0.4):
    """impacto visual do erro: tremida + marca vermelha"""
    p = prog(t, t0, 0.25)
    if p <= 0:
        return
    if kind == "x":
        icon_x(c, x, y, 1.4, p)
    elif kind == "drop":  # barra/linha despencando
        arrow(c, x, y - 200, x, y + 150 * ease(p), RED, 18, p)
    for k in range(6):
        a = k * 1.05 + t * 3
        cap_line(c, x + 90 * math.cos(a), y + 90 * math.sin(a), x + 140 * math.cos(a), y + 140 * math.sin(a), RED, 8, p * 0.8)
