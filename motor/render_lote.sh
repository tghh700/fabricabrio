#!/bin/bash
cd "$(dirname "$0")"
for n in "$@"; do
  sc=scenes_brio_$n; ro=roteiro_brio_$n
  [ "$n" = "25v4" ] && sc=scenes_brio_25v4 && ro=roteiro_brio_25v4
  python3 build2s.py $ro $sc > out/log_$n.txt 2>&1 && echo "ok $n" >> out/lote_status.txt || echo "ERRO $n" >> out/lote_status.txt
done
