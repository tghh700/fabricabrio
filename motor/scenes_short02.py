"""Só o helper chip() do SHORT 02 (usado pelos lotes BRIO)."""
from engine2 import *


def chip(c, s, x, y, bg, fg=WHITE, size=66, t=None, start=0.0):
    p = 1.0 if t is None else back_out(prog(t, start, 0.3))
    if p <= 0: return
    font(c, "Anton", size); w = c.text_extents(s).x_advance + 70
    c.save(); c.translate(x, y); c.scale(max(p, .001), max(p, .001))
    rrect(c, -w / 2, -size * 0.85, w, size * 1.55, 28, bg); label(c, s, 0, size * 0.42, fg, size); c.restore()
