"""Shared end-of-chapter structure, with chapter-specific learning content."""
from pathlib import Path
import re


# Each entry supplies an ordered method, a short calculation, linked self-checks,
# and common mistakes only if the existing summary has none.
CONTENT={
1: ([('Einfaldaðu heildisstofninn.', 'Skrifaðu rætur og brot sem veldi ef það hjálpar.'),('Veldu grunnreglu.', 'Heilda má summu lið fyrir lið.'),('Bættu við C og athugaðu.', 'Diffraðu svarið; notaðu upphafsskilyrði ef það er gefið.')],r'<p>Reiknum \(\int6x^2\,dx\). Tökum fasta stuðulinn út fyrir og notum veldisregluna:</p>\[\int6x^2\,dx=6\cdot\frac{x^3}{3}+C=2x^3+C.\]<p>Athugum með diffrun:</p>\[(2x^3+C)\prime=6x^2.\]',[],[]),
3: ([('Teiknaðu svæðið og finndu mörkin.', 'Finndu núllstöðvar eða skurðpunkta eftir því hvað afmarkar svæðið.'),('Athugaðu formerki og röð ferla.', 'Skiptu bilinu ef fall skiptir um formerki eða ef röð ferlanna breytist.'),('Reiknaðu hvern hluta.', 'Fyrir flatarmál milli ferla er heildað efra fall mínus neðra fall.'),('Leggðu saman og túlkaðu.', 'Flatarmál er óneikvætt. Í hreyfingu þarf að greina færslu frá vegalengd.')],r'<p>Finndu flatarmálið milli y=x og y=x². Skurðpunktar hafa x-gildin 0 og 1 og x≥x² þar á milli:</p>\[A=\int_0^1(x-x^2)\,dx.\]\[A=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1=\frac12-\frac13=\frac16.\]<p>Ef bilið nær út fyrir þessa skurðpunkta þarf að athuga röð ferlanna á ný.</p>',[(1,'greint á milli ákveðins heildis og flatarmáls'),(2,'skipt bili við formerkjaskipti'),(3,'reiknað flatarmál milli ferla og skipt við skurðpunkta'),(4,'greint magnbreytingu frá lokamagni og færslu frá vegalengd')],['Að nota ákveðið heildi sem flatarmál þótt fallið taki neikvæð gildi.','Að velja alltaf sama fallið sem efra fall án þess að athuga röð ferlanna.','Að rugla saman færslu og heildarvegalengd.']),
4: ([('Veldu nýja breytu.', 'Leitaðu að innri stæðu og afleiðu hennar.'),('Umritaðu alla þætti.', 'Notaðu du/dx til að finna hvernig dx og meðfylgjandi þættir breytast.'),('Heildaðu í nýju breytunni.', 'Í óákveðnu heildi er x-stæðan sett aftur inn; í ákveðnu heildi þarf að samræma breytu og mörk.'),('Athugaðu með diffrun.', 'Gættu sérstaklega að föstum stuðli frá keðjureglunni.')],r'<p>Reiknum \(\int2x(x^2+1)^2\,dx\). Veljum u=x²+1 og notum du/dx=2x:</p>\[du=2x\,dx.\]\[\int2x(x^2+1)^2\,dx=\int u^2\,du=\frac{u^3}{3}+C.\]\[\int2x(x^2+1)^2\,dx=\frac{(x^2+1)^3}{3}+C.\]',[(1,'þekkt mynstur keðjureglunnar'),(2,'umritað allt heildið með innsetningu'),(4,'notað logramynstur með réttu skilgreiningarskilyrði'),(5,'breytt heildunarmörkum með nýrri breytu')],[]),
5: ([('Veldu u og v′.', 'u á helst að einfaldast við diffrun og v′ þarf að vera hægt að heilda.'),('Finndu u′ og v.', 'Veldu eitt stofnfall fyrir v.'),('Settu inn í regluna.', 'Margfeldið uv kemur fyrst og síðan mínus heildið af u′v.'),('Heildaðu og sannprófaðu.', 'Endurtaktu ef það hjálpar. Í ákveðnu heildi þarf að nota mörkin á báðum hlutum reglunnar.')],r'<p>Reiknum \(\int xe^x\,dx\). Veljum u=x og v′=eˣ. Þá er u′=1 og v=eˣ:</p>\[\int xe^x\,dx=xe^x-\int e^x\,dx.\]\[\int xe^x\,dx=xe^x-e^x+C.\]<p>Afleiðan er eˣ+xeˣ−eˣ=xeˣ, eins og krafist var.</p>',[(1,'leitt hlutheildunarregluna af margfeldisreglunni'),(2,'fundið u, u′, v′ og v og beitt reglunni'),(3,'rökstutt val á þáttum'),(5,'endurtekið hlutheildun og notað heildunarmörk')],[]),
6: ([('Undirbúðu brotið.', 'Skoðaðu styttingu og stig. Notaðu margliðudeilingu ef stig teljara er ekki lægra en stig nefnara.'),('Þáttaðu nefnarann og skráðu skilyrðin.', 'Hér notum við tvo ólíka línulega þætti; x má ekki vera núllstöð nefnarans.'),('Settu upp stofnbrotin.', 'Settu A og B í teljarana og finndu samnefnara.'),('Finndu A og B.', 'Berðu saman teljara og veldu þægileg x-gildi eða berðu saman stuðla.'),('Heildaðu og sannprófaðu.', 'Heilda hvert brot með lograreglunni. Athugaðu liðunina með sameiginlegum nefnara og stofnfallið með diffrun.')],r'<p>Liðum í stofnbrot og heildum \(\frac{3x+4}{(x+1)(x+2)}\). Hér þarf ekki margliðudeilingu:</p>\[\frac{3x+4}{(x+1)(x+2)}=\frac A{x+1}+\frac B{x+2}.\]<p>Setjum yfir sama nefnara og berum saman teljarana:</p>\[3x+4=A(x+2)+B(x+1).\]<p>x=−1 gefur A=1 og x=−2 gefur B=2. Því fæst:</p>\[\int\frac{3x+4}{(x+1)(x+2)}\,dx=\ln|x+1|+2\ln|x+2|+C.\]<p>Við vinnum á bili sem inniheldur hvorki −1 né −2.</p>',[(1,'valið hvort einföldun eða margliðudeiling þurfi að koma fyrst'),(2,'sett upp ausudeilingu og athugað afganginn'),(3,'sett upp form stofnbrotaliðunar'),(4,'fundið stuðla stofnbrota og heildað'),(5,'sameinað deilingu og stofnbrot')],[]),
7: ([('Skoðaðu stæðuna áður en þú velur leið.', 'Einföldun getur gert lengri aðferð óþarfa.'),('Leitaðu að mynstri.', 'Innra fall og afleiða þess benda til innsetningar; margfeldi getur hentað í hlutheildun; rætt brot getur þurft undirbúning.'),('Metðu nýja heildið.', 'Eftir fyrsta skref getur önnur aðferð hentað.'),('Sannprófaðu svarið.', 'Diffraðu stofnfall. Athugaðu einnig formerki og stærð ákveðins heildis.')],r'<p>Reiknum \(\int\frac{x^2+2x}{x}\,dx\), þar sem x≠0. Fyrst einföldum við:</p>\[\frac{x^2+2x}{x}=x+2.\]<p>Nú nægja grunnreglur:</p>\[\int(x+2)\,dx=\frac{x^2}{2}+2x+C.\]<p>Afleiðan er x+2, sem er upphaflega brotið þar sem það er skilgreint.</p>',[(1,'rökstutt aðferðaval út frá byggingu heildisins'),(2,'sameinað tvær aðferðir þegar þess þarf'),(3,'fundið villur með diffrun og metið hvort svar sé trúverðugt')],['Að velja aðferð áður en stæðan hefur verið skoðuð eða einfölduð.','Að halda áfram með aðferð sem gerir heildið sífellt flóknara.','Að treysta trúverðugu tölusvari án þess að athuga útreikninginn.']),
8: ([('Teiknaðu svæðið og merktu snúningsásinn.', 'Geisli er fjarlægð frá ásnum.'),('Veldu sneið og aðferð.', 'Hornrétt sneið gefur skífu eða hringkrans; samsíða sneið gefur hólkskel.'),('Skráðu lengdir og mörk með einni breytu.', 'Notaðu x-mörk með dx og y-mörk með dy.'),('Reiknaðu rúmmálið og athugaðu einingar.', 'Rúmmál er óneikvætt og mælt í rúmeiningum.')],r'<p>Svæðinu undir y=x frá x=0 til x=1 er snúið um x-ás. Lóðrétt sneið myndar skífu með geisla x:</p>\[A(x)=\pi x^2.\]\[V=\pi\int_0^1x^2\,dx=\frac\pi3.\]',[(2,'sett upp rúmmálsheildi um x-ás'),(3,'notað láréttar sneiðar við snúning um y-ás'),(4,'fundið geisla og hæð hólkskeljar'),(5,'valið milli skífu- og hólkaaðferðar')],['Að hefja hæð svæðisins í annað veldi þegar draga á frá flatarmál tveggja hringa.','Að nota x-mörk með dy eða y-mörk með dx.','Að rugla geisla saman við hæð hólkskeljar.']),
9: ([('Finndu hvaða afleiða er gefin.', 'Ef y′ er gefið er heildað einu sinni; ef y″ er gefið er heildað tvisvar.'),('Skráðu almenna lausn með föstum.', 'Tvær heildanir gefa tvo sjálfstæða fasta.'),('Notaðu upphafsskilyrðin.', 'Athugaðu hvort hvert skilyrði á við y eða y′.'),('Athugaðu lausnina.', 'Settu afleiðurnar og fallgildin í upphaflegu jöfnuna og skilyrðin.')],r'<p>Leystu y′=2x með y(0)=3. Ein heildun gefur:</p>\[y=x^2+C.\]<p>Upphafsskilyrðið gefur C=3. Því er:</p>\[y=x^2+3.\]<p>Afleiðan er 2x og y(0)=3, svo bæði jafna og skilyrði standast.</p>',[(2,'athugað gefna lausn með diffrun'),(3,'leyst jöfnu þar sem y′ er gefið'),(4,'notað upphafsskilyrði'),(5,'heildað tvisvar þegar y″ er gefið')],[]),
10: ([('Færðu jöfnuna á formið y′+ay=0.', 'Stuðullinn við y′ þarf að vera 1.'),('Skráðu almenna lausn.', 'Notaðu y=Ce⁻ᵃˣ og gættu að formerki a.'),('Notaðu upphafsskilyrði.', 'Finndu C út frá gefnu fallgildi.'),('Athugaðu og túlkaðu.', 'Diffraðu lausnina og athugaðu hegðun hennar.')],r'<p>Leystu y′+2y=0 með y(0)=5. Hér er a=2:</p>\[y=Ce^{-2x}.\]<p>Við x=0 fæst C=5. Því er:</p>\[y=5e^{-2x}.\]<p>Afleiðan er −10e⁻²ˣ, svo y′+2y=0.</p>',[(1,'þekkt óhliðraða línulega deildajöfnu'),(2,'notað almenna lausnarformið'),(3,'ákvarðað fastann með upphafsskilyrði'),(5,'tengt lausnina við einfalt vaxtar- eða hnignunarlíkan')],[]),
11: ([('Finndu tiltekna lausn yₚ.', 'Prófaðu fall af viðeigandi gerð fyrir einfalda hægri hlið.'),('Bættu við óhliðruðu lausninni.', 'Almenna lausnin er y=yₚ+Ce⁻ᵃˣ.'),('Notaðu upphafsskilyrðið.', 'Það ákvarðar C.'),('Athugaðu jöfnuna og skilyrðið.', 'Heildunarþáttur er önnur leið þegar hann hentar.')],r'<p>Leystu y′+2y=6 með y(0)=5. Fastalausnin yₚ=3 uppfyllir jöfnuna:</p>\[y=3+Ce^{-2x}.\]<p>Upphafsskilyrðið gefur 5=3+C, svo C=2:</p>\[y=3+2e^{-2x}.\]<p>Afleiðan er −4e⁻²ˣ. Innsetning gefur y′+2y=6 og y(0)=5.</p>',[(2,'sameinað tiltekna lausn og óhliðraða lausn'),(3,'fundið tiltekna lausn í einföldu dæmi'),(4,'útskýrt tilgang heildunarþáttar'),(5,'fundið jafnvægislausn og túlkað hana')],[]),
12: ([('Athugaðu fastalausnir áður en þú deilir.', 'Deiling með stæðu sem inniheldur y getur útilokað lausn.'),('Aðskildu og heildaðu.', 'Heilda y-hlið með tilliti til y og x-hlið með tilliti til x.'),('Notaðu upphafsskilyrðið.', 'Finndu fastann og rétta lausnargrein.'),('Athugaðu lausnarbilið.', 'Fallið þarf að vera skilgreint, diffranlegt og uppfylla upphaflegu jöfnuna.')],r'<p>Leystu y·y′=x með y(0)=2. Heildun gefur:</p>\[\frac{y^2}{2}=\frac{x^2}{2}+C.\]<p>Við x=0 er y=2, svo C=2:</p>\[y^2=x^2+4.\]<p>Upphafsgildið er jákvætt og velur því jákvæðu rótina:</p>\[y=\sqrt{x^2+4}.\]<p>Hér er y aldrei núll og lausnin gildir fyrir öll x.</p>',[(1,'þekkt aðskiljanlegt form'),(2,'aðskilið breytur og heildað'),(3,'valið lausnargrein með upphafsskilyrði'),(4,'fundið fastalausnir sem deiling gæti útilokað')],[]),
13: ([('Greindu regluna.', 'Er gefinn almennur liður eða rakningarregla?'),('Athugaðu mismun eða hlutfall.', 'Fastur mismunur gefur jafnmunarunu; fastur margföldunarstuðull gefur jafnhlutfallarunu.'),('Veldu formúlu og settu rétt n inn.', 'Frá fyrsta lið til liðar númer n eru n−1 skref.'),('Athugaðu fyrstu liðina.', 'Reglan þarf að gefa upphaflegu gildin.')],r'<p>Jafnmunaruna byrjar 4, 7, 10, … með mismuninum d=3. Almenni liðurinn er:</p>\[a_n=4+3(n-1).\]<p>Sjötti liðurinn fæst með fimm skrefum frá þeim fyrsta:</p>\[a_6=4+3\cdot5=19.\]',[(1,'útskýrt lið og sæti hans í runu'),(2,'notað almenna reglu og rakningarreglu'),(3,'fundið lið í jafnmunarunu'),(4,'fundið lið í jafnhlutfallarunu')],[]),
14: ([('Greindu hvort spurt sé um lið eða summu.', 'aₙ og Sₙ merkja ekki það sama.'),('Ákvarðaðu a₁, n og d eða r.', 'Í hagnýtu dæmi þarf líka að skoða tímasetningar.'),('Veldu summureglu og athugaðu skilyrði.', 'Fyrir óendanlega jafnhlutfallaröð þarf |r|<1.'),('Reiknaðu og túlkaðu.', 'Berðu svarið saman við fyrstu liðina og samhengi dæmisins.')],r'<p>Reiknum summuna 3+6+12+24. Þetta er jafnhlutfallaröð með a₁=3, r=2 og n=4:</p>\[S_4=\frac{3(1-2^4)}{1-2}=45.\]<p>Bein samlagning gefur einnig 45. Óendanlega röðin með sömu liðum er hins vegar ekki samleitin, því r=2.</p>',[(1,'greint lið frá hlutsummu'),(2,'reiknað summu jafnmunaraðar'),(3,'reiknað endanlega jafnhlutfallaröð'),(4,'athugað samleitni óendanlegrar jafnhlutfallaraðar'),(5,'sett upp einfalda hagnýta röð')],[]),
15: ([('Skrifaðu fullyrðinguna og upphafsgildið.', 'Segðu nákvæmlega fyrir hvaða n á að sanna hana.'),('Sýndu grunnskrefið.', 'Settu fyrsta gildið inn báðum megin.'),('Settu fram þrepunarforsendu og sannaðu næsta skref.', 'Notaðu fullyrðinguna við k til að leiða hana út við k+1.'),('Ljúktu með niðurstöðu.', 'Grunnskref og þrepunarskref staðfesta fullyrðinguna fyrir öll n frá upphafsgildinu.')],r'<p>Til að sanna að summa fyrstu n oddatalnanna sé n² byrjum við við n=1: þá er 1=1². Gerum nú ráð fyrir að summan til k sé k². Næsta oddatala er 2k+1:</p>\[1+3+\cdots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2.\]<p>Því gildir fullyrðingin líka við k+1. Með grunnskrefinu fæst að hún gildir fyrir allar jákvæðar heiltölur n.</p>',[(1,'greint prófun nokkurra gilda frá sönnun'),(2,'sett fram grunnskref, forsendu og þrepunarskref'),(3,'notað þrepun við einfalda summureglu'),(4,'notað þrepun í einföldu deilanleikadæmi')],[])
}


