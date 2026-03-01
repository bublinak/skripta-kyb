# Strojové učení (Machine learning - ML)

Strojové učení je podmnožina umělé inteligence (AI), která se zaměřuje na vývoj algoritmů a modelů, které se mohou učit a zlepšovat svůj výkon na základě dat, aniž by byly explicitně naprogramovány. ML umožňuje počítačům rozpoznávat vzory, dělat predikce a rozhodovat.

### Základní pojmy:

- **_Data:_**
    Základní stavební kámen ML. Algoritmy potřebují velké množství kvalitních dat.
- **_Modely:_**
    Matematické reprezentace, které se učí vztahy mezi vstupy (feature) a výstupy (labely).
- **_Trénování:_**
    Proces, při kterém se model učí z tréninkových dat.
- **_Testování:_**
    Ověření modelu na nových datech (testovacích sadách).
- **_Generalizace:_**
    Schopnost modelu fungovat dobře na neviděných datech.

## Typy strojového učení

- **_Učení s učitelem („supervised learning“)_** – pro vstupní data je určen správný výstup (třída pro klasifikaci nebo hodnota pro regresi).
- **_Učení bez učitele („unsupervised learning“)_** – ke vstupním datům není známý výstup.
- **_Kombinace učení s učitelem a bez učitele („semi-supervised learning“)_** – část vstupních dat je se známým výstupem, ale další data, typicky větší, jsou bez něj.
- **_Zpětnovazebné učení („reinforcement learning“)_**, též učení posilováním.

## Učení s učitelem (Supervised learning)

Učení s učitelem je metoda strojového učení, při které model trénuje na označených datech, kde každý vstup (vektor vlastností / feature vector) má odpovídající výstup (label). Cílem je naučit model predikovat výstup pro nové, neznámé vstupy.

### Data:

Každá položka vstupu je tedy vektor:

$$ x = [x_1, x_2, \ldots , x_n], \qquad x_i \in \mathcal{R}, $$

kde x_i jsou jednotlivé vlastnosti jednoho vstupu.

A každá položka má k ní odpovídající *label*, což je odpovídající výstup (od učitele). Celkem jde tedy o soubor dvojic dat 

$$\mathcal{D} = \{(x^{(i)}, y^{(i)})\}_{i=1}^{m}$$

kde každá taková dvojice odpovídá jednomu datu (objeku, záznamu, ...)


> Například, pokud budou jako vstupy různá auta, bude vektor $$x$$ popisovat sadu jejich vlastností. x = [barva, objem motoru, počet kol, počet sedadel, ...], celá trénovací sada pak bude více takových položek a k nim odpovídající labely.

### Rozdělení na trénovací a testovací sadu:

Cílem strojového učení není jen zapamatovat si trénovací data, ale naučit se zobecňovat – tedy správně reagovat i na nová, dosud neviděná data.

Pokud bychom model hodnotili na stejných datech, na kterých se učil, dostaneme zkresleně dobrý výsledek. Model si totiž může data „zapamatovat“ (přeučení / overfitting).

Proto dataset rozdělíme na dvě části:

- trénovací sada (train set) – slouží k učení modelu

- testovací sada (test set) – slouží k nezávislému ověření jeho kvality

Testovací data simulují reálné nasazení modelu v praxi.

#### Jak se train–test split provádí?

- Celý dataset se náhodně promíchá.

- Rozdělí se na dvě disjunktní části. Typicky: 70–80 % trénovací data a 20–30 % → testovací data

Důležité je, že:

- testovací data se nesmí používat při trénování

- testovací data se použijí až po dokončení učení

### Úlohy učení s učitelem:

## Regrese

Výstup je spojitá hodnota.

$$ y \in \mathcal{R} $$

Příklady:

- predikce ceny domu

- předpověď teploty

- odhad spotřeby energie

Model se snaží minimalizovat chybu mezi skutečnou a predikovanou hodnotou (např. střední kvadratickou chybu - MSE).

Regrese je úloha učení s učitelem, při které se snažíme najít funkci, která mapuje vstupní data na spojitou výstupní hodnotu.
Cílem je nalézt takovou funkci, která minimalizuje chybu mezi skutečnými hodnotami a predikcí modelu.
Speciálním případem je lineární regrese, kde model předpokládá lineární závislost mezi vstupy a výstupem a hledá přímku (resp. rovinu či nadrovinu), která data nejlépe aproximuje.

## Klasifikace

Výstup je diskrétní třída.


$$ y \in {1, 2, \ldots, K} $$

Typy klasifikace a příkaldy:

- Binární (např. spam / nespam)

- Multitřídní (např. rozpoznání číslice 0–9, rozpoznávání pes, kočka, pták, letadlo, ...)

Model rozhoduje, do které třídy vstup patří.

Klasifikace je úloha učení s učitelem, při které se snažíme najít funkci, která mapuje vstupní data na diskrétní výstupní třídu.
Cílem je nalézt takovou funkci, která co nejlépe rozlišuje jednotlivé třídy a minimalizuje počet chybných klasifikací.

## Lineární separabilita v klasifikaci

U klasifikace se snažíme najít rozhodovací hranici, která odděluje jednotlivé třídy v prostoru příznaků.

