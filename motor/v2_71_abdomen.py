from cenas_1711 import *
import roteiro_brio_71_abdomen as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_walk(c, t, spd=4.0)
    torso_abs(c, t, 790, 1220, lerp(1.0, 0.3, 0.5 - 0.5 * math.cos(t * 1.6)), back_out(prog(t, 0.05, 0.3)))
    draw_text(c, "? %", 790, 1600, 90, YEL, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def todos(c, t, d):
    act_curl(c, t)
    torso_abs(c, t, 790, 1220, lerp(1.0, 0.0, ease(prog(t, 0.4, 1.2))), 1.0)
    tag(c, 790, 1560, "ESTÁ AÍ, EMBAIXO", YEL, INK, 42, back_out(prog(t, 1.2, 0.3)))

def homem(c, t, d):
    act_curl(c, t)
    torso_abs(c, t, 680, 1220, lerp(0.8, 0.1, ease(prog(t, 0.3, 1.2))), 0.8)
    counter(c, t, 965, 1180, 25, 12, "{:.0f}", 110, GRN, t0=0.3, suffix="%")
    draw_text(c, "10 A 12%", 965, 1360, 44, WHITE, "Anton", prog(t, 1.3, 0.3), align="center")

def mulher(c, t, d):
    act_walk(c, t, spd=4.0)
    torso_abs(c, t, 680, 1220, lerp(0.8, 0.15, ease(prog(t, 0.3, 1.2))), 0.8)
    counter(c, t, 965, 1180, 32, 20, "{:.0f}", 110, GRN, t0=0.3, suffix="%")
    draw_text(c, "18 A 20%", 965, 1360, 44, WHITE, "Anton", prog(t, 1.3, 0.3), align="center")

def ultimo(c, t, d):
    act_walk(c, t, spd=4.0)
    stack_list(c, t, ("ROSTO", "BRAÇOS", "PERNAS", "BARRIGA"), 790, 960, 420, 135, 3 if t > 1.4 else -1)

def treino(c, t, d):
    act_curl(c, t, heavy=True, spd=2.2)
    torso_abs(c, t, 790, 1220, 0.3, 1.0, thick=lerp(0.9, 1.15, ease(prog(t, 0.3, 1.2))))
    tag(c, 790, 1560, "GOMOS MAIS GROSSOS", GRN, INK, 42, back_out(prog(t, 0.9, 0.3)))

VIS = {"hook": scene(hook, "QUANDO APARECE?", YEL), "todos": scene(todos, "TODO MUNDO TEM", YEL),
       "homem": scene(homem, "HOMENS: 10 A 12%", GRN), "mulher": scene(mulher, "MULHERES: 18 A 20%", GRN),
       "ultimo": scene(ultimo, "A BARRIGA É A ÚLTIMA", RED), "treino": scene(treino, "TREINO COM CARGA AJUDA", GRN)}
SFX = finish(R, VIS, ("É PORCENTAGEM", "BARRIGA É A ÚLTIMA", "CARGA NO ABDÔMEN"), "TANQUINHO", "SUA EVOLUÇÃO",
 [("CINTURA: 88 > 82 CM", WHITE), ("CARGA: MANTIDA", WHITE), ("SECANDO CERTO", None)], ("ACOMPANHE SUA EVOLUÇÃO", "NO BRIO"))
