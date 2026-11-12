"""Builder vertical (Shorts/Reels/TikTok).
uso: python3 build2.py roteiro_short_01 scenes_short01 [--stills]"""
import sys, os, subprocess, importlib, math
import cairo
import engine2 as E
from tts import path_for, duration

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out"); SFXD = os.path.join(HERE, "sfx")
W, H, FPS = E.W, E.H, E.FPS
PAD = 0.12

SFX_DEF = {  # gerados com ffmpeg (sem arquivos externos)
    "whoosh": "anoisesrc=color=pink:d=0.32:a=0.6,highpass=f=600,lowpass=f=5000,afade=t=in:d=0.14,afade=t=out:st=0.14:d=0.18",
    "swish": "anoisesrc=color=white:d=0.25:a=0.35,bandpass=f=3000:w=2000,afade=t=in:d=0.08,afade=t=out:st=0.08:d=0.17",
    "pop": "aevalsrc='0.8*sin(2*PI*(300+1800*t)*t)*exp(-28*t)':d=0.14",
    "click": "aevalsrc='0.7*sin(2*PI*2400*t)*exp(-90*t)':d=0.05",
    "tick": "aevalsrc='0.5*sin(2*PI*3000*t)*exp(-120*t)':d=0.04",
    "clack": "anoisesrc=color=white:d=0.09:a=0.9,lowpass=f=2500,afade=t=out:d=0.09",
    "boom": "aevalsrc='0.9*sin(2*PI*(70-30*t)*t)*exp(-5*t)':d=0.7",
    "ding": "aevalsrc='0.45*sin(2*PI*1320*t)*exp(-6*t)+0.25*sin(2*PI*1980*t)*exp(-8*t)':d=0.7",
    "buzz": "aevalsrc='0.35*sgn(sin(2*PI*120*t))*exp(-2.5*t)':d=0.6,lowpass=f=1500",
    "shutter": "aevalsrc='0.7*sin(2*PI*2000*t)*exp(-80*t)+0.6*sin(2*PI*1500*(t-0.09))*exp(-80*(t-0.09))*gte(t,0.09)':d=0.2",
    "zip": "anoisesrc=color=brown:d=0.7:a=0.5,bandpass=f=900:w=500,tremolo=f=22:d=0.9,afade=t=out:st=0.5:d=0.2",
}

def ensure_sfx():
    os.makedirs(SFXD, exist_ok=True)
    for k, f in SFX_DEF.items():
        p = os.path.join(SFXD, k + ".wav")
        if not os.path.exists(p):
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f, "-ac", "1", "-ar", "44100", p], check=True)

def music_bed(total, path, bpm=124):
    """batida simples (kick + chimbal) bem baixa, pra dar ritmo"""
    beat = 60 / bpm
    expr = (f"0.55*sin(2*PI*(55+90*exp(-30*mod(t,{beat})))*mod(t,{beat}))*exp(-9*mod(t,{beat}))"
            f"+0.06*(random(0)*2-1)*exp(-60*mod(t+{beat/2},{beat}))")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"aevalsrc='{expr}':d={total:.2f}:s=44100",
                    "-af", "lowpass=f=6000,volume=0.22", "-ac", "1", path], check=True)

def plan(mod):
    nar = getattr(mod, "NARRATION", None)
    if nar:  # narração já montada (ex.: correção de uma frase) — não chama o ElevenLabs
        path = nar["file"] if os.path.isabs(nar["file"]) else os.path.join(HERE, nar["file"])
        dur = duration(path); st = nar["starts"]; tl = []
        for i, b in enumerate(mod.BEATS):
            s = 0.0 if i == 0 else max(0.0, st[i] - 0.08)
            e = (st[i + 1] - 0.08) if i + 1 < len(mod.BEATS) else dur + 0.5
            tl.append(dict(b=b, start=s, dur=e - s, audio=path if i == 0 else None))
        return tl, dur + 0.5
    if getattr(mod, "FULL", False):
        import tts
        mp3, starts, dur = tts.full(mod)
        tl = []
        for i, b in enumerate(mod.BEATS):
            s = 0.0 if i == 0 else max(0.0, starts[i] - 0.08)
            e = (starts[i + 1] - 0.08) if i + 1 < len(mod.BEATS) else dur + 0.5
            tl.append(dict(b=b, start=s, dur=e - s, audio=mp3 if i == 0 else None))
        return tl, dur + 0.5
    tl = []; t0 = 0.0
    settings = getattr(mod, "SETTINGS", None)
    for b in mod.BEATS:
        a = path_for(b["text"], mod.VOICE, settings)
        tempo = getattr(mod, "TEMPO", 1.0)
        if tempo != 1.0:  # desacelera/acelera o áudio já gerado, sem gastar crédito
            a2 = a.replace(".mp3", f"_t{tempo}.wav")
            if not os.path.exists(a2):
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a, "-af", f"atempo={tempo}", a2], check=True)
            a = a2
        ad = duration(a)
        d = ad + PAD
        tl.append(dict(b=b, start=t0, dur=d, audio=a)); t0 += d
    return tl, t0 + 0.4

