#!/usr/bin/env python3
# Gera o site principal do Tribuna 98 em / (sem tocar na bio da raiz).
# Método do mini site da Desentupidora SF: páginas, meta tags, JSON-LD, sitemap.
# Uso: python3 gerar.py   (na raiz do repositório)
import os

BASE = "https://tribuna98.pages.dev"
WA_PUBLICO = "https://wa.me/5598991056523"  # já é público na bio; contatos novos ficam no privado
WA_ANUNCIO = WA_PUBLICO + "?text=Ol%C3%A1%2C%20Tiago!%20Quero%20saber%20como%20anunciar%20no%20Tribuna%2098."
WA_PAUTA = WA_PUBLICO + "?text=Ol%C3%A1%2C%20Tiago!%20Vim%20pelo%20site%20e%20quero%20mandar%20uma%20pauta."

CSS_BASE = """
:root{--azul:#0b3fd6;--royal:#0a2fa8;--noite:#061a5e;--fundo:#040f3a;--amarelo:#ffd400;--branco:#fff;--cinza:#b9c3e6;--linha:rgba(255,255,255,.14);--cartao:rgba(255,255,255,.06)}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--fundo)}
body{font-family:Inter,system-ui,sans-serif;color:var(--branco);background:var(--fundo);-webkit-font-smoothing:antialiased;line-height:1.55;min-width:0}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.wrap{max-width:1120px;margin:0 auto;padding:0 18px}
h1,h2,h3{font-family:Anton,Impact,sans-serif;font-weight:400;line-height:.98;letter-spacing:.005em;text-transform:uppercase}
h1{font-size:clamp(44px,8vw,96px)}
h2{font-size:clamp(30px,4.5vw,52px);margin-bottom:18px}
h3{font-size:clamp(20px,2.4vw,26px)}
p{color:var(--cinza);max-width:68ch}
.kicker{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--amarelo);margin-bottom:14px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 22px;border-radius:999px;font-weight:700;font-size:15px;border:1.5px solid var(--amarelo);color:var(--amarelo)}
.btn.sol{background:var(--amarelo);color:var(--noite)}
.btn:hover{opacity:.9}
/* topo */
header.topo{position:sticky;top:0;z-index:10;background:rgba(4,15,58,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--linha)}
header.topo .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:64px}
header.topo img{height:30px;width:auto}
nav.menu{display:flex;gap:20px;font-size:14px;font-weight:600}
nav.menu a{color:var(--cinza)}
nav.menu a.on,nav.menu a:hover{color:var(--amarelo)}
/* barra de editorias (estilo de capa de jornal) */
.editorias{border-bottom:1px solid var(--linha);background:var(--noite)}
.editorias .wrap{display:flex;gap:6px;overflow-x:auto;padding-top:12px;padding-bottom:12px;scrollbar-width:none}
.editorias a{flex:0 0 auto;font-size:13px;font-weight:700;padding:7px 14px;border-radius:999px;background:var(--cartao);color:var(--branco)}
.editorias a:hover{background:var(--amarelo);color:var(--noite)}
/* hero: manchete + bloco de fotos de capa (sem foto nova: só tipo e cor) */
.hero{padding:56px 0 40px;background:radial-gradient(120% 90% at 85% 0%,#1652ff 0%,var(--royal) 42%,var(--fundo) 100%)}
.hero .grid{display:grid;grid-template-columns:1.25fr 1fr;gap:40px;align-items:start}
.hero .lead{font-size:clamp(16px,1.6vw,19px);margin:22px 0 28px;color:#dfe6ff}
.hero .acoes{display:flex;flex-wrap:wrap;gap:12px}
.hero .destaque{background:var(--cartao);border:1px solid var(--linha);border-radius:18px;padding:22px}
.hero .destaque .tit{font-family:Anton,sans-serif;font-size:28px;line-height:1;text-transform:uppercase;margin:6px 0 12px}
/* últimas do WordPress */
.bloco{padding:56px 0}
.bloco.alt{background:var(--noite)}
.ultimas{display:grid;grid-template-columns:1.2fr 1fr;gap:28px}
.nt{display:block;padding:18px 0;border-bottom:1px solid var(--linha)}
.nt:last-child{border-bottom:0}
.nt .dt{font-size:12px;font-weight:700;letter-spacing:.12em;color:var(--amarelo);text-transform:uppercase}
.nt h3{font-size:clamp(20px,2.2vw,24px);margin-top:6px;color:var(--branco);text-transform:none;font-family:Inter,sans-serif;font-weight:700;line-height:1.25}
.nt:hover h3{color:var(--amarelo)}
.lead-nt{background:var(--cartao);border:1px solid var(--linha);border-radius:18px;padding:26px}
.lead-nt h3{font-size:clamp(26px,3.4vw,40px);text-transform:uppercase;font-family:Anton,sans-serif;font-weight:400;line-height:1;margin-top:10px}
/* números e cartões */
.numeros{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px}
.num{background:var(--cartao);border:1px solid var(--linha);border-radius:16px;padding:22px}
.num b{display:block;font-family:Anton,sans-serif;font-size:clamp(34px,4.6vw,56px);font-weight:400;color:var(--amarelo);line-height:1}
.num span{font-size:14px;color:var(--cinza)}
.nota{font-size:12px;color:var(--cinza);margin-top:12px}
.cartoes{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px}
.cartao{background:var(--cartao);border:1px solid var(--linha);border-radius:18px;padding:24px}
.cartao h3{font-size:24px;margin-bottom:10px}
.cartao p{font-size:15px}
.faixa{background:var(--amarelo);color:var(--noite);border-radius:20px;padding:34px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
.faixa h2{color:var(--noite);margin-bottom:6px;font-size:clamp(28px,4vw,44px)}
.faixa p{color:#1a2a6a}
.faixa .btn{border-color:var(--noite);color:var(--noite)}
.faixa .btn.sol{background:var(--noite);color:var(--amarelo)}
/* páginas internas */
.pagina{padding:56px 0 24px}
.pagina .cab{max-width:820px}
.pagina .cab p{font-size:clamp(16px,1.6vw,19px);margin-top:18px}
.sumario{margin-top:12px}
.sumario li{list-style:none;padding:14px 0;border-bottom:1px solid var(--linha);color:var(--cinza)}
.sumario li b{color:var(--branco)}
ul.lista{padding-left:0;list-style:none;color:var(--cinza)}
ul.lista li{padding:8px 0 8px 22px;position:relative}
ul.lista li::before{content:"";position:absolute;left:0;top:17px;width:9px;height:9px;background:var(--amarelo);border-radius:2px}
.rodape{border-top:1px solid var(--linha);padding:36px 0 44px;margin-top:40px;background:var(--noite)}
.rodape .wrap{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:28px}
.rodape h4{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--amarelo);margin-bottom:12px}
.rodape a{display:block;color:var(--cinza);font-size:14px;padding:4px 0}
.rodape a:hover{color:var(--branco)}
.rodape small{color:#8995c4;font-size:12px}
/* celular */
@media (max-width:860px){
  .hero .grid,.ultimas,.rodape .wrap{grid-template-columns:1fr}
  .numeros,.cartoes{grid-template-columns:1fr}
  nav.menu{display:none}
  .hero{padding:40px 0 30px}
}
"""