def enrich(n,s,section_count):
    prefix_end=s.index('</p>',s.index('class="goal"'))+4
    close=s.index('</article>')
    source=s[prefix_end:close]
    headings=list(re.finditer(r'<h2>(.*?)</h2>',source))
    blocks={m[1]:source[m.end():headings[i+1].start() if i+1<len(headings) else len(source)] for i,m in enumerate(headings)}
    steps,example,checks,errors=CONTENT[n]
    if 'Að velja leið' not in blocks:
        blocks['Að velja leið']='<ol>'+''.join('<li><strong>'+a+'</strong> '+b+'</li>' for a,b in steps)+'</ol>'
    blocks['Skref fyrir skref']=example
    if 'Algeng mistök' not in blocks:
        blocks['Algeng mistök']='<ul>'+''.join('<li>'+e+'</li>' for e in errors)+'</ul>'
    if 'Ég get…' not in blocks:
        blocks['Ég get…']='<ul class="checklist">'+''.join(f'<li><a href="#s{i}">{text}</a>;</li>' for i,text in checks)+'</ul>'
    if n==6:
        blocks['Að velja leið']='<h3>Stofnbrotaliðun skref fyrir skref</h3>'+blocks['Að velja leið']
    blocks.pop('Athugaðu skilninginn',None)
    tail=blocks.pop('Fyrri umfjöllun',None)
    result=''
    for title in ['Aðalatriði','Orðalisti','Formúlur og skilyrði','Að velja leið','Skref fyrir skref','Algeng mistök','Ég get…']:
        if title=='Formúlur og skilyrði' and 'Formúlur og reglur' in blocks:
            result+='<h2>Formúlur og skilyrði</h2>'+blocks['Formúlur og reglur']
        else: result+='<h2>'+title+'</h2>'+blocks[title]
    if tail:result+='<details class="refresher"><summary>Fyrri umfjöllun</summary>'+tail+'</details>'
    # One link at the bottom; keep links within the self-check list intact.
    result=re.sub(r'<p><a class="summary-link".*?</a></p>','',result,flags=re.S)
    result+=f'<p><a class="summary-link" href="#s{section_count}">Halda áfram í blandað dæmasafn →</a></p>'
    return s[:prefix_end]+result+s[close:]


