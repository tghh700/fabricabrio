from cenas_2111 import *
import roteiro_brio_81_gelo as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    ice_tub(c, t, 780, 1180, 0.75, back_out(prog(t, 0.1, 0.35)))
    draw_text(c, "AJUDA?", 790, 950, 120 * (1 + 0.03 * math.sin(t * 5)), YEL, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def sinal(c, t, d):
    act_curl(c, t)
    k = ease(prog(t, 0.6, 1.2))
    sparks_up(c, t, 800, 1400, 6, YEL, 1 - 0.8 * k, 260)
    for i in range(4):
        snowflake(c, 680 + i * 80, 1450 - 50 * math.sin(t * 2 + i), 32, k)
    draw_text(c, "SINAL DE", 800, 900, 44, GREY, "Space Mono", prog(t, 0.05, 0.3), align="center", spacing=2)
    draw_text(c, "CRESCER", 800, 990, 80, mix(YEL, BLU, k), "Anton", back_out(prog(t, 0.1, 0.3)), align="center")
    icon_x(c, 1010, 960, 0.6, prog(t, 1.4, 0.3))

def estudo(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_curl(c, t, x, 1.0))
        for k in range(3):
            ice_cube(c, cx + 110 + (k % 2) * 50, by - 120 - k * 70, 24, 1.0, 0.3 * k)
    split(c, t, L, Rr, "SÓ TREINO", "+ GELO", GRN, BLU)
    q = ease_out(prog(t, 1.0, 1.0))
    rrect(c, 120, 1022, 340, 26, 13, (0.12, 0.13, 0.17)); rrect(c, 120, 1022, 340 * 0.85 * q, 26, 13, GRN)
    rrect(c, 620, 1022, 340, 26, 13, (0.12, 0.13, 0.17)); rrect(c, 620, 1022, 340 * 0.55 * q, 26, 13, BLU)
    draw_text(c, "12 SEMANAS", 540, 860, 48, WHITE, "Anton", back_out(prog(t, 0.9, 0.3)), align="center")
    draw_text(c, "MÚSCULO E FORÇA", 540, 1090, 32, GREY, "Space Mono", prog(t, 1.2, 0.3), align="center", spacing=1)

def quem(c, t, d):
    act_walk(c, t, spd=7.0)
    card(c, 790, 1000, 400, 150, CARD, back_out(prog(t, 0.05, 0.3)))
    draw_text(c, "JOGO AMANHÃ", 760, 1020, 52, WHITE, "Anton", prog(t, 0.1, 0.3), align="center")
    icon_ok(c, 960, 960, 0.55, prog(t, 0.4, 0.3))
    card(c, 790, 1250, 400, 150, CARD, back_out(prog(t, 0.6, 0.3)))
    draw_text(c, "QUER CRESCER", 760, 1270, 52, WHITE, "Anton", prog(t, 0.65, 0.3), align="center")
    icon_x(c, 960, 1210, 0.55, prog(t, 0.9, 0.3))

VIS = {"hook": scene(hook, "BANHO DE GELO AJUDA?", YEL), "sinal": scene(sinal, "PODE ATRAPALHAR", RED),
       "estudo": scene(estudo, "GANHOU MENOS MÚSCULO", BLU, bg=False), "quem": scene(quem, "SERVE PRA QUEM COMPETE", YEL)}
SFX = finish(R, VIS, ("GELO APAGA O SINAL", "MENOS MÚSCULO", "GELO LONGE DO TREINO"), "GELO", "SUA EVOLUÇÃO",
 [("ROSCA: 12 KG × 10", WHITE), ("ROSCA: 14 KG × 10", WHITE), ("+2 KG NO MÊS", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
