"""Motor v2 — estética "dark chunky": fundo escuro com grade em perspectiva, bonecos gordinhos de membros arredondados,
títulos em Anton (linha branca + linha amarela) e kicker monoespaçado. Vertical 1080x1920."""
import math, random
import cairo

W, H = 1080, 1920
FPS = 30
BG0 = (0.055, 0.063, 0.078)
BG1 = (0.105, 0.118, 0.141)
WHITE = (0.96, 0.95, 0.92)
YEL = (0.98, 0.73, 0.10)
RED = (0.93, 0.27, 0.29)
GRN = (0.24, 0.75, 0.42)
BLU = (0.35, 0.72, 1.0)
GREY = (0.62, 0.64, 0.69)
DARK = (0.17, 0.19, 0.23)
# boneco claro
L_BODY = (0.96, 0.95, 0.91); L_FRONT = (0.80, 0.77, 0.72); L_BACK = (0.66, 0.63, 0.59)
# boneco escuro
D_BODY = (0.31, 0.33, 0.39); D_FRONT = (0.27, 0.29, 0.34); D_BACK = (0.21, 0.22, 0.26)
FLOOR_Y = 1640

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def back_out(x):
    x = clamp(x); c = 1.9; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def lerp(a, b, t): return a + (b - a) * t
def prog(t, s, d): return clamp((t - s) / d) if d > 0 else float(t >= s)
def mix(a, b, t): return tuple(lerp(x, y, clamp(t)) for x, y in zip(a, b))

def rgb(c, col, a=1.0): c.set_source_rgba(*col, a)
def cap_line(c, x1, y1, x2, y2, col, w, a=1.0):
    c.move_to(x1, y1); c.line_to(x2, y2); rgb(c, col, a); c.set_line_width(w); c.set_line_cap(cairo.LINE_CAP_ROUND); c.stroke()
def poly(c, pts, col, w, a=1.0):
    c.move_to(*pts[0]);
    for p in pts[1:]: c.line_to(*p)
    rgb(c, col, a); c.set_line_width(w); c.set_line_cap(cairo.LINE_CAP_ROUND); c.set_line_join(cairo.LINE_JOIN_ROUND); c.stroke()
def disk(c, x, y, r, col, a=1.0):
    c.new_path(); c.arc(x, y, r, 0, 2 * math.pi); rgb(c, col, a); c.fill()
def rrect(c, x, y, w, h, r, col=None, a=1.0):
    r = min(r, w / 2, h / 2)
    c.new_sub_path(); c.arc(x + w - r, y + r, r, -math.pi / 2, 0); c.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    c.arc(x + r, y + h - r, r, math.pi / 2, math.pi); c.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2); c.close_path()
    if col is not None: rgb(c, col, a); c.fill()

# ------------------------------------------------------------ fundo
def background(c, t):
    g = cairo.RadialGradient(W / 2, 1150, 50, W / 2, 1150, 1300)
    g.add_color_stop_rgb(0, *BG1); g.add_color_stop_rgb(1, *BG0)
    c.set_source(g); c.paint()
    # grade em perspectiva no chão
    vx, vy = W / 2, 1180
    c.set_line_width(2)
    for i in range(-9, 10):
        x = W / 2 + i * 260
        c.move_to(vx + (x - vx) * 0.08, FLOOR_Y - 40); c.line_to(x, H)
    for k in range(7):
        f = (k + (t * 0.15) % 1) / 7
        y = FLOOR_Y - 40 + (H - FLOOR_Y + 40) * f ** 1.8
        c.move_to(0, y); c.line_to(W, y)
    rgb(c, (1, 1, 1), 0.045); c.stroke()
    # sombra do chão
    g2 = cairo.LinearGradient(0, FLOOR_Y - 120, 0, FLOOR_Y + 60)
    g2.add_color_stop_rgba(0, 0, 0, 0, 0); g2.add_color_stop_rgba(1, 0, 0, 0, 0.0)
    c.set_source(g2); c.rectangle(0, FLOOR_Y - 120, W, 180); c.fill()

