"""BRIO 17 — amplitude alongada / parciais alongadas."""
import math
from engine2 import *
from lote_h import *
import roteiro_brio_17 as R
from cta_brio import cta_brio, cta_sfx
BEAT_CTA = R.BEATS[-1]

def track(c, x, y0, y1, u, zone=None, col=None, mcol=None, dim=None, w=36):
    """trilho vertical: u=0 topo, 1 base. zone=(a,b) em fração destacada"""
    col = col or YEL
    cap_line(c, x, y0, x, y1, (0.2, 0.22, 0.27), w)
    if zone:
        a, b_ = zone
        cap_line(c, x, lerp(y0, y1, a), x, lerp(y0, y1, b_), col, w - 8, 0.9)
    if dim:
        a, b_ = dim
        cap_line(c, x, lerp(y0, y1, a), x, lerp(y0, y1, b_), (0.12, 0.13, 0.16), w - 8, 0.8)
    disk(c, x, lerp(y0, y1, u), 36, mcol or WHITE)

def hook(c, t, d, b):
    with Cam(c, t, punch=0.12):
        u = 0.5 + 0.5 * math.sin(t * 3.2)
        h = chunky(c, 330, FLOOR_Y, 0.85, pose_mix("curl_down", "curl_up", u), face=1)
        dumbbell_h(c, h[0], h[1], 0.8)
        zp = 0.5 + 0.5 * math.sin(t * 6)
        track(c, 800, 920, 1620, 1 - u, zone=(0.5, 1.0), col=mix(YEL, RED, zp * 0.4), mcol=WHITE)
        draw_text(c, "CIMA", 900, 960, 30, GREY, "Space Mono", spacing=3)
        draw_text(c, "BAIXO", 900, 1620, 30, GREY, "Space Mono", spacing=3)
        tg(c, 760, 1760, "A PARTE QUE VOCÊ CORTA", YEL, INK, 46, back_out(prog(t, d * 0.45, 0.3)))
        pq = back_out(prog(t, 0.3, 0.3))
        pop_in(c, 640, 1330, pq); label(c, "?", 0, 40, YEL, 150); c.restore()

