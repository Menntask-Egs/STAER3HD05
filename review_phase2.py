"""Complete the first seven chapters' review and shared summary conventions.

Runs after review_phase1. This pass removes the old area-in-y section and
updates its navigation, section and exercise references in one build.
"""
from pathlib import Path
import re
from review_phase1 import once, section


def body(s, content):
    start = s.index('</p>', s.index('class="goal"')) + 4
    end = s.find('<h2>Æfingadæmi</h2>', start)
    if end < 0:
        end = s.index('</article>', start)
    return s[:start] + content + s[end:]


def prompt(number, q, hint, step, answer, ref, label):
    n, i, j = number.split('.')
    eid = f'ex-{n}-{i}-{j}'
    return f'''<div class="exercise" id="{eid}"><h3>Dæmi {number}</h3><p>{q}</p><div class="helpbar"><button type="button" class="reveal" aria-expanded="false" aria-controls="{eid}-hint">Vísbending</button><span class="separator" aria-hidden="true">·</span><button type="button" class="reveal" aria-expanded="false" aria-controls="{eid}-answer">Lausn</button></div><div class="helppanel" id="{eid}-hint" hidden><p>{hint}</p><p>Upprifjun: <a href="{ref}">{label}</a></p><button type="button" class="morehint" aria-expanded="false" aria-controls="{eid}-step">Frekari vísbending</button><div class="nextstep" id="{eid}-step" hidden><p>{step}</p></div></div><div class="helppanel" id="{eid}-answer" hidden><p><strong>Lausn og skýring</strong></p><p>{answer}</p></div></div>'''


def diagram_crossing():
    ox, oy, scale = 150, 355, 72
    def pt(x, y): return f'{ox+x*scale:.2f},{oy-y*scale:.2f}'
    def curve(f): return ' '.join(pt(-1+3*k/120, f(-1+3*k/120)) for k in range(121))
    shapes = ''
    for lo, hi in [(-1, 0), (0, 1), (1, 2)]:
        xs = [lo+(hi-lo)*k/40 for k in range(41)]
        shapes += '<polygon points="' + ' '.join([pt(x,x*x) for x in xs]+[pt(x,x) for x in reversed(xs)]) + '" fill="#dedede"/>'
    ticks = ''.join(f'<text x="{ox+x*scale}" y="{oy+24}" text-anchor="middle">{x}</text>' for x in [-1, 0, 1, 2])
    ticks += ''.join(f'<text x="{ox-12}" y="{oy-y*scale+5}" text-anchor="end">{y}</text>' for y in [-1, 1, 2, 3, 4])
    return f'''<figure><svg viewBox="0 0 390 470" style="max-width:450px;margin:auto" role="img" aria-label="Ferlar f(x)=x² og g(x)=x frá mínus 1 til 2. Þeir skerast við x=0 og x=1. Fleygboginn er ofar utan bilsins frá 0 til 1 og línan ofar innan þess.">{shapes}<path d="M55 {oy}H350 M{ox} 440V25" stroke="black" fill="none"/><polyline points="{curve(lambda x:x*x)}" fill="none" stroke="black" stroke-width="2.5"/><polyline points="{curve(lambda x:x)}" fill="none" stroke="black" stroke-width="2" stroke-dasharray="6 4"/>{ticks}<text x="358" y="350">x</text><text x="159" y="22">y</text><text x="230" y="52">f(x) = x²</text><text x="302" y="204">g(x) = x</text></svg><figcaption>Heil lína: f(x)=x². Brotin lína: g(x)=x.</figcaption></figure>'''


AREA_WIDGET = r'''<div class="activity area-lab" id="area-lab"><h2>Sama x-gildi, tvö fallgildi</h2><p>Færðu sneiðina. Fyrstu tvær myndirnar sýna föllin hvort í sínu lagi. Þriðja myndin sýnir svæðið milli þeirra. Lóðréttu strikin vísa á sömu staðsetningu á öllum myndunum.</p><label for="area-slice">Staðsetning sneiðar: x = <output id="area-x">1</output></label><input id="area-slice" type="range" min="0" max="2" step="0.05" value="1"><div class="area-panels"><figure><h3>f(x) = 2x</h3><svg data-area="upper" viewBox="0 0 300 430" role="img" aria-label="Ferill f(x)=2x og fallgildið við valið x"></svg></figure><figure><h3>g(x) = x²</h3><svg data-area="lower" viewBox="0 0 300 430" role="img" aria-label="Ferill g(x)=x² og fallgildið við valið x"></svg></figure><figure><h3>Svæðið milli ferlanna</h3><svg data-area="region" viewBox="0 0 300 430" role="img" aria-label="Svæði milli ferlanna og lóðrétt sneið frá g(x) til f(x)"></svg></figure></div><p id="area-readout" class="activity-feedback" role="status" aria-live="polite"></p><p>Hæð sneiðarinnar er fjarlægðin frá neðri ferlinum að þeim efri. Því er hún f(x)−g(x). Hún er núll við skurðpunktana en jákvæð á milli þeirra.</p></div>'''


