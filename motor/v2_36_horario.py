from cenas_v2 import *
import roteiro_brio_36_horario as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    def L(c, t, cx, by):
        sun(c, t, cx + 140, by - 110, 34); mini(c, cx - 40, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by):
        moon(c, t, cx + 120, by - 100, 40); mini(c, cx - 40, by, 0.72, lambda x: act_curl(c, t + 1, x, 1.0))
    split(c, t, L, Rr, "MANHÃ", "NOITE", YEL, BLU)

def estudos(c, t, d):
    clock(c, 300, 1150, 150, t, 2.0)
    bars(c, 760, 1450, 480, 420, (0.93, 0.96, 1.0, 0.97), t, 0.15, (BLU, BLU, YEL, BLU))
    for i, l in enumerate(("7H", "12H", "17H", "21H")):
        draw_text(c, l, 760 - 240 + (i + 0.5) * 120, 1500, 30, GREY, "Space Mono", 1.0, align="center")

def tarde(c, t, d):
    sun(c, t, 820, lerp(950, 1080, ease(prog(t, 0, d))), 80)
    act_curl(c, t, HX, 0.95, 2.6, heavy=True)
    tag(c, 790, 1330, "UM POUCO MAIS DE FORÇA", YEL, INK, 42, back_out(prog(t, 0.5, 0.3)))

def pequena(c, t, d):
    act_pose(c, t, "shrug")
    bars(c, 780, 1500, 360, 480, (0.96, 1.0), t, 0.15, (BLU, YEL))
    for i, l in enumerate(("MANHÃ", "TARDE")):
        draw_text(c, l, 780 - 180 + (i + 0.5) * 180, 1550, 30, GREY, "Space Mono", 1.0, align="center")
    tag(c, 780, 920, "QUASE IGUAL", CARD, WHITE, 50, back_out(prog(t, 0.8, 0.3)))

def repetir(c, t, d):
    act_walk(c, t)
    for r in range(3):
        week(c, t, 760, 1020 + r * 150, (0, 2, 4), GRN, cell=62, t0=0.2 + r * 0.5)

def escolhe(c, t, d):
    act_pose(c, t, "point_up")
    calendar(c, 760, 1170, 7, 4, 58, int(min(28, t * 12)), t, 0.0, 8, None, GRN)
    draw_text(c, "4 SEMANAS", 760, 1480, 70, YEL, "Anton", back_out(prog(t, 0.5, 0.3)), align="center")

VIS = {"hook": scene(hook, "MANHÃ OU NOITE?", YEL, bg=False), "estudos": scene(estudos, "A FORÇA VARIA POUCO", BLU, bg=False),
       "tarde": scene(tarde, "FIM DA TARDE", YEL), "pequena": scene(pequena, "DIFERENÇA PEQUENA", BLU),
       "repetir": scene(repetir, "O QUE VOCÊ REPETE", GRN), "escolhe": scene(escolhe, "ESCOLHE E MANTÉM", YEL)}
SFX = finish(R, VIS, ("PERFEITO NÃO EXISTE", "O QUE VOCÊ MANTÉM", "4 SEMANAS"), "HORA", "SEU HORÁRIO",
 [("SEG 18:00 FEITO", WHITE), ("QUA 18:00 FEITO", WHITE), ("SEX 18:00 FEITO", None)], ("REGISTRE SEU TREINO", "NO BRIO"))
