"""BRIO 89 — manter o músculo nas férias (jornada de erros, ~1 min)."""
from jornada_kit import *
import roteiro_brio_89_ferias as R


def hook(c, t, d):
    act_walk(c, t, 300, 0.95)
    k = ease_out(prog(t, 0.2, 1.6))
    c.save(); c.translate(lerp(560, 900, k), lerp(1050, 880, k)); c.rotate(-0.15); plane(c, 0, 0, 0.9, YEL); c.restore()
    tag(c, 770, 1250, "DEZEMBRO", CARD, WHITE, 60, back_out(prog(t, 0.3, 0.3)))
    caption(c, "VIAGEM DE FIM DE ANO", 770, 1380, prog(t, d * 0.55, 0.3), WHITE)


def para(c, t, d):
    act_pose(c, t, "cheer", 300, 0.95)
    confetti(c, t, 300, 1000, 420, 300)
    counter(c, t, 770, 920, 2, 5, size=170, col=RED, t0=0.5, dur=1.6)
    caption(c, "SEMANAS SEM TREINO", 770, 1040, prog(t, 0.3, 0.3), WHITE)
    week(c, t, 770, 1250, (), None, cell=56, t0=0.3)
    cross_days(c, t, 770, 1250, range(7), cell=56, t0=0.8)


def hotel(c, t, d):
    k = prog(t, 0, d * 0.5)
    if k < 1:
        act_curl(c, t, 300, 0.95, 3.4)
    else:
        act_tired(c, t, 300, 0.95)
    counter(c, t, 770, 900, 0, 120, size=150, col=YEL, t0=0.1, dur=1.4, suffix=" MIN")
    caption(c, "DIA 1", 770, 1010, prog(t, 0.3, 0.3), WHITE)
    p = prog(t, d * 0.5, 0.3)
    if p > 0:
        tag(c, 770, 1200, "DIA 2", CARD, WHITE, 54, back_out(p))
        icon_x(c, 770, 1360, 0.9, prog(t, d * 0.6, 0.3))


def solto(c, t, d):
    act_pose(c, t, "shrug", 300, 0.95)
    week(c, t, 560, 860, (0, 4), GRN, cell=86, t0=0.1)
    cross_days(c, t, 560, 860, (1, 2, 3, 5, 6), cell=86, t0=0.6)
    c.save(); c.translate(780, 1200)
    draw_text(c, "?", 0, 0, 160 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", prog(t, d * 0.4, 0.3), align="center"); c.restore()
    caption(c, "SEM CONTAR NADA", 780, 1330, prog(t, d * 0.5, 0.3), WHITE)


def minimo(c, t, d):
    act_bwsquat(c, t, 300, 0.95)
    week(c, t, 560, 860, (0, 3), GRN, cell=86, t0=0.1)
    tag(c, 770, 1130, "2 × 30 MIN", GRN, INK, 60, back_out(prog(t, d * 0.35, 0.3)))
    caption(c, "COM O QUE TIVER", 770, 1250, prog(t, d * 0.5, 0.3), WHITE)


def como(c, t, d):
    act_bwsquat(c, t, 300, 0.95)
    rows(c, t, ("AGACHAMENTO", "FLEXÃO", "REMADA C/ MOCHILA"), x=770, y=830, hot=-1, hot_col=WHITE, size=42)
    backpack(c, 770, 1330, 0.9, back_out(prog(t, 1.4, 0.3)))


def mantem(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6)
    bars(c, 700, 1250, 300, 400, (0.9, 0.3), t, 0.2, (GREY, GRN))
    for i, l in enumerate(("NORMAL", "1/3")):
        draw_text(c, l, 700 - 150 + (i + 0.5) * 150, 1300, 30, GREY if i == 0 else GRN, "Space Mono", 1.0, align="center")
    caption(c, "TREINO", 700, 840, prog(t, 0.2, 0.3), WHITE)
    p = prog(t, d * 0.45, 0.3)
    if p > 0:
        battery(c, 940, 1080, 0.9, "MÚSCULO", 110, 200, GRN)


def janeiro(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6, heavy=True)
    tag(c, 770, 880, "JANEIRO", CARD, WHITE, 56, back_out(prog(t, 0.1, 0.3)))
    barbell_load(c, t, 770, 1250, 40, GRN, 0.8)
    check_mark(c, 770, 1430, 0.7, prog(t, d * 0.5, 0.3), GRN)


VIS = {
    "hook": scene(hook, "DEPOIS EU RECUPERO", YEL, bg=False),
    "para": scene(para, "2 VIRARAM 5", RED, bg=False),
    "hotel": scene(hotel, "DESISTIU NO 2º DIA", RED),
    "solto": scene(solto, "SEM PLANO", RED, bg=False),
    "minimo": scene(minimo, "MÍNIMO, MAS FIXO", GRN, bg=False),
    "como": scene(como, "PERTO DO LIMITE", GRN, bg=False),
    "mantem": scene(mantem, "1/3 DO TREINO MANTÉM", GRN),
    "janeiro": scene(janeiro, "SEM VOLTAR DO ZERO", GRN),
}
VIS["conc"] = wipe_in(lambda c, t, d, b: (concl(("2 TREINOS/SEMANA", "30 MINUTOS", "TODA SEMANA"))(c, t, d), tag_b(c, t, d, "O MÍNIMO SALVA", YEL, INK)))
VIS["cta"] = wipe_in(cta_factory("FÉRIAS", "FÉRIAS", [("SEG · 30 MIN", WHITE), ("QUI · 30 MIN", WHITE), ("2 DE 2 FEITOS", None)], ("REGISTRE SEUS TREINOS", "NO BRIO")), slide=0)
SFX = sfx_for(VIS, R.BEATS[-1])