CROSSING = r'''<h2>Ef ferlarnir skerast</h2><p>Skurðpunktur getur breytt því hvor ferillinn er ofar. Þá nægir ekki að nota sama mismuninn yfir allt bilið: jákvæð og neikvæð framlög gætu vegið hvort annað upp. Til að fá flatarmálið skiptum við bilinu við skurðpunktana og veljum efra fallgildið mínus það neðra á hverju hlutbili.</p><p>Skurðpunktur þýðir þó ekki alltaf að röð ferlanna breytist; þeir geta líka snert hvor annan. Við athugum því röðina á hvorri hlið.</p><h3>Sýnidæmi 3.3.2 — röð ferlanna breytist</h3><p>Finndu heildarflatarmálið milli ferla fallanna \(f(x)=x^2\) og \(g(x)=x\) á bilinu \([-1,2]\).</p>'''+diagram_crossing()+r'''<p>Fyrst finnum við öll x-gildi þar sem föllin hafa sama gildi:</p>\[x^2=x.\]\[x(x-1)=0.\]<p>Skurðpunktarnir hafa x-gildin 0 og 1. Þeir skipta bilinu í þrjá hluta:</p><ul><li>Á [−1,0] er x² ofar en x. Við x=−1/2 eru fallgildin 1/4 og −1/2.</li><li>Á [0,1] er x ofar en x². Við x=1/2 eru fallgildin 1/2 og 1/4.</li><li>Á [1,2] er x² aftur ofar. Við x=3/2 eru fallgildin 9/4 og 3/2.</li></ul><p>Reiknum flatarmál hvers hluta:</p>\[A_1=\int_{-1}^{0}(x^2-x)\,dx=\left[\frac{x^3}{3}-\frac{x^2}{2}\right]_{-1}^{0}=\frac56.\]\[A_2=\int_0^1(x-x^2)\,dx=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1=\frac16.\]\[A_3=\int_1^2(x^2-x)\,dx=\left[\frac{x^3}{3}-\frac{x^2}{2}\right]_1^2=\frac56.\]<p>Að lokum leggjum við flatarmálin saman:</p>\[A=A_1+A_2+A_3=\frac56+\frac16+\frac56=\frac{11}{6}.\]<aside>Á hverju hlutbili notum við efra fall mínus neðra fall. Við leggjum síðan saman jákvæð flatarmál, óháð því hvor ferillinn var ofar.</aside>'''


def area(text):
    text=text.replace('Velja breytu, mörk og túlkun sjálfstætt.','Velja mörk, uppskiptingu og túlkun sjálfstætt.')
    text = once(text, 'Í kafla 2 tengdum við ákveðið heildi við formerkta uppsöfnun. Nú notum við heildi til að reikna flatarmál og túlka breytingu á magni.', 'Í kafla 2 sáum við að ákveðið heildi tekur tillit til formerkis fallsins: svæði neðan x-ássins gefa neikvætt framlag. Nú notum við þessi tengsl til að reikna flatarmál og skoðum líka mismuninn á færslu og vegalengd.')
    text = once(text, 'Ef hluti svæðis er ofan x-áss og hluti neðan hans getur heildið falið í sér frádrátt. Til að finna heildarflatarmál skiptum við við núllstöðvar þar sem formerki breytist.', 'Ef fallið tekur bæði jákvæð og neikvæð gildi dragast neikvæðu framlögin frá þeim jákvæðu í ákveðna heildinu. Til að finna heildarflatarmálið skiptum við bilinu í hluta við núllstöðvar þar sem formerkið breytist. Við reiknum síðan flatarmál hvers hluta sem jákvæða tölu og leggjum niðurstöðurnar saman.')
    def between(s):
        s = re.sub(r'<figure>.*?</figure>', lambda m: AREA_WIDGET, s, count=1, flags=re.S)
        s = once(s, '<h2>Ef gröfin víxla stöðu</h2><p>Þá skiptum við bilinu við skurðpunktana og notum efra mínus neðra á hverju hlutbili. Almennt er flatarmálið heildi af |f−g|.</p>', CROSSING)
        return s
    text = section(text, 3, between)
    # Remove the entire old section, including its two exercises.
    text, count = re.subn(r'<section id="s4"(?=[\s>]).*?</section>', '', text, count=1, flags=re.S)
    assert count == 1
    def summ(s):
        s = once(s, '<li>Lóðrétt sneið gefur efra mínus neðra; lárétt sneið hægra mínus vinstra.</li>', '<li>Lóðrétt sneið milli ferla hefur hæðina efra fallgildi mínus neðra fallgildi.</li>')
        s = once(s, '<dt><a href="#s4">Lárétt sneið</a></dt><dd>Mjótt svæði með breidd R(y)−L(y).</dd>', '')
        s = once(s, r'\[A=\int_c^d(R(y)-L(y))\,dy.\]<p>Í seinni reglunni er R≥L. Föllin eru hér samfelld og mörkin í vaxandi röð.</p>', '<p>Föllin eru hér samfelld og mörkin í vaxandi röð. Ef röð ferlanna breytist er bilinu skipt og réttur mismunur notaður á hverjum hluta.</p>')
        return s
    text = section(text, 6, summ)
    def mixed(s):
        a = s.index('<div class="exercise" id="ex-3-7-3"')
        b = s.index('<div class="exercise" id="ex-3-7-4"', a)
        replacement = prompt('3.7.3', r'Finndu flatarmálið milli ferils fallsins \(f(x)=x+2\) og x-ássins á bilinu [−1,1].', 'Athugaðu hvort fallið sé jákvætt á öllu bilinu.', r'\(A=\int_{-1}^1(x+2)\,dx\).', r'\([x^2/2+2x]_{-1}^{1}=5/2-(-3/2)=4\).', '#s1', '3.1 Flatarmál og formerki')
        s = s[:a]+replacement+s[b:]
        extra = [
            (r'Finndu heildarflatarmálið milli ferla \(f(x)=x^2\) og \(g(x)=2x\) á [−1,3].', 'Finndu skurðpunktana og athugaðu hvor ferillinn er ofar á hverjum hluta.', r'Skiptu við x=0 og x=2. Reiknaðu \(\int_{-1}^0(x^2-2x)\,dx\), \(\int_0^2(2x-x^2)\,dx\) og \(\int_2^3(x^2-2x)\,dx\).', r'Hvert flatarmál er \(4/3\). Heildarflatarmálið er \(4\).', '#s3','3.3 Flatarmál milli tveggja ferla'),
            (r'Finndu flatarmálið milli ferla \(f(x)=x\) og \(g(x)=-x\) á bilinu [−2,1].', 'Röð ferlanna breytist við x=0.', r'\(A=\int_{-2}^0(-2x)\,dx+\int_0^1 2x\,dx\).', r'\(A=4+1=5\).', '#s3','3.3 Flatarmál milli tveggja ferla'),
            (r'Í geymi eru 8 L við t=0. Nettóinnrennsli er \(r(t)=2t-1\) L/mín á [0,2]. Finndu magnbreytingu og lokamagn.', 'Heildið gefur magnbreytingu þótt nettóinnrennslið skipti um formerki.', r'\(\Delta Q=\int_0^2(2t-1)\,dt=[t^2-t]_0^2\).', r'Magnbreytingin er 2 L. Lokamagnið er 8+2=10 L.', '#s5','3.5 Breyting á magni og heildarvegalengd'),
            (r'Hraði er \(v(t)=2t-4\) m/s á [0,3]. Finndu færslu og heildarvegalengd.', 'Athugaðu hvenær hraðinn skiptir um formerki.', r'Stefnubreyting verður við t=2. Færsla er \(\int_0^3v(t)\,dt\), en vegalengd er \(-\int_0^2v(t)\,dt+\int_2^3v(t)\,dt\).', r'Færsla er −3 m. Heildarvegalengd er 4+1=5 m.', '#s5','3.5 Breyting á magni og heildarvegalengd'),
        ]
        return once(s, '</article>', ''.join(prompt(f'3.7.{j}',*data) for j,data in enumerate(extra,5))+'</article>')
    return section(text, 7, mixed)


