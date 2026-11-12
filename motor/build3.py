"""Builder dos perfis novos (FIBRA, DIA UM) com tema plugável e área segura do Reels.
uso: python3 build3.py roteiro_fibra_p1 scenes_fibra_p1 [--stills] [--sem-audio]
O roteiro define BEATS, THEME ('fibra'|'diaum') e, opcionalmente, NARRATION = {'file': mp3, 'align': json}.
Sem narração, os tempos são estimados pelo número de caracteres (para quadros de conferência)."""
import sys, os, re, json, math, subprocess, importlib
import cairo
import engine2 as E
from build2 import ensure_sfx, music_bed, parse_at, SFXD

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
W, H, FPS = E.W, E.H, E.FPS
TAG = re.compile(r"\[[^\]]*\]\s*")


def limpa(s):
    return TAG.sub("", s).strip()


def duration(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip())


def plan(mod):
    beats = mod.BEATS
    nar = getattr(mod, "NARRATION", None)
    if nar and os.path.exists(os.path.join(HERE, nar["file"])):
        mp3 = os.path.join(HERE, nar["file"]); dur = duration(mp3)
        if nar.get("starts"):
            starts = nar["starts"]
        else:
            al = json.load(open(os.path.join(HERE, nar["align"])))
            st = al["character_start_times_seconds"]; chars = "".join(al["characters"])
            starts = []; pos = 0
            for b in beats:
                frag = b["text"].strip()[:12]
                k = chars.find(frag, pos)
                k = pos if k < 0 else k
                starts.append(st[min(k, len(st) - 1)]); pos = k + 1
        tl = []
        for i, b in enumerate(beats):
            s = 0.0 if i == 0 else max(0.0, starts[i] - 0.08)
            e = (starts[i + 1] - 0.08) if i + 1 < len(beats) else dur + 0.5
            tl.append(dict(b=b, start=s, dur=e - s))
        return tl, dur + 0.5, mp3
    tl = []; t0 = 0.0
    for b in beats:
        d = len(limpa(b["text"])) / 17.0 + 0.15
        tl.append(dict(b=b, start=t0, dur=d)); t0 += d
    return tl, t0 + 0.4, None


def main():
    mod = importlib.import_module(sys.argv[1]); sc = importlib.import_module(sys.argv[2]); name = sys.argv[1]
    T_ = importlib.import_module("tema_" + mod.THEME)
    os.makedirs(OUT, exist_ok=True); ensure_sfx()
    tl, total, mp3 = plan(mod)
    print(f"duração: {total:.1f}s", "(estimada, sem narração)" if not mp3 else "")
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); c = cairo.Context(surf)

    def draw(it, T):
        b = it["b"]; t = T - it["start"]; d = it["dur"]
        T_.background(c, T)
        sc.VIS[b["vis"]](c, t, d, b)
        if mod.THEME == "fibra":
            T_.headline(c, t, b.get("t1", ""), b.get("t2", ""), b.get("fig"))
        else:
            T_.headline(c, t, b.get("t1", ""), b.get("t2", ""))

    if "--stills" in sys.argv:
        sd = os.path.join(OUT, name + "_stills"); os.makedirs(sd, exist_ok=True)
        for i, it in enumerate(tl):
            for f in (0.35, 0.85):
                draw(it, it["start"] + it["dur"] * f); surf.write_to_png(os.path.join(sd, f"{i:02d}_{int(f * 100)}.png"))
        print("stills ok:", sd); return

    inputs, filt, labels = [], [], []; k = 0
    if mp3:
        inputs += ["-i", mp3]; filt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=mono[a{k}]"); labels.append(f"[a{k}]"); k += 1
    for it in tl:
        for at, kind in sc.SFX.get(it["b"]["vis"], []):
            tt = it["start"] + parse_at(at, it["dur"])
            inputs += ["-i", os.path.join(SFXD, kind + ".wav")]
            filt.append(f"[{k}:a]volume=0.5,adelay={int(tt * 1000)}[a{k}]"); labels.append(f"[a{k}]"); k += 1
    bed = os.path.join(OUT, name + "_bed.wav"); music_bed(total, bed, bpm=getattr(mod, "BPM", 118))
    inputs += ["-i", bed]; filt.append(f"[{k}:a]volume={getattr(mod, 'BED_VOL', 0.8)}[a{k}]"); labels.append(f"[a{k}]"); k += 1
    audio = os.path.join(OUT, name + "_audio.m4a")
    fc = ";".join(filt) + ";" + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0,apad=whole_dur={total:.3f},loudnorm=I=-14:TP=-1.0:LRA=9[out]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", fc, "-map", "[out]", "-ar", "44100", "-ac", "2",
                    "-t", f"{total:.3f}", "-c:a", "aac", "-b:a", "192k", audio], check=True)
    video = os.path.join(OUT, name + ".mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                           "-c:a", "copy", "-shortest", "-movflags", "+faststart", video], stdin=subprocess.PIPE)
    n = int(math.ceil(total * FPS)); j = 0
    for f in range(n):
        T = f / FPS
        while j + 1 < len(tl) and T >= tl[j + 1]["start"]:
            j += 1
        draw(tl[j], T); surf.flush(); ff.stdin.write(bytes(surf.get_data()))
    ff.stdin.close(); ff.wait(); print("ok:", video)


if __name__ == "__main__":
    main()
