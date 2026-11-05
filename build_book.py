from pathlib import Path
import runpy,re,html,json
from editorial_review import revise
from book_footer import install as install_footer, CSS as footer_css
from frontpage import brand,install as install_frontpage
from unit_content import units,page,ex,summary
from unit3 import make_unit
units[3]=make_unit(page,ex,summary)
from unit4 import make_unit as make_unit4
units[4]=make_unit4(units[4],page,summary)
from unit5 import make_unit as make_unit5
units[5]=make_unit5(units[5],page,summary)
from unit6 import make_unit as make_unit6
units[6]=make_unit6(units[6],page,summary)
from units78 import make_units
units.update(make_units(page,ex,summary))
from book_order import reorder
units=reorder(units)
from unit9 import make_unit as make_unit9
units[9]=make_unit9(page,ex,summary)
from unit10 import make_unit as make_unit10
units[10]=make_unit10(page,ex,summary)
from unit11 import make_unit as make_unit11
units[11]=make_unit11(page,ex,summary)
from unit12 import make_unit as make_unit12
units[12]=make_unit12(page,ex,summary)
from units1315 import make_units as make_units1315
units.update(make_units1315(page,ex,summary))
# Only reviewed chapters belong in the current web edition.
units={n:unit for n,unit in units.items() if n in (2,3,4,5,6,7,8,9,10,11,12,13,14,15)}
root=Path(__file__).parent
# One interactive prototype in the cone example; other sections stay unchanged.
u8name,u8pages=units[8]
title,goal,body,exercises=u8pages[1]
marker='<h2>Þegar gat er í miðjunni</h2>'
body=body.replace(marker,(root/'assets/cone.html').read_text()+marker,1)
u8pages[1]=(title,goal,body,exercises)
from solid_widgets import add_widgets
u8pages=add_widgets(u8pages)
units[8]=(u8name,u8pages)
(root/'dist/sequences.js').write_text((root/'assets/sequences.js').read_text())
(root/'dist/de-advanced.js').write_text((root/'assets/de-advanced.js').read_text())
(root/'dist/exp-de.js').write_text((root/'assets/exp-de.js').read_text())
(root/'dist/de.js').write_text((root/'assets/de.js').read_text())
(root/'dist/solids.js').write_text((root/'assets/solids.js').read_text())
(root/'dist/cone.js').write_text((root/'assets/cone.js').read_text())

