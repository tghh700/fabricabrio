"""Kit da cadeia "erro → consequência → volta" do BRIO (lote 22/11, BRIO 83–85).
- chain_vis(): monta o VIS de um roteiro de cadeia: entrada com wipe_in, ◀◀ (rewind_in) em todo beat "Então..." (vis f*),
  e por cima (coordenadas reais da tela) a trilha de ciclos (chips erro → certo), o rótulo da etapa (SE VOCÊ / ENTÃO / MAS SE / AÍ SIM)
  e a legenda de UMA palavra por vez no centro-baixo, com a palavra-chave do ciclo em destaque.
- peças: barra com carga, gráfico, cronômetro, relógio, medidor de esforço, peças do resumo.
Sem glifos fora da fonte: ◀◀ e marcas são desenhados (rewind_marks, check_mark, x_mark)."""
import math, re, unicodedata
from cenas_v2 import *

# ------------------------------------------------------------------ peças
def barbell_load(c, t, x, y, kg, col=None, s=1.0, plates=1):
    cap_line(c, x - 260 * s, y, x + 260 * s, y, STEEL, 14 * s)
    for sd in (-1, 1):
        for k in range(plates):
            rrect(c, x + sd * (200 + 34 * k) * s - 18 * s, y - (90 - 8 * k) * s, 36 * s, (180 - 16 * k) * s, 10 * s, (0.3, 0.32, 0.38))
    if kg is not None:
        tag(c, x, y - 150 * s, f"{kg} KG", col or CARD, WHITE if col in (None, RED, CARD) else INK, 54, 1.0)


def graph(c, t, x, y, w, h, pts, col, t0=0.2, dur=1.4, label_=None):
    cap_line(c, x, y + h, x + w, y + h, (1, 1, 1), 4, 0.25)
    cap_line(c, x, y, x, y + h, (1, 1, 1), 4, 0.25)
    p = ease_out(prog(t, t0, dur)); n = max(2, int(len(pts) * p + 0.999))
    xy = [(x + px * w, y + h - py * h) for px, py in pts[:n]]
    poly(c, xy, col, 12)
    for px, py in xy:
        disk(c, px, py, 12, col)
    if label_:
        draw_text(c, label_, x + w / 2, y + h + 50, 30, GREY, "Space Mono", 1.0, align="center", spacing=2)


