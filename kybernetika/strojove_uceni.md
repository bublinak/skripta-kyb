# Strojové učení


- jedná se o podoblast umělé inteligence.

- zabývá se technikami (algoritmy) umožňujícími systému řešit úlohy bez explicitního programování pro danou úlohu.

- analogie s učením člověka - systém během procesu učení změní svůj vnitřní stav tak, aby zlepšoval svoje výstupy.

- má široké uplatnění v mnoha oborech (výpočetní technika, robotika, ekonomie, sociologie, lékařství, ...)

## Základní algoritmy učení

- učení s učitelem ("supervised learning"): učení probíhá na základě znalosti vstupních dat a jim odpovídajícím (požadovaným) výstupům.

- učení bez učitele ("unsupervised learning"): učení probíhá na základě znalosti pouze vstupních dat. Systém sám musí identifikovat strukturální vlastnosti vstupních dat.

- *kombinace učení s učitelem a bez učitele* ("semi-supervised learning): část učení probíhá metodou učení s učitelem a část (zpravidla větší část) probíhá metodou učení bez učitele.

- učení posilováním neboli zpětnovazební učení ("reinforced learning): systém se učí jak pracovat v prostředí tak aby maximalizoval odměnu. (Systém nepracuje s daty tak jako u předchozích případů, ale pracuje pomocí zkoušení a omylů, jaké akce vedou k největší odměně.)

## Některé základní úlohy

- Klasifikace: Rozdělování vstupních dat do tzv. tříd (classes). Typicky učení s učitelem, systém dostává během trénování dvojici data-třída (vstup-požadovaný výstup) a mění svůj vnitřní stav tak, aby po skončení trénovací fáze na zadaný vstup odpověděl požadovaným výstupem. *Příkald: Klasifikace živočišného druhu na základě fotografie.*

- Regrese: Systém odhaduje číselné hodnoty (výstup) na základě vstupních dat. Jedná se o úlohy inteligentní interpolace nebo extrapolace dat. Typicky učení s učitelem. *Příklad: Odhad ceny bytu na základě údajů z trhu při zohlednění vstupních parametrů jako je např. lokalita, velikost bytu, počtu místností, pod.*

- Shlukování: Zařazování dat do skupin podle podobnosti vlastností. Typicky učení bez učitele. Cílem je, rozdělení dat do shluků tak, aby data s podobnými vlastnostmi byly součástí stejného shluku a data v různých shlucích byla od sebe odlišná. *Příklad: Rozdělení zákazníků do skupin v obchodě podle jejich nákupních zvyklostí.*

- Prohledávání prostoru řešení: např. Genetický algoritmus. (učení posilováním) Algoritmus prohledávání prostoru vlastností vhodných pro dané prostředí (vyjádřené hodnotící funkcí). Algoritmus napodobuje proces přirozeného výběru. Křížením a mutací vlastností se získávají nové vlastnosti. Nejvhodnější vlastnosti mají vyšší pravděpodobnost přenosu do další generace. *Příklad: Programování úrovní ve videohře. Cílem je automatizovat proces generování úrovní, aby byly zajímavé, hratelné a vyvážené, čímž se sníží náklady a čas potřebný na vývoj.*