CSS = CSS_BASE + """
/* ===== camada tecnológica (v2) ===== */
body{position:relative;overflow-x:hidden}
.fx{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.fx .grade{position:absolute;inset:-40% -10% auto -10%;height:140%;background-image:linear-gradient(rgba(120,160,255,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(120,160,255,.10) 1px,transparent 1px);background-size:56px 56px;transform:perspective(900px) rotateX(58deg);transform-origin:50% 0;mask-image:linear-gradient(to bottom,#000 10%,transparent 70%);-webkit-mask-image:linear-gradient(to bottom,#000 10%,transparent 70%);animation:deslizar 22s linear infinite}
.fx .brilho{position:absolute;width:60vmax;height:60vmax;border-radius:50%;filter:blur(60px);opacity:.5}
.fx .b1{background:radial-gradient(circle,#2b6bff,transparent 60%);top:-20vmax;right:-20vmax;animation:flutuar 16s ease-in-out infinite}
.fx .b2{background:radial-gradient(circle,#ffd40055,transparent 60%);bottom:-25vmax;left:-20vmax;animation:flutuar 20s ease-in-out infinite reverse}
.fx .ruido{position:absolute;inset:0;opacity:.07;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.fx .varredura{position:absolute;left:0;right:0;height:120px;background:linear-gradient(to bottom,transparent,rgba(255,212,0,.07),transparent);animation:varrer 7s linear infinite}
@keyframes deslizar{to{background-position:0 56px,56px 0}}
@keyframes flutuar{50%{transform:translate(4vmax,3vmax) scale(1.08)}}
@keyframes varrer{from{top:-130px}to{top:100%}}
main,header,footer,section,nav{position:relative;z-index:1}
header.topo{z-index:10}
/* cabeçalho com status ao vivo */
.status{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#cfe0ff;border:1px solid rgba(255,255,255,.18);padding:7px 12px;border-radius:999px;background:rgba(255,255,255,.05);backdrop-filter:blur(6px)}
.status i{width:8px;height:8px;border-radius:50%;background:#ff3b3b;box-shadow:0 0 0 0 rgba(255,59,59,.7);animation:pulso 1.8s infinite}
@keyframes pulso{70%{box-shadow:0 0 0 10px rgba(255,59,59,0)}100%{box-shadow:0 0 0 0 rgba(255,59,59,0)}}
/* hero em camadas */
.hero{padding:64px 0 56px;background:none;overflow:hidden}
.hero .grid{grid-template-columns:1.1fr 1fr;align-items:center}
.hero h1 .amarelo{color:var(--amarelo);display:inline-block;text-shadow:0 0 40px rgba(255,212,0,.35)}
.palco{position:relative;min-height:440px}
.radar{position:absolute;right:-6%;top:-4%;width:min(92%,460px);aspect-ratio:1;opacity:.9}
.radar .anel{fill:none;stroke:rgba(140,180,255,.25);stroke-width:1}
.radar .varre{transform-origin:50% 50%;animation:girar 5s linear infinite}
.radar .ponto{fill:var(--amarelo);animation:piscar 2.4s ease-in-out infinite}
@keyframes girar{to{transform:rotate(360deg)}}
@keyframes piscar{50%{opacity:.25}}
.cartao-vidro{position:absolute;background:rgba(10,30,110,.45);border:1px solid rgba(255,255,255,.16);border-radius:18px;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 30px 60px -20px rgba(0,0,0,.6);padding:18px 20px}
.cartao-vidro.c1{left:0;top:58px;width:min(84%,380px);animation:flutuar2 9s ease-in-out infinite}
.cartao-vidro.c2{right:0;bottom:12px;width:min(70%,300px);animation:flutuar2 11s ease-in-out infinite reverse}
@keyframes flutuar2{50%{transform:translateY(-14px)}}
.cartao-vidro .k{font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--amarelo)}
.cartao-vidro .t{font-family:Inter,sans-serif;font-weight:700;font-size:17px;line-height:1.3;margin-top:8px;color:var(--branco);text-transform:none}
.onda{display:block;width:100%;height:56px;margin-top:10px}
/* faixa de temas em movimento */
.ticker{overflow:hidden;border-block:1px solid var(--linha);background:rgba(4,15,58,.7);backdrop-filter:blur(6px)}
.ticker .trilho{display:flex;gap:44px;white-space:nowrap;padding:14px 0;width:max-content;animation:correr 36s linear infinite}
.ticker span{font-family:Anton,sans-serif;font-size:22px;text-transform:uppercase;color:var(--branco);letter-spacing:.02em}
.ticker span.x{color:var(--amarelo)}
@keyframes correr{to{transform:translateX(-50%)}}
/* pipeline de checagem */
.pipe{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:30px;position:relative}
.pipe::before{content:"";position:absolute;left:6%;right:6%;top:30px;height:2px;background:linear-gradient(90deg,transparent,var(--amarelo),transparent);background-size:200% 100%;animation:fluir 3.5s linear infinite}
@keyframes fluir{from{background-position:200% 0}to{background-position:-200% 0}}
.passo{padding:0 14px;text-align:left}
.passo .no{width:60px;height:60px;border-radius:16px;display:grid;place-items:center;background:var(--noite);border:1.5px solid var(--amarelo);box-shadow:0 0 30px rgba(255,212,0,.25);position:relative;z-index:1}
.passo .no svg{width:28px;height:28px;stroke:var(--amarelo);fill:none;stroke-width:1.8}
.passo h3{font-size:22px;margin:16px 0 8px}
.passo p{font-size:14px}
.passo .n{font-size:11px;color:#8fa6e8;font-weight:700;letter-spacing:.14em;margin-bottom:4px}
/* vidro: cartões com borda em gradiente */
.vidro{position:relative;background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.02));border-radius:20px;padding:26px;border:1px solid transparent;background-clip:padding-box;transition:transform .35s ease,box-shadow .35s ease}
.vidro::before{content:"";position:absolute;inset:-1px;border-radius:21px;padding:1px;background:linear-gradient(140deg,rgba(255,212,0,.65),rgba(80,130,255,.1) 40%,rgba(80,130,255,.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
.vidro:hover{transform:translateY(-6px);box-shadow:0 26px 50px -22px rgba(11,63,214,.8)}
.painel-num{font-family:Anton,sans-serif;font-size:clamp(40px,5vw,64px);color:var(--amarelo);line-height:1;font-weight:400;font-variant-numeric:tabular-nums}
.faixa-led{position:relative;overflow:hidden}
.faixa-led::after{content:"";position:absolute;top:-50%;left:-40%;width:30%;height:200%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);transform:rotate(18deg);animation:brilhar 4.5s ease-in-out infinite}
@keyframes brilhar{0%,60%{left:-40%}100%{left:120%}}
.foto-banda{position:relative;border-radius:24px;overflow:hidden;border:1px solid var(--linha);margin:0 0 34px;box-shadow:0 40px 80px -36px rgba(0,0,0,.75)}
.foto-banda img{width:100%;height:auto;max-height:520px;object-fit:cover;display:block}
.foto-banda .legenda{position:absolute;left:18px;bottom:16px;font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;background:var(--amarelo);color:var(--noite);padding:7px 12px;border-radius:999px}
/* entrada suave das camadas */
.rev{opacity:0;transform:translateY(24px);transition:opacity .8s ease,transform .8s ease}
.rev.on{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rev{opacity:1;transform:none}}
@media (max-width:860px){
  .hero .grid{grid-template-columns:1fr}
  .palco{min-height:540px;margin-top:10px}
  .pipe{grid-template-columns:1fr 1fr;row-gap:28px}
  .pipe::before{display:none}
  .passo{padding:0}
  .cartao-vidro.c1{top:40px;width:86%}
  .cartao-vidro.c2{width:70%;bottom:-6px;right:0}
  .radar{width:100%;right:-4%;top:-12%}
  .hero{overflow:hidden}
  .palco{overflow:visible}
}
"""

FONTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
          '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
          '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')

SECOES = [
    ("/", "Início"),
    ("/sobre/", "Sobre o Tiago"),
    ("/editorias/", "Editorias"),
    ("/anuncie/", "Anuncie"),
    ("/contato/", "Contato"),
]

EDITORIAS = ["Política", "Prefeituras", "Licitações", "Eleições", "Deputados", "Bastidores"]


def cabeca(titulo, descricao, caminho, tipo="WebPage", extra_ld=""):
    url = BASE + caminho
    ld = (
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"%s",'
        '"name":"%s","description":"%s","url":"%s","inLanguage":"pt-BR",'
        '"publisher":{"@type":"NewsMediaOrganization","name":"Tribuna 98","url":"%s/",'
        '"logo":{"@type":"ImageObject","url":"%s/img/logo.png"},'
        '"sameAs":["https://www.instagram.com/tribuna98_/","https://www.youtube.com/@tribuna098","https://www.tiktok.com/@tribuna098"]}}</script>'
    ) % (tipo, titulo, descricao, url, BASE, BASE)
    return (
        '<!doctype html><html lang="pt-BR"><head>'
        '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<title>%s</title>'
        '<meta name="description" content="%s">'
        '<meta name="robots" content="index,follow">'
        '<link rel="canonical" href="%s">'
        '<meta name="theme-color" content="#061a5e">'
        '<meta property="og:type" content="website"><meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s"><meta property="og:url" content="%s">'
        '<meta property="og:image" content="%s/img/og.jpg"><meta property="og:locale" content="pt_BR">'
        '<link rel="icon" href="/img/avatar.webp">'
        '%s<style>%s</style>%s%s</head><body>'+FX_OPEN
    ) % (titulo, descricao, url, titulo, descricao, url, BASE, FONTES, CSS, ld, extra_ld)