PART_STEPS = r'''<p>Við skrifum hlutheildunarregluna með afleiðum merktum með striki:</p>\[\int u(x)v'(x)\,dx=u(x)v(x)-\int u'(x)v(x)\,dx.\]<p>Hér veljum við tvo þætti: u og v′. Við diffrum u til að finna u′ og heildum v′ til að finna eitt stofnfall v. Öll föllin eru föll af x.</p><h3>Sýnidæmi 5.2.1 — hvert skref sýnt</h3><p>Reiknaðu \(\int x\cos x\,dx\).</p><h2>1. Veljum u og v′</h2><p>Við látum x vera þáttinn sem er diffraður og cos x vera þáttinn sem er heildaður:</p>\[u(x)=x.\]\[v'(x)=\cos x.\]<h2>2. Finnum u′ og v</h2>\[u'(x)=1.\]\[v(x)=\sin x.\]<p>Afleiða sin x er cos x, svo v er rétt stofnfall. Við veljum eitt stofnfall hér og tökum heildunarfastann með í lokasvarinu.</p><h2>3. Setjum inn í regluna</h2><p>Margfeldið uv er x sin x. Inni í nýja heildinu stendur u′v=1·sin x:</p>\[\int x\cos x\,dx=x\sin x-\int\sin x\,dx.\]<p>Nýja heildið er grunnheildi úr kafla 1. Þátturinn x er horfinn úr því.</p><h2>4. Heildum og einföldum</h2>\[\int\sin x\,dx=-\cos x+C.\]\[\int x\cos x\,dx=x\sin x-(-\cos x)+C.\]\[\int x\cos x\,dx=x\sin x+\cos x+C.\]<h2>5. Sannprófum með diffrun</h2>\[(x\sin x+\cos x)'=\sin x+x\cos x-\sin x=x\cos x.\]<aside>Reglan hefur mínusmerki fyrir framan nýja heildið. Plúsmerkið við cos x í lokasvarinu kemur af því að stofnfall sin x er −cos x.</aside>'''


def parts_notation(text):
    # Convert the integration-by-parts shorthand, not substitution differentials.
    text = text.replace(r'\int u\,dv=uv-\int v\,du.', r"\int u(x)v'(x)\,dx=u(x)v(x)-\int u'(x)v(x)\,dx.")
    pairs = [
        ('du og v','u′ og v'),('u og dv','u og v′'),('u, dv, du og v','u, v′, u′ og v'),
        ('u er diffrað og dv heildað til að finna v.','u er diffrað til að finna u′ og v′ heildað til að finna v.'),
        ('u og du','u og u′'),('dv og v','v′ og v'),
        ('u er þátturinn sem er diffraður; du=u′(x) dx.','u er þátturinn sem er diffraður og u′ er afleiða hans.'),
        ('dv er sá hluti sem er heildaður; v er eitt stofnfall hans.','v′ er þátturinn sem er heildaður og v er eitt stofnfall hans.'),
        ('Hér er du=u′(x) dx og dv=v′(x) dx. ','')]
    for old,new in pairs: text=text.replace(old,new)
    text=text.replace('Finna u, dv, u′ og v', 'Finna u, v′, u′ og v')
    text=text.replace(r'dv=\sin x\,dx',r'v\prime(x)=\sin x')
    text=text.replace(r'dv=e^xdx',r'v\prime(x)=e^x')
    # These finite phrases cover the authored choices, worked examples and hints.
    for old,new in [
        ('du=2x dx','u′=2x'),('du=eˣ dx','u′=eˣ'),('du=dx/x','u′=1/x'),('du=dx','u′=1'),
        ('dv=eˣdx','v′=eˣ'),('dv=eˣ dx','v′=eˣ'),('dv=cos x dx','v′=cos x'),('dv=cos xdx','v′=cos x'),
        ('dv=sin x dx','v′=sin x'),('dv=sin xdx','v′=sin x'),('dv=x²dx','v′=x²'),('dv=x dx','v′=x'),
        ('dv=dx','v′=1'),('dv = eˣ dx','v′ = eˣ'),('dv = x dx','v′ = x')]:text=text.replace(old,new)
    for old,new in [
        (r'\[du=dx.\]',r'\[u\prime(x)=1.\]'),
        (r'\[du=\frac1x\,dx.\]',r'\[u\prime(x)=\frac1x.\]'),
        (r'\[dv=\sin(2x)\,dx.\]',r'\[v\prime(x)=\sin(2x).\]'),
        (r'\[dv=1\,dx.\]',r'\[v\prime(x)=1.\]')]:text=text.replace(old,new)
    return text


