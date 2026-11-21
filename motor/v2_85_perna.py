"""BRIO 85 — por que a perna não cresce (cadeia erro → consequência → volta). Kit cenas_v2 + cenas_2211.
Agachamento sempre de perfil (squatter: barra nas costas, sobre os ombros); uma figura por cena."""
from cenas_2211 import *
from cenas_2011 import angle_gauge
import roteiro_brio_85_perna as R


def glow(c, x, y, r, a, col):
    if a <= 0:
        return
    c.new_path(); c.arc(x, y, r, 0, 2 * math.pi); rgb(c, col, 0.22 * a); c.fill_preserve(); rgb(c, col, 0.9 * a); c.set_line_width(8); c.stroke()


def thigh_tape(c, t, x, y, txt, col):
    rrect(c, x - 170, y - 50, 340, 100, 24, CARD)
    draw_text(c, "COXA", x - 140, y + 12, 30, GREY, "Space Mono", 1.0, align="left", spacing=2)
    draw_text(c, txt, x + 145, y + 22, 64, col, "Anton", 1.0, align="right")


def e1(c, t, d):
    k = 0.45 * d
    c.save(); shake(c, t, k)
    bar_squat(c, t, 330, 0.95, 4.2, 0.6)              # carga leve, rápido
    tag(c, 330, 860, "LEVINHO", RED, WHITE, 44, back_out(prog(t, 0.1, 0.3)))
    counter(c, t, 760, 900, 1, 20, size=120, col=WHITE, t0=0.1, dur=d * 0.8, suffix=" REP")
    thigh_tape(c, t, 760, 1160, "= 52 CM", RED)
    c.restore()
    consequence(c, t, "x", 760, 1350, k)
    red_flash(c, t, k)


def bar_squat(c, t, x, s, spd, depth):
    u = 0.5 - 0.5 * math.cos(t * spd)
    squatter(c, x, s, depth * u)
    return u


def f1(c, t, d):
    u = bar_squat(c, t, 330, 0.95, 1.9, 0.9)
    tag(c, 330, 860, "60 KG", GRN, INK, 54, back_out(prog(t, 0.1, 0.3)))
    effort(c, t, 760, 1400, lerp(0.3, 0.92, ease(prog(t, 0.2, d * 0.8))), prog(t, 0.05, 0.3), 420, "PERTO DA FALHA")
    icon_ok(c, 930, 1000, 0.8, prog(t, d * 0.65, 0.3))


def e2(c, t, d):
    k = 0.5 * d
    c.save(); shake(c, t, k)
    u = bar_squat(c, t, 330, 0.95, 2.2, 0.45)          # meio agachamento
    angle_gauge(c, t, 780, 1180, 150, 0.45 * u, prog(t, 0.05, 0.3), ok=False)
    draw_text(c, "METADE", 780, 1260, 40, GREY, "Space Mono", 1.0, align="center", spacing=3)
    glow(c, 290, 1290, 50, 0.6, RED)
    c.restore()
    if t > k:
        tag(c, 780, 950, "GLÚTEO: MENOS", RED, WHITE, 48, back_out(prog(t, k, 0.3)))
    red_flash(c, t, k)


def f2(c, t, d):
    u = bar_squat(c, t, 330, 0.95, 1.8, 1.0)           # agachamento fundo
    angle_gauge(c, t, 780, 1180, 150, u, prog(t, 0.05, 0.3), ok=True)
    draw_text(c, "FUNDO", 780, 1260, 40, GREY, "Space Mono", 1.0, align="center", spacing=3)
    glow(c, 280, 1330, 50 + 25 * u, 0.4 + 0.6 * u, GRN)
    tag(c, 780, 950, "GLÚTEO + COXA", GRN, INK, 48, back_out(prog(t, d * 0.45, 0.3)))


def e3(c, t, d):
    k = 0.55 * d
    c.save(); shake(c, t, k)
    act_curl(c, t, 300, 0.95, 2.6)                     # treinando só braço
    for r in range(2):
        week(c, t - r * 0.4, 720, 920 + r * 120, (2,) if r == 0 else (), RED, cell=62, t0=0.1)
    tag(c, 720, 1180, "PERNA A CADA 15 DIAS", RED, WHITE, 40, back_out(prog(t, 0.6, 0.3)))
    thigh_tape(c, t, 720, 1340, "= 52 CM", RED)
    c.restore()
    consequence(c, t, "x", 950, 1340, k)
    red_flash(c, t, k)


def f3(c, t, d):
    bar_squat(c, t, 330, 0.95, 2.0, 0.95)
    week(c, t, 720, 950, (1, 4), GRN, cell=62, t0=0.1)
    draw_text(c, "2×", 720, 1210, 170, GRN, "Anton", back_out(prog(t, d * 0.4, 0.3)), align="center")
    draw_text(c, "POR SEMANA", 720, 1270, 32, GREY, "Space Mono", 1.0, align="center", spacing=2)


def conc(c, t, d):
    u = bar_squat(c, t, 330, 0.95, 2.0, 0.95)
    pieces(c, t, 760, 1000, ("CARGA", "FUNDO", "2×"), 0.2, 0.45, 170)
    thigh_tape(c, t, 760, 1300, f"= {52 + 4 * ease(prog(t, 1.2, 1.2)):.0f} CM", GRN)


SCENES = dict(e1=e1, f1=f1, e2=e2, f2=f2, e3=e3, f3=f3, conc=conc)
CYCLES = [("LEVE", "CARGA"), ("METADE", "FUNDO"), ("15 DIAS", "2×")]
HOT = [b["k"] for b in R.BEATS]
VIS = chain_vis(R, SCENES, CYCLES, HOT, None)
VIS["cta"] = wipe_in(cta_factory("PERNA", "AGACHAMENTO", [("SEM 1 · 40 KG", WHITE), ("SEM 4 · 45 KG", WHITE), ("SEM 8 · 50 KG", None)],
                                 ("REGISTRE SUAS SÉRIES", "NO BRIO")), slide=0)
SFX = chain_sfx(R, VIS)
SFX["cta"] = sfx_for(["cta"], R.BEATS[-1])["cta"]
