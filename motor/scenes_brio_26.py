"""BRIO 26 — joelho pode passar da ponta do pé no agachamento?"""
import math
from engine2 import *
from lote_kit import *
from cta_brio import cta_brio, cta_sfx
import roteiro_brio_26 as R
BEAT_CTA = R.BEATS[-1]

def squat_side(c, x, y, s, kf, lean, hot_back=0.0, knee_col=None):
    """agachamento de perfil (olha pra direita). x,y = calcanhar no chão. kf = quanto o joelho avança (px, escala 1).
    lean = inclinação do tronco em relação à vertical (graus). Retorna (joelho, quadril, ponta do pé) em coordenadas de tela."""
    c.save(); c.translate(x, y); c.scale(s, s)
    A = (40, -30); K = (40 + kf, -30 - math.sqrt(max(210 ** 2 - kf ** 2, 1)))
    a = math.radians(8)
    H = (K[0] - 232 * math.cos(a), K[1] + 232 * math.sin(a))
    L = math.radians(lean)
    S = (H[0] + 290 * math.sin(L), H[1] - 290 * math.cos(L))
    shadow(c, 40, 4, 160)
    cap_line(c, -20, -22, 120, -22, L_BACK, 40)                    # pé
    poly(c, [A, K], L_BACK, 52); poly(c, [K, H], L_FRONT, 66)
    cap_line(c, H[0], H[1], S[0], S[1], L_BODY, 130)
    if hot_back > 0:
        mx, my = lerp(H[0], S[0], 0.28), lerp(H[1], S[1], 0.28)
        disk(c, mx - 62 * math.cos(L), my - 62 * math.sin(L), 40, RED, 0.5 + 0.4 * math.sin(hot_back * 10))
    hx, hy = S[0] + 110 * math.sin(L), S[1] - 110 * math.cos(L)
    disk(c, hx, hy, 64, L_BODY)
    cap_line(c, S[0], S[1] + 20, S[0] + 130, S[1] + 70 + 40 * (lean / 60), L_FRONT, 38)   # braço
    m = c.get_matrix(); c.restore()
    def tr(p): return (x + p[0] * s, y + p[1] * s)
    return tr(K), tr(H), (x + 120 * s, y)

def toe_line(c, x, y0, y1, col=None, p=1.0, a=0.9):
    col = col or WHITE
    c.set_dash([18, 14]); cap_line(c, x, y0, x, y0 + (y1 - y0) * p, col, 6, a); c.set_dash([])

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        u = 0.5 + 0.5 * math.sin(t * 2.2 - 1.2)
        s = 0.95; x = 330
        chunky(c, x, FLOOR_Y, s, pose_mix("bar_back", "squat_deep", u), face=1)
        tx = x + 125 * s
        toe_line(c, tx, 900, FLOOR_Y, WHITE, prog(t, 0.2, 0.4))
        mono(c, "PONTA DO PÉ", tx, 880, 26, WHITE, prog(t, 0.3, 0.3))
        ring(c, tx + 20, 1490, 90, t, YEL)
        pop(c, 760, 1100, back_out(prog(t, 0.5, 0.3))); label(c, "?", 0, 80, YEL, 260); c.restore()
        tag(c, 540, 1760, "JOELHO PASSA?", YEL, INK, 64, back_out(prog(t, d * 0.55, 0.3)))

def myth(c, t, d, b):
    with Cam(c, t, punch=0.06):
        K, H, T = squat_side(c, 300, FLOOR_Y, 0.95, 55, 52)
        tx = T[0]
        rrect(c, tx - 12, 1000, 24, 640 * ease_out(prog(t, 0.2, 0.5)) + 1, 8, RED)
        # joelho travado atrás da linha
        ring(c, K[0], K[1], 70, t, RED)
        # escudo
        ps = back_out(prog(t, 0.5, 0.3))
        pop(c, 760, 1180, ps)
        c.move_to(-90, -110); c.line_to(90, -110); c.line_to(90, 20); c.curve_to(90, 90, 30, 130, 0, 150); c.curve_to(-30, 130, -90, 90, -90, 20); c.close_path()
        rgb(c, BLU); c.fill(); c.restore()
        check_mark(c, 760, 1180, 0.9, prog(t, 0.8, 0.3), WHITE)
        txt(c, "PROTEGER?", 760, 1400, 46, WHITE, prog(t, 0.7, 0.3))
        tag(c, 540, 1760, "JOELHO TRAVADO ATRÁS", RED, WHITE, 54, back_out(prog(t, d * 0.45, 0.3)))