def parts(text):
    text = once(text,'Rifjum hana upp:</p>',r'Rifjum hana upp fyrir tvö föll u og v:</p>\[(uv)\prime=u\prime v+uv\prime.\]<p>Við diffrun margfeldis fáum við summu tveggja liða. Til dæmis:</p>')
    text = section(text,2,lambda s:body(s,PART_STEPS))
    text = once(text,'Berum saman tvö val','Berum saman tvo valkosti')
    return parts_notation(text)


# Precompiled LaTeX: \polylongdiv[style=A]{x^2+1}{x+1} (polynom).
# Embedded vector keeps GitHub builds independent of a TeX installation.
DIVISION_SVG = r'''<svg class="division-svg" role="img" aria-labelledby="division-title" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="134.781" height="132.503" viewBox="0 0 134.781 132.503">
<title id="division-title">Ausudeiling x²+1 með x+1: kvóti x−1 og afgangur 2. Frádráttarlínur sýna −x²−x og x+1.</title>
<defs>
<g>
<g id="division-glyph-0-0">
<path d="M 6.78125 -5.828125 C 6.3125 -5.75 6.140625 -5.40625 6.140625 -5.125 C 6.140625 -4.796875 6.421875 -4.671875 6.625 -4.671875 C 7.046875 -4.671875 7.34375 -5.046875 7.34375 -5.4375 C 7.34375 -6.03125 6.65625 -6.3125 6.0625 -6.3125 C 5.1875 -6.3125 4.703125 -5.453125 4.578125 -5.171875 C 4.25 -6.25 3.359375 -6.3125 3.109375 -6.3125 C 1.640625 -6.3125 0.875 -4.4375 0.875 -4.125 C 0.875 -4.0625 0.921875 -3.984375 1.03125 -3.984375 C 1.140625 -3.984375 1.171875 -4.078125 1.203125 -4.125 C 1.6875 -5.71875 2.640625 -6.015625 3.0625 -6.015625 C 3.703125 -6.015625 3.828125 -5.421875 3.828125 -5.078125 C 3.828125 -4.765625 3.75 -4.4375 3.578125 -3.75 L 3.09375 -1.78125 C 2.875 -0.921875 2.453125 -0.140625 1.703125 -0.140625 C 1.625 -0.140625 1.265625 -0.140625 0.96875 -0.328125 C 1.484375 -0.421875 1.59375 -0.859375 1.59375 -1.03125 C 1.59375 -1.3125 1.390625 -1.484375 1.109375 -1.484375 C 0.765625 -1.484375 0.40625 -1.1875 0.40625 -0.734375 C 0.40625 -0.125 1.078125 0.140625 1.6875 0.140625 C 2.375 0.140625 2.859375 -0.40625 3.15625 -0.984375 C 3.390625 -0.140625 4.109375 0.140625 4.625 0.140625 C 6.09375 0.140625 6.859375 -1.734375 6.859375 -2.046875 C 6.859375 -2.109375 6.8125 -2.171875 6.71875 -2.171875 C 6.59375 -2.171875 6.578125 -2.109375 6.53125 -1.984375 C 6.140625 -0.734375 5.3125 -0.140625 4.671875 -0.140625 C 4.171875 -0.140625 3.90625 -0.515625 3.90625 -1.09375 C 3.90625 -1.421875 3.953125 -1.640625 4.1875 -2.59375 L 4.6875 -4.53125 C 4.90625 -5.390625 5.390625 -6.015625 6.046875 -6.015625 C 6.078125 -6.015625 6.46875 -6.015625 6.78125 -5.828125 Z M 6.78125 -5.828125 "/>
</g>
<g id="division-glyph-1-0">
<path d="M 9.421875 -3.28125 C 9.671875 -3.28125 9.921875 -3.28125 9.921875 -3.578125 C 9.921875 -3.859375 9.671875 -3.859375 9.421875 -3.859375 L 1.6875 -3.859375 C 1.4375 -3.859375 1.1875 -3.859375 1.1875 -3.578125 C 1.1875 -3.28125 1.4375 -3.28125 1.6875 -3.28125 Z M 9.421875 -3.28125 "/>
</g>
<g id="division-glyph-2-0">
<path d="M 4.125 -9.171875 C 4.125 -9.5 4.125 -9.5 3.828125 -9.5 C 3.484375 -9.125 2.78125 -8.59375 1.296875 -8.59375 L 1.296875 -8.171875 C 1.625 -8.171875 2.34375 -8.171875 3.125 -8.546875 L 3.125 -1.09375 C 3.125 -0.59375 3.09375 -0.421875 1.828125 -0.421875 L 1.390625 -0.421875 L 1.390625 0 C 1.765625 -0.03125 3.15625 -0.03125 3.625 -0.03125 C 4.109375 -0.03125 5.46875 -0.03125 5.859375 0 L 5.859375 -0.421875 L 5.421875 -0.421875 C 4.15625 -0.421875 4.125 -0.59375 4.125 -1.09375 Z M 4.125 -9.171875 "/>
</g>
<g id="division-glyph-2-1">
<path d="M 5.703125 -3.296875 L 9.65625 -3.296875 C 9.84375 -3.296875 10.109375 -3.296875 10.109375 -3.5625 C 10.109375 -3.828125 9.859375 -3.828125 9.65625 -3.828125 L 5.703125 -3.828125 L 5.703125 -7.78125 C 5.703125 -7.984375 5.703125 -8.234375 5.453125 -8.234375 C 5.171875 -8.234375 5.171875 -7.984375 5.171875 -7.78125 L 5.171875 -3.828125 L 1.234375 -3.828125 C 1.03125 -3.828125 0.765625 -3.828125 0.765625 -3.578125 C 0.765625 -3.296875 1.015625 -3.296875 1.234375 -3.296875 L 5.171875 -3.296875 L 5.171875 0.640625 C 5.171875 0.84375 5.171875 1.09375 5.4375 1.09375 C 5.703125 1.09375 5.703125 0.859375 5.703125 0.640625 Z M 5.703125 -3.296875 "/>
</g>
<g id="division-glyph-2-2">
<path d="M 4.03125 -3.5625 C 4.03125 -4.640625 3.890625 -6.421875 3.09375 -8.078125 C 2.25 -9.796875 1.078125 -10.71875 0.921875 -10.71875 C 0.859375 -10.71875 0.78125 -10.6875 0.78125 -10.609375 C 0.78125 -10.5625 0.78125 -10.53125 1.03125 -10.296875 C 2.453125 -8.84375 3.265625 -6.484375 3.265625 -3.578125 C 3.265625 -0.796875 2.59375 1.59375 0.921875 3.28125 C 0.78125 3.40625 0.78125 3.4375 0.78125 3.46875 C 0.78125 3.5625 0.859375 3.59375 0.921875 3.59375 C 1.09375 3.59375 2.265625 2.5625 2.96875 1.15625 C 3.703125 -0.296875 4.03125 -1.84375 4.03125 -3.5625 Z M 4.03125 -3.5625 "/>
</g>
<g id="division-glyph-2-3">
<path d="M 6.296875 -2.40625 L 5.96875 -2.40625 C 5.9375 -2.15625 5.8125 -1.375 5.671875 -1.140625 C 5.578125 -1.015625 4.765625 -1.015625 4.328125 -1.015625 L 1.6875 -1.015625 C 2.078125 -1.34375 2.9375 -2.265625 3.3125 -2.609375 C 5.484375 -4.609375 6.296875 -5.34375 6.296875 -6.765625 C 6.296875 -8.40625 4.984375 -9.5 3.328125 -9.5 C 1.671875 -9.5 0.703125 -8.09375 0.703125 -6.859375 C 0.703125 -6.140625 1.328125 -6.140625 1.375 -6.140625 C 1.671875 -6.140625 2.046875 -6.34375 2.046875 -6.8125 C 2.046875 -7.203125 1.765625 -7.484375 1.375 -7.484375 C 1.25 -7.484375 1.21875 -7.484375 1.171875 -7.46875 C 1.4375 -8.4375 2.21875 -9.09375 3.140625 -9.09375 C 4.359375 -9.09375 5.109375 -8.078125 5.109375 -6.765625 C 5.109375 -5.546875 4.40625 -4.484375 3.59375 -3.578125 L 0.703125 -0.34375 L 0.703125 0 L 5.921875 0 Z M 6.296875 -2.40625 "/>
</g>
<g id="division-glyph-3-0">
<path d="M 1.265625 -0.765625 L 2.3125 -1.78125 C 3.859375 -3.15625 4.453125 -3.6875 4.453125 -4.6875 C 4.453125 -5.8125 3.5625 -6.609375 2.34375 -6.609375 C 1.234375 -6.609375 0.5 -5.6875 0.5 -4.8125 C 0.5 -4.25 0.984375 -4.25 1.015625 -4.25 C 1.1875 -4.25 1.53125 -4.375 1.53125 -4.78125 C 1.53125 -5.046875 1.359375 -5.296875 1.015625 -5.296875 C 0.9375 -5.296875 0.90625 -5.296875 0.890625 -5.28125 C 1.109375 -5.9375 1.640625 -6.296875 2.21875 -6.296875 C 3.125 -6.296875 3.546875 -5.5 3.546875 -4.6875 C 3.546875 -3.890625 3.0625 -3.109375 2.515625 -2.484375 L 0.609375 -0.359375 C 0.5 -0.265625 0.5 -0.234375 0.5 0 L 4.171875 0 L 4.453125 -1.71875 L 4.203125 -1.71875 C 4.15625 -1.421875 4.09375 -0.984375 3.984375 -0.84375 C 3.921875 -0.765625 3.265625 -0.765625 3.046875 -0.765625 Z M 1.265625 -0.765625 "/>
</g>
</g>
</defs>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="94.061461" y="20.446309"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-1-0" x="105.18972" y="20.446309"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-0" x="119.482112" y="20.446309"/>
</g>
<path fill="none" stroke-width="0.398" stroke-linecap="butt" stroke-linejoin="miter" stroke="rgb(0%, 0%, 0%)" stroke-opacity="1" stroke-miterlimit="10" d="M -0.000879471 0.000556778 L 81.071607 0.000556778 " transform="matrix(0.996263, 0, 0, -0.996263, 45.711814, 26.004461)"/>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="8.082954" y="41.28913"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-1" x="19.21221" y="41.28913"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-0" x="33.270402" y="41.28913"/>
<use xlink:href="#division-glyph-2-2" x="40.268054" y="41.28913"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="63.181288" y="41.28913"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-3-0" x="71.133461" y="36.102584"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-1" x="105.42185" y="41.28913"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-0" x="119.480042" y="41.28913"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-1-0" x="48.887901" y="59.155118"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="63.181288" y="59.155118"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-3-0" x="71.133461" y="53.968572"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-1-0" x="79.76907" y="59.155118"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="94.061461" y="59.155118"/>
</g>
<path fill="none" stroke-width="0.398" stroke-linecap="butt" stroke-linejoin="miter" stroke="rgb(0%, 0%, 0%)" stroke-opacity="1" stroke-miterlimit="10" d="M -0.000879471 -0.00157997 L 56.511078 -0.00157997 " transform="matrix(0.996263, 0, 0, -0.996263, 45.711814, 64.71327)"/>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-1-0" x="79.76907" y="79.998935"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="94.061461" y="79.998935"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-1" x="105.42185" y="79.998935"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-0" x="119.480042" y="79.998935"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-0-0" x="94.061461" y="97.863926"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-1" x="105.42185" y="97.863926"/>
</g>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-0" x="119.480042" y="97.863926"/>
</g>
<path fill="none" stroke-width="0.398" stroke-linecap="butt" stroke-linejoin="miter" stroke="rgb(0%, 0%, 0%)" stroke-opacity="1" stroke-miterlimit="10" d="M 0.000770088 0.00120418 L 50.074607 0.00120418 " transform="matrix(0.996263, 0, 0, -0.996263, 76.592983, 103.423075)"/>
<g fill="rgb(0%, 0%, 0%)" fill-opacity="1">
<use xlink:href="#division-glyph-2-3" x="119.482112" y="118.707744"/>
</g>
</svg>'''

