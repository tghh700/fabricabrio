"""Cena final padrão do BRIO: gatilho -> ponte com o app -> frase fixa + LINK NA BIO.
uso numa cena:  from cta_brio import cta_brio
    def cta(c, t, d, b): cta_brio(c, t, d, b, kind="bubble", text="DIA UM", app_title="SUPINO", app_lines=[...], app_big="62,5 KG")
kind: "bubble" (comentário digitando text), "poll" (text=("TIME A","TIME B")), "send" (text=nome do amigo), "save" (salvar), 
Tempos vêm de b["marks"] = {"ponte","fixa","link"} (segundos desde o início da narração da cena)."""
import math
from engine2 import *
from scenes_short02 import chip

INK = (0.1, 0.1, 0.1); PAPER = (0.93, 0.92, 0.89); CARD = (0.2, 0.22, 0.26)

def _bubble(c, x, y, w, h, a=1.0):
    rrect(c, x - w / 2, y - h / 2, w, h, 34, PAPER, a)
    c.move_to(x - w / 2 + 60, y + h / 2 - 2); c.line_to(x - w / 2 + 40, y + h / 2 + 50); c.line_to(x - w / 2 + 120, y + h / 2 - 2)
    c.close_path(); rgb(c, PAPER, a); c.fill()

def _avatar(c, x, y):
    disk(c, x, y, 46, (0.31, 0.33, 0.39)); disk(c, x, y - 15, 18, (0.6, 0.62, 0.66)); rrect(c, x - 28, y + 10, 56, 26, 13, (0.6, 0.62, 0.66))

def _scale_in(c, x, y, p):
    c.save(); c.translate(x, y); s = max(p, .001); c.scale(s, s); c.translate(-x, -y)

def _trigger(c, t, t_end, kind, text):
    p = back_out(prog(t, 0.05, 0.35))
    if kind == "poll":
        a, bb = text
        for i, (lab, col) in enumerate(((a, YEL), (bb, (0.31, 0.33, 0.39)))):
            pi = back_out(prog(t, 0.1 + i * 0.25, 0.35))
            if pi <= 0: continue
            y = 960 + i * 230
            _scale_in(c, 540, y, pi)
            rrect(c, 140, y - 90, 800, 180, 40, col)
            label(c, lab, 540, y + 30, INK if i == 0 else WHITE, 76)
            c.restore()
        label(c, "OU", 540, 1092, GREY, 50, a=prog(t, 0.6, 0.3))
        # barra de votos animada
        fill = ease(prog(t, 0.9, 1.4))
        rrect(c, 140, 1340, 800, 26, 13, (0.25, 0.27, 0.31))
        rrect(c, 140, 1340, 800 * 0.5 * fill + 1, 26, 13, YEL)
        chunky(c, 870, FLOOR_Y + 40, 0.6, "point_up" if int(t * 2) % 2 else "idle", face=-1)
        return
    if kind == "save":
        pb = back_out(prog(t, 0.1, 0.4)); bounce = 1 + 0.06 * math.sin(t * 7)
        _scale_in(c, 540, 1080, pb * bounce)
        x, y, w, h = 540, 1080, 220, 300
        c.move_to(x - w / 2, y - h / 2); c.line_to(x + w / 2, y - h / 2); c.line_to(x + w / 2, y + h / 2)
        c.line_to(x, y + h / 2 - 80); c.line_to(x - w / 2, y + h / 2); c.close_path()
        rgb(c, YEL if t > 0.8 else WHITE); c.fill()
        c.restore()
        if t > 0.8: ring(c, 540, 1080, 230, t, YEL)
        label(c, "SALVA", 540, 1420, WHITE, 90, a=prog(t, 0.5, 0.3))
        chunky(c, 230, FLOOR_Y + 40, 0.65, "thumb", face=1)
        return
    # bubble / send
    if p > 0:
        _scale_in(c, 600, 1010, p)
        _bubble(c, 600, 1010, 720, 230)
        _avatar(c, 320, 1010)
        txt = ("@" + text) if kind == "send" else text
        n = int(clamp((t - 0.35) * 16, 0, len(txt)))
        font(c, "Anton", 58)
        draw_text(c, txt[:n], 395, 1032, 58, INK, "Anton")
        if n < len(txt) and int(t * 3) % 2 == 0:
            xx = 405 + c.text_extents(txt[:n]).x_advance
            cap_line(c, xx, 990, xx, 1045, INK, 5)
        c.restore()
    if kind == "send" and t > 0.9:
        pa = ease_out(prog(t, 0.9, 0.8))
        plane(c, lerp(620, 900, pa), lerp(1250, 1150 - math.sin(pa * math.pi) * 80, pa), 1.0, YEL)
    chunky(c, 260 if kind != "send" else 300, FLOOR_Y + 40, 0.72, pose_mix("idle", "point_up", prog(t, 0.2, 0.3)), face=1)