def apply(dist):
    for n in range(1,16):
        p=Path(dist)/('index.html' if n==1 else f'unit-{n}.html')
        text=p.read_text(encoding='utf-8')
        sections=list(re.finditer(r'<section id="s(\d+)"(?=[\s>]).*?</section>',text,re.S))
        if n in CONTENT:
            count=len(sections)
            def edit(m):
                if 'Samantekt, orðalisti og formúlur</h1>' not in m[0]:return m[0]
                return enrich(n,m[0],count)
            text=re.sub(r'<section id="s(\d+)"(?=[\s>]).*?</section>',edit,text,flags=re.S)
        else:
            # Chapter 2 already has all sections; put them in the same order.
            def reorder(m):
                s=m[0]
                if 'Samantekt, orðalisti og formúlur</h1>' not in s:return s
                a=s.index('<h2>Aðalatriði</h2>');b=s.index('</article>')
                marks=list(re.finditer(r'<h2>(.*?)</h2>',s[a:b]));blocks={x[1]:s[a+x.start():a+(marks[i+1].start() if i+1<len(marks) else b-a)] for i,x in enumerate(marks)}
                return s[:a]+''.join(blocks[k] for k in ['Aðalatriði','Orðalisti','Formúlur og skilyrði','Að velja leið','Skref fyrir skref','Algeng mistök','Ég get…'])+s[b:]
            text=re.sub(r'<section id="s(\d+)"(?=[\s>]).*?</section>',reorder,text,flags=re.S)
        # Correct an existing truncated phrase while retaining the meaning.
        text=text.replace('Runa þar sem hver liður frá öðrum fæst með föstum margföldunarstuðli r.','Runa þar sem hver liður, frá og með öðrum lið, fæst með því að margfalda fyrri lið með föstum stuðli r.')
        p.write_text(text,encoding='utf-8')
