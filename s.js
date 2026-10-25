window.M = async (url) => {
  const b = await (await fetch(url)).blob(); const bm = await createImageBitmap(b);
  const W = bm.width, H = bm.height, T = Math.ceil(H/2);
  const t = document.createElement('canvas'); t.width=W; t.height=H; const tc=t.getContext('2d'); tc.drawImage(bm,0,0);
  const id = tc.getImageData(0,0,W,H); const p=id.data; for (let i=0;i<p.length;i+=4){const a=p[i+3]; p[i]=p[i+1]=p[i+2]=a; p[i+3]=255;} tc.putImageData(id,0,0);
  document.body.innerHTML=''; document.body.style.cssText='margin:0;background:#000'; document.documentElement.style.cssText='margin:0;background:#000;overflow:hidden';
  const c=document.createElement('canvas'); c.width=2*W; c.height=T; c.style.cssText='position:fixed;left:0;top:0'; document.body.appendChild(c);
  const x=c.getContext('2d'); x.fillStyle='#000'; x.fillRect(0,0,2*W,T); x.drawImage(t,0,0); x.drawImage(t,W,-T);
  bm.close && bm.close(); t.width=0;
  return W+'x'+H;
};
window.MM = async (k)=>{ if(!window.R) window.R = await (await fetch('https://raw.githubusercontent.com/OrbittechIA/Medqueen-Instagram/tmp-urls/r.json')).json(); return M('https://dnznrvs05pmza.cloudfront.net/birefnet-v2/'+R[k]); };
