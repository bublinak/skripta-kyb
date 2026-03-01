# Jak funguje perceptron

Perceptron je jednoduchý model umělého neuronu, který se používá pro binární klasifikaci. Jeho úkolem je rozdělit data do dvou tříd, například +1 a -1.

---

## Základní princip

Perceptron dostává několik vstupů x₁, x₂, ..., xₙ. Každý vstup má přiřazenou váhu w₁, w₂, ..., wₙ, která určuje, jak je daný vstup důležitý.

Model spočítá lineární kombinaci vstupů a vah:

z = w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ + b

kde b je bias (konstanta, která posouvá rozhodovací hranici).

---

## Rozhodnutí

Výsledek z se pošle do jednoduché aktivační funkce sign:

y = sign(z)

Pokud je z > 0, perceptron vrátí +1.  
Pokud je z ≤ 0, vrátí -1.

Tak perceptron určí, do které třídy vstup patří.

---

## Učení perceptronu

Perceptron se učí z trénovacích dat. Postupně prochází všechny příklady a upravuje váhy podle toho, jestli klasifikoval správně nebo ne.

1. Pro daný vstup xᵢ spočítá výstup ŷ = sign(w·xᵢ + b).
2. Pokud se spletl (ŷ ≠ yᵢ), upraví váhy podle pravidla:

   w := w + η * yᵢ * xᵢ  
   b := b + η * yᵢ

   kde η je koeficient učení (learning rate).

3. Proces se opakuje, dokud nejsou všechny příklady správně klasifikovány
   nebo dokud se chyba dále nezmenšuje.

---

## Výsledek

Po natrénování perceptron najde takové váhy a bias, které určují rozhodovací hranici:

w₁·x₁ + w₂·x₂ + b = 0

Tato přímka (v 2D) nebo rovina (v nD) rozděluje prostor na dvě oblasti odpovídající dvěma třídám.

---

## Omezení

Perceptron dokáže správně fungovat pouze tehdy, když jsou data lineárně oddělitelná.  
Pokud se třídy překrývají, nebo jsou nelineárně rozloženy (například problém XOR), perceptron správné řešení nenajde.
