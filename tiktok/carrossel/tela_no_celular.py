"""Põe a tela real do app (PNG do HyperFrames, banco carrossel/telas/) dentro do celular de tela branca de uma foto da Kairogen.

Uso: python3 -I tela_no_celular.py <foto com celular de tela branca> <tela.png> <saida.png> [zoom] [x0,y0,x1,y1]
- Pede à Kairogen um celular de frente, "screen completely plain white and blank".
- Acha a maior área branca com formato de tela (a tela), pega os 4 cantos e encaixa a tela com perspectiva,
  recortada pela própria máscara branca (cantos arredondados do aparelho).
- zoom (ex. 1.5): recorta a foto em volta do celular (mantendo 9:16) pra tela ficar maior e legível.
- caixa x0,y0,x1,y1 (na foto já com 1920 de altura): só procura a tela ali (cena muito branca).
- A tela fica idêntica ao PNG (nada redesenhado pela IA), de frente e legível.
"""
import sys
import cv2
import numpy as np

foto, tela, out = sys.argv[1], sys.argv[2], sys.argv[3]
ZOOM = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
BOX = [int(v) for v in sys.argv[5].split(",")] if len(sys.argv) > 5 else None


def to1920(im):
    k = 1920 / im.shape[0]
    return cv2.resize(im, (round(im.shape[1] * k), 1920), interpolation=cv2.INTER_LANCZOS4)


def acha(img, box):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = ((hsv[..., 2] > 228) & (hsv[..., 1] < 25)).astype(np.uint8) * 255
    if box:
        keep = np.zeros_like(mask); keep[box[1]:box[3], box[0]:box[2]] = 255; mask &= keep
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(mask)
    best = None
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if h > w * 1.4 and a > 0.01 * img.shape[0] * img.shape[1] and a > 0.75 * w * h:
            if best is None or a > st[best][4]:
                best = i
    assert best is not None, "não achei a tela branca"
    m = (lab == best).astype(np.uint8) * 255
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cnts, key=cv2.contourArea).reshape(-1, 2).astype(np.float32)
    s = c.sum(1); d = c[:, 0] - c[:, 1]
    quad = np.array([c[np.argmin(s)], c[np.argmax(d)], c[np.argmax(s)], c[np.argmin(d)]], np.float32)
    cen = quad.mean(0)
    x, y, w, h = cv2.boundingRect(c.astype(np.int32))
    quad = quad + (quad - cen) / np.linalg.norm(quad - cen, axis=1, keepdims=True) * min(w, h) * 0.06
    return m, quad


raw = cv2.imread(foto)
img = to1920(raw)
m, quad = acha(img, BOX)
if ZOOM > 1:
    k = raw.shape[0] / 1920
    cx, cy = quad.mean(0) * k
    H, W = raw.shape[0] / ZOOM, raw.shape[0] / ZOOM * 9 / 16
    x0 = int(min(max(cx - W / 2, 0), raw.shape[1] - W)); y0 = int(min(max(cy - H / 2, 0), raw.shape[0] - H))
    raw = raw[y0:y0 + int(H), x0:x0 + int(W)]
    img = to1920(raw)
    m, quad = acha(img, None)  # com zoom, sem caixa (use caixa só sem zoom)

scr = cv2.imread(tela)
h0, w0 = scr.shape[:2]
scr = scr[int(h0 * 0.006):h0 - int(h0 * 0.004), int(w0 * 0.012):w0 - int(w0 * 0.012)]
Hm = cv2.getPerspectiveTransform(np.array([[0, 0], [scr.shape[1], 0], [scr.shape[1], scr.shape[0]], [0, scr.shape[0]]], np.float32), quad)
warp = cv2.warpPerspective(scr, Hm, (img.shape[1], img.shape[0]), flags=cv2.INTER_AREA)
mm = cv2.GaussianBlur(cv2.dilate(m, np.ones((3, 3), np.uint8)), (3, 3), 0).astype(np.float32)[..., None] / 255
cv2.imwrite(out, (warp * mm + img * (1 - mm)).astype(np.uint8))
print("tela em", [tuple(map(int, p)) for p in quad])
