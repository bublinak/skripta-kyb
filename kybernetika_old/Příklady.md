# Příklady

## Příklad 1:
RC obvod:

<img src=img/VEJWq.png height=150/>
<img src=img/priklad1.drawio.png/>

vstup: $v_{in} = u$ 

výstup: $v_{out} = y$

## Řešení:
Aplikací Ohmova a  Kirchhoffových zákonů:

$i_R = i_C$

$\frac{v_i(t) - v_o(t)}{R} = C \cdot \frac{dv_o(t)}{dt}$

po úpravě dostaneme:

$v_i(t) - v_o(t) = RC \dot{v}_o(t)$

$RC \dot{v}_o(t) + v_o(t)$

Popis systému diferenciální rovnicí:

$\dot{v}_o(t) + \frac{v_o(t)}{RC} = \frac{v_i(t)}{RC} $

Přenos je definován jako:
$F(p) = \frac{Y(p)}{U(p)}$
... řešení lineární diferenciální rovnice ...

$v_o(t) = 1 - e^{-\frac{1}{RC}t}$

Přenos F( 