def shadow(c, x, y, w):
    c.save(); c.translate(x, y); c.scale(1, 0.18)
    g = cairo.RadialGradient(0, 0, 0, 0, 0, w)
    g.add_color_stop_rgba(0, 0, 0, 0, 0.55); g.add_color_stop_rgba(1, 0, 0, 0, 0)
    c.set_source(g); c.arc(0, 0, w, 0, 2 * math.pi); c.fill(); c.restore()

# ------------------------------------------------------------ texto
def font(c, name, size, bold=False):
    c.select_font_face(name, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL); c.set_font_size(size)

def wrap(c, s, size, maxw, fname="Anton"):
    font(c, fname, size); words = s.split(); lines = []; cur = ""
    for w_ in words:
        test = (cur + " " + w_).strip()
        if c.text_extents(test).x_advance > maxw and cur: lines.append(cur); cur = w_
        else: cur = test
    if cur: lines.append(cur)
    return lines

def draw_text(c, s, x, y, size, col, fname="Anton", a=1.0, align="left", spacing=0.0):
    font(c, fname, size)
    if spacing:
        total = sum(c.text_extents(ch).x_advance + spacing for ch in s) - spacing
        xx = x - (total / 2 if align == "center" else 0)
        for ch in s:
            c.move_to(xx, y); rgb(c, col, a); c.show_text(ch); xx += c.text_extents(ch).x_advance + spacing
        return total
    ext = c.text_extents(s)
    xx = x - ext.x_advance / 2 if align == "center" else x
    c.move_to(xx, y); rgb(c, col, a); c.show_text(s)
    return ext.x_advance

def headline(c, t, k, t1, t2, x=56, y=300, size=150):
    """kicker + título em 2 cores, com entrada animada"""
    pk = ease_out(prog(t, 0.0, 0.25))
    if k:
        rrect(c, x, y - 22, 18, 18, 2, YEL, pk)
        draw_text(c, k.upper(), x + 36, y - 3, 30, GREY, "Space Mono", pk, spacing=7)
    yy = y + 40
    lines = [(l, WHITE) for l in wrap(c, t1, size, W - 2 * x)] + [(l, YEL) for l in wrap(c, t2, size, W - 2 * x)]
    if len(lines) > 3:
        size = int(size * 0.78)
        lines = [(l, WHITE) for l in wrap(c, t1, size, W - 2 * x)] + [(l, YEL) for l in wrap(c, t2, size, W - 2 * x)]
    for i, (ln, col) in enumerate(lines):
        p = ease_out(prog(t, 0.04 + i * 0.07, 0.28))
        if p <= 0: continue
        draw_text(c, ln, x, yy + size * 0.92 * (i + 1) + (1 - p) * 60, size, col, "Anton", p)
    return yy + size * 0.92 * len(lines)

def label(c, s, x, y, col=WHITE, size=78, a=1.0):
    draw_text(c, s, x, y, size, col, "Anton", a, align="center")

# ------------------------------------------------------------ boneco gordinho
POSES = {
    #        braço trás     braço frente    perna trás    perna frente   (graus; 0 = pra baixo, + = pra frente)
    "idle":  (-12, 25,      14, 30,         -10, 6,       12, 6),
    "reach": (-12, 25,      78, 8,          -10, 6,       14, 6),
    "reach_low": (-12, 25,  55, 20,         -10, 6,       14, 6),
    "point_up": (-12, 25,   150, 10,        -10, 6,       12, 6),
    "scratch": (-12, 25,    150, 140,       -10, 6,       12, 6),
    "shrug": (55, -95,      55, -95,        -10, 6,       12, 6),
    "laugh": (25, -125,     30, -120,       -16, 8,       16, 8),
    "phone_up": (-12, 25,   120, 35,        -10, 6,       12, 6),
    "thumb": (-12, 25,      55, -110,       -10, 6,       12, 6),
    "cheer": (150, 10,      160, 10,        -16, 6,       16, 6),
    "push": (-12, 25,       95, -10,        -18, 10,      28, 0),
    "guard": (45, -150,     60, -140,       -22, 14,      24, -8),
    "shock": (150, 30,      155, -30,       -28, 0,       28, 0),
    "walk1": (25, 15,       -25, 25,        -28, 18,      28, 0),
    "walk2": (-25, 25,      25, 15,         28, 0,        -28, 18),
    # academia
    "bar_back": (150, -150,   150, -150,      -8, 4,        8, 4),      # barra nas costas, em pé
    "squat_half": (150, -150, 150, -150,      45, -70,      55, -80),
    "squat_deep": (150, -150, 150, -150,      85, -115,     95, -125),
    "curl_down": (-5, 5,      5, 5,           -10, 6,       12, 6),
    "curl_up": (-5, 5,        5, 150,         -10, 6,       12, 6),
    "flex": (-5, 5,           90, 90,         -14, 6,       14, 6),      # bíceps de perfil: braço à frente, antebraço pra cima (12/11)
    "tired": (-5, 0,          5, 0,           -6, 4,        6, 4),
}

