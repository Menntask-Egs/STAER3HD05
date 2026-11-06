"""First review pass, applied after the existing book build.

Exact anchors make changes fail visibly if the underlying text changes.
No page anchors or exercise IDs are renumbered in this pass.
"""
from pathlib import Path
import re


def once(text, old, new):
    assert text.count(old) == 1, (old[:100], text.count(old))
    return text.replace(old, new, 1)


def section(text, number, edit):
    pattern = rf'<section id="s{number}"(?=[\s>]).*?</section>'
    text, count = re.subn(pattern, lambda m: edit(m[0]), text, flags=re.S)
    assert count == 1, number
    return text


def exercise(number, question, hint, step, answer, ref):
    eid = 'ex-2-8-' + str(number)
    return f'''<div class="exercise" id="{eid}"><h3>Dæmi 2.8.{number}</h3><p>{question}</p>
<div class="helpbar"><button type="button" class="reveal" aria-expanded="false" aria-controls="{eid}-hint">Vísbending</button><span class="separator" aria-hidden="true">·</span><button type="button" class="reveal" aria-expanded="false" aria-controls="{eid}-answer">Lausn</button></div>
<div class="helppanel" id="{eid}-hint" hidden><p>{hint}</p><p>Upprifjun: <a href="#s{ref}">2.{ref}</a></p><button type="button" class="morehint" aria-expanded="false" aria-controls="{eid}-step">Frekari vísbending</button><div class="nextstep" id="{eid}-step" hidden><p>{step}</p></div></div>
<div class="helppanel" id="{eid}-answer" hidden><p><strong>Lausn og skýring</strong></p><p>{answer}</p></div></div>'''


