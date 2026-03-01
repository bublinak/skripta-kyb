# K-means (metoda k-průměrů)

## Co je K-means
K-means je **neučící se (neřízená)** metoda strojového učení používaná pro **shlukování dat (clustering)**.  
Jejím cílem je **rozdělit data do K skupin (shluků)** tak, aby si body ve stejném shluku byly co nejpodobnější a body v různých shlucích co nejvíce odlišné.

---

## Hlavní myšlenka
K-means hledá **středy (centroidy)** K shluků a přiřazuje každý bod k nejbližšímu středu.  
Poté středy přepočítá jako průměry všech bodů, které do daného shluku patří.  
Proces se opakuje, dokud se středy „neustálí“.

---

## Postup algoritmu

| Krok | Popis                                                                 |
|------|------------------------------------------------------------------------|
| 1    | Zvol počet shluků **K**.                                               |
| 2    | Náhodně inicializuj **K počátečních středů (centroidů)**.              |
| 3    | Každý bod přiřaď ke **nejbližšímu středu** (např. podle Eukleidovské vzdálenosti). |
| 4    | **Přepočítej středy** jako průměr všech bodů, které do shluku patří.   |
| 5    | Opakuj kroky 3–4, dokud se středy nezmění nebo se změny stanou malé.   |

---

## Matematicky (zjednodušeně)

Hledáme rozdělení dat \( X = \{x_1, x_2, ..., x_n\} \) do K shluků \( C_1, ..., C_K \), které minimalizuje tzv. **chybu (SSE – Sum of Squared Errors):**

\[
J = \sum_{k=1}^{K} \sum_{x_i \in C_k} ||x_i - \mu_k||^2
\]

kde:
- \( \mu_k \) je centroid (střed) shluku \( C_k \),
- \( ||x_i - \mu_k|| \) je vzdálenost bodu od středu shluku.

---

## Intuice
- Každý shluk má svůj **střed (centroid)**.
- Body se **přiřazují** ke středu, který je nejblíže.
- Poté se středy **posunou** do nových pozic – do průměru svých bodů.
- Tento proces se **opakuje**, dokud se středy ustálí.

---

## Vlastnosti
- Algoritmus **vždy konverguje**, i když může uvíznout v **lokálním minimu**.
- Pořadí inicializace může ovlivnit výsledky – často se používá **K-means++** pro lepší výběr počátečních středů.

---

## Výhody
- Jednoduchý a rychlý.
- Dobře škáluje na velké množství dat.
- Snadno interpretovatelný výsledek (centroidy).

---

## Nevýhody
- Musí se **předem zvolit K** (počet shluků).
- Citlivý na **počáteční pozici centroidů**.
- Funguje dobře pouze pro **sférické (kulovité) shluky**.
- Špatně pracuje s odlehlými body (outliery).

---

## Shrnutí
K-means je jednoduchý, ale účinný algoritmus pro **rozdělení dat na K shluků** na základě jejich podobnosti.  
Pracuje iterativně – střídavě **přiřazuje body ke středům** a **přepočítává středy**, dokud nedojde ke stabilizaci.