DIVISION = r'''<p>Við margliðudeilingu skrifum við teljarann sem margfeldi nefnarans og kvóta, að viðbættum afgangi:</p>\[P(x)=D(x)Q(x)+R(x).\]<p>Afgangurinn R er núll eða hefur lægra stig en nefnarinn D. Við deilum á svipaðan hátt og með venjulegri ausudeilingu: deilum fremstu liðum, margföldum, drögum frá og höldum áfram.</p><h3>Sýnidæmi 6.2.1 — ausudeiling</h3><p>Deildu \(x^2+1\) með \(x+1\) og reiknaðu síðan \(\int\frac{x^2+1}{x+1}\,dx\).</p><p>Teljarinn x²+1 hefur engan x-lið. Við höldum því sæti fyrir hann í uppsetningunni, eins og við hefðum skrifað x²+0x+1.</p><div class="division-scroll">__DIVISION_SVG__</div><p>Hver dálkur heldur utan um sama veldi af x. Í frádráttarlínunum höfum við þegar skipt um formerki á margfeldinu sem er dregið frá: fyrst stendur −x²−x og síðan +x+1. Þannig leggjast dálkarnir saman að niðurstöðunni fyrir neðan strikið.</p><h2>1. Deilum fremstu liðunum</h2>\[\frac{x^2}{x}=x.\]<p>Fyrsti liður kvótans er x. Margföldum allan nefnarann með x:</p>\[x(x+1)=x^2+x.\]<p>Drögum þetta margfeldi frá teljaranum. Svigarnir hjálpa okkur að halda utan um mínusmerkið:</p>\[(x^2+0x+1)-(x^2+x)=-x+1.\]<h2>2. Endurtökum með nýju stæðunni</h2>\[\frac{-x}{x}=-1.\]<p>Næsti liður kvótans er −1. Margföldum nefnarann með honum:</p>\[-1(x+1)=-x-1.\]<p>Drögum frá:</p>\[(-x+1)-(-x-1)=2.\]<h2>3. Lesum kvóta og afgang</h2><p>Kvótinn er x−1 og afgangurinn 2. Afgangurinn hefur stig 0, sem er lægra en stig nefnarans. Deilingunni er því lokið.</p>\[x^2+1=(x+1)(x-1)+2.\]<p>Deilum nú allri jöfnunni með x+1, þar sem x≠−1:</p>\[\frac{x^2+1}{x+1}=x-1+\frac2{x+1}.\]<aside>Afgangurinn situr áfram yfir upprunalega nefnaranum. Afgangurinn 2 verður því brotið 2/(x+1), ekki sjálfstæður fastaliður.</aside><h2>4. Heildum og athugum</h2>\[\int\frac{x^2+1}{x+1}\,dx=\int\left(x-1+\frac2{x+1}\right)\,dx.\]\[\int\frac{x^2+1}{x+1}\,dx=\frac{x^2}{2}-x+2\ln|x+1|+C.\]<p>Margföldun athugar deilinguna:</p>\[(x+1)(x-1)+2=x^2+1.\]<p>Diffrun athugar heildunina:</p>\[\left(\frac{x^2}{2}-x+2\ln|x+1|\right)'=x-1+\frac2{x+1}.\]<p>Svarið gildir á bili sem inniheldur ekki −1.</p>'''
DIVISION = DIVISION.replace('__DIVISION_SVG__', DIVISION_SVG)


