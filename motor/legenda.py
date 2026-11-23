"""Legenda falada (usuário, 22/11): frase curta de 1–3 palavras num cartão na faixa de baixo, com a palavra
que está sendo dita destacada na cor do perfil. Mesma linguagem visual dos cartões de cada perfil:
  BRIO  — cartão grafite arredondado (como os cartões de semana/carga), Anton, destaque coral.
  FIBRA — etiqueta de prancha técnica (azul-marinho, contorno ciano fino), Barlow Condensed, destaque ciano.
A faixa fica em y 1478–1566 (dentro da área segura do Reels); os builders encolhem a cena para caber acima dela.

Uso no builder: L = legenda.carregar(mod) → lista de frases; legenda.desenhar(c, T, L, perfil)."""
import json, os, re, unicodedata
import engine2 as E

HERE = os.path.dirname(os.path.abspath(__file__))
Y = 1528            # centro da faixa (1488–1568)
H_CARD = 80
MAXW = 860

ESTILO = {
    "brio": dict(font="Anton", size=54, up=True, fill=(0.105, 0.118, 0.141), fill_a=0.94, stroke=None, r=26,
                 txt=(0.96, 0.95, 0.92), dim=0.55, acc=(1.0, 0.302, 0.18), pad=34, gap=17),
    "fibra": dict(font="Barlow Condensed", size=60, up=True, fill=(0.027, 0.094, 0.180), fill_a=0.92,
                  stroke=(0.220, 0.882, 0.824), r=6, txt=(0.949, 0.969, 0.980), dim=0.55,
                  acc=(0.220, 0.882, 0.824), pad=30, gap=15),
}
ESTILO["diaum"] = ESTILO["brio"]


# ------------------------------------------------------------------ tempos das palavras
def _palavras_do_alinhamento(al, mapa):
    chars = al["characters"]; st = al["character_start_times_seconds"]; en = al["character_end_times_seconds"]
    out, cur, i0, dentro, pont = [], "", None, False, False
    for i, ch in enumerate(chars + [" "]):
        if ch == "[":
            dentro = True; continue
        if dentro:
            if ch == "]":
                dentro = False
            continue
        if ch.isalnum() or ch in "-'":
            if not cur:
                i0 = i
            cur += ch
        else:
            if cur:
                out.append([mapa(st[i0]), mapa(en[i - 1]), cur, False]); cur = ""
            if ch in ".,:;?!…" and out:
                out[-1][3] = True  # pontuação depois da palavra: quebra a frase aqui
    fix = []
    for a, b, w, p in out:
        if re.fullmatch(r"br[íi]u", w, re.I):
            w = "Brio"  # na tela é sempre Brio
        fix.append((round(a, 3), round(b, 3), w, p))
    return fix


def palavras(mod):
    """[(t0, t1, palavra, pontuação_depois)] no tempo do áudio apertado"""
    nar = mod.NARRATION
    base = os.path.basename(nar["file"]).replace("_tight.mp3", "").replace(".mp3", "")
    al = json.load(open(os.path.join(HERE, "audio", base + ".json")))
    orig = os.path.join(HERE, "audio", base + ".mp3")
    if nar["file"].endswith("_tight.mp3"):
        from apertar import apertar
        tight = os.path.join(HERE, nar["file"])
        # mesmos parâmetros da produção (gera_roteiros_*): BRIO pausas de até 0,45 s (23/11) sem acelerar; FIBRA padrão
        kw = getattr(mod, "APERTAR", None) or (dict(max_pausa=0.45, tempo=1.0) if getattr(mod, "THEME", "") == "brio" else {})
        _, mapa = apertar(orig, tight, **kw)
    else:
        mapa = lambda x: x
    return _palavras_do_alinhamento(al, mapa)


FUNC = set("a o e é de da do das dos em no na nos nas um uma uns umas se que pra pro com por os as ao mais sem".split())


