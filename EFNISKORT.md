# Efniskort og ritstjórn

## Mikilvægasta aðgreiningin

**Það sem sést í vafra er í `dist/`. Frumtextinn er í Python-skrám og `assets/`.** GitHub Actions endurskapar vefsíðuna úr þeim frumskrám. Breyting eingöngu á útbúinni HTML-síðu endist ekki við næstu byggingu.

Þetta er núverandi höfundakerfi bókarinnar, ekki Markdown-bók eða Sphinx/Edbook. Ekki þarf að endurskrifa hana í öðru kerfi til að hýsa hana á GitHub.

## Hvar er efnið?

| Birt eining / hluti | Helstu frumskrár |
| --- | --- |
| Forsíða og stuttir kynningartextar | `frontpage.py` |
| Um vefbókina | `assets/about.html` |
| Haus, meginútlit og grunnur einingar 1 | `build.py`, `build_book.py`, `frontpage.py` |
| 1. Stofnföll og óákveðin heildi | `build.py` |
| 2. Ákveðið heildi og uppsöfnun | `unit_content.py`, `units[2]` |
| 3. Flatarmál og hagnýting heilda | `units78.py`, höfundareining 7 |
| 4. Heildun með innsetningu | `unit3.py` (grunnur í `unit_content.py`) |
| 5. Hlutheildun | `unit4.py` (grunnur í `unit_content.py`) |
| 6. Ræð föll og stofnbrot | `unit5.py` (grunnur í `unit_content.py`) |
| 7. Að velja heildunaraðferð | `unit6.py` (grunnur í `unit_content.py`) |
| 8. Rúmmál snúða | `units78.py`, `solid_widgets.py`, `assets/cone.html` |
| 9. Deildajöfnur og upphafsskilyrði | `unit9.py` |
| 10. Óhliðraðar deildajöfnur | `unit10.py` |
| 11. Hliðraðar deildajöfnur | `unit11.py` |
| 12. Aðskiljanlegar deildajöfnur | `unit12.py` |
| 13–15. Runur, raðir og þrepun | `units1315.py` |
| Ritstjórnarviðbætur við sýnidæmi og skýringar | `editorial_review.py`, númerað eftir **birtum** einingum |
| Endurnúmerun og röð eininga 2–8 | `book_order.py` |
| Vinstri valmynd og samsetning allra síðna | `build_book.py` |
| Forsíðuútlit og ME-merki í haus | `assets/frontpage.css`, `assets/me-logo.png` |
| Valmynd á mjóum skjám | `assets/navigation.css`, `assets/navigation.js` |
| Gagnvirk gröf og myndir | JavaScript-skrár í `assets/`; sumar athafnir einnig í `build.py` og `build_book.py` |
| Síðufótur | `book_footer.py` — `ENABLED = False`, eins og samþykkt var |

## Hvers vegna samsvara skráarnöfnin ekki alltaf kaflanúmerunum?

Flatarmálsefnið var fært framar í bókina. Til að varðveita efnið var endurnúmerun sett í `book_order.py`. Birt eining 4 kemur því úr höfundareiningu 3, birt 5 úr 4, birt 6 úr 5 og birt 7 úr 6. Flatarmál er höfundareining 7 en birt eining 3. Breyttu ekki þessum númerum sjálfvirkt í öllum skrám.

## Örugg byrjun á orðalagsbreytingu

1. Skráðu síðuna, dæmanúmerið og nákvæma textann sem á að breyta.
2. Leitaðu að textanum í geymslunni. Skoðaðu hvort hann er í `editorial_review.py` eða í grunnskránni.
3. Breyttu aðeins textanum. Haltu Python-gæsalöppum, HTML-tögum og stærðfræðitáknum óbreyttum nema ætlunin sé sérstaklega að breyta þeim.
4. Láttu byggingu og athuganir ljúka. Ef ritstjórnarstaðfesting (`AssertionError` með einingar- og síðunúmeri) bregst þarf að samræma grunntexta og ritstjórnarlag; ekki eyða staðfestingunni til að fela villuna.
5. Skoðaðu sjálfa síðuna í vafra, ekki aðeins græna niðurstöðu athugunar.

Auðveldasta skráin til að prófa fyrstu breytingu er `assets/about.html`. Texti er þar venjulegt HTML. Til dæmis má breyta orðalagi innan `<p>…</p>` án þess að breyta töggunum.

Við stærri yfirferð getum við unnið úr breytingalistanum saman og skilað uppfærðum frumskrám. Þegar GitHub verður aðalvinnustaðurinn þarf alltaf að byrja á nýjustu útgáfu þaðan, svo nýlegum breytingum sé ekki skrifað yfir.