base=runpy.run_path(str(root/'build.py'))
original=base['html']
unitnames={1:'Stofnföll og óákveðin heildi',**{n:u[0] for n,u in units.items()}}
styles=base['css']+'''nav.book-nav{display:block;max-height:calc(100vh - 48px);overflow-y:auto;padding:0 8px 12px 0}.book-nav .nav-title{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 14px 12px}.book-nav details{border:0;padding:0;margin:5px 0}.book-nav summary{font-size:15px;line-height:1.5;font-weight:650;color:var(--ink);padding:12px;border-radius:7px}.book-nav details[open]>summary{background:var(--soft)}.book-nav details.current-unit>summary{color:var(--accent)}.book-nav .subsections{border-left:1px solid var(--line);margin:8px 0 14px 18px;padding-left:7px}.book-nav a{font-size:14px;line-height:1.5;padding:10px 12px}.book-nav a.active{background:var(--active);color:var(--ink)}@media(max-width:800px){nav.book-nav{display:block;max-height:50vh;position:static;margin-bottom:28px;padding-right:4px}.book-nav a{display:block}.book-nav summary{padding:12px}}@media print{nav.book-nav{display:none!important}}'''
styles+=' .rect-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}.rect-grid h3{margin:16px 0 10px}.rect-grid p{font-size:15px;overflow-wrap:anywhere}#riemann-values{font-weight:600}#riemann-widget input{accent-color:var(--accent)}@media(max-width:700px){.rect-grid{grid-template-columns:1fr}}'
styles+=(root/'assets/cone.css').read_text()
styles+=(root/'assets/navigation.css').read_text()
styles+=(root/'assets/frontpage.css').read_text()
styles+=footer_css
styles+='#sequence-widget button[aria-pressed=true],#induction-practice button[aria-pressed=true]{outline:3px solid var(--accent);outline-offset:3px}'
head=original.split('<style>')[0]+'<style>'+styles+'</style>'+original.split('</style>',1)[1].split('<body>',1)[0]
header=(original.split('<body>',1)[1].split('</header>',1)[0]+'</header>').replace('Prufueining · Vinnuútgáfa','Vefbók · Vinnuútgáfa')
mobile_nav = '<div class="mobile-bookbar"><button type="button" id="book-menu-toggle" aria-controls="book-drawer" aria-expanded="false" aria-haspopup="dialog"><span class="menu-symbol" aria-hidden="true">☰</span>Efnisyfirlit</button></div><dialog class="book-drawer" id="book-drawer" aria-labelledby="book-drawer-title"><div class="drawer-heading"><h2 id="book-drawer-title">Efnisyfirlit</h2><button type="button" id="book-menu-close" aria-label="Loka efnisyfirliti" autofocus>×</button></div><div class="drawer-content"></div></dialog>'
header=brand(header)
header+=mobile_nav
(root/'dist/me-logo.png').write_bytes((root/'assets/me-logo.png').read_bytes())
(root/'dist/home-geometry.png').write_bytes((root/'assets/home-geometry.png').read_bytes())
(root/'dist/navigation.js').write_text((root/'assets/navigation.js').read_text())
substitution_js="""document.querySelectorAll('[data-sub-choice]').forEach(b=>b.addEventListener('click',()=>{const messages=['Rétt. Stæðan x² verður u og allur þátturinn 2x dx verður du. Heildið verður ∫cos u du.','Afleiða x² er 2x, svo du=2x dx. Parið du=dx tekur ekki tillit til keðjureglunnar.','Afleiðan er rétt, en þetta val breytir ekki heildinu beint í þekkt grunnheildi. Prófaðu að gefa stæðunni inni í cosinus nýtt nafn.'];document.getElementById('sub-feedback').textContent=messages[Number(b.dataset.subChoice)]}));"""
substitution_js+="""document.querySelectorAll('[data-parts-choice]').forEach(b=>b.addEventListener('click',()=>{document.getElementById('parts-feedback').textContent=Number(b.dataset.partsChoice)===0?'Þetta val einfaldar dæmið. u=x gefur du=dx og v=eˣ. Nýja heildið er ∫eˣ dx, sem er grunnheildi.':'Valið er gilt en hjálpar síður hér. u=eˣ gefur du=eˣ dx og v=x²/2. Nýja heildið inniheldur x²eˣ/2 og er flóknara en upphaflega heildið.'}));"""
substitution_js+="""document.querySelectorAll('[data-fraction-choice]').forEach(b=>b.addEventListener('click',()=>{document.getElementById('fraction-feedback').textContent=Number(b.dataset.fractionChoice)===0?'Rétt. (x−1)(x+2)=x²+x−2. Formið er A/(x−1)+B/(x+2).':'Margfaldaðu svigana til að athuga valið: (x+1)(x−2)=x²−x−2. Miðliðurinn hefur rangt formerki. Prófaðu hitt valið.'}));"""
substitution_js+="""document.querySelectorAll('[data-solid-choice]').forEach(b=>b.addEventListener('click',()=>{document.getElementById('solid-feedback').textContent=Number(b.dataset.solidChoice)===0?'Rétt. Lóðrétta sneiðin er samsíða y-ás. Hún gefur hólkskel með geisla x og hæð x.':'Lárétt sneið er hornrétt á y-ás og gefur hér hringkrans með ytri geisla 2 og innri geisla y. Hólkskeljar fást með lóðréttum sneiðum.'}));"""
shared_js=original.rsplit('<script>',1)[1].split('const c=document.getElementById',1)[0]
# Only the section navigation belongs to the numbered page links.
shared_js=shared_js.replace("document.querySelectorAll('nav a')",'document.querySelectorAll(\'nav.section-nav a[href^="#"]\')')
def sidebar(n):
 out='<nav id="book-navigation" class="book-nav section-nav" aria-label="Efnisyfirlit vefbókar"><p class="nav-title">Efnisyfirlit</p>'
 out+='<a class="book-home-link" href="index.html#home">Forsíða</a>'
 for k,title in unitnames.items():
  current=k==n
  out+='<details'+(' open class="current-unit"' if current else '')+f'><summary>{k}. {title}</summary><div class="subsections">'
  chapters=base['pages'] if k==1 else units[k][1]
  for i,p in enumerate(chapters,1):
   path='' if current else ('index.html' if k==1 else f'unit-{k}.html')
   out+=f'<a href="{path}#s{i}">{k}.{i} {p[0]}</a>'
  out+='</div></details>'
 return out+'</nav>'