def fractions(text):
    def first(s):
        a=s.index('<h2>Stig teljara og nefnara</h2>')
        b=s.index('<h2>Æfingadæmi</h2>',a)
        return s[:a]+'<details class="refresher"><summary>Upprifjun: stig teljara og nefnara</summary>'+s[a+len('<h2>Stig teljara og nefnara</h2>'):b]+'</details>'+s[b:]
    text=section(text,1,first)
    text=section(text,2,lambda s:body(s,DIVISION))
    text=once(text,'Þekkja summu einfaldra brota sem sama rætt fall.','Skrifa rætt fall sem summu einfaldari brota sem hafa sama samanlagða gildi.')
    text=text.replace('<h2>1. Samnefnum</h2>','<h2>1. Finnum samnefnara</h2>')
    text=text.replace('Samnefndu og berðu saman teljara.','Finndu samnefnara fyrir brotin og berðu saman teljarana.')
    text=text.replace('Samnefndu','Finndu samnefnara fyrir').replace('samnefndu','finndu samnefnara fyrir')
    text=text.replace('Samnefning gefur','Þegar brotin eru sett yfir sama nefnara fæst')
    return text


def methods(text):
    text=once(text,'<h2>Prófaðu að velja leið</h2><div id="method-practice"></div>',r'<h2>Prófaðu að velja leið</h2><p>Veldu þá aðferð sem þér finnst henta best sem næsta skref í hverju heildi. Smelltu á valkost til að fá rökstuðning. Sömu fjórir valkostir fylgja öllum dæmunum og þú getur breytt vali þínu.</p><div id="method-practice"></div>')
    text=once(text,'<h3>Sýnidæmi 7.3.1 — stuðull gleymist</h3>',r'<h3>Sýnidæmi 7.3.1 — stuðull gleymist</h3><p>Reiknaðu \(\int\cos(3x)\,dx\) og athugaðu hvort tillaga nemandans hér fyrir neðan sé rétt.</p>')
    text=once(text,'<h3>Sýnidæmi 7.3.2 — mínusmerki í hlutheildun</h3>',r'<h3>Sýnidæmi 7.3.2 — mínusmerki í hlutheildun</h3><p>Reiknaðu \(\int x\cos x\,dx\). Finndu fyrst villuna í útreikningi nemandans og leiðréttu hann síðan.</p>')
    return parts_notation(text)


