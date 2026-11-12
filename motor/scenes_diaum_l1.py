"""DIA UM — lote extra 12/11: começar depois dos 40 e flexão em 3 níveis."""
import math
from engine2 import clamp, ease, ease_out, back_out, lerp, prog, mix, disk, rrect, draw_text, Cam, pose_mix
from tema_diaum import *
from scenes_diaum_p1 import chip, bubble, FLOOR

PENCIL = (0.85, 0.65, 0.2)


def cta_factory(label):
    def cta(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=1100):
            p = ease_out(prog(t, 0, 0.35))
            hcircle(c, W / 2, 840, 130, INK, 9, t, 800, p, fill=LIME if p >= 1 else None)
            if p > 0.6:
                marker(c, "1", W / 2 - 34, 905, 180, INK)
            chip(c, label, W / 2, 1060, 62, ease_out(prog(t, 0.15, 0.35)), t=t, seed=810)
            q = ease_out(prog(t, 0.35 * d, 0.4))
            hand(c, "registre e acompanhe seus", W / 2, 1180, 52, INK, q, align="center")
            hand(c, "treinos gratuitamente", W / 2, 1236, 52, INK, q, align="center")
            chip(c, "LINK NA BIO", W / 2, 1360, 56, ease_out(prog(t, 0.55 * d, 0.35)), col=(1, 1, 1), t=t, seed=820)
    return cta


def pushup(c, px, py, L, ang, hand_pt, t, seed, mood="neutral", knees=False):
    """boneco de perfil fazendo flexão. (px,py) = ponto de apoio (pés ou joelhos); ang = inclinação do corpo (graus, 0 = deitado);
    hand_pt = onde as mãos apoiam. Olhando para a direita."""
    a = math.radians(ang)
    sh = (px + L * math.cos(a), py - L * math.sin(a))
    head = (px + (L + 85) * math.cos(a), py - (L + 85) * math.sin(a))
    hip = (px + 0.45 * L * math.cos(a), py - 0.45 * L * math.sin(a))
    if knees:  # canelas no chão, para trás
        hline(c, seg(px, py, px - 200, py, 4), INK, 9, t, seed)
    hline(c, seg(px, py, sh[0], sh[1], 6), INK, 9, t, seed + 1)
    # braço com cotovelo (2 segmentos de 150)
    hx, hy = hand_pt
    D = math.hypot(hx - sh[0], hy - sh[1]); seg_ = 112
    mx, my = (sh[0] + hx) / 2, (sh[1] + hy) / 2
    if D >= 2 * seg_:
        el = (mx, my)
    else:
        k = math.sqrt(max(0, seg_ ** 2 - (D / 2) ** 2))
        nx, ny = -(hy - sh[1]) / D, (hx - sh[0]) / D
        if nx * (px - mx) + ny * (py - my) < 0:  # cotovelo aponta para o lado dos pés
            nx, ny = -nx, -ny
        el = (mx + nx * k, my + ny * k)
    hline(c, seg(sh[0], sh[1], el[0], el[1], 3) + seg(el[0], el[1], hx, hy, 3)[1:], INK, 9, t, seed + 2)
    hcircle(c, head[0], head[1], 55, INK, 8, t, seed + 3, fill=PAPER)
    if mood == "happy":
        c.new_path(); c.arc(head[0] + 6, head[1] + 4, 24, 0.3, math.pi - 0.3); rgb(c, INK); c.set_line_width(6); c.stroke()
    disk(c, head[0] + 18, head[1] - 12, 6, INK)
    return hip


def nivel(kind):
    def f(c, t, d, b):
        with Cam(c, t, punch=0.05, cy=1100):
            bob = 0.5 + 0.5 * math.sin(t * 3.2)
            p = ease_out(prog(t, 0, 0.3))
            if kind == "parede":
                wx = 860
                hline(c, seg(wx, FLOOR, wx, 700, 6), INK, 9, t, 900)
                for k in range(5):
                    hline(c, seg(wx, 760 + k * 140, wx + 60, 720 + k * 140, 2), MUTED, 4, t, 905 + k)
                L = 470; px_ = 470
                shx = wx - 212 * lerp(0.97, 0.5, bob)
                ang = math.degrees(math.acos(clamp((shx - px_) / L)))
                sh_y = FLOOR - L * math.sin(math.radians(ang))
                pushup(c, px_, FLOOR, L, ang, (wx - 6, sh_y + 10), t, 910, "happy")
                hand(c, "parede", LEFT + 20, 800, 64, MARGIN, p)
            elif kind == "banco":
                bx0, bx1, by = 560, 840, 1250
                hline(c, [(bx0, by), (bx1, by), (bx1, FLOOR), (bx0, FLOOR), (bx0, by)], INK, 8, t, 920)
                L = 600; ax = 150
                shy = by - 212 * lerp(0.97, 0.5, bob)
                ang = math.degrees(math.asin(clamp((FLOOR - shy) / L)))
                shx = ax + L * math.cos(math.radians(ang))
                pushup(c, ax, FLOOR, L, ang, (shx + 8, by), t, 930, "happy")
                hand(c, "banco ou mesa", LEFT + 20, 800, 58, MARGIN, p)
            elif kind == "joelho":
                L = 400; ax = 380
                ang = math.degrees(math.asin(clamp(212 * lerp(0.97, 0.5, bob) / L)))
                shx = ax + L * math.cos(math.radians(ang))
                pushup(c, ax, FLOOR, L, ang, (shx + 8, FLOOR), t, 940, "happy", knees=True)
                hcircle(c, ax, FLOOR - 8, 34, MARGIN, 6, t, 945, p)
                hand(c, "joelhos no chão", LEFT + 20, 800, 58, MARGIN, p)
            else:  # chão
                L = 600; ax = 160
                ang = math.degrees(math.asin(clamp(212 * lerp(0.97, 0.5, bob) / L)))
                shx = ax + L * math.cos(math.radians(ang))
                pushup(c, ax, FLOOR, L, ang, (shx + 8, FLOOR), t, 950, "happy")
                highlight(c, LEFT + 10, 755, 330, 64, prog(t, 0.4 * d, 0.3))
                hand(c, "a primeira!", LEFT + 20, 800, 70, MARGIN, p)
            hline(c, seg(LEFT, FLOOR + 6, RIGHT, FLOOR + 6, 10), INK, 6, t, 960)
    return f


