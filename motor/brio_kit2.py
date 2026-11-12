"""Kit dos BRIO 28–31 (13/11): figuras de desenvolvimento, agachamento com barra e close do punho no supino."""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx

PLATE = (0.30, 0.32, 0.38)


def plate_end(c, x, y, r=62, col=PLATE):
    """barra vista de lado: anilha (disco) com o furo"""
    disk(c, x, y, r, col); disk(c, x, y, r * 0.72, (0.24, 0.26, 0.31)); disk(c, x, y, r * 0.18, STEEL)


def _drop(p):
    lh = 155 * math.cos(math.radians(p[6])) + 150 * math.cos(math.radians(p[6] + p[7]))
    return max(0.0, 305 - lh)


def presser(c, x, s, u, lean=0.0, hip=0.0, face=1):
    """boneco fazendo desenvolvimento; u 0..1 = barra do ombro até em cima; lean = arqueia para trás (rad)"""
    c.save(); c.translate(x + hip * 50 * face, FLOOR_Y); c.rotate(-lean * face); c.translate(-x, -FLOOR_Y)
    p = pose_mix("bar_back", "cheer", u)
    hx, hy = chunky(c, x, FLOOR_Y, s, p, face=face)
    plate_end(c, hx, hy - 10 * s, 64 * s)
    c.restore()


def squatter(c, x, s, d, face=1, belly=0.0, t=0.0):
    """agachamento com barra nas costas; d 0..1 = profundidade; belly 0..1 = ar na barriga (anel amarelo)"""
    p = pose_mix("bar_back", "squat_deep", d)
    chunky(c, x, FLOOR_Y, s, p, face=face)
    dr = _drop(p)
    sy = FLOOR_Y + (dr - 520) * s
    plate_end(c, x - 60 * s * face, sy + 35 * s, 66 * s)
    if belly > 0:
        by = FLOOR_Y + (dr - 380) * s
        r = (60 + 40 * belly) * s
        c.new_path(); c.arc(x + 18 * s * face, by, r, 0, 2 * math.pi)
        rgb(c, YEL, 0.25 * belly); c.fill_preserve(); rgb(c, YEL, 0.9 * belly); c.set_line_width(8); c.stroke()
    return sy


def wrist(c, x, y, s, bend, ok_col=None):
    """close do antebraço + mão segurando a barra (vista de lado). bend 0 = punho reto, 1 = dobrado pra trás"""
    c.save(); c.translate(x, y); c.scale(s, s)
    # antebraço (de baixo pra cima)
    cap_line(c, 0, 420, 0, 0, L_FRONT, 120)
    a = math.radians(-55 * bend)  # mão tomba para trás (esquerda)
    c.save(); c.rotate(a)
    rrect(c, -62, -190, 124, 190, 50, L_BODY)  # palma
    c.restore()
    # barra: com punho reto fica em cima do antebraço; dobrado, cai para trás da linha
    bx = math.sin(a) * 150; by = -math.cos(a) * 150
    plate_end(c, bx, by, 58)
    # linha do antebraço (eixo de força)
    c.set_dash([18, 14]); cap_line(c, 0, 440, 0, -260, ok_col or GREY, 6, 0.8); c.set_dash([])
    c.restore()
    return x + bx * s, y + by * s


def conc_cards(items):
    def conc(c, t, d, b):
        with Cam(c, t, punch=0.06):
            for i, s in enumerate(items):
                p = back_out(prog(t, 0.15 + i * d * 0.15, 0.3))
                y = 960 + i * 175
                card(c, 540, y, 760, 140, CARD, p * (1 + (0.025 * math.sin(t * 4) if i == len(items) - 1 else 0)))
                if p > 0:
                    check_mark(c, 220, y, 0.5, prog(t, 0.3 + i * d * 0.15, 0.3))
                    draw_text(c, s, 300, y + 22, 60, WHITE if i < len(items) - 1 else YEL, "Anton", p)
            # brilho leve para não ficar quadro parado
            yy = 880 + (t * 220) % 720
            cap_line(c, 170, yy, 910, yy, YEL, 6, 0.35)
            pul = 1 + 0.03 * math.sin(t * 5)
            draw_text(c, "✓", 900, 900, 40 * pul, YEL, "Anton", 0.0)
    return conc


def cta_factory(word, app_title, app_lines, lines):
    def cta(c, t, d, b):
        cta_brio(c, t, d, b, kind="bubble", text=word, app_title=app_title,
                 app_lines=[(s, col or (YEL if i == len(app_lines) - 1 else WHITE)) for i, (s, col) in enumerate(app_lines)],
                 chart=False, lines=lines)
    return cta


SFX_BASE = {
    "hook": [(0.0, "boom"), (0.35, "buzz"), ("0.45d", "pop")],
    "conc": [(0.0, "whoosh"), (0.3, "tick"), ("0.3d", "tick"), ("0.45d", "tick"), ("0.6d", "tick")],
}


def sfx_for(vis_names, beat_cta):
    out = {}
    for k in vis_names:
        if k == "cta":
            out[k] = cta_sfx(beat_cta, "bubble")
        else:
            out[k] = SFX_BASE.get(k, [(0.0, "whoosh"), ("0.45d", "pop")])
    return out
