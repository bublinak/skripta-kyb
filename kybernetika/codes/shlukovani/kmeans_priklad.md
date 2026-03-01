# K-means – ruční příklad (inicializace z bodů A a B)

## Zadání
Máme 8 bodů v rovině.  
Chceme je rozdělit do **K = 2 shluků** metodou K-means.

| Bod | x₁ | x₂ |
|-----|----|----|
| A   | 1.0 | 1.0 |
| B   | 1.5 | 2.0 |
| C   | 2.0 | 1.3 |
| D   | 2.5 | 2.7 |
| E   | 5.0 | 4.0 |
| F   | 6.0 | 5.0 |
| G   | 5.5 | 3.5 |
| H   | 7.0 | 5.0 |

---

## Krok 1 – Inicializace středů
Zvolíme počáteční středy **přímo z dat**:

- μ₁⁽⁰⁾ = **A** = (1.0, 1.0)  
- μ₂⁽⁰⁾ = **B** = (1.5, 2.0)

> Pozn.: Oba počáteční středy leží v levém shluku → první iterace rozdělí levé body mezi dva centroidy a **všechny pravé body** připadne jednomu z nich.

---

## Krok 2 – Přiřazení k μ⁽⁰⁾ a přepočet μ⁽¹⁾

### Přiřazení k (μ₁⁽⁰⁾, μ₂⁽⁰⁾)
| Bod | d k μ₁⁽⁰⁾=(1,1) | d k μ₂⁽⁰⁾=(1.5,2) | Nejbližší |
|-----|------------------|-------------------|-----------|
| A   | 0.00 | 1.12 | μ₁ |
| B   | 1.12 | 0.00 | μ₂ |
| C   | 1.31 | 0.86 | μ₂ |
| D   | 2.13 | 1.12 | μ₂ |
| E   | 5.00 | 4.03 | μ₂ |
| F   | 5.66 | 5.32 | μ₂ |
| G   | 4.72 | 4.03 | μ₂ |
| H   | 6.73 | 6.02 | μ₂ |

→ Shluky po 1. přiřazení:
- **C₁** = {A}  
- **C₂** = {B, C, D, E, F, G, H}

### Přepočet centroidů
- μ₁⁽¹⁾ = průměr(C₁) = (1.00, 1.00)  
- μ₂⁽¹⁾ = průměr(C₂) = \(\big(\frac{1.5+2+2.5+5+6+5.5+7}{7}, \frac{2+1.3+2.7+4+5+3.5+5}{7}\big)\) = **(4.2143, 3.3571)**

---

## Krok 3 – Přiřazení k μ⁽¹⁾ a přepočet μ⁽²⁾

### Přiřazení k (μ₁⁽¹⁾, μ₂⁽¹⁾)
| Bod | d k μ₁⁽¹⁾=(1,1) | d k μ₂⁽¹⁾≈(4.214,3.357) | Nejbližší |
|-----|------------------|-------------------------|-----------|
| A   | 0.00 | 4.00+ | μ₁ |
| B   | 1.12 | 3.26 | μ₁ |
| C   | 1.31 | 2.74 | μ₁ |
| D   | 2.13 | 2.42 | μ₂ |
| E   | 4.24 | 0.89 | μ₂ |
| F   | 5.66 | 2.18 | μ₂ |
| G   | 4.72 | 1.42 | μ₂ |
| H   | 6.73 | 3.41 | μ₂ |

→ Shluky:
- **C₁** = {A, B, C}  
- **C₂** = {D, E, F, G, H}

### Přepočet centroidů
- μ₁⁽²⁾ = průměr(A,B,C) = \(\big(\frac{1+1.5+2}{3}, \frac{1+2+1.3}{3}\big)\) = **(1.50, 1.4333)**
- μ₂⁽²⁾ = průměr(D,E,F,G,H) = \(\big(\frac{2.5+5+6+5.5+7}{5}, \frac{2.7+4+5+3.5+5}{5}\big)\) = **(5.20, 4.04)**

---

## Krok 4 – Přiřazení k μ⁽²⁾ a přepočet μ⁽³⁾

### Přiřazení k (μ₁⁽²⁾, μ₂⁽²⁾)
| Bod | d k μ₁⁽²⁾≈(1.50,1.433) | d k μ₂⁽²⁾≈(5.20,4.04) | Nejbližší |
|-----|-------------------------|------------------------|-----------|
| A   | 0.57 | 4.78 | μ₁ |
| B   | 0.57 | 3.76 | μ₁ |
| C   | 0.53 | 3.29 | μ₁ |
| D   | 1.01 | 2.08 | μ₂ |
| E   | 3.91 | 0.89 | μ₂ |
| F   | 5.31 | 1.35 | μ₂ |
| G   | 4.42 | 0.87 | μ₂ |
| H   | 6.45 | 1.97 | μ₂ |

→ Shluky:
- **C₁** = {A, B, C, D}  
- **C₂** = {E, F, G, H}

### Přepočet centroidů
- μ₁⁽³⁾ = průměr(A,B,C,D) = **(1.75, 1.75)**
- μ₂⁽³⁾ = průměr(E,F,G,H) = **(5.875, 4.375)**

---

## Krok 5 – Kontrola konvergence
Přiřazení bodů k (μ₁⁽³⁾, μ₂⁽³⁾) už **zůstává stejné** jako v předchozím kroku ⇒ **konvergence po 3 iteracích** (počítáno od inicializace).

---

## Výsledek

| Shluk | Body           | Střed (μₖ)        |
|-------|----------------|-------------------|
| 1     | A, B, C, D     | (1.75, 1.75)      |
| 2     | E, F, G, H     | (5.875, 4.375)    |

**Poznámky:**
- Start se dvěma centroidy v **levém** shluku vedl k tomu, že **μ₂** si v prvním kroku „natáhl“ **všechny pravé body** a posunul se velkým skokem doprava.  
- Následující 2 iterace už jen **doladily** hranici mezi shluky.