def parse_at(v, d):
    if isinstance(v, (int, float)): return v
    s = v.replace("d", f"*{d}")
    return eval(s)

def draw(c, sc, it, T, total):
    b = it["b"]; t = T - it["start"]; d = it["dur"]
    E.background(c, T)
    sc.VIS[b["vis"]](c, t, d, b)
    E.headline(c, t, "", b.get("t1", ""), b.get("t2", ""))  # sem kicker (pedido do usuário, 09/11)
    if BRAND: E.watermark(c, BRAND)
    # barra de progresso fininha (retenção)
    E.rrect(c, 0, H - 14, W * (T / total), 14, 0, E.YEL, 0.9)

BRAND = None
def main():
    global BRAND
    mod = importlib.import_module(sys.argv[1])
    BRAND = getattr(mod, "BRAND", None)
    if getattr(mod, "THEME", None): E.set_theme(mod.THEME)
    sc = importlib.import_module(sys.argv[2]); name = sys.argv[1]
    os.makedirs(OUT, exist_ok=True); ensure_sfx()
    tl, total = plan(mod)
    print(f"duração: {total:.1f}s")
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); c = cairo.Context(surf)
    if "--stills" in sys.argv:
        sd = os.path.join(OUT, name + "_stills"); os.makedirs(sd, exist_ok=True)
        for i, it in enumerate(tl):
            for f in (0.35, 0.85):
                draw(c, sc, it, it["start"] + it["dur"] * f, total)
                surf.write_to_png(os.path.join(sd, f"{i:02d}_{int(f*100)}.png"))
        print("stills ok"); return
    # áudio: narração + efeitos + batida
    inputs, filt, labels = [], [], []
    k = 0
    for it in tl:
        if it["audio"]:
            inputs += ["-i", it["audio"]]; ms = int(it["start"] * 1000)
            filt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=mono,adelay={ms}[a{k}]"); labels.append(f"[a{k}]"); k += 1
        for at, kind in sc.SFX.get(it["b"]["vis"], []):
            tt = it["start"] + parse_at(at, it["dur"])
            inputs += ["-i", os.path.join(SFXD, kind + ".wav")]; ms = int(tt * 1000)
            filt.append(f"[{k}:a]volume=0.55,adelay={ms}[a{k}]"); labels.append(f"[a{k}]"); k += 1
    bed = os.path.join(OUT, name + "_bed.wav"); music_bed(total, bed)
    inputs += ["-i", bed]; filt.append(f"[{k}:a]volume=1.0[a{k}]"); labels.append(f"[a{k}]"); k += 1
    audio = os.path.join(OUT, name + "_audio.m4a")
    fc = ";".join(filt) + ";" + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0,apad=whole_dur={total:.3f},loudnorm=I=-12:TP=-1.0:LRA=9[out]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", fc, "-map", "[out]", "-ar", "44100", "-ac", "2", "-t", f"{total:.3f}", "-c:a", "aac", "-b:a", "192k", audio], check=True)
    video = os.path.join(OUT, name + ".mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p",
                           "-c:a", "copy", "-shortest", "-movflags", "+faststart", video], stdin=subprocess.PIPE)
    n = int(math.ceil(total * FPS)); j = 0
    for f in range(n):
        T = f / FPS
        while j + 1 < len(tl) and T >= tl[j + 1]["start"]: j += 1
        draw(c, sc, tl[j], T, total); surf.flush(); ff.stdin.write(bytes(surf.get_data()))
    ff.stdin.close(); ff.wait(); print("ok:", video)

if __name__ == "__main__":
    main()
