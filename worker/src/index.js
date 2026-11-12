// Worker maestro da Fábrica Brio.
// Rotas:
//   GET  /health                      -> "ok"
//   GET  /webhook                     -> verificação da Meta (hub.challenge)
//   POST /webhook                     -> recebe comentários (assinatura X-Hub-Signature-256)
//   GET  /c/:perfil[/:video]?o=dm|bio -> registra clique e redireciona ao site com UTM
// Segredos (wrangler secret): IG_TOKEN_BRIO, IG_TOKEN_FIBRA, IG_TOKEN_DIAUM, META_APP_SECRET.
// O token de verificação do webhook fica no D1 (config.webhook_verify_token), nunca no repositório.

const PERFIS = new Set(["brio", "fibra", "diaum"]);

async function getConfig(env, chave) {
  const row = await env.DB.prepare("SELECT valor FROM config WHERE chave = ?").bind(chave).first();
  return row ? row.valor : null;
}

async function setConfig(env, chave, valor) {
  await env.DB.prepare(
    "INSERT INTO config (chave, valor) VALUES (?, ?) ON CONFLICT(chave) DO UPDATE SET valor = excluded.valor, atualizado_em = datetime('now')"
  ).bind(chave, valor).run();
}

function hex(buf) {
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function assinaturaValida(secret, corpo, header) {
  if (!secret || !header || !header.startsWith("sha256=")) return false;
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const mac = hex(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(corpo)));
  const recebido = header.slice(7);
  if (mac.length !== recebido.length) return false;
  let diff = 0;
  for (let i = 0; i < mac.length; i++) diff |= mac.charCodeAt(i) ^ recebido.charCodeAt(i);
  return diff === 0;
}

async function verificarWebhook(url, env) {
  const modo = url.searchParams.get("hub.mode");
  const token = url.searchParams.get("hub.verify_token");
  const desafio = url.searchParams.get("hub.challenge");
  const esperado = await getConfig(env, "webhook_verify_token");
  if (modo === "subscribe" && esperado && token === esperado && desafio) {
    return new Response(desafio, { status: 200 });
  }
  return new Response("forbidden", { status: 403 });
}

async function receberWebhook(request, env) {
  const corpo = await request.text();
  const ok = await assinaturaValida(env.META_APP_SECRET, corpo, request.headers.get("x-hub-signature-256"));
  await setConfig(env, "webhook_ultimo", JSON.stringify({ ts: new Date().toISOString(), assinatura_ok: ok, amostra: corpo.slice(0, 1500) }));
  if (!ok) return new Response("ok", { status: 200 }); // não processa, mas não faz a Meta repetir

  let dados;
  try { dados = JSON.parse(corpo); } catch { return new Response("ok", { status: 200 }); }

  const contas = await env.DB.prepare("SELECT perfil, ig_user_id FROM contas").all();
  const porId = Object.fromEntries((contas.results || []).filter((c) => c.ig_user_id).map((c) => [c.ig_user_id, c.perfil]));

  for (const entry of dados.entry || []) {
    const perfil = porId[String(entry.id)] || null;
    for (const ch of entry.changes || []) {
      if (ch.field !== "comments" || !ch.value) continue;
      const v = ch.value;
      // Ignora comentários do próprio perfil.
      if (v.from && String(v.from.id) === String(entry.id)) continue;
      await env.DB.prepare(
        "INSERT OR IGNORE INTO dms (comment_id, perfil, ig_media_id, palavra_chave, status) VALUES (?, ?, ?, ?, 'pendente')"
      ).bind(String(v.id), perfil || "desconhecido", v.media ? String(v.media.id) : null, (v.text || "").slice(0, 200)).run();
    }
  }
  return new Response("ok", { status: 200 });
}

async function clique(url, env, request) {
  const partes = url.pathname.split("/").filter(Boolean); // ["c", perfil, video?]
  const perfil = partes[1];
  const video = partes[2] || "bio";
  const origem = url.searchParams.get("o") === "dm" ? "dm" : "bio";
  const site = env.SITE || "https://briotreino.app";
  if (!PERFIS.has(perfil)) return Response.redirect(site, 302);
  await env.DB.prepare("INSERT INTO cliques (perfil, video_id, origem, pais) VALUES (?, ?, ?, ?)")
    .bind(perfil, video, origem, request.cf ? request.cf.country || null : null).run();
  const destino = new URL(site);
  destino.searchParams.set("utm_source", "instagram");
  destino.searchParams.set("utm_medium", origem);
  destino.searchParams.set("utm_campaign", env.CAMPANHA || "sprint_nov26");
  destino.searchParams.set("utm_content", `${perfil}_${video}`);
  return Response.redirect(destino.toString(), 302);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    try {
      if (url.pathname === "/health") return new Response("ok");
      if (url.pathname === "/webhook" && request.method === "GET") return verificarWebhook(url, env);
      if (url.pathname === "/webhook" && request.method === "POST") return receberWebhook(request, env);
      if (url.pathname.startsWith("/c/")) return clique(url, env, request);
      return new Response("not found", { status: 404 });
    } catch (e) {
      return new Response("erro", { status: 500 });
    }
  },
};
