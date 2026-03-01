# Support Vector Machine (SVM)

## Co je SVM
Support Vector Machine (SVM) je metoda strojového učení určená pro **klasifikaci** a **regresi**.  
Používá se hlavně k rozdělení dat do dvou tříd.  
Patří mezi **lineární klasifikátory**, ale díky tzv. *kernelům* dokáže řešit i **nelineární problémy**.

---

## Hlavní myšlenka
SVM hledá **rozhodovací hranici (hyperrovinu)**, která nejlépe odděluje data dvou tříd.

Nejde jen o jakoukoli přímku, ale o tu, která má **největší možný odstup (margin)** od nejbližších bodů obou tříd.

Tyto nejbližší body se nazývají **support vectors** – podpůrné vektory.

---

## Intuice
Představ si dva shluky bodů (např. červené a modré).  
Existuje mnoho čar, které je mohou rozdělit, ale SVM vybere tu, která:

1. **odděluje třídy správně**, a  
2. **je od nich co nejdál**.

Tím zajišťuje, že klasifikátor bude **stabilní a méně citlivý na šum**.

---

## Matematicky (zjednodušeně)
SVM hledá přímku (v 2D) nebo rovinu (v nD):

w·x + b = 0

takovou, aby pro všechny body platilo:

yᵢ (w·xᵢ + b) ≥ 1

a zároveň minimalizovalo velikost vah:

min ||w||²

To zajišťuje maximální vzdálenost od obou tříd (maximalizaci marginu).

---

## Když data nejsou dokonale oddělitelná
V praxi se často třídy **překrývají**.  
SVM proto umožňuje malé chyby pomocí tzv. **měkkého marginu (soft margin)**.

Každý bod může být na špatné straně hranice, ale platí penalizace za chybu.  
Model hledá kompromis mezi:
- **velkým marginem** (obecnost) a
- **malou chybovostí** (přesnost na tréninku).

---

## Nelineární SVM (kernel trick)
Pokud data **nejdou rozdělit přímkou**, SVM je dokáže **převést do vyšší dimenze**, kde už lineárně oddělitelná jsou.

To dělá pomocí tzv. **jádrové funkce (kernel)**.

Běžné typy kernelů:
- **lineární kernel** – pro lineární úlohy
- **polynomiální kernel** – pro zakřivené hranice
- **RBF (Gaussovský) kernel** – pro složité, nepravidelné hranice

Pomocí kernelu tak SVM zvládne i nelineární klasifikaci bez explicitního přepočtu do vyšší dimenze.

---

## Shrnutí principu

| Krok | Popis                                                                      |
|------|----------------------------------------------------------------------------|
| 1    | Najdi přímku/rovinu, která odděluje třídy.                                 |
| 2    | Vyber takovou, která maximalizuje vzdálenost od nejbližších bodů (margin). |
| 3    | Tyto body jsou podpůrné vektory (support vectors).                         |
| 4    | Umožni malé chyby (soft margin) – lepší odolnost proti šumu.               |
| 5    | Pomocí kernelu umožni nelineární rozdělení.                                |

---

## Výhody
- Funguje dobře i s malým množstvím dat.
- Dobře se chová při vysoké dimenzi (mnoho vstupních znaků).
- Lze přizpůsobit různým typům dat pomocí kernelů.
- Obvykle se vyhne přeučení (overfittingu).

---

## Nevýhody
- Pomalejší trénink pro velmi velké datasety.
- Nutnost zvolit vhodný kernel a jeho parametry.
- Hůře interpretovatelný než jednoduché lineární modely.

---

## Příklad rozhodovací hranice
V 2D je hranicí přímka:
w₁·x₁ + w₂·x₂ + b = 0

- body na jedné straně → třída +1  
- body na druhé straně → třída -1  
- body nejblíže hranici → support vectors

---

## Shrnutí
Support Vector Machine hledá **nejrobustnější hranici mezi třídami** – takovou, která maximalizuje odstup od obou tříd.  
Díky jádrovým funkcím dokáže vytvářet i **nelineární hranice** a patří mezi nejvýkonnější klasifikátory pro mnoho typů dat.
