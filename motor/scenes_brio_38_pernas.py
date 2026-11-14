"""BRIO 38 — treinar perna toda semana."""
from cenas_1411 import *
import roteiro_brio_38_pernas as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("shrug", [W(p_q, 700, 1000)], "PULOU A PERNA?", RED, WHITE, punch=0.12),
 "maior": scene("flex", [W(p_bars, (1.0, 0.6, 0.45, 0.3), ("PERNA", "COSTAS", "PEITO", "BRAÇO"), 700, 1240, 430, 480, (YEL, BLU, BLU, BLU))], "PERNA: O MAIOR GRUPO", YEL, INK),
 "desp": scene("flex", [W(p_bars, (0.9, 0.9, 0.3), ("TRONCO", "BRAÇOS", "PERNAS"), 700, 1240, 400, 480, (BLU, BLU, RED))], "PERNA ATRASADA", RED, WHITE),
 "ajuda": scene("thumb", [W(p_list, ("AGACHAMENTO", "TERRA", "ESCADA"), 700, 950, 470, 160, -1)], "PERNA FORTE AJUDA", GRN, INK),
 "curto": scene("idle", [W(p_list, ("2 EXERCÍCIOS", "3 SÉRIES CADA"), 700, 1000, 470, 160, 0), W(p_clock, 700, 1380, 110, 0.6)], "NÃO PRECISA SER LONGO", YEL, INK),
 "leve": scene("walk1", [W(p_dumb, 700, 1000, 1.5), W(p_arrow, 700, 1250, 700, 1130, GRN)], "COMEÇA LEVE", GRN, INK),
}
SFX = finish(R, VIS, ("PERNA ENTRA NA SEMANA", "POUCOS EXERCÍCIOS", "BEM FEITOS"), "PERNAS", "SEU TREINO DE PERNA",
 [("AGACHAMENTO 3 × 10", WHITE), ("LEG PRESS 3 × 12", WHITE), ("EVOLUÇÃO ✓", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