def pose_mix(a, b, t):
    pa = POSES[a] if isinstance(a, str) else a; pb = POSES[b] if isinstance(b, str) else b
    return tuple(lerp(x, y, ease(t)) for x, y in zip(pa, pb))

def chunky(c, x, y, s=1.0, pose="idle", dark=False, face=1, bob=0.0, glove=False, helmet=False, t=0.0, squash=0.0):
    """pés em (x,y); face=1 olha pra direita, -1 pra esquerda. Retorna posição da mão da frente."""
    p = POSES[pose] if isinstance(pose, str) else pose
    body, front, back = (D_BODY, D_FRONT, D_BACK) if dark else (L_BODY, L_FRONT, L_BACK)
    shadow(c, x, y + 4, 170 * s)
    lh = 155 * math.cos(math.radians(p[6])) + 150 * math.cos(math.radians(p[6] + p[7]))
    drop = max(0.0, 305 - lh)
    c.save(); c.translate(x, y); c.scale(s * face, s * (1 - squash)); c.translate(0, bob + drop)
    LW = 50
    hip = (0, -300); sh = (0, -520)
    def limb(base, a1, a2, L1, L2, col, foot=False):
        r1 = math.radians(a1); j = (base[0] + L1 * math.sin(r1), base[1] + L1 * math.cos(r1))
        r2 = math.radians(a1 + a2); e = (j[0] + L2 * math.sin(r2), j[1] + L2 * math.cos(r2))
        poly(c, [base, j, e], col, LW)
        if foot: cap_line(c, e[0] - 8, e[1], e[0] + 46, e[1], col, LW * 0.8)
        return e
    # trás
    limb((hip[0] - 6, hip[1]), p[4], p[5], 155, 150, back, foot=True)
    limb((sh[0] - 10, sh[1] + 10), p[0], p[1], 120, 110, back)
    # tronco
    rrect(c, -68, sh[1] - 40, 136, (hip[1] - sh[1]) + 80, 66, body)
    # frente
    limb((hip[0] + 6, hip[1]), p[6], p[7], 155, 150, front, foot=True)
    hand = limb((sh[0] + 10, sh[1] + 10), p[2], p[3], 120, 110, front)
    if glove: disk(c, hand[0], hand[1], 34, YEL)
    # cabeça
    disk(c, 0, sh[1] - 95, 68, body)
    if helmet:
        c.new_path(); c.arc(0, sh[1] - 110, 74, math.pi, 2 * math.pi); c.close_path(); rgb(c, YEL); c.fill()
        cap_line(c, -10, sh[1] - 108, 92, sh[1] - 108, YEL, 16)
    c.restore()
    return (x + hand[0] * s * face, y + (hand[1] + bob + drop) * s * (1 - squash))

# ------------------------------------------------------------ objetos (flat)
def wall(c, x, y, w, h):
    rrect(c, x, y, w, h, 26, (0.16, 0.18, 0.22))

