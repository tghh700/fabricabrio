from cenas_v2 import *
import roteiro_brio_37_semana as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    week(c, t, 540, 1050, (5,), YEL, cell=110)
    act_pose(c, t, "shrug", 330, 0.75)
    draw_text(c, "?", 780, 1560, 230 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", 1.0, align="center")

def sim(c, t, d):
    split(c, t, lambda c, t, cx, by: mini(c, cx, by, 0.72, lambda x: act_pose(c, t, "tired", x, 1.0)),
                lambda c, t, cx, by: mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0)),
          "0 DIAS", "1 DIA", RED, GRN)

def total(c, t, d):
    act_curl(c, t)
    n = int(min(12, t * 6))
    for i in range(12):
        x = 620 + (i % 4) * 100; y = 1450 - (i // 4) * 100
        rrect(c, x - 42, y - 42, 84, 84, 16, YEL if i < n else CARD)
    counter(c, t, 770, 1000, 0, 12, size=110, t0=0, dur=2.0, suffix=" SÉRIES")

def cansa(c, t, d):
    act_tired(c, t)
    battery(c, 800, 1150, lerp(1.0, 0.25, ease(prog(t, 0.2, d * 0.7))), "QUALIDADE", 170, 300)
    tag(c, 800, 1450, "ÚLTIMAS SÉRIES PIORAM", RED, WHITE, 40, back_out(prog(t, d * 0.5, 0.3)))

def dois(c, t, d):
    week(c, t, 540, 1050, (2, 5), GRN, cell=110)
    act_walk(c, t, 330, 0.75)
    draw_text(c, "2 TREINOS CURTOS", 760, 1450, 64, GRN, "Anton", back_out(prog(t, 0.8, 0.3)), align="center")

def corpo(c, t, d):
    act_squat(c, t)
    stack_list(c, t, ("AGACHAMENTO", "SUPINO", "REMADA"), 780, 1000, 470, 160)

VIS = {"hook": scene(hook, "SÓ 1 VEZ POR SEMANA?", YEL, bg=False), "sim": scene(sim, "É MELHOR QUE ZERO", GRN, bg=False),
       "total": scene(total, "CONTA O TOTAL DE SÉRIES", YEL), "cansa": scene(cansa, "TUDO NUM DIA CANSA", RED),
       "dois": scene(dois, "SE DER: 2 DIAS", GRN, bg=False), "corpo": scene(corpo, "1 DIA: CORPO TODO", YEL)}
SFX = finish(R, VIS, ("1 DIA > NENHUM", "2 DIAS É MELHOR", "NÃO FICA PARADO"), "SEMANA", "SUA SEMANA",
 [("SÁBADO: 12 SÉRIES", WHITE), ("SEMANA: 12 SÉRIES", WHITE), ("META: 2 DIAS", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
