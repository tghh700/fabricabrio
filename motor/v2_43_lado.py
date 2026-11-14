from cenas_1511 import *
import roteiro_brio_43_lado as R
BEAT_CTA = R.BEATS[-1]

def lr_bars(c, t, x, y, a, b, t0=0.2, la="ESQ", lb="DIR"):
    for i, (v, lab, col) in enumerate(((a, la, RED if a < b else GRN), (b, lb, RED if b < a else GRN))):
        p = ease_out(prog(t, t0 + i * 0.2, 0.8))
        h = 380 * v * p
        bx = x - 110 + i * 220
        rrect(c, bx - 70, y - h, 140, h + 1, 18, col)
        draw_text(c, lab, bx, y + 56, 34, GREY, "Space Mono", 1.0, align="center")

def hook(c, t, d):
    act_curl(c, t, HX, 0.95)
    lr_bars(c, t, 780, 1500, 0.7, 1.0)

def normal(c, t, d):
    act_pose(c, t, "thumb")
    stack_list(c, t, ("ESCREVE COM UMA MÃO", "CHUTA COM UM PÉ", "UM LADO DOMINA"), 780, 1000, 520, 160, 2, num=False)

def barra(c, t, d):
    act_squat(c, t, HX, 0.95, 2.4)
    lr_bars(c, t, 780, 1500, 0.55, 1.0, 0.4, "FRACO", "FORTE")
    arrow(c, 900, 1250, 700, 1250, YEL, 14, ease_out(prog(t, 1.2, 0.4)))

def halter(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t + 1.2, x, 1.0))
    split(c, t, L, Rr, "ESQUERDO", "DIREITO", BLU, BLU)

def fraco(c, t, d):
    act_curl(c, t, HX, 0.95, 2.6)
    for i, (lab, n, col) in enumerate((("FRACO", 8, YEL), ("FORTE", 8, GRN))):
        p = back_out(prog(t, 0.3 + i * 0.7, 0.3))
        y = 1060 + i * 240
        if p <= 0.01: continue
        card(c, 780, y, 440, 200, CARD, p)
        draw_text(c, f"{i + 1}º {lab}", 780, y - 45, 42, GREY, "Anton", p, align="center")
        if p > 0.6:
            counter(c, t, 780, y + 28, 0, n, "{:.0f}", 90, col, 0.5 + i * 0.7, 0.8, " REP")

def tempo(c, t, d):
    act_curl(c, t, HX, 0.95)
    k = ease(prog(t, 0.3, d * 0.6))
    lr_bars(c, t, 780, 1420, lerp(0.6, 0.92, k), 1.0, 0.0)
    week(c, t, 780, 1600, (0, 2, 4), GRN, cell=60, labels=("S", "T", "Q", "Q", "S", "S", "D"))

VIS = {"hook": scene(hook, "UM LADO MAIS FORTE?", YEL), "normal": scene(normal, "É NORMAL", GRN),
       "barra": scene(barra, "NA BARRA, O FORTE AJUDA", RED), "halter": scene(halter, "CADA LADO SOZINHO", BLU, bg=False),
       "fraco": scene(fraco, "COMEÇA PELO FRACO", YEL), "tempo": scene(tempo, "A DIFERENÇA DIMINUI", GRN)}
SFX = finish(R, VIS, ("UM LADO POR VEZ", "FRACO PRIMEIRO", "MESMAS REPETIÇÕES"), "LADO", "ROSCA ALTERNADA",
 [("ESQUERDO: 10 KG × 8", WHITE), ("DIREITO: 10 KG × 8", WHITE), ("EMPATADO", None)], ("REGISTRE CADA LADO", "NO BRIO"))
