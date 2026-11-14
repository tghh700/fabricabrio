"""BRIO 36 — melhor horário para treinar."""
from cenas_1411 import *
import roteiro_brio_36_horario as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("idle", [W(p_sun, 760, 1000, 80), W(p_moon, 760, 1300, 80), W(p_q, 930, 1130, YEL)], "MANHÃ OU NOITE?", YEL, INK, punch=0.12),
 "estudos": scene("idle", [W(p_bars, (0.96, 0.98, 1.0, 0.98), ("7H", "12H", "17H", "21H"), 700, 1240, 430, 480, (BLU, BLU, YEL, BLU))], "A FORÇA VARIA", BLU, INK),
 "tarde": scene("flex", [W(p_sun, 700, 960, 100), W(p_big, "+ FORÇA", 700, 1300, 110, YEL)], "FIM DA TARDE: + FORÇA", YEL, INK),
 "pequena": scene("shrug", [W(p_bars, (0.96, 1.0), ("MANHÃ", "TARDE"), 700, 1240, 300, 480, (BLU, YEL))], "DIFERENÇA PEQUENA", GREY, WHITE),
 "repetir": scene("thumb", [W(p_cal, 7, 2, 14, 700, 980, 66, None, GRN)], "O QUE VOCÊ REPETE", GRN, INK),
 "escolhe": scene("point_up", [W(p_clock, 700, 940, 200, 0.5), W(p_big, "4 SEMANAS", 700, 1290, 100, YEL)], "ESCOLHE E MANTÉM", YEL, INK),
}
SFX = finish(R, VIS, ("PERFEITO NÃO EXISTE", "O QUE VOCÊ MANTÉM", "4 SEMANAS"), "HORA", "SEU HORÁRIO",
 [("SEG 18:00 ✓", WHITE), ("QUA 18:00 ✓", WHITE), ("SEXTA 18:00 ✓", None)], ("REGISTRE SEU TREINO", "NO BRIO"))
