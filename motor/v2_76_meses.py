from cenas_2011 import *
import roteiro_brio_76_meses as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    counter(c, t, 790, 1060, 0, 6, size=260, col=YEL, dur=1.0)
    draw_text(c, "MESES", 790, 1240, 70, WHITE, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")
    calendar(c, 790, 1400, 6, 1, 70, int(lerp(0, 6, ease_out(prog(t, 0.15, 1.0)))) , t, 0.15, 8)

def forca(c, t, d):
    act_curl(c, t, heavy=True)
    v = lerp(20, 38, ease_out(prog(t, 0.2, 1.4)))
    draw_text(c, f"{v:.0f} KG", 790, 1120, 170 * (1 + 0.03 * math.sin(t * 5)), GRN, "Anton", back_out(prog(t, 0.05, 0.3)), align="center")
    draw_text(c, "MÊS 1  >  MÊS 6", 790, 1240, 38, GREY, "Space Mono", prog(t, 0.3, 0.3), align="center", spacing=1)
    arrow(c, 990, 1420, 990, 1300, GRN, 14, ease_out(prog(t, 0.9, 0.3)))
    tag(c, 790, 1420, "QUASE DOBRA", GRN, INK, 46, back_out(prog(t, 1.0, 0.3)))

def roupa(c, t, d):
    act_curl(c, t)
    k = ease(prog(t, 0.3, 1.4))
    tshirt(c, t, 790, 1150, 0.95, k, back_out(prog(t, 0.05, 0.3)))
    tag(c, 790, 1430, "APERTOU", YEL, INK, 50, back_out(prog(t, 1.2, 0.3)))

def outros(c, t, d):
    act_walk(c, t, spd=5.0)
    bubble(c, 760, 900, "TÁ TREINANDO?", back_out(prog(t, 0.15, 0.3)), WHITE, INK, 46, -1)
    bubble(c, 820, 1090, "TÁ MAIOR!", back_out(prog(t, 0.7, 0.3)), YEL, INK, 52, -1)
    bubble(c, 760, 1280, "MUDOU, HEIN", back_out(prog(t, 1.3, 0.3)), GRN, INK, 46, -1)

VIS = {"hook": scene(hook, "6 MESES DE ACADEMIA", YEL), "forca": scene(forca, "PRIMEIRO, A FORÇA", GRN),
       "roupa": scene(roupa, "A ROUPA APERTA", BLU), "outros": scene(outros, "OS OUTROS NOTAM", YEL)}
SFX = finish(R, VIS, ("FORÇA SOBE ANTES", "ROUPA APERTA", "COMPARA A CARGA"), "MESES", "SUA EVOLUÇÃO",
 [("MÊS 1: 20 KG × 10", WHITE), ("MÊS 6: 36 KG × 10", WHITE), ("+16 KG EM 6 MESES", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
