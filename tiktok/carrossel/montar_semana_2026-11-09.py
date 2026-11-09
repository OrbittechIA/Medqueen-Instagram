"""7 carrosséis TikTok (09 a 15/11): fotos Kairogen + texto no padrão do carrossel 01 (Poppins Bold branco com contorno)."""
import os
from PIL import Image, ImageDraw, ImageFont

D = "/home/claude/carrosseis"
POP = "/tmp/Poppins-Bold.ttf"
W, H = 1080, 1920

def fit(path):
    im = Image.open(path).convert("RGB")
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))

def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out

def texto(img, text, yc, size=64, maxw=900):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(POP, size)
    lines = wrap(d, text, f, maxw); lh = int(size * 1.22)
    y = yc - lh * len(lines) / 2
    for ln in lines:
        w = d.textlength(ln, font=f)
        d.text(((W - w) / 2, y), ln, font=f, fill="white", stroke_width=max(4, size // 13), stroke_fill="black")
        y += lh

# (texto, y do centro, tamanho) por slide; slide 5 pode ter 2 textos
C = {
 "c1": [("3 jeitos de decorar a cascata de coagulação (o 3º salvou meu semestre)", 330, 66),
        ("1. desenhar a cascata à mão até a mão doer", 330, 64),
        ("2. inventar musiquinha pros fatores (não funcionou)", 1250, 64),
        ("3. jogar o PDF da aula na IA e virar flashcard", 330, 64),
        [("a IA transformou o PDF da aula em 20 flashcards", 300, 62)]],
 "c2": [("coisas que eu queria saber no 1º período de Medicina", 330, 68),
        ("resumo bonito não é revisão", 1250, 70),
        ("questão ensina mais do que reler o PDF", 300, 66),
        ("ninguém dá conta do PDF inteiro sozinho", 300, 66),
        [("hoje eu estudo pelo simulado que a IA monta do meu material", 300, 60)]],
 "c3": [("meu método pra estudar fisiologia em 30 minutos", 300, 68),
        ("min 0 a 5: subo o PDF da aula", 1280, 66),
        ("min 5 a 15: a IA me dá a aula do material", 1330, 64),
        ("min 15 a 30: flashcard e simulado", 1350, 66),
        [("e a aula vem do meu PDF, com quadro e tudo", 1400, 62)]],
 "c4": [("ciclo de Krebs sem sofrimento (salva esse)", 300, 70),
        ("onde acontece: na matriz da mitocôndria", 330, 66),
        ("entra acetil-CoA, sai CO2 e energia", 1400, 66),
        ("por volta: 3 NADH, 1 FADH2 e 1 GTP", 1330, 66),
        [("o resto eu revisei com flashcard que a IA cria do meu material", 1330, 58)]],
 "c5": [("professor mandou PDF de 200 páginas e a prova é em 5 dias", 1330, 64),
        ("antes: lia tudo e não lembrava de nada", 300, 66),
        ("agora: subo o material da aula na IA", 300, 66),
        ("e ela separa o que cai na prova", 1350, 68),
        [("olha o que ela separou do meu material", 300, 64)]],
 "c6": [("checklist da véspera de prova (de quem passa)", 300, 68),
        ("1. não abrir matéria nova", 300, 70),
        ("2. fazer 1 simulado do conteúdo", 1350, 68),
        ("3. revisar só o que errou", 1300, 70),
        [("meu simulado da véspera, corrigido na hora", 300, 64)]],
 "c7": [("minha veterana passou em tudo e eu descobri o segredo dela", 1330, 64),
        ("ela não fazia resumo", 330, 72),
        ("ela não lia o PDF inteiro", 1350, 72),
        ("aí ela me mostrou o celular dela...", 330, 68),
        [("uma IA feita só pra Medicina", 240, 70), ("resume o PDF, cria flashcard e simulado", 440, 52)]],
}

os.makedirs(f"{D}/saida", exist_ok=True)
for c, slides in C.items():
    os.makedirs(f"{D}/saida/{c}", exist_ok=True)
    for i, s in enumerate(slides, 1):
        img = fit(f"{D}/raw/{c}_{i}.png")
        for t, y, sz in (s if isinstance(s, list) else [s]):
            texto(img, t, y, sz)
        img.save(f"{D}/saida/{c}/slide{i}.jpg", quality=93)
    # folha de contato
    ims = [Image.open(f"{D}/saida/{c}/slide{i}.jpg").resize((270, 480)) for i in range(1, 6)]
    sh = Image.new("RGB", (270 * 5 + 40, 520), "white")
    for i, im in enumerate(ims): sh.paste(im, (20 + i * 270, 20))
    sh.save(f"{D}/saida/{c}_folha.jpg", quality=88)
print("ok")
