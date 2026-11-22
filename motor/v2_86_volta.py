"""BRIO 86 — voltar depois de meses parado (jornada de erros, ~1 min). Kit cenas_v2 + jornada_kit."""
from jornada_kit import *
import roteiro_brio_86_volta as R


def hook(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6, heavy=True)
    counter(c, t, 770, 900, 0, 90, size=150, col=RED, t0=0.1, dur=1.0)
    caption(c, "DIAS PARADO", 770, 1000, back_out(prog(t, 0.3, 0.3)))
    p = back_out(prog(t, d * 0.4, 0.3))
    if p > 0:
        barbell_load(c, t, 770, 1300, 40, YEL, 0.8)
        caption(c, "A CARGA DE ANTES", 770, 1450, p, WHITE)


def dor(c, t, d):
    stairs(c, 120, 1180, n=6, step=140, rise=75)
    fx, fy = stair_walker(c, t, 120, 1180, step=140, rise=75, n=6, s=0.62)
    pain_marks(c, t, fx + 20, fy - 120, 0.8, prog(t, 0.3, 0.3))
    tag(c, 790, 900, "DIA SEGUINTE", CARD, WHITE, 50, back_out(prog(t, 0.15, 0.3)))


def falta(c, t, d):
    act_tired(c, t, 300, 0.95)
    pain_marks(c, t, 335, 1460, 1.0, prog(t, 0.2, 0.3))
    week(c, t, 560, 860, range(5), RED, cell=86, t0=0.15)
    caption(c, "5 DIAS DE DOR", 560, 960, prog(t, 0.6, 0.3), RED)
    p = prog(t, d * 0.45, 0.3)
    week(c, t, 770, 1180, (), None, cell=56, t0=d * 0.45) if p > 0 else None
    if p > 0:
        caption(c, "TREINOS: 0", 770, 1270, p, WHITE)
        icon_x(c, 770, 1400, 0.8, prog(t, d * 0.6, 0.3))


def leve(c, t, d):
    act_curl(c, t, 300, 0.95, 3.4)
    rows(c, t, ("SEM 1 · 10 KG", "SEM 2 · 10 KG", "SEM 3 · 10 KG"), x=770, y=830, hot=2, hot_col=RED)
    graph(c, t, 600, 1230, 340, 200, [(0, 0.35), (0.5, 0.35), (1, 0.35)], RED, 1.4, 1.0)
    caption(c, "CARGA PARADA", 770, 1500, prog(t, d * 0.55, 0.3), RED)


def todo(c, t, d):
    k = prog(t, 0, d * 0.45)
    if k < 1:
        act_curl(c, t, 300, 0.95, 3.0)
    else:
        act_tired(c, t, 300, 0.95)
    week(c, t, 560, 860, range(7), GRN, cell=86, t0=0.1)
    battery(c, 770, 1250, lerp(0.95, 0.15, ease(prog(t, 0.6, d * 0.6))), "ENERGIA", 170, 300)
    if k >= 1:
        arrow(c, 930, 1120, 930, 1360, RED, 16, prog(t, d * 0.5, 0.4))


def metade(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6)
    barbell_load(c, t, 770, 1000, 40, CARD, 0.75)
    strike(c, 640, 888, 900, prog(t, 0.5, 0.3))
    p = back_out(prog(t, d * 0.35, 0.3))
    if p > 0:
        barbell_load(c, t, 770, 1320, 20, GRN, 0.75)
    caption(c, "4 SÉRIES  >  2 SÉRIES", 770, 1500, prog(t, d * 0.55, 0.3), WHITE)


def sobe(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6, heavy=True)
    rows(c, t, ("SEM 1 · 20 KG", "SEM 2 · 25 KG", "SEM 3 · 30 KG"), x=770, y=830)
    graph(c, t, 600, 1230, 340, 200, [(0, 0.15), (0.5, 0.5), (1, 0.85)], GRN, 1.4, 1.0)
    tag(c, 770, 1520, "DOR: 2 DIAS", GRN, INK, 44, back_out(prog(t, d * 0.55, 0.3)))


def memoria(c, t, d):
    act_pose(c, t, "flex", 300, 0.95)
    graph(c, t, 590, 900, 360, 420, [(0, 0.05), (0.25, 0.2), (0.5, 0.4), (0.75, 0.6), (1, 0.8)], GREY, 0.2, 1.2)
    graph(c, t, 590, 900, 360, 420, [(0, 0.3), (0.25, 0.65), (0.5, 0.8)], GRN, d * 0.35, 0.8)
    caption(c, "1ª VEZ", 880, 1380, prog(t, 0.8, 0.3), GREY)
    caption(c, "NA VOLTA", 700, 1430, prog(t, d * 0.5, 0.3), GRN)


VIS = {
    "hook": scene(hook, "MESMA CARGA DE ANTES", RED),
    "dor": scene(dor, "NEM DESCE A ESCADA", RED, bg=False),
    "falta": scene(falta, "SEMANA PERDIDA", RED, bg=False),
    "leve": scene(leve, "LEVE DEMAIS NÃO SOBE", RED),
    "todo": scene(todo, "TODO DIA ESGOTA", RED),
    "metade": scene(metade, "METADE DA CARGA", GRN),
    "sobe": scene(sobe, "UM POUCO POR SEMANA", GRN),
    "memoria": scene(memoria, "O MÚSCULO LEMBRA", GRN),
}
VIS["conc"] = wipe_in(lambda c, t, d, b: (concl(("METADE DA CARGA", "SOBE TODA SEMANA", "SEM PRESSA"))(c, t, d), tag_b(c, t, d, "COMECE PELA METADE", YEL, INK)))
VIS["cta"] = wipe_in(cta_factory("VOLTA", "VOLTA", [("SEM 1 · 20 KG", WHITE), ("SEM 2 · 25 KG", WHITE), ("SEM 4 · 40 KG", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO")), slide=0)
SFX = sfx_for(VIS, R.BEATS[-1])
