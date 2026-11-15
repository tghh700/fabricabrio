from cenas_1611 import *
import roteiro_brio_60_shape as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_tired(c, t, x, 1.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_pose(c, t, "flex", x, 1.0))
    split(c, t, L, Rr, "DIA 1", "DIA 90", GREY, GRN)

def parte(c, t, d):
    act_curl(c, t)
    stack_list(c, t, ("TREINO", "LUZ", "PUMP", "POSTURA"), 790, 960, 420, 140, 0 if t < 1.0 else 1 + int(t * 2) % 3, num=False)

def luz(c, t, d):
    frame(c, 760, 1290, 440, 560, "FOTO", YEL, back_out(prog(t, 0.05, 0.3)))
    mini(c, 760, 1540, 0.5, lambda x: act_pose(c, t, "flex", x, 1.0))
    lamp(c, t, 760, 1115, prog(t, 0.3, 0.3))

def pump(c, t, d):
    act_curl(c, t, spd=6.0)
    bicep_glow(c, t, 330, 1215, prog(t, 0.3, 0.3))
    draw_text(c, "30 MIN", 790, 1180, 140, YEL, "Anton", back_out(prog(t, 0.2, 0.3)), align="center")
    draw_text(c, "DE BRAÇO INCHADO", 790, 1280, 40, GREY, "Space Mono", prog(t, 0.5, 0.3), align="center", spacing=1)

def postura(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_tired(c, t, x, 1.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.62, lambda x: act_pose(c, t, "cheer", x, 1.0))
    split(c, t, L, Rr, "SOLTO", "CONTRAÍDO", GREY, YEL)

def compara(c, t, d):
    act_walk(c, t, spd=4.0)
    frame(c, 790, 1220, 380, 460, "EDITADA", RED, back_out(prog(t, 0.05, 0.3)))
    for k in range(3):
        rrect(c, 640, 1150 + k * 70, 300 - k * 60, 30, 12, GREY, 0.5 * prog(t, 0.2 + k * 0.1, 0.3))
    q = prog(t, 0.6, 0.3)
    if q > 0:
        x_mark(c, 790, 1220, 1.3, q, RED)

VIS = {"hook": scene(hook, "90 DIAS É REAL?", YEL, bg=False), "parte": scene(parte, "PARTE É TRUQUE", YEL),
       "luz": scene(luz, "LUZ DE CIMA", YEL), "pump": scene(pump, "PUMP ANTES DA FOTO", RED),
       "postura": scene(postura, "POSTURA E CONTRAÇÃO", YEL, bg=False), "compara": scene(compara, "NÃO COMPARA", RED)}
SFX = finish(R, VIS, ("90 DIAS MUDAM MUITO", "FOTO TEM TRUQUE", "VOCÊ × VOCÊ"), "REAL", "SUA EVOLUÇÃO",
 [("DIA 1: 30 KG × 10", WHITE), ("DIA 90: 45 KG × 10", WHITE), ("+15 KG DE VERDADE", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
