from cenas_1611 import *
import roteiro_brio_51_mes as R
BEAT_CTA = R.BEATS[-1]

def kg(c, t, x, y, a, b, size=170, col=GRN, t0=0.15, dur=1.2):
    v = lerp(a, b, ease_out(prog(t, t0, dur)))
    draw_text(c, f"{v:.1f}".replace(".", ",") + " KG", x, y + size * 0.35, size * (1 + 0.04 * math.sin(t * 5)), col, "Anton", back_out(prog(t, 0.05, 0.25)), align="center")

def hook(c, t, d):
    act_curl(c, t)
    draw_text(c, "? KG", 780, 1220, 220 * (1 + 0.06 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.1, 0.3)), align="center")
    draw_text(c, "POR MÊS", 780, 1330, 48, GREY, "Space Mono", prog(t, 0.4, 0.3), align="center", spacing=3)

def real(c, t, d):
    act_curl(c, t)
    kg(c, t, 780, 1130, 0, 1)
    draw_text(c, "POR MÊS NO ANO 1", 780, 1300, 40, GREY, "Space Mono", prog(t, 0.6, 0.3), align="center", spacing=2)
    tag(c, 780, 1430, "COMEÇANDO DO ZERO", BLU, INK, 44, back_out(prog(t, 1.0, 0.3)))

def cai(c, t, d):
    act_curl(c, t, spd=2.0)
    bars(c, t, 780, 1480, (0.95, 0.5, 0.27), ("ANO 1", "ANO 2", "ANO 3"), (GRN, YEL, RED), w=110, gap=36, h=430)

def balanca(c, t, d):
    act_walk(c, t, spd=5.0)
    vals = ("70,0", "71,4", "69,6", "70,8", "69,9")
    bath_scale(c, 760, 1470, vals[int(t * 3) % 5], back_out(prog(t, 0.05, 0.3)), YEL, 4 * math.sin(t * 20))
    for i, (s, col) in enumerate((("MÚSCULO", GRN), ("ÁGUA", BLU), ("COMIDA", YEL), ("GORDURA", RED))):
        tag(c, 640 + (i % 2) * 260, 1040 + (i // 2) * 150, s, col, INK if col != RED else WHITE, 46, back_out(prog(t, 0.3 + i * 0.25, 0.3)))

def promessa(c, t, d):
    def L(c, t, cx, by):
        draw_text(c, "5 KG", cx, by - 330, 150, RED, "Anton", 1.0, align="center")
        draw_text(c, "EM 1 MÊS", cx, by - 250, 40, GREY, "Space Mono", 1.0, align="center", spacing=2)
        icon_x(c, cx, by - 110, 1.0, prog(t, 0.9, 0.3))
    def Rr(c, t, cx, by):
        draw_text(c, "1 KG", cx, by - 330, 150, GRN, "Anton", 1.0, align="center")
        draw_text(c, "EM 1 MÊS", cx, by - 250, 40, GREY, "Space Mono", 1.0, align="center", spacing=2)
        icon_ok(c, cx, by - 110, 1.0, prog(t, 1.3, 0.3))
    split(c, t, L, Rr, "PROMESSA", "REAL", RED, GRN)

def medida(c, t, d):
    act_curl(c, t, heavy=True, spd=2.2)
    bars(c, t, 780, 1480, (0.35, 0.5, 0.68, 0.88), ("M1", "M2", "M3", "M4"), (BLU, BLU, BLU, GRN), w=82, gap=28, h=380,
         fmt=("10", "11", "12", "14"))
    draw_text(c, "CARGA (KG)", 780, 1000, 40, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center", spacing=2)

VIS = {"hook": scene(hook, "QUANTO POR MÊS?", YEL), "real": scene(real, "ATÉ 1 KG POR MÊS", GRN),
       "cai": scene(cai, "DEPOIS, DESACELERA", YEL), "balanca": scene(balanca, "A BALANÇA ENGANA", RED),
       "promessa": scene(promessa, "5 KG EM 1 MÊS? NÃO", RED, bg=False), "medida": scene(medida, "OLHA A CARGA", GRN)}
SFX = finish(R, VIS, ("1 KG/MÊS NO COMEÇO", "BALANÇA MISTURA TUDO", "OLHA A CARGA"), "QUILO", "SUA CARGA",
 [("SET: 10 KG × 10", WHITE), ("OUT: 12 KG × 10", WHITE), ("NOV: 14 KG × 10", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
