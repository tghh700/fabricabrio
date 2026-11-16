from cenas_1711 import *
import roteiro_brio_72_falsomagro as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_walk(c, t, spd=4.0)
    bath_scale(c, 790, 1470, "65,0", back_out(prog(t, 0.05, 0.3)), GRN)
    fat_blob(c, t, 790, 1180, 70, back_out(prog(t, 0.5, 0.3)))
    draw_text(c, "PESO OK", 790, 1000, 56, GRN, "Anton", back_out(prog(t, 0.2, 0.3)), align="center")

def nome(c, t, d):
    act_tired(c, t)
    p1 = prog(t, 0.1, 0.35); p2 = prog(t, 0.45, 0.35)
    card(c, 640, 1200, 230, 380, CARD, back_out(p1)); card(c, 940, 1200, 230, 380, CARD, back_out(p2))
    muscle_fiber(c, t, 640, 1160, 120, 50, p1)
    fat_blob(c, t, 940, 1160, 70, p2)
    draw_text(c, "POUCO", 640, 1340, 44, MEAT, "Anton", p1, align="center")
    draw_text(c, "SOBRANDO", 940, 1340, 44, FAT, "Anton", p2, align="center")

def erro(c, t, d):
    act_tired(c, t)
    plate_food(c, 650, 1150, lerp(1.0, 0.65, ease(prog(t, 0.2, 1.0))), back_out(prog(t, 0.05, 0.3)))
    muscle_fiber(c, t, 900, 1150, 240, 110, 1.0, lerp(1.0, 0.5, ease(prog(t, 0.6, 1.0))))
    arrow(c, 900, 1260, 900, 1420, RED, 14, ease_out(prog(t, 0.8, 0.3)))
    draw_text(c, "DIETA PESADA", 650, 1340, 48, RED, "Anton", prog(t, 0.3, 0.3), align="center")

def certo(c, t, d):
    act_curl(c, t, heavy=True, spd=2.2)
    muscle_fiber(c, t, 790, 1180, 380, 120, 1.0, lerp(0.7, 1.2, ease(prog(t, 0.3, 1.4))))
    arrow(c, 1000, 1300, 1000, 1080, GRN, 14, ease_out(prog(t, 0.6, 0.3)))
    tag(c, 790, 1420, "TREINO DE FORÇA", GRN, INK, 46, back_out(prog(t, 0.8, 0.3)))

def come(c, t, d):
    act_curl(c, t)
    for i in range(3):
        plate_food(c, 620 + i * 170, 1200, 0.6, back_out(prog(t, 0.1 + i * 0.3, 0.3)))
    tag(c, 790, 1420, "PROTEÍNA EM TODAS", GRN, INK, 46, back_out(prog(t, 1.0, 0.3)))

def muda(c, t, d):
    def L(c, t, cx, by):
        draw_text(c, "65 KG", cx, by - 440, 80, WHITE, "Anton", 1.0, align="center")
        mini(c, cx, by, 0.5, lambda x: act_tired(c, t, x, 1.0))
    def Rr(c, t, cx, by):
        draw_text(c, "66 KG", cx, by - 440, 80, WHITE, "Anton", 1.0, align="center")
        mini(c, cx, by, 0.5, lambda x: act_curl(c, t, x, 1.0, heavy=True))
    split(c, t, L, Rr, "DIA 1", "6 MESES", GREY, GRN)

VIS = {"hook": scene(hook, "MAGRO COM BARRIGA?", YEL), "nome": scene(nome, "FALSO MAGRO", YEL),
       "erro": scene(erro, "O ERRO: DIETA PESADA", RED), "certo": scene(certo, "O CERTO: GANHAR MÚSCULO", GRN),
       "come": scene(come, "COME NORMAL", GRN), "muda": scene(muda, "O PESO NÃO MUDA, O CORPO SIM", GRN, bg=False)}
SFX = finish(R, VIS, ("SEM PASSAR FOME", "TREINO DE FORÇA", "PROTEÍNA ALTA"), "MAGRO", "SUAS CARGAS",
 [("MÊS 1: 20 KG × 10", WHITE), ("MÊS 6: 40 KG × 10", WHITE), ("O DOBRO DE FORÇA", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
