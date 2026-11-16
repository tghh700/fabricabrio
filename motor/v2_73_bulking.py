from cenas_1711 import *
import roteiro_brio_73_bulking as R
BEAT_CTA = R.BEATS[-1]

def burger(c, x, y, s=1.0, p=1.0):
    if p <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s * max(p, .001), s * max(p, .001))
    rrect(c, -100, -80, 200, 70, 35, (0.85, 0.6, 0.3)); rrect(c, -110, -14, 220, 30, 12, (0.45, 0.25, 0.15))
    rrect(c, -105, 14, 210, 16, 8, GRN); rrect(c, -100, 30, 200, 44, 20, (0.85, 0.6, 0.3))
    c.restore()

def hook(c, t, d):
    act_walk(c, t, spd=4.0)
    for i in range(4):
        burger(c, 620 + (i % 2) * 300, 1080 + (i // 2) * 250, 0.8, back_out(prog(t, 0.05 + i * 0.15, 0.25)))
    x_mark(c, 770, 1210, 1.6, prog(t, 0.9, 0.3), RED)

def ideia(c, t, d):
    act_walk(c, t, spd=6.0)
    for i in range(6):
        burger(c, 600 + (i % 3) * 190, 1100 + (i // 3) * 220, 0.6, back_out(prog(t, 0.1 + i * 0.15, 0.25)))
    tag(c, 790, 1500, "COME TUDO", RED, WHITE, 46, back_out(prog(t, 1.0, 0.3)))

def limite(c, t, d):
    act_curl(c, t, spd=2.0)
    muscle_fiber(c, t, 790, 1200, 400, 140, 1.0, 1.0 + 0.05 * ease(prog(t, 0.4, 1.2)))
    tag(c, 790, 1400, "CRESCE DEVAGAR", YEL, INK, 46, back_out(prog(t, 0.6, 0.3)))

def sobra(c, t, d):
    act_tired(c, t)
    bars(c, t, 720, 1480, (0.15, 0.85), ("MÚSCULO", "GORDURA"), (MEAT, FAT), w=140, gap=60, h=420)
    fat_blob(c, t, 1000, 1300, 30 + 35 * ease_out(prog(t, 0.9, 1.0)), prog(t, 0.9, 0.3))

def certo(c, t, d):
    act_curl(c, t, heavy=True)
    plate_food(c, 790, 1150, 1.0, back_out(prog(t, 0.05, 0.3)))
    draw_text(c, "+300 A 500", 790, 1430, 100 * (1 + 0.04 * math.sin(t * 5)), GRN, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")
    draw_text(c, "CALORIAS POR DIA", 790, 1530, 34, GREY, "Space Mono", prog(t, 0.9, 0.3), align="center", spacing=2)

def ritmo(c, t, d):
    act_curl(c, t, heavy=True, spd=2.2)
    bars(c, t, 790, 1470, (0.3, 0.42, 0.54, 0.66), ("M1", "M2", "M3", "M4"), (BLU, BLU, BLU, GRN), w=80, gap=28, h=400, fmt=("70", "70,5", "71", "71,5"))
    draw_text(c, "PESO (KG)", 790, 1000, 36, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center", spacing=2)

VIS = {"hook": scene(hook, "COMER DE TUDO? NÃO", RED), "ideia": scene(ideia, "BULKING SUJO", RED),
       "limite": scene(limite, "O MÚSCULO TEM LIMITE", YEL), "sobra": scene(sobra, "O RESTO VIRA GORDURA", RED),
       "certo": scene(certo, "SÓ UM POUCO A MAIS", GRN), "ritmo": scene(ritmo, "MEIO QUILO POR MÊS", GRN)}
SFX = finish(R, VIS, ("SOBRA PEQUENA", "+300 A 500 KCAL", "CARGA SUBINDO"), "BULK", "SUAS CARGAS",
 [("PESO: 70 > 71,5 KG", WHITE), ("SUPINO: 50 > 60 KG", WHITE), ("O PESO NOVO É FORÇA", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
