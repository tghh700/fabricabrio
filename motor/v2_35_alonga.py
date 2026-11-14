from cenas_v2 import *
import roteiro_brio_35_alonga as R
BEAT_CTA = R.BEATS[-1]

def hook(c, t, d):
    act_pose(c, t, "shrug")
    band(c, t, 760, 1100, 0.5 + 0.5 * math.sin(t * 2.5))
    draw_text(c, "?", 760, 1500, 220 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", 1.0, align="center")

def forca(c, t, d):
    band(c, t, 540, 1000, 1.0)
    battery(c, 540, 1360, lerp(0.9, 0.6, ease(prog(t, 0.3, d * 0.6))), "FORÇA NA HORA", 170, 280)
    arrow(c, 720, 1260, 720, 1450, RED, 14, ease_out(prog(t, 0.5, 0.4)))

def minuto(c, t, d):
    clock(c, 330, 1250, 180, t, 3.0)
    v = lerp(0, 75, ease_out(prog(t, 0.15, d * 0.7)))
    draw_text(c, f"{v:.0f} S", 780, 1250, 150, RED if v > 60 else WHITE, "Anton", 1.0, align="center")
    draw_text(c, "LIMITE: 60 S", 780, 1380, 40, GREY, "Space Mono", 1.0, align="center", spacing=2)

def antes(c, t, d):
    act_squat(c, t, HX, 0.95, 2.8, 0.7)
    tag(c, 790, 1060, "PESO LEVE", GRN, INK, 54, back_out(prog(t, 0.3, 0.3)))
    tag(c, 790, 1220, "MESMO MOVIMENTO", CARD, WHITE, 46, back_out(prog(t, 0.6, 0.3)))
    icon_ok(c, 790, 1420, 1.0, prog(t, 0.9, 0.3))

def depois(c, t, d):
    split(c, t, lambda c, t, cx, by: mini(c, cx, by, 0.72, lambda x: act_squat(c, t, x, 1.0, 2.8, 0.7)),
                lambda c, t, cx, by: band(c, t, cx, by - 220, 0.8 + 0.2 * math.sin(t * 1.5), 300),
          "ANTES: MOVE", "DEPOIS: ALONGA", GRN, BLU)

def proibido(c, t, d):
    act_pose(c, t, "thumb")
    band(c, t, 760, 1050, 0.3 + 0.1 * math.sin(t * 2))
    icon_ok(c, 760, 1350, 1.4, prog(t, 0.3, 0.3))

VIS = {"hook": scene(hook, "ALONGAR ANTES?", YEL), "forca": scene(forca, "PARADO TIRA FORÇA", RED, bg=False),
       "minuto": scene(minuto, "MAIS DE 1 MINUTO", RED, bg=False), "antes": scene(antes, "ANTES: MOVIMENTO LEVE", GRN),
       "depois": scene(depois, "ALONGAMENTO NO FIM", BLU, bg=False), "proibido": scene(proibido, "NÃO É PROIBIDO", YEL)}
SFX = finish(R, VIS, ("MOVIMENTO ANTES", "ALONGA DEPOIS", "1 MIN NO MÁXIMO"), "ALONGA", "SEU AQUECIMENTO",
 [("AQUEC. 40 KG × 10", WHITE), ("SÉRIE 80 KG × 8", WHITE), ("TUDO REGISTRADO", None)], ("REGISTRE AQUECIMENTO", "E SÉRIES NO BRIO"))
