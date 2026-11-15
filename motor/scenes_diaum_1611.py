"""DIA UM — produção 16/11: agachamento em 3 níveis (ag_). Caderno, boneco palito rabiscado (build3).
Agachamento de perfil olhando para a direita: joelho vai à frente, quadril vai para trás, tronco inclina um pouco,
braços à frente como contrapeso. Uma figura por cena."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, disk, rrect, draw_text, Cam
from tema_diaum import *
from scenes_diaum_p1 import chip, bubble, FLOOR
from scenes_diaum_g import floor_line, conc_factory, cta_flex, pr_niveis, CY
import pauta_1611 as PA


def stick_squat(c, x, y, s, depth, t, seed, mood="happy", shake=0.0):
    """tornozelo em (x, y). depth 0 = em pé, 1 = coxa um pouco abaixo da paralela"""
    Ls, Lt, Lb = 150 * s, 155 * s, 220 * s
    a_s = math.radians(lerp(3, 30, depth)); a_t = math.radians(lerp(6, 88, depth)); a_b = math.radians(lerp(4, 38, depth))
    x += shake * 4 * math.sin(t * 28)
    ank = (x, y)
    kne = (x + math.sin(a_s) * Ls, y - math.cos(a_s) * Ls)
    hip = (kne[0] - math.sin(a_t) * Lt, kne[1] - math.cos(a_t) * Lt)
    sho = (hip[0] + math.sin(a_b) * Lb, hip[1] - math.cos(a_b) * Lb)
    # pé
    hline(c, seg(ank[0] - 20 * s, y, ank[0] + 70 * s, y, 3), INK, 9, t, seed)
    # pernas (as duas quase sobrepostas, de perfil) + tronco
    hline(c, seg(*ank, *kne, 4) + seg(*kne, *hip, 4)[1:], INK, 9, t, seed + 1)
    hline(c, seg(ank[0] + 8, ank[1], kne[0] + 8, kne[1], 4) + seg(kne[0] + 8, kne[1], hip[0] + 4, hip[1], 4)[1:], INK, 7, t, seed + 2, a=0.55)
    hline(c, seg(*hip, *sho, 5), INK, 9, t, seed + 3)
    # braços à frente (contrapeso), mais alto quanto mais fundo
    arm_a = math.radians(lerp(20, 88, depth))
    hx, hy = sho[0] + math.sin(arm_a) * 220 * s, sho[1] + math.cos(arm_a) * 220 * s
    hline(c, seg(*sho, hx, hy, 4), INK, 9, t, seed + 4)
    # cabeça
    hx_, hy_ = sho[0] + math.sin(a_b) * 85 * s, sho[1] - math.cos(a_b) * 85 * s
    hcircle(c, hx_, hy_, 62 * s, INK, 9, t, seed + 6, fill=PAPER)
    if mood == "happy":
        c.new_path(); c.arc(hx_ + 6 * s, hy_ + 4 * s, 28 * s, 0.3, math.pi - 0.3); rgb(c, INK); c.set_line_width(6); c.stroke()
    elif mood == "worried":
        c.new_path(); c.arc(hx_ + 6 * s, hy_ + 34 * s, 22 * s, math.pi + 0.5, 2 * math.pi - 0.5); rgb(c, INK); c.set_line_width(6); c.stroke()
    disk(c, hx_ - 12 * s, hy_ - 16 * s, 6, INK); disk(c, hx_ + 26 * s, hy_ - 16 * s, 6, INK)
    return dict(hip=hip, kne=kne, sho=sho)


def chair(c, x, seat_y, t, seed, p=1.0):
    """cadeira de perfil; x = frente do assento"""
    if p <= 0:
        return
    pts_seat = seg(x - 230, seat_y, x, seat_y, 4)
    hline(c, pts_seat, INK, 9, t, seed, p=p)
    hline(c, seg(x - 10, seat_y, x - 10, FLOOR, 4), INK, 8, t, seed + 1, p=p)
    hline(c, seg(x - 220, seat_y, x - 220, FLOOR, 4), INK, 8, t, seed + 2, p=p)
    hline(c, seg(x - 230, seat_y, x - 250, seat_y - 230, 4), INK, 8, t, seed + 3, p=p)


AX = 560   # tornozelo
S = 1.15


def _depth_cycle(t, down=1.0, hold=0.3, up=0.9, rest=0.4):
    T = down + hold + up + rest
    f = t % T
    if f < down: return ease(f / down), 0.0
    if f < down + hold: return 1.0, (f - down)
    if f < down + hold + up: return 1 - ease((f - down - hold) / up), 0.0
    return 0.0, 0.0


def _seat_y(depth):
    a_s = math.radians(lerp(3, 30, depth)); a_t = math.radians(lerp(6, 88, depth))
    ky = FLOOR - math.cos(a_s) * 150 * S
    return ky - math.cos(a_t) * 155 * S, AX + math.sin(a_s) * 150 * S - math.sin(a_t) * 155 * S


SEAT_Y, SEAT_X = _seat_y(0.82)


def ag_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        floor_line(c, t)
        q = ease_out(prog(t, 0.45 * d, 0.4))
        if q > 0:
            chair(c, SEAT_X + 40 + (1 - q) * -300, SEAT_Y + 6, t, 3000, q)
        dep = 0.5 - 0.5 * math.cos(t * 3.0)
        stick_squat(c, AX, FLOOR, S, dep * (0.55 if q < 1 else 0.82), t, 3010, "worried" if q < 1 else "happy", shake=1.0 - q)
        bubble(c, "difícil?", 330, 820, 300, ease_out(prog(t, 0.15, 0.3)), t, 3020, 58)


def _nivel(kind, label, note):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=CY):
            floor_line(c, t)
            if kind == "cadeira":
                dep, _ = _depth_cycle(t, 1.0, 0.5, 0.9, 0.4)
                dep *= 0.82
                chair(c, SEAT_X + 40, SEAT_Y + 6, t, 3100)
            elif kind == "livre":
                dep, _ = _depth_cycle(t, 1.0, 0.15, 0.9, 0.35)
            else:
                dep, held = _depth_cycle(t, 1.0, 3.0, 0.9, 0.4)
                if held > 0:
                    marker(c, str(min(3, int(held) + 1)), 860, 930, 150, MARGIN)
            stick_squat(c, AX, FLOOR, S, dep, t, 3110, "happy")
            p = ease_out(prog(t, 0.2, 0.35))
            hand(c, label, LEFT + 10, 820, 64, MARGIN, p)
            q = ease_out(prog(t, 0.45 * d, 0.35))
            hand(c, note, LEFT + 10, 900, 56, BLUEPEN, q)
    return f


def ag_regra(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        for i in range(3):
            y = 820 + i * 140
            hand(c, f"série {i + 1}", LEFT + 20, y + 50, 64, INK, ease_out(prog(t, 0.1 + i * 0.2, 0.3)))
            checkbox(c, LEFT + 300, y, 64, ease_out(prog(t, 0.3 + i * 0.35, 0.3)), t, 3300 + i)
            hand(c, "12 bem feitas", LEFT + 400, y + 50, 58, BLUEPEN, ease_out(prog(t, 0.3 + i * 0.35, 0.3)))
        p2 = ease_out(prog(t, 0.55 * d, 0.35))
        if p2 > 0.05:
            harrow(c, LEFT + 20, 1330, LEFT + 330, 1330, p2, t, 3350, MARGIN, 8)
        if p2 > 0.6:
            chip(c, "PRÓXIMO NÍVEL", 650, 1330, 50, p2, t=t, seed=3360)


VIS = dict(ag_hook=ag_hook, ag_niveis=pr_niveis,
           ag_n1=_nivel("cadeira", "senta e levanta", "sem usar as mãos"),
           ag_n2=_nivel("livre", "sem a cadeira", "quadril pra trás"),
           ag_n3=_nivel("pausa", "pausa embaixo", "segura 3 segundos"),
           ag_regra=ag_regra)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "swish"), ("0.5d", "pop")]) for k in VIS}
v = PA.P["diaum_09_agacha"]
VIS["ag_conc"] = conc_factory(v["conc"])
VIS["ag_cta"] = cta_flex(v["palavra"], v["cta"])
SFX["ag_conc"] = [(0.0, "swish"), ("0.3", "tick"), ("0.5d", "tick")]
SFX["ag_cta"] = [(0.0, "swish"), ("0.15", "pop"), ("0.55d", "ding")]
