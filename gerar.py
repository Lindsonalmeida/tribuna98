#!/usr/bin/env python3
# Gera o site principal do Tribuna 98 em / (sem tocar na bio da raiz).
# Método do mini site da Desentupidora SF: páginas, meta tags, JSON-LD, sitemap.
# Uso: python3 gerar.py   (na raiz do repositório)
import os

BASE = "https://tribuna98.pages.dev"
WA_PUBLICO = "https://wa.me/5598991056523"  # já é público na bio; contatos novos ficam no privado
WA_ANUNCIO = WA_PUBLICO + "?text=Ol%C3%A1%2C%20Thiago!%20Quero%20saber%20como%20anunciar%20no%20Tribuna%2098."
WA_PAUTA = WA_PUBLICO + "?text=Ol%C3%A1%2C%20Thiago!%20Vim%20pelo%20site%20e%20quero%20mandar%20uma%20pauta."

CSS = """
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

FONTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
          '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
          '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')

SECOES = [
    ("/", "Início"),
    ("/sobre/", "Sobre o Thiago"),
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
        '%s<style>%s</style>%s%s</head><body>'
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
        '<div><h4>Site</h4><a href="/">Início</a><a href="/sobre/">Sobre o Thiago</a>'
        '<a href="/editorias/">Editorias</a><a href="/anuncie/">Anuncie</a><a href="/contato/">Contato</a></div>'
        '<div><h4>Canais</h4><a href="https://www.instagram.com/tribuna98_/" target="_blank" rel="noopener">Instagram</a>'
        '<a href="https://www.youtube.com/@tribuna098" target="_blank" rel="noopener">YouTube</a>'
        '<a href="https://www.tiktok.com/@tribuna098" target="_blank" rel="noopener">TikTok</a>'
        '<a href="https://tribuna98.com.br/" target="_blank" rel="noopener">Blog (tribuna98.com.br)</a>'
        '<a href="/">Todos os canais (bio)</a></div>'
        '<div style="grid-column:1/-1"><small>© 2026 Tribuna 98 · Thiago Azevedo. Opinião assinada é separada de notícia.</small></div>'
        '</div></footer>'
    )


FIM = '</body></html>'

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
    corpo = (
        topo("/") + editorias_bar() +
        '<section class="hero"><div class="wrap grid"><div>'
        '<span class="kicker">Informação · Política · Bastidores</span>'
        '<h1>Política e dinheiro público do Maranhão, com fonte.</h1>'
        '<p class="lead">O Tribuna 98 acompanha prefeituras, licitações, deputados e eleições. Cada informação tem fonte e documento público, e quem é citado tem direito de resposta.</p>'
        '<div class="acoes"><a class="btn sol" href="#ultimas">Ver as últimas</a>'
        '<a class="btn" href="/anuncie/">Anuncie no Tribuna</a></div>'
        '</div><aside class="destaque">'
        '<span class="kicker">Quem fala com você</span>'
        '<p class="tit" style="font-family:Anton,sans-serif;color:var(--branco);text-transform:uppercase;font-size:28px;line-height:1;margin:6px 0 12px">Thiago Azevedo</p>'
        '<p>Comunicador e dono do Tribuna 98. Entrevista, apresenta e assina as matérias.</p>'
        '<p style="margin-top:14px"><a class="btn" href="/sobre/">Conhecer o Thiago</a></p>'
        '</aside></div></section>'
        '<section class="bloco" id="ultimas"><div class="wrap">'
        '<span class="kicker">Do site</span><h2>Últimas do Tribuna</h2>'
        '<div class="ultimas"><div class="lead-nt" id="lead-nt"><span class="dt">Carregando…</span></div>'
        '<div id="lista-nt"></div></div></div></section>'
        '<section class="bloco alt"><div class="wrap">'
        '<span class="kicker">Como checamos</span><h2>Fiscalização com fonte</h2>'
        '<div class="cartoes">'
        '<div class="cartao"><h3>Fonte citada</h3><p>Toda acusação ou dado vem com a fonte: documento público, contrato, portal de compras ou órgão responsável.</p></div>'
        '<div class="cartao"><h3>Direito de resposta</h3><p>Quem é citado pode responder. A resposta sai no mesmo espaço, sem corte.</p></div>'
        '<div class="cartao"><h3>Opinião separada</h3><p>Opinião é assinada e aparece como opinião. Notícia não se mistura com análise.</p></div>'
        '</div></div></section>'
        '<section class="bloco"><div class="wrap">'
        '<span class="kicker">Em números</span><h2>Onde você nos encontra</h2>'
        '<div class="numeros">'
        '<div class="num"><b>71,5 mil</b><span>seguidores no Instagram (@tribuna98_)</span></div>'
        '<div class="num"><b>2.510</b><span>publicações no Instagram</span></div>'
        '<div class="num"><b>30</b><span>entrevistas longas no YouTube</span></div>'
        '</div><p class="nota">Números de 03/11/2026, a confirmar com o Insights antes de qualquer divulgação.</p>'
        '</div></section>'
        '<section class="bloco" style="padding-top:0"><div class="wrap">'
        '<div class="faixa"><div><h2>Anuncie no Tribuna 98</h2><p>Quem lê são eleitores e cidadãos do Maranhão que acompanham a política da sua cidade.</p></div>'
        '<a class="btn sol" href="/anuncie/">Ver o mídia kit</a></div></div></section>'
        + rodape() + NEWS_JS + FIM
    )
    return cabeca(
        "Tribuna 98 · Thiago Azevedo | Política e dinheiro público do Maranhão",
        "Tribuna 98 com Thiago Azevedo: política, prefeituras, licitações e eleições do Maranhão, com fonte e documento público.",
        "/", tipo="WebSite", extra_ld=ld,
    ) + corpo


def sobre():
    corpo = (
        topo("/sobre/") +
        '<section class="pagina"><div class="wrap"><div class="cab">'
        '<span class="kicker">Sobre o Thiago</span>'
        '<h1>Thiago Azevedo</h1>'
        '<p>Comunicador e dono do Tribuna 98, um veículo de jornalismo político do Maranhão. Ele é o rosto da marca: grava, apresenta, entrevista e assina as matérias.</p>'
        '</div></div></section>'
        '<section class="bloco"><div class="wrap ultimas">'
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
        '<section class="bloco alt"><div class="wrap"><span class="kicker">Fale com a redação</span>'
        '<h2>Mande uma pauta</h2><p>Tem uma licitação, uma obra parada ou um caso que precisa de checagem? Mande a pauta pelo WhatsApp.</p>'
        '<p style="margin-top:22px"><a class="btn sol" href="%s" target="_blank" rel="noopener">Mandar pauta</a></p>'
        '</div></section>' % WA_PAUTA +
        rodape() + FIM
    )
    return cabeca(
        "Thiago Azevedo · Tribuna 98 | Quem faz o jornalismo político do Maranhão",
        "Quem é Thiago Azevedo, dono e apresentador do Tribuna 98: cobertura de prefeituras, licitações e eleições do Maranhão.",
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
        '<div class="cartao" id="%s"><span class="kicker">Editoria</span><h3>%s</h3><p>%s</p></div>' % (i, n, d)
        for i, n, d in itens
    )
    corpo = (
        topo("/editorias/") +
        '<section class="pagina"><div class="wrap"><div class="cab">'
        '<span class="kicker">Editorias</span><h1>O que cobrimos</h1>'
        '<p>Os temas do Tribuna 98, com o que cada um traz para quem mora no Maranhão.</p></div>'
        '<div class="cartoes">%s</div></div></section>' % cards +
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
        '</div></div></section>' % (WA_PAUTA, WA_ANUNCIO, WA_PUBLICO + "?text=Ol%C3%A1%2C%20Thiago!%20Quero%20exercer%20direito%20de%20resposta.") +
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
