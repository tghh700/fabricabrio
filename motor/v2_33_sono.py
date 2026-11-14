from cenas_v2 import *
import roteiro_brio_33_sono as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    sleeper(c, t, 600, 1420, 0.95, restless=1.0)
    moon(c, t, 840, 1010, 75)
    counter(c, t, 330, 1060, 0, 4, size=120, col=RED, suffix=" H")

def forca(c, t, d):
    def L(c, t, cx, by):
        mini(c, cx - 60, by, 0.72, lambda x: act_curl(c, t * 0.6, x, 1.0))
        battery(c, cx + 160, by - 330, 0.3, None, 70, 150)
    def Rr(c, t, cx, by):
        mini(c, cx - 60, by, 0.72, lambda x: act_curl(c, t, x, 1.0, heavy=True))
        battery(c, cx + 160, by - 330, 0.9, None, 70, 150)
    split(c, t, L, Rr, "4 H DE SONO", "8 H DE SONO", RED, GRN)

def repara(c, t, d):
    sleeper(c, t, 560, 1500, 0.75)
    battery(c, 820, 1060, lerp(0.2, 1.0, ease(prog(t, 0.2, d * 0.7))), "RECUPERAÇÃO", 150, 260, GRN)
    for k in range(5):
        f = (t * 0.7 + k / 5) % 1
        x, y = 420 + 90 * k, 1360 - 260 * f
        cap_line(c, x - 16, y, x + 16, y, GRN, 8, 1 - f); cap_line(c, x, y - 16, x, y + 16, GRN, 8, 1 - f)

def meta(c, t, d):
    clock(c, 330, 1240, 170, t, 3.0)
    for i in range(9):
        p = back_out(prog(t, 0.2 + i * 0.12, 0.2))
        hot = i >= 6
        y = 1530 - i * 70
        card(c, 760, y, 300, 56, GRN if hot else CARD, p)
        draw_text(c, f"{i + 1} H", 760, y + 16, 38, INK if hot else GREY, "Anton", p, align="center")

def horario(c, t, d):
    for i, (fn, txt) in enumerate(((moon, "DEITA 23 H"), (sun, "ACORDA 7 H"))):
        x = 330 + i * 420
        fn(c, t, x, 1070, 70)
        tag(c, x, 1240, txt, CARD, WHITE, 46, back_out(prog(t, 0.3 + i * 0.3, 0.3)))
    week(c, t, 540, 1450, range(7), BLU, cell=100, t0=0.8)

def leve(c, t, d):
    act_curl(c, t, HX, 0.95, 2.0)
    battery(c, 760, 1150, 0.5, "ENERGIA", 150, 260)
    icon_ok(c, 760, 1480, 1.0, prog(t, 0.8, 0.3))

VIS = {"hook": scene(hook, "DORMIU MAL?", RED, bg=False), "forca": scene(forca, "FORÇA CAI", RED, bg=False),
       "repara": scene(repara, "DORMINDO, O MÚSCULO REPARA", BLU, bg=False), "meta": scene(meta, "META: 7 A 9 HORAS", GRN),
       "horario": scene(horario, "HORÁRIO FIXO", BLU, bg=False), "leve": scene(leve, "DIA RUIM: TREINO LEVE", YEL)}
SFX = finish(R, VIS, ("SONO FAZ PARTE", "7 A 9 HORAS", "HORÁRIO FIXO"), "SONO", "SEU TREINO",
 [("AGACHAMENTO 80 KG", WHITE), ("NOITE RUIM: 70 KG", WHITE), ("COMPARE AS SEMANAS", None)], ("REGISTRE SEU TREINO", "NO BRIO"))
