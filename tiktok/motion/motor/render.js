// Grava um motion do TikTok quadro a quadro (Chromium invisível + FFmpeg depois, no mix.py).
// Uso: node render.js <pasta do vídeo com config.json> preview|frames
// preview: 10 quadros em <pasta>/preview para conferir. frames: todos os quadros em <pasta>/frames.
// Sempre grava <pasta>/meta.json com DUR, DROP e EVENTS (efeitos sonoros) para o mix.py.
const { chromium } = require("playwright");
const path = require("path"), fs = require("fs");
const DIR = path.resolve(process.argv[2]);
const mode = process.argv[3] || "preview";
const CFG = JSON.parse(fs.readFileSync(path.join(DIR, "config.json"), "utf8"));
const FPS = 30;
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  page.on("pageerror", (e) => { console.error("ERRO NA PÁGINA:", e.message); process.exitCode = 1; });
  await page.addInitScript((c) => { window.CFG = c; }, CFG);
  await page.goto("file://" + path.join(__dirname, "base.html"));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const meta = await page.evaluate(() => ({ DUR: window.DUR, DROP: window.DROP, EVENTS: window.EVENTS, T: window.T }));
  fs.writeFileSync(path.join(DIR, "meta.json"), JSON.stringify(meta, null, 1));
  const at = (t) => page.evaluate((x) => window.render(x), t);
  if (mode === "preview") {
    const out = path.join(DIR, "preview"); fs.mkdirSync(out, { recursive: true });
    for (let i = 0; i < 12; i++) { const t = 0.1 + i * (meta.DUR - 0.6) / 11; await at(t); await page.screenshot({ path: path.join(out, `p${String(i).padStart(2, "0")}_${t.toFixed(1)}.png`) }); }
  } else {
    const out = path.join(DIR, "frames"); fs.rmSync(out, { recursive: true, force: true }); fs.mkdirSync(out, { recursive: true });
    const N = Math.round(FPS * meta.DUR);
    for (let f = 0; f < N; f++) { await at(f / FPS); await page.screenshot({ path: path.join(out, `f${String(f).padStart(4, "0")}.png`) }); }
  }
  console.log(JSON.stringify({ DUR: meta.DUR, DROP: meta.DROP }));
  await browser.close();
})();