def topo(ativo):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (c, ' class="on"' if c == ativo else "", n) for c, n in SECOES
    )
    return (
        '<header class="topo"><div class="wrap">'
        '<a href="/" aria-label="Tribuna 98 · início"><img src="/img/logo.png" alt="Tribuna 98"></a>'
        '<nav class="menu" aria-label="Principal">%s</nav>'
        '<a class="btn" href="%s" target="_blank" rel="noopener" style="padding:10px 16px;font-size:14px">WhatsApp</a>'
        '</div></header>'
    ) % (links, WA_ANUNCIO)


def editorias_bar():
    return '<nav class="editorias" aria-label="Editorias"><div class="wrap">%s</div></nav>' % "".join(
        '<a href="/editorias/#%s">%s</a>' % (e.lower(), e) for e in EDITORIAS
    )


def rodape():
    return (
        '<footer class="rodape"><div class="wrap">'
        '<div><img src="/img/logo.png" alt="Tribuna 98" style="height:34px;width:auto;margin-bottom:14px">'
        '<p style="font-size:14px">Informação, política e bastidores do Maranhão. Fiscalização com fonte e documento público.</p></div>'
        '<div><h4>Site</h4><a href="/">Início</a><a href="/sobre/">Sobre o Tiago</a>'
        '<a href="/editorias/">Editorias</a><a href="/anuncie/">Anuncie</a><a href="/contato/">Contato</a></div>'
        '<div><h4>Canais</h4><a href="https://www.instagram.com/tribuna98_/" target="_blank" rel="noopener">Instagram</a>'
        '<a href="https://www.youtube.com/@tribuna098" target="_blank" rel="noopener">YouTube</a>'
        '<a href="https://www.tiktok.com/@tribuna098" target="_blank" rel="noopener">TikTok</a>'
        '<a href="https://tribuna98.com.br/" target="_blank" rel="noopener">Blog (tribuna98.com.br)</a>'
        '<a href="/">Todos os canais (bio)</a></div>'
        '<div style="grid-column:1/-1"><small>© 2026 Tribuna 98 · Tiago Azevedo. Opinião assinada é separada de notícia.</small></div>'
        '</div></footer>'
    )


FIM = '</body></html>'
FX_OPEN = '<div class="fx" aria-hidden="true"><div class="grade"></div><div class="brilho b1"></div><div class="brilho b2"></div><div class="ruido"></div><div class="varredura"></div></div>'

NEWS_JS = """<script>
(function(){
  var lead=document.getElementById('lead-nt'), lista=document.getElementById('lista-nt');
  if(!lead||!lista)return;
  function limpa(h){var d=document.createElement('div');d.innerHTML=h;return d.textContent||'';}
  function data(s){try{return new Date(s).toLocaleDateString('pt-BR',{day:'2-digit',month:'short'}).replace('.','');}catch(e){return '';}}
  fetch('https://tribuna98.com.br/wp-json/wp/v2/posts?per_page=4&_fields=title,link,date')
  .then(function(r){return r.json();}).then(function(p){
    if(!p||!p.length)throw new Error('vazio');
    var a=p[0];
    lead.innerHTML='<span class="dt">'+data(a.date)+'</span><h3>'+limpa(a.title.rendered)+'</h3><p style="margin-top:14px"><a class="btn" href="'+a.link+'" target="_blank" rel="noopener">Ler no site</a></p>';
    lista.innerHTML=p.slice(1).map(function(x){return '<a class="nt" href="'+x.link+'" target="_blank" rel="noopener"><span class="dt">'+data(x.date)+'</span><h3>'+limpa(x.title.rendered)+'</h3></a>';}).join('');
  }).catch(function(){
    lead.innerHTML='<span class="dt">tribuna98.com.br</span><h3>Leia as últimas matérias no site</h3><p style="margin-top:14px"><a class="btn" href="https://tribuna98.com.br/" target="_blank" rel="noopener">Abrir o site</a></p>';
    lista.innerHTML='';
  });
})();
</script>"""


