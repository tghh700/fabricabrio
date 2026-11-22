"""BRIO 87 — 8 semanas pro verão: atalhos x plano simples (jornada de erros, ~1 min)."""
from jornada_kit import *
import roteiro_brio_87_verao as R


def hook(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6)
    sun(c, t, 900, 880, 70)
    counter(c, t, 700, 900, 8, 8, size=170, col=YEL, t0=0.05, dur=0.2)
    caption(c, "SEMANAS", 700, 1010, back_out(prog(t, 0.2, 0.3)), WHITE)
    rows(c, t, ("+ BRAÇO", "+ OMBRO"), x=770, y=1180, w=380, t0=d * 0.4, hot=-1, hot_col=YEL)


def duas(c, t, d):
    k = prog(t, 0, d * 0.5)
    if k < 1:
        act_curl(c, t, 300, 0.95, 3.2)
    else:
        act_tired(c, t, 300, 0.95)
    sun(c, t, 640, 880, 55); moon(c, t, 900, 880, 55)
    caption(c, "MANHÃ      NOITE", 770, 1010, prog(t, 0.2, 0.3), WHITE)
    battery(c, 770, 1290, lerp(0.95, 0.2, ease(prog(t, 0.5, d * 0.6))), "FORÇA", 160, 280)


def falha(c, t, d):
    act_curl_struggle(c, t, 300, 0.95)
    rows(c, t, ("SÉRIE 1 · FALHA", "SÉRIE 2 · FALHA", "SÉRIE 3 · FALHA"), x=770, y=830, hot=-1, hot_col=RED, size=40)
    barbell_load(c, t, 770, 1420, 20, RED, 0.7)
    consequence(c, t, "x", 960, 1240, d * 0.6)


def troca(c, t, d):
    act_pose(c, t, "shrug", 300, 0.95)
    names = ("TREINO A", "TREINO B", "TREINO C", "TREINO D")
    i = min(3, int(t / max(d / 4.5, 0.4)))
    phone_screen(c, 780, 1130, 0.75, lines=[(names[i], YEL), ("NOVO!", WHITE)], title="SEMANA " + str(i + 1))
    c.save(); c.translate(560, 900)
    draw_text(c, "?", 0, 0, 140 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", prog(t, d * 0.5, 0.3), align="center"); c.restore()


def sono(c, t, d):
    sleeper(c, t, 420, 1430, 0.6, restless=1.0)
    moon(c, t, 820, 880, 60)
    tag(c, 560, 920, "5 HORAS", RED, WHITE, 60, back_out(prog(t, 0.2, 0.3)))
    tag(c, 770, 1150, "BRAÇO: IGUAL", CARD, WHITE, 48, back_out(prog(t, d * 0.35, 0.3)))
    battery(c, 930, 1330, 0.2, None, 80, 150, RED) if prog(t, d * 0.5, 0.2) > 0 else None


def base(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6)
    week(c, t, 560, 860, (0, 1, 3, 4), GRN, cell=86, t0=0.1)
    tag(c, 770, 1150, "MESMO PLANO", GRN, INK, 54, back_out(prog(t, d * 0.35, 0.3)))
    caption(c, "POR 8 SEMANAS", 770, 1260, prog(t, d * 0.5, 0.3), WHITE)


def carga(c, t, d):
    act_curl(c, t, 300, 0.95, 2.6, heavy=True)
    rows(c, t, ("SEM 1 · 20 KG × 10", "SEM 2 · 20 KG × 11", "SEM 3 · 22 KG × 10"), x=770, y=830, size=40)
    moon(c, t, 700, 1290, 50)
    tag(c, 850, 1300, "7 HORAS", GRN, INK, 48, back_out(prog(t, d * 0.55, 0.3)))


def result(c, t, d):
    act_pose(c, t, "flex", 300, 0.95)
    bars(c, 770, 1300, 380, 440, (0.4, 0.85), t, 0.2, (GREY, GRN))
    for i, l in enumerate(("SEM 1", "SEM 8")):
        draw_text(c, l, 770 - 190 + (i + 0.5) * 190, 1350, 30, GREY, "Space Mono", 1.0, align="center")
    caption(c, "CARGA", 770, 830, prog(t, 0.2, 0.3), WHITE, 34)


VIS = {
    "hook": scene(hook, "8 SEMANAS", YEL),
    "duas": scene(duas, "A FORÇA CAI", RED),
    "falha": scene(falha, "DESTRUÍDO E PARADO", RED),
    "troca": scene(troca, "EVOLUIU? NÃO DÁ PRA SABER", RED),
    "sono": scene(sono, "O BRAÇO FICA IGUAL", RED, bg=False),
    "base": scene(base, "O SIMPLES", GRN),
    "carga": scene(carga, "+1 REPETIÇÃO OU +1 KG", GRN),
    "result": scene(result, "A CARGA SUBIU", GRN),
}
VIS["conc"] = wipe_in(lambda c, t, d, b: (concl(("MESMO PLANO", "CARGA SUBINDO", "DESCANSO"))(c, t, d), tag_b(c, t, d, "NÃO FOI O ATALHO", YEL, INK)))
VIS["cta"] = wipe_in(cta_factory("VERÃO", "VERÃO", [("SEM 1 · 10 REP", WHITE), ("SEM 4 · 12 REP", WHITE), ("SEM 8 · +6 KG", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO")), slide=0)
SFX = sfx_for(VIS, R.BEATS[-1])
