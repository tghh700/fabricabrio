from cenas_1511 import *
import roteiro_brio_47_oscila as R
BEAT_CTA = R.BEATS[-1]
ZZ = (0.3, 0.5, 0.35, 0.6, 0.42, 0.66, 0.55, 0.8, 0.68, 0.88)

def hook(c, t, d):
    act_tired(c, t)
    zigzag(c, t, 560, 1000, 440, 420, (0.5, 0.62, 0.55, 0.7, 0.6, 0.3), BLU, trend=False, dur=1.0)
    if t > 1.1:
        disk(c, 560 + 5 * 88, 1420 - 0.3 * 420, 24 + 6 * math.sin(t * 6), RED)

def varia(c, t, d):
    act_curl(c, t, HX, 0.95, heavy=(t % 2.4) < 1.2)
    zigzag(c, t, 560, 1000, 440, 420, ZZ[:6], BLU, trend=False)

def causas(c, t, d):
    act_pose(c, t, "scratch")
    stack_list(c, t, ("SONO", "COMIDA", "ESTRESSE", "HORÁRIO"), 780, 950, 420, 140, -1, num=False)

def isolado(c, t, d):
    act_curl(c, t, HX, 0.95)
    zigzag(c, t, 560, 1000, 440, 420, ZZ, BLU, trend=False, dur=1.0)
    p = back_out(prog(t, 1.2, 0.3))
    if p > 0:
        x = 560 + 4 * 440 / 9; y = 1420 - 0.42 * 420
        c.new_path(); c.arc(x, y, 50 * p, 0, 2 * math.pi); rgb(c, RED); c.set_line_width(10); c.stroke()

def tendencia(c, t, d):
    act_curl(c, t, HX, 0.95)
    zigzag(c, t, 560, 1000, 440, 420, ZZ, BLU, trend=True, dur=1.0)
    draw_text(c, "4 SEMANAS × 4 SEMANAS", 780, 1500, 40, GREY, "Space Mono", 1.0, align="center", spacing=1)

def alerta(c, t, d):
    act_tired(c, t)
    vals = (0.85, 0.7, 0.55, 0.4)
    for i, v in enumerate(vals):
        p = ease_out(prog(t, 0.2 + i * 0.3, 0.4))
        x = 600 + i * 115; h = 400 * v * p
        rrect(c, x - 40, 1450 - h, 80, h + 1, 14, RED)
        draw_text(c, f"S{i + 1}", x, 1500, 30, GREY, "Space Mono", 1.0, align="center")
    tag(c, 770, 960, "SONO, TREINO, DESCANSO", YEL, INK, 38, back_out(prog(t, 1.6, 0.3)))

VIS = {"hook": scene(hook, "TREINO FRACO?", RED), "varia": scene(varia, "A FORÇA VARIA", YEL),
       "causas": scene(causas, "O QUE MUDA O DIA", YEL), "isolado": scene(isolado, "1 DIA NÃO DIZ NADA", YEL),
       "tendencia": scene(tendencia, "OLHA A TENDÊNCIA", GRN), "alerta": scene(alerta, "CAIU 4 SEMANAS? SINAL", RED)}
SFX = finish(R, VIS, ("DIA RUIM É NORMAL", "OLHA O MÊS", "QUEDA LONGA: REVÊ"), "OSCILA", "SUA EVOLUÇÃO",
 [("OUT: 60 KG", WHITE), ("NOV: 65 KG", WHITE), ("TENDÊNCIA: SUBINDO", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
