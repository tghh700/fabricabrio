#!/bin/bash
# Prepara a máquina para renderizar: pycairo, ffmpeg e fontes do motor.
set -e
cd "$(dirname "$0")"
command -v ffmpeg >/dev/null || (sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg) || apt-get install -y -qq ffmpeg
python3 -c "import cairo" 2>/dev/null || pip install --quiet --break-system-packages pycairo
mkdir -p ~/.fonts && cp fontes/*.ttf ~/.fonts/ && fc-cache -f >/dev/null 2>&1 || true
mkdir -p out audio
echo "motor pronto"