def body(c, t, d, b):
    with Cam(c, t, punch=0.06):
        f = ease(prog(t, 0.2, 1.0))
        K, H, T = squat_side(c, 280, FLOOR_Y, 0.95, lerp(20, 135, f), lerp(35, 14, f))
        toe_line(c, T[0], 980, FLOOR_Y, WHITE, prog(t, 0.1, 0.3))
        mono(c, "PONTA DO PÉ", T[0], 960, 26, WHITE, prog(t, 0.2, 0.3))
        ring(c, K[0], K[1], 80, t, GRN)
        arrow(c, 760, 1100, 760, 1500, YEL, 14, p=prog(t, 0.6, 0.5))
        txt(c, "DESCER FUNDO", 780, 1580, 44, WHITE, prog(t, 0.8, 0.3))
        tag(c, 700, 1000, "TRONCO EM PÉ", GRN, INK, 54, back_out(prog(t, d * 0.45, 0.3)))
        arrow(c, 540, 1300, 620, 1300, GRN, 12, p=prog(t, d * 0.55, 0.3))
        tag(c, 540, 1760, "O JOELHO VAI PRA FRENTE", YEL, INK, 52, back_out(prog(t, d * 0.35, 0.3)))

def back(c, t, d, b):
    with Cam(c, t, punch=0.06):
        f = ease(prog(t, 0.3, 1.2))
        K, H, T = squat_side(c, 280, FLOOR_Y, 0.95, lerp(135, 45, f), lerp(14, 58, f), hot_back=f * t)
        toe_line(c, T[0], 980, FLOOR_Y, WHITE, 1.0)
        pa = back_out(prog(t, d * 0.45, 0.3))
        tag(c, 800, 1050, "LOMBAR", RED, WHITE, 56, pa)
        tag(c, 800, 1200, "QUADRIL", RED, WHITE, 56, back_out(prog(t, d * 0.55, 0.3)))
        if pa > 0:
            cap_line(c, 700, 1070, H[0] + 60, H[1] - 90, RED, 5, 0.6)
        arrow(c, 440, 1130, 560, 1230, YEL, 12, p=prog(t, 0.6, 0.5))
        x_mark(c, 800, 1420, 0.8, prog(t, d * 0.6, 0.3))
        tag(c, 540, 1760, "TRONCO DEITA PRA FRENTE", YEL, INK, 52, back_out(prog(t, 0.3, 0.3)))

