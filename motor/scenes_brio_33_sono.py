"""BRIO 33 — sono e treino."""
from cenas_1411 import *
import roteiro_brio_33_sono as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("tired", [W(p_bed, 700, 1180, 0.8), W(p_moon, 760, 760, 70)], "DORMIU MAL?", RED, WHITE, punch=0.12),
 "forca": scene("tired", [W(p_dumb, 700, 820, 2.2), W(p_gauge, "FORÇA", 1.0, 0.55, 880, 1050, 70, 460, GRN), W(p_arrow, 700, 650, 700, 900, RED)], "FORÇA CAI", RED, WHITE),
 "repara": scene("flex", [W(p_bed, 700, 1220, 0.8), W(p_ok, 700, 800, 1.6, 0.8)], "SONO REPARA O MÚSCULO", BLU, INK),
 "meta": scene("idle", [W(p_clock, 700, 940, 200, 0.6), W(p_big, "7–9 H", 700, 1300, 130, YEL)], "META: 7 A 9 HORAS", YEL, INK),
 "horario": scene("idle", [W(p_cal, 7, 2, 14, 700, 980, 66, None, BLU)], "HORÁRIO FIXO", BLU, INK),
 "leve": scene("walk1", [W(p_dumb, 700, 980, 1.5), W(p_ok, 860, 760, 1.0, 0.7)], "DIA RUIM: TREINO LEVE", YEL, INK),
}
SFX = finish(R, VIS, ("SONO FAZ PARTE", "7 A 9 HORAS", "HORÁRIO FIXO"), "SONO", "SEU TREINO",
 [("AGACHAMENTO 80 KG", WHITE), ("SONO RUIM: 70 KG", WHITE), ("COMPARE AS SEMANAS", None)], ("REGISTRE SEU TREINO", "NO BRIO"))