def outlet(c, x, y, s=1.0, plate=True, module=True, heat=0.0, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    if plate: rrect(c, -110, -160, 220, 320, 34, mix((0.93, 0.92, 0.89), (1, 0.55, 0.4), heat), a)
    if module:
        # rebaixo sextavado do padrão brasileiro (NBR 14136): pontas à esquerda/direita, topo e base retos
        def hexa(rx, ry):
            c.new_path()
            for i in range(6):
                ang = i * math.pi / 3
                (c.move_to if i == 0 else c.line_to)(rx * math.cos(ang), ry * math.sin(ang))
            c.close_path()
        hexa(92, 84); rgb(c, (0.72, 0.71, 0.68), a); c.fill()
        hexa(80, 72); rgb(c, (0.86, 0.85, 0.82), a); c.fill()
        # 3 furos quase em linha, o do meio (terra) levemente deslocado pra cima
        for px, py in [(-44, 10), (0, -6), (44, 10)]: disk(c, px, py, 12, (0.12, 0.12, 0.14), a)
    c.restore()

def module_back(c, x, y, s=1.0):
    """parte de trás do módulo de tomada, com os 3 bornes (parafusos) alinhados aos furos"""
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -100, -85, 200, 170, 22, (0.78, 0.77, 0.74))
    rrect(c, -88, -73, 176, 146, 16, (0.70, 0.69, 0.66))
    for px, py in [(-44, 10), (0, -6), (44, 10)]:
        rrect(c, px - 17, py - 17, 34, 34, 6, (0.80, 0.62, 0.25))
        disk(c, px, py, 11, (0.62, 0.62, 0.64)); cap_line(c, px - 7, py, px + 7, py, (0.3, 0.3, 0.32), 3)
    c.restore()

def wall_box(c, x, y, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -95, -140, 190, 280, 18, (0.09, 0.10, 0.12))
    c.restore()

def wires(c, x, y, s=1.0, t=0.0, out=1.0, highlight=None, ends=None):
    """3 fios saindo da caixinha: terra (verde), neutro (azul claro), fase (vermelho)"""
    cols = [("T", GRN), ("N", BLU), ("F", RED)]
    res = {}
    for i, (nm, col) in enumerate(cols):
        sx = x + (i - 1) * 40 * s
        ex = x + (i - 1) * 120 * s + math.sin(t * 2 + i) * 6
        ey = y + 40 * s - 170 * s * out
        if ends and nm in ends: ex, ey = ends[nm]
        a = 1.0 if highlight in (None, nm) else 0.25
        c.move_to(sx, y + 60 * s); c.curve_to(sx, y - 40 * s, ex, ey + 80 * s, ex, ey)
        rgb(c, col, a); c.set_line_width(26 * s); c.set_line_cap(cairo.LINE_CAP_ROUND); c.stroke()
        disk(c, ex, ey, 9 * s, (0.85, 0.6, 0.3), a)
        res[nm] = (ex, ey)
    return res

def breaker_panel(c, x, y, s=1.0, ons=(1, 1, 1), hl=None):
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -230, -230, 460, 460, 30, (0.24, 0.26, 0.31))
    rrect(c, -200, -170, 400, 300, 18, (0.15, 0.16, 0.19))
    for i, on in enumerate(ons):
        bx = -130 + i * 130
        rrect(c, bx - 45, -140, 90, 240, 14, (0.90, 0.89, 0.86))
        ly = lerp(30, -60, on)
        rrect(c, bx - 26, ly - 30, 52, 60, 12, YEL if hl == i else (0.25, 0.26, 0.3))
    c.restore()

def screwdriver(c, x, y, s=1.0, ang=0.0, glow=0.0):
    c.save(); c.translate(x, y); c.rotate(ang); c.scale(s, s)
    cap_line(c, 0, 0, 0, -170, (0.75, 0.77, 0.8), 14)
    rrect(c, -28, 0, 56, 150, 26, YEL if glow == 0 else (0.85, 0.88, 0.95))
    if glow > 0:
        disk(c, 0, 50, 46, RED, 0.35 * glow); disk(c, 0, 50, 20, RED, glow)
    c.restore()

