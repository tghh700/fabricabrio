# render3d — vídeos 3D do Brio sem Blender

Cena 3D em tempo real (Three.js: PBR, sombras suaves, ambiente HDR, bloom) renderizada quadro a quadro num Chrome sem tela,
montada em MP4 pelo ffmpeg. Cada quadro depende só de `t`, então o resultado é determinístico e não precisa de placa de vídeo.

- `scene.js` — cena, boneco, banco, barra, câmera, texto por cima (Anton).
- `render.mjs` — servidor local + Chrome headless (puppeteer-core) + ffmpeg.
- Local: `npm install && node render.mjs piloto_brio_3d.mp4` (`--stills 0,150` para prévias, `--scale 0.5` para rascunho).
- Nuvem: workflow `render-3d` (push em `render3d/**`) → branch `previas`, pasta `render3d/`.

Tempo medido (piloto 10 s, 1080×1920, 30 fps, 300 quadros): 161 s numa máquina de 2 núcleos sem GPU (0,54 s/quadro).
