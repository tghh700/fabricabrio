"""BRIO 34 — ordem dos exercícios."""
from cenas_1411 import *
import roteiro_brio_34_ordem as R
BEAT_CTA = R.BEATS[-1]
VIS = {
 "hook": scene("reach", [W(p_list, ("AGACHAMENTO", "SUPINO", "ROSCA"), 620, 1000, 400, 150, -1), W(p_q, 930, 1060, YEL)], "ORDEM IMPORTA?", YEL, INK, punch=0.12),
 "primeiro": scene("flex", [W(p_gauge, "ENERGIA", 1.0, 1.0, 860, 1050, 90, 500, GRN), W(p_big, "1º", 640, 1000, 220, YEL)], "O 1º RENDE MAIS", GRN, INK),
 "prior": scene("point_up", [W(p_list, ("O QUE IMPORTA", "O RESTO", "O RESTO"), 660, 950, 470, 160, 0)], "COMEÇA PELO PRIORITÁRIO", YEL, INK),
 "composto": scene("flex", [W(p_list, ("AGACHAMENTO", "SUPINO", "REMADA"), 660, 950, 470, 160, 0), W(p_big, "ISOLADOS DEPOIS", 660, 1480, 60, GREY)], "COMPOSTOS ANTES", YEL, INK, fs=0.8),
 "cansado": scene("tired", [W(p_gauge, "ENERGIA", 1.0, 0.2, 700, 1000, 90, 500, RED, 0.2, 2.2), W(p_arrow, 840, 800, 840, 1180, RED)], "CANSADO ERRA MAIS", RED, WHITE),
 "atrasado": scene("flex", [W(p_list, ("MÚSCULO ATRASADO", "O RESTO", "O RESTO"), 660, 950, 500, 160, 0)], "ATRASADO? VAI 1º", YEL, INK),
}
SFX = finish(R, VIS, ("O MELHOR VEM 1º", "COMPOSTOS ANTES", "ATRASADO PRIMEIRO"), "ORDEM", "SEU TREINO",
 [("1. AGACHAMENTO 90 KG", WHITE), ("2. SUPINO 60 KG", WHITE), ("3. ROSCA 14 KG", None)], ("ANOTE A CARGA DE CADA", "EXERCÍCIO NO BRIO"))
