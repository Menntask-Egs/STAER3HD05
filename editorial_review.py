"""Reviewed prose additions, keyed to the published unit and section numbers.

This layer edits teaching text only; exercises, controls and deep links remain stable.
Anchors are asserted so a future authoring change cannot silently skip a revision.
"""
import re

TASKS = {
 '1.1.1':r'Finna á eitt stofnfall fallsins \(f(x)=6x\) og athuga það með diffrun.',
 '1.3.1':r'Reiknum óákveðna heildið \(\int6x\,dx\) og setjum svarið fram með heildunarfastanum.',
 '1.4.1':r'Finna á óákveðna heildið \(\int x^3\,dx\) með veldisreglunni.',
 '1.5.1':r'Reiknum \(\int(3x^2-4x+2)\,dx\). Markmiðið er að finna eitt almennt stofnfall allrar summunnar.',
 '1.6.1':r'Finna á óákveðna heildið \(\int(2e^x-3\sin x+4/x)\,dx\), á bili sem inniheldur ekki núll.',
 '1.6.2':r'Finna á eitt stofnfall \(\sin x\) og útskýra hvaða formerki þarf að vera í svarinu.',
 '1.6.3':r'Útskýrum hvers vegna \(\ln|x|\) gefur stofnfall \(1/x\) bæði á jákvæðum og neikvæðum bilum.',
 '2.3.1':r'Finna á bæði ákveðna heildið \(\int_{-1}^{1}x\,dx\) og heildarflatarmál svæðanna milli grafsins og x-ássins á sama bili.',
 '2.4.1':r'Reiknum ákveðna heildið \(\int_0^2(3x^2+1)\,dx\) með því að finna stofnfall og nota bæði heildunarmörkin.',
 '2.5.1':r'Reiknum \(\int_1^2(x+1)\,dx\) og skoðum sérstaklega framlag neðri markanna.',
 '2.6.1':r'Finna á hversu mikið vatn bætist í tankinn og hversu mikið er í honum eftir þrjár mínútur.',
 '3.1.1':r'Finna á flatarmál svæðisins milli grafsins \(y=x^2\) og x-ássins frá x=0 til x=2.',
 '3.1.2':r'Finna á flatarmál svæðisins milli grafsins \(y=-x\) og x-ássins frá x=0 til x=2. Berum það saman við ákveðna heildið á sama bili.',
 '3.2.1':r'Reiknum bæði ákveðna heildið og heildarflatarmálið milli grafsins \(y=x\) og x-ássins frá x=−1 til x=1.',
 '3.4.1':r'Finna á flatarmál svæðisins milli \(y=x\) og \(y=x^2\) í fyrsta fjórðungi með láréttum sneiðum.',
 '3.5.1':r'Finna á magnbreytinguna í geyminum og lokamagnið eftir tvær mínútur.',
 '3.5.2':r'Finna á færslu og heildarvegalengd hlutar á fyrstu þremur sekúndunum út frá hraðafallinu hér fyrir neðan.',
 '4.2.1':r'Reiknum eftirfarandi óákveðna heildi. Við viljum finna stofnfall með því að umrita heildið í nýrri breytu.',
 '4.3.1':r'Reiknum óákveðna heildið hér fyrir neðan. Skoðum hvernig fasti í innri stæðunni hefur áhrif á stuðul stofnfallsins.',
 '4.3.2':r'Reiknum óákveðna heildið hér fyrir neðan og höldum sérstaklega utan um stuðulinn sem innsetningin gefur.',
 '4.4.1':r'Finna á óákveðna heildið hér fyrir neðan. Athugum hvort teljarinn tengist afleiðu nefnarans.',
 '4.4.2':r'Finna á óákveðna heildið hér fyrir neðan á bili sem inniheldur ekki x=3/2.',
 '4.5.1':r'Reiknum eftirfarandi ákveðna heildi með innsetningu. Niðurstaðan á að vera tala, ekki fall af u eða x.',
 '4.5.2':r'Reiknum eftirfarandi ákveðna heildi og breytum mörkunum um leið og heildunarbreytunni.',
 '5.1.1':r'Finna á \(\int xe^x\,dx\). Nýtum diffrunina hér að ofan til að sjá hvaða stofnfall hentar.',
 '5.2.1':r'Reiknum eftirfarandi óákveðna heildi með hlutheildun. Við sýnum sérstaklega hvað er diffrað og hvað er heildað.',
 '5.3.1':r'Finna á óákveðna heildið hér fyrir neðan. Hér þarf bæði að velja þætti og halda utan um innri stuðul hornafallsins.',
 '5.4.1':r'Reiknum \(\int\ln x\,dx\) fyrir x>0 með því að líta á heildisstofninn sem margfeldi tveggja þátta.',
 '5.4.2':r'Reiknum óákveðna heildið hér fyrir neðan fyrir x>0.',
 '5.5.1':r'Finna á óákveðna heildið hér fyrir neðan. Veljum þættina þannig að margliðan lækki um stig við hverja umferð.',
 '5.5.2':r'Reiknum ákveðna heildið \(\int_0^1xe^x\,dx\) og sýnum hvernig mörkin fylgja báðum hlutum hlutheildunarreglunnar.',
 '6.1.1':r'Finna á \(\int\frac{x^2-1}{x-1}\,dx\), á bili sem inniheldur ekki 1. Byrjum á að athuga hvort brotið einfaldist.',
 '6.2.1':r'Finna á \(\int\frac{x^2+1}{x+1}\,dx\). Margliðudeilingin er undirbúningur fyrir heildunina, ekki lokamarkmið dæmisins.',
 '6.3.1':r'Samnefnum brotin \(1/(x+1)\) og \(2/(x+2)\). Skoðum síðan hvernig sama jafna má lýsa liðun eins brots í tvö.',
 '6.4.1':r'Reiknum óákveðna heildið hér fyrir neðan með því að finna fyrst einfaldari brot með sama samanlagða gildi.',
 '6.5.1':r'Finna á óákveðna heildið hér fyrir neðan. Fyrst þarf að greina margliðuhlutann frá brotahlutanum.',
 '7.1.1':r'Finna á bæði óákveðnu heildin hér fyrir neðan og rökstyðja hvers vegna ólíkar aðferðir henta þeim.',
 '7.1.2':r'Reiknum \(\int\frac{(x+1)^2}{x+1}\,dx\), á bili sem inniheldur ekki −1. Skoðum hvort sértæk heildunaraðferð sé yfirleitt nauðsynleg.',
 '7.2.1':r'Reiknum óákveðna heildið hér fyrir neðan. Eftir fyrsta skrefið metum við hvaða leið hentar nýja heildinu.',
 '7.3.1':r'Finna á villuna í tillögu nemandans hér fyrir neðan og leiðrétta stofnfallið með hjálp diffrunar.',
 '7.3.2':r'Athugum lausnarskref nemandans og finnum fyrsta ranga formerkið.',
 '7.3.3':r'Metum neðri og efri mörk fyrir \(\int_0^1e^x\,dx\) og athugum hvort reiknað svar geti staðist.',
 '8.1.1':r'Reiknum rúmmál sívalningsins hér fyrir neðan með heildi af þversniðsflatarmáli.',
 '8.2.1':r'Finna á rúmmál snúðsins sem myndast við snúninginn sem lýst er hér fyrir neðan.',
 '8.2.2':r'Finna á rúmmál snúðsins. Hér þarf að taka tillit til gatsins sem myndast í miðjunni.',
 '8.3.1':r'Reiknum rúmmál snúðsins um y-ás með skífum og heildun með tilliti til y.',
 '8.3.2':r'Reiknum rúmmál snúðsins um y-ás. Finna þarf bæði ytri og innri geisla þversniðsins.',
 '8.4.1':r'Finna á rúmmál snúðsins um y-ás með hólkaaðferð. Ákveðum geisla og hæð áður en heildið er reiknað.',
 '8.4.2':r'Reiknum rúmmál sama flata svæðis þegar því er snúið um x-ás, nú með láréttum hólkskeljum.',
 '9.1.1':r'Athugum hvort bæði föllin \(y=x^2\) og \(y=x^2+3\) leysi deildajöfnuna \(y\prime=2x\).',
 '9.3.1':r'Finna á almenna lausn deildajöfnunnar hér fyrir neðan. Ekkert upphafsskilyrði er gefið, svo einn frjáls fasti á að vera í svarinu.',
 '9.5.1':r'Finna á almenna lausn jöfnunnar hér fyrir neðan, þar sem önnur afleiða er gefin.',
 '9.5.3':r'Finna á staðsetningarfall hlutarins og staðsetningu hans eftir tvær sekúndur út frá hröðun og upphafsgildum.',
 '10.1.1':r'Athugum með diffrun hvort \(y=3e^{2x}\) leysi jöfnuna \(y\prime=2y\).',
 '10.2.1':r'Finna á almenna lausn jöfnunnar hér fyrir neðan.',
 '10.2.2':r'Finna á almenna lausn jöfnunnar hér fyrir neðan. Mínusmerkið fyrir framan y er hluti af stuðlinum a.',
 '10.2.3':r'Finna á almenna lausn jöfnunnar hér fyrir neðan. Stuðullinn við y′ er ekki enn 1.',
 '10.3.1':r'Leyst er deildajafnan hér fyrir neðan með gefnu upphafsskilyrði. Finna þarf fallið y, ekki aðeins fastann C.',
 '10.3.2':r'Finna á lausn sem uppfyllir bæði jöfnuna og gefið fallgildi við x=1.',
 '10.5.1':r'Setja á upp líkan fyrir massann, finna magnið eftir fimm klukkustundir og reikna hvenær helmingur upphafsmassans er eftir.',
 '11.1.1':r'Athugum hvort fastafallið y=3 og fallið \(y=3+4e^{-2x}\) uppfylli bæði jöfnuna hér fyrir neðan.',
 '11.2.1':r'Finna á almenna lausn jöfnunnar hér fyrir neðan og síðan þá lausn sem uppfyllir y(0)=7.',
 '11.3.1':r'Finna á almenna lausn jöfnunnar hér fyrir neðan. Leitum fyrst að einni tiltekinni lausn sem er línulegt fall.',
 '11.3.2':r'Finna á almenna lausn jöfnunnar hér fyrir neðan. Leitum fyrst að einni tiltekinni lausn með vísisfalli.',
 '11.4.1':r'Finna á almenna lausn jöfnunnar hér fyrir neðan með heildunarþætti og síðan nota skilyrðið y(0)=2.',
 '11.5.1':r'Finna á hitastigsfall hlutarins og hitastigið eftir tíu mínútur samkvæmt kælingarlíkaninu.',
 '12.2.1':r'Finna á allar lausnir jöfnunnar hér fyrir neðan. Athugum fastalausn áður en við deilum með y.',
 '12.3.1':r'Leyst er deildajafnan með gefnu upphafsskilyrði. Finna þarf rétta lausnargrein og hvar hún gildir.',
 '12.3.2':r'Leyst er deildajafnan með upphafsskilyrðinu hér fyrir neðan. Útskýrum hvers vegna lausnin má ekki taka gildið núll.',
 '12.4.1':r'Finna á fastalausnir og ófastar lausnir jöfnunnar hér fyrir neðan, og síðan þá lausn sem hefur y(0)=1.',
 '13.1.1':r'Finna á fimmta lið rununnar sem er skilgreind með reglunni hér fyrir neðan.',
 '13.2.1':r'Finna á lið númer 20 í rununni sem gefin er með almenna liðnum hér fyrir neðan.',
 '13.2.2':r'Finna á fyrstu fjóra liði rununnar sem rakningarreglan skilgreinir og bera þá saman við fyrra sýnidæmið.',
 '13.3.1':r'Finna á almenna lið jafnmunarununnar og síðan tíunda lið hennar út frá upplýsingunum hér fyrir neðan.',
 '13.3.2':r'Finna á almenna lið jafnmunarununnar sem byrjar á 12, 8, 4 og 0.',
 '13.4.1':r'Finna á almenna lið jafnhlutfallarununnar og reikna sjötta lið hennar.',
 '14.1.1':r'Finna á fjórða lið rununnar og summu fyrstu fjögurra liða hennar. Berum þessar tvær stærðir saman.',
 '14.2.1':r'Finna á summuna hér fyrir neðan með því að para liði frá sitt hvorum enda.',
 '14.3.1':r'Reiknum summuna 3+6+12+24 og notum hana sem inngang að almennri summureglu.',
 '14.4.1':r'Skoðum hvort óendanlega röðin hér fyrir neðan sé samleitin og hvaða tölu hlutsummurnar nálgast.',
 '14.4.2':r'Athugum samleitni óendanlegu raðarinnar hér fyrir neðan og reiknum summuna ef hún er til.'
}

