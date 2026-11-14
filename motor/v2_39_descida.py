from cenas_1511 import *
import roteiro_brio_39_descida as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_curl_tempo(c, t, HX, 0.95, down=0.18, up=0.8, heavy=True)
    u, ph = curl_cycle(t, 0.8, 0.18)
    if ph:
        draw_text(c, "TUM!", 760, 1500, 120, RED, "Anton", 1.0, align="center")
    icon_x(c, 780, 1100, 1.1, prog(t, 0.6, 0.3))

def metade(c, t, d):
    act_curl_tempo(c, t, HX, 0.95, down=1.2, up=0.8)
    for i, (txt, col) in enumerate((("SUBIDA", GRN), ("DESCIDA", YEL))):
        p = back_out(prog(t, 0.2 + i * 0.4, 0.3))
        card(c, 770, 1050 + i * 190, 420, 150, col if i == 1 else CARD, p)
        draw_text(c, txt, 770, 1050 + i * 190 + 24, 66, INK if i == 1 else col, "Anton", p, align="center")
    draw_text(c, "50%", 770, 1500, 110, YEL, "Anton", back_out(prog(t, 1.0, 0.3)), align="center")

def cai(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl_tempo(c, t, x, 1.0, down=0.18, up=0.8))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl_tempo(c, t, x, 1.0, down=1.6, up=0.8))
    split(c, t, L, Rr, "GRAVIDADE", "MÚSCULO", RED, GRN)

def tranco(c, t, d):
    hx, hy = act_curl_tempo(c, t, HX, 0.95, down=0.18, up=0.9, heavy=True)
    u, ph = curl_cycle(t, 0.9, 0.18)
    for k in range(6):  # ondas de impacto no cotovelo
        a = k * math.pi / 3
        r0 = 50 + 30 * ((t * 3) % 1)
        cap_line(c, HX + 60 + r0 * math.cos(a), FLOOR_Y - 400 + r0 * math.sin(a), HX + 60 + (r0 + 30) * math.cos(a), FLOOR_Y - 400 + (r0 + 30) * math.sin(a), RED, 8, 0.9 if ph or u < 0.05 else 0.25)
    tag(c, 800, 1150, "ARTICULAÇÃO", RED, WHITE, 52, back_out(prog(t, 0.4, 0.3)))

def conta(c, t, d):
    act_curl_tempo(c, t, HX, 0.95, down=2.0, up=0.7)
    u, ph = curl_cycle(t, 0.7, 2.0)
    T = 0.7 + 0.15 + 2.0 + 0.15; f = t % T
    sec = 0 if f < 0.85 else min(2, int((f - 0.85) / 1.0) + 1)
    draw_text(c, f"{sec} s", 780, 1250, 200, YEL if ph else GREY, "Anton", 1.0, align="center")
    draw_text(c, "DESCENDO" if ph else "SUBINDO", 780, 1400, 52, GRN, "Space Mono", 1.0, align="center", spacing=3)

def lento(c, t, d):
    act_curl_tempo(c, t, HX, 0.95, down=1.6, up=0.7)
    def gauge(x, txt, col, ok):
        p = back_out(prog(t, 0.2 + (0.5 if ok else 0), 0.3))
        card(c, x, 1150, 260, 260, CARD, p)
        draw_text(c, txt, x, 1180, 64, col, "Anton", p, align="center")
        (icon_ok if ok else icon_x)(c, x, 1360, 0.6, prog(t, 0.6 + (0.5 if ok else 0), 0.3))
    gauge(640, "10 s", RED, False); gauge(930, "2 s", GRN, True)

def peso(c, t, d):
    act_curl_tempo(c, t, HX, 0.95, down=0.25, up=1.1, heavy=True)
    counter(c, t, 780, 1100, 14, 10, "{:.0f}", 170, YEL, 0.6, 1.0, " KG")
    arrow(c, 780, 1260, 780, 1420, GRN, 16, ease_out(prog(t, 1.4, 0.4)))

VIS = {"hook": scene(hook, "DEIXA CAIR?", RED, bg=False), "metade": scene(metade, "METADE DA REPETIÇÃO", YEL),
       "cai": scene(cai, "QUEM TRABALHA?", YEL, bg=False), "tranco": scene(tranco, "O TRANCO", RED),
       "conta": scene(conta, "DESCE EM 2 SEGUNDOS", GRN), "lento": scene(lento, "CONTROLE, SEM EXAGERO", YEL, bg=False),
       "peso": scene(peso, "SEM CONTROLE? MENOS PESO", RED)}
SFX = finish(R, VIS, ("SOBE FIRME", "DESCE EM 2 SEGUNDOS", "SEMPRE CONTROLADO"), "DESCIDA", "ROSCA DIRETA",
 [("SÉRIE 1: 12 KG × 10", WHITE), ("SÉRIE 2: 12 KG × 9", WHITE), ("SUBIU 2 KG", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
