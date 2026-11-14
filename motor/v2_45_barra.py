from cenas_1511 import *
import roteiro_brio_45_barra as R
BEAT_CTA = R.BEATS[-1]
BY = 960

def hook(c, t, d):
    u = 0.18 * (0.5 - 0.5 * math.cos(t * 5))  # tenta subir e não sai do lugar
    hanger(c, 360, BY, 0.8, u)
    counter(c, t, 820, 1250, 0, 0, "{:.0f}", 220, RED, 0.1, 0.2)
    draw_text(c, "BARRAS", 820, 1420, 54, GREY, "Space Mono", 1.0, align="center", spacing=3)

def normal(c, t, d):
    hanger(c, 360, BY, 0.8, 0.1 * (0.5 - 0.5 * math.cos(t * 4)))
    p = ease_out(prog(t, 0.3, 0.8))
    card(c, 850, 1250, 320, 300, CARD, back_out(prog(t, 0.2, 0.3)))
    draw_text(c, "100%", 850, 1250, 110, YEL, "Anton", p, align="center")
    draw_text(c, "DO SEU PESO", 850, 1330, 40, GREY, "Anton", p, align="center")

def negativa(c, t, d):
    T = 6.0; f = t % T
    u = 1.0 if f < 0.6 else max(0.0, 1 - (f - 0.6) / 5.0)
    hanger(c, 360, BY, 0.8, u, box=f < 0.6)
    sec = 0 if f < 0.6 else min(5, int(f - 0.6) + 1)
    draw_text(c, f"{sec} s", 830, 1300, 200, YEL, "Anton", 1.0, align="center")
    draw_text(c, "DESCENDO", 830, 1440, 46, GRN, "Space Mono", 1.0, align="center", spacing=3)

def pendura(c, t, d):
    hanger(c, 360, BY, 0.8, 0.0)
    clock(c, 830, 1250, 140, t, 1.0)
    draw_text(c, "SEGURA", 830, 1480, 64, GRN, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def semana(c, t, d):
    T = 2.4; f = t % T
    u = 1.0 if f < 0.3 else max(0.0, 1 - (f - 0.3) / 2.0)
    hanger(c, 330, BY, 0.8, u, box=f < 0.3)
    week(c, t, 790, 1100, (0, 2, 4), GRN, cell=74)
    draw_text(c, "3 A 5", 790, 1430, 110 * (1 + 0.04 * math.sin(t * 5)), YEL, "Anton", back_out(prog(t, 0.5, 0.3)), align="center")
    draw_text(c, "DESCIDAS", 790, 1520, 40, GREY, "Space Mono", 1.0, align="center", spacing=3)

def puxada(c, t, d):
    stack_machine(c, 790, 1640, 0.95, 0.5 - 0.5 * math.cos(t * 2.4), hi=BLU)
    battery(c, 330, 1250, lerp(0.25, 0.95, ease(prog(t, 0.2, d * 0.7))), "COSTAS", 170, 300, GRN)

VIS = {"hook": scene(hook, "NEM UMA BARRA?", RED, bg=False), "normal": scene(normal, "É O CORPO INTEIRO", YEL, bg=False),
       "negativa": scene(negativa, "NEGATIVA: DESCE DEVAGAR", GRN, bg=False), "pendura": scene(pendura, "FICA PENDURADO", YEL, bg=False),
       "semana": scene(semana, "2 A 3 VEZES NA SEMANA", GRN, bg=False), "puxada": scene(puxada, "PUXADA AJUDA", BLU, bg=False)}
SFX = finish(R, VIS, ("PRIMEIRO DESCER", "DEPOIS SUBIR", "A 1ª BARRA VEM"), "BARRA", "BARRA FIXA",
 [("NEGATIVAS: 3 × 5 s", WHITE), ("PENDURADO: 30 s", WHITE), ("1ª BARRA!", None)], ("REGISTRE SUAS DESCIDAS", "NO BRIO"))