def daily(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # escada
        card(c, 290, 1250, 480, 700, CARD, back_out(prog(t, 0.1, 0.3)))
        for i in range(4):
            rrect(c, 90 + i * 100, 1520 - i * 80, 100, 80 + i * 80, 4, IRON)
        u = ease(0.5 + 0.5 * math.sin(t * 3))
        K, H, T = squat_side(c, 330, 1440 - 80 * 2, 0.4, lerp(70, 120, u), 18)
        toe_line(c, T[0], 1000, 1440 - 80 * 2, WHITE, 1.0, 0.7)
        txt(c, "ESCADA", 290, 960, 44, WHITE, prog(t, 0.2, 0.3))
        # sentar no chão
        card(c, 790, 1250, 480, 700, CARD, back_out(prog(t, 0.4, 0.3)))
        rrect(c, 570, 1560, 440, 30, 8, IRON)
        K2, H2, T2 = squat_side(c, 770, 1560, 0.5, lerp(100, 140, u), 25)
        toe_line(c, T2[0], 1040, 1560, WHITE, 1.0, 0.7)
        txt(c, "SENTAR NO CHÃO", 790, 960, 40, WHITE, prog(t, 0.5, 0.3))
        for k in (K, K2): ring(c, k[0], k[1], 40, t, YEL)
        tag(c, 540, 1745, "JÁ PASSA TODO DIA", YEL, INK, 60, back_out(prog(t, d * 0.5, 0.3)))

def foot_top(c, x, y, s=1.0, ang=0.0, col=None):
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    rrect(c, -50, -140, 100, 230, 46, col or L_FRONT)
    c.restore()

def what(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # vista de cima: dois pés, pontos de apoio e joelho na direção dos dedos
        for sd in (-1, 1):
            foot_top(c, 540 + sd * 170, 1300, 1.5, sd * 0.2)
        pts = [(-1, -110), (-1, 0), (-1, 100)]
        for sd in (-1, 1):
            for k, (_, oy) in enumerate(((0, -90), (0, 30), (0, 130))):
                pp = back_out(prog(t, 0.3 + k * 0.25, 0.3))
                if pp > 0:
                    pop(c, 540 + sd * 170 + sd * 0.2 * 0 + sd * (oy * 0) , 1300 + oy * 1.5 * 0.9 - 40, pp)
                    disk(c, 0, 0, 20, GRN); c.restore()
            arrow(c, 540 + sd * 170, 1060 + 0, 540 + sd * 170 + sd * 36, 960, YEL, 12, p=prog(t, 1.0, 0.4))
        mono(c, "PÉ INTEIRO", 540, 1520, 30, WHITE, prog(t, 0.4, 0.3))
        tag(c, 540, 1000, "JOELHO NA DIREÇÃO DOS DEDOS", YEL, INK, 42, back_out(prog(t, d * 0.5, 0.3)))
        tag(c, 300, 1680, "CALCANHAR FIRME", GRN, INK, 46, back_out(prog(t, d * 0.35, 0.3)))
        check_mark(c, 860, 1680, 0.7, prog(t, d * 0.6, 0.3))

def secret(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # vista frontal: joelhos
        def legs(x, inward, col):
            for sd in (-1, 1):
                hip = (x + sd * 70, 1050); kn = (x + sd * (140 - inward), 1300); ft = (x + sd * 150, 1560)
                poly(c, [hip, kn, ft], L_FRONT, 56)
                disk(c, kn[0], kn[1], 40, col)
                cap_line(c, ft[0] - 30, ft[1], ft[0] + 30, ft[1], L_BACK, 30)
            rrect(c, x - 110, 1000, 220, 110, 50, L_BODY)
        legs(290, 0, GRN)
        check_mark(c, 290, 1700, 0.7, prog(t, 0.6, 0.3))
        inw = 70 * (0.5 + 0.5 * math.sin(t * 2.5))
        legs(790, inw if t > 0.6 else 0, RED)
        x_mark(c, 790, 1700, 0.7, prog(t, 0.9, 0.3))
        for sd in (-1, 1):
            arrow(c, 790 + sd * 200, 1300, 790 + sd * 120, 1300, RED, 10, p=prog(t, 0.9, 0.3))
        txt(c, "NEUTRO", 290, 930, 40, GRN, prog(t, 0.3, 0.3)); txt(c, "PRA DENTRO", 790, 930, 40, RED, prog(t, 0.5, 0.3))
        # devagar
        arrow(c, 120, 1160, 120, 1420, YEL, 10, p=prog(t, d * 0.4, 0.6))
        tag(c, 540, 1790, "CONTROLE: DEVAGAR", YEL, INK, 50, back_out(prog(t, d * 0.35, 0.3)))

def pain(c, t, d, b):
    with Cam(c, t, punch=0.06, shake=2 if t < 1.2 else 0):
        K, H, T = squat_side(c, 280, FLOOR_Y, 0.9, 120, 18)
        ring(c, K[0], K[1], 70, t, RED)
        pb = back_out(prog(t, 0.2, 0.3)); pop(c, K[0] + 10, K[1], pb); bolt(c, -22, -34, 22, 34, t, RED, 12); c.restore()
        # amplitude menor
        pa = back_out(prog(t, d * 0.35, 0.3))
        card(c, 780, 1100, 340, 100, CARD, pa)
        rrect(c, 640, 1075, 280, 50, 10, GREY, pa) if pa > 0 else None
        if pa > 0:
            rrect(c, 640, 1075, 280 * (0.6 - 0.1 * math.sin(t * 3)), 50, 10, YEL, pa)
        txt(c, "MENOS AMPLITUDE", 780, 1010, 34, WHITE, pa)
        # cruz de saúde
        pc = back_out(prog(t, d * 0.6, 0.3))
        pop(c, 780, 1400, pc)
        rrect(c, -90, -90, 180, 180, 30, WHITE); rrect(c, -22, -64, 44, 128, 6, RED); rrect(c, -64, -22, 128, 44, 6, RED); c.restore()
        txt(c, "FISIOTERAPEUTA", 780, 1560, 44, WHITE, pc)
        tag(c, 540, 1760, "SE DOER, A REGRA MUDA", RED, WHITE, 52, back_out(prog(t, 0.1, 0.3)))

def progress(c, t, d, b):
    with Cam(c, t, punch=0.06):
        steps = [1, 2, 3, 4]
        for i, pl in enumerate(steps):
            x = 200 + i * 230
            p = back_out(prog(t, 0.2 + i * 0.55, 0.3))
            card(c, x, 1300, 200, 300 + 0 * i, CARD, p, 20)
            if p > 0:
                for k in range(pl):
                    rrect(c, x - 70 + k * 36, 1180 + k * 6, 28, 190 - k * 12, 8, YEL if k % 2 == 0 else (0.85, 0.6, 0.08))
                    c.save()
                c.restore()
                for r in range(3):
                    disk(c, x - 40 + r * 40, 1430, 12, GRN, p)
            if i < 3:
                arrow(c, x + 105, 1300, x + 125, 1300, WHITE, 6, p=prog(t, 0.5 + i * 0.55, 0.3)) if False else None
        # barra subindo devagar
        cap_line(c, 100, 1000, 100 + 880 * ease(prog(t, 0.3, 2.0)), 1000, YEL, 14)
        mono(c, "AOS POUCOS", 540, 960, 30, WHITE)
        tag(c, 540, 1620, "TÉCNICA FIRME EM TODAS AS REPS", GRN, INK, 46, back_out(prog(t, d * 0.5, 0.3)))
        check_mark(c, 540, 1740, 0.6, prog(t, d * 0.65, 0.3))

def stance(c, t, d, b):
    with Cam(c, t, punch=0.06):
        # vista de cima: ombros, pés
        pw = back_out(prog(t, 0.1, 0.3))
        pop(c, 540, 1000, pw); rrect(c, -230, -35, 460, 70, 35, L_BODY); disk(c, 0, 0, 40, L_BACK); c.restore()
        for sd in (-1, 1):
            foot_top(c, 540 + sd * 190, 1400, 1.3, sd * 0.35)
        c.set_dash([14, 12])
        for sd in (-1, 1): cap_line(c, 540 + sd * 190, 1040, 540 + sd * 190, 1300, YEL, 5, 0.9 * prog(t, 0.5, 0.4))
        c.set_dash([])
        pa = prog(t, 0.6, 0.5)
        arrow(c, 350, 1180, 730, 1180, WHITE, 8, p=pa); arrow(c, 730, 1180, 350, 1180, WHITE, 8, p=pa)
        mono(c, "LARGURA DOS OMBROS", 540, 1230, 28, WHITE, pa)
        # pontas pra fora
        for sd in (-1, 1):
            cap_line(c, 540 + sd * 190, 1400, 540 + sd * (190 + 70 * math.sin(0.35)), 1400 - 70, GRN, 6, prog(t, d * 0.45, 0.3))
        tag(c, 540, 1620, "PONTAS UM POUCO PRA FORA", YEL, INK, 46, back_out(prog(t, d * 0.4, 0.3)))
        tag(c, 540, 1750, "AJUSTA ATÉ FICAR CONFORTÁVEL", GRN, INK, 44, back_out(prog(t, d * 0.7, 0.3)))

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="poll", text=("PODE PASSAR", "NÃO PODE"), app_title="AGACHAMENTO", app_lines=[("S1  10 × 60 KG", None), ("S2  10 × 60 KG", None), ("S3  8 × 60 KG", None)])

VIS = {k: globals()[k] for k in "hook myth body back daily what secret pain progress stance cta".split()}
SFX = {
    "hook": [(0.0, "boom"), (0.2, "swish"), (0.5, "pop"), ("0.55d", "pop")],
    "myth": [(0.0, "whoosh"), (0.2, "swish"), (0.5, "pop"), (0.8, "pop"), ("0.45d", "buzz")],
    "body": [(0.0, "whoosh"), (0.2, "swish"), (0.6, "pop"), ("0.45d", "pop"), ("0.55d", "ding")],
    "back": [(0.0, "whoosh"), (0.3, "swish"), (0.6, "pop"), ("0.45d", "buzz"), ("0.55d", "buzz")],
    "daily": [(0.0, "whoosh"), (0.1, "pop"), (0.4, "pop"), ("0.5d", "pop")],
    "what": [(0.0, "whoosh"), (0.3, "pop"), (0.55, "pop"), (0.8, "pop"), ("0.35d", "pop"), ("0.6d", "ding")],
    "secret": [(0.0, "whoosh"), (0.3, "ding"), (0.6, "pop"), (0.9, "buzz"), ("0.35d", "pop")],
    "pain": [(0.0, "whoosh"), (0.2, "buzz"), ("0.35d", "pop"), ("0.6d", "pop")],
    "progress": [(0.0, "whoosh"), (0.2, "pop"), (0.75, "pop"), (1.3, "pop"), (1.85, "pop"), ("0.5d", "ding")],
    "stance": [(0.0, "whoosh"), (0.1, "pop"), (0.6, "swish"), ("0.4d", "pop"), ("0.7d", "pop")],
    "cta": cta_sfx(BEAT_CTA, "poll"),
}
