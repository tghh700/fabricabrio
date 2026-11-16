from cenas_1711 import *
import roteiro_brio_69_pesa as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    tilt = 0.25 * math.sin(t * 2.0) * (1 - prog(t, 1.4, 0.6))
    scale_beam(c, t, 815, 1150, tilt, "MÚSCULO", "GORDURA", L=170)

def quilo(c, t, d):
    act_curl(c, t, spd=2.0)
    cube(c, 650, 1420, 170, MEAT, "1 KG", back_out(prog(t, 0.05, 0.35)))
    draw_text(c, "=", 790, 1360, 110, WHITE, "Anton", prog(t, 0.4, 0.3), align="center")
    cube(c, 930, 1420, 170, FAT, "1 KG", back_out(prog(t, 0.5, 0.35)))

def espaco(c, t, d):
    act_curl(c, t, spd=2.0)
    cube(c, 640, 1440, 160, MEAT, "1 KG", 1.0, "MÚSCULO")
    cube(c, 920, 1440, lerp(160, 190, ease(prog(t, 0.3, 1.0))), FAT, "1 KG", 1.0, "GORDURA")

def volume(c, t, d):
    act_walk(c, t, spd=4.0)
    counter(c, t, 790, 1060, 0, 18, "+{:.0f}", 190, FAT, suffix="%")
    draw_text(c, "DE VOLUME", 790, 1200, 44, GREY, "Space Mono", prog(t, 0.5, 0.3), align="center", spacing=3)
    bars(c, t, 790, 1500, (0.5, 0.59), ("MÚSCULO", "GORDURA"), (MEAT, FAT), w=170, gap=80, h=420, t0=0.6)

def roupa(c, t, d):
    def L(c, t, cx, by):
        draw_text(c, "70 KG", cx, by - 440, 90, WHITE, "Anton", 1.0, align="center")
        tape(c, t, cx + 30, by - 250, 300, 0.95, 1.0)
        draw_text(c, "90 CM", cx, by - 120, 70, RED, "Anton", 1.0, align="center")
    def Rr(c, t, cx, by):
        draw_text(c, "70 KG", cx, by - 440, 90, WHITE, "Anton", 1.0, align="center")
        tape(c, t, cx + 30, by - 250, 300, lerp(0.95, 0.78, ease(prog(t, 0.9, 0.8))), 1.0, GRN)
        draw_text(c, "84 CM", cx, by - 120, 70, GRN, "Anton", prog(t, 1.2, 0.3), align="center")
    split(c, t, L, Rr, "ANTES", "6 MESES DEPOIS", GREY, GRN)

def sinal(c, t, d):
    act_curl(c, t, heavy=True)
    tape(c, t, 820, 1100, 340, lerp(0.95, 0.8, ease(prog(t, 0.3, 1.0))), prog(t, 0.05, 0.3), GRN)
    bars(c, t, 790, 1480, (0.4, 0.55, 0.75), ("M1", "M2", "M3"), (BLU, BLU, GRN), w=100, gap=36, h=300, t0=0.5)

VIS = {"hook": scene(hook, "PESA MAIS?", YEL), "quilo": scene(quilo, "1 KG = 1 KG", YEL),
       "espaco": scene(espaco, "A DIFERENÇA É O ESPAÇO", GRN), "volume": scene(volume, "GORDURA OCUPA MAIS", RED),
       "roupa": scene(roupa, "MESMO PESO, ROUPA FOLGA", GRN, bg=False), "sinal": scene(sinal, "CINTURA E CARGA", GRN)}
SFX = finish(R, VIS, ("1 KG = 1 KG", "MÚSCULO OCUPA MENOS", "OLHA A CINTURA"), "ESPAÇO", "SUA EVOLUÇÃO",
 [("PESO: 70 KG", WHITE), ("SUPINO: 30 > 40 KG", WHITE), ("MESMO PESO, + FORTE", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
