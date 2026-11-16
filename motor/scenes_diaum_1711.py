"""DIA UM — produção 17/11: ponte de glúteo em 3 níveis (po_) e medo de se machucar (me_). Caderno (build3).
Ponte de perfil: deitado de costas, cabeça à esquerda, ombros no chão, joelhos dobrados e pés no chão à direita;
o quadril sobe até alinhar ombro-quadril-joelho. No nível 3 a perna livre fica esticada NA LINHA DA COXA (sai do quadril).
Uma figura por cena."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, disk, rrect, draw_text, Cam
from tema_diaum import *
from scenes_diaum_p1 import chip, bubble, FLOOR
from scenes_diaum_g import floor_line, conc_factory, cta_flex, pr_niveis, xmark, CY
from scenes_diaum_1611 import stick_squat
import pauta_1711 as PA

SX = 250          # ombro (no chão)
FX = 800          # tornozelo


def stick_bridge(c, lift, t, seed, one_leg=False, mood="happy", s=1.0):
    """lift 0 = quadril no chão, 1 = ponte completa (ombro-quadril-joelho em linha)"""
    sh = (SX, FLOOR - 34)
    ank = (FX, FLOOR)
    kne = (FX - 70, FLOOR - 230)
    hip_dn = (SX + 300, FLOOR - 34)
    hip_up = (sh[0] + 0.66 * (kne[0] - sh[0]), sh[1] + 0.66 * (kne[1] - sh[1]))
    hip = (lerp(hip_dn[0], hip_up[0], lift), lerp(hip_dn[1], hip_up[1], lift))
    # tronco + braços apoiados no chão
    hline(c, seg(*sh, *hip, 5), INK, 9, t, seed)
    hline(c, seg(sh[0], sh[1], sh[0] + 230, FLOOR - 6, 4), INK, 8, t, seed + 1)
    # perna de apoio: quadril -> joelho -> tornozelo, pé no chão
    hline(c, seg(*hip, *kne, 4) + seg(*kne, *ank, 4)[1:], INK, 9, t, seed + 2)
    hline(c, seg(ank[0] - 10, FLOOR, ank[0] + 70, FLOOR, 3), INK, 9, t, seed + 3)
    if one_leg:
        # perna livre esticada, continuando a linha da coxa
        dx, dy = kne[0] - hip[0], kne[1] - hip[1]
        L = math.hypot(dx, dy)
        ex, ey = hip[0] + dx / L * 300, hip[1] + dy / L * 300
        hline(c, seg(*hip, ex, ey, 5), INK, 9, t, seed + 4)
    else:
        # segunda perna (de perfil, quase sobreposta)
        hline(c, seg(hip[0] + 6, hip[1], kne[0] + 10, kne[1] + 4, 4) + seg(kne[0] + 10, kne[1] + 4, ank[0] + 10, ank[1], 4)[1:],
              INK, 7, t, seed + 5, a=0.5)
    # cabeça deitada à esquerda do ombro
    hx, hy = sh[0] - 82, FLOOR - 60
    hcircle(c, hx, hy, 58, INK, 9, t, seed + 6, fill=PAPER)
    disk(c, hx - 4, hy - 26, 6, INK); disk(c, hx + 22, hy - 20, 6, INK)
    if mood == "happy":
        c.new_path(); c.arc(hx + 10, hy + 2, 24, -0.2, math.pi - 0.9); rgb(c, INK); c.set_line_width(6); c.stroke()
    # glúteo aceso em cima
    if lift > 0.6:
        hcircle(c, hip[0], hip[1] + 8, 40, MARGIN, 6, t, seed + 7)
    return hip


def _lift_cycle(t, up=0.8, hold=0.3, down=0.8, rest=0.3):
    T = up + hold + down + rest
    f = t % T
    if f < up: return ease(f / up), 0.0
    if f < up + hold: return 1.0, f - up
    if f < up + hold + down: return 1 - ease((f - up - hold) / down), 0.0
    return 0.0, 0.0


# ================================================================ PONTE
def po_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        floor_line(c, t)
        lift, _ = _lift_cycle(t)
        stick_bridge(c, lift, t, 4000)
        bubble(c, "glúteo forte?", 560, 860, 360, ease_out(prog(t, 0.15, 0.3)), t, 4010, 56)


def po_ponte(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        floor_line(c, t)
        lift, _ = _lift_cycle(t)
        stick_bridge(c, lift, t, 4100)
        hand(c, "ponte de glúteo", LEFT + 10, 820, 70, MARGIN, ease_out(prog(t, 0.15, 0.35)))
        hand(c, "dá pra fazer em casa", LEFT + 10, 905, 56, BLUEPEN, ease_out(prog(t, 0.45 * d, 0.35)))
        q = ease_out(prog(t, 0.6 * d, 0.35))
        if q > 0:
            chip(c, "3 NÍVEIS", 820, 990, 50, q, t=t, seed=4120)


def _nivel(kind, label, note):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=CY):
            floor_line(c, t)
            if kind == "pausa":
                lift, held = _lift_cycle(t, 0.8, 3.0, 0.8, 0.3)
                if held > 0:
                    marker(c, str(min(3, int(held) + 1)), 880, 990, 140, MARGIN)
            else:
                lift, _ = _lift_cycle(t)
            stick_bridge(c, lift, t, 4200, one_leg=(kind == "uma"))
            hand(c, label, LEFT + 10, 820, 64, MARGIN, ease_out(prog(t, 0.2, 0.35)))
            hand(c, note, LEFT + 10, 900, 56, BLUEPEN, ease_out(prog(t, 0.45 * d, 0.35)))
    return f


def po_regra(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = clamp(prog(t, 0.1, d * 0.5))
        tally(c, LEFT + 20, 800, 15, t, 4300, p)
        hand(c, "15 fáceis", LEFT + 420, 870, 64, INK, ease_out(prog(t, 0.2, 0.3)))
        p2 = ease_out(prog(t, 0.5 * d, 0.35))
        if p2 > 0.05:
            harrow(c, LEFT + 20, 1010, LEFT + 330, 1010, p2, t, 4350, MARGIN, 8)
        if p2 > 0.6:
            chip(c, "SOBE DE NÍVEL", 650, 1010, 50, p2, t=t, seed=4360)
        q = ease_out(prog(t, 0.65 * d, 0.35))
        hand(c, "costas: sem dor", LEFT + 20, 1180, 60, BLUEPEN, q)
        hand(c, "quem trabalha: glúteo", LEFT + 20, 1260, 60, BLUEPEN, q)
        if q > 0:
            checkbox(c, LEFT + 640, 1130, 60, q, t, 4370)


# ================================================================ MEDO
def me_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=CY):
        floor_line(c, t)
        sh = 2.0 * math.sin(t * 22) * (1 - prog(t, 1.2, 0.4))
        stick(c, 300 + sh, FLOOR, 0.9, "guard", t, 5000, mood="sad", blush=True)
        bubble(c, "e se eu me machucar?", 620, 860, 420, ease_out(prog(t, 0.15, 0.3)), t, 5010, 52)
        dumbbell(c, 800, FLOOR - 50, 0.9, t, 5020)


def me_normal(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        floor_line(c, t)
        stick(c, 300, FLOOR, 0.9, "thumb", t, 5100, mood="happy")
        p = ease_out(prog(t, 0.15, 0.35))
        highlight(c, 510, 870, 450 * p, 50, p)
        hand(c, "medo muito comum", 520, 900, 62, INK, p)
        q = ease_out(prog(t, 0.5 * d, 0.35))
        marker(c, "SEGURA", 560, 1080, 96, MARGIN, q)
        hand(c, "das mais seguras", 560, 1160, 56, BLUEPEN, q)


def me_raro(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        hand(c, "lesões (por hora treinada)", LEFT + 10, 820, 56, MUTED, ease_out(prog(t, 0.1, 0.3)))
        base = 1380
        for i, (lab, h, col) in enumerate((("musculação", 120, LIME), ("futebol", 520, MARGIN))):
            p = ease_out(prog(t, 0.3 + i * 0.4, 0.6))
            x = LEFT + 120 + i * 360
            hh = h * p
            pts = [(x, base), (x, base - hh), (x + 200, base - hh), (x + 200, base)]
            if hh > 4:
                c.new_path(); c.move_to(*pts[0])
                for q_ in pts[1:]:
                    c.line_to(*q_)
                c.close_path(); rgb(c, col, 0.85); c.fill()
                hline(c, pts, INK, 6, t, 5200 + i)
            hand(c, lab, x + 100, base + 70, 56, INK, p, align="center")
        hline(c, seg(LEFT, base, RIGHT, base, 8), INK, 6, t, 5210)
        q = ease_out(prog(t, 1.2, 0.4))
        if q > 0:  # seta balançando sobre a barra da musculação (evita quadro parado)
            yb = base - 220 - 30 * math.sin(t * 4)
            harrow(c, LEFT + 220, yb - 120, LEFT + 220, yb, q, t, 5220, MARGIN, 8)
            hand(c, "baixo!", LEFT + 260, yb - 70, 58, MARGIN, q)


def me_leve(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        floor_line(c, t)
        u = 0.5 - 0.5 * math.cos(t * 3.0)
        hx, hy = stick(c, 260, FLOOR, 0.85, pose_mix_("curl_down", "curl_up", u), t, 5300, mood="happy")
        dumbbell(c, hx, hy, 0.55, t, 5310)
        k = clamp(prog(t, 0.2, d * 0.6))
        for i in range(10):
            x = 520 + (i % 5) * 92; y = 900 + (i // 5) * 110
            on = i < 7
            checkbox(c, x, y, 64, (1.0 if k * 7 > i else 0.0) if on else 0.0, t, 5320 + i)
        q = ease_out(prog(t, 0.65 * d, 0.3))
        hand(c, "sobram 3", 720, 1200, 66, MARGIN, q)


def pose_mix_(a, b, u):
    from engine2 import pose_mix
    return pose_mix(a, b, u)


def me_movimento(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        floor_line(c, t)
        dep = 0.5 - 0.5 * math.cos(t * 2.4)
        stick_squat(c, 520, FLOOR, 1.0, dep * 0.85, t, 5400, "happy")
        hand(c, "1º sem peso", LEFT + 10, 820, 62, MARGIN, ease_out(prog(t, 0.15, 0.35)))
        hand(c, "depois, a carga", LEFT + 10, 900, 56, BLUEPEN, ease_out(prog(t, 0.4 * d, 0.35)))
        bubble(c, "me ajuda?", 800, 820, 250, ease_out(prog(t, 0.6 * d, 0.3)), t, 5410, 52)


def me_dor(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=CY):
        p = ease_out(prog(t, 0.1, 0.35))
        marker(c, "NORMAL", LEFT + 20, 840, 70, INK, p)
        for i, s in enumerate(("cansaço", "queimação")):
            q = ease_out(prog(t, 0.25 + i * 0.25, 0.3))
            checkbox(c, LEFT + 20, 900 + i * 100, 58, q, t, 5500 + i)
            hand(c, s, LEFT + 110, 945 + i * 100, 60, INK, q)
        p2 = ease_out(prog(t, 0.5 * d, 0.35))
        marker(c, "PARA", LEFT + 20, 1180, 70 * (1 + 0.05 * math.sin(t * 5)), MARGIN, p2)
        stick(c, 820, FLOOR, 0.6, "guard" if (t % 2.4) > 1.2 else "idle", t, 5530, mood="happy")
        for i, s in enumerate(("pontada", "dor na articulação")):
            q = ease_out(prog(t, 0.55 * d + i * 0.25, 0.3))
            xmark(c, LEFT + 50, 1255 + i * 100, 26 * (1 + 0.15 * math.sin(t * 6 + i)), q, t, 5520 + i)
            hand(c, s, LEFT + 110, 1280 + i * 100, 60, INK, q)


def conc_vivo(items):
    """conclusão do caderno com um lápis marcando cada item em loop (evita quadro congelado > 3 s)"""
    base = conc_factory(items)

    def f(c, t, d, b):
        base(c, t, d, b)
        with Cam(c, t, punch=0.0, cy=CY):
            k = int(t / 1.4) % len(items)
            u = (t % 1.4) / 1.4
            y = 820 + k * 150 + 18
            highlight(c, LEFT + 100, y - 70, 560 * ease(min(1, u * 1.5)), 70, 1.0, LIME, 0.45)
            hline(c, seg(LEFT + 110, y, LEFT + 110 + 520 * ease(u), y, 6), MARGIN, 6, t, 760 + k, a=0.9)
    return f


VIS = dict(po_hook=po_hook, po_ponte=po_ponte,
           po_n1=_nivel("dois", "dois pés no chão", "sobe e aperta o glúteo"),
           po_n2=_nivel("pausa", "pausa lá em cima", "segura 3 segundos"),
           po_n3=_nivel("uma", "uma perna só", "a outra esticada no ar"),
           po_regra=po_regra,
           me_hook=me_hook, me_normal=me_normal, me_raro=me_raro, me_leve=me_leve, me_movimento=me_movimento, me_dor=me_dor)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "swish"), ("0.5d", "pop")]) for k in VIS}
for chave, pre in (("diaum_10_ponte", "po_"), ("diaum_11_medo", "me_")):
    v = PA.P[chave]
    VIS[pre + "conc"] = conc_vivo(v["conc"])
    VIS[pre + "cta"] = cta_flex(v["palavra"], v["cta"])
    SFX[pre + "conc"] = [(0.0, "swish"), ("0.3", "tick"), ("0.5d", "tick")]
    SFX[pre + "cta"] = [(0.0, "swish"), ("0.15", "pop"), ("0.55d", "ding")]
