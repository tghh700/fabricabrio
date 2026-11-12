// Worker maestro da Fábrica Brio.
// Rotas:
//   GET  /health                      -> "ok"
//   GET  /webhook                     -> verificação da Meta (hub.challenge)
//   POST /webhook                     -> comentários: registra e, se bater a palavra-chave do post, responde em público + DM
//   GET  /c/:perfil[/:video]?o=dm|bio -> registra clique e redireciona ao site com UTM
//   GET  /v/<arquivo>.mp4             -> serve o vídeo do branch "midia" do GitHub com content-type correto (a Meta busca daqui)
// Cron (a cada 5 min): publicador (cria contêiner ~15 min antes, publica na hora) + coleta de métricas.
// Segredos (wrangler secret): IG_TOKEN_BRIO, IG_TOKEN_FIBRA, IG_TOKEN_DIAUM, META_APP_SECRET.

const GRAPH = "https://graph.facebook.com/v25.0";
const RAW = "https://raw.githubusercontent.com/tghh700/fabricabrio/midia/";
const PERFIS = new Set(["brio", "fibra", "diaum"]);

// "Bríu" é só a pronúncia usada na narração; na escrita é sempre "Brio".
const escrita = (s) => (s || "").replace(/br[íi]u/gi, (m) => (m === m.toUpperCase() ? "BRIO" : "Brio"));
const token = (env, perfil) => ({ brio: env.IG_TOKEN_BRIO, fibra: env.IG_TOKEN_FIBRA, diaum: env.IG_TOKEN_DIAUM })[perfil];

async function getConfig(env, chave) {
  const row = await env.DB.prepare("SELECT valor FROM config WHERE chave = ?").bind(chave).first();
  return row ? row.valor : null;
}
async function setConfig(env, chave, valor) {
  await env.DB.prepare(
    "INSERT INTO config (chave, valor) VALUES (?, ?) ON CONFLICT(chave) DO UPDATE SET valor = excluded.valor, atualizado_em = datetime('now')"
  ).bind(chave, valor).run();
}
async function log(env, tipo, msg) {
  await env.DB.prepare("INSERT INTO tasks (tipo, para, status, titulo, saida, criada_por) VALUES (?, 'opus', 'log', ?, ?, 'worker')")
    .bind(tipo, String(msg).slice(0, 200), String(msg).slice(0, 2000)).run();
}

async function graph(method, path, tok, params = {}) {
  const body = new URLSearchParams({ ...params, access_token: tok });
  const url = method === "GET" ? `${GRAPH}/${path}?${body}` : `${GRAPH}/${path}`;
  const r = await fetch(url, method === "GET" ? {} : { method, body, headers: { "content-type": "application/x-www-form-urlencoded" } });
  let j = {};
  try { j = await r.json(); } catch { j = { error: { message: "resposta não-JSON", code: r.status } }; }
  return { ok: r.ok && !j.error, status: r.status, j };
}

// ------------------------------------------------------------------ webhook
function hex(buf) { return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join(""); }
async function assinaturaValida(secret, corpo, header) {
  if (!secret || !header || !header.startsWith("sha256=")) return false;
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const mac = hex(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(corpo)));
  const rec = header.slice(7);
  if (mac.length !== rec.length) return false;
  let d = 0; for (let i = 0; i < mac.length; i++) d |= mac.charCodeAt(i) ^ rec.charCodeAt(i);
  return d === 0;
}
async function verificarWebhook(url, env) {
  const esperado = await getConfig(env, "webhook_verify_token");
  if (url.searchParams.get("hub.mode") === "subscribe" && esperado && url.searchParams.get("hub.verify_token") === esperado && url.searchParams.get("hub.challenge")) {
    return new Response(url.searchParams.get("hub.challenge"), { status: 200 });
  }
  return new Response("forbidden", { status: 403 });
}

