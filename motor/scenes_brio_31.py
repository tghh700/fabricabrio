"""BRIO 31 — punho dobrado no supino: close do punho, erro e correção."""
import math
from brio_kit2 import *
import roteiro_brio_31_punho as R
BEAT_CTA = R.BEATS[-1]
WX, WY = 500, 1060


def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        wrist(c, WX, WY, 1.5, 1.0, RED)
        x_mark(c, 820, 1000, 0.9, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "PARA!", RED, WHITE, 72, back_out(prog(t, d * 0.45, 0.3)))


def erro(c, t, d, b):
    with Cam(c, t, punch=0.06):
        bx, by = wrist(c, WX, WY, 1.5, 0.85 + 0.15 * math.sin(t * 3), RED)
        arrow(c, bx, by - 30, bx, by + 230, RED, 14, ease_out(prog(t, 0.3, 0.4)))
        tag(c, 540, 1745, "BARRA ATRÁS DO ANTEBRAÇO", RED, WHITE, 50, back_out(prog(t, d * 0.45, 0.3)))


def dor(c, t, d, b):
    with Cam(c, t, punch=0.07):
        wrist(c, WX, WY, 1.5, 1.0, RED)
        a = 0.5 + 0.5 * math.sin(t * 9)
        c.new_path(); c.arc(WX, WY, 100 + 10 * a, 0, 2 * math.pi); rgb(c, RED, 0.9); c.set_line_width(10); c.stroke()
        for k in range(3):
            spark(c, WX + 170 + k * 50, WY - 60 + k * 50, 0.6, t)
        tag(c, 780, 1050, "ALAVANCA NO PUNHO", RED, WHITE, 44, back_out(prog(t, 0.3, 0.3)))
        tag(c, 540, 1745, "DÓI E PERDE FORÇA", RED, WHITE, 58, back_out(prog(t, d * 0.45, 0.3)))


def fix1(c, t, d, b):
    with Cam(c, t, punch=0.06):
        bend = 1 - ease(prog(t, 0.2, d * 0.5))
        bx, by = wrist(c, WX, WY, 1.5, bend, GRN if bend < 0.2 else GREY)
        tag(c, 790, 1000, "BASE DA PALMA", GRN, INK, 46, back_out(prog(t, d * 0.4, 0.3)))
        tag(c, 540, 1745, "NÃO NOS DEDOS", YEL, INK, 60, back_out(prog(t, d * 0.55, 0.3)))


def fix2(c, t, d, b):
    with Cam(c, t, punch=0.06):
        bx, by = wrist(c, WX, WY, 1.5, 0.0, GRN)
        arrow(c, bx, by - 30, bx, WY + 560, GRN, 14, ease_out(prog(t, 0.2, 0.5)))
        check_mark(c, 820, 1050, 0.9, prog(t, 0.35, 0.3))
        tag(c, 540, 1745, "EMPILHADO NO ANTEBRAÇO", GRN, INK, 52, back_out(prog(t, d * 0.4, 0.3)))


def mais(c, t, d, b):
    with Cam(c, t, punch=0.07):
        u = 0.5 - 0.5 * math.cos(t * 2.4)
        wrist(c, 330, WY - 80 * u, 1.2, 0.0, GRN)
        bars(c, 760, 1450, 300, 380, [0.55, 0.8], t, 0.2, cols=[GREY, YEL])
        draw_text(c, "ANTES", 685, 1510, 28, GREY, "Space Mono", 1.0, align="center")
        draw_text(c, "DEPOIS", 835, 1510, 28, YEL, "Space Mono", 1.0, align="center")
        tag(c, 540, 1745, "MAIS FORÇA, MENOS DOR", GRN, INK, 54, back_out(prog(t, d * 0.4, 0.3)))


conc = conc_cards(("BARRA NA BASE DA MÃO", "PUNHO EM PÉ", "ANTEBRAÇO EMBAIXO", "MAIS FORÇA"))
cta = cta_factory("PUNHO", "CARGA · SUPINO", [("40 KG × 8", WHITE), ("42 KG × 8", None)], ("REGISTRE SEU SUPINO", "E VEJA A CARGA SUBIR"))
VIS = {"hook": hook, "erro": erro, "dor": dor, "fix1": fix1, "fix2": fix2, "mais": mais, "conc": conc, "cta": cta}
SFX = sfx_for(VIS, BEAT_CTA)
