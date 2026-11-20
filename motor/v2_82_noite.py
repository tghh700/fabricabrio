from cenas_2111 import *
import roteiro_brio_82_noite as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl(c, t)
    moon(c, t, 820, 900, 80)
    draw_text(c, "22:00", 790, 1130, 120, WHITE, "Anton", back_out(prog(t, 0.1, 0.3)), align="center")
    draw_text(c, "E O SONO?", 790, 1260, 80 * (1 + 0.03 * math.sin(t * 5)), YEL, "Anton", back_out(prog(t, 0.5, 0.3)), align="center")

def nao(c, t, d):
    sleeper(c, t, 540, 1440, 0.75)
    moon(c, t, 260, 880, 70)
    counter(c, t, 760, 840, 0, 23, size=170, col=YEL)
    draw_text(c, "ESTUDOS", 760, 960, 40, GREY, "Space Mono", prog(t, 0.3, 0.3), align="center", spacing=2)
    tag(c, 680, 1060, "NA MAIORIA, NÃO", GRN, INK, 50, back_out(prog(t, 0.6, 0.3)))

def profundo(c, t, d):
    sleeper(c, t, 540, 1440, 0.75)
    bars(c, t, 540, 1010, (0.7, 0.8), ("SEM TREINO", "TREINO À NOITE"), (GREY, GRN), w=150, gap=170, h=220, step=0.3)
    icon_ok(c, 820, 780, 0.55, prog(t, 1.0, 0.3))

def excecao(c, t, d):
    act_squat(c, t, spd=3.6)
    clock(c, 790, 1060, 150, 0.0, 0.0)
    a = ease_out(prog(t, 0.2, 0.8))
    c.new_path(); c.move_to(790, 1060); c.arc(790, 1060, 130, -math.pi / 2, -math.pi / 2 + a * math.pi / 6); c.close_path()
    rgb(c, RED, 0.55); c.fill()
    tag(c, 790, 1310, "MENOS DE 1 H", RED, WHITE, 52, back_out(prog(t, 0.6, 0.3)))
    draw_text(c, "ANTES DE DEITAR", 790, 1420, 36, GREY, "Space Mono", prog(t, 0.7, 0.3), align="center", spacing=1)

VIS = {"hook": scene(hook, "TREINAR À NOITE TIRA O SONO?", YEL), "nao": scene(nao, "REVISÃO DE 23 ESTUDOS", GRN, bg=False),
       "profundo": scene(profundo, "DORMIU TÃO BEM QUANTO", GRN, bg=False), "excecao": scene(excecao, "SÓ EVITA MUITO PESADO", RED)}
SFX = finish(R, VIS, ("PODE TREINAR À NOITE", "SONO IGUAL", "1 H ANTES DE DEITAR"), "NOITE", "SEUS TREINOS",
 [("TREINO 20:00", WHITE), ("AGACHAMENTO: 4 × 8", WHITE), ("TREINO REGISTRADO", None)], ("REGISTRE SEUS TREINOS", "NO BRIO"))
