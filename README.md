# STÆR3HD05 — Heildun, deildajöfnur, runur og raðir

Vinnuútgáfa gagnvirkrar vefbókar fyrir Menntaskólann á Egilsstöðum.

**Byrjaðu hér:** [Flutningur á GitHub, skref fyrir skref](docs/GITHUB_LEIDBEININGAR.md).

Í afhendingarpakkanum er líka `BYRJADU_HER.html`, sem má opna beint í vafra.

## Hvað er í verkefninu?

- Allar frumskrár, myndir og gagnvirkni bókarinnar.
- `build_site.py`: ein skipun til að byggja alla bókina.
- `.github/workflows/pages.yml`: sjálfvirk bygging, athuganir og valfrjáls birting á GitHub Pages.
- `docs/EFNISKORT.md`: hvar efnið er skrifað og hvernig kaflanúmer tengjast skránum.
- `docs/BREYTINGASKRA.md`: tafla til að safna athugasemdum við yfirlestur.
- `scripts/check_site.py`: athugun á staðbundnum tenglum, myndum og stuðningshnöppum.
- `verify_math.py`: tölulegar athuganir á völdum heildum; þetta er ekki full stærðfræðileg yfirferð.

`dist/` í ZIP-pakkanum er tilbúin vefsíða. Git hunsar þá möppu því hún er byggð aftur úr frumskrám í hverri keyrslu. **Breyttu frumskrám, ekki skrám í `dist/`.**

## Byggja og skoða á eigin tölvu

Python 3.12 eða nýrra nægir. Enga Python-aukpakka þarf.

```sh
python build_site.py
python scripts/check_site.py
python verify_math.py
python -m http.server 8000 --directory dist
```

Opnaðu síðan `http://localhost:8000/`. Á Windows má nota `py -3.12` í stað `python` ef Python-ræsirinn er uppsettur. Stöðvaðu vefþjóninn með Ctrl+C.

**Ekki keyra aðeins `build.py`.** Sú skrá býr aðeins til grunn einingar 1. `build_site.py` keyrir alla bygginguna og samræminguna.

## Hýsing

Bókin er kyrrstæð vefsíða: HTML, CSS, JavaScript og myndir. Hún þarf engan gagnagrunn, API-lykil eða tengingu við fyrri hýsingu. Allar leiðir innan bókarinnar eru afstæðar og henta verkefnasíðu á GitHub Pages.

Formúlubirting notar áfram **MathJax 3 frá jsDelivr** (`https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js`). Þessi almenna forritasafnsháð er óbreytt frá vinnuútgáfunni. Hún krefst nettengingar fyrir rétta formúlubirtingu; MathJax-safnið sjálft er ekki innifalið. Ef skólinn vill líka hýsa það safn sjálfur má gera það síðar.

**Sjálfvirk birting er óvirk í upphafi.** Settu GitHub Pages Source á GitHub Actions og geymslubreytuna `PUBLISH_PAGES` á `true` þegar þú vilt birta. Nánar í leiðbeiningunum. Fyrir þann tíma keyra byggingar og athuganir eingöngu.

## Breytingar og útgáfur

Bókin má halda áfram að þróast eftir flutning. Breytingar fara í frumskrár, eru vistaðar sem Git-commit og bókin byggist aftur sjálfvirkt. Breytingar á `main` fara á vefinn ef birting hefur verið virkjuð; drög má vinna á sérstakri grein.

Núverandi frumskrár eru Python með innfelldum HTML- og stærðfræðitexta. Kaflar 3–7 eru endurnúmeraðir við byggingu og `editorial_review.py` leggur ritstjórnarbreytingar ofan á grunntexta. Lestu efniskortið áður en þú breytir slíku efni. Ritstjórnarlagið sannreynir textafestur og getur stöðvað byggingu ef þeim er breytt; uppfæra þarf samhangandi staði saman.

## Uppruni pakkans

Útflutningur úr varðveittri frumgeymslu 5. nóvember 2026, commit `b6ff99d4cb5716ef608ea814fd1fdbe40e77eb3c` (síðan „Um vefbókina“ komin inn, síðufótur tekinn út). Engum breytingum hefur verið ýtt í þá geymslu við gerð þessa pakka. Námsefnið er óbreytt í útflutningnum; við bætast færanleg bygging, athuganir og leiðbeiningar.

Fyrri hýsingarstillingar, auðkenni hýsingarþjónustu, aðgangsupplýsingar og vinnsluskrár fylgja ekki. Pakkinn stofnar nýja Git-sögu við innflutning; fyrri breytingasagan fylgir ekki ZIP-skránni.

Ekki hefur verið valið sérstakt opið birtingarleyfi fyrir þennan pakka. Skólinn getur tekið afstöðu til leyfis og höfundarmerkinga fyrir opinbera útgáfu. Merki skólans er varðveitt óbreytt.
