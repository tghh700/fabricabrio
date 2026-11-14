from cenas_1511 import *
import roteiro_brio_40_maquina as R
BEAT_CTA = R.BEATS[-1]

def stack_cycle(t, spd=2.4): return 0.5 - 0.5 * math.cos(t * spd)

def hook(c, t, d):
    stack_machine(c, 760, 1640, 1.0, stack_cycle(t), hi=YEL)
    act_pose(c, t, "thumb", 330)
    icon_ok(c, 1010, 1000, 0.8, prog(t, 0.5, 0.3))

def mito(c, t, d):
    act_curl(c, t, HX, 0.95)
    p = back_out(prog(t, 0.3, 0.3))
    card(c, 770, 1100, 440, 220, CARD, p)
    draw_text(c, "SÓ BARRA", 770, 1090, 66, WHITE, "Anton", p, align="center")
    draw_text(c, "E HALTER?", 770, 1170, 66, WHITE, "Anton", p, align="center")
    tag(c, 770, 1360, "MITO", RED, WHITE, 90, back_out(prog(t, 1.0, 0.3)))

def estudo(c, t, d):
    def L(c, t, cx, by): stack_machine(c, cx, by, 0.5, stack_cycle(t), hi=YEL)
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    split(c, t, L, Rr, "MÁQUINA", "PESO LIVRE", YEL, BLU)
    for i, x in enumerate((290, 790)):
        rrect(c, x - 150, 1582, 300 * ease_out(prog(t, 0.9, 0.9)), 30, 12, GRN)

def vantagem(c, t, d):
    stack_machine(c, 330, 1640, 0.95, stack_cycle(t, 3.0), hi=YEL)
    battery(c, 790, 1120, lerp(1.0, 0.12, ease(prog(t, 0.2, d * 0.7))), "ESFORÇO", 170, 300)
    tag(c, 790, 1460, "COM SEGURANÇA", GRN, INK, 46, back_out(prog(t, 0.8, 0.3)))

def livre(c, t, d):
    act_curl(c, t, HX, 0.95)
    # prato de equilíbrio balançando
    a = 0.25 * math.sin(t * 2.2)
    cx, cy = 780, 1250
    c.save(); c.translate(cx, cy); c.rotate(a)
    cap_line(c, -200, 0, 200, 0, STEEL, 14); disk(c, -170, -40, 36, BLU); disk(c, 170, -40, 36, BLU)
    c.restore(); disk(c, cx, cy + 20, 20, YEL)
    draw_text(c, "EQUILÍBRIO", 780, 1450, 60, BLU, "Anton", back_out(prog(t, 0.4, 0.3)), align="center")

def ambos(c, t, d):
    def L(c, t, cx, by): stack_machine(c, cx, by, 0.5, stack_cycle(t), hi=YEL)
    def Rr(c, t, cx, by): mini(c, cx, by, 0.72, lambda x: act_curl(c, t, x, 1.0))
    split(c, t, L, Rr, "USA", "OS DOIS", GRN, GRN)

VIS = {"hook": scene(hook, "MÁQUINA FUNCIONA", GRN), "mito": scene(mito, "SÓ PESO LIVRE?", RED),
       "estudo": scene(estudo, "GANHO PARECIDO", GRN, bg=False), "vantagem": scene(vantagem, "PERTO DO LIMITE", YEL),
       "livre": scene(livre, "PESO LIVRE TAMBÉM", BLU), "ambos": scene(ambos, "TÉCNICA E PROGRESSO", GRN, bg=False)}
SFX = finish(R, VIS, ("MÁQUINA DÁ MÚSCULO", "PESO LIVRE TAMBÉM", "CARGA SUBINDO"), "MÁQUINA", "EXTENSORA",
 [("SEMANA 1: 40 KG", WHITE), ("SEMANA 4: 45 KG", WHITE), ("SUBIU 5 KG", None)], ("REGISTRE A CARGA", "NO BRIO"))
