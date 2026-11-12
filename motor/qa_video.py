"""Portão 4 (arquivo) + folha de contato para o portão 6 (visual).
uso: python3 qa_video.py out/<arquivo>.mp4 [--starts 0,3.1,7.2,...]
Sai com código 1 se reprovar. Gera out/<nome>_folha.png (12 quadros) e out/<nome>_cortes.png (1 quadro por cena, 0,6 s depois do início)."""
import json, re, subprocess, sys, os


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True)


def main():
    f = sys.argv[1]; nome = os.path.splitext(os.path.basename(f))[0]; outd = os.path.dirname(f) or "."
    starts = []
    if "--starts" in sys.argv:
        starts = [float(x) for x in sys.argv[sys.argv.index("--starts") + 1].split(",")]
    info = json.loads(sh("ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", f).stdout)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"]
    dur = float(info["format"]["duration"])
    erros = []
    if (v["width"], v["height"]) != (1080, 1920): erros.append("resolução")
    if v["codec_name"] != "h264": erros.append("codec de vídeo")
    if not a or a[0]["codec_name"] != "aac": erros.append("sem áudio AAC")
    if not 15 <= dur <= 60: erros.append(f"duração {dur:.1f}s fora de 15–60")
    log = sh("ffmpeg", "-hide_banner", "-i", f, "-vf", "blackdetect=d=0.5:pix_th=0.05,freezedetect=n=0.001:d=3", "-af",
             "silencedetect=noise=-45dB:d=0.8,ebur128=peak=true", "-f", "null", "-").stderr
    if "black_start" in log: erros.append("tela preta")
    if "freeze_start" in log: erros.append("imagem congelada > 3 s")
    sil = re.findall(r"silence_start: ([0-9.]+)", log)
    sil = [float(s) for s in sil if float(s) < dur - 1.5]
    if sil: erros.append(f"buraco de áudio em {sil[:3]}")
    m = re.findall(r"I:\s+(-?[0-9.]+) LUFS", log)
    lufs = float(m[-1]) if m else None
    if lufs is not None and not -15.5 <= lufs <= -10: erros.append(f"volume {lufs} LUFS")
    pk = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", log)
    if pk and float(pk[-1]) > -0.5: erros.append(f"pico {pk[-1]} dBFS")
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", f, "-vf", f"fps=12/{dur},scale=270:480,tile=6x2", "-frames:v", "1", os.path.join(outd, nome + "_folha.png"))
    if starts:
        ins = []; fl = []
        for i, s in enumerate(starts):
            ins += ["-ss", f"{min(dur - 0.1, s + 0.6):.2f}", "-i", f]
            fl.append(f"[{i}:v]scale=270:480,trim=end_frame=1[v{i}]")
        fl.append("".join(f"[v{i}]" for i in range(len(starts))) + f"hstack=inputs={len(starts)}[o]" if len(starts) > 1 else "[v0]null[o]")
        sh("ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fl), "-map", "[o]", "-frames:v", "1", os.path.join(outd, nome + "_cortes.png"))
    print(json.dumps({"arquivo": f, "duracao": round(dur, 2), "lufs": lufs, "erros": erros}, ensure_ascii=False))
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