def half(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 * (0.5 + 0.5 * math.sin(t * 3.5))
        track(c, 230, 920, 1640, u, zone=(0, 0.5), col=GRN, dim=(0.5, 1.0))
        x_mark(c, 230, 1480, 0.7, prog(t, 0.4, 0.3))
        draw_text(c, "SÓ A METADE", 230, 880, 34, WHITE, "Anton", align="center")
        pb = back_out(prog(t, 0.3, 0.35))
        pop_in(c, 700, 1180, pb); barbell(c, 0, 0, 0.62, plates=3); c.restore()
        tg(c, 700, 1020, "MAIS PESO", YEL, INK, 56, back_out(prog(t, 0.6, 0.3)))
        tg(c, 700, 1400, "MAIS FÁCIL", GRN, INK, 52, back_out(prog(t, d * 0.55, 0.3)))
        ring(c, 230, 1100, 110, t, GRN)

def stretch(c, t, d, b):
    with Cam(c, t, punch=0.06):
        s = 0.5 + 0.5 * math.sin(t * 2.2)
        L = 520 + 160 * s; H = 200 - 50 * s
        cx, cy = 540, 1150
        for sd in (-1, 1):
            disk(c, cx + sd * (L / 2 + 40), cy, 30, (0.85, 0.84, 0.8))
            arrow(c, cx + sd * (L / 2 + 80), cy, cx + sd * (L / 2 + 190), cy, YEL, 12, p=s)
        c.save(); c.translate(cx, cy); c.scale(1, 1); rrect(c, -L / 2, -H / 2, L, H, H / 2, mix(RED, YEL, 0.35 * s)); c.restore()
        for i in range(-2, 3): cap_line(c, cx + i * L / 6, cy - H / 3, cx + i * L / 6, cy + H / 3, WHITE, 5, 0.35)
        draw_text(c, "ALONGADO", 540, 1010, 56, YEL, "Anton", prog(t, 0.3, 0.3), align="center")
        draw_text(c, "ESTUDOS RECENTES", 540, 880, 30, GREY, "Space Mono", align="center", spacing=4)
        base = 1740
        for x, h, col, lab, dl in ((330, 220, GREY, "CURTO", 0.4), (750, 400, GRN, "ALONGADO", d * 0.45)):
            pp = ease_out(prog(t, dl, 0.6))
            bar(c, x, base, 200, h, col, pp, 14); draw_text(c, lab, x, base + 50, 32, WHITE, "Anton", align="center")
        draw_text(c, "CRESCIMENTO", 540, 1330, 28, GREY, "Space Mono", align="center", spacing=4)

def where(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.5 + 0.5 * math.sin(t * 3)
        # painel 1: supino (lado)
        rrect(c, 70, 880, 940, 380, 30, (0.16, 0.18, 0.22))
        rrect(c, 130, 1170, 620, 26, 8, IRON)
        disk(c, 190, 1130, 40, L_BODY); rrect(c, 230, 1105, 380, 60, 28, L_BODY); cap_line(c, 600, 1135, 740, 1135, L_FRONT, 36)
        by = lerp(1115, 960, 1 - u)
        cap_line(c, 400, 1110, 440, by, L_FRONT, 26); disk(c, 440, by, 22, (0.75, 0.76, 0.8)); disk(c, 440, by, 60, YEL, 0.9)
        ring(c, 440, 1112, 90, t, YEL) if u < 0.2 else None
        tg(c, 800, 960, "SUPINO", CARD, WHITE, 40, 1.0)
        pp = back_out(prog(t, d * 0.2, 0.3))
        tg(c, 800, 1060, "BARRA NO PEITO", YEL, INK, 38, pp)
        # painel 2: rosca
        rrect(c, 70, 1300, 940, 450, 30, (0.16, 0.18, 0.22))
        h = chunky(c, 330, 1700, 0.5, pose_mix("curl_down", "curl_up", 1 - u * 0.85 if False else 0.5 - 0.5 * math.cos(t * 3)), face=1)
        dumbbell_h(c, h[0], h[1], 0.5)
        pr = prog(t, d * 0.5, 0.3)
        tg(c, 760, 1400, "ROSCA", CARD, WHITE, 40, 1.0)
        tg(c, 760, 1500, "BRAÇO QUASE ESTICADO", YEL, INK, 36, back_out(pr))
        ring(c, 760, 1620, 80, t, GRN)
        draw_text(c, "ALONGADO = EMBAIXO", 540, 1810 - 20, 34, WHITE, "Anton", prog(t, 0.2, 0.3), align="center")

def squat(c, t, d, b):
    with Cam(c, t, punch=0.06):
        per = 3.0
        u = 0.5 - 0.5 * math.cos((t % per) / per * 2 * math.pi)
        s = 0.85
        h = chunky(c, 400, FLOOR_Y, s, pose_mix("bar_back", "squat_deep", u), face=1)
        disk(c, h[0] - 30, h[1] - 20, 38, YEL); cap_line(c, h[0] - 200, h[1] - 20, h[0] + 140, h[1] - 20, (0.75, 0.76, 0.8), 12)
        arrow(c, 800, 960, 800, 1400, YEL, 18, p=prog(t, 0.3, 0.5))
        tg(c, 800, 900, "DESCE FUNDO", YEL, INK, 54, back_out(prog(t, 0.2, 0.3)))
        pg = back_out(prog(t, d * 0.45, 0.3))
        tg(c, 800, 1530, "GLÚTEO", RED, WHITE, 48, pg); tg(c, 800, 1640, "COXA", RED, WHITE, 48, back_out(prog(t, d * 0.55, 0.3)))
        ring(c, 400, FLOOR_Y - 300 * s, 140, t, RED)
        c.set_dash([20, 14]); cap_line(c, 100, FLOOR_Y - 190, 700, FLOOR_Y - 190, GRN, 5, 0.8); c.set_dash([])

def partial_(c, t, d, b):
    with Cam(c, t, punch=0.06):
        u = 0.62 + 0.3 * (0.5 + 0.5 * math.sin(t * 6))
        track(c, 220, 920, 1640, u, zone=(0.5, 1.0), col=YEL, dim=(0.0, 0.5))
        draw_text(c, "BAIXO", 220, 880, 32, YEL, "Anton", align="center")
        for i in range(8):
            pp = back_out(prog(t, 0.2 + i * 0.12, 0.25))
            pop_in(c, 440 + (i % 4) * 130, 1020 + (i // 4) * 120, pp); disk(c, 0, 0, 44, GRN); c.restore()
        draw_text(c, "REPS COMPLETAS", 640, 960, 30, GREY, "Space Mono", align="center", spacing=2)
        for i in range(3):
            pp = back_out(prog(t, d * 0.4 + i * 0.25, 0.25))
            if pp <= 0: continue
            pop_in(c, 500 + i * 130, 1370, pp)
            c.new_path(); c.arc(0, 0, 44, 0, math.pi); c.close_path(); rgb(c, YEL); c.fill(); c.restore()
        draw_text(c, "MEIAS REPS EMBAIXO", 560, 1470, 30, GREY, "Space Mono", align="center", spacing=1)
        chunky(c, 960, FLOOR_Y, 0.45, pose_mix("idle", "tired", prog(t, d * 0.3, 0.4)), face=-1)
        tg(c, 600, 1620, "FIM DA SÉRIE", YEL, INK, 54, back_out(prog(t, d * 0.55, 0.3)))

def control(c, t, d, b):
    with Cam(c, t, punch=0.06):
        per = 3.4
        ph = (t % per) / per
        u = ease(clamp(ph / 0.7)) if ph < 0.85 else 1 - ease(clamp((ph - 0.85) / 0.15))
        track(c, 230, 920, 1640, u, zone=(0.0, 1.0), col=GRN, mcol=WHITE)
        arrow(c, 340, 1000, 340, 1500, GRN, 14, p=prog(t, 0.2, 0.5))
        draw_text(c, "DEVAGAR", 360, 920, 48, GRN, "Anton")
        clock(c, 520, 1250, 70, t * 0.8, hour=3)
        draw_text(c, "3 SEG", 520, 1380, 44, WHITE, "Anton", align="center")
        # quicar errado
        bx = 800; q = abs(math.sin(t * 7))
        cap_line(c, bx, 960, bx, 1640, (0.2, 0.22, 0.27), 36)
        disk(c, bx, 1640 - 120 * q, 36, RED)
        x_mark(c, bx, 1300, 0.9, prog(t, d * 0.4, 0.3))
        draw_text(c, "QUICAR", bx, 920, 44, RED, "Anton", align="center")
        tg(c, 540, 1760, "CONTROLA EMBAIXO", YEL, INK, 54, back_out(prog(t, d * 0.55, 0.3)))

def weight(c, t, d, b):
    with Cam(c, t, punch=0.06):
        pl = ease(prog(t, d * 0.3, 0.6))
        barbell(c, 540, 1130, 0.9, plates=3)
        # anilha extra "sai"
        for sd in (-1, 1):
            px = 540 + sd * 0.9 * (215 + 2 * 34)
            if pl > 0:
                rrect(c, px - 14 + sd * pl * 160, 1130 - 95 + 12 + pl * 500, 28, 166, 10, (0.2, 0.22, 0.27), 1 - pl)
            rgb(c, (0.12, 0.13, 0.16)); 
        tg(c, 540, 900, "MENOS PESO", YEL, INK, 64, back_out(prog(t, 0.2, 0.3)))
        pe = back_out(prog(t, 0.5, 0.35))
        tg(c, 300, 1500, "EGO", RED, WHITE, 64, pe)
        arrow(c, 300, 1380, 300, 1470 - 0, RED, 12, p=1.0) if False else None
        arrow(c, 300, 1590, 300, 1700, RED, 14, p=pe)
        pm = back_out(prog(t, d * 0.5, 0.35))
        tg(c, 780, 1500, "MÚSCULO", GRN, INK, 64, pm)
        arrow(c, 780, 1700, 780, 1590, GRN, 14, p=pm)
        ring(c, 780, 1500, 130, t, GRN) if pm > 0.9 else None

def pain(c, t, d, b):
    with Cam(c, t, punch=0.06):
        chunky(c, 300, FLOOR_Y, 0.8, "squat_half", face=1)
        k = 0.5 + 0.5 * math.sin(t * 8)
        kx, ky = 300 + 95 * 0.8, FLOOR_Y - 200 * 0.8
        ring(c, kx, ky, 90, t, RED); disk(c, kx, ky, 30, RED, 0.3 + 0.4 * k)
        warn(c, 800, 1000, 1.3 * back_out(prog(t, 0.2, 0.3)) + .01, RED)
        tg(c, 800, 1180, "DOR NA ARTICULAÇÃO", RED, WHITE, 40, back_out(prog(t, 0.4, 0.3)))
        # amplitude diminui
        sh = ease(prog(t, d * 0.4, 0.6))
        cap_line(c, 800, 1280, 800, 1560, (0.2, 0.22, 0.27), 32)
        cap_line(c, 800, 1280, 800, lerp(1560, 1440, sh), GRN, 24)
        tg(c, 800, 1640, "DIMINUI A AMPLITUDE", YEL, INK, 38, back_out(prog(t, d * 0.45, 0.3)))
        tg(c, 540, 1770, "PROCURA UM PROFISSIONAL", WHITE, INK, 44, back_out(prog(t, d * 0.7, 0.3)))

def examples(c, t, d, b):
    with Cam(c, t, punch=0.06):
        cards = [("CADEIRA FLEXORA", "JOELHO BEM ESTICADO", 0.1), ("CRUCIFIXO", "BRAÇOS BEM ABERTOS", 0.9), ("SEMPRE", "A PARTE MAIS DIFÍCIL", 1.9)]
        for i, (a, b2, st) in enumerate(cards):
            y = 1020 + i * 250
            pp = back_out(prog(t, st, 0.35))
            if pp <= 0: continue
            pop_in(c, 540, y, pp)
            rrect(c, -470, -105, 940, 210, 30, (0.2, 0.22, 0.27))
            s = 0.5 + 0.5 * math.sin(t * 2.5)
            if i == 0:
                ang = lerp(80, 8, s) * math.pi / 180
                kx, ky = -330, -20
                cap_line(c, -400, -20, kx, ky, L_FRONT, 34)
                cap_line(c, kx, ky, kx + 90 * math.sin(ang) * 1.0 + 0, ky + 90 * math.cos(ang), L_FRONT, 34)
            elif i == 1:
                sp = lerp(30, 130, s)
                disk(c, -330, -10, 40, L_BODY)
                for sd in (-1, 1):
                    cap_line(c, -330, -10, -330 + sd * sp * 0.9, -10 - sp * 0.0 + 20, L_FRONT, 22)
                    disk(c, -330 + sd * sp * 0.9, 10, 22, IRON)
            else:
                flame(c, -330, 5, 0.6, YEL, t)
            draw_text(c, a, -200, -12, 52, WHITE, "Anton")
            draw_text(c, b2, -200, 52, 36, YEL, "Anton")
            c.restore()

def cta(c, t, d, b):
    cta_brio(c, t, d, b, kind="send", text="seuparceiro", app_title="CARGA DA SEMANA",
             app_lines=[("VOCÊ  62,5 KG", None), ("PARCEIRO  60 KG", None), ("SUBIU CARGA", GRN)], app_big="+2,5 KG", app_big_label="QUEM SOBE 1º")

VIS = {"hook": hook, "half": half, "stretch": stretch, "where": where, "squat": squat, "partial": partial_, "control": control,
       "weight": weight, "pain": pain, "examples": examples, "cta": cta}
SFX = {k: [(0.0, "whoosh"), (0.25, "pop"), ("0.5d", "pop")] for k in VIS}
SFX["hook"] = [(0.0, "boom"), (0.3, "pop"), ("0.45d", "pop")]
SFX["half"] += [("0.55d", "pop")]
SFX["pain"] += [(0.3, "buzz"), ("0.4d", "pop")]
SFX["weight"] += [("0.3d", "clack"), ("0.5d", "ding")]
SFX["examples"] += [(0.9, "pop"), (1.9, "pop")]
SFX["cta"] = cta_sfx(BEAT_CTA, "send")
