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


# ------------------------------------------------------------------ desenvolvimento em 3 planos (12/11)
def front_presser(c, x, s, u, hip=0.0, ring=None):
    """boneco de FRENTE (plano frontal) fazendo desenvolvimento com barra.
    u 0..1: barra na altura do ombro -> braços estendidos acima da cabeça. hip: quadril avança (vira para a câmera como inclinação)."""
    fy = FLOOR_Y
    shadow(c, x, fy + 4, 200 * s)
    hipy = fy - 300 * s; shy = fy - 560 * s
    tilt = 0.0  # vista frontal: o quadril à frente aparece só no quadro lateral
    # pernas
    for sd in (-1, 1):
        cap_line(c, x + sd * 45 * s + tilt * 0.3, hipy, x + sd * 55 * s, fy - 10 * s, L_BACK, 62 * s)
    # tronco (afina na cintura) e cabeça
    rrect(c, x - 95 * s + tilt, shy - 20 * s, 190 * s, (hipy - shy) + 50 * s, 60 * s, L_BODY)
    disk(c, x + tilt * 1.2, shy - 95 * s, 70 * s, L_BODY)
    if ring is not None:
        c.new_path(); c.arc(x + tilt, hipy - 70 * s, 110 * s, 0, 2 * math.pi); rgb(c, ring, 0.9); c.set_line_width(10); c.stroke()
    # braços: ombro -> cotovelo (para fora) -> mão
    hy = lerp(shy + 40 * s, shy - 330 * s, ease(u))
    for sd in (-1, 1):
        sx = x + tilt + sd * 95 * s
        hx = x + tilt * 1.2 + sd * 150 * s
        ex = sx + sd * lerp(95, 40, ease(u)) * s; ey = lerp(shy + 70 * s, shy - 150 * s, ease(u))
        cap_line(c, sx, shy + 5 * s, ex, ey, L_FRONT, 52 * s)
        cap_line(c, ex, ey, hx, hy, L_FRONT, 46 * s)
    # barra com anilhas
    bx = x + tilt * 1.2
    cap_line(c, bx - 290 * s, hy, bx + 290 * s, hy, STEEL, 14 * s)
    for sd in (-1, 1):
        rrect(c, bx + sd * 250 * s - 18 * s, hy - 70 * s, 36 * s, 140 * s, 9 * s, PLATE)
        rrect(c, bx + sd * 290 * s - 14 * s, hy - 52 * s, 28 * s, 104 * s, 8 * s, PLATE)
    return bx, hy


def spine_inset(c, x, y, arch, t, p=1.0, ok=None):
    """quadro "VISTA LATERAL": perfil simplificado com a coluna. arch 0 = reta, 1 = lombar arqueada (quadril à frente)."""
    if p <= 0:
        return
    card(c, x, y, 340, 470, CARD, p)
    draw_text(c, "VISTA LATERAL", x, y - 255, 26, GREY, "Space Mono", p, align="center", spacing=2)
    c.save(); c.translate(x, y); c.scale(1.25, 1.25); c.translate(-x, -y)
    col = ok if ok is not None else mix(GRN, RED, arch)
    # pés -> quadril -> ombros -> cabeça; o quadril vai à frente e o tronco inclina para trás quando arqueia
    fx, fy = x - 10, y + 150
    hx, hy = x + 45 * arch, y + 20
    sx, sy = x - 60 * arch, y - 90
    cap_line(c, fx, fy, hx, hy, L_BACK, 26, p)
    pts = []
    for i in range(13):
        f = i / 12
        bow = math.sin(f * math.pi) * 45 * arch
        pts.append((lerp(hx, sx, f) + bow, lerp(hy, sy, f)))
    poly(c, pts, col, 14, p)
    disk(c, sx - 5 * arch, sy - 40, 30, L_BODY, p)
    cap_line(c, sx, sy, sx + 10, sy - 120 + 20 * arch, L_FRONT, 18, p)  # braço para cima
    c.restore()
