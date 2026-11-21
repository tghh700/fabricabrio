"""BRIO 75 — por que você não cresce (jornada de erros, 1 min). Estilo atual: cenas_v2."""
from cenas_v2 import *
import roteiro_brio_75_cresce as R
BEAT_CTA = R.BEATS[-1]


# ------------------------------------------------------------------ peças próprias
def mirror(c, t, x, y, s=0.62, big=False):
    rrect(c, x - 150, y - 470, 300, 500, 26, (0.20, 0.23, 0.30)); rrect(c, x - 134, y - 454, 268, 468, 20, (0.27, 0.31, 0.40))
    cap_line(c, x - 90, y - 420, x - 40, y - 370, (1, 1, 1), 6, 0.18)
    mini(c, x, y - 10, s, lambda xx: act_pose(c, t, "flex" if big else "idle", xx, 1.0))


def plate(c, t, x, y, fill, junk=False, r=150):
    disk(c, x, y, r + 14, (0.85, 0.84, 0.80)); disk(c, x, y, r, (0.95, 0.94, 0.91))
    items = ([(0.95, 0.75, 0.25), (0.82, 0.25, 0.18), (0.55, 0.32, 0.18), (0.95, 0.85, 0.3), (0.82, 0.25, 0.18), (0.55, 0.32, 0.18)] if junk
             else [(0.98, 0.93, 0.78), (0.48, 0.30, 0.20), (0.30, 0.65, 0.35), (0.98, 0.93, 0.78), (0.30, 0.65, 0.35)])
    pos = [(-60, -30), (50, -45), (0, 50), (-55, 55), (60, 40), (5, -5)]
    for i, col in enumerate(items):
        a = clamp(fill * len(items) - i)
        if a > 0:
            dx, dy = pos[i % len(pos)]; disk(c, x + dx, y + dy, 46 * back_out(min(a, 1)), col)


def belly_fig(c, t, x, belly, s=0.95):
    """boneco em pé com barriga crescendo (elipse do mesmo creme na frente do tronco)"""
    act_pose(c, t, "idle", x, s)
    by = FLOOR_Y - 400 * s
    c.save(); c.translate(x + 30 * s, by); c.scale((70 + 70 * belly) * s, (80 + 40 * belly) * s); disk(c, 0, 0, 1, L_BODY); c.restore()


def tape_arm(c, t, x, y, val, col=None, label_="BRAÇO"):
    rrect(c, x - 150, y - 50, 300, 100, 24, CARD)
    draw_text(c, label_, x - 120, y + 12, 30, GREY, "Space Mono", 1.0, align="left", spacing=2)
    draw_text(c, val, x + 125, y + 22, 64, col or WHITE, "Anton", 1.0, align="right")


def puzzle(c, t, x, y, labels, n_in, t0=0.2):
    for i, s in enumerate(labels):
        p = back_out(prog(t, t0 + i * 0.45, 0.35)) if i < n_in else 0.0
        bx = x + (i - (len(labels) - 1) / 2) * 190
        rrect(c, bx - 88, y - 88, 176, 176, 22, CARD)
        if p > 0:
            c.save(); c.translate(bx, y + (1 - min(p, 1)) * -260); rrect(c, -80, -80, 160, 160, 20, YEL if i == len(labels) - 1 else GRN)
            disk(c, 80, 0, 26, YEL if i == len(labels) - 1 else GRN); c.restore()
            draw_text(c, s, bx, y + 140, 30, WHITE, "Anton", min(p, 1), align="center")


def barbell_load(c, t, x, y, kg, col=None, s=1.0):
    cap_line(c, x - 260 * s, y, x + 260 * s, y, STEEL, 14 * s)
    for sd in (-1, 1):
        rrect(c, x + sd * 200 * s - 20 * s, y - 90 * s, 40 * s, 180 * s, 10 * s, (0.3, 0.32, 0.38))
    tag(c, x, y - 150 * s, f"{kg} KG", col or CARD, WHITE if col in (None, RED) else INK, 54, 1.0)


def graph(c, t, x, y, w, h, pts, col, t0=0.2, dur=1.4):
    cap_line(c, x, y + h, x + w, y + h, (1, 1, 1), 4, 0.25)
    p = ease_out(prog(t, t0, dur)); n = max(2, int(len(pts) * p + 0.999))
    xy = [(x + px * w, y + h - py * h) for px, py in pts[:n]]
    poly(c, xy, col, 12)
    for px, py in xy:
        disk(c, px, py, 12, col)


# ------------------------------------------------------------------ cenas
def hook(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6)
    week(c, t, 560, 860, range(7), GRN, cell=86, t0=0.2)
    mirror(c, t, 800, 1500, 0.55)
    tag(c, 800, 1590, "2 MESES DEPOIS", CARD, WHITE, 36, back_out(prog(t, d * 0.55, 0.3)))
    icon_x(c, 930, 1020, 0.7, prog(t, d * 0.7, 0.3))


def descanso(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.7, lambda x: act_tired(c, t, x, 1.0))
    def Rr(c, t, cx, by): sleeper(c, t, cx, by - 120, 0.5); battery(c, cx + 140, by - 380, lerp(0.2, 1.0, ease(prog(t, 0.6, d * 0.6))), None, 70, 140, GRN)
    split(c, t, L, Rr, "TREINO TODO DIA", "DESCANSO", RED, GRN)


def pouco(c, t, d):
    week(c, t, 560, 860, (0, 2, 3, 5), GRN, cell=86)
    act_curl(c, t, 300, 0.95, 2.6)
    plate(c, t, 780, 1180, 0.25)
    tag(c, 780, 1380, "PRATO VAZIO", RED, WHITE, 44, back_out(prog(t, d * 0.45, 0.3)))


