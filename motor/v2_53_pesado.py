from cenas_1611 import *
import roteiro_brio_53_pesado as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_squat(c, t, spd=2.2)
    draw_text(c, "BOMBADA?", 790, 1200, 120 * (1 + 0.04 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.15, 0.3)), align="center")

def nao(c, t, d):
    act_curl(c, t, heavy=True)
    p = back_out(prog(t, 0.1, 0.3))
    draw_text(c, "BOMBADA", 790, 1200, 110, GREY, "Anton", p, align="center")
    q = ease_out(prog(t, 0.5, 0.3))
    if q > 0:
        cap_line(c, 600, 1165, 600 + 380 * q, 1165, RED, 16)
    icon_x(c, 790, 1380, 1.0, prog(t, 0.7, 0.3))

def hormonio(c, t, d):
    act_curl(c, t)
    draw_text(c, "TESTOSTERONA", 780, 1010, 44, GREY, "Space Mono", prog(t, 0.1, 0.3), align="center", spacing=2)
    battery(c, 660, 1280, ease_out(prog(t, 0.2, 0.8)) * 0.92, "HOMEM", col=BLU)
    battery(c, 900, 1280, ease_out(prog(t, 0.5, 0.8)) * 0.12, "MULHER", col=YEL)

def anos(c, t, d):
    act_curl(c, t, spd=2.0)
    v = int(lerp(1, 5, ease_out(prog(t, 0.2, 1.4))))
    draw_text(c, f"{v} ANO" + ("S" if v > 1 else ""), 790, 1200, 150, YEL, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    for i in range(5):
        on = i < v
        rrect(c, 600 + i * 80, 1330, 60, 60, 14, GRN if on else CARD)

def forma(c, t, d):
    act_squat(c, t, spd=2.4)
    stack_list(c, t, ("FORÇA", "FIRMEZA", "FORMA"), 790, 1010, 380, 160, int(t * 1.5) % 3, num=False)

def leve(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0, spd=8.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0, spd=2.2, heavy=True))
    split(c, t, L, Rr, "LEVE × 50", "PESADO × 10", RED, GRN)

VIS = {"hook": scene(hook, "FICA BOMBADA?", YEL), "nao": scene(nao, "NÃO DO NADA", RED),
       "hormonio": scene(hormonio, "MENOS TESTOSTERONA", YEL), "anos": scene(anos, "VOLUME LEVA ANOS", YEL),
       "forma": scene(forma, "O PESO DÁ FORMA", GRN), "leve": scene(leve, "LEVE NÃO TONIFICA MAIS", RED, bg=False)}
SFX = finish(R, VIS, ("PESO NÃO INCHA", "FORÇA E FORMA", "VOLUME LEVA ANOS"), "PESADO", "AGACHAMENTO",
 [("SET: 30 KG × 10", WHITE), ("NOV: 40 KG × 10", WHITE), ("SUBIU 10 KG", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
