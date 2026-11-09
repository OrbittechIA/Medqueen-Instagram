import sys, subprocess, asyncio
from playwright.async_api import async_playwright
mode=sys.argv[1]; out=sys.argv[2]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        import os
        await pg.goto('file://'+os.path.abspath('index.html')); await pg.wait_for_timeout(800)
        dur=await pg.evaluate('DUR')
        if mode=='prev':
            ts=[float(x) for x in sys.argv[3].split(',')]
            for i,t in enumerate(ts):
                await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'{out}/p{i:02d}.jpg',type='jpeg',quality=70)
        else:
            fps=30; n=int(dur*fps)
            ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(fps),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium',out],stdin=subprocess.PIPE)
            for i in range(n):
                await pg.evaluate(f'render({i/fps})')
                ff.stdin.write(await pg.screenshot(type='jpeg',quality=92))
            ff.stdin.close(); ff.wait()
        await b.close()
asyncio.run(main())
