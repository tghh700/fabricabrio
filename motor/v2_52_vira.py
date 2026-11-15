from cenas_1611 import *
import roteiro_brio_52_vira as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    muscle_fiber(c, t, 780, 1020, 340, 110, prog(t, 0.05, 0.3))
    arrow(c, 780, 1100, 780, 1260, WHITE, 14, ease_out(prog(t, 0.35, 0.3)))
    fat_blob(c, t, 780, 1370, 80, prog(t, 0.6, 0.3))
    p = back_out(prog(t, 0.9, 0.3))
    if p > 0:
        x_mark(c, 780, 1180, 1.1 * p, 1.0, RED)

def tecido(c, t, d):
    act_curl(c, t, spd=2.0)
    p1 = prog(t, 0.1, 0.35); p2 = prog(t, 0.45, 0.35)
    card(c, 640, 1200, 230, 380, CARD, back_out(p1)); card(c, 940, 1200, 230, 380, CARD, back_out(p2))
    muscle_fiber(c, t, 640, 1160, 160, 80, p1)
    fat_blob(c, t, 940, 1160, 52, p2)
    draw_text(c, "MÚSCULO", 640, 1340, 44, MEAT, "Anton", p1, align="center")
    draw_text(c, "GORDURA", 940, 1340, 44, FAT, "Anton", p2, align="center")
    q = prog(t, 0.9, 0.3)
    cap_line(c, 772, 1180, 808, 1180, WHITE, 10, q); cap_line(c, 772, 1214, 808, 1214, WHITE, 10, q)
    cap_line(c, 812, 1160, 768, 1234, RED, 10, q)

def duas(c, t, d):
    act_walk(c, t, spd=4.0)
    stack_list(c, t, ("MÚSCULO DIMINUI", "GORDURA AUMENTA"), 760, 1060, 520, 190, int(t * 1.2) % 2)

def encolhe(c, t, d):
    act_tired(c, t)
    k = lerp(1.0, 0.55, ease(prog(t, 0.3, max(0.5, d * 0.6))))
    muscle_fiber(c, t, 780, 1180, 380, 170, prog(t, 0.05, 0.3), k)
    draw_text(c, "SEM TREINO", 780, 1420, 48, GREY, "Space Mono", prog(t, 0.2, 0.3), align="center", spacing=3)
    arrow(c, 990, 1100, 990, 1260, RED, 14, ease_out(prog(t, 0.5, 0.3)))

def sobra(c, t, d):
    act_walk(c, t, spd=4.0)
    bars(c, t, 720, 1480, (0.9, 0.62), ("COME", "GASTA"), (YEL, BLU), w=120, gap=50, h=420)
    g = ease_out(prog(t, 1.0, 1.2))
    fat_blob(c, t, 950, 1120, 30 + 45 * g, prog(t, 1.0, 0.3))
    draw_text(c, "SOBRA", 950, 1260, 40, FAT, "Anton", prog(t, 1.1, 0.3), align="center")

def parece(c, t, d):
    def L(c, t, cx, by):
        muscle_fiber(c, t, cx, by - 470, 220, 70, 1.0)
        arrow(c, cx, by - 410, cx, by - 280, WHITE, 12, 1.0)
        fat_blob(c, t, cx, by - 190, 50, 1.0)
    def Rr(c, t, cx, by):
        q = ease(prog(t, 0.8, 1.0))
        muscle_fiber(c, t, cx - 80, by - 300, 150, 70, 1.0, lerp(1, 0.55, q))
        fat_blob(c, t, cx + 90, by - 300, lerp(30, 60, q), 1.0)
        draw_text(c, "-", cx - 80, by - 120, 120, RED, "Anton", 1.0, align="center")
        draw_text(c, "+", cx + 90, by - 120, 120, FAT, "Anton", 1.0, align="center")
    split(c, t, L, Rr, "PARECE", "NA VERDADE", YEL, GRN)

def ajusta(c, t, d):
    act_walk(c, t, spd=4.0)
    s = lerp(1.15, 0.85, ease(prog(t, 0.6, 1.0)))
    plate_food(c, 780, 1200, s, back_out(prog(t, 0.05, 0.3)))
    arrow(c, 990, 1120, 990, 1290, YEL, 14, ease_out(prog(t, 0.6, 0.4)))
    tag(c, 780, 1450, "MENOS TREINO, MENOS COMIDA", YEL, INK, 38, back_out(prog(t, 0.9, 0.3)))

VIS = {"hook": scene(hook, "NÃO VIRA GORDURA", RED), "tecido": scene(tecido, "TECIDOS DIFERENTES", YEL),
       "duas": scene(duas, "DUAS COISAS", YEL), "encolhe": scene(encolhe, "1. O MÚSCULO DIMINUI", RED),
       "sobra": scene(sobra, "2. A SOBRA VIRA GORDURA", RED), "parece": scene(parece, "SÓ PARECE QUE VIROU", YEL, bg=False),
       "ajusta": scene(ajusta, "PAROU? AJUSTA A COMIDA", GRN)}
SFX = finish(R, VIS, ("NÃO SE TRANSFORMA", "PAROU: ENCOLHE", "SOBROU: GORDURA"), "VIRA", "SUA EVOLUÇÃO",
 [("SEMANA 1: 3 TREINOS", WHITE), ("SEMANA 2: 3 TREINOS", WHITE), ("CARGA MANTIDA", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
