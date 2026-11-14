from cenas_v2 import *
import roteiro_brio_34_ordem as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_pose(c, t, "shrug")
    items = ["ROSCA", "SUPINO", "AGACHAMENTO"]
    sw = ease(prog((t % 2.4), 0.6, 0.8)) if t > 0.6 else 0  # cartões trocando de lugar
    for i, s in enumerate(items):
        j = (i + 1) % 3
        y = lerp(960 + i * 160, 960 + j * 160, sw)
        card(c, 740, y, 520, 120, CARD, back_out(prog(t, 0.1 + i * 0.15, 0.3)))
        draw_text(c, s, 520, y + 22, 54, WHITE, "Anton", prog(t, 0.1 + i * 0.15, 0.3))
    draw_text(c, "?", 900, 1560, 220 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", 1.0, align="center")

def primeiro(c, t, d):
    act_squat(c, t, HX, 0.95, 2.6)
    battery(c, 800, 1100, 1.0, "ENERGIA", 170, 300)
    draw_text(c, "1º EXERCÍCIO", 800, 1420, 60, YEL, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def prior(c, t, d):
    act_pose(c, t, "point_up")
    stack_list(c, t, ("O QUE QUER EVOLUIR", "O RESTO", "O RESTO"), 740, 1000, 560, 160, 0)

def composto(c, t, d):
    split(c, t, lambda c, t, cx, by: mini(c, cx, by, 0.72, lambda x: act_squat(c, t, x, 1.0)),
                lambda c, t, cx, by: mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0)),
          "1º COMPOSTO", "DEPOIS ISOLADO", YEL, BLU)

def cansado(c, t, d):
    act_tired(c, t)
    battery(c, 800, 1150, lerp(1.0, 0.18, ease(prog(t, 0.2, d * 0.7))), "ENERGIA", 170, 300)
    icon_x(c, 800, 1460, 0.9, prog(t, d * 0.6, 0.3))

def atrasado(c, t, d):
    act_press(c, t)
    stack_list(c, t, ("OMBRO ATRASADO", "PEITO", "COSTAS"), 790, 1000, 470, 160, 0)

VIS = {"hook": scene(hook, "A ORDEM IMPORTA?", YEL), "primeiro": scene(primeiro, "O 1º RENDE MAIS", GRN),
       "prior": scene(prior, "COMEÇA PELO QUE IMPORTA", YEL), "composto": scene(composto, "COMPOSTOS ANTES", YEL, bg=False),
       "cansado": scene(cansado, "CANSADO, A CARGA CAI", RED), "atrasado": scene(atrasado, "ATRASADO? VAI 1º", YEL, bg=False)}
SFX = finish(R, VIS, ("O MELHOR VEM 1º", "COMPOSTOS ANTES", "ATRASADO PRIMEIRO"), "ORDEM", "SEU TREINO",
 [("1. AGACHAMENTO 90 KG", WHITE), ("2. SUPINO 60 KG", WHITE), ("3. ROSCA 14 KG", None)], ("ANOTE A CARGA DE CADA", "EXERCÍCIO NO BRIO"))
