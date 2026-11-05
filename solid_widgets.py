import re

def widget(key,title,mode='disk',compare=False):
 formulas={
 'cylinder':r'\[V=\pi\int_0^3 2^2\,dx=12\pi\text{ cm}^3.\]',
 'washer-x':r'\[V=\pi\int_0^1(1-x^4)\,dx=\frac{4\pi}{5}.\]',
 'paraboloid-y':r'\[V=\pi\int_0^4 y\,dy=8\pi.\]',
 'washer-y':r'\[V=\pi\int_0^1((2y)^2-y^2)\,dy=\pi.\]',
 'shell-y':r'\[V=2\pi\int_0^1x(1-x^2)\,dx=\frac\pi2.\]',
 'shell-x':r'\[V=2\pi\int_0^1y\sqrt y\,dy=\frac{4\pi}{5}.\]',
 'compare-y':r'<p>Skífur:</p>\[V=\pi\int_0^1y\,dy=\frac\pi2.\]<p>Hólkaaðferð:</p>\[V=2\pi\int_0^1x(1-x^2)\,dx=\frac\pi2.\]'}
 return f'''<div class="cone-lab solid-lab" data-solid="{key}"><h2>{title}</h2><p>Skoðaðu skyggða svæðið og snúðinn sem það myndar. Færðu sneiðina til að tengja geisla og lengdir við heildið.</p><div class="cone-views"><figure><h3>Svæðið og sneiðin</h3><svg data-part="plane" viewBox="0 0 360 360" role="img" aria-label="Svæðið í tvívídd"></svg></figure><figure><h3>Snúður og {'valin sneið' if compare else 'hólkskel' if mode=='shell' else 'þversnið'}</h3><canvas data-part="space" role="img" aria-label="Þrívíður snúður">Þrívíddarmynd af snúði.</canvas></figure></div><div class="cone-controls">'''+('''<label>Aðferð <select data-part="mode"><option value="disk">Skífur / hringkransar</option><option value="shell">Hólkaaðferð</option></select></label>''' if compare else f'<input data-part="mode" type="hidden" value="{mode}">')+'''<label>Staðsetning sneiðar: <output data-part="slice-value"></output><input data-part="slice" aria-label="Staðsetning sneiðar" type="range" min="0" max="100" step="1" value="50"></label><label>Snúningur: <output data-part="angle-value">0°</output><input data-part="angle" aria-label="Snúningur svæðisins" type="range" min="0" max="360" step="1" value="0"></label><div class="cone-buttons"><button data-part="play" type="button">Spila snúning</button><button data-part="reset" type="button">Byrja upp á nýtt</button></div><details><summary>Sjónarhorn</summary><label>Snúa sjónarhorni<input data-part="yaw" type="range" min="-160" max="160" value="-35"></label><label>Horfa ofan frá<input data-part="pitch" type="range" min="10" max="75" value="25"></label><button data-part="view" type="button">Endurstilla sjónarhorn</button></details></div><div class="formula"><p data-part="readout" aria-live="polite"></p><div data-part="integral">'''+formulas[key]+'''</div><p data-part="progress"></p></div></div>'''

def add_widgets(pages):
 settings=[(0,'8.1.1','cylinder','Sívalningurinn með þversniðum','disk',False),(1,'8.2.2','washer-x','Sjáðu holrúmið myndast','disk',False),(2,'8.3.1','paraboloid-y','Skífur hornréttar á y-ás','disk',False),(2,'8.3.2','washer-y','Hringkransar um y-ás','disk',False),(3,'8.4.1','shell-y','Lóðrétt sneið verður hólkskel','shell',False),(3,'8.4.2','shell-x','Lárétt sneið verður hólkskel','shell',False),(4,'8.5.1','compare-y','Sami snúður, tvær aðferðir','disk',True)]
 for i,num,key,title,mode,compare in settings:
  heading,goal,body,ex=pages[i]
  assert '<h3>Sýnidæmi '+num in body, (i,num)
  start=body.index('<h3>Sýnidæmi '+num)
  match=re.search(r'<h[23]>',body[start+4:]);end=start+4+match.start() if match else len(body)
  body=body[:end]+widget(key,title,mode,compare)+body[end:]
  pages[i]=(heading,goal,body,ex)
 return pages
