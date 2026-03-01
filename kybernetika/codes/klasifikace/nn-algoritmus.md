# Algoritmus k-nejbližších sousedů (k-NN)

## Cíl
Klasifikovat nový (neznámý) bod podle tříd jeho nejbližších sousedů v trénovacích datech.

---

## Postup algoritmu krok za krokem

### 1. Příprava dat
Máme sadu trénovacích dat:
(x₁, y₁), (x₂, y₂), …, (xₙ, yₙ)

kde xᵢ jsou vstupní vektory (např. souřadnice bodů)  
a yᵢ jsou známé třídy (např. červená / modrá).

---

### 2. Nastavení parametru k
Zvolíš číslo k – kolik nejbližších sousedů chceš při klasifikaci brát v úvahu.  
Typicky malé liché číslo: 1, 3, 5, 7…

---

### 3. Výpočet vzdálenosti od všech trénovacích bodů
Pro nový (testovací) bod x_new spočítej jeho vzdálenost ke každému trénovacímu bodu:

dᵢ = distance(x_new, xᵢ)

Nejčastěji používáme Eukleidovskou vzdálenost:

dᵢ = √((xᵢ₁ − x_new₁)² + (xᵢ₂ − x_new₂)²)

---

### 4. Seřazení sousedů podle vzdálenosti
Seřaď všechny trénovací body podle rostoucí vzdálenosti dᵢ.  
Vyber k nejbližších sousedů.

---

### 5. Hlasování o třídě
Z těchto k sousedů zjisti, jaké mají třídy.  
Spočítej, která třída se vyskytuje nejčastěji.  
Třída s největším počtem hlasů je výsledná třída bodu x_new.

---

### 6. (Volitelně: vážené hlasování)
Blízkým sousedům můžeš dát větší váhu (např. 1 / dᵢ).  
Potom se místo prostého počtu hlasů používá součet vah podle tříd.

---

### 7. Výsledek
Bod x_new dostane třídu, která „vyhrála“ hlasování.  
Pro každý nový bod proces opakuješ.

---

## Shrnutí algoritmu

| Krok | Co dělá              | Výsledek                       |
|------|----------------------|--------------------------------|
| 1    | Měj trénovací data   | Body s třídami                 |
| 2    | Zvol k               | Kolik sousedů použít           |
| 3    | Spočítej vzdálenosti | Seznam (vzdálenost, třída)     |
| 4    | Seřaď                | Najdi k nejbližších            |
| 5    | Hlasování            | Urči třídu podle většiny       |
| 6    | (volitelné) vážení   | Blízcí sousedi mají větší vliv |
| 7    | Výsledek             | Predikovaná třída bodu         |

---

## Příklad

Tréninková data:

| Bod | x₁ | x₂ | Třída |
|-----|----|----|-------|
| A   | 1  | 1  | +1    |
| B   | 2  | 1  | +1    |
| C   | 1  | -1 | -1    |

Nový bod: Q = (2, 0), k = 3

Vzdálenosti:

| Sous. | Třída | Vzdál. |
|:-----:|:-----:|:------:|
|   B   |  +1   |  1.00  |
|   A   |  +1   |  1.41  |
|   C   |  -1   |  2.24  |

Hlasování: (+1, +1, -1) → Výsledek: třída **+1**