def home():
    ld = (
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite",'
        '"name":"Tribuna 98","url":"%s/","inLanguage":"pt-BR"}</script>'
    ) % BASE
    onda = ('<svg class="onda" viewBox="0 0 400 56" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0 28 C40 6 80 50 120 28 S200 6 240 28 S320 50 360 28 S400 6 400 28" fill="none" stroke="#ffd400" stroke-width="2"/>'
            '<path d="M0 36 C40 16 80 56 120 36 S200 16 240 36 S320 56 360 36 S400 16 400 36" fill="none" stroke="rgba(140,180,255,.6)" stroke-width="1.4"/></svg>')
    radar = ('<svg class="radar" viewBox="0 0 400 400" aria-hidden="true">'
             '<circle class="anel" cx="200" cy="200" r="190"/><circle class="anel" cx="200" cy="200" r="140"/>'
             '<circle class="anel" cx="200" cy="200" r="90"/><circle class="anel" cx="200" cy="200" r="40"/>'
             '<line x1="10" y1="200" x2="390" y2="200" stroke="rgba(140,180,255,.2)"/>'
             '<line x1="200" y1="10" x2="200" y2="390" stroke="rgba(140,180,255,.2)"/>'
             '<g class="varre"><path d="M200 200 L200 10 A190 190 0 0 1 320 52 Z" fill="rgba(255,212,0,.16)"/></g>'
             '<circle class="ponto" cx="262" cy="130" r="5"/><circle class="ponto" cx="140" cy="236" r="4" style="animation-delay:-1s"/>'
             '<circle class="ponto" cx="226" cy="282" r="5" style="animation-delay:-2s"/></svg>')
    ticker = ''.join('<span>%s</span><span class="x">✦</span>' % t for t in
                     ['Política','Prefeituras','Licitações','Eleições','Deputados','Bastidores','Fiscalização com fonte'])
    corpo = (
        topo("/") + editorias_bar() +
        '<section class="hero"><div class="wrap grid"><div class="rev">'
        '<span class="status"><i></i>Ao vivo · Maranhão</span>'
        '<h1 style="margin-top:20px">Política e <span class="amarelo">dinheiro público</span> do Maranhão, com fonte.</h1>'
        '<p class="lead">O Tribuna 98 acompanha prefeituras, licitações, deputados e eleições. Cada informação tem fonte e documento público, e quem é citado tem direito de resposta.</p>'
        '<div class="acoes"><a class="btn sol" href="#ultimas">Ver as últimas</a>'
        '<a class="btn" href="/anuncie/">Anuncie no Tribuna</a></div>'
        '</div>'
        '<div class="palco rev" style="transition-delay:.15s">' + radar +
        '<img src="/img/thiago-entrevista.webp" alt="Tiago Azevedo em entrevista, microfone à frente" '
        'style="position:absolute;inset:0 0 auto 0;width:100%;height:auto;border-radius:22px;object-fit:cover;'
        'filter:saturate(1.05) contrast(1.05);box-shadow:0 40px 80px -30px rgba(0,0,0,.7);opacity:.92;'
        'mask-image:linear-gradient(to bottom,#000 70%,transparent)" width="1280" height="761" fetchpriority="high">'
        '<div class="cartao-vidro c1"><span class="k">Acompanhe</span><p class="t" style="margin:0">Prefeituras, licitações e o que o dinheiro público está pagando</p>' + onda + '</div>'
        '<div class="cartao-vidro c2"><span class="k">Checagem</span><p class="t" style="margin:0">Fonte e documento antes da publicação</p></div>'
        '</div></div></section>'
        '<div class="ticker" aria-hidden="true"><div class="trilho">' + ticker + ticker + '</div></div>'
        '<section class="bloco" id="ultimas"><div class="wrap">'
        '<div class="rev"><span class="kicker">Do site · ao vivo</span><h2>Últimas do Tribuna</h2></div>'
        '<div class="ultimas"><div class="lead-nt vidro faixa-led rev" id="lead-nt"><span class="dt">Carregando…</span></div>'
        '<div id="lista-nt" class="rev"></div></div></div></section>'
        '<section class="bloco alt"><div class="wrap">'
        '<div class="foto-banda rev"><img src="/img/tiago-documento.webp" alt="Tiago Azevedo lendo documentos na mesa" width="1200" height="786" loading="lazy"><span class="legenda">Documento antes da manchete</span></div>'
        '<div class="rev"><span class="kicker">Como checamos</span><h2>Do fato à publicação</h2></div>'
        '<div class="pipe">'
        '<div class="passo rev"><div class="n">01</div><div class="no"><svg viewBox="0 0 24 24"><path d="M4 4h10l6 6v10H4z"/><path d="M14 4v6h6"/></svg></div><h3>Documento</h3><p>O contrato, a licitação ou a ata é encontrado e lido antes de qualquer texto.</p></div>'
        '<div class="passo rev" style="transition-delay:.1s"><div class="n">02</div><div class="no"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/></svg></div><h3>Fonte</h3><p>Toda acusação ou dado tem a origem citada: órgão, portal ou pessoa.</p></div>'
        '<div class="passo rev" style="transition-delay:.2s"><div class="n">03</div><div class="no"><svg viewBox="0 0 24 24"><path d="M5 12l4 4 10-10"/></svg></div><h3>Checagem</h3><p>Os fatos são conferidos de novo. Opinião é assinada e separada da notícia.</p></div>'
        '<div class="passo rev" style="transition-delay:.3s"><div class="n">04</div><div class="no"><svg viewBox="0 0 24 24"><path d="M4 6h16v10H8l-4 4z"/></svg></div><h3>Resposta</h3><p>Quem é citado pode responder, e a resposta sai no mesmo espaço, sem corte.</p></div>'
        '</div></div></section>'
        '<section class="bloco"><div class="wrap">'
        '<div class="rev"><span class="kicker">Em números</span><h2>Onde você nos encontra</h2></div>'
        '<div class="numeros">'
        '<div class="num vidro rev"><b class="painel-num">71,5 mil</b><span>seguidores no Instagram (@tribuna98_)</span></div>'
        '<div class="num vidro rev" style="transition-delay:.1s"><b class="painel-num">2.510</b><span>publicações no Instagram</span></div>'
        '<div class="num vidro rev" style="transition-delay:.2s"><b class="painel-num">30</b><span>entrevistas longas no YouTube</span></div>'
        '</div><p class="nota">Números de 03/11/2026, a confirmar com o Insights antes de qualquer divulgação.</p>'
        '</div></section>'
        '<section class="bloco" style="padding-top:0"><div class="wrap">'
        '<div class="faixa faixa-led rev"><div><h2>Anuncie no Tribuna 98</h2><p>Quem lê são eleitores e cidadãos do Maranhão que acompanham a política da sua cidade.</p></div>'
        '<a class="btn sol" href="/anuncie/">Ver o mídia kit</a></div></div></section>'
        + rodape() + NEWS_JS +
        '<script>(function(){var els=document.querySelectorAll(".rev");if(!("IntersectionObserver" in window)){els.forEach(function(e){e.classList.add("on")});return;}'
        'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("on");io.unobserve(e.target);}});},{threshold:.12});'
        'els.forEach(function(e){io.observe(e);});})();</script>'
        + FIM
    )
    return cabeca(
        "Tribuna 98 · Tiago Azevedo | Política e dinheiro público do Maranhão",
        "Tribuna 98 com Tiago Azevedo: política, prefeituras, licitações e eleições do Maranhão, com fonte e documento público.",
        "/", tipo="WebSite", extra_ld=ld,
    ) + corpo


