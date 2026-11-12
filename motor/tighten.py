"""Deixa a narração mais fluida SEM gastar crédito: encurta pausas longas e acelera um pouco o gancho.
Gera audio_tight/<nome>.mp3 e devolve os novos inícios de cada beat + marks da cena final.
uso: python3 tighten.py roteiro_brio_10 [roteiro_brio_11 ...]   (grava NARRATION no roteiro)"""
import sys, os, json, subprocess, importlib, re, numpy as np
import tts
SR = 44100
MAX_GAP, KEEP_GAP, LEAD = 0.20, 0.11, 0.04   # pausas > 0,20 s viram 0,11 s
HOOK_TEMPO = 1.08                             # gancho 8% mais rápido

def load(p):
    return np.frombuffer(subprocess.check_output(['ffmpeg','-loglevel','error','-i',p,'-ac','1','-ar',str(SR),'-f','f32le','-']),np.float32).copy()

def silences(x):
    fr = int(0.01 * SR); n = len(x) // fr
    rms = np.sqrt(np.mean(x[:n*fr].reshape(n, fr)**2, axis=1) + 1e-12)
    thr = max(np.percentile(rms, 95) * 0.04, 1e-4)
    q = rms < thr; out = []; i = 0
    while i < n:
        if q[i]:
            j = i
            while j < n and q[j]: j += 1
            out.append((i * 0.01, j * 0.01)); i = j
        else: i += 1
    return out

def process(name):
    m = importlib.import_module(name)
    mp3, starts, dur = tts.full(m)
    al = json.load(open(mp3.replace('.mp3', '.json'))); cs = al['character_start_times_seconds']
    x = load(mp3); T = len(x) / SR
    texts = [b['text'].strip() for b in m.BEATS]
    # cortes: [(t0,t1)] trechos removidos
    cuts = []
    for a, b in silences(x):
        if a <= 0.001:  # silêncio inicial
            if b > LEAD: cuts.append((0.0, b - LEAD)); 
            continue
        if b >= T - 0.01: continue
        if b - a > MAX_GAP: cuts.append((a + KEEP_GAP / 2, b - KEEP_GAP / 2))
    keep = []; t = 0.0
    for a, b in cuts:
        if a > t: keep.append((t, a))
        t = b
    keep.append((t, T))
    # gancho mais rápido: até o início do beat 2
    hook_end = starts[1] - 0.05 if len(starts) > 1 else 0
    segs = []; 
    for a, b in keep:
        if b <= hook_end: segs.append((a, b, HOOK_TEMPO))
        elif a < hook_end: segs += [(a, hook_end, HOOK_TEMPO), (hook_end, b, 1.0)]
        else: segs.append((a, b, 1.0))
    # mapa de tempo
    pts = []; nt = 0.0
    for a, b, k in segs:
        pts.append((a, nt, b, nt + (b - a) / k, k)); nt += (b - a) / k
    def tmap(t):
        for a, n0, b, n1, k in pts:
            if t <= b: return n0 + max(0.0, t - a) / k
        return nt
    # áudio novo
    os.makedirs('audio_tight', exist_ok=True); tmp = 'audio_tight/_seg'; parts = []
    for i, (a, b, k) in enumerate(segs):
        y = x[int(a * SR):int(b * SR)]
        p = f'{tmp}{i}.f32'; y.astype(np.float32).tofile(p)
        q = f'{tmp}{i}.wav'
        af = f'atempo={k}' if k != 1.0 else 'anull'
        subprocess.run(['ffmpeg','-loglevel','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i',p,'-af',af,q], check=True); parts.append(q)
    lst = f'{tmp}list.txt'; open(lst, 'w').write(''.join(f"file '{os.path.abspath(q)}'\n" for q in parts))
    out = f'audio_tight/{name}.mp3'
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',lst,'-af','afade=t=out:st=%.2f:d=0.05' % (nt - 0.05),'-c:a','libmp3lame','-b:a','160k',out], check=True)
    for f in os.listdir('audio_tight'):
        if f.startswith('_seg'): os.remove(os.path.join('audio_tight', f))
    new_starts = [round(tmap(s), 3) for s in starts]; new_starts[0] = 0.0
    # marks da cena final (relativos ao início do último beat)
    b = m.BEATS[-1]; marks = dict(b.get('marks', {}))
    if marks:
        p0 = len(' '.join(texts[:-1])) + 1; t0o = cs[p0]
        for kk, v in marks.items(): marks[kk] = round(tmap(t0o + v) - tmap(t0o), 3)
    src = open(name + '.py').read()
    src = re.sub(r"\nNARRATION = .*\n", "\n", src)
    src = src.replace('\nBEATS = [', f"\nNARRATION = {{'file': {out!r}, 'starts': {new_starts!r}}}  # narração enxuta (tighten.py)\n\nBEATS = [", 1)
    if marks:
        src = re.sub(r"marks=\{[^}]*\}", f"marks={marks!r}", src)
    open(name + '.py', 'w').write(src)
    print(name, f'{T:.1f}s -> {nt:.1f}s', 'pausas cortadas:', len(cuts))

if __name__ == '__main__':
    for n in sys.argv[1:]: process(n)
