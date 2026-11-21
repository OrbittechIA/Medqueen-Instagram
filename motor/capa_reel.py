"""Coloca a CAPA como primeiros quadros do vídeo (regra do Matheus, 21/11/2026).

O Best Content não tem campo de capa no upload de vídeo, e o Instagram usa o
primeiro quadro como capa no grid. Sem isso a capa sai branca (fade de entrada).

Uso: python3 capa_reel.py <video.mp4> <capa.png|jpg> <saida.mp4> [segundos=0.5]
- A capa é redimensionada para 1080x1920 (cover, sem distorcer).
- Título e elemento principal da capa precisam caber no miolo 1080x1440
  (o grid do perfil corta 3:4 no centro): nada importante nos 240 px de cima e de baixo.
- O áudio do vídeo é atrasado pelo tempo da capa (silêncio por baixo dela).
"""
import subprocess, sys
video, capa, saida = sys.argv[1], sys.argv[2], sys.argv[3]
seg = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
fps = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                      'stream=r_frame_rate', '-of', 'csv=p=0', video], capture_output=True, text=True).stdout.strip() or '30'
tem_audio = bool(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries',
                                 'stream=index', '-of', 'csv=p=0', video], capture_output=True, text=True).stdout.strip())
v = (f"[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps={fps},format=yuv420p,"
     f"trim=duration={seg}[c];[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps={fps},format=yuv420p[m];")
if tem_audio:
    f = v + f"[0:a]adelay={int(seg*1000)}:all=1[a];[c][m]concat=n=2:v=1:a=0[v]"
    maps = ['-map', '[v]', '-map', '[a]', '-c:a', 'aac', '-b:a', '192k']
else:
    f = v + "[c][m]concat=n=2:v=1:a=0[v]"
    maps = ['-map', '[v]']
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', video, '-loop', '1', '-t', str(seg + 0.2), '-i', capa,
                '-filter_complex', f, *maps, '-c:v', 'libx264', '-crf', '21', '-preset', 'medium',
                '-movflags', '+faststart', saida], check=True)
# conferência: o primeiro quadro tem que ser a capa
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', saida, '-frames:v', '1', saida.rsplit('.', 1)[0] + '-quadro0.jpg'], check=True)
print('ok:', saida, '| confira', saida.rsplit('.', 1)[0] + '-quadro0.jpg')
