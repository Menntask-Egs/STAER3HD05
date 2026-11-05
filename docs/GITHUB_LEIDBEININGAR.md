# Flutningur STÆR3HD05 á GitHub

Leiðbeiningar útbúnar 5. nóvember 2026. Pakkinn er tilbúinn til innflutnings, en hefur **ekki** verið settur á GitHub reikning skólans og engin ný vefsíða hefur verið birt.

## 1. Hvað þú þarft

- Aðgang að GitHub reikningi skólans eða heimild til að stofna geymslu í GitHub-stofnun skólans.
- Réttindi til að breyta geymslunni og stilla GitHub Pages. Ef þú sérð ekki Settings þarf stjórnandi að aðstoða.
- ZIP-pakkann, afþjappaðan á tölvuna.
- GitHub Desktop, ef þú fylgir aðalleiðinni hér að neðan: https://desktop.github.com/ . Innskráning fer fram í forritinu/vafra; ekki setja lykilorð eða aðgangstákn í skrár bókarinnar.

Þú þarft **ekki** að kunna skipanalínu eða setja Python upp á tölvunni til að nýta sjálfvirku bygginguna á GitHub.

## 2. Ákveða geymslu og sýnileika

Tillaga að heiti geymslu: **staer3hd05**. Veldu reikning/stofnun skólans sem **Owner**. Ekki nefna geymsluna `<reikningur>.github.io` nema hún eigi að vera aðalvefsíða alls reikningsins; þessi pakki er hugsaður sem verkefnasíða sem má hafa við hlið annarra bóka.

**Byrjaðu með Private meðan þú ert að flytja inn og yfirfara.** Birting er óvirk í vinnuflæðinu þar til hún er sérstaklega virkjuð.

Geymslan og vefsíðan eru tveir ólíkir hlutir:

| Val | Hvað það þýðir |
| --- | --- |
| Private repository | Frumskrár sjá aðeins þeir sem fá aðgang. Bókin getur verið geymd og athuganir keyrðar án þess að vefsíðan sé birt. |
| Public repository | Frumskrárnar eru opinberar. Þetta er leiðin sem GitHub Free styður fyrir Pages. |
| GitHub Pages | Birtir útbúna vefsíðu. Einkageymsla tryggir ekki að Pages-vefurinn sé einkavefur. Einkabirting með aðgangsstýringu er sérstakur Enterprise Cloud-eiginleiki. |

Á GitHub Free er Pages fyrir opinberar geymslur; önnur áskrift getur heimilað Pages úr einkageymslu. Ef skólinn vill lokaðan aðgang að bókinni skaltu geyma frumskrárnar einkalegar og bíða með Pages þar til hýsingarleið hefur verið valin. **Ekki gera geymsluna opinbera eingöngu til að komast framhjá stillingavillu.**

Þú getur lokið skrefum 3–5 og haldið yfirlestri áfram áður en þú ákveður opinbera birtingu.

## 3. Stofna geymslu skólans

1. Skráðu þig inn á GitHub og veldu **New repository**.
2. Veldu réttan **Owner**: reikning eða stofnun skólans.
3. Skrifaðu `staer3hd05` í **Repository name**.
4. Veldu **Private** fyrir fyrstu uppsetningu.
5. Kveiktu á **Add README** svo geymslan hafi upphafscommit og `main`-grein.
6. Ekki bæta við sjálfvirku leyfi eða .gitignore hér; pakkinn hefur eigin .gitignore og ekki hefur verið ákveðið opið leyfi.
7. Veldu **Create repository**.

Þessi leið gerir ráð fyrir nýrri geymslu. Ef geymsla með þessu heiti er þegar til og hefur efni skaltu ekki yfirskrifa hana; notaðu annað heiti eða fáðu aðstoð við að sameina efnið.

## 4. Flytja skrárnar inn með GitHub Desktop

1. Opnaðu GitHub Desktop og skráðu þig inn með reikningi sem hefur aðgang að geymslu skólans.
2. Veldu **File → Clone repository**. Finndu nýju geymsluna; ef hún sést ekki má nota **URL**-flipann og líma geymsluslóðina frá GitHub.
3. Veldu stað á tölvunni og smelltu á **Clone**.
4. Veldu **Repository → Show in Explorer** (á macOS: **Show in Finder**).
5. Opnaðu afþjappaða flutningspakkann. Þar er mappan `staer3hd05` með `README.md`, `build_site.py`, `assets`, `docs` og fleiri skrám.
6. Afritaðu **innihald** þeirrar möppu í möppuna sem GitHub Desktop bjó til. Ekki afrita ytri möppuna sem eina undirmöppu. Samþykkja má að skipta út upphafs-README sem þú stofnaðir í skrefi 3.
7. Gættu þess að **`.github` mappan fylgi**, ásamt `.gitignore` og `.gitattributes`. Á Windows má kveikja á **View → Show → Hidden items**; á macOS má nota **Cmd+Shift+.** til að sjá punktaskrár. Ekki hreyfa `.git` möppuna sem GitHub Desktop bjó til.
8. Farðu aftur í GitHub Desktop. Í **Changes** ættu að sjást frumskrár, myndir, leiðbeiningar og `.github/workflows/pages.yml`.
9. Settu lýsinguna **Upphafsútgáfa vefbókar STÆR3HD05** í Summary. Veldu **Commit to main** og síðan **Push origin**.

