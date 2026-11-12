import sys, subprocess, os
from PIL import Image
name = sys.argv[1]; src = f"out/roteiro_{name}.mp4"
d = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src]))
ts = [d * (i + 0.5) / 8 for i in range(8)]
os.makedirs("out/rev", exist_ok=True); ims = []
for i, t in enumerate(ts):
    p = f"out/rev/{name}_{i}.png"
    subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",f"{t:.2f}","-i",src,"-frames:v","1","-vf","scale=240:427",p], check=True)
    ims.append(Image.open(p))
sheet = Image.new("RGB", (240 * 8, 427)); [sheet.paste(im, (i * 240, 0)) for i, im in enumerate(ims)]
sheet.save(f"out/rev/{name}_sheet.png"); print(name, round(d, 1))
