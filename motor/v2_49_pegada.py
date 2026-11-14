from cenas_1511 import *
import roteiro_brio_49_pegada as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    sl = ease(prog(t, d * 0.4, 0.5))
    holder(c, t, HX, 0.95, slip=sl, shake=1.0 - sl)
    battery(c, 690, 1150, lerp(0.8, 0.1, ease(prog(t, 0.1, d * 0.5))), "MÃO", 140, 260)
    battery(c, 900, 1150, 0.9, "COSTAS", 140, 260)

def limita(c, t, d):
    holder(c, t, HX, 0.95, shake=1.0)
    stack_list(c, t, ("REMADA PESADA", "TERRA PESADO"), 790, 1000, 440, 160, -1, num=False)
    tag(c, 790, 1400, "A MÃO FALHA ANTES", RED, WHITE, 44, back_out(prog(t, 0.9, 0.3)))

def sobra(c, t, d):
    act_tired(c, t)
    for i in range(10):
        x = 610 + (i % 5) * 92; y = 1100 + (i // 5) * 110
        rrect(c, x - 36, y - 40, 72, 80, 14, GRN if i < 6 else CARD)
        if i >= 6: x_mark(c, x, y, 0.25, prog(t, 0.4 + (i - 6) * 0.15, 0.2), RED)
    draw_text(c, "4 REPETIÇÕES SOBRANDO", 790, 1400, 46, YEL, "Anton", back_out(prog(t, 1.0, 0.3)), align="center")

def strap(c, t, d):
    # close da mão na barra com a fita enrolando
    p = ease_out(prog(t, 0.2, 1.2))
    cx, cy = 540, 1200
    cap_line(c, cx - 400, cy, cx + 400, cy, STEEL, 40)
    cap_line(c, cx, cy + 330, cx, cy + 40, L_FRONT, 120)   # antebraço
    disk(c, cx, cy, 90, L_BODY)                           # mão fechada
    for k in range(3):
        a = prog(p, k / 3, 1 / 3)
        if a <= 0: continue
        c.new_path(); c.arc(cx, cy, 100 + k * 12, -math.pi / 2, -math.pi / 2 + 2 * math.pi * a)
        rgb(c, YEL); c.set_line_width(24); c.stroke()
    cap_line(c, cx + 20, cy + 110, cx + 30, cy + 260, YEL, 24, prog(t, 1.3, 0.3))

def quando(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: holder(c, t, x, 1.0, strap=True))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    split(c, t, L, Rr, "PESADO: STRAP", "LEVE: MÃO LIVRE", YEL, GRN)

def treina(c, t, d):
    hanger(c, 360, 960, 0.8, 0.0)
    clock(c, 830, 1250, 140, t, 1.0)
    draw_text(c, "SEGURA PARADO", 830, 1480, 56, GRN, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

VIS = {"hook": scene(hook, "A MÃO CANSA PRIMEIRO", RED), "limita": scene(limita, "A PEGADA LIMITA", RED),
       "sobra": scene(sobra, "COSTAS COM SOBRA", YEL), "strap": scene(strap, "STRAP: PRENDE NA BARRA", YEL, bg=False),
       "quando": scene(quando, "QUANDO USAR", YEL, bg=False), "treina": scene(treina, "PEGADA À PARTE", GRN, bg=False)}
SFX = finish(R, VIS, ("STRAP NO PESADO", "MÃO LIVRE NO LEVE", "AS COSTAS DECIDEM"), "PEGADA", "REMADA CURVADA",
 [("SEM STRAP: 60 KG × 6", WHITE), ("COM STRAP: 60 KG × 9", WHITE), ("+3 REPETIÇÕES", None)], ("REGISTRE SUA REMADA", "NO BRIO"))