const RESPOSTAS = ["Te mandei no direct! 📩", "Enviado! Confere a DM 👀", "Mandei aí no privado, bom treino! 💪"];
const norm = (s) => (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toUpperCase();

async function responderComentario(env, perfil, igId, comentario, mediaId) {
  const tok = token(env, perfil);
  // acha o post e a palavra-chave
  const post = await env.DB.prepare(
    "SELECT p.video_id, v.palavra_chave, v.dm_texto FROM posts p LEFT JOIN videos v ON v.id = p.video_id WHERE p.ig_media_id = ?"
  ).bind(mediaId).first();
  if (!post || !post.palavra_chave) return "sem_palavra";
  const kw = norm(post.palavra_chave).trim();
  if (!kw || !norm(comentario.text).includes(kw)) return "nao_bateu";
  const base = (await getConfig(env, "worker_url")) || "";
  const link = `${base}/c/${perfil}/${post.video_id}?o=dm`;
  const texto = escrita(post.dm_texto || "Aqui tá o link do Brio 👇 Registre e acompanhe seus treinos de graça: {link}").replace("{link}", link);
  const dm = await graph("POST", `${igId}/messages`, tok, {
    recipient: JSON.stringify({ comment_id: comentario.id }),
    message: JSON.stringify({ text: texto }),
  });
  const pub = await graph("POST", `${comentario.id}/replies`, tok, { message: RESPOSTAS[Math.floor(Math.random() * RESPOSTAS.length)] });
  await env.DB.prepare("UPDATE dms SET status = ?, erro = ?, enviado_em = datetime('now') WHERE comment_id = ?")
    .bind(dm.ok ? "enviada" : "erro", dm.ok ? (pub.ok ? null : "publica: " + JSON.stringify(pub.j.error || {}).slice(0, 300)) : JSON.stringify(dm.j.error || {}).slice(0, 500), String(comentario.id)).run();
  return dm.ok ? "enviada" : "erro";
}

async function receberWebhook(request, env, ctx) {
  const corpo = await request.text();
  const ok = await assinaturaValida(env.META_APP_SECRET, corpo, request.headers.get("x-hub-signature-256"));
  await setConfig(env, "webhook_ultimo", JSON.stringify({ ts: new Date().toISOString(), assinatura_ok: ok, amostra: corpo.slice(0, 1200) }));
  if (!ok) return new Response("ok");
  let dados; try { dados = JSON.parse(corpo); } catch { return new Response("ok"); }
  const contas = (await env.DB.prepare("SELECT perfil, ig_user_id FROM contas").all()).results || [];
  const porId = Object.fromEntries(contas.filter((c) => c.ig_user_id).map((c) => [String(c.ig_user_id), c.perfil]));
  const tarefas = [];
  for (const entry of dados.entry || []) {
    const perfil = porId[String(entry.id)];
    for (const ch of entry.changes || []) {
      if (ch.field !== "comments" || !ch.value) continue;
      const v = ch.value;
      if (v.from && String(v.from.id) === String(entry.id)) continue; // comentário do próprio perfil
      const ins = await env.DB.prepare(
        "INSERT OR IGNORE INTO dms (comment_id, perfil, ig_media_id, palavra_chave, status) VALUES (?, ?, ?, ?, 'pendente')"
      ).bind(String(v.id), perfil || "desconhecido", v.media ? String(v.media.id) : null, (v.text || "").slice(0, 200)).run();
      if (perfil && v.media && ins.meta && ins.meta.changes) {
        tarefas.push(responderComentario(env, perfil, entry.id, v, String(v.media.id)).catch((e) => log(env, "dm_erro", e.message)));
      }
    }
  }
  if (tarefas.length) ctx.waitUntil(Promise.all(tarefas));
  return new Response("ok");
}

// ------------------------------------------------------------------ cliques e vídeo
async function clique(url, env, request) {
  const partes = url.pathname.split("/").filter(Boolean);
  const perfil = partes[1]; const video = partes[2] || "bio";
  const origem = url.searchParams.get("o") === "dm" ? "dm" : "bio";
  const site = env.SITE || "https://briotreino.app";
  if (!PERFIS.has(perfil)) return Response.redirect(site, 302);
  await env.DB.prepare("INSERT INTO cliques (perfil, video_id, origem, pais) VALUES (?, ?, ?, ?)")
    .bind(perfil, video, origem, request.cf ? request.cf.country || null : null).run();
  const d = new URL(site);
  d.searchParams.set("utm_source", "instagram"); d.searchParams.set("utm_medium", origem);
  d.searchParams.set("utm_campaign", env.CAMPANHA || "sprint_nov26"); d.searchParams.set("utm_content", `${perfil}_${video}`);
  return Response.redirect(d.toString(), 302);
}
async function video(url) {
  const nome = url.pathname.slice(3);
  if (!/^[a-z0-9_\-\/]+\.mp4$/i.test(nome)) return new Response("not found", { status: 404 });
  const r = await fetch(RAW + nome);
  if (!r.ok) return new Response("not found", { status: 404 });
  return new Response(r.body, { headers: { "content-type": "video/mp4", "cache-control": "public, max-age=3600" } });
}

// ------------------------------------------------------------------ publicador
async function publicador(env) {
  if ((await getConfig(env, "pausa_global")) === "1") return;
  const base = await getConfig(env, "worker_url");
  const contas = Object.fromEntries(((await env.DB.prepare("SELECT perfil, ig_user_id, pausado FROM contas").all()).results || []).map((c) => [c.perfil, c]));
  // 1) cria contêiner para posts que vencem nos próximos 20 min
  const novos = (await env.DB.prepare(
    "SELECT p.id, p.perfil, p.video_id, v.legenda, v.arquivo FROM posts p JOIN videos v ON v.id = p.video_id " +
    "WHERE p.status = 'agendado' AND p.agendado_para <= datetime('now', '+20 minutes') ORDER BY p.agendado_para LIMIT 4"
  ).all()).results || [];
  for (const p of novos) {
    const c = contas[p.perfil];
    if (!c || !c.ig_user_id || c.pausado) continue;
    const r = await graph("POST", `${c.ig_user_id}/media`, token(env, p.perfil), {
      media_type: "REELS", video_url: `${base}/v/${p.arquivo}`, caption: escrita(p.legenda), share_to_feed: "true",
    });
    if (r.ok) await env.DB.prepare("UPDATE posts SET status = 'contêiner', container_id = ?, erro = NULL WHERE id = ?").bind(r.j.id, p.id).run();
    else await env.DB.prepare("UPDATE posts SET status = 'erro', erro = ? WHERE id = ?").bind(JSON.stringify(r.j.error || r.j).slice(0, 500), p.id).run();
  }
  // 2) publica os contêineres prontos cujo horário chegou
  const prontos = (await env.DB.prepare(
    "SELECT id, perfil, container_id, agendado_para FROM posts WHERE status = 'contêiner' ORDER BY agendado_para LIMIT 6"
  ).all()).results || [];
  for (const p of prontos) {
    const c = contas[p.perfil]; const tok = token(env, p.perfil);
    const st = await graph("GET", p.container_id, tok, { fields: "status_code,status" });
    const code = st.j.status_code;
    if (code === "ERROR" || code === "EXPIRED") {
      await env.DB.prepare("UPDATE posts SET status = 'erro', erro = ? WHERE id = ?").bind(JSON.stringify(st.j).slice(0, 500), p.id).run();
      continue;
    }
    const venceu = await env.DB.prepare("SELECT ? <= datetime('now') AS v").bind(p.agendado_para).first();
    if (code !== "FINISHED" || !venceu.v) continue;
    const pub = await graph("POST", `${c.ig_user_id}/media_publish`, tok, { creation_id: p.container_id });
    if (pub.ok) {
      const info = await graph("GET", pub.j.id, tok, { fields: "permalink" });
      await env.DB.prepare("UPDATE posts SET status = 'publicado', ig_media_id = ?, permalink = ?, publicado_em = datetime('now') WHERE id = ?")
        .bind(pub.j.id, info.j.permalink || null, p.id).run();
    } else {
      await env.DB.prepare("UPDATE posts SET status = 'erro', erro = ? WHERE id = ?").bind(JSON.stringify(pub.j.error || pub.j).slice(0, 500), p.id).run();
    }
  }
}

// ------------------------------------------------------------------ métricas (a cada ~hora, só posts de até 7 dias)
async function metricas(env) {
  const agora = new Date();
  if (agora.getUTCMinutes() >= 5) return; // roda só na primeira passada de cada hora
  const posts = (await env.DB.prepare(
    "SELECT id, perfil, ig_media_id FROM posts WHERE status = 'publicado' AND publicado_em >= datetime('now', '-7 days') LIMIT 40"
  ).all()).results || [];
  for (const p of posts) {
    const r = await graph("GET", `${p.ig_media_id}/insights`, token(env, p.perfil), { metric: "views,reach,likes,comments,saved,shares,ig_reels_avg_watch_time" });
    if (!r.ok) continue;
    const m = Object.fromEntries((r.j.data || []).map((x) => [x.name, (x.values && x.values[0] && x.values[0].value) || 0]));
    await env.DB.prepare(
      "INSERT OR REPLACE INTO metricas (post_id, coletado_em, views, alcance, curtidas, comentarios, salvamentos, compartilhamentos, tempo_medio_ms) VALUES (?, strftime('%Y-%m-%d %H:00', 'now'), ?, ?, ?, ?, ?, ?, ?)"
    ).bind(p.id, m.views || 0, m.reach || 0, m.likes || 0, m.comments || 0, m.saved || 0, m.shares || 0, m.ig_reels_avg_watch_time || 0).run();
  }
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    try {
      if (url.pathname === "/health") return new Response("ok");
      if (url.pathname === "/webhook" && request.method === "GET") return verificarWebhook(url, env);
      if (url.pathname === "/webhook" && request.method === "POST") return receberWebhook(request, env, ctx);
      if (url.pathname.startsWith("/c/")) return clique(url, env, request);
      if (url.pathname.startsWith("/v/")) return video(url);
      return new Response("not found", { status: 404 });
    } catch (e) {
      return new Response("erro", { status: 500 });
    }
  },
  async scheduled(event, env, ctx) {
    ctx.waitUntil((async () => {
      try { await publicador(env); } catch (e) { await log(env, "publicador_erro", e.message); }
      try { await metricas(env); } catch (e) { await log(env, "metricas_erro", e.message); }
      await setConfig(env, "cron_ultimo", new Date().toISOString());
    })());
  },
};