def revise(n,markup):
 def section_edit(match):
  section=match.group(0)
  number=int(re.search(r'id="s(\d+)"',section)[1])
  for eid,task in TASKS.items():
   if not eid.startswith(f'{n}.{number}.'):continue
   pattern=r'(<h3>Sýnidæmi '+re.escape(eid)+r'(?:\s[^<]*)?</h3>)'
   section,count=re.subn(pattern,lambda m:m[0]+'<p class="example-task">'+task+'</p>',section,count=1)
   assert count==1,('Missing worked example',eid)
  return explain(n,number,section)
 return re.sub(r'<section\b.*?</section>',section_edit,markup,flags=re.S)

# Exact local prose edits keep mathematics and controls outside the reviewed text intact.
def explain(n,i,s):
 def after(anchor,text):
  nonlocal s
  assert anchor in s,(n,i,anchor)
  s=s.replace(anchor,anchor+text,1)
 def before(anchor,text):
  nonlocal s
  assert anchor in s,(n,i,anchor)
  s=s.replace(anchor,text+anchor,1)
 def replace(old,new):
  nonlocal s
  assert old in s,(n,i,old)
  s=s.replace(old,new,1)
 if (n,i)==(1,3):
  after('<p>Svarið er fjölskylda falla, ekki ein tala. Við athugum með því að diffra hægri hliðina.</p>',r'<p>Í \(\int6x\,dx\) er 6x fallið sem við þekkjum fyrir fram. Svarið 3x²+C er hins vegar fallið sem við vorum að leita að. Við diffrun lækkar veldið úr 2 í 1 og stuðullinn 3 margfaldast með 2, svo afleiðan verður aftur 6x.</p>')
 if (n,i)==(1,4):
  before(r'\[\int x^3\,dx=\frac{x^4}{4}+C.\]',r'<p>Veldisvísirinn er 3. Við hækkum hann í 4, en x⁴ eitt og sér hefði afleiðuna 4x³. Þess vegna þurfum við líka að deila með 4 svo afleiðan verði nákvæmlega x³.</p>')
 if (n,i)==(1,5):
  before(r'\[\begin{aligned}\int(3x^2-4x+2)',r'<p>Við heildum þrjá liði sitt í hvoru lagi. Stuðlarnir 3 og −4 halda sér utan við heildunina. Fastaliðurinn 2 verður 2x, því afleiða 2x er 2.</p>')
 if (n,i)==(1,6):
  before(r'\[\int(2e^x-3\sin x+4/x)',r'<p>Vísisliðurinn notar stofnfall eˣ, hornafallsliðurinn notar stofnfall sin x og brotið 4/x notar lograregluna. Við höldum stuðlunum og sameinum heildunarfasta í einn C.</p>')
 if (n,i)==(2,3):
  before('<h3>Sýnidæmi',r'<p>Hægt er að hugsa hvert framlag sem fallgildi sinnum litla bilbreidd. Ofan x-áss er framlagið jákvætt en neðan hans neikvætt. Þegar a&lt;b dregst flatarmálið neðan ássins því frá flatarmálinu ofan hans. Þetta er merking þess að heildið sé <strong>formerkt</strong>.</p>')
 if (n,i)==(2,4):
  replace(r'\[\int_0^2(3x^2+1)\,dx=\left[x^3+x\right]_0^2=(8+2)-(0+0)=10.\]',r'<p>Fyrst finnum við stofnfall heildisstofnsins, alveg eins og í einingu 1:</p>\[F(x)=x^3+x.\]<p>Næst reiknum við fallgildi þess við hvorn endapunkt. Mörkin fara inn í stofnfallið F:</p>\[F(2)=2^3+2=10.\]\[F(0)=0^3+0=0.\]<p>Að lokum drögum við neðra fallgildið frá því efra:</p>\[\int_0^2(3x^2+1)\,dx=F(2)-F(0)=10-0=10.\]<p>Við þurfum ekki frjálsan C í lokasvarinu, því ákveðið heildi er tala. Heildunarfasti í stofnfallinu myndi hvort sem er falla út við frádráttinn.</p>')
 if (n,i)==(2,5):
  before('<h3>Sýnidæmi',r'<p>Reglurnar lýsa hvernig bil og framlög leggjast saman. Heildi frá a til a er núll því bilið hefur enga lengd. Ef við förum frá b aftur til a verður breytingin andstæð þeirri sem fæst frá a til b. Uppskipting við c skiptir sama heildarframlagi í tvo samliggjandi hluta.</p>')
  after('<p>Villan „4“ kæmi af því að reikna aðeins efra fallgildið.</p>',r'<p>Gildið við x=1 er ekki núll: það er 3/2. Svigarnir utan um neðra fallgildið minna á að draga þarf <em>alla</em> stæðuna frá, líka þegar hún inniheldur fleiri en einn lið.</p>')
 if (n,i)==(2,6):
  before('<h3>Sýnidæmi',r'<p>Hraðafallið segir hversu margar magneiningar bætast við á hverri tímaeiningu. Heildið safnar þessum breytingum saman yfir tímabilið. Það segir ekki hvað var til fyrir, svo upphafsmagnið þarf að vera þekkt til að reikna lokamagnið.</p>')
  after(r'<p>Lokamagnið er \(10+12=22\) L. Talan 12 er breytingin, ekki lokamagnið.</p>',r'<p>Við athugum einingarnar: L/mín margfaldað með mínútum gefur lítra. Það passar við að 12 sé viðbótarmagn sem má leggja við upphaflegu 10 lítrana.</p>')
 if (n,i)==(2,7):
  replace(r'\[\int_a^b f=F(b)-F(a)\]',r'\[\int_a^b f(x)\,dx=F(b)-F(a).\]')
  before('</article>','''<h2>Algeng mistök</h2><ul><li>Að setja mörkin inn í heildisstofninn í stað stofnfallsins.</li><li>Að reikna aðeins efra fallgildið.</li><li>Að túlka neikvætt heildi sem neikvætt flatarmál.</li><li>Að rugla saman magnbreytingu og lokamagni.</li></ul>''')
 if (n,i)==(3,2):
  before(r'\[A=-\int_{-1}^0x\,dx',r'<p>Við skiptum í tvo hluta við x=0. Heildið á [−1,0] er −1/2, svo við skiptum um formerki til að fá flatarmálið 1/2. Hægra megin er fallið jákvætt og heildið gefur flatarmálið beint. Nú leggjast stærðir svæðanna saman í stað þess að eyða hvor annarri.</p>')
 if (n,i)==(3,4):
  replace('Sýnidæmi 3.4.1 — sama svæði á annan hátt','Sýnidæmi 3.4.1 — láréttar sneiðar')
  before(r'\[A=\int_0^1(\sqrt y-y)',r'<p>Hér skerast y=x og y=x² við (0,0) og (1,1). Því liggja y-mörkin frá 0 til 1. Við y=1/4 er hægri endi sneiðarinnar x=1/2 og vinstri endinn x=1/4. Þetta sýnir hvers vegna breiddin er √y−y, ekki öfugt.</p>')
  replace('Þetta er sama niðurstaða og fæst með lóðréttum sneiðum í 3.3.',r'Með lóðréttum sneiðum á þessu svæði fengist \(\int_0^1(x-x^2)\,dx=1/6\), svo báðar leiðir gefa sama flatarmál.')
 if (n,i)==(3,5):
  before(r'\[\text{Vegalengd}=',r'<p>Stefnubreytingin verður við v(t)=0, það er t=1. Fyrsta sekúnduna er færslan −1 m; næstu tvær sekúndur er hún 4 m. Færslurnar leggjast saman með formerkjum, en vegalengdirnar eru stærðirnar 1 m og 4 m.</p>')
 if (n,i)==(4,3):
  after(r'\[x\,dx=\frac12\,du.\]',r'<p>Í upphaflega heildinu er x dx, en í du er 2x dx. Því þarf aðeins hálft du til að koma í stað þáttarins sem við höfum. Við erum að umrita sama heildi, ekki að bæta nýjum þætti við það.</p>')
 if (n,i)==(5,4):
  before('<p>Logrinn einfaldast við diffrun.',r'<p>Stofnfall ln x er ekki fengið með því að nota lograregluna fyrir 1/x: þar er verið að heilda annað fall. Með því að skrifa ln x sem ln x·1 fáum við tvo þætti sem hlutheildun getur unnið með.</p>')
 if (n,i)==(6,2):
  before(r'\[\int\frac{x^2+1}{x+1}dx',r'<p>Kvótinn er x−1 og afgangurinn 2. Þegar jöfnunni er deilt með upprunalega nefnaranum fæst:</p>\[\frac{x^2+1}{x+1}=x-1+\frac2{x+1}.\]<p>Þetta er sama fall og áður, en nú má heilda þrjá einfalda liði. Afgangurinn 2 situr áfram yfir nefnaranum x+1; hann verður ekki sjálfstæður fastaliður.</p>')
 if (n,i)==(7,1):
  before('<p>Í fyrra heildinu er innri stæðan',r'<p>Heildin líkjast hvort öðru, en innri stæðan í vísisfallinu er ekki sú sama. Í fyrra dæminu veljum við u=x². Í seinna dæminu hjálpar ekki að skipta eˣ út fyrir nýja breytu ef x-þátturinn verður enn eftir.</p>')
 if (n,i)==(8,4):
  before(r'\[V=2\pi\int\text{geisli}',r'<p>Hugsum hólkskelina skorna eftir endilöngum ás og lagða flata. Lengdin utan um hana er ummálið 2πr og hin lengdin er hæðin h. Flatarmálið er því nálægt 2πrh. Margföldun með lítilli þykkt gefur rúmmál þunnrar skeljar. Heildið leggur slíkar skeljar saman.</p>')
  before(r'\[V=2\pi\int_0^1y\sqrt y',r'<p>Lárétt sneið við y hefur lengdina √y−0 og fjarlægðina y frá x-ásnum. Þótt sneiðin sé lárétt köllum við lengd hennar „hæð“ hólkskeljarinnar: hún liggur eftir snúningsásnum. Ummálið er 2πy og þykktin dy. Þess vegna verður margfeldið inni í heildinu y√y.</p>')
 if (n,i)==(9,5):
  replace('<p>Bætum við skilyrðunum:</p>',r'<p>Leyst er nú sama jafna \(y\prime\prime=6x\), en með eftirfarandi tveimur upphafsskilyrðum:</p>')
  before('<p>Fyrra skilyrðið er sett inn',r'<p>Almenna lausnin er enn y=x³+C₁x+C₂ og afleiðan y′=3x²+C₁. Við þurfum því að velja rétta formúlu fyrir hvort skilyrði: y′(0) gefur upplýsingar um afleiðuna en y(0) um fallið sjálft.</p>')
 if (n,i)==(10,2):
  before('<h3>Sýnidæmi',r'<p>Lausnarreglan er því ekki óháð því sem við kunnum um diffrun. Veldisvísirinn −ax sér um margföldunarstuðulinn −a í afleiðunni, en C velur stærð og formerki lausnarinnar. Við byrjum á að koma jöfnunni nákvæmlega á formið y′+ay=0 áður en a er lesið af.</p>')
 if (n,i)==(11,3):
  before('<p>Prófum yₚ=Ax+B.',r'<p>Hægri hliðin er línuleg í x. Við prófum því línulegt fall með tveimur óþekktum stuðlum. Jafnvel þótt hægri hliðin hafi engan fastalið þurfum við að leyfa B, því afleiðan af Ax býr sjálf til fastalið.</p>')
  before('<p>Prófum yₚ=Ae²ˣ:',r'<p>Afleiða e²ˣ er fasti sinnum e²ˣ. Því heldur þessi fallgerð sér þegar afleiðan og fallið eru lögð saman. Við vitum ekki stuðulinn fyrir fram og köllum hann A.</p>')
 if (n,i)==(11,4):
  before('<p>Margfeldisreglan segir',r'<p>Þátturinn eᵃˣ er valinn vegna þess að afleiða hans er aeᵃˣ. Þetta gefur nákvæmlega aukaþáttinn sem þarf í margfeldisreglunni. Markmiðið með margfölduninni er því að geta heildað eina heila afleiðu, ekki að eyða y-liðnum.</p>')
  replace('Við notum þessa aðferð í fáum einföldum dæmum; ekki þarf að læra sérstakar útgáfur fyrir breytilegan stuðul a hér.','Hér notum við aðeins fastan stuðul a.')
 if (n,i)==(12,1):
  before('<p>Við heildum vinstri hlið',r'<p>Á vinstri hlið kemur y′ með af því að y er fall af x. Þegar við skrifum heildið með dy er þetta samband þegar tekið með í breytingu heildunarbreytunnar. Þess vegna heildum við g(y) með tilliti til y, en ekki meðhöndlum y sem fasta við heildun í x.</p>')
  s=s.replace(' og gefðu samband milli x og y.','.',1)
 if (n,i)==(12,2):
  before('<p>Þar sem eᶜ&gt;0',r'<p>Algildismerkið felur í sér að bæði jákvæð og neikvæð y-gildi eru möguleg. Á bili þar sem y er ekki núll helst formerkið hið sama. Nýi fastinn A tekur því með bæði stærðina eᶜ og valið á formerki. Hann er ekki sami fasti og C, heldur ný táknun fyrir niðurstöðuna eftir veldisvörpun.</p>')
 if (n,i)==(12,3):
  before('<p>Við gætum tekið jákvæða',r'<p>Sambandið y²=x²+4 ákvarðar ekki eitt fall fyrr en formerkið hefur verið valið. Bæði jákvæð og neikvæð rót uppfylla það. Hér segir y(0)=−2 til um að ferillinn þurfi að liggja neðan x-ássins við upphafspunktinn.</p>')
 if (n,i)==(12,5):
  before('<p>Upphafshraðinn er jákvæður.',r'<p>Finna á hraðafallið v(t), hraðann eftir fjórar sekúndur og hvernig hann breytist með tímanum. Við notum líkanið frá upphafstímanum t=0.</p>')
 if (n,i)==(13,2):
  before('<p>Byrjum í 3 og bætum 2 við',r'<p>Táknmálið aₙ₊₁ merkir liðinn strax á eftir aₙ. Fyrir n=1 segir reglan a₂=a₁+2=5. Fyrir n=2 segir hún a₃=a₂+2=7. Í hvert skipti þarf því að þekkja fyrri liðinn áður en næsti er reiknaður.</p>')
 if (n,i)==(13,3):
  before('<h3>Sýnidæmi',r'<p>Munurinn á n og n−1 sést þegar við skrifum fyrstu skrefin: a₂=a₁+d og a₃=a₁+2d. Fyrsti liðurinn er upphafspunkturinn; til að komast í sæti 3 höfum við aðeins bætt d tvisvar við.</p>')
 if (n,i)==(13,4):
  replace('fæst hver liður frá öðrum lið','fæst hver liður, frá og með öðrum lið,')
  before('<h3>Sýnidæmi',r'<p>Við byrjum á a₁. Annar liðurinn er a₁r og sá þriðji a₁r². Í sæti n höfum við því margfaldað með r alls n−1 sinnum. Þetta skýrir veldisvísinn í formúlunni.</p>')
 if (n,i)==(14,2):
  before('<h3>Sýnidæmi 14.2.2',r'<p>Ef n er oddatala stendur miðliður eftir þegar parað er innan einnar summu. Tvíritunin, ein summa áfram og ein afturábak, forðast þann vanda: saman mynda þær alltaf n pör. Við deilum með 2 vegna þess að við höfum þá reiknað tvöfalda upphaflegu summuna.</p>')
 if (n,i)==(14,3):
  before('<p>Drögum seinni línuna frá',r'<p>Margföldun með r færir hverja r-veldisstæðu einu sæti áfram. Því koma a₁r, a₁r² og aðrir milliliðir fyrir í báðum línum. Aðeins fyrsti liður fyrri línunnar og síðasti liður seinni línunnar eiga sér ekki mótlið.</p>')
 if (n,i)==(14,4):
  before('<h2>Hvenær fæst endanleg summa?',r'<p>Í flatarmálsdæminu er hver endanleg hlutsumma minni en 1. Eftir n liði er óskyggða flatarmálið 1/2ⁿ, sem má gera eins lítið og við viljum með því að fjölga liðum. Summan 1 er markgildið, þótt engin endanleg hlutsumma verði nákvæmlega 1.</p>')
 if (n,i)==(14,5):
  before('<p>Hæðirnar eftir fyrsta',r'<p>Finna á samanlagða vegalengd boltans frá fyrsta fallinu og í öllum skoppunum, samkvæmt þessu líkani. Við þurfum að greina á milli hæðar hvers skopps og vegalengdarinnar sem boltinn fer.</p>')
 if (n,i)==(15,2):
  after('<p>Látum P(n) tákna fullyrðingu um jákvæða heiltölu n. Þrepunarsönnun fyrir öll n≥1 hefur eftirfarandi uppbyggingu.</p>',r'<p>P(n) er stutt heiti á heilli setningu, ekki nýtt fall sem þarf að reikna. Til dæmis má láta P(n) merkja setninguna „summa fyrstu n oddatalnanna er n²“. Þá er P(1) fyrsta tilvikið og P(k+1) sama setning með k+1 í stað n.</p>')
 if (n,i)==(15,3):
  before(r'\[\frac{k(k+1)}2+(k+1)=',r'<p>Til að leggja liðina saman skrifum við k+1 sem 2(k+1)/2. Teljarinn verður þá k(k+1)+2(k+1). Sameiginlegi þátturinn k+1 er tekinn út fyrir sviga og eftir stendur k+2.</p>')
 if (n,i)==(15,4):
  before(r'\[4^{k+1}-1=4(4^k-1)+3.',r'<p>Við viljum fá stæðuna 4ᵏ−1 inn í næsta skref, því þrepunarforsendan segir eitthvað um hana. Margfeldið 4(4ᵏ−1) er 4ᵏ⁺¹−4. Við bætum því 3 við til að fá aftur 4ᵏ⁺¹−1. Umritunin breytir ekki gildinu.</p>')
 return s