def barriga(c, t, d):
    b = ease(prog(t, 0.4, d * 0.7))
    belly_fig(c, t, 300, b)
    plate(c, t, 780, 1000, ease(prog(t, 0.2, 1.0)), junk=True)
    tape_arm(c, t, 780, 1290, "= 32 CM", RED)


def calorias(c, t, d):
    belly_fig(c, t, 300, 0.35)
    counter(c, t, 780, 900, 0, 300, size=170, col=YEL, t0=0.2, dur=1.2, suffix="")
    draw_text(c, "KCAL A MAIS", 780, 990, 34, GREY, "Space Mono", 1.0, align="center", spacing=2)
    tape_arm(c, t, 780, 1180, "= 32 CM", GREY, "BARRIGA")
    tape_arm(c, t, 780, 1320, "= 32 CM", RED, "BRAÇO")


def proteina(c, t, d):
    act_curl(c, t, 300, 0.95, 2.2)
    k = prog(t, 0, d * 0.45)
    if k < 1:
        bars(c, 780, 1300, 360, 480, (0.45, 0.95), t, 0.15, (GREY, GRN))
        for i, l in enumerate(("ANTES", "2 G/KG")):
            draw_text(c, l, 780 - 180 + (i + 0.5) * 180, 1350, 28, GREY, "Space Mono", 1.0, align="center")
    else:
        sleeper(c, t, 780, 1210, 0.55, restless=1.0)
        tag(c, 780, 950, "5 HORAS", RED, WHITE, 60, back_out(prog(t, d * 0.45, 0.3)))
        battery(c, 960, 1180, 0.25, None, 70, 140, RED)


def sono(c, t, d):
    k = prog(t, 0, d * 0.4)
    if k < 1:
        sleeper(c, t, 600, 1260, 0.6)
        moon(c, t, 760, 820, 70)
        battery(c, 900, 1100, lerp(0.25, 1.0, ease(k)), None, 80, 160, GRN)
        tag(c, 560, 960, "8 HORAS", GRN, INK, 60, back_out(prog(t, 0.3, 0.3)))
    else:
        act_curl(c, t, 300, 0.95, 2.6, heavy=True)
        barbell_load(c, t, 760, 1100, 20, RED, 0.9)
        graph(c, t, 590, 1250, 340, 200, [(0, 0.4), (0.33, 0.4), (0.66, 0.4), (1, 0.4)], RED, d * 0.42, 1.0)
        draw_text(c, "3 MESES", 760, 1520, 30, GREY, "Space Mono", 1.0, align="center", spacing=2)


def anota(c, t, d):
    act_pose(c, t, "shrug", 300, 0.95)
    c.save(); c.translate(360, 760); draw_text(c, "?", 0, 0, 160 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", 1.0, align="center"); c.restore()
    barbell_load(c, t, 770, 1000, 20, CARD, 0.85)
    graph(c, t, 600, 1180, 340, 220, [(0, 0.35), (0.25, 0.35), (0.5, 0.35), (0.75, 0.35), (1, 0.35)], RED, 0.3, 1.2)
    icon_x(c, 950, 1150, 0.6, prog(t, d * 0.6, 0.3))


def sobe(c, t, d):
    act_curl(c, t, 300, 0.95 + 0.06 * ease(prog(t, 0.5, d * 0.8)), 2.6, heavy=True)
    rows = ("SEM 1 · 20 KG", "SEM 2 · 21 KG", "SEM 3 · 22 KG")
    for i, s in enumerate(rows):
        p = back_out(prog(t, 0.2 + i * 0.5, 0.3))
        card(c, 770, 780 + i * 120, 460, 96, CARD, p)
        if p > 0:
            draw_text(c, s, 570, 800 + i * 120, 44, GRN if i == 2 else WHITE, "Anton", p)
    graph(c, t, 590, 1150, 360, 260, [(0, 0.2), (0.33, 0.4), (0.66, 0.62), (1, 0.9)], GRN, 1.4, 1.3)


def conc(c, t, d):
    act_pose(c, t, "flex", 540, 0.8)
    puzzle(c, t, 540, 830, ("DESCANSO", "COMIDA", "SONO", "CARGA"), 4, 0.2)


VIS = {
    "hook": scene(hook, "2 MESES. NADA.", RED, bg=False),
    "descanso": scene(descanso, "CRESCE NO DESCANSO", GRN, bg=False),
    "pouco": scene(pouco, "COMENDO POUCO", RED, bg=False),
    "barriga": scene(barriga, "BARRIGA CRESCE PRIMEIRO", RED, bg=False),
    "calorias": scene(calorias, "BARRIGA PAROU. BRAÇO TAMBÉM.", YEL, bg=False),
    "proteina": scene(proteina, "SEM SONO, SEM FORÇA", RED, bg=False),
    "sono": scene(sono, "MESMO PESO DE SEMPRE", RED, bg=False),
    "anota": scene(anota, "SEM ANOTAR, NÃO SOBE", RED, bg=False),
    "sobe": scene(sobe, "+1 QUILO POR SEMANA", GRN),
}
VIS["conc"] = wipe_in(lambda c, t, d, b: (conc(c, t, d), tag_b(c, t, d, "A PEÇA QUE FALTAVA", YEL, INK)))
VIS["cta"] = wipe_in(cta_factory("CARGA", "SUA CARGA", [("ROSCA 20 KG", WHITE), ("ROSCA 21 KG", WHITE), ("ROSCA 22 KG", None)], ("ANOTE SUAS SÉRIES", "NO BRIO")), slide=0)
SFX = sfx_for(VIS, R.BEATS[-1])
