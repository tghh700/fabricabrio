from cenas_1511 import *
import roteiro_brio_46_musica as R
BEAT_CTA = R.BEATS[-1]

def curl_music(c, t, x=HX, s=0.95, spd=2.6, heavy=False):
    u = 0.5 - 0.5 * math.cos(t * spd)
    p = pose_mix("curl_down", "curl_up", u)
    hx, hy = chunky(c, x, FLOOR_Y, s, p)
    dumbbell(c, hx, hy, s * (1.25 if heavy else 1.0), 0.0)
    h = head_pos(x, s, p); headphones(c, h[0], h[1], s)

def hook(c, t, d):
    curl_music(c, t)
    notes_float(c, t, 700, 1300)
    draw_text(c, "?", 860, 1560, 220 * (1 + 0.06 * math.sin(t * 5)), YEL, "Anton", 1.0, align="center")

def estudos(c, t, d):
    curl_music(c, t)
    n = int(min(24, t * 14))
    for i in range(24):
        x = 590 + (i % 6) * 72; y = 960 + (i // 6) * 92
        rrect(c, x - 26, y - 34, 52, 68, 8, YEL if i < n else CARD)
    counter(c, t, 770, 1500, 0, 139, "{:.0f}", 110, YEL, 0.2, 1.8, " ESTUDOS")

def esforco(c, t, d):
    curl_music(c, t, heavy=True)
    battery(c, 780, 1150, lerp(0.35, 0.65, ease(prog(t, 0.3, d * 0.6))), "FÔLEGO", 170, 300)
    notes_float(c, t, 920, 1200, 2, BLU)

def gosta(c, t, d):
    curl_music(c, t, spd=3.4, heavy=True)
    for i in range(7):  # equalizador
        h = 60 + 220 * abs(math.sin(t * 4 + i * 0.9))
        rrect(c, 600 + i * 62, 1450 - h, 44, h, 10, YEL if i % 2 else GRN)
    draw_text(c, "SÉRIE PESADA", 790, 1540, 50, GREY, "Anton", 1.0, align="center")

def playlist(c, t, d):
    act_walk(c, t, HX, 0.95)
    stack_list(c, t, ("MÚSICA 1", "MÚSICA 2", "MÚSICA 3"), 790, 1000, 440, 160, int(t * 1.5) % 3)
    draw_text(c, "PRONTA ANTES", 790, 1480, 56, GRN, "Anton", back_out(prog(t, 1.0, 0.3)), align="center")

def pequena(c, t, d):
    def L(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: curl_music(c, t, x, 1.0))
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0, heavy=True))
    split(c, t, L, Rr, "MÚSICA: POUCO", "CARGA: MUITO", BLU, GRN)

VIS = {"hook": scene(hook, "FONE DÁ FORÇA?", YEL), "estudos": scene(estudos, "MAIS DE 100 ESTUDOS", YEL),
       "esforco": scene(esforco, "PARECE MAIS LEVE", GRN), "gosta": scene(gosta, "A QUE VOCÊ GOSTA", YEL),
       "playlist": scene(playlist, "PLAYLIST ANTES", GRN, bg=False), "pequena": scene(pequena, "NÃO FAZ MILAGRE", RED, bg=False)}
SFX = finish(R, VIS, ("MÚSICA AJUDA", "É TEMPERO", "CARGA É O PRATO"), "MÚSICA", "SUPINO RETO",
 [("SEMANA 1: 50 KG", WHITE), ("SEMANA 3: 52 KG", WHITE), ("SUBIU 2 KG", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
