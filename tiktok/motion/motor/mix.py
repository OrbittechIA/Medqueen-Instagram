"""Trilha + efeitos + vídeo final de um motion do TikTok.

Uso: python3 -I mix.py <pasta do vídeo> <musica.mp3> [segundo do drop na música | calma]
- Lê <pasta>/meta.json (DUR, DROP, EVENTS) gravado pelo render.js e os quadros em <pasta>/frames.
- Com o segundo do drop: a música começa de forma que o drop caia em DROP (o momento da revelação).
  Sem o terceiro argumento, acha o drop sozinho (maior salto de energia em janelas de 50 ms).
  "calma" ou "calma:SEG": começa do segundo 2 (ou SEG) da faixa, sem alinhar drop (faixa sem virada).
  Confira se a faixa não tem silêncio no meio do trecho (algumas fazem fade e recomeçam).
- Música a -6 dB com fade de entrada e saída, efeitos por cima, loudnorm -14 LUFS, pico -1,5 dBTP.
- Grava <pasta>/video.mp4 (H.264 veryfast crf 20, AAC 192k).
"""
import json, subprocess, sys, os
import numpy as np

DIR, MUS = sys.argv[1], sys.argv[2]
ARG = sys.argv[3] if len(sys.argv) > 3 else None
SR = 44100
EFX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "motor", "www", "som", "efeitos")
meta = json.load(open(os.path.join(DIR, "meta.json")))
DUR, DROP = meta["DUR"], meta["DROP"]


def load(path, filt=None, sr=SR, ch=2):
    cmd = ["ffmpeg", "-v", "error", "-i", path] + (["-af", filt] if filt else []) + ["-ac", str(ch), "-ar", str(sr), "-f", "f32le", "-"]
    a = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype=np.float32)
    return a.reshape(-1, ch).copy()


def acha_drop(path):
    a = load(path, sr=8000, ch=1)[:, 0]
    w = 400
    e = np.array([np.sqrt((a[i:i + w] ** 2).mean()) for i in range(0, len(a) - w, w)])
    db = 20 * np.log10(e + 1e-9)
    # salto entre a média de 1 s antes e 0,5 s depois
    best, bt = -1, 0
    for i in range(20, len(db) - 10):
        j = db[i:i + 10].mean() - db[i - 20:i].mean()
        if j > best: best, bt = j, i * 0.05
    return bt, best


if ARG and ARG.startswith("calma"):
    start = float(ARG.split(":")[1]) if ":" in ARG else 2.0
else:
    md = float(ARG) if ARG else acha_drop(MUS)[0]
    start = max(0.0, md - DROP)
N = int(SR * DUR)
out = np.zeros((N, 2), np.float32)
fade_out = DUR - 1.6
mus = load(MUS, f"atrim=start={start},asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st={fade_out}:d=1.5")[:N]
out[:len(mus)] += mus * 10 ** (-6 / 20)
for t, name, db in meta["EVENTS"]:
    a = load(os.path.join(EFX, name + ".wav"))
    peak = np.abs(a).max(axis=1).argmax() / SR
    a = a * 10 ** (db / 20)
    s = int((t - peak) * SR)
    if s < 0: a = a[-s:]; s = 0
    e = min(N, s + len(a)); out[s:e] += a[:e - s]
raw = os.path.join(DIR, "mix.f32"); out.astype(np.float32).tofile(raw)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "30", "-i", os.path.join(DIR, "frames", "f%04d.png"),
                "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", raw, "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-14:TP=-1.5", "-shortest",
                os.path.join(DIR, "video.mp4")], check=True)
os.remove(raw)
print(json.dumps({"inicio_musica": round(start, 2), "drop_video": DROP, "dur": DUR}))
