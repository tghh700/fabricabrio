from cenas_1611 import *
import roteiro_brio_54_whey as R
BEAT_CTA = R.BEATS[-1]

def ring(c, x, y, r, frac, col, txt, p=1.0):
    if p <= 0:
        return
    disk(c, x, y, r, CARD)
    c.new_path(); c.arc(x, y, r - 18, -math.pi / 2, -math.pi / 2 + 2 * math.pi * clamp(frac)); rgb(c, col); c.set_line_width(24); c.stroke()
    draw_text(c, txt, x, y + 30, 80, WHITE, "Anton", p, align="center")

def hook(c, t, d):
    act_walk(c, t, spd=10.0)
    shaker(c, 790, 1300 - 30 * abs(math.sin(t * 10)), 1.0, back_out(prog(t, 0.05, 0.3)))
    for k in range(3):
        cap_line(c, 600, 1130 + k * 60, 520 - 40 * ((t * 3 + k * 0.3) % 1), 1130 + k * 60, WHITE, 8, 0.5)

def janela(c, t, d):
    act_walk(c, t, spd=9.0)
    left = max(0.0, 30 - t * 6)
    m = int(left); sec = int((left - m) * 60)
    ring(c, 790, 1200, 210, left / 30, RED, f"{m:02d}:{sec:02d}", back_out(prog(t, 0.05, 0.3)))

def horas(c, t, d):
    act_curl(c, t)
    p = ease_out(prog(t, 0.3, 1.2))
    w = lerp(80, 440, p)
    rrect(c, 560, 1250, 460, 40, 20, CARD)
    rrect(c, 790 - w / 2, 1250, w, 40, 20, GRN)
    disk(c, 790, 1270, 34, YEL)
    draw_text(c, "TREINO", 790, 1210, 40, YEL, "Anton", 1.0, align="center")
    draw_text(c, "ANTES", 640, 1360, 36, GREY, "Space Mono", prog(t, 0.8, 0.3), align="center", spacing=2)
    draw_text(c, "DEPOIS", 940, 1360, 36, GREY, "Space Mono", prog(t, 0.8, 0.3), align="center", spacing=2)
    draw_text(c, "HORAS", 790, 1500, 110, GRN, "Anton", back_out(prog(t, 1.2, 0.3)), align="center")

def total(c, t, d):
    act_walk(c, t, spd=4.0)
    stack_list(c, t, ("CAFÉ", "ALMOÇO", "LANCHE", "JANTAR"), 790, 960, 420, 140, int(t * 1.6) % 4, num=False)

def comida(c, t, d):
    def L(c, t, cx, by):
        shaker(c, cx, by - 280, 0.95, 1.0)
        icon_ok(c, cx + 120, by - 110, 0.7, prog(t, 0.8, 0.3))
    def Rr(c, t, cx, by):
        plate_food(c, cx, by - 280, 1.1, 1.0)
        icon_ok(c, cx + 120, by - 110, 0.7, prog(t, 1.1, 0.3))
    split(c, t, L, Rr, "WHEY", "COMIDA", GRN, GRN)

def quando(c, t, d):
    act_curl(c, t, spd=2.4)
    shaker(c, 760, 1320, 0.9, back_out(prog(t, 0.05, 0.3)))
    tag(c, 790, 1010, "QUANDO FOR PRÁTICO", YEL, INK, 46, back_out(prog(t, 0.4, 0.3)))

VIS = {"hook": scene(hook, "CORRENDO PRO WHEY?", YEL), "janela": scene(janela, "JANELA DE 30 MIN?", RED),
       "horas": scene(horas, "A JANELA É DE HORAS", GRN), "total": scene(total, "O TOTAL DO DIA", YEL),
       "comida": scene(comida, "WHEY É COMIDA", GRN, bg=False), "quando": scene(quando, "TOMA QUANDO DER", GRN)}
SFX = finish(R, VIS, ("JANELA DE HORAS", "TOTAL DO DIA", "WHEY É PRÁTICO"), "WHEY", "SUPINO",
 [("SEG: 40 KG × 8", WHITE), ("QUI: 42 KG × 8", WHITE), ("CARGA SUBINDO", None)], ("REGISTRE SEUS TREINOS", "NO BRIO"))