`dist/` fylgir pakkanum til að eiga tilbúna afritsútgáfu, en sést ekki í Changes því `.gitignore` undanskilur hana. Það er rétt: GitHub byggir hana aftur.

### Athugaðu rétta möppuskipan

Í **Code** á GitHub á `build_site.py` að sjást strax við hlið `README.md`. `.github/workflows/pages.yml` á að vera undir `.github`, ekki undir annarri `staer3hd05` möppu.

## 5. Fyrsta bygging — engin birting enn

1. Opnaðu **Actions** í geymslunni.
2. Finndu **Build and publish book** og opnaðu fyrstu keyrsluna.
3. **Build and check** á að verða grænt. Það byggir allar síður, athugar tengla og keyrir tölulegar prófanir á völdum heildum.
4. **Publish to GitHub Pages** á að vera merkt **Skipped**. Það er viljandi þar til `PUBLISH_PAGES` er virkjuð.

Ef Actions eru óvirkar samkvæmt reglum skólans þarf stjórnandi að heimila notkun opinberu GitHub Actions sem eru tilgreindar í YAML-skránni. Enga persónulega aðgangslykla eða geymslu-Secrets þarf fyrir þetta vinnuflæði.

**Staða prófana:** Pakkinn hefur verið byggður og prófaður í hreinni staðbundinni möppu. Keyrsla á raunverulegum GitHub-runner og réttindi reiknings skólans verða staðfest við þetta skref.

## 6. Virkja GitHub Pages þegar þú vilt birta

Ljúktu fyrst ákvörðun um sýnileika í skrefi 2. GitHub Pages er venjulega opin vefsíða; birtingin getur gert alla bókina, vísbendingar og lausnir aðgengilegar á netinu.

1. Farðu í **Settings → Pages** í geymslunni.
2. Undir **Build and deployment → Source** velurðu **GitHub Actions**. Ekki velja **Deploy from a branch** eða `/docs`; `docs` í þessum pakka geymir leiðbeiningar, ekki sjálfa bókina.
3. Farðu í **Settings → Secrets and variables → Actions → Variables**.
4. Veldu **New repository variable**.
5. **Name:** `PUBLISH_PAGES`. **Value:** `true` (lágstafir, án gæsalappa). Þetta er almenn breyta, ekki Secret.
6. Farðu í **Actions → Build and publish book → Run workflow**. Veldu greinina **main** og keyrðu.
7. Nú eiga bæði bygging og birting að verða græn.
8. Síðuslóðina finnurðu undir **Settings → Pages → Visit site** eða í birtingarverkefninu undir environment **github-pages**.

Venjuleg verkefnaslóð hefur formið `https://REIKNINGUR.github.io/staer3hd05/`. GitHub sýnir nákvæma slóð; þú þarft ekki að skrifa eigið reikningsheiti inn í kóða bókarinnar. Hýsing er ekki bundin þessu geymsluheiti.

Engin CNAME-skrá eða eigið lén er sett í pakkann. Ef skólinn vill eigið lén má bæta því við síðar.

## 7. Prófa áður en nýja slóðin verður aðalslóð

- Opnaðu forsíðuna og **Hefja lestur**.
- Prófaðu kaflavalmyndina og **Um vefbókina**.
- Athugaðu að formúlurnar séu settar upp; þetta reynir á MathJax-safnið frá jsDelivr.
- Opnaðu vísbendingu, frekari vísbendingu og lausn.
- Prófaðu rennistiku í einingu 2 og snúðsmyndir í einingu 8.
- Prófaðu **Næsta síða** og **Til baka** yfir einingamörk.
- Skoðaðu síðu í síma eða mjóum vafraramma og skiptu á milli ljósrar og dökkrar stillingar.
- Límdu beinan tengil að undirkafla í nýjan flipa og endurhladdu.

Haltu gömlu vinnuútgáfunni tiltækri þar til þetta er staðfest. Hún þarf ekki að vera eytt við flutninginn. Þegar GitHub-útgáfan hefur verið samþykkt veljum við hana sem eina aðalvinnuútgáfu og forðumst samhliða breytingar á tveimur stöðum.

## 8. Breyta eftir flutning

Bókin þarf ekki að vera fullbúin. Allur yfirlestur og þróun geta haldið áfram.

### Safna athugasemdum

