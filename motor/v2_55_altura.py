from cenas_1611 import *
import roteiro_brio_55_altura as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    ruler(c, t, 540, 900, FLOOR_Y, prog(t, 0.05, 0.4), mark=1010)
    act_squat(c, t, x=320, spd=2.2)
    draw_text(c, "?", 800, 1260, 300 * (1 + 0.05 * math.sin(t * 6)), YEL, "Anton", back_out(prog(t, 0.3, 0.3)), align="center")

def origem(c, t, d):
    act_curl(c, t)
    bone(c, 790, 1180, 440, 70, 0.5 + 0.5 * math.sin(t * 5), back_out(prog(t, 0.05, 0.3)))
    draw_text(c, "PLACA DE", 790, 1330, 40, YEL, "Space Mono", prog(t, 0.5, 0.3), align="center", spacing=2)
    draw_text(c, "CRESCIMENTO", 790, 1380, 40, YEL, "Space Mono", prog(t, 0.5, 0.3), align="center", spacing=2)

def estudos(c, t, d):
    act_squat(c, t, spd=2.0, depth=0.8)
    stack_list(c, t, ("COM ORIENTAÇÃO", "TÉCNICA BOA"), 790, 1010, 460, 160, -1, num=False)
    icon_ok(c, 790, 1400, 1.3, prog(t, 0.8, 0.3))

def impacto(c, t, d):
    act_walk(c, t, spd=11.0)
    bars(c, t, 790, 1480, (0.9, 0.72, 0.3), ("PULO", "CORRIDA", "SÉRIE"), (RED, YEL, GRN), w=120, gap=36, h=430)
    draw_text(c, "IMPACTO NO OSSO", 790, 990, 38, GREY, "Space Mono", prog(t, 0.1, 0.3), align="center", spacing=2)

def risco(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: squatter(c, x + 6 * math.sin(t * 30), 1.0, 0.5 - 0.5 * math.cos(t * 6)))
    def Rr(c, t, cx, by):
        mini(c, cx, by, 0.6, lambda x: act_squat(c, t, x, 1.0, spd=2.0))
    split(c, t, L, Rr, "TÉCNICA RUIM", "COM ORIENTAÇÃO", RED, GRN)

def osso(c, t, d):
    act_squat(c, t, spd=2.2)
    bone(c, 790, 1220, 440, 64, 0.0, back_out(prog(t, 0.05, 0.3)), thick=ease(prog(t, 0.4, 1.2)))
    arrow(c, 790, 1420, 790, 1330, GRN, 14, ease_out(prog(t, 0.6, 0.4)))
    draw_text(c, "MAIS FORTE", 790, 1500, 60, GRN, "Anton", prog(t, 0.9, 0.3), align="center")

VIS = {"hook": scene(hook, "DEIXA BAIXO? NÃO", RED), "origem": scene(origem, "O MEDO: A PLACA", YEL),
       "estudos": scene(estudos, "SEM PREJUÍZO", GRN), "impacto": scene(impacto, "PULAR TEM MAIS IMPACTO", YEL),
       "risco": scene(risco, "O RISCO: TÉCNICA RUIM", RED, bg=False), "osso": scene(osso, "OSSO MAIS FORTE", GRN)}
SFX = finish(R, VIS, ("NÃO DEIXA BAIXO", "COM ORIENTAÇÃO", "TÉCNICA PRIMEIRO"), "ALTURA", "AGACHAMENTO",
 [("SEM 1: 20 KG × 12", WHITE), ("SEM 4: 22 KG × 12", WHITE), ("SOBE AOS POUCOS", None)], ("REGISTRE SEUS TREINOS", "NO BRIO"))
