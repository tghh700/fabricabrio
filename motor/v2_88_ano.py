"""BRIO 88 — um ano de academia (TESTE: antes/depois). Comparação explícita em split (duas figuras só aí)."""
from jornada_kit import *
import roteiro_brio_88_ano as R


def hook(c, t, d):
    act_walk(c, t, 300, 0.95)
    counter(c, t, 770, 950, 0, 365, size=170, col=YEL, t0=0.1, dur=1.4)
    caption(c, "DIAS DE TREINO", 770, 1070, back_out(prog(t, 0.3, 0.3)), WHITE)


def forca(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.55, lambda x: act_curl(c, t, x, 1.0, 3.4))
        tag(c, cx, by - 420, "30 KG", CARD, WHITE, 48, 1.0)

    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.55, lambda x: act_curl(c, t, x, 1.0, 2.4, heavy=True))
        tag(c, cx, by - 420, "55 KG", GRN, INK, 48, 1.0)
    split(c, t, L, Rr, "ANTES", "1 ANO", GREY, GRN)


def musculo(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.52, lambda x: act_pose(c, t, "idle", x, 1.0))

    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.58, lambda x: act_pose(c, t, "flex", x, 1.0))
        tag(c, cx, by - 440, "+2 A 5 KG", GRN, INK, 46, back_out(prog(t, d * 0.4, 0.3)))
    split(c, t, L, Rr, "ANTES", "1 ANO", GREY, GRN)


def espelho(c, t, d):
    def L(c, t, cx, by):
        mirror(c, t, cx, by, 0.45, big=False)

    def Rr(c, t, cx, by):
        mirror(c, t, cx, by, 0.45, big=True)
    split(c, t, L, Rr, "ANTES", "1 ANO", GREY, GRN)


def rotina(c, t, d):
    def L(c, t, cx, by):
        week(c, t, cx, by - 300, (1,), CARD, cell=44, t0=0.2)
        caption(c, "ESFORÇO", cx, by - 160, 1.0, GREY)

    def Rr(c, t, cx, by):
        week(c, t, cx, by - 300, (0, 1, 3, 4), GRN, cell=44, t0=0.5)
        caption(c, "HÁBITO", cx, by - 160, 1.0, GRN)
    split(c, t, L, Rr, "ANTES", "1 ANO", GREY, GRN)


def conc(c, t, d):
    act_pose(c, t, "flex", 300, 0.95)
    graph(c, t, 580, 880, 400, 440, [(0, 0.05), (0.2, 0.45), (0.4, 0.62), (0.6, 0.72), (0.8, 0.79), (1, 0.84)], GRN, 0.2, 1.4)
    c.save(); rgb(c, YEL, 0.18 * prog(t, 1.0, 0.4)); c.rectangle(580, 880, 80, 440); c.fill(); c.restore()
    caption(c, "1º ANO", 620, 1380, prog(t, 1.0, 0.3), YEL)


VIS = {
    "hook": scene(hook, "O QUE MUDA?", YEL),
    "forca": scene(forca, "FORÇA: PERTO DO DOBRO", GRN, bg=False),
    "musculo": scene(musculo, "MÚSCULO: +2 A 5 KG", GRN, bg=False),
    "espelho": scene(espelho, "A MANGA APERTA", GRN, bg=False),
    "rotina": scene(rotina, "VIRA HÁBITO", GRN, bg=False),
}
VIS["conc"] = wipe_in(lambda c, t, d, b: (conc(c, t, d), tag_b(c, t, d, "NÃO PARE NO MEIO", YEL, INK)))
VIS["cta"] = wipe_in(cta_factory("ANO", "UM ANO", [("MÊS 1 · 30 KG", WHITE), ("MÊS 6 · 45 KG", WHITE), ("MÊS 12 · 58 KG", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO")), slide=0)
SFX = sfx_for(VIS, R.BEATS[-1])