def sobre():
    corpo = (
        topo("/sobre/") +
        '<section class="pagina"><div class="wrap"><div class="cab">'
        '<span class="kicker">Sobre o Tiago</span>'
        '<h1>Tiago Azevedo</h1>'
        '<p>Comunicador e dono do Tribuna 98, um veículo de jornalismo político do Maranhão. Ele é o rosto da marca: grava, apresenta, entrevista e assina as matérias.</p>'
        '</div></div></section>'
        '<section class="bloco" style="padding-top:0"><div class="wrap ultimas" style="align-items:center">''<div class="rev"><img src="/img/thiago-sobre.webp" alt="Tiago Azevedo, retrato de corpo inteiro de terno azul" width="853" height="1280" style="border-radius:22px;width:100%%;max-width:440px;height:auto;box-shadow:0 40px 80px -30px rgba(0,0,0,.7)"></div>''<div class="rev">'
        '<div><h2>O que ele faz</h2><ul class="lista">'
        '<li>Cobre prefeituras do interior e os contratos e licitações delas</li>'
        '<li>Entrevista candidatos e deputados, em vídeos longos</li>'
        '<li>Apresenta o noticiário nas redes e assina as matérias do site</li>'
        '<li>Acompanha eleições com checagem de fatos</li></ul></div>'
        '<div><h2>Como trabalha</h2><ul class="lista">'
        '<li>Busca o documento público antes de publicar</li>'
        '<li>Separa notícia de opinião, e opinião é assinada</li>'
        '<li>Dá direito de resposta a quem for citado</li>'
        '<li>Em ano de eleição, segue a legislação eleitoral em conteúdo pago e impulsionado</li></ul></div>'
        '</div></section>'
        '<section class="bloco"><div class="wrap">'
        '<div class="foto-banda rev"><img src="/img/tiago-mesa.webp" alt="Tiago Azevedo com as mãos cruzadas sobre a mesa" width="1170" height="1130" loading="lazy"><span class="legenda">Quem fiscaliza precisa ouvir os dois lados</span></div>'
        '<div class="foto-banda rev"><img src="/img/tiago-escritorio.webp" alt="Tiago Azevedo lendo em um escritório" width="1200" height="800" loading="lazy"><span class="legenda">Antes de publicar, a leitura</span></div>'
        '</div></section>'
        '<section class="bloco alt"><div class="wrap"><span class="kicker">Fale com a redação</span>'
        '<h2>Mande uma pauta</h2><p>Tem uma licitação, uma obra parada ou um caso que precisa de checagem? Mande a pauta pelo WhatsApp.</p>'
        '<p style="margin-top:22px"><a class="btn sol" href="%s" target="_blank" rel="noopener">Mandar pauta</a></p>'
        '</div></section>' % WA_PAUTA +
        rodape() + FIM
    )
    return cabeca(
        "Tiago Azevedo · Tribuna 98 | Quem faz o jornalismo político do Maranhão",
        "Quem é Tiago Azevedo, dono e apresentador do Tribuna 98: cobertura de prefeituras, licitações e eleições do Maranhão.",
        "/sobre/", tipo="AboutPage",
    ) + corpo


