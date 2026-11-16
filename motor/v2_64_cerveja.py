from cenas_1711 import *
import roteiro_brio_64_cerveja as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    beer(c, t, 790, 1240, 1.0, back_out(prog(t, 0.1, 0.3)))
    draw_text(c, "?", 990, 1060, 160, YEL, "Anton", back_out(prog(t, 0.5, 0.3)), align="center")

def depende(c, t, d):
    act_walk(c, t, spd=4.0)
    n = 1 + int(clamp(prog(t, 0.2, d * 0.7)) * 5.99)
    for i in range(6):
        beer(c, t, 580 + (i % 3) * 190, 1080 + (i // 3) * 330, 0.55, back_out(prog(t, 0.2 + i * d * 0.12, 0.25)))
    draw_text(c, "DOSE", 790, 1560, 44, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center", spacing=3)

def estudo(c, t, d):
    act_tired(c, t)
    for i in range(3):
        beer(c, t, 600 + i * 190, 1100, 0.5, back_out(prog(t, 0.05 + i * 0.15, 0.25)))
    muscle_fiber(c, t, 790, 1370, 360, 110, prog(t, 0.6, 0.3), lerp(1.0, 0.75, ease(prog(t, 0.9, 1.0))))
    draw_text(c, "FABRICAÇÃO DE MÚSCULO", 790, 1500, 32, GREY, "Space Mono", prog(t, 0.7, 0.3), align="center", spacing=1)

def numero(c, t, d):
    act_tired(c, t)
    counter(c, t, 790, 1100, 0, 37, "-{:.0f}", 200, RED, suffix="%")
    bars(c, t, 790, 1470, (0.9, 0.57), ("NORMAL", "PORRE"), (GRN, RED), w=150, gap=110, h=260, t0=0.5)

def sono(c, t, d):
    sleeper(c, t, 700, 1380, 0.95, restless=1.0)
    moon(c, t, 830, 1000, 70)
    beer(c, t, 960, 1180, 0.45, back_out(prog(t, 0.1, 0.3)))

def uma(c, t, d):
    def L(c, t, cx, by):
        beer(c, t, cx - 70, by - 260, 0.55, 1.0); beer(c, t, cx + 90, by - 260, 0.55, 1.0)
        icon_ok(c, cx, by - 70, 0.9, prog(t, 0.9, 0.3))
    def Rr(c, t, cx, by):
        for i in range(6):
            beer(c, t, cx - 120 + (i % 3) * 120, by - 380 + (i // 3) * 170, 0.38, 1.0)
        icon_x(c, cx, by - 70, 0.9, prog(t, 1.3, 0.3))
    split(c, t, L, Rr, "UMA OU DUAS", "PORRE", GRN, RED)

VIS = {"hook": scene(hook, "CERVEJA ESTRAGA?", YEL), "depende": scene(depende, "DEPENDE DA DOSE", YEL),
       "estudo": scene(estudo, "PORRE PÓS-TREINO", RED), "numero": scene(numero, "ATÉ 37% A MENOS", RED),
       "sono": scene(sono, "E PIORA O SONO", RED, bg=False), "uma": scene(uma, "O PROBLEMA É O PORRE", YEL, bg=False)}
SFX = finish(R, VIS, ("1 OU 2: TRANQUILO", "PORRE: ATRAPALHA", "LONGE DO TREINO"), "CERVEJA", "SEUS TREINOS",
 [("SEXTA: 60 KG × 8", WHITE), ("SEGUNDA: 60 KG × 8", WHITE), ("CARGA SEGUROU", None)], ("REGISTRE SEUS TREINOS", "NO BRIO"))
