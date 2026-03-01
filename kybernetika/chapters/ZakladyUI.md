# Zákaldy umělé inteligence

## Základní pojmy

### Inteligence

je komplexní a mnohostranný pojem, který se vztahuje na schopnost myslet, chápat, učit se, řešit problémy, přizpůsobovat se novým situacím a vytvářet nové myšlenky. Definice inteligence se liší v závislosti na kontextu a oboru, který ji zkoumá, jako je psychologie, filozofie, informatika nebo biologie.

Obecná definice **inteligence**:

- Schopnost adaptace: Přizpůsobení se změnám a prostředí.
- Schopnost řešení problémů: Analýza a hledání efektivních řešení.
- Schopnost učení: Získávání, uchovávání a aplikace nových informací.
- Abstraktní myšlení: Pochopení složitých konceptů, symbolů a vztahů.
---

### Umelá inteligence
je technologie (také název oboru), která se zabývá vytvářením strojů a systémů schopných vykonávat úkoly, které by normálně vyžadovaly lidskou inteligenci. To zahrnuje schopnosti jako například učení, uvažování, plánování, rozhodování, zpracování přirozeného jazyka nebo rozpoznávání obrazů.

formální definice **umělé inteligence**:

- Umělá inteligence je věda a inženýrství tvorby inteligentních strojů. - John McCarthy (1956)
- Umělá inteligence je studium toho, jak umožnit strojům jednat tak, aby jejich chování bylo považováno za inteligentní. - Russell & Norvig (1995) 
- Turingův koncept „strojů myslících“ a definoval test (Turingův test) jako způsob, jak určit, zda je stroj schopen inteligentního chování nerozeznatelného od člověka. - Alan Turing (1950)

### Experimenty pro zkoumání umělé inteligence:

**Turingův test**
- Autor: Alan Turing (1950).
- Cíl: Určit, zda stroj dokáže vykazovat inteligentní chování nerozeznatelné od lidského.
- Princip:
  - Osoba (rozhodčí) komunikuje s počítačem a člověkem prostřednictvím textového rozhraní.
  - Pokud rozhodčí nedokáže spolehlivě určit, kdo je člověk a kdo stroj, pak stroj prošel Turingovým testem.
- Kritika:
  - Test měří pouze schopnost stroje napodobit lidské chování, ne skutečnou inteligenci nebo vědomí.
  - Nevztahuje se na úlohy, kde není jazyk rozhodující.
 
**Čínský pokoj**

- Autor: John Searle (1980).
- Cíl: Zpochybnit, že schopnost stroje simulovat inteligentní chování znamená, že rozumí nebo má vědomí.
- Princip:
  - Představte si člověka, který sedí v místnosti a dostává čínské znaky, na které má reagovat podle předem daných pravidel (např. slovník).
  - Osoba v místnosti nemusí rozumět čínštině, ale zvenku to vypadá, že plynule komunikuje.
  - Argument: Počítače podobně jen manipulují symboly bez skutečného pochopení.
- Kritika:
  - Někteří tvrdí, že systém jako celek (místnost, pravidla, člověk) by mohl vykazovat pochopení, i když jednotlivé části ne.

---
### Hard AI vs Soft AI

**Soft AI (Narrow AI)**
- Zaměřena na konkrétní úkoly nebo oblasti.
- Dokáže provádět úkoly, které byly explicitně naprogramovány nebo naučeny na základě dat.
- Funguje pouze v rámci omezeného kontextu a nemá schopnost generalizace.
- Nemá vědomí, schopnost porozumění nebo samostatné rozhodování mimo definovaný rámec.

Příklady:
- Rozpoznávání obrazu: Systémy, které dokážou identifikovat objekty nebo tváře na fotografiích.
- Hlasoví asistenti: Siri, Alexa, Google Assistant – schopní odpovídat na otázky nebo provádět úkoly na základě hlasových pokynů.
- Doporučovací systémy: Netflix, Spotify, YouTube – nabízejí obsah na základě uživatelských preferencí.
- Autonomní vozidla: Specializované na řízení, rozpoznávání překážek a plánování trasy.
- Prediktivní modely: Diagnostika nemocí, detekce podvodů ve finančnictví.

Výhody:
- Vysoká efektivita a přesnost při řešení úzkých a specifických problémů.
- Snadná implementace v praktických aplikacích.
- Bezpečnější než Hard AI, protože nemůže přejít mimo svůj specifický úkol.