def solids(text):
    def intro(s):
        a=s.index('<h2>Upprifjun: flatarmál með sneiðum</h2>')
        b=s.index('<h2>Nú hefur sneiðin þversniðsflatarmál</h2>',a)
        new=r'''<h2>Upprifjun: flatarmál með lóðréttum sneiðum</h2><p>Í <a href="unit-3.html#s3">kafla 3</a> reiknuðum við flatarmál milli ferla með efra fallgildi mínus neðra fallgildi. Til dæmis liggur svæðið milli y=x og y=x² í fyrsta fjórðungi frá x=0 til x=1:</p>\[A=\int_0^1(x-x^2)\,dx=\frac16.\]<p>Lóðrétt sneið hefur hæðina x−x² og litla breidd dx. Heildið leggur saman flatarmál slíkra sneiða.</p><h2 id="horizontal-slices">Ný hugmynd: láréttar sneiðar</h2><p>Við rúmmálsreikninga þurfum við stundum láréttar sneiðar, sérstaklega þegar snúið er um y-ás. Þá veljum við ákveðna hæð y og finnum x-gildið við hvorn enda sneiðarinnar.</p><p>Fyrir ferilinn y=x² hægra megin við y-ás má skrifa:</p>\[x=\sqrt y.\]<p>Til dæmis endar sneið í hæðinni y=4 við x=2. Ef hinn endinn er á y-ásnum, þar sem x=0, er lengd sneiðarinnar 2−0=2. Almennt hefur þessi sneið lengdina √y og litla þykkt dy.</p><p>Hér þurfum við ekki að reikna flatarmál með tilliti til y. Við notum x-gildin til að finna geisla eða lengd sneiðar þegar hún myndar snúð. Í <a href="#s3">8.3</a> sjáum við þetta í mynd og notum það við snúning um y-ás.</p>'''
        new=new.replace('Hér þurfum við ekki að reikna flatarmál með tilliti til y. ','')
        return s[:a]+new+s[b:]
    return section(text,1,intro)


def renumber_area(text, local):
    # Remove the obsolete sidebar entry before shifting anything.
    text=re.sub(r'<a href="(?:unit-3\.html)?#s4">3\.4 Flatarmál með tilliti til y</a>','',text)
    if local:
        text=re.sub(r'(href="#s)([5-7])(?=")',lambda m:m[1]+str(int(m[2])-1),text)
        text=re.sub(r'(id="s)([5-7])(?=")',lambda m:m[1]+str(int(m[2])-1),text)
        text=re.sub(r'(ex-3-)([5-7])-',lambda m:m[1]+str(int(m[2])-1)+'-',text)
    text=re.sub(r'(unit-3\.html#s)([5-7])\b',lambda m:m[1]+str(int(m[2])-1),text)
    # Renumber prose references only, not decimal numbers, math, SVGs or code.
    chunks=re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<svg\b.*?</svg>|\\\[.*?\\\]|\\\(.*?\\\)|<[^>]*>)',text,flags=re.S)
    for i in range(0,len(chunks),2):
        chunks[i]=re.sub(r'(?<![\d.])3\.([5-7])(?=\b|\.)',lambda m:'3.'+str(int(m[1])-1),chunks[i])
    return ''.join(chunks)