SIGNED = r'''<p>Í 2.2 nálguðum við flatarmál með rétthyrningum fyrir fall sem var ofan x-ássins. Nú skoðum við líka föll sem taka neikvæð gildi. Þá þurfum við að greina á milli <strong>flatarmáls</strong> og <strong>ákveðins heildis</strong>.</p>
<h2>Táknmál ákveðins heildis</h2>
\[\int_a^b f(x)\,dx.\]
<p>Táknunin segir að heildað sé frá \(x=a\) til \(x=b\). Tölurnar \(a\) og \(b\) kallast heildunarmörk og \(dx\) segir að heildað sé með tilliti til x. Ákveðið heildi er tala, en óákveðið heildi lýsir fjölskyldu stofnfalla.</p>
<p>Fyrir samfellt, óneikvætt fall á bili þar sem \(a&lt;b\) er ákveðna heildið flatarmál svæðisins milli ferilsins og x-ássins. Ef fallið tekur líka neikvæð gildi þarf að taka tillit til formerkjanna.</p>
<h3>Sýnidæmi 2.3.1 — tvö svæði við x-ásinn</h3>
<p>Finndu ákveðna heildið \(\int_{-1}^{1}x\,dx\) og heildarflatarmál svæðanna milli ferils fallsins \(f(x)=x\) og x-ássins á sama bili. Hér má nota rúmfræði.</p>
<svg viewBox="0 0 510 370" style="max-width:600px;margin:24px auto" role="img" aria-labelledby="signed-title signed-desc">
<title id="signed-title">Jákvætt og neikvætt framlag heildis fallsins f(x)=x</title>
<desc id="signed-desc">Tveir þríhyrningar með grunnlínu 1 og hæð 1. Á bilinu frá mínus 1 til 0 er fallið neikvætt og framlag heildisins mínus einn hálfur. Á bilinu frá 0 til 1 er það jákvætt og framlagið einn hálfur. Flatarmál hvors svæðis er einn hálfur.</desc>
<polygon points="120,185 250,185 120,315" fill="#dedede"/>
<polygon points="250,185 380,185 380,55" fill="#dedede"/>
<path d="M50 185H465 M250 345V20" fill="none" stroke="black" stroke-width="1.5"/>
<path d="M105 330L395 40" stroke="black" stroke-width="2.5"/>
<path d="M120 185V315 M380 185V55" stroke="#777" stroke-dasharray="5 5"/>
<path d="M120 180V190 M380 180V190 M245 55H255 M245 315H255" stroke="black"/>
<g fill="black" font-size="17"><text x="111" y="211">−1</text><text x="373" y="211">1</text><text x="232" y="207">0</text><text x="226" y="61">1</text><text x="216" y="321">−1</text><text x="470" y="179">x</text><text x="258" y="26">y</text><text x="381" y="39">f(x) = x</text><text x="45" y="248">Framlag: −½</text><text x="310" y="150">Framlag: +½</text></g></svg>
<p>Hvor þríhyrningur hefur grunnlínuna 1 og hæðina 1. Flatarmál hvors þeirra er því:</p>
\[A=\frac12\cdot1\cdot1=\frac12.\]
<p>Á vinstri hlutanum er \(f(x)&lt;0\), svo framlag hans til heildisins er \(-\tfrac12\). Á hægri hlutanum er \(f(x)&gt;0\), svo framlagið er \(+\tfrac12\). Framlögin vega því hvort annað upp:</p>
\[\int_{-1}^{1}x\,dx=-\frac12+\frac12=0.\]
<p>Til að finna heildarflatarmálið leggjum við hins vegar saman stærðir beggja svæða:</p>
\[A_{\text{alls}}=\frac12+\frac12=1.\]
<h2>Hvers vegna verður framlagið neikvætt?</h2>
<p>Þegar rétthyrningasumma er notuð til að nálga heildi er hvert framlag <strong>fallgildi sinnum bilbreidd</strong>. Fyrir \(a&lt;b\) er bilbreiddin jákvæð. Ofan x-ássins er fallgildið jákvætt og margfeldið því jákvætt. Neðan x-ássins er fallgildið neikvætt og margfeldið því neikvætt.</p>
<p>Til dæmis gefur fallgildið \(-0{,}5\) og bilbreiddin \(0{,}2\) framlagið \(-0{,}1\) til summunnar. Flatarmál rétthyrningsins er samt \(0{,}1\): rúmfræðilega hæðin er fjarlægð frá x-ásnum og er því jákvæð.</p>
<aside><strong>Flatarmál er aldrei neikvætt.</strong> Fyrir \(a&lt;b\) er ákveðið heildi flatarmálið ofan x-ássins mínus flatarmálið neðan hans. Formerkið tilheyrir framlaginu til heildisins, ekki flatarmálinu sjálfu.</aside>
<p>Heildi getur því verið núll þótt svæðin milli ferilsins og x-ássins hafi jákvætt flatarmál. Í kafla 3 reiknum við slík flatarmál með heildun.</p>'''


RULES = r'''<p>Hér eru helstu reglur um fasta stuðla, summur og heildunarmörk. Gert er ráð fyrir að heildin séu til á viðkomandi bilum.</p>
<h2>Fastur stuðull</h2>
\[\int_a^b c f(x)\,dx=c\int_a^b f(x)\,dx.\]
<p>Hér er c fasti. Margföldun allra fallgilda með c margfaldar hvert framlag til heildisins með sama fasta. Því má taka c út fyrir heildistáknið.</p>
<h2>Summa tveggja falla</h2>
\[\int_a^b\bigl(f(x)+g(x)\bigr)\,dx=\int_a^b f(x)\,dx+\int_a^b g(x)\,dx.\]
<p>Heilda má lið fyrir lið og leggja niðurstöðurnar saman. Sama gildir um mismun: mínusmerki helst þegar heildinu er skipt upp.</p>
<h2>Sömu mörk</h2>
\[\int_a^a f(x)\,dx=0.\]
<p>Þegar bæði mörkin eru a hefur bilið enga lengd. Ekkert framlag safnast því saman og heildið er núll.</p>
<h2>Viðsnúin mörk</h2>
\[\int_b^a f(x)\,dx=-\int_a^b f(x)\,dx.\]
<p>Ef skipt er á heildunarmörkunum breytist formerki heildisins. Þetta sést líka á stofnfalli: F(a)−F(b) er andstæð tala við F(b)−F(a).</p>
<h2>Uppskipting bils</h2>
\[\int_a^b f(x)\,dx=\int_a^c f(x)\,dx+\int_c^b f(x)\,dx.\]
<p>Hér er \(a\le c\le b\). Heildi yfir allt bilið fæst með því að leggja saman heildin yfir hlutabilin tvö. Framlög neðan x-áss halda neikvæðu formerki sínu í báðum hlutum.</p>'''


