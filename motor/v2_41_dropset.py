from cenas_1511 import *
import roteiro_brio_41_dropset as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t, HX, 0.95, 3.0, heavy=True)
    clock(c, 780, 1150, 150, t, 2.0)
    draw_text(c, "MENOS TEMPO", 780, 1450, 64, YEL, "Anton", back_out(prog(t, 0.6, 0.3)), align="center")

def como(c, t, d):
    heavy = t < d * 0.45
    act_curl(c, t, HX, 0.95, 2.8, heavy=heavy)
    for i, (txt, on) in enumerate((("ATÉ QUASE FALHAR", t > 0.2), ("TIRA PESO", t > d * 0.45), ("CONTINUA", t > d * 0.65))):
        p = back_out(prog(t, [0.2, d * 0.45, d * 0.65][i], 0.3))
        card(c, 770, 1000 + i * 170, 480, 130, YEL if i == 1 else CARD, p)
        draw_text(c, txt, 770, 1000 + i * 170 + 22, 50, INK if i == 1 else WHITE, "Anton", p, align="center")

def exemplo(c, t, d):
    heavy = t < d * 0.5
    act_curl(c, t, HX, 0.95, 3.0, heavy=heavy)
    v = 14 if heavy else 10
    draw_text(c, f"{v} KG", 780, 1200, 200 * (1 + 0.04 * math.sin(t * 6)), YEL if heavy else GRN, "Anton", 1.0, align="center")
    arrow(c, 780, 1290, 780, 1440, GRN, 16, ease_out(prog(t, d * 0.45, 0.3)))
    draw_text(c, "+ REPETIÇÕES", 780, 1520, 56, GRN, "Anton", back_out(prog(t, d * 0.55, 0.3)), align="center")

def tempo(c, t, d):
    p = ease_out(prog(t, 0.3, 1.2))
    for i, (lab, w, col) in enumerate((("SÉRIES NORMAIS", 1.0, BLU), ("DROP SET", 0.5, GRN))):
        y = 1000 + i * 260
        draw_text(c, lab, 140, y - 30, 48, GREY, "Anton", 1.0)
        rrect(c, 140, y, 800 * w * p, 90, 24, col)
    clock(c, 540, 1530, 110, t, 2.0)

def ultima(c, t, d):
    act_curl(c, t, HX, 0.95)
    for i in range(3):
        p = back_out(prog(t, 0.2 + i * 0.3, 0.3))
        hot = i == 2
        card(c, 780, 980 + i * 170, 440, 130, YEL if hot else CARD, p)
        draw_text(c, f"SÉRIE {i + 1}" + (" + DROP" if hot else ""), 780, 980 + i * 170 + 22, 54, INK if hot else WHITE, "Anton", p, align="center")

def isolado(c, t, d):
    def L(c, t, cx, by): stack_machine(c, cx, by, 0.5, 0.5 - 0.5 * math.cos(t * 2.6), hi=YEL)
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_squat(c, t, x, 1.0))
    split(c, t, L, Rr, "MÁQUINA", "AGACHAMENTO", GRN, RED)

VIS = {"hook": scene(hook, "DROP SET", YEL), "como": scene(como, "COMO FUNCIONA", YEL),
       "exemplo": scene(exemplo, "14 KG, DEPOIS 10", YEL), "tempo": scene(tempo, "PARECIDO, MAIS RÁPIDO", GRN, bg=False),
       "ultima": scene(ultima, "SÓ NA ÚLTIMA SÉRIE", YEL), "isolado": scene(isolado, "ONDE USAR", YEL, bg=False)}
SFX = finish(R, VIS, ("ÚLTIMA SÉRIE", "MÁQUINA E ISOLADO", "COM TÉCNICA"), "DROP", "ROSCA + DROP",
 [("14 KG × 10", WHITE), ("10 KG × 8", WHITE), ("DROP REGISTRADO", None)], ("REGISTRE CADA ETAPA", "NO BRIO"))