def timer(c, t, x, y, r, frac, txt, col, p=1.0):
    """cronômetro: anel que enche até frac (0..1) e o texto no meio"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); s = max(back_out(p), .001); c.scale(s, s)
    rrect(c, -22, -r - 44, 44, 30, 8, CARD)
    disk(c, 0, 0, r + 16, CARD)
    c.new_path(); c.arc(0, 0, r - 8, -math.pi / 2, -math.pi / 2 + 2 * math.pi * clamp(frac)); rgb(c, col); c.set_line_width(26); c.stroke()
    draw_text(c, txt, 0, r * 0.22, r * 0.62, WHITE, "Anton", 1.0, align="center")
    c.restore()


def clock(c, t, x, y, r, minutes, col, p=1.0, label_=None):
    """relógio: ponteiro dos minutos dá voltas conforme 'minutes'"""
    if p <= 0:
        return
    c.save(); c.translate(x, y); s = max(back_out(p), .001); c.scale(s, s)
    disk(c, 0, 0, r + 14, col); disk(c, 0, 0, r, CARD)
    for i in range(12):
        a = i * math.pi / 6
        cap_line(c, (r - 28) * math.cos(a), (r - 28) * math.sin(a), (r - 12) * math.cos(a), (r - 12) * math.sin(a), GREY, 6)
    a = -math.pi / 2 + 2 * math.pi * (minutes / 60.0)
    cap_line(c, 0, 0, (r - 40) * math.cos(a), (r - 40) * math.sin(a), WHITE, 12)
    ah = -math.pi / 2 + 2 * math.pi * (minutes / 720.0)
    cap_line(c, 0, 0, (r - 80) * math.cos(ah), (r - 80) * math.sin(ah), WHITE, 16)
    disk(c, 0, 0, 14, WHITE)
    c.restore()
    if label_:
        tag(c, x, y + r + 70, label_, col, WHITE if col == RED else INK, 50, p)


def effort(c, t, x, y, v, p=1.0, h=360, label_="ESFORÇO"):
    """medidor vertical de esforço; v 0..1 (verde no alto = perto da falha)"""
    if p <= 0:
        return
    rrect(c, x - 44, y - h, 88, h, 30, CARD, p)
    hh = (h - 20) * clamp(v)
    rrect(c, x - 32, y - 10 - hh, 64, hh, 22, mix(RED, GRN, clamp((v - 0.3) / 0.6)), p)
    draw_text(c, label_, x, y + 46, 28, GREY, "Space Mono", p, align="center", spacing=2)


def pieces(c, t, x, y, labels, t0=0.2, step=0.4, w=250):
    """resumo: peças verdes caindo no lugar, a última em destaque"""
    n = len(labels)
    for i, s in enumerate(labels):
        p = back_out(prog(t, t0 + i * step, 0.35))
        bx = x + (i - (n - 1) / 2) * (w + 20)
        rrect(c, bx - w / 2, y - 80, w, 160, 26, CARD)
        if p > 0:
            col = YEL if i == n - 1 else GRN
            c.save(); c.translate(bx, y + (1 - min(p, 1)) * -260)
            rrect(c, -w / 2 + 8, -72, w - 16, 144, 22, col)
            check_mark(c, 0, -14, 0.42, prog(t, t0 + i * step + 0.25, 0.2), INK)
            c.restore()
            draw_text(c, s, bx, y + 132, 40, WHITE, "Anton", min(p, 1), align="center")


def shake(c, t, t0, amp=14):
    """tremida da consequência (chame antes de desenhar a cena)"""
    k = prog(t, t0, 0.05) * (1 - prog(t, t0 + 0.05, 0.45))
    if k > 0:
        c.translate(amp * k * math.sin(t * 90), amp * 0.6 * k * math.cos(t * 77))


def red_flash(c, t, t0):
    k = prog(t, t0, 0.04) * (1 - prog(t, t0 + 0.04, 0.35))
    if k > 0:
        c.save(); c.identity_matrix(); rgb(c, RED, 0.16 * k); c.paint(); c.restore()


# ------------------------------------------------------------------ cadeia
STEP = {"e": ("SE VOCÊ", RED), "m": ("MAS SE", RED), "f": ("ENTÃO", GRN), "conc": ("AÍ SIM", YEL)}


def _norm(w):
    w = unicodedata.normalize("NFD", w.upper())
    return "".join(ch for ch in w if unicodedata.category(ch) != "Mn")


def words_from_alignment(al, mapa):
    """[(t0, t1, palavra)] no tempo do áudio apertado; tira [marcas], troca Bríu por BRIO"""
    chars = al["characters"]; st = al["character_start_times_seconds"]; en = al["character_end_times_seconds"]
    out, cur, i0, inside = [], "", None, False
    for i, ch in enumerate(chars + [" "]):
        if ch == "[":
            inside = True; continue
        if inside:
            if ch == "]":
                inside = False
            continue
        if ch.isalnum() or ch in "-'":
            if not cur:
                i0 = i
            cur += ch
        elif cur:
            out.append((round(mapa(st[i0]), 3), round(mapa(en[i - 1]), 3), cur)); cur = ""
    fixed = []
    for a, b, w in out:
        if re.fullmatch(r"br[íi]u", w, re.I):
            w = "Brio"
        fixed.append((a, b, w))
    return fixed


def caption(c, T, words, hot_words, y=1505):
    """(22/11) substituída pela legenda.py desenhada pelo build2s — mantida só para os vídeos já publicados"""
    if True:
        return
    cur = None
    for i, (a, b, w) in enumerate(words):
        nxt = words[i + 1][0] if i + 1 < len(words) else b + 0.6
        end = nxt if nxt - b < 0.45 else b + 0.25
        if a - 0.03 <= T < end:
            cur = (a, w); break
    if not cur:
        return
    a, w = cur
    up = w.upper()
    hot = any(_norm(w) == kw and t0 - 0.1 <= a < t1 for t0, t1, kw in hot_words)
    p = back_out(prog(T, a - 0.03, 0.12))
    size = 132 if len(up) <= 8 else max(84, int(132 * 8 / len(up)))
    c.save(); c.identity_matrix(); c.translate(540, y - size * 0.3); s = 0.75 + 0.25 * min(p, 1.15); c.scale(s, s)
    for dx, dy in ((-5, 0), (5, 0), (0, -5), (0, 6), (4, 6), (-4, 6)):
        draw_text(c, up, dx, size * 0.3 + dy, size, (0.05, 0.05, 0.06), "Anton", 0.9, align="center")
    draw_text(c, up, 0, size * 0.3, size, YEL if hot else WHITE, "Anton", 1.0, align="center")
    c.restore()


def trail(c, t, cycles, state, p=1.0):
    """chips no topo: um por ciclo. state[i] = 0 escondido, 1 erro (vermelho), 2 certo (verde)"""
    n = len(cycles); w = 280; gap = 24; x0 = 540 - (n * w + (n - 1) * gap) / 2
    for i, (bad, good) in enumerate(cycles):
        s = state[i]
        if s == 0:
            continue
        cx = x0 + i * (w + gap) + w / 2; y = 400
        col = RED if s == 1 else GRN
        rrect(c, cx - w / 2, y - 48, w, 96, 30, col, p)
        txt = bad if s == 1 else good
        draw_text(c, txt, cx + 26, y + 20, 50 if len(txt) <= 7 else 40, WHITE if s == 1 else INK, "Anton", p, align="center")
        if s == 1:
            x_mark(c, cx - w / 2 + 40, y, 0.26, p, WHITE)
        else:
            check_mark(c, cx - w / 2 + 40, y, 0.28, p, INK)


def step_label(c, t, kind, p):
    txt, col = STEP[kind]
    draw_text(c, txt, 540, 660 + (1 - p) * 40, 130, col, "Anton", p, align="center")
    if kind == "f":
        rewind_marks(c, 540 - 270, 615, 1.0, p * 0.9)


def chain_vis(R, scenes, cycles, hot_words, hook_title):
    """R = módulo do roteiro (BEATS, NARRATION, WORDS); scenes = {vis: fn(c, t, d)}; cycles = [(erro, certo), ...]"""
    st = R.NARRATION["starts"]
    starts = [0.0 if i == 0 else max(0.0, s - 0.08) for i, s in enumerate(st)]
    durs = [(starts[i + 1] if i + 1 < len(starts) else 99) - starts[i] for i in range(len(starts))]
    names = [b["vis"] for b in R.BEATS]
    hot = [(starts[i], starts[i] + durs[i], _norm(b["k"])) for i, b in enumerate(R.BEATS) if b["vis"] != "cta"]
    VIS = {}

    def base(fn):
        def f(c, t, d, b):
            gym(c, t)
            fn(c, t, d)
        return f

    for i, nm in enumerate(names):
        if nm == "cta":
            continue
        inner = wipe_in(base(scenes[nm]), slide=120)
        if nm.startswith("f") and i > 0:
            inner = rewind_in(inner, _RAW[names[i - 1]], prev_dur=durs[i - 1], dur=0.55)
        _RAW[nm] = inner

        def make(inner=inner, i=i, nm=nm):
            def f(c, t, d, b):
                inner(c, t, d, b)
                T = starts[i] + t
                # sobreposições em coordenadas reais
                c.save(); c.identity_matrix()
                # estado da trilha
                state = []
                for k in range(len(cycles)):
                    ie = names.index(f"e{k + 1}") if f"e{k + 1}" in names else 99
                    jf = names.index(f"f{k + 1}") if f"f{k + 1}" in names else 99
                    state.append(2 if i >= jf else 1 if i >= ie else 0)
                if nm == "e1":
                    pass  # título no topo (headline do builder)
                else:
                    pt = 1.0 if not nm.startswith("f") else prog(t, 0.55, 0.2)
                    trail(c, t, cycles, state, pt)
                    kind = "conc" if nm == "conc" else ("f" if nm.startswith("f") else "m")
                    step_label(c, t, kind, ease_out(prog(t, 0.6 if kind == "f" else 0.05, 0.25)))
                c.restore()
                caption(c, T, R.WORDS, hot)
            return f
        VIS[nm] = make()
    return VIS


_RAW = {}


def chain_sfx(R, VIS, cons_at=0.45):
    out = {}
    for b in R.BEATS:
        nm = b["vis"]
        if nm == "cta":
            continue
        if nm == "e1":
            out[nm] = [(0.0, "boom"), (f"{cons_at}d", "buzz")]
        elif nm.startswith("e"):
            out[nm] = [(0.0, "whoosh"), (f"{cons_at}d", "buzz")]
        elif nm.startswith("f"):
            out[nm] = [(0.0, "zip"), (0.6, "pop"), ("0.6d", "ding")]
        else:
            out[nm] = [(0.0, "whoosh"), (0.3, "tick"), ("0.3d", "tick"), ("0.5d", "ding")]
    return out
