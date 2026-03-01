# Perceptron – ruční výpočet a vizualizace kroků

## Zadání

Máme 2D data se dvěma třídami:

| Bod | x₁ | x₂ | Třída y |
|-----|----|----|---------|
| A   | 2  | 1  | +1      |
| B   | 1  | -1 | -1      |

Bod A (2,1) patří do třídy +1  
Bod B (1,-1) patří do třídy -1

Cílem perceptronu je najít přímku, která tyto body oddělí.

---

## Počáteční hodnoty

- Počáteční váhy: w = [0, 0]  
- Bias: b = 0  
- Learning rate: η = 1

Rozhodovací hranice:  
w₁x₁ + w₂x₂ + b = 0

Na začátku:  
0 * x₁ + 0 * x₂ + 0 = 0

---

## Iterace 1

Bod A = (2, 1), y = +1  
Predikce:  
ŷ = sign(w · x + b) = sign(0*2 + 0*1 + 0) = 0  
Chybná klasifikace.

Aktualizace:
w = w + η * y * x = [0,0] + 1 * (+1) * [2,1] = [2,1]  
b = b + η * y = 0 + 1 * (+1) = 1

---

## Stav po 1. kroku

w = [2, 1], b = 1

Rozhodovací přímka:  
2x₁ + 1x₂ + 1 = 0  
x₂ = -2x₁ - 1

---

## Iterace 2

Bod B = (1, -1), y = -1  
Predikce:  
w · x + b = (2)(1) + (1)(-1) + 1 = 2  
ŷ = sign(2) = +1 → Chyba

Aktualizace:
w = w + η * y * x = [2, 1] + 1 * (-1) * [1, -1] = [1, 2]  
b = b + η * y = 1 + (-1) = 0

---

## Stav po 2. kroku

w = [1, 2], b = 0

Rozhodovací přímka:  
x₂ = -½x₁

---

## Iterace 3

Bod A = (2, 1), y = +1  
w · x + b = 1*2 + 2*1 + 0 = 4 → ŷ = +1  
Správně, žádná změna.

Bod B = (1, -1), y = -1  
w · x + b = 1*1 + 2*(-1) + 0 = -1 → ŷ = -1  
Správně, žádná změna.

---

## Výsledek

Po 2 iteracích:  
w = [1, 2], b = 0  
Rozhodovací přímka:  
x₂ = -½x₁

---

## Shrnutí kroků

| Krok | Bod (x₁,x₂) | y  | Predikce | Chyba? | Nové w | b |
|------|-------------|----|----------|--------|--------|---|
| 1    | (2,1)       | +1 | 0        | Ano    | [2,1]  | 1 |
| 2    | (1,-1)      | -1 | +1       | Ano    | [1,2]  | 0 |
| 3    | (2,1)       | +1 | +1       | Ne     | [1,2]  | 0 |
| 4    | (1,-1)      | -1 | -1       | Ne     |
