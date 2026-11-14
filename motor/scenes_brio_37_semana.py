"""BRIO 37 — treinar uma vez por semana."""
from cenas_1411 import *
import roteiro_brio_37_semana as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("idle", [W(p_cal, 7, 1, 1, 700, 980, 80, None, YEL), W(p_q, 700, 1230, YEL)], "SÓ 1 VEZ POR SEMANA?", YEL, INK, punch=0.12),
 "sim": scene("thumb", [W(p_cal, 7, 1, 1, 700, 960, 80, None, GRN), W(p_ok, 700, 1180, 1.4, 0.6)], "É MELHOR QUE ZERO", GRN, INK),
 "total": scene("flex", [W(p_bars, (0.4, 0.8, 1.0), ("1 DIA", "2 DIAS", "3 DIAS"), 700, 1240, 400, 460, (YEL, YEL, YEL)), W(p_big, "SÉRIES NA SEMANA", 700, 650, 56, GREY)], "O TOTAL DE SÉRIES", YEL, INK),
 "cansa": scene("tired", [W(p_gauge, "QUALIDADE", 1.0, 0.25, 700, 1000, 90, 500, RED, 0.2, 2.2)], "TUDO NUM DIA CANSA", RED, WHITE),
 "dois": scene("walk1", [W(p_cal, 7, 1, 2, 700, 980, 80, None, GRN)], "SE DER: 2 DIAS", GRN, INK),
 "corpo": scene("flex", [W(p_list, ("AGACHAMENTO", "SUPINO", "REMADA"), 700, 800, 470, 160, -1)], "1 DIA: CORPO TODO", YEL, INK, fs=0.8),
}
SFX = finish(R, VIS, ("1 DIA > NENHUM", "2 DIAS É MELHOR", "NÃO FICA PARADO"), "SEMANA", "SUA SEMANA",
 [("SÁBADO: 12 SÉRIES", WHITE), ("SEMANA: 12 SÉRIES", WHITE), ("EVOLUÇÃO ✓", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
