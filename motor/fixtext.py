"""Troca o texto antigo "GRÁTIS PRA REGISTRAR" pelo novo, em 2 linhas (usar: from fixtext import draw_text depois de from engine2 import *)."""
import engine2 as _E
def draw_text(c, s, x, y, size, col, *a, **kw):
    if s == "GRÁTIS PRA REGISTRAR":
        sz = int(size * 0.86); kw2 = dict(kw); kw2['spacing'] = min(kw.get('spacing', 3), 2)
        _E.draw_text(c, "REGISTRE E ACOMPANHE SEUS", x, y - sz * 0.55, sz, col, *a, **kw2)
        return _E.draw_text(c, "TREINOS GRATUITAMENTE", x, y + sz * 0.75, sz, col, *a, **kw2)
    return _E.draw_text(c, s, x, y, size, col, *a, **kw)
