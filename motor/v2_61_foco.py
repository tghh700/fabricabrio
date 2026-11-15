from cenas_1611 import *
import roteiro_brio_61_foco as R
BEAT_CTA = R.BEATS[-1]
BX, BY = 330, 1215   # bíceps do boneco principal

def hook(c, t, d):
    act_curl(c, t)
    bicep_glow(c, t, BX, BY, prog(t, 0.2, 0.3))
    draw_text(c, "?", 800, 1300, 300 * (1 + 0.05 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def estudo(c, t, d):
    act_curl(c, t)
    tag(c, 790, 1050, "ESTUDO DE 2018", BLU, INK, 54, back_out(prog(t, 0.1, 0.3)))
    stack_list(c, t, ("ROSCA", "EXTENSORA"), 790, 1220, 400, 150, -1, t0=0.5, num=False)

def braco(c, t, d):
    act_curl(c, t)
    bicep_glow(c, t, BX, BY, 1.0)
    bars(c, t, 790, 1460, (0.55, 1.0), ("SÓ O PESO", "NO MÚSCULO"), (GREY, GRN), w=150, gap=60, h=380, fmt=("+7%", "+12%"))

def perna(c, t, d):
    act_squat(c, t, spd=2.2)
    bars(c, t, 790, 1460, (0.93, 1.0), ("SÓ O PESO", "NO MÚSCULO"), (GREY, YEL), w=150, gap=60, h=380, fmt=("+8,5%", "+9,1%"))

def como(c, t, d):
    act_curl_tempo(c, t, HX, 0.95, down=1.6, up=1.0)
    bicep_glow(c, t, BX, BY, 0.8)
    stack_list(c, t, ("PESO CONTROLADO", "MAIS DEVAGAR", "SENTE APERTAR"), 790, 990, 500, 160, int(t * 1.4) % 3)

def pesado(c, t, d):
    act_squat(c, t, spd=2.0)
    tag(c, 790, 1150, "PESADO = TÉCNICA", YEL, INK, 60, back_out(prog(t, 0.2, 0.3)))
    icon_ok(c, 790, 1360, 1.1, prog(t, 0.6, 0.3))

VIS = {"hook": scene(hook, "PENSAR NO MÚSCULO?", YEL), "estudo": scene(estudo, "UM ESTUDO TESTOU", BLU),
       "braco": scene(braco, "BÍCEPS: CRESCEU MAIS", GRN), "perna": scene(perna, "PERNA: QUASE IGUAL", YEL),
       "como": scene(como, "SENTE O MÚSCULO", GRN), "pesado": scene(pesado, "NO PESADO, TÉCNICA", YEL)}
SFX = finish(R, VIS, ("ISOLADO: SENTE", "PESADO: TÉCNICA", "É DE GRAÇA"), "FOCO", "ROSCA DIRETA",
 [("SÉRIE 1: 12 KG × 10", WHITE), ("SÉRIE 2: 12 KG × 10", WHITE), ("SÉRIE 3: 12 KG × 11", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