def editorias():
    itens = [
        ("politica", "Política", "Bastidores dos partidos, pré-candidatos e disputas no Maranhão, com entrevistas longas e checagem."),
        ("prefeituras", "Prefeituras", "Cobertura do interior: obras, decisões do executivo e cobrança do que foi prometido."),
        ("licitacoes", "Licitações", "Contratos e licitações de prefeituras, com o documento público citado no texto."),
        ("eleicoes", "Eleições", "Candidatos, agenda e propostas, com a legislação eleitoral seguida à risca."),
        ("deputados", "Deputados", "Atuação de deputados estaduais e federais do Maranhão, com votos e falas verificáveis."),
        ("bastidores", "Bastidores", "O que acontece antes da notícia: reuniões, acordos e os nomes por trás das decisões."),
    ]
    cards = "".join(
        '<div class="cartao vidro" id="%s"><span class="kicker">Editoria</span><h3>%s</h3><p>%s</p>%s</div>' % (i, n, d, '<img src="/img/thiago-bastidores.webp" alt="Tiago Azevedo de costas, olhando pela janela" width="1200" height="675" style="border-radius:14px;margin-top:16px;width:100%%;height:auto">' if i == 'bastidores' else '')
        for i, n, d in itens
    )
    corpo = (
        topo("/editorias/") +
        '<section class="pagina"><div class="wrap"><div class="cab">'
        '<span class="kicker">Editorias</span><h1>O que cobrimos</h1>'
        '<p>Os temas do Tribuna 98, com o que cada um traz para quem mora no Maranhão.</p></div>'
        '<div class="cartoes">%s</div></div></section>' % cards +
        '<section class="bloco" style="padding-bottom:0"><div class="wrap"><div class="foto-banda rev"><img src="/img/tiago-politica.webp" alt="Tiago Azevedo em frente a uma mesa de trabalho" width="822" height="1280" loading="lazy" style="max-height:620px;object-position:50% 25%"><span class="legenda">Política, na mesa de quem apura</span></div></div></section>'
        '<section class="bloco alt"><div class="wrap"><span class="kicker">Mais recentes</span>'
        '<h2>Veja no site</h2><p><a class="btn sol" href="https://tribuna98.com.br/" target="_blank" rel="noopener">Abrir o tribuna98.com.br</a></p>'
        '</div></section>' +
        rodape() + FIM
    )
    return cabeca(
        "Editorias · Tribuna 98 | Política, prefeituras, licitações e eleições",
        "Editorias do Tribuna 98: política, prefeituras, licitações, eleições, deputados e bastidores do Maranhão.",
        "/editorias/", tipo="CollectionPage",
    ) + corpo