def cta_brio(c, t, d, b, kind="bubble", text="", app_title="", app_lines=(), app_big=None, app_big_label="", chart=False, lines=("REGISTRE E ACOMPANHE SEUS", "TREINOS GRATUITAMENTE")):
    mk = b.get("marks", {}); off = 0.08
    t_app = mk.get("ponte", d * 0.4) + off; t_fix = mk.get("fixa", d * 0.6) + off
    with Cam(c, t, punch=0.10):
        if t < t_app:
            _trigger(c, t, t_app, kind, text)
        else:
            tt = t - t_app
            px, py = 540, 1180
            pp = back_out(prog(tt, 0.0, 0.35))
            _scale_in(c, px, py, pp)
            ring(c, px, py, 330, t, YEL)
            phone_screen(c, px, py, 1.0, glow=0.6 + 0.4 * math.sin(t * 5))
            brio_mark(c, px - 85, py - 245, 0.5, trail=True, t=t)
            brio_wordmark(c, px - 40, py - 228, 46, LILAC, align="left")
            p1 = ease_out(prog(tt, 0.2, 0.35))
            if p1 > 0 and app_title:
                draw_text(c, app_title, px - 125, py - 150, 24, GREY, "Space Mono", p1, spacing=2)
            for i, (ln, col) in enumerate(app_lines):
                pl = ease_out(prog(tt, 0.3 + i * 0.18, 0.3))
                if pl <= 0: continue
                y = py - 110 + i * 62
                rrect(c, px - 140, y - 24, 280, 52, 12, CARD, pl)
                draw_text(c, ln, px - 120, y + 14, 32, col or WHITE, "Anton", pl)
            if chart:
                chart_up(c, px - 130, py + 40, 260, 150, ease_out(prog(tt, 0.4, 1.0)), YEL)
            if app_big:
                p2 = back_out(prog(tt, 1.0, 0.35))
                if p2 > 0:
                    pul = 1 + 0.04 * math.sin(t * 8)
                    c.save(); c.translate(px, py + 150); s = max(p2 * pul, .001); c.scale(s, s)
                    rrect(c, -150, -85, 300, 170, 24, YEL)
                    if app_big_label: draw_text(c, app_big_label, 0, -30, 24, INK, "Space Mono", align="center", spacing=1)
                    label(c, app_big, 0, 55 if app_big_label else 30, INK, 76)
                    c.restore()
            c.restore()
            if t > t_fix:
                pf = prog(t, t_fix, 0.35)
                for i, ln in enumerate(lines[:2]):
                    draw_text(c, ln, 540, 1630 + i * 45, 34, WHITE, "Space Mono", pf, align="center", spacing=2)
                chip(c, "LINK NA BIO", 540, 1775, YEL, INK, 66, t=t, start=t_fix + 0.5)

def cta_sfx(b, kind="bubble"):
    mk = b.get("marks", {}); a = mk.get("ponte", 3) + 0.08; f = mk.get("fixa", 5) + 0.08
    base = [(0.0, "whoosh"), (0.05, "pop")]
    if kind in ("bubble", "send"): base += [(0.5, "tick"), (0.8, "tick"), (1.1, "tick")]
    if kind == "send": base += [(0.9, "swish")]
    if kind == "poll": base += [(0.1, "pop"), (0.35, "pop"), (0.9, "zip")]
    if kind == "save": base += [(0.8, "ding")]
    return base + [(a, "whoosh"), (a + 1.0, "ding"), (f + 0.5, "pop")]
