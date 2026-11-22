// Tira a tela do app (1290x2796, igual ao banco telas/) de um motion, sem legenda por cima.
// Uso: node carrossel/tela_do_motion.js <pasta do vídeo> "<tempo, pode usar T: T.end, T.res+2, T.rv+2, T.cards[0][1]+0.6>" <saida.png>
// Aula: T.end. Prova: T.end+0.15. Flashcards: T.cards[0][1]+0.6. Simulado: T.res+2 (resultado) ou T.rv+2 (revisar).
const { chromium } = require("playwright");
const path=require("path"),fs=require("fs");
const MOTOR=path.join(__dirname,"..","motion","motor");
const [DIR,EXPR,OUT]=process.argv.slice(2);
const CFG=JSON.parse(fs.readFileSync(path.join(DIR,"config.json"),"utf8"));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:3});
await p.addInitScript(c=>{window.CFG=c},CFG);await p.goto("file://"+MOTOR+"/base.html");await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const t=await p.evaluate(e=>{const T=window.T;return eval(e)},EXPR);await p.evaluate(x=>window.render(x),t);
await p.evaluate(()=>{const c=document.getElementById("cam");c.style.transform="none";const d=document.getElementById("device");d.style.transform="translateX(-50%)";d.style.top="20px";d.style.opacity="1";const keep=new Set();let e=d;while(e){keep.add(e);e=e.parentElement;}document.querySelectorAll("body *").forEach(x=>{if(!keep.has(x)&&!d.contains(x))x.style.visibility="hidden";});});
const r=await p.evaluate(()=>{const s=document.getElementById("screen").getBoundingClientRect();return{x:s.x,y:s.y,width:s.width,height:s.height}});
await p.screenshot({path:OUT,clip:r});console.log(t,JSON.stringify(r));await b.close();})();
