# Základní pojmy a principy

Kybernetika se svým pojetím liší od ostatních věd (fyziky, chemie, biologie, ...). Odlišnost spočívá v tom, že ony vědy vidí reálný svět jako svět interakcí (vzájemné působení entit reálného světa), zatím co kybernetika ho vidí jako svět, kde něco plyne od někud někam, tedy jedním směrem, může to být nějaký rozruch v reálném světě nebo jindy informace. Je to pohled, který vznikl při studiu principu zpětné vazby, a který byl pro kybernetiku určující. Poznání reálného světa se tedy odehrává pod jiným zorným úhlem a s jinou interpretací. Tento odlišný pohled začal vznikat ve 20. letech dvacátého století v rodící se elektronice a sdělovací technice. Tímto viděním se potkává s teorií informace a sdělování, a nabízí jim včlenění do společného oboru. 
  
* **Model:** Systematické studium různých systémů vedlo k poznatku, že systémy různé fyzikální podstaty mohou mít velmi podobné chování a že chování jednoho systému můžeme zkoumat prostřednictvím chování jiného, snáze realizovatelného systému ve zcela jiných časových či prostorových měřítkách. Ukázalo se, že mnohé systémy mechanické, hydraulické, pneumatické, tepelné ad. jsou popsány formálně stejnými diferenciálními rovnicemi jako elektrické obvody. To vedlo ke vzniku speciálnich elektrických obvodů analogových počítačů. Brzy však byly vytlačeny symbolickými modely na číslicových počítačích.
* **Informace:** Postupně vznikla exaktní teorie informace jako odnož teorie pravděpodobnosti. Informace doplnila náš fyzikální obraz světa v tom smyslu, že jde o stejně důležitou entitu, jako je hmota či energie. Informace je zřejmě nejfrekventovanějším pojmem, který kybernetika přinesla. Zpracování informace se stává stále důležitějším a pomalu ale jistě mění charakter našeho života.
* **Zpětná vazba:** Princip zpětné vazby byl znám již dříve v regulační technice a používal se při návrhu zpětnovazebních zesilovačů pro účely sdělovací techniky. Zakladatelé kybernetiky ale rozpoznali, že jde o velmi obecný princip. Je především zásluhou kybernetiky, že se stal obecně známým a umožnil vysvětlit řadu dějů odehrávajících se v nejrůznějších dynamických systémech.


## Základní kybernetické přístupy:
* **Systémový přístup:** Modelovaný systém lze rozkládat (dekompozice) nebo naopak různé systémy spojovat (agrerace), popis systému probíhá zpravidla od jednoduššího ke složitějšímu.

* **Informační přístup:** Konání je prováděno na základě znalosti "věci".

* **Řídíci přístup:** Cílevědomé dosahování požadované kvality.

## Pojmy:

* **Systém:** soubor určitého množství prvků ($S_i$)navzájem spolu souvisejících ($R_i$) a nějak vázaných na svoje okolí. Jedná se tedy o pojem k označení zkoumané části objektivní reality vydělené z okolního světa za účelem poznání.

<img src="img/system_obecne.drawio.png">

$S = \set{S_i,R_i}$
>Systém $S$ je definován jako množina prvků $S_i$ a jejich vzájemnými relacemi $R_i$ reprezentujícími vzájemné funkční vztahy jednotlivých prvků a vztah systému k jeho okolí.

### Klasifikace systémů
* **Fyzikální systém:** objekt - soubor fyzikálních zařízení, spojených určitým počtem příznaků, důležitých z hlediska praktického použití (např.: motor, operační zesilovač, procesorová deska, RLC obvod, ...)
* **Abstraktní systém:** matematický model - je množina proměnných a množina relací mezi těmito proměnnými (např. dynamické rovnice, přenos, diferenciální rovnice, Ohmův zákon, ...) 

---
* **Neorientovaný systém** * - systém s dvojicí vstupu a výstupu

<img src="img/neorientovany_system.drawio.png">

* **Orientovaný systém:** - proměnné se dělí na vstupní a výstupní proměnné (nezávislé, závislé proměnné)

<img src="img/system.drawio.png">

* **Kauzální systémy:** jsou takové systémy, jejichž chování v přítomnosti závisí na hodnotách vstupů v minulosti a přítomnosti. Respektují kauzální vztah příčiny a následku. Tyto systémy jsou fyzikálně realizovatelné.
  
* **Nekauzální systémy:** jsou takové systémy, jejichž chování v přítomnosti závisí na hodnotách v minulosti, přítomnosti, ale i budoucnosti. Tyto systémy nerepektují kauzální vztah příčiny a následku, mají tedy "schopnost předvídat". Tyto systémy jsou fyzikálně nerealizovatelné.

---

* **Deterministické systémy:** vykazují při opakovaném využití stejné chování při zachování stejných počátečních podmínek.
  
* **Stochastické systémy:** ve systému je přítomna náhoda i když jsou počáteční podmínky stejné (řeší se zpravidla pomocí pravděpodobnostních modelů).

### Systém se zpětnou vazbou
![systém se zpětnou vazbou](https://github.com/skely/SPSE-KYB/blob/main/img/zp%C4%9Btn%C3%A1%20vazba.drawio.png)

### Popisy systému:
* **Vnější popis systému:** spočívá ve vyjádření dynamických vlastností mezi vstupem a výstupem. Systém se považuje za černou skříňku (black box), která má vstup a výstup (obecně může mít více vstupů a výstupů). Vnější popis (lineárního spojitého dynamického) systému s jednou vstupní a jednou výstupní veličinou může být představován:
  * diferenciální rovnicí
  * přenosem (v Laplaceově transformaci)
  * přechodovou funkcí a přechodovou charakteristikou
  * impulzní funkcí a impulzní charakteristikou
  * frekvenčním přenosem a frekvenční charakteristikou
  * rozložením pólů a nul přenosu
* **Vnitřní popis systému:** sleduje dynamické vlastnosti systému v závislosti na vstupu, vnitřním stavu a výstupu. 