SUMMARY = r'''<h2>Að velja leið</h2>
<ol><li><strong>Skoða bilið og formerkið.</strong> Eru mörkin í vaxandi röð? Er fallið ofan eða neðan x-ássins, eða hvort tveggja?</li><li><strong>Greina hvað er spurt um.</strong> Á að finna ákveðið heildi, flatarmál, magnbreytingu eða lokamagn?</li><li><strong>Velja útreikning.</strong> Einfalt svæði má stundum reikna með rúmfræði. Annars finnum við stofnfall. Rétthyrningar gefa nálgun.</li><li><strong>Reikna bæði fallgildin.</strong> Setja mörkin inn í stofnfallið og draga neðra fallgildið frá því efra.</li><li><strong>Túlka svarið.</strong> Athuga formerki, stærð og einingar. Bæta upphafsmagni við ef spurt er um lokamagn.</li></ol>
<h2>Skref fyrir skref</h2>
<p>Reiknum \(\int_1^3 2x\,dx\). Stofnfall er \(F(x)=x^2\).</p>
\[\int_1^3 2x\,dx=\left[x^2\right]_1^3.\]
\[F(3)=3^2=9.\]
\[F(1)=1^2=1.\]
\[\int_1^3 2x\,dx=9-1=8.\]
<p>Fallið er jákvætt á bilinu og mörkin í vaxandi röð. Jákvætt svar passar því við mynd svæðisins.</p>
<h2>Ég get…</h2>
<ul class="checklist"><li>tengt <a href="#s1">mismun á stofnfallsgildum við flatarmál</a>;</li><li>fundið <a href="#s2">undir- og yfirsummur</a> í einföldum dæmum;</li><li>lesið <a href="#s3">heildunarmörk og útskýrt formerki heildis</a>;</li><li>notað <a href="#s4">höfuðsetningu heildareiknings</a>;</li><li>beitt <a href="#s5">reglum um stuðla, summur og mörk</a>;</li><li>greint <a href="#s6">magnbreytingu frá lokamagni</a> og athugað einingar.</li></ul>
<p><a class="summary-link" href="#s8">Halda áfram í blandað dæmasafn →</a></p>'''


