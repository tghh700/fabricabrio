"""Portão 6: folha com 16 quadros do mp4 FINAL (4×4). uso: python3 folha16.py out/<x>.mp4"""
import subprocess, sys, json, os
from PIL import Image
f = sys.argv[1]
dur = float(json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_format", "-of", "json", f], capture_output=True, text=True).stdout)["format"]["duration"])
ims = []
for i in range(16):
    t = dur * (i + 0.5) / 16
    tmp = f"/tmp/_f16_{i}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", f, "-frames:v", "1", "-vf", "scale=270:480", tmp])
    ims.append(Image.open(tmp).convert("RGB"))
S = Image.new("RGB", (4 * 270, 4 * 480))
for i, im in enumerate(ims):
    S.paste(im, ((i % 4) * 270, (i // 4) * 480))
out = os.path.splitext(f)[0] + "_folha16.png"; S.save(out); print(out)
