from cenas_1611 import *
import roteiro_brio_62_rapido as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_walk(c, t, spd=10.0)
    v = lerp(80, 72, ease(prog(t, 0.2, 1.2)))
    bath_scale(c, 790, 1460, f"{v:.1f}".replace(".", ","), back_out(prog(t, 0.05, 0.3)), RED)
    muscle_fiber(c, t, 790, 1150, 340, 120, prog(t, 0.05, 0.3), lerp(1.0, 0.6, ease(prog(t, 0.3, 1.2))))

def sim(c, t, d):
    act_tired(c, t)
    q = ease(prog(t, 0.3, 1.2))
    fat_blob(c, t, 660, 1200, lerp(80, 45, q), 1.0)
    muscle_fiber(c, t, 920, 1200, 220, 110, 1.0, lerp(1.0, 0.6, q))
    draw_text(c, "GORDURA", 660, 1380, 42, FAT, "Anton", 1.0, align="center")
    draw_text(c, "MÚSCULO", 920, 1380, 42, MEAT, "Anton", 1.0, align="center")

def estudo(c, t, d):
    act_curl(c, t)
    draw_text(c, "MÚSCULO GANHO", 790, 1000, 38, GREY, "Space Mono", prog(t, 0.1, 0.3), align="center", spacing=2)
    bars(c, t, 790, 1460, (0.08, 0.75), ("RÁPIDO", "DEVAGAR"), (RED, GRN), w=150, gap=60, h=380)

def ritmo(c, t, d):
    act_walk(c, t, spd=4.0)
    bars(c, t, 790, 1460, (0.9, 0.86, 0.82, 0.78), ("S1", "S2", "S3", "S4"), (BLU,) * 4, w=80, gap=26, h=360, step=0.2)
    draw_text(c, "0,5 A 1% POR SEMANA", 790, 1010, 48, YEL, "Anton", back_out(prog(t, 0.8, 0.3)), align="center")

def treino(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0, spd=8.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_curl(c, t, x, 1.0, spd=2.2, heavy=True))
    split(c, t, L, Rr, "PESO LEVE", "CARGA ALTA", RED, GRN)

def proteina(c, t, d):
    act_curl(c, t)
    for i in range(3):
        plate_food(c, 620 + i * 170, 1250, 0.6, back_out(prog(t, 0.1 + i * 0.3, 0.3)))
    tag(c, 790, 1450, "PROTEÍNA EM TODAS", GRN, INK, 46, back_out(prog(t, 1.0, 0.3)))

VIS = {"hook": scene(hook, "RÁPIDO DEMAIS?", RED), "sim": scene(sim, "O MÚSCULO VAI JUNTO", RED),
       "estudo": scene(estudo, "DEVAGAR GANHOU MÚSCULO", GRN), "ritmo": scene(ritmo, "RITMO SEGURO", YEL),
       "treino": scene(treino, "NÃO TIRA A CARGA", RED, bg=False), "proteina": scene(proteina, "PROTEÍNA ALTA", GRN)}
SFX = finish(R, VIS, ("DEVAGAR SEGURA", "CARGA ALTA", "PROTEÍNA SEMPRE"), "DEVAGAR", "AGACHAMENTO",
 [("SEMANA 1: 60 KG × 8", WHITE), ("SEMANA 8: 60 KG × 8", WHITE), ("CARGA MANTIDA", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