def revise_first(text):
    text = once(text, 'Á samfelldu bili eru öll stofnföll sama falls frábrugðin hvert öðru um fasta.', r'Ef F og G eru stofnföll sama falls á einu bili, þá er mismunurinn F(x)−G(x) fasti á öllu bilinu. Því má fá öll stofnföllin með því að bæta fasta við eitt þeirra: \(F(x)+C\).')
    text = once(text, 'Á bili eru stofnföll sama falls frábrugðin hvert öðru um fasta. Fastinn', 'Stofnföll sama falls á einu bili eru aðeins ólík um fastalið. Fastinn')
    text = once(text, 'Í \\(\\int6x\\,dx\\) er 6x fallið sem við þekkjum fyrir fram.', r'Í heildinu \(\int6x\,dx\) er fallið \(f(x)=6x\) gefið. Við leitum að falli sem hefur afleiðuna 6x.')
    text = once(text, 'Diffrun lækkar veldisvísi um einn. Við heildun hækkum við hann um einn og deilum með nýja veldisvísinum:', r'Við diffrun veldis margföldum við með veldisvísinum og lækkum hann síðan um einn: \((x^n)\prime=nx^{n-1}\). Við heildun förum við í öfuga átt: hækkum veldisvísinn um einn og deilum með nýja veldisvísinum. Þannig verður stuðullinn aftur réttur þegar svarið er diffrað:')
    intro = r'''<h2>Fastan stuðul má taka út fyrir heildi</h2><p>Ef c er fasti má heilda fallið fyrst og margfalda stofnfallið síðan með c:</p>
\[\int c f(x)\,dx=c\int f(x)\,dx.\]
<p>Þetta byggir á því að fastur stuðull heldur sér við diffrun. Til dæmis er stofnfall 3f(x) þrisvar sinnum stofnfall f(x).</p>
<h2>Summu má heilda lið fyrir lið</h2>
\[\int\bigl(f(x)+g(x)\bigr)\,dx=\int f(x)\,dx+\int g(x)\,dx.\]
<p>Við finnum stofnfall hvors liðar og leggjum þau saman. Sama gildir um frádrátt: mínusmerkið helst.</p>
<h2>Reglurnar saman</h2><p>Þegar a og b eru fastar má sameina reglurnar:</p>'''
    text = once(text, '<p>Við getum heildað summu lið fyrir lið og dregið fasta stuðla út fyrir heildi:</p>', intro)
    text = text.replace('sameinum heildunarfasta í einn C.', 'sameinum heildunarfasta í eitt C.')
    text = text.replace('Plusmerkið fyrir framan', 'Formerkið fyrir framan')
    text = once(text, r'Við höldum okkur hér við grunnföll. Föll eins og \(e^{2x}\) og \(\sin(3x)\) fá sérstaka umfjöllun með innsetningu.', r'Hér notum við reglurnar fyrir grunnföllin. Fjallað verður um stofnföll falla eins og \(e^{2x}\) og \(\sin(3x)\) í <a href="unit-4.html#s2">kafla 4 um innsetningu</a>.')
    text = once(text, 'Þetta er einfalt dæmi um deildajöfnu með upphafsskilyrði.', 'Þetta kallast deildajafna með upphafsskilyrði. Við kynnum deildajöfnur í <a href="unit-9.html#s1">kafla 9</a>; hér snýst verkefnið eingöngu um að finna stofnfall og nota gefið fallgildi til að velja fastann.')
    text = once(text, r' Þegar \(x=0\) þarf samt að setja inn í allt fallið; \(C\) er ekki alltaf jafnt upphafsgildinu. Til dæmis gefur \(F(x)=e^x+C\) gildið \(F(0)=1+C\).</p>', r'</p><aside><strong>Fastinn C og upphafsgildið eru ekki alltaf sama talan.</strong> Þegar \(x=0\) er sett inn þarf að reikna alla liði fallsins. Til dæmis gefur \(F(x)=e^x+C\) gildið \(F(0)=1+C\), því \(e^0=1\).</aside>')
    text = text.replace('Línuleikareglur — summur og fastir stuðlar:', 'Summur og fastir stuðlar:')
    def new_example(s):
        for old, new in [
            (r'Reiknaðu \(\int 2t\,dt\).', r'Reiknaðu \(\int 6t\,dt\).'),
            ('Heildunarbreytan er t.', 'Leitaðu að falli af t sem hefur afleiðuna 6t.'),
            (r'Afleiða \(t^2\) með tilliti til t er \(2t\).', r'Afleiða \(At^2\) er \(2At\). Veldu A þannig að 2A=6.'),
            (r'\(t^2+C\).', r'\(3t^2+C\), því afleiðan með tilliti til t er 6t.')]:
            s = once(s, old, new)
        return s
    text = section(text, 3, new_example)
    # Only change exercise prompts, never answers, mathematics in scripts or IDs.
    def clear_prompt(m):
        prefix, q = m[1], m[2]
        q = re.sub(r'(Finndu (?:eitt |þrjú )?stofnf(?:all|öll)) \\\((.*?)\\\)', lambda x: x[1] + r' fallsins \(f(x)=' + x[2] + r'\)', q)
        q = q.replace(r'stofnfall \(2x\)', r'stofnfall fallsins \(f(x)=2x\)')
        q = q.replace(r'stofnfall \(x^3\)', r'stofnfall fallsins \(f(x)=x^3\)')
        return prefix + q + '</p>'
    text = re.sub(r'(<div class="exercise"[^>]*><h3>.*?</h3><p>)(.*?)</p>', clear_prompt, text, flags=re.S)
    return text


