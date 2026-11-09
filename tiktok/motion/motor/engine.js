// Motor de motion do TikTok da MedQueen IA.
// Lê window.CFG (config.json do vídeo) e monta a linha do tempo pelo formato.
// Formatos: "flashcards", "aula" (quadro/tabela), "prova" (o que cai na prova), "simulado".
// Expõe window.render(t), window.DUR, window.DROP (segundo em que a música deve estourar) e window.EVENTS (efeitos sonoros).
const $ = (id) => document.getElementById(id);
const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
const prog = (t, a, b) => clamp((t - a) / (b - a));
const ease = (x) => 1 - Math.pow(1 - x, 3);
const easeIn = (x) => x * x * x;
const easeIO = (x) => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const back = (x) => { const c1 = 1.5, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
const show = (el, o, y = 0, s = 1) => { el.style.opacity = String(o); el.style.transform = `translateY(${y}px) scale(${s})`; };
const TOK = /(<[^>]+>|\s+)/;
function partialHTML(html, n) {
  const out = []; let c = 0;
  for (const tk of html.split(TOK).filter(Boolean)) {
    if (tk.startsWith("<") || /^\s+$/.test(tk)) { out.push(tk); continue; }
    if (c >= n) break; out.push(tk); c++;
  }
  let s = out.join(""); if ((s.match(/<strong>/g) || []).length > (s.match(/<\/strong>/g) || []).length) s += "</strong>"; return s;
}
const words = (h) => h.split(TOK).filter((tk) => tk && !tk.startsWith("<") && !/^\s+$/.test(tk)).length;
function typed(text, p) { return text.slice(0, Math.round(text.length * p)); }
function ripple(el, t, a) { const r = prog(t, a, a + 0.35); el.style.opacity = r > 0 && r < 1 ? String(.9 * (1 - r)) : "0"; el.style.transform = `scale(${1 + r * 14})`; }

const C = window.CFG;
const F = C.formato;
const ANS = C.resposta || [];
const parts = (b) => b.t === "table" ? [...b.head, ...b.rows.flat()] : b.t === "ul" || b.t === "ol" ? b.items : b.t === "call" ? b.lines : [b.h];
const bw = (b) => parts(b).reduce((a, h) => a + words(h), 0);
const W_AT = (t) => { let w = 0; for (const b of ANS) { w += bw(b); if (b.t === t) return w; } return w; };
const W_ALL = ANS.reduce((a, b) => a + bw(b), 0);
function renderBlock(b, n) {
  const take = (h) => { const w = words(h); const s = partialHTML(h, Math.min(w, n)); n -= w; return s; };
  if (b.t === "table") {
    const head = b.head.map((h) => `<th>${take(h)}</th>`).join("");
    let rows = "";
    for (const r of b.rows) { if (n <= 0) break; rows += "<tr>" + r.map((c) => `<td>${n > 0 ? take(c) : ""}</td>`).join("") + "</tr>"; }
    return `<div class="tbl" id="tblZ"><table><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table></div>`;
  }
  if (b.t === "ul" || b.t === "ol") {
    let li = "", i = 0;
    for (const it of b.items) { if (n <= 0) break; i++; li += `<li>${b.t === "ul" ? '<span class="d"></span>' : `<span class="n">${i}</span>`}<span>${take(it)}</span></li>`; }
    return `<${b.t}>${li}</${b.t}>`;
  }
  if (b.t === "call") {
    let ls = ""; for (const l of b.lines) { if (n <= 0) break; ls += `<span>${take(l)}</span>`; }
    return `<div class="call" id="callZ"><i></i><div>${ls}</div></div>`;
  }
  return `<${b.t}>${take(b.h)}</${b.t}>`;
}
function stream(n) { let html = "", left = n; for (const b of ANS) { if (left <= 0) break; const w = bw(b); html += renderBlock(b, left); left -= w; } return html; }

// ---------- preenche a tela com o conteúdo do vídeo ----------
$("hook").innerHTML = C.gancho.map((l, i) => `<div>${i === 1 ? `<span class="grad">${l}</span>` : l}</div>`).join("");
$("attnm").textContent = C.pdf;
["u1pdf", "u2pdf"].forEach((id) => ($(id).textContent = C.pdf));
$("u1txt").textContent = C.pedido; $("u2txt").textContent = C.pedido;
if (C.flashcards) {
  $("fctitle").textContent = `${C.flashcards.total} flashcards prontos para estudar`;
  $("fcc").textContent = `${C.flashcards.total} cards.`; $("fcsrc").textContent = "Fonte: " + C.pdf;
  C.flashcards.cards.forEach(([q, r], i) => { const k = "ABC"[i]; $("q" + k).textContent = q; $("r" + k).textContent = r; });
}
const S = C.simulado;
if (S) {
  $("simtt").textContent = "Simulado · " + S.materia; $("simchip1").textContent = C.pdf.replace(/\.pdf$/, ""); $("simchip2").textContent = S.area;
  $("simstem").textContent = S.enunciado; $("rvstem").textContent = S.enunciado;
  $("opts").innerHTML = S.opcoes.map((o, i) => `<div class="opt" id="opt${i}"><span class="l">${"ABCD"[i]}</span><span>${o}</span></div>`).join("");
  $("rvans").textContent = `✓ ${"ABCD"[S.certa]}. ${S.opcoes[S.certa]}`; $("rvwhy").textContent = S.porque;
  $("rvsrc").textContent = "Questão 3 · " + C.pdf.replace(/\.pdf$/, ""); $("errs").textContent = String(10 - S.acertos);
}
if (C.queen) $("fqueen").src = "../../../motor/www/marca/queen-poses/" + C.queen;
// esconde as cenas do Reel longo que não entram no TikTok
["s1", "s2", "s6", "st1", "st2", "st3", "st4", "zc0", "zc1", "zc2", "zc3", "zc4", "zc5"].forEach((id) => { const e = $(id); if (e) e.style.display = "none"; });
const useU2 = F === "flashcards";
$(useU2 ? "u1" : "u2").style.display = "none"; $(useU2 ? "a1" : "a2").style.display = "none";
if (F !== "simulado") $("sim").style.display = "none";
// legendas dos zooms
const caps = (C.legendas || []).map((html) => { const d = document.createElement("div"); d.className = "zcap"; d.style.top = "150px"; d.innerHTML = html; document.body.appendChild(d); return d; });

// ---------- linha do tempo ----------
const T = {};
T.att = 0.5; T.up0 = 0.6; T.up1 = 1.9; T.ty0 = 2.2;
T.ty1 = T.ty0 + clamp(C.pedido.length * 0.028, 0.8, 1.4); T.send = T.ty1 + 0.12; T.chat = T.send + 0.15;
T.row = T.chat + 0.1; T.ans = T.chat + 0.4; T.body = T.chat + 0.65;
const Z = []; // [início, fim, alvo, zoom, índice da legenda]
const EV = [[0.3, "mouse_click", -10], [T.up1, "notification", -15], [T.ty0 + 0.2, "keyboard_typing", -16], [T.send, "mouse_click", -10]];
if (F === "flashcards") {
  T.fc = T.body + 0.35; T.reveal = T.fc; T.drop = T.fc;
  T.cards = [[T.fc + 0.7, T.fc + 1.4, T.fc + 3.0], [T.fc + 3.2, T.fc + 3.8, T.fc + 5.4], [T.fc + 5.6, T.fc + 6.2, 99]];
  Z.push([T.fc + 0.3, T.fc + 7.6, () => $("fc"), 1.42, 0]);
  T.out = T.fc + 7.4;
  EV.push([T.fc, "toggle", -12]); T.cards.forEach((c) => EV.push([c[1], "woosh_1", -17]));
} else if (F === "aula") {
  T.reveal = T.body; T.tA = T.body + 3.0; Z.push([T.tA + 0.1, T.tA + 3.1, () => $("tblZ"), 1.7, 0]);
  T.tB = T.tA + 4.4; Z.push([T.tB + 0.1, T.tB + 3.3, () => $("callZ"), 1.7, 1]);
  T.end = T.tB + 3.8; T.out = T.end + 0.2; T.drop = T.tA + 0.1;
  EV.push([T.tA + 0.1, "woosh_1", -17], [T.tA + 1.2, "toggle", -14], [T.tB + 0.1, "woosh_1", -17]);
} else if (F === "prova") {
  T.reveal = T.body; T.tB = T.body + 2.2; T.hl = T.tB + 0.7; T.hlStep = 1.15;
  const nl = ANS.find((b) => b.t === "call").lines.length - 1;
  Z.push([T.tB + 0.1, T.hl + nl * T.hlStep + 0.6, () => $("callZ"), 1.75, 0]);
  T.end = T.hl + nl * T.hlStep + 1.1; T.out = T.end + 0.2; T.drop = T.tB + 0.1;
  EV.push([T.tB + 0.1, "woosh_1", -17]); for (let i = 0; i < nl; i++) EV.push([T.hl + i * T.hlStep, "toggle", -15]);
} else if (F === "simulado") {
  T.reveal = T.body; T.sim = T.body + 1.5; T.drop = T.sim;
  T.sel = T.sim + 2.4; T.fin = T.sim + 3.9; T.res = T.sim + 4.2; T.rv = T.sim + 6.5;
  Z.push([T.sim + 0.4, T.sim + 3.6, () => document.querySelector(".qcard"), 1.3, 0]);
  Z.push([T.res + 0.2, T.res + 2.0, () => $("ov"), 1.35, 1]);
  Z.push([T.rv + 0.2, T.rv + 2.7, () => $("rv"), 1.3, 2]);
  T.out = T.rv + 2.9;
  EV.push([T.sim, "woosh_1", -16], [T.sel, "mouse_click", -10], [T.fin, "mouse_click", -10], [T.res + 0.4, "glitch_counter", -18], [T.rv, "toggle", -13]);
}
T.final = T.out + 0.4; window.DUR = Math.round((T.final + 4.4) * 10) / 10; window.DROP = T.drop;
EV.push([T.out, "woosh_2", -17], [T.final + 0.3, "hit", -13]);
window.EVENTS = EV; window.T = T;

window.render = function (t) {
  ["bg1", "bg2", "bg3", "bg4"].forEach((b) => ($(b).style.opacity = "0"));
  $("bg4").style.opacity = String(1 - prog(t, T.final, T.final + 0.4)); $("bg1").style.opacity = String(prog(t, T.final, T.final + 0.4));
  const hk = $("hook"); const ho = 1 - ease(prog(t, T.reveal, T.reveal + 0.4));
  hk.style.opacity = String(ho); hk.style.transform = `translateX(-50%) scale(${0.96 + 0.04 * ho})`;
  const dev = $("device"); const dout = easeIO(prog(t, T.out, T.out + 0.6));
  dev.style.transform = `translateX(-50%) scale(1.5)`; dev.style.top = (450 + dout * 1600) + "px"; dev.style.opacity = t > T.out + 0.7 ? "0" : "1";

  // anexa o PDF e digita o pedido
  $("attbox").style.display = t >= T.att ? "block" : "none";
  $("anexar").style.background = t > 0.25 && t < T.att ? "#efeafb" : "#fff";
  const rd = prog(t, T.up0, T.up1);
  $("attbar").style.width = (rd * 100) + "%"; $("attok").style.display = rd >= 1 ? "block" : "none"; $("safety").style.display = rd < 1 ? "block" : "none";
  const tp = prog(t, T.ty0, T.ty1);
  $("typed").innerHTML = tp <= 0 ? '<span class="ph">Pergunte à Queen</span>' : typed(C.pedido, tp) + (t < T.send + 0.05 ? '<span class="caret"></span>' : "");
  $("send").style.background = tp >= 1 ? "#3a1d8f" : "#9d8fd3";
  ripple($("rip1"), t, T.send);

  // conversa
  const sw = ease(prog(t, T.chat, T.chat + 0.3));
  $("home").style.opacity = String(1 - sw); $("chat").style.opacity = String(sw);
  const U = useU2 ? "u2" : "u1", A = useU2 ? "a2" : "a1";
  $(U).style.display = t >= T.row ? "flex" : "none";
  const u = ease(prog(t, T.row, T.row + 0.3)); show($(U), u, 16 * (1 - u), 0.96 + 0.04 * u);
  $(A).style.display = t >= T.ans ? "flex" : "none";
  const a = ease(prog(t, T.ans, T.ans + 0.25)); show($(A), a, 10 * (1 - a));
  document.querySelectorAll(".dots i").forEach((d, i) => { d.style.transform = `translateY(${-3 * Math.max(0, Math.sin(t * 9 - i * 0.9))}px)`; });
  $("dockt").className = "ph"; $("dockt").innerHTML = "Pergunte à Queen";

  if (F === "flashcards") {
    $("st_a2").style.display = t < T.fc ? "inline-flex" : "none";
    $("fc").style.display = t >= T.fc ? "block" : "none";
    const fc = ease(prog(t, T.fc, T.fc + 0.4)); show($("fc"), fc, 24 * (1 - fc));
    T.cards.forEach(([tin, tflip, tout], i) => {
      const inn = i === 0 ? 1 : easeIO(prog(t, tin - 0.4, tin)), f = easeIO(prog(t, tflip, tflip + 0.45)), out = easeIO(prog(t, tout, tout + 0.45));
      const el = $("flip" + "ABC"[i]);
      el.style.transform = `translateX(${420 * (1 - inn) - 420 * out}px) rotate(${-8 * out}deg) rotateY(${180 * f}deg)`;
      el.style.opacity = String(Math.min(inn, 1 - out));
    });
    const tot = C.flashcards.total;
    $("num").textContent = t >= T.cards[1][2] ? `3 / ${tot}` : t >= T.cards[0][2] ? `2 / ${tot}` : `1 / ${tot}`;
  } else {
    let n;
    if (F === "aula") {
      const WA = W_AT("table"), WB = W_AT("call");
      if (t < T.tA) n = WA * easeIn(prog(t, T.body, T.tA));
      else if (t < T.tA + 3.1) n = WA;
      else if (t < T.tB) n = WA + (WB - WA) * prog(t, T.tA + 3.1, T.tB);
      else if (t < T.tB + 3.3) n = WB;
      else n = WB + (W_ALL - WB) * prog(t, T.tB + 3.3, T.end);
    } else if (F === "prova") {
      const WB = W_AT("call");
      if (t < T.tB) n = WB * prog(t, T.body, T.tB); else if (t < T.end - 0.5) n = WB; else n = WB + (W_ALL - WB) * prog(t, T.end - 0.5, T.end);
    } else n = W_ALL * prog(t, T.body, T.body + 1.0);
    $("ans1").innerHTML = stream(Math.round(n));
    $("st_a1").style.display = n < W_ALL ? "inline-flex" : "none";
    if (F === "aula" && C.linha_destaque != null) {
      const tr = document.querySelectorAll("#tblZ tbody tr")[C.linha_destaque];
      if (tr && t > T.tA + 1.2) tr.className = "hl";
    }
    if (F === "prova") document.querySelectorAll("#callZ span").forEach((s, i) => {
      if (i === 0) return; const k = 100 * ease(prog(t, T.hl + (i - 1) * T.hlStep, T.hl + (i - 1) * T.hlStep + 0.5));
      s.innerHTML = `<mark class="hlm" style="background-size:${k}% 100%">${s.innerHTML}</mark>`;
    });
  }
  const th = $("thread"); th.style.transform = "none";
  const need = Math.max(0, th.offsetTop + th.offsetHeight - (752 - 82));
  th.style.transform = `translateY(${-need}px)`;

  if (F === "simulado") {
    const sm = ease(prog(t, T.sim, T.sim + 0.5));
    $("sim").style.opacity = String(sm); $("sim").style.transform = `translateX(${(1 - sm) * 60}px)`;
    const secs = 252 + Math.floor(Math.max(0, t - T.sim));
    $("clock").textContent = `${String(Math.floor(secs / 60)).padStart(2, "0")}:${String(secs % 60).padStart(2, "0")}`;
    const sel = t >= T.sel; const o = $("opt" + S.certa); o.className = "opt" + (sel ? " sel" : "");
    o.style.transform = `scale(${t > T.sel - 0.1 && t < T.sel + 0.1 ? 0.97 : 1})`;
    $("answered").textContent = sel ? "3" : "2";
    ripple($("rip3"), t, T.fin);
    const rs = ease(prog(t, T.res, T.res + 0.4)); $("res").style.opacity = String(rs); $("res").style.transform = `translateY(${(1 - rs) * 40}px)`;
    const cnt = ease(prog(t, T.res + 0.4, T.res + 1.5));
    const sc = Math.round(S.acertos * cnt); $("score").textContent = String(sc); $("pct").textContent = String(sc * 10);
    const rvOn = t >= T.rv;
    $("tab1").className = rvOn ? "" : "on"; $("tab2").className = rvOn ? "on" : "";
    $("ov").style.display = rvOn ? "none" : "block"; $("rv").style.display = rvOn ? "block" : "none";
    const rv = ease(prog(t, T.rv, T.rv + 0.4)); $("rv").style.opacity = String(rv); $("rv").style.transform = `translateY(${(1 - rv) * 20}px)`;
  }

  // zoom de câmera e legenda do zoom
  let zk = 0, zoom = null;
  for (const z of Z) { const k = Math.min(easeIO(prog(t, z[0], z[0] + 0.45)), 1 - easeIO(prog(t, z[1] - 0.45, z[1]))); if (k > 0) { zk = k; zoom = z; } }
  caps.forEach((c, i) => { const on = zoom && zoom[4] === i && t > T.reveal + 0.4; const o = on ? ease(prog(zk, 0.5, 1)) : 0; c.style.opacity = String(o); c.style.transform = `translateX(-50%) translateY(${(1 - o) * -20}px) scale(${0.9 + 0.1 * o})`; });
  const cam = $("cam"); cam.style.transform = "none";
  if (zoom && zk > 0) {
    const el = zoom[2]();
    if (el) {
      const r = el.getBoundingClientRect();
      const fx = r.left + r.width / 2, fy = r.top + r.height / 2;
      cam.style.transform = `translate(${(540 - fx * zoom[3]) * zk}px, ${(1080 - fy * zoom[3]) * zk}px) scale(${1 + (zoom[3] - 1) * zk})`;
    }
  }

  // card final
  const f0 = T.final;
  $("final").style.opacity = String(ease(prog(t, f0, f0 + 0.5)));
  const fl = back(prog(t, f0 + 0.2, f0 + 0.8)); $("final").querySelector(".logo").style.transform = `translateX(-50%) scale(${0.8 + 0.2 * fl})`;
  $("final").querySelectorAll(".checks div").forEach((d, i) => { const p = ease(prog(t, f0 + 0.6 + i * 0.2, f0 + 1.0 + i * 0.2)); d.style.opacity = String(p); d.style.transform = `translateX(${(1 - p) * -40}px)`; });
  const fq = ease(prog(t, f0 + 0.8, f0 + 1.6)); const qe = $("final").querySelector(".queen"); qe.style.transform = `translateX(-50%) translateY(${(1 - fq) * 300}px)`; qe.style.opacity = String(fq);
  const cta = back(prog(t, f0 + 1.5, f0 + 2.0)); const ce = $("final").querySelector(".cta"); ce.style.transform = `scale(${(0.7 + 0.3 * cta) * (1 + 0.025 * Math.sin(Math.max(0, t - f0 - 2.2) * 5))})`; ce.style.opacity = String(prog(t, f0 + 1.5, f0 + 1.7));
  $("final").querySelector(".bio").style.opacity = String(prog(t, f0 + 1.8, f0 + 2.2));
};
window.render(0);