def frases(ws, cortes=(), max_pal=3, max_chars=18):
    """agrupa em frases curtas: quebra em pontuação, pausa > 0,25 s, início de beat ou limite de tamanho;
    nunca termina frase em palavra de ligação ("de", "a", "se"…) e não deixa palavra órfã antes do ponto"""
    cortes = sorted(cortes); out, cur = [], []
    for a, b, w, p in ws:
        if cur:
            txt = " ".join(x[2] for x in cur) + " " + w
            novo_beat = any(cur[-1][1] < c_ <= a + 0.02 for c_ in cortes)
            if novo_beat or a - cur[-1][1] > 0.25:
                out.append(cur); cur = []
            elif len(cur) >= max_pal or len(txt) > max_chars:
                leva = []
                while len(cur) > 1 and cur[-1][2].lower() in FUNC:
                    leva.insert(0, cur.pop())
                out.append(cur); cur = leva
        cur.append((a, b, w, p))
        if p:
            if len(cur) == 1 and out and not out[-1][-1][3] and len(out[-1]) <= 3 \
                    and len(" ".join(x[2] for x in out[-1] + cur)) <= 22 and a - out[-1][-1][1] <= 0.25:
                out[-1] = out[-1] + cur
            else:
                out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def carregar(mod, cortes=()):
    return frases(palavras(mod), cortes)


# ------------------------------------------------------------------ desenho
def _ativa(T, L):
    for i, f in enumerate(L):
        a = f[0][0]; b = f[-1][1]
        nxt = L[i + 1][0][0] if i + 1 < len(L) else b + 0.6
        fim = nxt if nxt - b < 0.5 else b + 0.3
        if a - 0.06 <= T < fim:
            return f
    return None


def desenhar(c, T, L, perfil="brio", y=Y):
    f = _ativa(T, L)
    if not f:
        return
    S = ESTILO.get(perfil, ESTILO["brio"])
    c.save(); c.identity_matrix()
    E.font(c, S["font"], S["size"])
    txts = [(w.upper() if S["up"] else w) for _, _, w, _ in f]
    larg = [c.text_extents(t).x_advance for t in txts]
    size = S["size"]
    tot = sum(larg) + S["gap"] * (len(txts) - 1)
    if tot > MAXW - 2 * S["pad"]:
        k = (MAXW - 2 * S["pad"]) / tot; size = S["size"] * k; larg = [l * k for l in larg]; tot *= k
    w_card = tot + 2 * S["pad"]
    # entrada: sobe 14 px e cresce de 92% → 100% em 0,14 s
    p = E.back_out(E.prog(T, f[0][0] - 0.06, 0.14))
    sc = 0.92 + 0.08 * min(p, 1.08)
    c.translate(540, y + (1 - min(p, 1)) * 14); c.scale(sc, sc)
    a = min(1.0, p * 1.4)
    x0, y0 = -w_card / 2, -H_CARD / 2
    E.rrect(c, x0 + 4, y0 + 7, w_card, H_CARD, S["r"], (0, 0, 0), 0.35 * a)  # sombra curta
    E.rrect(c, x0, y0, w_card, H_CARD, S["r"], S["fill"], S["fill_a"] * a)
    if S["stroke"]:
        E.rgb(c, S["stroke"], 0.75 * a); c.set_line_width(3)
        c.rectangle(x0 + 1.5, y0 + 1.5, w_card - 3, H_CARD - 3); c.stroke()
        for cx, cy, dx, dy in ((x0, y0, 1, 1), (x0 + w_card, y0, -1, 1), (x0, y0 + H_CARD, 1, -1), (x0 + w_card, y0 + H_CARD, -1, -1)):
            E.rgb(c, S["stroke"], a); c.set_line_width(5)
            c.move_to(cx, cy + dy * 18); c.line_to(cx, cy); c.line_to(cx + dx * 18, cy); c.stroke()
    xx = -tot / 2; base = size * 0.36
    for (wa, wb, _, _), t_, l in zip(f, txts, larg):
        if T >= wa - 0.04 and T < wb + 0.08:
            col, aa = S["acc"], 1.0          # palavra sendo dita
        elif T >= wb:
            col, aa = S["txt"], 1.0          # já dita
        else:
            col, aa = S["txt"], S["dim"]     # ainda vai ser dita
        E.draw_text(c, t_, xx, base, size, col, S["font"], a * aa)
        xx += l + S["gap"]
    c.restore()