def revise_second(text):
    def signed(s):
        start = s.index('</p>', s.index('class="goal"')) + 4
        stop = s.index('<h2>Æfingadæmi</h2>')
        return s[:start] + SIGNED + s[stop:]
    text = section(text, 3, signed)
    text = once(text, 'tengir uppsöfnun og stofnföll.', 'tengir ákveðið heildi við stofnföll. Fyrir óneikvætt fall gefur hún okkur leið til að reikna flatarmál undir ferlinum án þess að leggja saman sífellt fleiri rétthyrninga. Ef fallið tekur líka neikvæð gildi reiknum við heildið með sömu reglu og túlkunin er þá eins og í 2.3.')
    text = once(text, r'\[\int_a^b f(x)\,dx=F(b)-F(a)=\left[F(x)\right]_a^b.\]', r'\[\int_a^b f(x)\,dx=\left[F(x)\right]_a^b=F(b)-F(a).\]')
    def rules(s):
        start = s.index('</p>', s.index('class="goal"')) + 4
        stop = s.index('<h3>Sýnidæmi')
        return s[:start] + RULES + s[stop:]
    text = section(text, 5, rules)
    text = text.replace('Notaðu línuleika;', 'Notaðu reglurnar um summur og fasta stuðla;')
    def summary(s):
        s = s.replace('Ákveðið heildi er tala sem lýsir formerktri uppsöfnun.', 'Fyrir a&lt;b er ákveðið heildi flatarmálið ofan x-ássins mínus flatarmálið neðan hans.')
        s = s.replace('Formerkt uppsöfnun á tilteknu bili.', 'Tala sem fæst sem markgildi rétthyrningasumma. Fyrir a&lt;b dragast framlög neðan x-ássins frá framlögum ofan hans.')
        s = s.replace(r'\[\int_a^b f(x)\,dx=F(b)-F(a).\]', r'\[\int_a^b f(x)\,dx=\left[F(x)\right]_a^b=F(b)-F(a).\]')
        return once(s, '</article>', SUMMARY + '</article>')
    text = section(text, 7, summary)
    additions = [
        (r'Reiknaðu \(\int_3^{-1}2x\,dx\) og útskýrðu formerki svarsins.', 'Stofnfall er x². Gættu að röð markanna.', r'\([x^2]_3^{-1}=(-1)^2-3^2\).', r'\(-8\). Heildið frá −1 til 3 er 8; viðsnúningur markanna breytir formerkinu.', 5),
        (r'Ferill fallsins \(f(x)=-3\) er skoðaður frá x=0 til x=2. Finndu heildið og flatarmál svæðisins milli ferilsins og x-ássins.', 'Teiknaðu lárétta línu og greindu flatarmál frá framlagi til heildisins.', 'Rétthyrningurinn hefur breiddina 2 og hæðina 3.', r'\(\int_0^2(-3)\,dx=-6\), en flatarmálið er 6.', 3),
        (r'Gefið er \(\int_0^2 f(x)\,dx=3\) og \(\int_2^5 f(x)\,dx=7\). Finndu \(\int_0^5 2f(x)\,dx\).', 'Skiptu bilinu við 2 og taktu fasta stuðulinn út fyrir.', r'\(2\left(\int_0^2f(x)\,dx+\int_2^5f(x)\,dx\right)\).', r'\(2(3+7)=20\).', 5),
        (r'Í geymi eru 15 L þegar t=0. Nettóhraði er \(r(t)=2t-4\) L/mín fyrstu tvær mínúturnar. Finndu magnbreytinguna og lokamagnið.', 'Heildið gefur breytinguna. Upphafsmagnið þarf að leggja við.', r'\(\int_0^2(2t-4)\,dt=[t^2-4t]_0^2=-4\).', 'Magnið minnkar um 4 L. Lokamagnið er 15−4=11 L.', 6),
        (r'Nemandi skrifar \(\int_1^2x^2\,dx=2^3/3=8/3\). Hvað vantar? Reiknaðu rétt svar.', 'Setja þarf bæði mörkin inn í stofnfallið.', r'Neðra fallgildið er \(1^3/3=1/3\).', r'Rétt svar er \(8/3-1/3=7/3\). Nemandi gleymdi að draga neðra fallgildið frá.', 4),
    ]
    def mixed(s):
        html = ''.join(exercise(j, *values) for j, values in enumerate(additions, 6))
        return once(s, '</article>', html + '</article>')
    return section(text, 8, mixed)