def phone(c, x, y, s=1.0, flash=0.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -60, -110, 120, 220, 22, (0.08, 0.09, 0.11))
    rrect(c, -50, -96, 100, 180, 12, (0.2, 0.24, 0.32))
    if flash > 0:
        c.restore(); c.save(); c.translate(x, y)
        g = cairo.RadialGradient(0, 0, 0, 0, 0, 500 * s)
        g.add_color_stop_rgba(0, 1, 1, 1, 0.8 * flash); g.add_color_stop_rgba(1, 1, 1, 1, 0)
        c.set_source(g); c.arc(0, 0, 500 * s, 0, 2 * math.pi); c.fill()
    c.restore()

def check_mark(c, x, y, s=1.0, p=1.0, col=GRN):
    if p <= 0: return
    pts = [(x - 50 * s, y), (x - 15 * s, y + 38 * s), (x + 58 * s, y - 45 * s)]
    if p < 0.5: pts = [pts[0], (lerp(pts[0][0], pts[1][0], p * 2), lerp(pts[0][1], pts[1][1], p * 2))]
    else: pts = [pts[0], pts[1], (lerp(pts[1][0], pts[2][0], (p - .5) * 2), lerp(pts[1][1], pts[2][1], (p - .5) * 2))]
    poly(c, pts, col, 26 * s)

def x_mark(c, x, y, s=1.0, p=1.0, col=RED):
    r = 50 * s
    q1, q2 = clamp(p * 2), clamp(p * 2 - 1)
    if q1 > 0: cap_line(c, x - r, y - r, x - r + 2 * r * q1, y - r + 2 * r * q1, col, 26 * s)
    if q2 > 0: cap_line(c, x + r, y - r, x + r - 2 * r * q2, y - r + 2 * r * q2, col, 26 * s)

def spark(c, x, y, s, t, col=None):
    col = col or YEL
    rnd = random.Random(int(t * 14) + int(x))
    c.new_path()
    for i in range(16):
        ang = i * math.pi / 8 + rnd.uniform(-.15, .15); r = (52 if i % 2 == 0 else 18) * s * rnd.uniform(.7, 1.2)
        (c.move_to if i == 0 else c.line_to)(x + r * math.cos(ang), y + r * math.sin(ang))
    c.close_path(); rgb(c, col); c.fill()

def bolt(c, x1, y1, x2, y2, t, col=None, w=12):
    col = col or YEL
    rnd = random.Random(int(t * 16)); pts = [(x1, y1)]
    for i in range(1, 7):
        f = i / 7; nx, ny = -(y2 - y1), (x2 - x1); L = math.hypot(nx, ny) or 1; o = rnd.uniform(-30, 30)
        pts.append((lerp(x1, x2, f) + nx / L * o, lerp(y1, y2, f) + ny / L * o))
    pts.append((x2, y2)); poly(c, pts, col, w)

def ring(c, x, y, r, t, col=None):
    col = col or YEL
    p = (t * 1.6) % 1
    c.new_path(); c.arc(x, y, r * (0.6 + p * 0.8), 0, 2 * math.pi); rgb(c, col, 0.8 * (1 - p)); c.set_line_width(8); c.stroke()

def arrow(c, x1, y1, x2, y2, col=None, w=16, p=1.0):
    col = col or YEL
    x2, y2 = lerp(x1, x2, p), lerp(y1, y2, p); cap_line(c, x1, y1, x2, y2, col, w)
    if p > .1:
        a = math.atan2(y2 - y1, x2 - x1); hd = 40
        poly(c, [(x2 - hd * math.cos(a - .5), y2 - hd * math.sin(a - .5)), (x2, y2), (x2 - hd * math.cos(a + .5), y2 - hd * math.sin(a + .5))], col, w)

def plane(c, x, y, s=1.0, col=None):
    col = col or YEL
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-120, 10); c.line_to(130, -90); c.line_to(40, 110); c.line_to(10, 40); c.close_path(); rgb(c, col); c.fill()
    c.move_to(10, 40); c.line_to(130, -90); c.line_to(-10, 55); rgb(c, (0.75, 0.55, 0.05)); c.fill()
    c.restore()

