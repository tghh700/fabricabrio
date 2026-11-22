"""Gera a capa (JPEG 1080x1920) de um Reels a partir do próprio vídeo: escolhe, entre 1,2 s e 3,2 s,
o quadro mais nítido/claro (título já na tela, fora de transição). Uso: python3 capa.py video.mp4 [saida.jpg]"""
import subprocess, sys, os, tempfile
from PIL import Image, ImageStat, ImageFilter

def capa(mp4, out=None):
    out = out or mp4[:-4] + ".jpg"
    best, score = None, -1
    with tempfile.TemporaryDirectory() as d:
        for i, t in enumerate([1.2, 1.5, 1.8, 2.1, 2.4, 2.8, 3.2]):
            f = os.path.join(d, f"{i}.png")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", mp4, "-frames:v", "1", f], check=True)
            im = Image.open(f).convert("L")
            bright = ImageStat.Stat(im).mean[0]
            sharp = ImageStat.Stat(im.filter(ImageFilter.FIND_EDGES)).mean[0]
            s = bright + 3 * sharp
            if s > score:
                score, best = s, Image.open(f).convert("RGB")
    best.resize((1080, 1920)).save(out, "JPEG", quality=90)
    return out

if __name__ == "__main__":
    print(capa(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