def anuncie():
    corpo = (
        topo("/anuncie/") +
        '<section class="pagina"><div class="wrap"><div class="cab">'
        '<span class="kicker">Mídia kit</span><h1>Anuncie no Tribuna 98</h1>'
        '<p>Para quem quer falar com quem acompanha a política e as obras do Maranhão. Os valores e os formatos são passados em conversa, por WhatsApp.</p>'
        '</div></div></section>'
        '<section class="bloco" style="padding-bottom:0"><div class="wrap"><div class="foto-banda rev"><img src="/img/tiago-anuncio.webp" alt="Tiago Azevedo de terno vermelho, olhar firme" width="853" height="1280" loading="lazy" style="max-height:620px;object-position:50%% 20%%"><span class="legenda">Quem fala com quem acompanha</span></div></div></section>'
        '<section class="bloco"><div class="wrap"><span class="kicker">Quem lê</span><h2>Público</h2>'
        '<div class="cartoes">'
        '<div class="cartao"><h3>Eleitor</h3><p>Morador de São Luís e do interior que quer saber o que acontece na sua cidade.</p></div>'
        '<div class="cartao"><h3>Assessor</h3><p>Equipes de político, de vereador e de prefeitura que acompanham a repercussão.</p></div>'
        '<div class="cartao"><h3>Comércio local</h3><p>Negócios das cidades que querem aparecer para quem lê notícia da região.</p></div>'
        '</div></div></section>'
        '<section class="bloco alt"><div class="wrap"><span class="kicker">Canais</span><h2>Onde o anúncio aparece</h2>'
        '<div class="numeros">'
        '<div class="num"><b>Instagram</b><span>@tribuna98_, 71,5 mil seguidores (03/11/2026)</span></div>'
        '<div class="num"><b>YouTube</b><span>@tribuna098, entrevistas longas</span></div>'
        '<div class="num"><b>Site</b><span>tribuna98.com.br, publicações diárias</span></div>'
        '</div><p class="nota">Audiência de cada canal a confirmar com os Insights antes do envio do mídia kit.</p>'
        '</div></section>'
        '<section class="bloco"><div class="wrap"><span class="kicker">Regras</span><h2>Como anunciar</h2>'
        '<ul class="lista"><li>Conteúdo pago aparece como pago, com identificação clara</li>'
        '<li>Em período eleitoral, seguimos a legislação eleitoral</li>'
        '<li>Não publicamos anúncio que contrarie a checagem de fatos da casa</li></ul>'
        '</div></section>'
        '<section class="bloco" style="padding-top:0"><div class="wrap">'
        '<div class="faixa"><div><h2>Peça o mídia kit</h2><p>Mande o nome da empresa ou do candidato e o objetivo do anúncio.</p></div>'
        '<a class="btn sol" href="%s" target="_blank" rel="noopener">Falar no WhatsApp</a></div></div></section>' % WA_ANUNCIO +
        rodape() + FIM
    )
    return cabeca(
        "Anuncie no Tribuna 98 · Mídia kit | Maranhão",
        "Mídia kit do Tribuna 98: público de política e cidades do Maranhão, canais e regras para anunciar. Valores por WhatsApp.",
        "/anuncie/", tipo="WebPage",
    ) + corpo


def contato():
    corpo = (
        topo("/contato/") +
        '<section class="pagina"><div class="wrap"><div class="cab">'
        '<span class="kicker">Contato</span><h1>Fale com a redação</h1>'
        '<p>Pauta, denúncia com documento, direito de resposta ou anúncio: a conversa começa pelo WhatsApp.</p>'
        '</div>'
        '<div class="cartoes" style="margin-top:34px">'
        '<div class="cartao"><h3>Pauta</h3><p>Mande o caso e, se tiver, o documento público.</p>'
        '<p style="margin-top:14px"><a class="btn sol" href="%s" target="_blank" rel="noopener">Mandar pauta</a></p></div>'
        '<div class="cartao"><h3>Anúncio</h3><p>Mídia kit e formatos por conversa.</p>'
        '<p style="margin-top:14px"><a class="btn" href="%s" target="_blank" rel="noopener">Anunciar</a></p></div>'
        '<div class="cartao"><h3>Direito de resposta</h3><p>Se você foi citado, responda aqui e sua resposta sai no mesmo espaço.</p>'
        '<p style="margin-top:14px"><a class="btn" href="%s" target="_blank" rel="noopener">Responder</a></p></div>'
        '</div></div></section>' % (WA_PAUTA, WA_ANUNCIO, WA_PUBLICO + "?text=Ol%C3%A1%2C%20Tiago!%20Quero%20exercer%20direito%20de%20resposta.") +
        '<section class="bloco"><div class="wrap"><div class="foto-banda rev"><img src="/img/tiago-pauta.webp" alt="Tiago Azevedo olhando o celular, em um corredor" width="1200" height="675" loading="lazy"><span class="legenda">Mande a pauta pelo WhatsApp</span></div></div></section>'
        '<section class="bloco alt"><div class="wrap"><span class="kicker">Redes</span><h2>Siga o Tribuna 98</h2>'
        '<p><a class="btn" href="https://www.instagram.com/tribuna98_/" target="_blank" rel="noopener">Instagram</a> '
        '<a class="btn" href="https://www.youtube.com/@tribuna098" target="_blank" rel="noopener">YouTube</a> '
        '<a class="btn" href="https://www.tiktok.com/@tribuna098" target="_blank" rel="noopener">TikTok</a></p>'
        '</div></section>' +
        rodape() + FIM
    )
    return cabeca(
        "Contato · Tribuna 98 | Pauta, anúncio e direito de resposta",
        "Fale com o Tribuna 98: mande pauta, peça o mídia kit ou exerça direito de resposta pelo WhatsApp.",
        "/contato/", tipo="ContactPage",
    ) + corpo


def sitemap(paths):
    urls = "".join("<url><loc>%s%s</loc></url>" % (BASE, p) for p in paths)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n') % urls


def main():
    raiz = os.path.dirname(os.path.abspath(__file__))
    paginas = {
        "index.html": home(),
        "sobre/index.html": sobre(),
        "editorias/index.html": editorias(),
        "anuncie/index.html": anuncie(),
        "contato/index.html": contato(),
    }
    for caminho, html in paginas.items():
        destino = os.path.join(raiz, caminho)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(html)
    # sitemap: a bio da raiz continua; o site principal entra com as rotas /
    with open(os.path.join(raiz, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap(["/", "/sobre/", "/editorias/", "/anuncie/", "/contato/", "/bio/"]))
    print("ok:", ", ".join(paginas))


if __name__ == "__main__":
    main()
