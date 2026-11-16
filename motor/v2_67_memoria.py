from cenas_1711 import *
import roteiro_brio_67_memoria as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t, spd=3.0)
    zigzag(c, t, 580, 1000, 420, 400, (0.75, 0.3, 0.3, 0.72), GRN, trend=False, dur=1.4)
    for i, s in enumerate(("TREINO", "PAROU", "VOLTOU")):
        draw_text(c, s, 600 + i * 190, 1480, 32, GREY, "Space Mono", prog(t, 0.3 + i * 0.3, 0.3), align="center", spacing=1)

def nome(c, t, d):
    act_curl(c, t)
    draw_text(c, "MEMÓRIA", 790, 1150, 110, YEL, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    draw_text(c, "MUSCULAR", 790, 1280, 110, YEL, "Anton", back_out(prog(t, 0.3, 0.3)), align="center")

def nervo(c, t, d):
    act_squat(c, t)
    c.save(); c.translate(790, 1150)
    for sd in (-1, 1):
        disk(c, sd * 60, 0, 110 * back_out(prog(t, 0.05, 0.3)), (0.95, 0.6, 0.7))
    for k in range(5):
        a = k * 1.2 + t * 0.5
        cap_line(c, 90 * math.cos(a) - 40, 70 * math.sin(a), 90 * math.cos(a + 0.8) + 40, 70 * math.sin(a + 0.8), (0.8, 0.4, 0.5), 8, prog(t, 0.3, 0.3))
    c.restore()
    for k in range(3):
        f = (t * 1.2 + k / 3) % 1
        disk(c, lerp(790, 400, f), lerp(1260, 1300, f), 12, YEL, 1 - f)
    tag(c, 790, 1430, "LEMBRA O MOVIMENTO", YEL, INK, 42, back_out(prog(t, 0.7, 0.3)))

def musculo(c, t, d):
    act_curl(c, t)
    k = lerp(1.0, 0.6, ease(prog(t, 0.3, 1.0)))
    nuclei_fiber(c, t, 790, 1200, 420, 170, k, 6, prog(t, 0.05, 0.3), glow=prog(t, 1.0, 0.4))
    draw_text(c, "AS MARCAS FICAM", 790, 1420, 48, YEL, "Anton", prog(t, 1.0, 0.3), align="center")

def estudo(c, t, d):
    act_curl(c, t, heavy=True)
    draw_text(c, "TEMPO PRA CRESCER", 790, 1000, 36, GREY, "Space Mono", prog(t, 0.1, 0.3), align="center", spacing=1)
    bars(c, t, 790, 1460, (0.9, 0.45), ("1ª VEZ", "2ª VEZ"), (GREY, GRN), w=150, gap=70, h=380)

def volta(c, t, d):
    act_curl(c, t, heavy=True, spd=2.2)
    bars(c, t, 790, 1470, (0.4, 0.55, 0.7, 0.85), ("S1", "S2", "S3", "S4"), (BLU, BLU, BLU, GRN), w=80, gap=28, h=380, fmt=("20", "24", "28", "32"))
    draw_text(c, "CARGA (KG)", 790, 1000, 36, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center", spacing=2)

VIS = {"hook": scene(hook, "VOLTA MAIS RÁPIDO", GRN), "nome": scene(nome, "TEM NOME", YEL),
       "nervo": scene(nervo, "O CÉREBRO LEMBRA", YEL), "musculo": scene(musculo, "O MÚSCULO GUARDA MARCAS", YEL),
       "estudo": scene(estudo, "2ª VEZ É MAIS RÁPIDA", GRN), "volta": scene(volta, "VOLTA LEVE, SOBE", GRN)}
SFX = finish(R, VIS, ("NADA FOI PERDIDO", "VOLTA MAIS LEVE", "SOBE TODA SEMANA"), "VOLTA", "SUAS CARGAS",
 [("VOLTA: 20 KG × 10", WHITE), ("4 SEMANAS: 32 KG", WHITE), ("FORÇA VOLTANDO", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