Notaðu [breytingaskrána](BREYTINGASKRA.md) eða eigið skjal. Hafðu með einingu, síðu og dæmanúmer. Þú getur sent mér safn breytinga og fengið uppfærðar frumskrár til að setja inn.

### Lítil breyting í GitHub-vafranum

1. Veldu frumskrá samkvæmt [efniskortinu](EFNISKORT.md). Til dæmis er **Um vefbókina** í `assets/about.html`.
2. Smelltu á blýantinn, breyttu textanum og haltu töggum/táknum óbreyttum.
3. Veldu **Commit changes** og skrifaðu stutta lýsingu.
4. Ef þú vilt birta strax má vista á `main`. Bygging og birting keyra sjálfvirkt þegar `PUBLISH_PAGES=true`.
5. Ef þú vilt drög velurðu nýja grein, til dæmis `yfirlestur-eining-1`, og stofnar **Pull request**. Athuganir keyra þar en breytingarnar fara ekki á aðalvefinn fyrr en þú velur **Merge** yfir í `main`.

Vafra-Preview á GitHub sýnir ekki sjálfa gagnvirku bókina. Pull request fær í þessum pakka athuganir, en ekki sérstaka forskoðunarslóð. Til að skoða heila dragaútgáfu fyrir sameiningu þarf að byggja hana staðbundið eða setja upp sérstaka forskoðun síðar.

### Breyta með GitHub Desktop

Veldu **Fetch origin / Pull origin** áður en þú byrjar, breyttu frumskrám á tölvunni, skoðaðu Changes, veldu Commit og Push. Frumskrárnar eru að hluta Python með HTML-texta; lestu efniskortið. Ekki gera handvirkar breytingar eingöngu í `dist/`.

## 9. Ef þú vilt bakka

- **Afturkalla nýlega breytingu:** í GitHub Desktop, farðu í **History**, hægrismelltu á viðkomandi commit og veldu **Revert changes in commit**. Ýttu nýja afturköllunarcommitinu með Push. Notaðu ekki eyðingu geymslu eða force-push til að laga orðalag.
- **Stöðva nýjar sjálfvirkar birtingar:** breyttu `PUBLISH_PAGES` í `false`. Núverandi birt útgáfa stendur áfram; þetta tekur hana ekki af netinu.
- **Taka Pages-vefinn af netinu:** það er sérstök aðgerð í Pages-stillingum, ekki það sama og að stöðva sjálfvirkni.

## 10. Algengar hnökrar

| Vandamál | Hvað á að skoða |
| --- | --- |
| Ekkert birtist undir Actions | Er `.github/workflows/pages.yml` á réttum stað á `main`? Eru Actions heimilaðar? |
| Build grænt, Publish skipped | Er `PUBLISH_PAGES` repository **Variable** nákvæmlega `true`? Er keyrslan frá `main`, ekki pull request? |
| Pages er ekki í boði | Athugaðu réttindi, áskrift og sýnileika geymslu. Ekki opna frumskrár án þess að það sé ætlunin. |
| 403 eða vantar Pages-réttindi við birtingu | Source á að vera GitHub Actions. Stjórnandi getur þurft að yfirfara Actions- og environment-reglur skólans. |
| Bygging stöðvast eftir textabreytingu | Opnaðu rauða Build-skrefið. Athugaðu gæsalappir og hvort textafesta í `editorial_review.py` hafi breyst. |
| Vefur sýnir gamla textann | Athugaðu síðustu grænu birtingu og endurhladdu vafra. Röng frumskrá eða breyting í `dist/` getur verið orsökin. |
| Vefsíðan sýnir bara README eða leiðbeiningar | Röng Pages Source eða möppuskipan. Notaðu GitHub Actions sem birtir `dist`, ekki `/docs`. |
| Formúlur birtast sem kóði | Prófaðu nettengingu og hvort jsDelivr sé aðgengilegt á neti skólans. Bókin notar MathJax þaðan. |

## Stutt yfirlit yfir það sem þú gerir

1. Stofnar geymsluna hjá skólanum og flytur inn innihald pakkans.
2. Staðfestir græna byggingu.
3. Ákveður sýnileika og virkjar Pages þegar þú ert tilbúin.
4. Prófar bókina á nýju slóðinni.
5. Heldur áfram yfirlestri og breytingum í sömu geymslu.

## Opinberar heimildir

Leiðbeiningar og vinnuflæði miða við opinber gögn GitHub, skoðuð 5. nóvember 2026:

- [GitHub Pages: hvað þjónustan gerir og áskriftir](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [Val á birtingaruppsprettu](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Sérsniðin GitHub Actions-vinnuflæði fyrir Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Sýnileiki Pages-vefs og Enterprise-aðgangsstýring](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)
- [Klónun með GitHub Desktop](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
- [Breyta skrám í vafra](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
