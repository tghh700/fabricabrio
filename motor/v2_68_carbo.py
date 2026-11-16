from cenas_1711 import *
import roteiro_brio_68_carbo as R
BEAT_CTA = R.BEATS[-1]

def rice(c, x, y, s=1.0, p=1.0):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -120, -10, 240, 90, 40, WHITE)
    for k in range(7):
        disk(c, -90 + k * 30, -10 - 18 * math.sin(k * 0.45), 26, (0.97, 0.96, 0.9))
    c.restore()

def hook(c, t, d):
    act_walk(c, t, spd=4.0)
    rice(c, 790, 1220, 1.3, back_out(prog(t, 0.05, 0.3)))
    x_mark(c, 790, 1200, 1.5, prog(t, 0.5, 0.3), RED)

def rapido(c, t, d):
    act_walk(c, t, spd=8.0)
    v = lerp(80.0, 77.5, ease(prog(t, 0.2, 1.4)))
    bath_scale(c, 790, 1460, f"{v:.1f}".replace(".", ","), back_out(prog(t, 0.05, 0.3)), GRN)
    draw_text(c, "1ª SEMANA", 790, 1100, 60, WHITE, "Anton", back_out(prog(t, 0.3, 0.3)), align="center")

def agua(c, t, d):
    act_tired(c, t)
    muscle_fiber(c, t, 790, 1150, 380, 140, 1.0, lerp(1.0, 0.85, ease(prog(t, 0.3, 1.0))))
    for i in range(5):
        f = (t * 0.8 + i / 5) % 1
        droplet(c, 630 + i * 80, 1240 + 220 * f, 0.9, 1 - f)
    tag(c, 790, 1000, "ÁGUA, NÃO GORDURA", BLU, INK, 44, back_out(prog(t, 0.6, 0.3)))

def estudo(c, t, d):
    def L(c, t, cx, by):
        rice(c, cx, by - 380, 0.7, 1.0)
        fat_blob(c, t, cx, by - 180, lerp(70, 45, ease(prog(t, 0.8, 1.0))), 1.0)
    def Rr(c, t, cx, by):
        chicken(c, cx, by - 380, 0.7, 1.0)
        fat_blob(c, t, cx, by - 180, lerp(70, 45, ease(prog(t, 1.1, 1.0))), 1.0)
    split(c, t, L, Rr, "COM CARBO", "SEM CARBO", YEL, BLU)

def treino(c, t, d):
    act_squat(c, t, spd=2.0)
    battery(c, 800, 1180, lerp(0.9, 0.25, ease(prog(t, 0.4, 1.2))), None, w=220, h=380)
    draw_text(c, "COMBUSTÍVEL", 800, 1440, 50, YEL, "Anton", prog(t, 0.2, 0.3), align="center")

def decide(c, t, d):
    act_walk(c, t, spd=4.0)
    plate_food(c, 790, 1200, lerp(1.2, 0.95, ease(prog(t, 0.5, 1.0))), back_out(prog(t, 0.05, 0.3)))
    tag(c, 790, 1430, "O TOTAL DO DIA", YEL, INK, 50, back_out(prog(t, 0.6, 0.3)))

VIS = {"hook": scene(hook, "CORTAR NÃO SECA MAIS", RED), "rapido": scene(rapido, "OS PRIMEIROS QUILOS...", YEL),
       "agua": scene(agua, "É ÁGUA", BLU), "estudo": scene(estudo, "MESMA GORDURA", YEL, bg=False),
       "treino": scene(treino, "O TREINO SENTE", RED), "decide": scene(decide, "O TOTAL DECIDE", GRN)}
SFX = finish(R, VIS, ("1ª QUEDA É ÁGUA", "MESMAS CALORIAS", "PROTEÍNA ALTA"), "CARBO", "SUAS CARGAS",
 [("ANTES: 80 KG × 8", WHITE), ("NA DIETA: 80 KG × 8", WHITE), ("FORÇA SEGUROU", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