def graph_words(text):
    # Sequence plots are discrete point plots, not continuous curves.
    text=text.replace('Í grafinu eru aðeins punktar','Í punktaritinu eru aðeins punktar')
    chunks=re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<[^>]*>)',text,flags=re.S)
    special=[('að grafinu','að ferlinum'),('í gegnum punktinn','í gegnum punktinn'),('Velja graf','Velja feril'),('Skoðum nú graf','Skoðum nú feril'),('ekki graf stofnfallsins','ekki feril stofnfallsins'),('Berðu saman gröfin','Berðu saman ferlana'),('Hvaða graf','Hvaða ferill'),('Í grafverkfærinu','Í gagnvirku myndinni'),('grafið og hallann','ferilinn og hallann')]
    words={'grafsins':'ferilsins','grafs':'ferils','grafinu':'ferlinum','grafi':'ferli','grafið':'ferillinn','gröfunum':'ferlunum','gröfum':'ferlum','grafa':'ferla','gröfin':'ferlarnir','gröf':'ferlar','graf':'ferill'}
    for i in range(0,len(chunks),2):
        for a,b in special:chunks[i]=chunks[i].replace(a,b)
        def sub(m):
            new=words[m[0].lower()]
            return new.capitalize() if m[0][0].isupper() else new
        chunks[i]=re.sub(r'\b(?:'+'|'.join(words)+r')\b',sub,chunks[i],flags=re.I)
    result=''.join(chunks)
    result=result.replace('Hvar \\(f\\) er jákvætt og neikvætt?', 'Hvar er \\(f\\) jákvætt og hvar er það neikvætt?')
    return result


def clear_function_prompts(text):
    def edit(m):
        opening,q=m[1],m[2]
        def named(x):
            expr=x[2]
            if '=' in expr or expr in {'f','g','F','G','u','v','f(x)','g(x)'}:
                return x[0]
            variable='t' if re.search(r'\bt\b',expr) and 'x' not in expr else 'x'
            return x[1]+r' fallsins \(f('+variable+')='+expr+r'\)'
        q=re.sub(r'(stofnf(?:all|öll)) \\\((.*?)\\\)',named,q)
        return opening+q+'</p>'
    return re.sub(r'(<div class="exercise"[^>]*><h3>.*?</h3><p>|<p class="example-task">)(.*?)</p>',edit,text,flags=re.S)


def escape_math_angles(text):
    # Raw '<x' in a TeX inequality otherwise becomes an HTML start tag.
    chunks=re.split(r'(<script\b.*?</script>|<style\b.*?</style>)',text,flags=re.S)
    for i in range(0,len(chunks),2):
        chunks[i]=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]',lambda m:m[0].replace('<','&lt;').replace('>','&gt;'),chunks[i],flags=re.S)
    return ''.join(chunks)


def apply(root):
    root=Path(root); dist=root/'dist'
    edits={3:area,5:parts,6:fractions,7:methods,8:solids}
    for n,fn in edits.items():
        p=dist/f'unit-{n}.html';p.write_text(fn(p.read_text(encoding='utf-8')),encoding='utf-8')
    for p in dist.glob('*.html'):
        text=renumber_area(p.read_text(encoding='utf-8'),p.name=='unit-3.html')
        text=clear_function_prompts(graph_words(text))
        text=re.sub(r'((?:aria-label|alt)=")([^"]*)"',lambda m:m[1]+graph_words(m[2])+'"',text)
        text=text.replace("document.querySelectorAll('.activity').forEach(activity=>", "document.querySelectorAll('.activity[data-correct]').forEach(activity=>")
        text=text.replace('sameinum heildunarfasta í einn C','sameinum heildunarfasta í eitt C').replace('heildunarfasta saman í einn C','heildunarfasta saman í eitt C')
        # The same parts-choice handler is embedded in all numbered pages.
        text=text.replace('u=x gefur du=dx','u=x gefur u′=1').replace('u=eˣ gefur du=eˣ dx','u=eˣ gefur u′=eˣ')
        if p.name=='unit-7.html':
            a=text.index("const method=document.getElementById('method-practice');")
            b=text.index('\n</script>',a)
            text=text[:a]+text[b:]
        text=text.replace('</head>',CSS+'</head>',1)
        if p.name in ('unit-3.html','unit-7.html'):
            text=text.replace('</body>','<script src="review-interactions.js" defer></script></body>',1)
        p.write_text(text,encoding='utf-8')
    (dist/'review-interactions.js').write_text((root/'review-interactions.js').read_text(encoding='utf-8'),encoding='utf-8')
    from review_summaries import apply as apply_summaries
    apply_summaries(dist)
    for p in dist.glob('*.html'):
        p.write_text(escape_math_angles(p.read_text(encoding='utf-8')),encoding='utf-8')
    print('Review phase 2: chapters 3–7, area references and chapter 8 bridge.')


CSS='''<style>.area-panels{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.area-panels figure{margin:0}.area-panels h3{font-size:17px;margin:8px 0}.area-lab .activity-feedback{line-height:1.8}.division-scroll{overflow-x:auto;margin:28px 0;padding:20px;background:var(--surface);border:1px solid var(--line);border-radius:8px}.division-svg{display:block;width:340px;max-width:100%;height:auto;margin:0 auto;background:#fff;color:#000;border-radius:4px}.method-card h3{font-size:22px;margin:0 0 18px}.method-card .method-integral{font-size:1.12em}.method-card .activity-options button{background:var(--soft);color:var(--ink);border-color:var(--line);font-size:16px;min-height:48px}.method-card .activity-options button[aria-pressed=true]{outline:3px solid var(--accent);outline-offset:2px}.method-card .activity-feedback:empty{display:none}.method-reset{background:transparent;color:var(--accent);font-size:15px;padding:6px 12px}.method-reset[hidden]{display:none}@media(max-width:700px){.area-panels{grid-template-columns:1fr}.area-panels svg{max-width:300px;margin:auto}.area-panels h3{text-align:center}.method-card .activity-options{display:grid;grid-template-columns:1fr 1fr}.division-scroll{padding:12px}}@media(max-width:420px){.method-card .activity-options{grid-template-columns:1fr}}</style>'''
