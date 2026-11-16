// Renderiza a cena Three.js quadro a quadro num Chrome sem tela e monta o MP4 com ffmpeg.
// uso: node render.mjs [saida.mp4] [--stills 0,60,150] [--scale 0.5] [--chrome /caminho/do/chrome]
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";
import puppeteer from "puppeteer-core";

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const out = args.find((a) => a.endsWith(".mp4")) || "piloto_brio_3d.mp4";
const stills = opt("--stills", null);
const scale = opt("--scale", "1");
const sceneF = opt("--scene", "scene.js");
const chrome = opt("--chrome", process.env.CHROME_PATH || "/usr/bin/google-chrome");
const ROOT = path.dirname(new URL(import.meta.url).pathname);

const types = { ".html": "text/html", ".js": "text/javascript", ".ttf": "font/ttf", ".json": "application/json" };
const server = http.createServer((req, res) => {
  const p = path.join(ROOT, decodeURIComponent(req.url.split("?")[0]));
  if (!p.startsWith(ROOT) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": types[path.extname(p)] || "application/octet-stream" }); fs.createReadStream(p).pipe(res);
}).listen(0);
const port = server.address().port;

const browser = await puppeteer.launch({
  executablePath: chrome, headless: true,
  args: ["--no-sandbox", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist", "--disable-dev-shm-usage"],
});
const page = await browser.newPage();
page.on("console", (m) => { if (m.type() === "error") console.error("[página]", m.text()); });
page.on("pageerror", (e) => console.error("[página]", e.message));
await page.setViewport({ width: 1080, height: 1920 });
await page.goto(`http://127.0.0.1:${port}/index.html?scale=${scale}&scene=${sceneF}`, { waitUntil: "load" });
await page.waitForFunction("window.ready && window.renderFrame", { timeout: 60000 });
await page.evaluate("window.ready");
const N = await page.evaluate("window.FRAMES"), FPS = await page.evaluate("window.FPS");
const gl = await page.evaluate(() => { const c = document.createElement("canvas").getContext("webgl2"); const d = c.getExtension("WEBGL_debug_renderer_info"); return d ? c.getParameter(d.UNMASKED_RENDERER_WEBGL) : "?"; });
console.log("WebGL:", gl);

const t0 = Date.now();
if (stills) {
  for (const f of stills.split(",").map(Number)) {
    const url = await page.evaluate((f) => window.renderFrame(f, "image/png"), f);
    fs.writeFileSync(path.join(ROOT, `still_${String(f).padStart(4, "0")}.png`), Buffer.from(url.split(",")[1], "base64"));
  }
  console.log(`stills em ${((Date.now() - t0) / 1000).toFixed(1)} s`);
} else {
  const ff = spawn("ffmpeg", ["-v", "error", "-y", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
    "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], { stdio: ["pipe", "inherit", "inherit"] });
  for (let f = 0; f < N; f++) {
    const url = await page.evaluate((f) => window.renderFrame(f), f);
    if (!ff.stdin.write(Buffer.from(url.split(",")[1], "base64"))) await new Promise((r) => ff.stdin.once("drain", r));
    if (f % 30 === 0) console.log(`quadro ${f}/${N}  ${((Date.now() - t0) / 1000).toFixed(1)} s`);
  }
  ff.stdin.end(); await new Promise((r) => ff.on("close", r));
  const s = (Date.now() - t0) / 1000;
  console.log(`RENDER: ${N} quadros em ${s.toFixed(1)} s (${(s / N).toFixed(2)} s/quadro) -> ${out}`);
}
await browser.close(); server.close();
