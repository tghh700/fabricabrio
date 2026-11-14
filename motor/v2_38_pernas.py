from cenas_v2 import *
import roteiro_brio_38_pernas as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    def L(c, t, cx, by): mini(c, cx - 30, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.72, lambda x: act_pose(c, t, "shrug", x, 1.0)); icon_x(c, cx + 120, by - 380, 0.8, prog(t, 0.9, 0.3))
    split(c, t, L, Rr, "DIA DE BRAÇO", "DIA DE PERNA", GRN, RED)

def maior(c, t, d):
    act_squat(c, t)
    bars(c, 770, 1480, 460, 470, (1.0, 0.62, 0.48, 0.3), t, 0.15, (YEL, BLU, BLU, BLU))
    for i, l in enumerate(("PERNA", "COSTAS", "PEITO", "BRAÇO")):
        draw_text(c, l, 770 - 230 + (i + 0.5) * 115, 1530, 26, GREY, "Space Mono", 1.0, align="center")

def desp(c, t, d):
    act_pose(c, t, "flex")
    bars(c, 770, 1480, 420, 470, (0.95, 0.9, 0.3), t, 0.15, (BLU, BLU, RED))
    for i, l in enumerate(("TRONCO", "BRAÇOS", "PERNAS")):
        draw_text(c, l, 770 - 210 + (i + 0.5) * 140, 1530, 28, GREY, "Space Mono", 1.0, align="center")

def ajuda(c, t, d):
    act_squat(c, t, HX, 0.95, 3.0)
    stack_list(c, t, ("AGACHAMENTO", "TERRA", "ESCADA"), 760, 1000, 460, 160)
    for i in range(3):
        icon_ok(c, 1065, 1000 + i * 160, 0.5, prog(t, 0.6 + i * 0.3, 0.3))

def curto(c, t, d):
    clock(c, 300, 1150, 140, t, 1.0)
    stack_list(c, t, ("2 EXERCÍCIOS", "3 SÉRIES CADA"), 740, 1050, 520, 170, 0, num=False)
    draw_text(c, "SEM 2 HORAS", 740, 1480, 64, GRN, "Anton", back_out(prog(t, 1.0, 0.3)), align="center")

def leve(c, t, d):
    act_squat(c, t, HX, 0.95, 2.4, 0.8)
    for i, (h, l) in enumerate(((0.35, "S1"), (0.55, "S2"), (0.75, "S3"))):
        p = ease_out(prog(t, 0.3 + i * 0.4, 0.4))
        x = 640 + i * 150
        rrect(c, x - 50, 1500 - 420 * h * p, 100, 420 * h * p + 1, 14, GRN)
        draw_text(c, l, x, 1550, 28, GREY, "Space Mono", 1.0, align="center")
    draw_text(c, "SEMANAS", 790, 1600, 28, GREY, "Space Mono", 1.0, align="center", spacing=2)
    arrow(c, 600, 1250, 950, 1000, YEL, 14, ease_out(prog(t, 1.4, 0.4)))

VIS = {"hook": scene(hook, "PULOU A PERNA?", RED, bg=False), "maior": scene(maior, "O MAIOR GRUPO DO CORPO", YEL),
       "desp": scene(desp, "PERNA ATRASADA", RED), "ajuda": scene(ajuda, "PERNA FORTE AJUDA", GRN),
       "curto": scene(curto, "NÃO PRECISA SER LONGO", YEL, bg=False), "leve": scene(leve, "COMEÇA LEVE E SOBE", GRN)}
SFX = finish(R, VIS, ("PERNA ENTRA NA SEMANA", "POUCOS EXERCÍCIOS", "BEM FEITOS"), "PERNAS", "SEU TREINO DE PERNA",
 [("AGACHAMENTO 3 × 10", WHITE), ("LEG PRESS 3 × 12", WHITE), ("SUBIU 5 KG", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