### Lineárně separabilní problém

Problém je lineárně separabilní, pokud existuje lineární rozhodovací hranice, která dokonale oddělí všechny třídy bez chyby.

V 2D prostoru je tato hranice přímka, ve 3D prostoru rovina, ve vyššícch dimenzích se nazývá obecně nadrovina.

Rozhodovací hranici lze zapsat jako:

$$
w^T x + b = 0
$$

kde:
- $w$ je vektor vah  
- $b$ je bias (posun)

Pokud lze najít takové $w$ a $b$, že všechny body jedné třídy splňují

$$
w^T x + b > 0
$$

a body druhé třídy

$$
w^T x + b < 0,
$$

pak je problém lineárně separabilní.

---

### Lineárně neseparabilní problém

Problém je lineárně neseparabilní, pokud neexistuje žádná lineární hranice, která by data dokonale oddělila.

V takovém případě je nutné zvolit jiný přístup:

- **Použít nelineární model**  
  Například neuronovou síť nebo rozhodovací strom, které dokáží vytvářet nelineární rozhodovací hranice (křivky místo přímek).

- **Transformovat data do vyšší dimenze**  
  Pomocí vhodné transformace příznaků lze původně neseparabilní data učinit separabilními v jiném prostoru.  
  Příkladem je přidání nových příznaků (např. $x_1^2$, $x_1 x_2$) nebo použití jádrové funkce (kernel trick) u metod jako SVM.

- **Připustit určitou klasifikační chybu (soft margin)**  
  V reálných datech často existuje šum nebo překryv tříd.  
  Model proto hledá rozhodovací hranici, která minimalizuje chybu, ale nemusí data oddělit dokonale.  
  Cílem je dobrá generalizace, nikoli perfektní oddělení trénovacích dat.


## Učení bez učitele (Unsupervised learning)

Učení bez učitele je metoda strojového učení, při které model pracuje pouze se vstupními daty bez známých výstupních hodnot (labelů).  
Cílem není predikovat konkrétní výstup, ale objevit skrytou strukturu, vzory nebo vztahy v datech.

### Data:

Každá položka vstupu je opět vektor:

$$
x = [x_1, x_2, \ldots , x_n], \qquad x_i \in \mathcal{R}
$$

Dataset tedy obsahuje pouze vstupy:

$$
\mathcal{D} = \{ x^{(i)} \}_{i=1}^{m}
$$

Na rozdíl od učení s učitelem zde neexistují odpovídající hodnoty $y^{(i)}$.

---

### Cíl učení bez učitele

Model se snaží:

- seskupovat podobná data dohromady,
- odhalovat strukturu dat,
- snižovat dimenzionalitu,
- identifikovat anomálie.

Nejde tedy o aproximaci známé funkce $f(x) \approx y$, ale o hledání vnitřní struktury dat.

---

## Úlohy učení bez učitele

### Shlukování (Clustering)

Cílem je rozdělit data do skupin (shluků) tak, aby si body v rámci jednoho shluku byly co nejvíce podobné a mezi shluky co nejméně podobné.

Příklady:
- segmentace zákazníků
- rozdělení dokumentů podle tématu
- seskupování obrázků

Typický algoritmus:
- K-means

---

### Redukce dimenzionality

Cílem je snížit počet příznaků při zachování co největšího množství informace.

Použití:
- vizualizace vícerozměrných dat
- zjednodušení modelu
- odstranění šumu

Typický algoritmus:
- PCA (Principal Component Analysis)

---

### Detekce anomálií

Cílem je najít data, která se výrazně liší od ostatních.

Příklady:
- detekce podvodů
- odhalení chyb v systému
- monitorování bezpečnosti


## Učení posilováním (Reinforcement learning)

Učení posilováním je metoda strojového učení, při které se agent učí rozhodovat prostřednictvím interakce s prostředím.  
Na rozdíl od učení s učitelem zde nejsou k dispozici správné odpovědi (labely).  
Agent dostává zpětnou vazbu ve formě odměny nebo trestu a jeho cílem je maximalizovat celkovou dlouhodobou odměnu.

---

### Základní prvky:

- **Agent** – rozhodovací jednotka (model).
- **Prostředí (environment)** – svět, ve kterém agent působí.
- **Stav (state) $s$** – aktuální situace prostředí.
- **Akce (action) $a$** – rozhodnutí, které agent provede.
- **Odměna (reward) $r$** – číselná zpětná vazba po provedení akce.
- **Politika (policy) $\pi(a|s)$** – strategie, podle které agent volí akce.

---

### Princip učení

V každém kroku:

1. Agent pozoruje aktuální stav $s_t$.
2. Zvolí akci $a_t$.
3. Prostředí vrátí novou situaci $s_{t+1}$ a odměnu $r_t$.
4. Agent upraví svou strategii tak, aby maximalizoval budoucí součet odměn.

Cílem je maximalizovat očekávanou kumulativní odměnu:

$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}
$$

kde:
- $\gamma \in (0,1)$ je diskontní faktor (určuje důležitost budoucích odměn).

---

## Příklady použití

- hraní her (např. šachy, Go)
- autonomní řízení
- robotika
- řízení průmyslových procesů
- optimalizace strategií