def connect_next_unit(markup,n):
 if n==max(unitnames): return markup
 target=f'unit-{n+1}.html#s1'
 old="document.getElementById('next').disabled=n===sections.length-1"
 assert markup.count(old)==1
 markup=markup.replace(old,"document.getElementById('next').disabled=false",1)
 old="document.getElementById('next').onclick=()=>location.hash='s'+(current+2)"
 assert markup.count(old)==1
 new="document.getElementById('next').onclick=()=>{if(current===sections.length-1)location.href="+json.dumps(target)+";else location.hash='s'+(current+2)}"
 return markup.replace(old,new,1)

def connect_previous_unit(markup,n):
 if n==1: return markup
 previous=n-1
 filename='index.html' if previous==1 else f'unit-{previous}.html'
 count=len(base['pages'] if previous==1 else units[previous][1])
 target=f'{filename}#s{count}'
 old="document.getElementById('prev').disabled=n===0"
 assert markup.count(old)==1
 markup=markup.replace(old,"document.getElementById('prev').disabled=false",1)
 old="document.getElementById('prev').onclick=()=>location.hash='s'+current"
 assert markup.count(old)==1
 new="document.getElementById('prev').onclick=()=>{if(current===0)location.href="+json.dumps(target)+";else location.hash='s'+current}"
 return markup.replace(old,new,1)

# Preserve all existing contents, exercise numbers, and deep links in unit 1.
home=original.replace('<style>'+base['css']+'</style>','<style>'+styles+'</style>')
home=re.sub(r'<nav aria-label="Efnisyfirlit einingar">.*?</nav>',lambda m:sidebar(1),home,count=1)
home=home.replace("document.querySelectorAll('nav a')", """document.querySelectorAll('nav.section-nav a[href^="#"]')""")
home=home.replace('Prufueining · Vinnuútgáfa','Vefbók · Vinnuútgáfa')
home=home.replace('</header>','</header>'+mobile_nav,1).replace('</body>','<script src="navigation.js" defer></script></body>')
home=install_frontpage(brand(home),unitnames)
(root/'dist/index.html').write_text(install_footer(connect_next_unit(revise(1,home),1)))

def reflabel(ref,n):
 path,_,hashid=ref.partition('#'); target=n
 if path:
  target=1 if path=='index.html' else int(re.search(r'unit-(\d+)',path).group(1))
 num=int(hashid[1:])
 title=(base['pages'] if target==1 else units[target][1])[num-1][0]
 return f'{target}.{num} {title}'

