from cenas_1611 import *
import roteiro_brio_56_junto as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    q = ease(prog(t, 0.3, 1.4))
    battery(c, 660, 1250, lerp(0.85, 0.4, q), "GORDURA", col=FAT)
    battery(c, 900, 1250, lerp(0.4, 0.85, q), "MÚSCULO", col=GRN)

def sim(c, t, d):
    act_curl(c, t, heavy=True)
    tag(c, 790, 1150, "RECOMPOSIÇÃO", GRN, INK, 70, back_out(prog(t, 0.2, 0.3)))
    icon_ok(c, 790, 1360, 1.2, prog(t, 0.6, 0.3))

def quem(c, t, d):
    act_walk(c, t, spd=4.0)
    stack_list(c, t, ("INICIANTE", "VOLTANDO DE PAUSA", "MAIS GORDURA"), 780, 990, 540, 160, -1, num=False)

def receita(c, t, d):
    act_squat(c, t, spd=2.4)
    stack_list(c, t, ("FORÇA PESADA", "PROTEÍNA ALTA", "UM POUCO MENOS"), 790, 990, 500, 160, int(t * 1.4) % 3)

def balanca(c, t, d):
    act_walk(c, t, spd=4.0)
    q = ease(prog(t, 0.4, 1.4))
    fat_blob(c, t, 660, 1120, lerp(70, 35, q), 1.0)
    muscle_fiber(c, t, 900, 1120, 200, 70, 1.0, lerp(0.8, 1.3, q))
    bath_scale(c, 780, 1440, "80,0", back_out(prog(t, 0.05, 0.3)), GRN)

def sinal(c, t, d):
    act_curl(c, t, heavy=True)
    draw_text(c, "CINTURA", 790, 1000, 40, GREY, "Space Mono", 1.0, align="center", spacing=2)
    tape(c, t, 800, 1080, 400, lerp(0.95, 0.65, ease(prog(t, 0.3, 1.2))), prog(t, 0.05, 0.3))
    draw_text(c, "CARGA", 790, 1240, 40, GREY, "Space Mono", 1.0, align="center", spacing=2)
    counter(c, t, 760, 1340, 40, 47, "{:.0f}", 130, GRN, 0.4, 1.2, " KG")
    arrow(c, 980, 1420, 980, 1290, GRN, 14, ease_out(prog(t, 0.8, 0.4)))

VIS = {"hook": scene(hook, "SECAR E CRESCER?", YEL), "sim": scene(sim, "DÁ, SIM", GRN),
       "quem": scene(quem, "QUEM CONSEGUE MAIS", YEL), "receita": scene(receita, "A RECEITA", GRN),
       "balanca": scene(balanca, "A BALANÇA NÃO MEXE", YEL), "sinal": scene(sinal, "CINTURA CAI, CARGA SOBE", GRN)}
SFX = finish(R, VIS, ("DÁ, NO COMEÇO", "CINTURA E CARGA", "NÃO A BALANÇA"), "JUNTO", "SUA CARGA",
 [("SEMANA 1: 40 KG", WHITE), ("SEMANA 6: 47 KG", WHITE), ("FORÇA SUBINDO", None)], ("REGISTRE SUAS CARGAS", "NO BRIO"))
