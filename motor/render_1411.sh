#!/bin/bash
cd "$(dirname "$0")"
for n in 32_dor 33_sono 34_ordem 35_alonga 36_horario 37_semana; do
  python3 build2s.py roteiro_brio_$n scenes_brio_$n > out/log_$n.txt 2>&1 && echo "ok $n" >> out/lote_status.txt || echo "ERRO $n" >> out/lote_status.txt
done