for n,(name,pages) in units.items():
 out=head.replace('<title>STÆR3HD05 · Stofnföll</title>',f'<title>STÆR3HD05 · {name}</title>')+'<body>'+header+'<div class="layout">'+sidebar(n)+'<main>'
 for i,(title,goal,body,exercises) in enumerate(pages,1):
  out+=f'<section id="s{i}" '+('hidden' if i>1 else '')+f'><article><div class="eyebrow">Eining {n} · {name}</div><h1>{n}.{i} {title}</h1><p class="goal"><strong>Markmið:</strong> {goal}</p>{body}'
  if exercises:out+='<h2>Æfingadæmi</h2>'
  for j,(q,h,step,a,ref) in enumerate(exercises,1):
   eid=f'ex-{n}-{i}-{j}'
   reference=f'<p>Upprifjun: <a href="{ref}">{reflabel(ref,n)}</a></p>' if title.startswith('Blandað') else ''
   out+=f'''<div class="exercise" id="{eid}"><h3>Dæmi {n}.{i}.{j}</h3><p>{q}</p><div class="helpbar"><button type="button" class="reveal" aria-expanded="false" aria-controls="{eid}-hint">Vísbending</button><span class="separator" aria-hidden="true">·</span><button type="button" class="reveal" aria-expanded="false" aria-controls="{eid}-answer">Lausn</button></div><div class="helppanel" id="{eid}-hint" hidden><p>{h}</p>{reference}<button type="button" class="morehint" aria-expanded="false" aria-controls="{eid}-step">Frekari vísbending</button><div class="nextstep" id="{eid}-step" hidden><p>{step}</p></div></div><div class="helppanel" id="{eid}-answer" hidden><p><strong>Lausn og skýring</strong></p><p>{a}</p></div></div>'''
  out+='</article></section>'
 out+='<div class="bottom"><button id="prev">← Til baka</button><button id="next">Næsta síða →</button></div></main></div><script>'+shared_js+substitution_js+'''\nconst nr=document.getElementById('rectangles');if(nr){const format=n=>new Intl.NumberFormat('en-US',{useGrouping:false,maximumFractionDigits:3}).format(n).replace('.',',');function graph(target,n,upper){const w=2/n;let rectangles='';for(let k=0;k<n;k++){const h=((k+(upper?1:0))*w)**2;const xx=55+k*w*75,yy=330-h*75;rectangles+='<rect x="'+xx+'" y="'+yy+'" width="'+(w*75)+'" height="'+(h*75)+'" fill="#dedede" stroke="#777" stroke-width="1"/>';if(n<=4)rectangles+='<text x="'+(xx+w*37.5)+'" y="'+((h<0.6?yy-8:Math.max(yy+22,40)))+'" text-anchor="middle" font-size="16" fill="black">h = '+format(h)+'</text>'}let path='';for(let k=0;k<=120;k++){const x=2*k/120;path+=(k?'L':'M')+(55+x*75)+','+(330-x*x*75)}target.innerHTML=rectangles+'<path d="M35 330H250 M55 345V15" fill="none" stroke="black"/><path d="'+path+'" fill="none" stroke="black" stroke-width="2.5"/><text x="38" y="351" fill="black">0</text><text x="200" y="351" fill="black">2</text><path d="M130 326V334 M205 326V334 M51 255H59 M51 180H59 M51 105H59 M51 30H59" stroke="black"/><text x="125" y="351" fill="black">1</text><text x="32" y="260" fill="black">1</text><text x="32" y="185" fill="black">2</text><text x="32" y="110" fill="black">3</text><text x="32" y="35" fill="black">4</text><text x="260" y="325" fill="black">x</text><text x="61" y="20" fill="black">y</text><path d="M55 368V373H'+(55+w*75)+'V368" fill="none" stroke="black"/><text x="'+(55+w*37.5)+'" y="393" text-anchor="middle" fill="black" font-size="14">breidd '+format(w)+'</text>';target.setAttribute('aria-label',(upper?'Yfirsumma':'Undirsumma')+' fyrir f(x)=x² á [0,2], '+n+' rétthyrningar, breidd '+format(w))}function drawRects(){const n=Number(nr.value),w=2/n;let lower=0,upper=0;const lo=[],hi=[];for(let k=0;k<n;k++){const a=(k*w)**2,b=((k+1)*w)**2;lower+=a*w;upper+=b*w;lo.push(a);hi.push(b)}document.getElementById('rect-count').textContent=n;document.getElementById('rect-width').textContent='Breidd hvers rétthyrnings: 2 ÷ '+n+' = '+format(w)+'.';graph(document.getElementById('lower-graph'),n,false);graph(document.getElementById('upper-graph'),n,true);document.getElementById('lower-calc').textContent=n<=6?format(w)+' × ('+lo.map(format).join(' + ')+') = '+format(lower):'Samanlagt flatarmál: '+format(lower);document.getElementById('upper-calc').textContent=n<=6?format(w)+' × ('+hi.map(format).join(' + ')+') = '+format(upper):'Samanlagt flatarmál: '+format(upper);document.getElementById('riemann-values').textContent='Undirsumma '+format(lower)+' ≤ flatarmál svæðis ≤ yfirsumma '+format(upper)+'. Bilið milli summanna er '+format(upper-lower)+(n>6?' (tölur námundaðar).':'.')}nr.addEventListener('input',drawRects);drawRects()}
const method=document.getElementById('method-practice');if(method){const methodOptions=['Einföldun og grunnreglur','Innsetning','Hlutheildun','Stofnbrot'];const cards=[['Heildi af 2x cos(x²)',1,'Innri stæðan x² hefur afleiðuna 2x. Innsetning breytir heildinu í ∫cos u du.'],['Heildi af x eˣ',2,'x einfaldast við diffrun og eˣ er auðvelt að heilda.'],['Heildi af 1/(x²−1)',3,'Nefnarinn þáttast í (x−1)(x+1), svo tvö einföld brot henta.'],['Heildi af (x²+2x)/x',0,'Brotið einfaldast í x+2 þar sem x≠0.']];cards.forEach((card,k)=>{const box=document.createElement('div');box.className='activity';const heading=document.createElement('h3');heading.textContent=card[0];box.append(heading);const opts=document.createElement('div');opts.className='activity-options';const feedback=document.createElement('p');feedback.setAttribute('role','status');methodOptions.forEach((label,i)=>{const button=document.createElement('button');button.textContent=label;button.type='button';button.addEventListener('click',()=>{feedback.textContent=(i===card[1]?'Rétt. ':'Þetta val er ekki heppilegasta leiðin hér. ')+card[2]});opts.append(button)});box.append(opts,feedback);method.append(box)})}
</script></body></html>'''
 if n==8: out=out.replace('</body>','<script src="cone.js" defer></script><script src="solids.js" defer></script></body>')
 if n==9: out=out.replace('</body>','<script src="de.js" defer></script></body>')
 if n==10: out=out.replace('</body>','<script src="exp-de.js" defer></script></body>')
 if n in (11,12): out=out.replace('</body>','<script src="de-advanced.js" defer></script></body>')
 if n in (13,14,15): out=out.replace('</body>','<script src="sequences.js" defer></script></body>')
 out=out.replace('</body>','<script src="navigation.js" defer></script></body>')
 (root/f'dist/unit-{n}.html').write_text(install_footer(connect_previous_unit(connect_next_unit(revise(n,out),n),n)))
# The About page uses the shared chrome and theme, without numbered lesson controls.
about_head=head.replace('<title>STÆR3HD05 · Stofnföll</title>','<title>Um vefbókina · STÆR3HD05</title>')
about_head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Um tilgang og uppbyggingu vefbókarinnar í STÆR3HD05 við Menntaskólann á Egilsstöðum.">',about_head,count=1)
theme_js=re.search(r'const themeToggle=.*?\n',shared_js).group(0)
about=about_head+'<body>'+header+'<div class="layout">'+sidebar(0)+'<main>'+(root/'assets/about.html').read_text()+'</main></div><script>'+theme_js+'</script><script src="navigation.js" defer></script></body></html>'
(root/'dist/about.html').write_text(about)
print('Nýjar einingar:',len(units),'Nýjar síður:',sum(len(u[1]) for u in units.values()),'Ný dæmi:',sum(len(p[3]) for u in units.values() for p in u[1]))