def fl_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=1100):
        L = 560; ax = 180
        ang = math.degrees(math.asin(clamp(212 * (0.5 + 0.06 * math.sin(t * 5)) / L)))  # tenta e não sobe
        pushup(c, ax, FLOOR, L, ang, (ax + L * math.cos(math.radians(ang)) + 8, FLOOR), t, 970)
        hline(c, seg(LEFT, FLOOR + 6, RIGHT, FLOOR + 6, 10), INK, 6, t, 975)
        bubble(c, "nem uma...", 640, 820, 380, ease_out(prog(t, 0.3, 0.4)), t, 980, 56)
        if prog(t, 0.55 * d, 0.2) > 0:
            chip(c, "NORMAL!", 760, 1100, 60, ease_out(prog(t, 0.55 * d, 0.3)), t=t, seed=985)


def fl_sobe(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        for i in range(3):
            y = 780 + i * 150
            p = ease_out(prog(t, 0.1 + i * 0.2, 0.3))
            hand(c, f"série {i + 1}", LEFT + 20, y + 50, 64, INK, p)
            tally(c, LEFT + 300, y, 12, t, 990 + i * 20, prog(t, 0.15 + i * 0.2, 0.5), 70)
        p2 = ease_out(prog(t, 0.6 * d, 0.35))
        if p2 > 0.05:
            harrow(c, LEFT + 300, 1330, LEFT + 650, 1330, p2, t, 1050, MARGIN, 8)
        if p2 > 0.6:
            chip(c, "PRÓXIMO NÍVEL", 790, 1330, 50, p2, t=t, seed=1060)


# ----------------------------------------------------------------- 40 anos
def id_hook(c, t, d, b):
    with Cam(c, t, punch=0.07, cy=1100):
        stick(c, 300, FLOOR, 0.95, "guard", t, 1100, face=1, mood="sad", blush=True)
        bubble(c, "tenho 40...", 640, 760, 400, ease_out(prog(t, 0.2, 0.4)), t, 1110, 56)
        if prog(t, 0.5 * d, 0.2) > 0:
            hcircle(c, 760, 1100, 130, INK, 8, t, 1120, ease_out(prog(t, 0.5 * d, 0.4)), fill=LIME)
            marker(c, "DÁ!", 690, 1130, 90, INK, ease_out(prog(t, 0.6 * d, 0.3)))


def id_idade(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        for i, (age, x) in enumerate(((20, 220), (40, 520), (70, 820))):
            p = ease_out(prog(t, 0.1 + i * 0.25, 0.35))
            if p <= 0:
                continue
            up = int(t * 2 + i) % 2
            stick(c, x, FLOOR, 0.7, "curl_up" if up else "curl_down", t, 1200 + i * 10, face=1, mood="happy")
            dumbbell(c, x + 12, FLOOR - 346 if up else FLOOR - 228, 0.34, t, 1205 + i * 10)
            marker(c, str(age), x - 40, 760, 84, MARGIN if age == 70 else INK, p)
        hand(c, "o músculo responde", W / 2, 1520, 56, MUTED, ease_out(prog(t, 0.6 * d, 0.3)), align="center") if False else None


def id_corpo(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        bob = 0.5 + 0.5 * math.sin(t * 3)
        # 1) agachamento na cadeira
        p1 = ease_out(prog(t, 0.05, 0.3))
        hline(c, [(90, 1300), (230, 1300), (230, FLOOR), (90, FLOOR)], INK, 7, t, 1300, p=p1)
        hline(c, seg(90, 1300, 90, 1120, 3), INK, 7, t, 1301, p=p1)
        stick(c, 260, FLOOR, 0.55, pose_mix("squat_half", "idle", bob) if p1 > 0 else "idle", t, 1302, face=1)
        hand(c, "cadeira", 110, 790, 50, MARGIN, p1)
        # 2) flexão na parede
        p2 = ease_out(prog(t, 0.3 * d, 0.3))
        if p2 > 0:
            wx = 650
            hline(c, seg(wx, FLOOR, wx, 1000, 4), INK, 7, t, 1310)
            L = 330; px_ = 420
            shx = wx - 200 * lerp(0.97, 0.55, bob)
            ang = math.degrees(math.acos(clamp((shx - px_) / L)))
            pushup(c, px_, FLOOR, L, ang, (wx - 4, FLOOR - L * math.sin(math.radians(ang)) + 8), t, 1311)
            hand(c, "parede", 430, 790, 50, MARGIN, p2)
        # 3) remada com elástico
        p3 = ease_out(prog(t, 0.55 * d, 0.3))
        if p3 > 0:
            px = 850
            stick(c, px, FLOOR, 0.55, "idle", t, 1320, face=-1)
            hx = px - 150 + 60 * bob
            hline(c, seg(RIGHT - 10, 1180, hx, 1170, 4), MARGIN, 6, t, 1321)  # elástico preso
            hline(c, seg(RIGHT - 10, 1100, RIGHT - 10, 1260, 2), INK, 8, t, 1322)
            hand(c, "elástico", 760, 790, 50, MARGIN, p3)


def id_vezes(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        dias = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
        marcados = {0: 0.2, 2: 0.4, 4: 0.6}
        for i, s in enumerate(dias):
            x = LEFT + 10 + i * 118
            p = ease_out(prog(t, 0.05 + i * 0.04, 0.3))
            hand(c, s.lower(), x + 6, 900, 46, INK, p)
            checkbox(c, x + 10, 940, 70, ease_out(prog(t, marcados[i] * d + 0.2, 0.3)) if i in marcados else 0.0, t, 1400 + i)
        clock(c, W / 2, 1230, 120, 0.67 * ease(prog(t, 0.3 * d, 0.5 * d)), t, 1420)
        hand(c, "40 min", W / 2 + 160, 1250, 60, BLUEPEN, ease_out(prog(t, 0.5 * d, 0.3)))


def id_devagar(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        up = int(t * 1.2) % 2  # devagar
        stick(c, 330, FLOOR, 0.85, "curl_up" if up else "curl_down", t, 1500, face=1, mood="happy")
        dumbbell(c, 345, FLOOR - 422 if up else FLOOR - 280, 0.36, t, 1505)
        hand(c, "leve", 250, 790, 60, MARGIN, ease_out(prog(t, 0.1, 0.3)))
        p = ease_out(prog(t, 0.45 * d, 0.35))
        if p > 0:
            hcircle(c, 790, 1050, 120, MARGIN, 8, t, 1510, p)
            hline(c, seg(790, 990, 790, 1110, 2), MARGIN, 16, t, 1511, p=p)
            hline(c, seg(730, 1050, 850, 1050, 2), MARGIN, 16, t, 1512, p=p)
            hand(c, "passa no médico", 790, 1250, 54, INK, p, align="center")
            hand(c, "se precisar", 790, 1305, 54, INK, p, align="center")


def id_anota(c, t, d, b):
    with Cam(c, t, punch=0.05, cy=1100):
        linhas = [("agacha cadeira", "3 × 10"), ("flexão parede", "3 × 8"), ("remada elástico", "3 × 12")]
        for i, (a_, b_) in enumerate(linhas):
            y = 830 + i * 150
            hand(c, a_, LEFT + 20, y, 64, INK, ease_out(prog(t, 0.1 + i * 0.2, 0.35)))
            hand(c, b_, LEFT + 560, y, 64, BLUEPEN, ease_out(prog(t, 0.2 + i * 0.2, 0.35)))
        p = ease_out(prog(t, 0.6 * d, 0.35))
        if p > 0:
            highlight(c, LEFT + 320, 1275, 330, 64, prog(t, 0.65 * d, 0.3))
            marker(c, "+ FORTE", LEFT + 330, 1330, 84, INK, p)


VIS = dict(
    fl_hook=fl_hook, fl_parede=nivel("parede"), fl_banco=nivel("banco"), fl_joelho=nivel("joelho"), fl_sobe=fl_sobe, fl_chao=nivel("chao"),
    fl_cta=cta_factory("COMENTA SEU NÍVEL"),
    id_hook=id_hook, id_idade=id_idade, id_corpo=id_corpo, id_vezes=id_vezes, id_devagar=id_devagar, id_anota=id_anota,
    id_cta=cta_factory("COMENTA COMECEI"),
)
SFX = {k: ([(0.0, "boom"), ("0.4", "pop")] if k.endswith("hook") else [(0.0, "swish"), ("0.15", "pop"), ("0.55d", "ding")] if k.endswith("cta")
           else [(0.0, "swish"), ("0.5d", "pop")]) for k in VIS}