class Cam:
    """zoom/tremida de câmera aplicados ao cenário"""
    def __init__(self, c, t, punch=0.05, shake=0.0, cx=W / 2, cy=1250):
        self.c, self.t, self.punch, self.shake, self.cx, self.cy = c, t, punch, shake, cx, cy
    def __enter__(self):
        c = self.c; c.save()
        z = 1 + self.punch * (1 - ease_out(prog(self.t, 0, 0.35)))
        dx = dy = 0
        if self.shake > 0:
            rnd = random.Random(int(self.t * 40)); dx, dy = rnd.uniform(-1, 1) * self.shake, rnd.uniform(-1, 1) * self.shake
        c.translate(self.cx + dx, self.cy + dy); c.scale(z, z); c.translate(-self.cx, -self.cy)
    def __exit__(self, *a): self.c.restore()

# ------------------------------------------------------------ chuveiro / DR / extras
COPPER = (0.90, 0.52, 0.22)

def resistor(c, x, y, s=1.0, broken=False, glow=0.0, t=0.0, a=1.0):
    """resistência em espiral (vista de frente), com rompimento opcional"""
    c.save(); c.translate(x, y); c.scale(s, s)
    col = mix(COPPER, (1.0, 0.35, 0.15), glow)
    n = 9; w = 300
    for i in range(n):
        x0 = -w / 2 + i * w / n
        if broken and i == 5: continue
        c.new_path(); c.save(); c.translate(x0 + w / n / 2, 0); c.scale(1, 2.2)
        c.arc(0, 0, w / n / 2 - 2, 0, 2 * math.pi); c.restore()
        rgb(c, col, a); c.set_line_width(9); c.stroke()
    if broken:
        bx = -w / 2 + 5 * w / n
        cap_line(c, bx - 4, -30, bx + 10, -48, col, 9, a); cap_line(c, bx + w / n + 4, 30, bx + w / n - 10, 48, col, 9, a)
    cap_line(c, -w / 2 - 40, 0, -w / 2, 0, (0.75, 0.75, 0.78), 12, a); cap_line(c, w / 2, 0, w / 2 + 40, 0, (0.75, 0.75, 0.78), 12, a)
    c.restore()

def shower(c, x, y, s=1.0, open_=0.0, water=0.0, steam=0.0, t=0.0, heat=0.0, coil=None):
    """chuveiro elétrico (corpo + espalhador que desenrosca). (x,y) = centro do corpo"""
    c.save(); c.translate(x, y); c.scale(s, s)
    # cano + cabos
    cap_line(c, 0, -170, 0, -420, (0.55, 0.57, 0.62), 34)
    cap_line(c, -40, -150, -120, -420, (0.15, 0.15, 0.17), 18); cap_line(c, 40, -150, 120, -420, (0.15, 0.15, 0.17), 18)
    body = mix((0.94, 0.93, 0.90), (1.0, 0.7, 0.55), heat)
    rrect(c, -150, -190, 300, 200, 60, body)
    rrect(c, -120, -30, 240, 30, 10, (0.82, 0.81, 0.78))
    dy = 260 * ease(open_)
    if open_ > 0 and coil is not None:
        coil(c, 0, 60 + dy * 0.3)
    # espalhador
    c.save(); c.translate(0, dy); c.rotate(open_ * 0.3)
    c.new_path(); c.move_to(-170, 0); c.curve_to(-170, 90, 170, 90, 170, 0); c.close_path(); rgb(c, (0.88, 0.87, 0.84)); c.fill()
    rrect(c, -175, -14, 350, 28, 14, (0.94, 0.93, 0.90))
    c.restore()
    if water > 0 and open_ == 0:
        for i in range(9):
            px = -120 + i * 30
            for k in range(4):
                ph = (t * 2.2 + k / 4 + i * 0.11) % 1
                cap_line(c, px * (1 + ph * 0.6), 90 + ph * 700, px * (1 + ph * 0.6), 120 + ph * 700, BLU, 8, water * (1 - ph * 0.3))
    c.restore()
    if steam > 0:
        for i in range(6):
            ph = (t * 0.5 + i / 6) % 1
            disk(c, x + math.sin(ph * 7 + i) * 120 * s, y + 500 * s - ph * 500 * s, (40 + 70 * ph) * s, (1, 1, 1), 0.18 * steam * (1 - ph))

