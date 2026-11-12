"""Ritmo de Reels sem gastar crédito: encurta pausas longas e acelera levemente, remapeando as marcas de tempo.
uso: from apertar import apertar; mp3_out, mapa = apertar(mp3_in, mp3_out, max_pausa=0.14, tempo=1.06)
mapa(t) converte um tempo do áudio original para o áudio novo."""
import re
import subprocess


def _silencios(mp3, db=-35, minimo=0.18):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp3, "-af", f"silencedetect=noise={db}dB:d={minimo}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    fim = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    return list(zip(ini, fim))


def apertar(mp3_in, mp3_out, max_pausa=0.14, tempo=1.06, inicio_min=0.05):
    sil = [(a, b) for a, b in _silencios(mp3_in) if a > inicio_min]
    cortes = []  # (início do trecho removido, duração removida) no tempo original
    for a, b in sil:
        dur = b - a
        if dur > max_pausa:
            meio = a + max_pausa / 2
            cortes.append((meio, dur - max_pausa))
    # monta o filtro: mantém tudo menos os trechos cortados
    keep = []; t0 = 0.0
    for meio, rem in cortes:
        keep.append((t0, meio)); t0 = meio + rem
    keep.append((t0, None))
    parts = []
    for i, (a, b) in enumerate(keep):
        if b is None:
            parts.append(f"[0:a]atrim=start={a:.3f},asetpts=PTS-STARTPTS[p{i}]")
        else:
            parts.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[p{i}]")
    fc = ";".join(parts) + ";" + "".join(f"[p{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1,atempo={tempo}[o]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3_in, "-filter_complex", fc, "-map", "[o]", "-b:a", "192k", mp3_out], check=True)

    def mapa(t):
        rem = 0.0
        for meio, r in cortes:
            if t > meio + r:
                rem += r
            elif t > meio:
                rem += t - meio
        return (t - rem) / tempo
    return mp3_out, mapa


def inicios_por_beat(alinhamento, textos):
    """acha o início (s) de cada beat no alinhamento de caracteres do texto completo"""
    chars = "".join(alinhamento["characters"]); st = alinhamento["character_start_times_seconds"]
    out = []; pos = 0
    for tx in textos:
        frag = tx.strip()[:14]
        k = chars.find(frag, pos)
        if k < 0:
            k = pos
        # pula espaços/marcas iniciais
        out.append(st[min(k, len(st) - 1)]); pos = k + 1
    return out
