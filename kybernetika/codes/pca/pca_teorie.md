# PCA – Analýza hlavních komponent (Principal Component Analysis)

## Co je PCA
PCA je **statistická metoda** používaná pro **snížení rozměrnosti dat**.  
Jejím cílem je převést původní data do nového souřadného systému tak, aby:

- co nejvíce zachovala **variabilitu dat (informaci)**,  
- a zároveň používala **co nejméně dimenzí**.

---

## Intuice
PCA hledá **nové osy (hlavní komponenty)**, které:

1. jsou **kolmé (nezávislé)**,  
2. zachycují **maximální rozptyl** dat.

Tím umožňuje:
- zjednodušit data,
- odstranit šum,
- a zlepšit vizualizaci i výkon následných algoritmů (např. klasifikátorů).

---

## Kdy použít PCA
- Máš **hodně vstupních znaků (features)**.
- Některé jsou **silně korelované**.
- Chceš **zredukovat rozměr** dat bez ztráty většiny informace.

---

## Hlavní myšlenka
Místo původních os (x₁, x₂, …, xₙ) se najdou **nové osy (PC₁, PC₂, …)**, které:

- směřují tam, kde mají data největší rozptyl,  
- postupně zachycují co nejvíce informace.

První osa (PC₁) vysvětluje největší část rozptylu, druhá menší atd.

---

## Postup algoritmu

| Krok | Popis |
|------|--------|
| 1 | **Normalizuj data** – odečti průměr každého sloupce (centrace). |
| 2 | **Spočítej kovarianční matici** dat. |
| 3 | **Najdi vlastní čísla a vlastní vektory** kovarianční matice. |
| 4 | **Seřaď vlastní vektory** podle velikosti vlastních čísel (rozptyl). |
| 5 | **Vyber prvních k komponent** – ty zachytí největší část variability. |
| 6 | **Projektuj data** na tyto komponenty → získáš data v menší dimenzi. |

---

## Matematicky (zjednodušeně)

Máme matici dat \( X \in \mathbb{R}^{n \times d} \):

1. Centrovaná data:  
   \( X' = X - \bar{X} \)

2. Kovarianční matice:  
   \( C = \frac{1}{n-1} (X')^T X' \)

3. Vlastní čísla λ a vlastní vektory v:
   \[
   C v = \lambda v
   \]

4. Seřadíme vektory podle λ (od největšího).

5. Projekce na k komponent:
   \[
   Z = X' W_k
   \]
   kde \( W_k \) obsahuje první k vlastních vektorů.

---

## Vizuální intuice
Představ si body rozložené podél šikmé přímky v rovině.  
PCA najde **směr této přímky** (největší rozptyl) a **projekcí bodů** na ni vytvoří 1D reprezentaci.

---

## Výhody
- Zjednodušuje data (menší počet dimenzí).  
- Odstraňuje šum a korelované znaky.  
- Zrychluje učení modelů.  
- Umožňuje vizualizovat i vysokodimenzionální data (např. v 2D).

---

## Nevýhody
- **Ztrácí interpretaci** – nové osy jsou lineární kombinace původních znaků.  
- Funguje pouze na **lineární** závislosti.  
- **Citlivá na měřítko** – je nutná standardizace.

---

## Shrnutí

| Vlastnost | Popis |
|------------|--------|
| Typ | Neřízená metoda (unsupervised) |
| Účel | Snížení rozměrnosti |
| Hlavní princip | Najde směry s největším rozptylem |
| Matematika | Vlastní vektory kovarianční matice |
| Výsledek | Data v novém souřadném systému s menším počtem dimenzí |
