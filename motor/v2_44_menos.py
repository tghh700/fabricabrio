from cenas_1511 import *
import roteiro_brio_44_menos as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t, HX, 0.95, 3.2)
    items = ("ROSCA DIRETA", "ROSCA MARTELO", "ROSCA SCOTT", "ROSCA CONCENTRADA", "ROSCA NO CABO")
    for i, s in enumerate(items):
        p = back_out(prog(t, 0.1 + i * 0.18, 0.25))
        if p <= 0: continue
        card(c, 790, 900 + i * 125, 470, 100, CARD, p)
        draw_text(c, s, 790, 900 + i * 125 + 18, 42, WHITE, "Anton", p, align="center")
    draw_text(c, "5?", 790, 1600, 120, RED, "Anton", back_out(prog(t, 1.1, 0.3)), align="center")

def rende(c, t, d):
    act_curl(c, t, HX, 0.95)
    vals = (1.0, 0.8, 0.6, 0.42, 0.28, 0.18, 0.12, 0.08)
    p = ease_out(prog(t, 0.2, 1.4))
    for i, v in enumerate(vals):
        if i / len(vals) > p: break
        x = 580 + i * 58
        h = 380 * v
        rrect(c, x - 22, 1500 - h, 44, h, 10, GRN if i < 4 else RED)
    draw_text(c, "SÉRIES NO TREINO", 790, 1560, 30, GREY, "Space Mono", 1.0, align="center", spacing=2)

def cansa(c, t, d):
    act_tired(c, t)
    battery(c, 690, 1150, lerp(0.9, 0.15, ease(prog(t, 0.2, d * 0.7))), "ENERGIA", 140, 260)
    battery(c, 900, 1150, lerp(0.3, 0.38, ease(prog(t, 0.2, d * 0.7))), "ESTÍMULO", 140, 260, BLU)

def faixa(c, t, d):
    act_curl(c, t, HX, 0.95, 2.6)
    n = int(min(8, t * 5))
    for i in range(8):
        x = 610 + (i % 4) * 110; y = 1050 + (i // 4) * 120
        rrect(c, x - 45, y - 45, 90, 90, 18, YEL if i < n else CARD)
    draw_text(c, "6 A 8 SÉRIES", 775, 1450, 90, YEL, "Anton", back_out(prog(t, 1.4, 0.3)), align="center")

def divide(c, t, d):
    act_walk(c, t, HX, 0.95)
    week(c, t, 780, 1250, (1, 4), GRN, cell=70)
    draw_text(c, "2 TREINOS", 780, 1450, 70, GRN, "Anton", back_out(prog(t, 0.9, 0.3)), align="center")

def qualidade(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t * 2.2, x, 1.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl_tempo(c, t, x, 1.0, down=1.4, up=0.8))
    split(c, t, L, Rr, "5 NO AUTOMÁTICO", "2 BEM FEITOS", RED, GRN)

VIS = {"hook": scene(hook, "EXAGERO", RED, bg=False), "rende": scene(rende, "CADA SÉRIE RENDE MENOS", YEL),
       "cansa": scene(cansa, "SÓ SOMA CANSAÇO", RED), "faixa": scene(faixa, "REFERÊNCIA POR TREINO", YEL),
       "divide": scene(divide, "O RESTO EM OUTRO DIA", GRN, bg=False), "qualidade": scene(qualidade, "BEM FEITO VALE MAIS", GRN, bg=False)}
SFX = finish(R, VIS, ("POUCAS SÉRIES DURAS", "BEM FEITAS", "O RESTO OUTRO DIA"), "MENOS", "TREINO DE BRAÇO",
 [("ROSCA: 3 SÉRIES", WHITE), ("MARTELO: 3 SÉRIES", WHITE), ("6 SÉRIES DURAS", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
