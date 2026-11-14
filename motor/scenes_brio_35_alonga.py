"""BRIO 35 — alongamento parado antes do treino."""
from cenas_1411 import *
import roteiro_brio_35_alonga as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("reach", [W(p_q, 700, 940), W(p_dumb, 700, 1260, 1.4)], "ALONGAR ANTES?", YEL, INK, punch=0.12),
 "forca": scene("reach", [W(p_gauge, "FORÇA", 1.0, 0.8, 700, 980, 80, 480, RED), W(p_arrow, 870, 760, 870, 1020, RED)], "PARADO TIRA FORÇA", RED, WHITE),
 "minuto": scene("reach", [W(p_clock, 700, 940, 210, 1.6), W(p_big, "> 60 S", 700, 1300, 120, RED)], "MAIS DE 1 MINUTO", RED, WHITE),
 "antes": scene("walk1", [W(p_dumb, 700, 960, 1.5), W(p_ok, 880, 740, 1.0, 0.6)], "ANTES: MOVIMENTO LEVE", GRN, INK),
 "depois": scene("reach_low", [W(p_clock, 700, 940, 190, 0.5), W(p_big, "DEPOIS", 700, 1290, 120, YEL)], "DEPOIS: ALONGA", BLU, INK),
 "proibido": scene("shrug", [W(p_ok, 700, 980, 1.8)], "NÃO É PROIBIDO", YEL, INK),
}
SFX = finish(R, VIS, ("MOVIMENTO ANTES", "ALONGA DEPOIS", "1 MIN NO MÁXIMO"), "ALONGA", "SEU AQUECIMENTO",
 [("AQUEC. 40 KG × 10", WHITE), ("SÉRIE 80 KG × 8", WHITE), ("TUDO REGISTRADO ✓", None)], ("REGISTRE AQUECIMENTO", "E SÉRIES NO BRIO"))