def snowflake(c, x, y, r, a=1.0, col=BLU):
    for i in range(3):
        ang = i * math.pi / 3
        cap_line(c, x - r * math.cos(ang), y - r * math.sin(ang), x + r * math.cos(ang), y + r * math.sin(ang), col, r * 0.18, a)

def pizza(c, x, y, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.new_path(); c.move_to(0, 120); c.line_to(-110, -90); c.curve_to(-50, -125, 50, -125, 110, -90); c.close_path(); rgb(c, (0.98, 0.78, 0.35)); c.fill()
    c.new_path(); c.move_to(-110, -90); c.curve_to(-50, -125, 50, -125, 110, -90); rgb(c, (0.8, 0.5, 0.2)); c.set_line_width(24); c.stroke()
    for px, py in [(-30, -40), (35, -30), (0, 30)]: disk(c, px, py, 18, RED)
    c.restore()

def dr_flat(c, x, y, s=1.0, on=1.0, press=0.0, hl_t=False, stuck=False):
    """DR no estilo flat: 2 alavancas + botão T amarelo"""
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -150, -200, 300, 400, 26, (0.92, 0.91, 0.88))
    draw_text(c, "DR", -110, -125, 60, (0.15, 0.15, 0.17), "Anton")
    bs = 1 - 0.18 * press
    if hl_t: disk(c, 70, -150, 62, YEL, 0.25)
    rrect(c, 70 - 34 * bs, -150 - 34 * bs, 68 * bs, 68 * bs, 14, YEL)
    draw_text(c, "T", 70, -150 + 18, 48, (0.15, 0.15, 0.17), "Anton", align="center")
    rrect(c, -110, -60, 220, 210, 18, (0.20, 0.21, 0.25))
    ly = lerp(90, -10, on)
    rrect(c, -90, ly - 34, 180, 68, 16, mix(GREY, BLU, on))
    if stuck:
        for i in range(5):
            disk(c, -80 + i * 40, ly + 40 + (i % 2) * 14, 14, (0.6, 0.45, 0.3), 0.8)
    c.restore()

def finger(c, x, y, s=1.0, col=L_FRONT):
    """dedo/braço vindo de baixo apertando em (x,y)"""
    cap_line(c, x + 60 * s, y + 420 * s, x, y + 30 * s, col, 56 * s)
    disk(c, x, y + 30 * s, 30 * s, L_BODY)


# ------------------------------------------------------------ academia
def barbell(c, x, y, s=1.0, plates=2, col=None):
    col = col or YEL
    c.save(); c.translate(x, y); c.scale(s, s)
    cap_line(c, -330, 0, 330, 0, (0.75, 0.76, 0.8), 18)
    for side in (-1, 1):
        for i in range(plates):
            px = side * (215 + i * 34)
            rrect(c, px - 14, -95 + i * 6, 28, 190 - i * 12, 10, col if i % 2 == 0 else (0.85, 0.6, 0.08))
    c.restore()

def bed(c, x, y, s=1.0, t=0.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -380, -40, 760, 120, 30, (0.24, 0.26, 0.31))
    rrect(c, -360, -120, 180, 90, 40, (0.85, 0.85, 0.82))
    disk(c, -250, -150, 68, L_BODY)
    rrect(c, -200, -130, 560, 110, 50, (0.35, 0.45, 0.65))
    cap_line(c, -380, 80, -380, 160, (0.24, 0.26, 0.31), 30); cap_line(c, 380, 80, 380, 160, (0.24, 0.26, 0.31), 30)
    for i in range(3):
        ph = (t * 0.6 + i / 3) % 1
        draw_text(c, "Z", -180 + ph * 160, -230 - ph * 220, 50 + ph * 40, WHITE, "Anton", 1 - ph)
    c.restore()

