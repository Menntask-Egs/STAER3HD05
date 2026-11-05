"""Book front page. Existing index.html#sN links retain their meaning."""
import re

def brand(markup):
 return re.sub(r'(<header>)<strong>(.*?)</strong>',r'\1<a class="book-brand" href="index.html#home" aria-label="ME · STÆR3HD05 — forsíða"><img class="me-logo" src="me-logo.png" width="142" height="89" alt="ME"><strong>\2</strong></a>',markup,count=1)

def contents(unitnames):
 groups=[('01','Heildi og hagnýting','Stofnföll, ákveðin heildi og flatarmál.',range(1,4)),('02','Heildunaraðferðir og rúmmál','Innsetning, hlutheildun, stofnbrot og snúðar.',range(4,9)),('03','Deildajöfnur','Lausnir, upphafsskilyrði og líkön af breytingum.',range(9,13)),('04','Runur, raðir og þrepun','Mynstur, summur og stærðfræðilegar sannanir.',range(13,16))]
 cards=''
 for number,title,description,units in groups:
  units=list(units)
  links=''.join(f'<li><a href="'+('index.html' if n==1 else f'unit-{n}.html')+f'#s1"><span>{n}.</span> {unitnames[n]}</a></li>' for n in units)
  cards+=f'<details class="home-group"><summary><span class="home-group-meta">Einingar {units[0]}–{units[-1]}</span><span class="home-group-title">{title}<span class="group-chevron" aria-hidden="true">＋</span></span><span class="home-group-description">{description}</span></summary><ol class="home-unit-list">{links}</ol></details>'
 return '''<div id="book-home" class="book-home"><article id="home">
<div class="home-hero"><div class="home-intro"><p class="eyebrow">STÆR3HD05 · Gagnvirk vefbók</p><h1>Heildun,<br>deildajöfnur,<br>runur og raðir</h1><p class="home-lead">Bókin fjallar um heildun og notkun hennar við flatarmáls- og rúmmálsreikninga.</p><p>Í framhaldinu er fjallað um deildajöfnur, runur og raðir og sannanir með stærðfræðilegri þrepun.</p><a class="home-start" href="#s1">Hefja lestur <span aria-hidden="true">→</span></a></div>
<figure class="home-figure"><img src="home-geometry.png" width="300" height="350" alt="Þríhyrningssvæði undir línunni y=x myndar keilu við snúning um x-ás."><figcaption>Frá svæði að snúði</figcaption></figure></div>
<div class="home-content"><h2>Efni bókarinnar</h2><p class="home-section-intro">Opnaðu efnisflokk til að sjá kaflana.</p><div class="home-groups">'''+cards+'''</div></div>
<div class="home-support"><h2>Í vefbókinni</h2><div class="home-features"><div><h3>Sýnidæmi</h3><p>Sýnidæmin fylgja lausn frá upphafi til enda. Skýringar tengja reikniskrefin saman og rökstyðja aðferðavalið.</p></div><div><h3>Dæmi með stuðningi</h3><p>Við dæmin má opna vísbendingar um næstu skref og skoða lausnina.</p></div><div><h3>Gagnvirkar myndir</h3><p>Með rennistikum og öðrum stillingum má skoða hvernig breyting á einni stærð hefur áhrif á aðrar.</p></div></div></div>
<p class="home-about"><a href="about.html">Um vefbókina <span aria-hidden="true">→</span></a></p>
</article></div>'''

def install(markup,unitnames):
 markup=markup.replace('<main>','<main>'+contents(unitnames),1)
 markup=markup.replace('<title>STÆR3HD05 · Stofnföll</title>','<title>STÆR3HD05 · Heildun, deildajöfnur, runur og raðir</title>')
 markup=markup.replace('Prufueining í STÆR3HD05: stofnföll, óákveðin heildi og æfingar með vísbendingum.','Gagnvirk vefbók í STÆR3HD05 um heildun, deildajöfnur, runur, raðir og þrepun.')
 # Keep the landing page outside the numbered section array so all deep links,
 # exercise numbers and next/previous chapter transitions remain unchanged.
 prefix="""const onHome=!/^#s[1-9]\\d*$/.test(location.hash);document.getElementById('book-home').hidden=!onHome;document.querySelector('.bottom').hidden=onHome;const homeLink=document.querySelector('.book-home-link');homeLink.classList.toggle('active',onHome);if(onHome)homeLink.setAttribute('aria-current','page');else homeLink.removeAttribute('aria-current');const firstUnit=document.querySelector('#book-navigation details');firstUnit.classList.toggle('current-unit',!onHome);firstUnit.open=!onHome;if(onHome){sections.forEach(s=>s.hidden=true);links.forEach(a=>{a.classList.remove('active');a.removeAttribute('aria-current')});document.title='STÆR3HD05 · Heildun, deildajöfnur, runur og raðir';window.scrollTo(0,0);return;}document.title='STÆR3HD05 · Stofnföll og óákveðin heildi';"""
 assert markup.count('function show(){')==1
 return markup.replace('function show(){','function show(){'+prefix,1)
