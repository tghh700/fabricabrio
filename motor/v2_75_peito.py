from cenas_2011 import *
import roteiro_brio_75_peito as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_bench(c, t)
    m = int(t * 1.6) % 3 + 1
    draw_text(c, f"MÊS {m}", 800, 900, 60, GREY, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    draw_text(c, "100 CM", 800, 1040, 120 * (1 + 0.03 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.15, 0.3)), align="center")
    icon_x(c, 990, 860, 0.7, prog(t, 0.6, 0.3))

def pouca(c, t, d):
    act_bench(c, t, s=0.8)
    counter(c, t, 820, 900, 0, 3, size=190, col=RED)
    draw_text(c, "SÉRIES NA SEMANA", 820, 1060, 34, GREY, "Space Mono", prog(t, 0.3, 0.3), align="center", spacing=1)
    icon_x(c, 820, 1170, 0.8, prog(t, 0.9, 0.3))

def dez(c, t, d):
    act_bench(c, t, s=0.8, spd=2.6)
    draw_text(c, "CRESCIMENTO", 810, 850, 36, GREY, "Space Mono", prog(t, 0.05, 0.3), align="center", spacing=2)
    bars(c, t, 810, 1250, (0.3, 0.95), ("< 5", "10+"), (RED, GRN), w=120, gap=50, h=330, step=0.4)

def carga(c, t, d):
    def L(c, t, cx, by):
        mini_bench(c, t, cx, by, 0.5)
        draw_text(c, "20 KG", cx, 1110, 80, RED, "Anton", 1.0, align="center")
        draw_text(c, "HÁ 3 MESES", cx, 1170, 30, GREY, "Space Mono", 1.0, align="center")
    def Rr(c, t, cx, by):
        mini_bench(c, t, cx, by, 0.5)
        v = lerp(20, 25, ease_out(prog(t, 0.8, 1.2)))
        draw_text(c, f"{v:.1f}".replace(".", ",").replace(",0", "") + " KG", cx, 1110, 80, GRN, "Anton", 1.0, align="center")
        draw_text(c, "SUBINDO", cx, 1170, 30, GREY, "Space Mono", 1.0, align="center")
    split(c, t, L, Rr, "PARADA", "SUBINDO", RED, GRN)

VIS = {"hook": scene(hook, "PEITO NÃO CRESCE?", RED), "pouca": scene(pouca, "3 SÉRIES NÃO BASTAM", RED),
       "dez": scene(dez, "10+ SÉRIES POR SEMANA", GRN), "carga": scene(carga, "A CARGA TEM QUE SUBIR", YEL, bg=False)}
SFX = finish(R, VIS, ("10 SÉRIES/SEMANA", "2 TREINOS", "CARGA SUBINDO"), "PEITO", "SUAS SÉRIES",
 [("SUPINO: 4 × 10", WHITE), ("CRUCIFIXO: 3 × 12", WHITE), ("10 SÉRIES NA SEMANA", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