def phone_screen(c, x, y, s=1.0, lines=(), title="", glow=0.0, logo=None):
    c.save(); c.translate(x, y); c.scale(s, s)
    if glow > 0: disk(c, 0, 0, 380, YEL, 0.12 * glow)
    rrect(c, -190, -340, 380, 680, 50, (0.07, 0.08, 0.1))
    rrect(c, -170, -310, 340, 620, 34, (0.13, 0.14, 0.17))
    if logo:
        label(c, logo, 0, 40, YEL, 150)
    if title: draw_text(c, title, -140, -230, 34, GREY, "Space Mono", spacing=4)
    for i, (txt, col) in enumerate(lines):
        rrect(c, -145, -190 + i * 110, 290, 86, 18, (0.2, 0.22, 0.26))
        draw_text(c, txt, -120, -132 + i * 110, 44, col, "Anton")
    c.restore()

def chart_up(c, x, y, w, h, p, col=None):
    col = col or YEL
    pts = [(0, 0.15), (0.2, 0.25), (0.4, 0.32), (0.6, 0.48), (0.8, 0.62), (1.0, 0.85)]
    n = max(2, int(len(pts) * p + 0.999))
    xy = [(x + px * w, y + h - py * h) for px, py in pts[:n]]
    cap_line(c, x, y + h, x + w, y + h, (1, 1, 1), 4, 0.25)
    poly(c, xy, col, 14)
    for px, py in xy: disk(c, px, py, 14, col)

# ------------------------------------------------------------ marcas
CORAL = (1.0, 0.302, 0.18); LILAC = (0.788, 0.722, 1.0)

def set_theme(name):
    """'brio' troca o amarelo de destaque pelo coral do BRIO (o resto da estética fica igual)"""
    global YEL
    if name == "brio":
        YEL = CORAL

def brio_mark(c, x, y, s=1.0, trail=True, t=0.0):
    """halter inclinado do logo do BRIO (coral) com 2 rastros lilás"""
    def dumbbell(dx, dy, col, a):
        c.save(); c.translate(dx, dy); c.translate(110, 55); c.rotate(math.radians(-18)); c.translate(-110, -55)
        disk(c, 70, 55, 26, col, a); disk(c, 150, 55, 26, col, a); rrect(c, 70, 44, 80, 22, 11, col, a); c.restore()
    c.save(); c.translate(x, y); c.scale(s, s); c.translate(-110, -55)
    if trail:
        wob = math.sin(t * 6) * 3
        dumbbell(-36 + wob, 30, LILAC, 0.18); dumbbell(-18 + wob / 2, 15, LILAC, 0.4)
    dumbbell(0, 0, CORAL, 1.0)
    c.restore()

def brio_wordmark(c, x, y, size, col=LILAC, align="center"):
    c.select_font_face("Unbounded", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); c.set_font_size(size)
    ext = c.text_extents("brio"); xx = x - ext.x_advance / 2 if align == "center" else x
    c.move_to(xx, y); rgb(c, col); c.show_text("brio")
    return ext.x_advance

def fioterra_mark(c, cx, cy, s=1.0, bg=None, fg=(0.07, 0.075, 0.09)):
    bg = bg or (0.98, 0.73, 0.10)
    c.save(); c.translate(cx, cy); c.scale(s, s)
    rrect(c, -200, -200, 400, 400, 96, bg)
    cap_line(c, 6, -158, 6, -120, fg, 30)
    pts = [(30, -132), (-40, -24), (2, -24), (-26, 46), (52, -60), (10, -60), (40, -132)]
    c.move_to(*pts[0])
    for p in pts[1:]: c.line_to(*p)
    c.close_path(); rgb(c, fg); c.fill()
    for i, w in enumerate((128, 86, 44)): cap_line(c, -w, 62 + i * 42, w, 62 + i * 42, fg, 30)
    c.restore()

def watermark(c, brand):
    if brand == "fioterra":
        font(c, "Anton", 36); tw = c.text_extents("FIO TERRA").x_advance
        x0 = W - 50 - tw
        fioterra_mark(c, x0 - 34, 112, 0.12); draw_text(c, "FIO TERRA", x0, 126, 36, WHITE, "Anton", 0.85)
    elif brand == "brio":
        c.select_font_face("Unbounded", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); c.set_font_size(38)
        x0 = W - 50 - c.text_extents("brio").x_advance
        brio_mark(c, x0 - 62, 110, 0.45, trail=False); brio_wordmark(c, x0, 126, 38, LILAC, align="left")