Nevýhody:
- Neschopnost učit se a přizpůsobovat novým úkolům mimo oblast, na kterou byla navržena.
- Závislost na datech a programování – omezená flexibilita.
- Neumí porozumět širšímu kontextu nebo obecným problémům.

**Hard AI (General AI)**
- Snaží se vytvořit systémy schopné obecné inteligence, podobné lidské schopnosti uvažovat, učit se a rozhodovat.
- Dokáže vykonávat širokou škálu úkolů, přizpůsobovat se novým situacím a řešit neznámé problémy.
- Má hypoteticky schopnost samostatného myšlení, plánování a generalizace poznatků.
- Zahrnuje prvky vědomí, porozumění a kreativity.

Cíle:
- Vytvořit inteligenci, která dokáže přemýšlet, učit se a jednat nezávisle na člověku.
- Napodobit nebo překonat lidskou inteligenci.

Příklady:
- Zatím žádné skutečné příklady neexistují, protože Hard AI je v současnosti teoretickým cílem.
- Fikční příklady: HAL 9000 (film 2001: Vesmírná odysea), Skynet (Terminátor), Jarvis (Iron Man).

Výhody:
- Potenciál řešit širokou škálu problémů, které dosud nebyly automatizovány.
- Schopnost přizpůsobit se novým podmínkám a úkolům bez nutnosti programování.
- Mohla by přinést revoluci v oblastech, jako je medicína, věda, energetika nebo klimatologie.

Nevýhody a výzvy:
- Technologická náročnost: Současná AI není schopna dosáhnout obecné inteligence.
- Etické otázky: Jak zajistit, že bude Hard AI bezpečná a neohrozí lidskou existenci?
- Kontrola: Obava, že vysoce inteligentní systémy se stanou neřízené a nepředvídatelné.
- Výpočetní výkon: Potřeba obrovských zdrojů pro simulaci obecné inteligence.

---
## Nástroje umělé inteligence

### Strojové učení (Machine Learning - ML)

- Podobor AI, který umožňuje systémům učit se a zlepšovat svůj výkon na základě dat bez explicitního programování.
- Hlavní metody:
  - Supervised learning (učení s učitelem) (klasifikace, regrese).
  - Unsupervised learning (učení bez učitele) (shlukování, redukce dimenzionality).
  - Reinforcement Learning (Posilované učení / učení posilováním).
- Aplikace: Prediktivní analýza, doporučovací systémy, analýza dat, zdravotnictví.

### Hluboké učení (Deep Learning - DL)

- Využívá hluboké neuronové sítě k analýze a porozumění složitým datovým vzorům.
- Typy neuronových sítí:
  - Konvoluční neuronové sítě (CNN) – Zpracování obrazu.
  - Rekurentní neuronové sítě (RNN) – Zpracování sekvenčních dat.
  - Transformery – Zpracování přirozeného jazyka.
- Aplikace: Rozpoznávání obrazu, generování textu, autonomní vozidla.

### Expertní systémy

- Systémy založené na pravidlech a databázích znalostí, které simulují rozhodování odborníků.
- Aplikace:
  - Lékařské diagnózy.
  - Technická podpora.
  - Řízení rizik.

### Bayesovské systémy 
- Pravděpodobnostní modely založené na Bayesově teorému, který umožňuje aktualizaci pravděpodobností na základě nových informací. Pracují s nejistotou a umožňují efektivní rozhodování, modelování závislostí a predikce.
- Hlavní metody:
  - Naivní Bayes - Jednoduchý klasifikační algoritmus, předpokládá nezávislost mezi atributy. Použití: Klasifikace textu, spam filtry.
  - Bayesovské sítě - Grafické modely, které znázorňují pravděpodobnostní vztahy mezi proměnnými. Použití: Diagnostika, plánování, modelování komplexních systémů.
  - Bayesovská inference: - Postup aktualizace pravděpodobností na základě nových dat. Použití: Dynamické modely, sledování časových řad.
  - Bayesovské filtrování: - Používá se k predikci a odstranění šumu v datech. Použití: Sledování objektů, robotika (např. Kalmanův filtr).
 
### Genetické algoritmy
- Genetické algoritmy (GA) jsou optimalizační metody inspirované evoluční teorií a principy přirozeného výběru. Simulují evoluční procesy, jako jsou mutace, křížení a selekce, aby našly optimální řešení komplexních problémů.
- Genetické algoritmy jsou silný nástroj pro hledání optimálních řešení a jsou hojně využívány v širokém spektru aplikací od inženýrství po vědecký výzkum.