def terminology(text):
    forms = {'einingarinnar':'kaflans', 'eininganna':'kaflanna', 'einingunum':'köflunum'}
    # Leave code, formulas, SVGs, filenames and IDs untouched.
    chunks = re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<svg\b.*?</svg>|\\\[.*?\\\]|\\\(.*?\\\)|<[^>]*>)', text, flags=re.S)
    for i in range(0, len(chunks), 2):
        def word(m):
            original = m[0]
            replacement = forms[original.lower()]
            return replacement.capitalize() if original[0].isupper() else replacement
        chunks[i] = re.sub(r'\b(?:' + '|'.join(forms) + r')\b', word, chunks[i], flags=re.I)
        numbered = {'eining':'kafli', 'einingu':'kafla', 'einingar':'kaflar'}
        chunks[i] = re.sub(r'\b(eining|einingu|einingar)(?= \d)', lambda m: numbered[m[0].lower()].capitalize() if m[0][0].isupper() else numbered[m[0]], chunks[i], flags=re.I)
        for old,new in [('þessari einingu','þessum kafla'),('viðkomandi einingum','viðkomandi köflum'),('fyrri einingum','fyrri köflum'),('Hver eining hefur','Hver kafli hefur')]:
            chunks[i] = chunks[i].replace(old,new)
    text = ''.join(chunks)
    text = text.replace('Prufueining í STÆR3HD05: stofnföll, óákveðin heildi og æfingar með vísbendingum.','Gagnvirk vefbók í STÆR3HD05 um heildun, deildajöfnur, runur, raðir og þrepun.')
    return text.replace('efni kaflarinnar', 'efni kaflans').replace('Prufueining · Vinnuútgáfa', 'Vefbók').replace('Vefbók · Vinnuútgáfa', 'Vefbók')


def apply(root):
    dist = Path(root) / 'dist'
    first = dist / 'index.html'
    first.write_text(revise_first(first.read_text(encoding='utf-8')), encoding='utf-8')
    second = dist / 'unit-2.html'
    second.write_text(revise_second(second.read_text(encoding='utf-8')), encoding='utf-8')
    text = first.read_text(encoding='utf-8')
    text = once(text, 'Lausnir, upphafsskilyrði og líkön af breytingum.', 'Lausnir deildajafna, upphafsskilyrði og hagnýt viðfangsefni.')
    text = once(text, '</div></div>\n<p class="home-about">', '<div><h3>Samantektir</h3><p>Í lok hvers kafla eru aðalatriði, orðalisti og formúlur dregin saman. Tenglar vísa aftur í viðeigandi umfjöllun.</p></div></div></div>\n<p class="home-about">')
    first.write_text(text, encoding='utf-8')
    about = dist / 'about.html'
    text = about.read_text(encoding='utf-8')
    text = once(text, '<h2>Vinnuútgáfa</h2>\n<p>Efnið er enn í þróun. Texti, dæmi og gagnvirkar myndir verða endurskoðuð eftir því sem reynsla fæst af notkun bókarinnar.</p>', '<h2>Endurskoðun og ábendingar</h2>\n<p>Vefbókin verður endurskoðuð eftir því sem reynsla fæst af notkun hennar. Texti, dæmi og gagnvirkar myndir geta því breyst, til dæmis til að skýra erfið atriði, leiðrétta villur eða bæta framsetningu.</p>\n<p>Ábendingar um efnið, orðalag eða virkni síðunnar má senda á <a href="mailto:elin.asa@me.is">elin.asa@me.is</a>. Gott er að tilgreina kafla og dæmanúmer og láta fylgja hlekk á viðkomandi síðu.</p>')
    about.write_text(text, encoding='utf-8')
    for path in dist.glob('*.html'):
        text = terminology(path.read_text(encoding='utf-8'))
        path.write_text(text, encoding='utf-8')
    print('Review phase 1: general text, chapters 1–2; anchors and existing IDs retained.')
