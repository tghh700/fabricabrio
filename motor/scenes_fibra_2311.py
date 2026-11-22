"""FIBRA — produção 23/11 (prancha técnica, build3): agachar fundo e joelho (jo_), 1º treino de perna dói mais (pr_),
última repetição não sobe (fa_), série de agachamento segundo a segundo (sg_, TESTE linha do tempo).
Uma figura por cena; nada atravessa o corpo; só glifos da fonte (marcas desenhadas)."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, cap_line, poly, disk, rrect, draw_text, Cam, rgb
from tema_fibra import *
from tema_fibra import _mono_right
from scenes_fibra_l1 import ellipse, capsule, panel, conclusao_factory, cta_flex, SFX_CTA, squat, units
from scenes_fibra_g import bar_pct, ok_mark, no_mark
from scenes_fibra_1911 import CX, CY, RED, ORANGE, throb
from scenes_fibra_2111 import pain_marks
from scenes_fibra_2211 import arrow_v, hbar, curl_arm
import pauta_2311 as PA

SQX, SQY = 470, 1430


def ring_pulse(c, x, y, r, t, col=PINK, p=1.0):
    for i in range(2):
        f = (t * 1.2 + i * 0.5) % 1
        c.new_path(); c.arc(x, y, r + 50 * f, 0, 2 * math.pi); rgb(c, col, p * (1 - f)); c.set_line_width(5); c.stroke()


def heart(c, x, y, s, t, p=1.0):
    k = 1 + 0.12 * max(0.0, math.sin(t * 15))
    c.save(); c.translate(x, y); c.scale(s * k, s * k)
    disk(c, -38, -20, 46, PINK, p); disk(c, 38, -20, 46, PINK, p)
    poly(c, [(-82, -5), (0, 85), (82, -5)], PINK, 2, p)
    c.new_path(); c.move_to(-82, -8); c.line_to(0, 88); c.line_to(82, -8); c.close_path(); rgb(c, PINK, p); c.fill()
    c.restore()


def timeline(c, t, sec, p=1.0, y=760):
    """régua 0–40 s no topo da cena; destaca até `sec`"""
    x0, x1 = LEFT + 30, RIGHT - 30
    cap_line(c, x0, y, x1, y, LINE, 10, p)
    cap_line(c, x0, y, lerp(x0, x1, sec / 40 * ease_out(prog(t, 0, 0.5))), y, PINK, 10, p)
    for s in (0, 10, 20, 30, 40):
        xx = lerp(x0, x1, s / 40)
        disk(c, xx, y, 12 if s != sec else 18, PINK if s <= sec else LINE, p)
        mono(c, f"{s}S", xx, y + 50, 24, INK if s == sec else MUTED, p, align="center")


# ================================================================ JOELHO (jo_)
def jo_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = 0.55 + 0.45 * math.sin(t * 2.2 - 1.5)
        j = squat(c, SQX, SQY, 0.72, dep, {"quad": 0.5}, t, p)
        ring_pulse(c, j["kne"][0], j["kne"][1], 40, t, PINK, ease_out(prog(t, 0.3, 0.3)))
        chip(c, "ESTRAGA?", CX, 1530, PINK, NAVY, 50, ease_out(prog(t, 0.5, 0.3)))


def _joint(c, t, x, y, squeeze, p, thick=1.0):
    """fêmur em cima, tíbia embaixo, cartilagem (ciano) entre eles; squeeze 0..1 comprime e expulsa líquido"""
    gap = lerp(70, 40, squeeze) * thick
    capsule(c, x, y - 330, x, y - gap / 2 - 40, 70, p)
    capsule(c, x, y + gap / 2 + 40, x, y + 330, 62, p)
    for sg in (-1, 1):
        rrect(c, x - 110, y + sg * (gap / 2) - (22 * thick if sg < 0 else 0), 220, 22 * thick, 10, CYAN, p * 0.9)
    for k in range(6):  # líquido entrando/saindo da cartilagem
        a = k * 1.05 + t * 0.6
        r = lerp(60, 170, squeeze) + 10 * math.sin(t * 3 + k)
        disk(c, x + r * math.cos(a) * 1.2, y + r * math.sin(a) * 0.35, 9, CYAN, p * 0.8)


def jo_carga(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        sq = 0.5 + 0.5 * math.sin(t * 2.4)
        _joint(c, t, 380, 1080, sq, p)
        arrow_v(c, 380, 640, 700 + 40 * sq, PINK, 8, ease_out(prog(t, 0.2, 0.3)))
        mono(c, "CARGA", 420, 680, 26, PINK, p)
        callout(c, 490, 1080, 700, 980, "CARTILAGEM", ease_out(prog(t, 0.3, 0.4)), CYAN, 28)
        chip(c, "PRESSÃO ALIMENTA", CX, 1500, CYAN, NAVY, 46, ease_out(prog(t, 0.45 * d, 0.3)))


def jo_grossa(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        panel(c, LEFT + 10, 720, RIGHT - LEFT - 20, 560, p)
        mono(c, "CARTILAGEM ATRÁS DA PATELA", LEFT + 50, 790, 28, CYAN, p)
        for i, (lab, h, col) in enumerate((("SEM TREINO", 60, MUTED), ("LEVANTADOR", 110, CYAN))):
            q = ease_out(prog(t, 0.3 + i * 0.5, 0.4))
            x = LEFT + 120 + i * 400
            rrect(c, x, 900, 240, 160, 20, NAVY, q)
            rrect(c, x, 1060 + 0, 240, h * q, 14, col, q)
            rrect(c, x, 1060 + h * q, 240, 120, 20, NAVY, q)
            mono(c, lab, x + 120, 1240 + 40, 28, col, q, align="center")
        chip(c, "MAIS GROSSA", CX, 1440, CYAN, NAVY, 50, ease_out(prog(t, 0.55 * d, 0.3)))


def jo_apoio(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = clamp(0.8 + 0.2 * math.sin(t * 1.6))
        j = squat(c, SQX, SQY, 0.76, dep, {"quad": 0.5, "gluteo": 0.4}, t, p)
        kx, ky = j["kne"]; hx, hy = j["hip"]
        cx_, cy_ = lerp(kx, hx, 0.35) - 10, lerp(ky, hy, 0.35) + 40
        g = ease_out(prog(t, 0.3, 0.4))
        ring_pulse(c, cx_, cy_, 34, t, CYAN, g)
        callout(c, cx_, cy_ + 20, 760, 1240, "COXA APOIA", g, CYAN, 30)
        chip(c, "DIVIDE A FORÇA", CX, 1550, PINK, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


# ================================================================ PRIMEIRO TREINO (pr_)
def pr_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = 0.55 + 0.45 * math.sin(t * 2.4 - 1.5)
        j = squat(c, SQX, SQY, 0.72, dep, {"quad": 0.9}, t, p)
        pain_marks(c, j["quad"][0], j["quad"][1], t, ease_out(prog(t, 0.3, 0.3)), 1.0, 7, 60)
        chip(c, "TREINO 1", CX, 1530, PINK, NAVY, 50, ease_out(prog(t, 0.5, 0.3)))


def pr_novo(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        mono(c, "FIBRA DA COXA", LEFT + 40, 800, 28, CYAN, p)
        fiber(c, LEFT + 40, 1020, RIGHT - LEFT - 80, 230, p, acid=0.0, tears=ease(prog(t, 0.4, 1.2)), t=t)
        callout(c, LEFT + 420, 1000, LEFT + 560, 1230, "MICROLESÕES", ease_out(prog(t, 1.0, 0.4)), PINK, 28)
        chip(c, "MOVIMENTO NOVO", CX, 1450, PINK, NAVY, 48, ease_out(prog(t, 0.5 * d, 0.3)))


def pr_protege(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        brain(c, W / 2 - 40, 690, 0.55, 0.5 + 0.5 * math.sin(t * 4))
        k = 1 + int(2.999 * clamp(prog(t, 0.3, d * 0.45)))
        units(c, LEFT + 130, 1080, t, k, 0, p)
        q = ease_out(prog(t, 0.55 * d, 0.3))
        if q > 0:
            for i in range(3):  # reforço por dentro: linhas extras em cada feixe
                ux = LEFT + 130 + i * 270
                for kk in range(5):
                    cap_line(c, ux - 60, 1003 + kk * 40, ux + 60, 1003 + kk * 40, CYAN, 3, q)
        chip(c, "ESFORÇO ESPALHADO", CX, 1430, CYAN, NAVY, 46, ease_out(prog(t, 0.35 * d, 0.3)))


def pr_menos(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        panel(c, LEFT + 10, 720, RIGHT - LEFT - 20, 520, p)
        mono(c, "DOR NO DIA SEGUINTE", LEFT + 50, 790, 28, CYAN, p)
        q1 = ease_out(prog(t, 0.3, 0.5)); q2 = ease_out(prog(t, 0.9, 0.5))
        hbar(c, LEFT + 50, 900, RIGHT - LEFT - 100, 0.9, "TREINO 1", PINK, q1)
        hbar(c, LEFT + 50, 1040, RIGHT - LEFT - 100, 0.3, "MESMO TREINO, 1 SEMANA DEPOIS", CYAN, q2)
        clock(c, CX, 1180 + 30, 0, 0) if False else None
        chip(c, "PROTEÇÃO POR SEMANAS", CX, 1420, CYAN, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


# ================================================================ FALHA (fa_)
def fa_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        ph = (t * 0.45) % 1  # sobe devagar, trava no meio, treme e desce
        bend = 0.45 * ease(ph / 0.5) if ph < 0.5 else (0.45 + 0.02 * math.sin(t * 40) if ph < 0.8 else 0.45 * (1 - ease((ph - 0.8) / 0.2)))
        curl_arm(c, t, LEFT + 40, 1020, 1.05, bend, p)
        chip(c, "NÃO SOBE", CX, 1450, PINK, NAVY, 50, ease_out(prog(t, 0.5, 0.3)))


def fa_poucas(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        brain(c, W / 2 - 40, 690, 0.55, 0.6)
        k = 1 + int(2.999 * clamp(prog(t, 0.6, d * 0.6)))
        units(c, LEFT + 130, 1080, t, k, max(0, k - 1), p)
        chip(c, "CHAMA AS OUTRAS", CX, 1430, CYAN, NAVY, 46, ease_out(prog(t, 0.45 * d, 0.3)))


def fa_todas(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        panel(c, LEFT + 10, 720, RIGHT - LEFT - 20, 560, p)
        mono(c, "DENTRO DA FIBRA", LEFT + 50, 790, 28, CYAN, p)
        k = ease(prog(t, 0.3, d * 0.6))
        hbar(c, LEFT + 50, 900, RIGHT - LEFT - 100, lerp(0.95, 0.15, k), "ENERGIA RÁPIDA", CYAN, ease_out(prog(t, 0.2, 0.3)))
        hbar(c, LEFT + 50, 1040, RIGHT - LEFT - 100, lerp(0.1, 0.9, k), "FOSFATO", PINK, ease_out(prog(t, 0.4, 0.3)))
        for i in range(3):  # 3 grupos, todos acesos
            disk(c, LEFT + 200 + i * 250, 1190, 26, PINK, ease_out(prog(t, 0.5 + i * 0.1, 0.2)))
        mono(c, "TODAS TRABALHANDO", CX, 1250, 24, MUTED, p, align="center")
        chip(c, "CADA UMA RENDE MENOS", CX, 1450, PINK, NAVY, 44, ease_out(prog(t, 0.55 * d, 0.3)))


def fa_lenta(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        panel(c, LEFT + 10, 720, RIGHT - LEFT - 20, 600, p)
        mono(c, "VELOCIDADE DA BARRA", LEFT + 50, 790, 28, CYAN, p)
        vals = (0.95, 0.9, 0.82, 0.72, 0.6, 0.45, 0.28, 0.0)
        bw = (RIGHT - LEFT - 160) / len(vals)
        for i, v in enumerate(vals):
            q = ease_out(prog(t, 0.2 + i * 0.22, 0.25))
            x = LEFT + 80 + i * bw
            h = 380 * v * q
            col = PINK if i >= 6 else CYAN
            if v > 0:
                rrect(c, x + 8, 1240 - h, bw - 16, h, 8, col, q)
            else:
                no_mark(c, x + bw / 2, 1200, 30, q)
            mono(c, str(i + 1), x + bw / 2, 1290, 24, MUTED, q, align="center")
        chip(c, "FICA LENTA E PARA", CX, 1450, PINK, NAVY, 46, ease_out(prog(t, 0.6 * d, 0.3)))


# ================================================================ SEGUNDO A SEGUNDO (sg_) — TESTE: linha do tempo
def sg_hook(c, t, d, b):
    with Cam(c, t, punch=0.08, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        dep = 0.5 + 0.5 * math.sin(t * 2.6 - 1.5)
        squat(c, 400, SQY, 0.7, dep, {"quad": 0.6}, t, p)
        clock(c, RIGHT - 130, 900, 110, clamp(t / max(d, 0.1)), p)
        chip(c, "40 SEGUNDOS", CX, 1530, PINK, NAVY, 50, ease_out(prog(t, 0.5, 0.3)))


def sg_s10(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        timeline(c, t, 10, p)
        mono(c, "RESERVA PRONTA", LEFT + 40, 880, 28, CYAN, p)
        bar_pct(c, LEFT + 40, 905, RIGHT - LEFT - 80, 60, lerp(1.0, 0.45, ease(prog(t, 0.4, d * 0.7))), CYAN, p)
        _mono_right(c, "CREATINA FOSFATO", RIGHT - 40, 1010, 26, MUTED, p)
        dep = 0.5 + 0.5 * math.sin(t * 2.8 - 1.5)
        squat(c, 330, 1560, 0.42, dep, {"quad": 0.4}, t, p)
        chip(c, "0 A 10 S", RIGHT - 170, 1360, CYAN, NAVY, 44, ease_out(prog(t, 0.4 * d, 0.3)))


def sg_s20(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        timeline(c, t, 20, p)
        mono(c, "RESERVA", LEFT + 40, 900, 26, MUTED, p)
        bar_pct(c, LEFT + 40, 920, RIGHT - LEFT - 80, 44, lerp(0.45, 0.15, ease(prog(t, 0.2, 1.0))), MUTED, p)
        mono(c, "AÇÚCAR RÁPIDO", LEFT + 40, 1010, 26, PINK, p)
        bar_pct(c, LEFT + 40, 1030, RIGHT - LEFT - 80, 44, lerp(0.2, 0.85, ease(prog(t, 0.3, 1.2))), PINK, p)
        fiber(c, LEFT + 40, 1250, RIGHT - LEFT - 80, 150, p, acid=ease(prog(t, 0.8, 1.2)), t=t)
        chip(c, "ARDÊNCIA", CX, 1440, PINK, NAVY, 48, ease_out(prog(t, 0.5 * d, 0.3)))


def sg_s30(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY):
        p = ease_out(prog(t, 0, 0.3))
        timeline(c, t, 30, p)
        heart(c, 300, 1040, 1.0, t, p)
        throb(c, 300, 1040, 110, t, 1.0, p)
        bpm = int(lerp(100, 150, ease(prog(t, 0.2, d * 0.7))))
        _mono_right(c, f"{bpm} BPM", RIGHT - 40, 1010, 44, PINK, p)
        # coxa enchendo de sangue
        q = ease(prog(t, 0.3, d * 0.6))
        ellipse(c, 700, 1260, 210, 70, 0, mix(NAVY2, PINK, 0.2 + 0.7 * q), p, CYAN)
        mono(c, "COXA", 700, 1370, 26, MUTED, p, align="center")
        chip(c, "SANGUE CHEGANDO", CX, 1490, PINK, NAVY, 44, ease_out(prog(t, 0.55 * d, 0.3)))


def sg_s40(c, t, d, b):
    with Cam(c, t, punch=0.06, cy=CY, shake=4 * prog(t, 0.5, 0.5)):
        p = ease_out(prog(t, 0, 0.3))
        timeline(c, t, 40, p)
        dep = 0.55 + 0.03 * math.sin(t * 38)
        j = squat(c, 400, 1540, 0.56, dep, {"quad": 1.0, "gluteo": 0.8}, t, p)
        for i in range(3):
            disk(c, RIGHT - 220 + i * 80, 960, 24, PINK, ease_out(prog(t, 0.3 + i * 0.15, 0.2)))
        _mono_right(c, "TODAS AS FIBRAS", RIGHT - 40, 1040, 26, PINK, p)
        chip(c, "A PERNA TREME", RIGHT - 190, 1260, PINK, NAVY, 46, ease_out(prog(t, 0.5 * d, 0.3)))


VIS = dict(jo_hook=jo_hook, jo_carga=jo_carga, jo_grossa=jo_grossa, jo_apoio=jo_apoio,
           pr_hook=pr_hook, pr_novo=pr_novo, pr_protege=pr_protege, pr_menos=pr_menos,
           fa_hook=fa_hook, fa_poucas=fa_poucas, fa_todas=fa_todas, fa_lenta=fa_lenta,
           sg_hook=sg_hook, sg_s10=sg_s10, sg_s20=sg_s20, sg_s30=sg_s30, sg_s40=sg_s40)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "whoosh"), ("0.5d", "pop")]) for k in VIS}
PRE = {"fibra_34_joelho": "jo_", "fibra_35_primeiro": "pr_", "fibra_36_falha": "fa_", "fibra_37_segundos": "sg_"}
for chave, pre in PRE.items():
    v = PA.P[chave]
    VIS[pre + "conc"] = conclusao_factory([(x, True) for x in v["conc"]])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "whoosh"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = SFX_CTA
