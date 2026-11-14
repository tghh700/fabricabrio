"""BRIO 32 — dor no dia seguinte não mede treino."""
from cenas_1411 import *
import roteiro_brio_32_dor as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("tired", [W(p_q, PX, PY - 40), W(p_pain, 640, 1230, 4)], "DOR = TREINO BOM?", RED, WHITE, punch=0.12),
 "nova": scene("shock", [W(p_dumb, 700, 960, 2.2), W(p_arrow, 700, 640, 700, 820, YEL)], "EXERCÍCIO NOVO", YEL, INK),
 "veterano": scene("flex", [W(p_bars, (1.0, 0.7, 0.45, 0.25), ("ANO 1", "ANO 2", "ANO 3", "ANO 4"), 700, 1240, 430, 480, (RED, RED, YEL, GRN))], "DOR CAI COM O TEMPO", BLU, INK),
 "carga": scene("curl_up", [W(p_chart, 480, 700, 440, 420, 0.2, 1.6, GRN), W(p_dumb, 840, 640, 1.2)], "CARGA SOBE = CRESCE", GRN, INK),
 "semdor": scene("thumb", [W(p_ok, 700, 960, 2.2)], "SEM DOR, VALEU", GRN, INK),
 "forte": scene("tired", [W(p_warn, 700, 960, 1.4)], "DOR FORTE: PROFISSIONAL", RED, WHITE),
}
SFX = finish(R, VIS, ("DOR NÃO MEDE", "CARGA SOBE = CRESCEU", "SEMANA × SEMANA"), "DOR", "SUAS SÉRIES",
 [("SUPINO 60 KG × 8", WHITE), ("SEMANA PASSADA: 55", WHITE), ("+5 KG ✓", None)], ("REGISTRE SUAS SÉRIES", "NO BRIO"))
