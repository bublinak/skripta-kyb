# Nutné základy elektrotechniky
## Literatura
- [NEČÁSEK, Sláva: Radiotechnika do kapsy](https://docplayer.cz/8018397-Radiotechnika-do-kapsy.html), SNTL 1981 (II. červené vydání)
> Odkaz vede na 1. vydání, druhé není zdarma dostupné
- [MALÝ, Martin: Hradla, volty, jednočipy](https://knihy.nic.cz/files/edice/hradla_volty_jednocipy.pdf), edice CZ.NIC 2017
- [Názorná elektrotechnika - YouTube](https://www.youtube.com/@nazornaelektrotechnika9527)
## Obsah
1. Ohmův zákon
2. Sériové/paralelní řazení součástek
3. Kirchhoffovy zákony
---

--- 

# Technická praxe

Umět teorii je jedna věc, ale zážitek z praxe má své kouzlo. 

1. Nutné základy
2. Pasivní součástky
3. Polovodiče a dokumentace
4. Základy HW designu, CAD software




## Ohmův zákon
Ohmův zákon je základní princip v elektrotechnice, který popisuje vztah mezi napětím (V), proudem (I) a odporem (R) v elektrickém obvodu. Ohmův zákon (ve stejnosměrném napětí) lze vyjádřit následujícím vztahem:
$U=I*R$, kde:
![Úbytek na odporu](img/ubytek_na_soucastce.png)
U je napětí na svorkách měřené v voltech (V),
I je proud obvodem měřený v ampérech (A),
R je odpor obvodu/součástky měřený v ohmech (Ω).

Podle tohoto zákona, pokud se napětí ve vodiči zvýší, tak se zvýší i proud, pokud je odpor konstantní. Obdobně, pokud se odpor zvýší při konstantním napětí, proud se sníží. 

Druhá část tohoto zákona popisuje závislost výkonu spotřebovaného zařízením.

![Ohmův zákon](img/ohmuv_zakon.png)

### Rezistory
Rezistor je pasivní elektrotechnická součástka, která se v elektrickém obvodu projevuje (ideálně) jedinou vlastností – elektrickým odporem (jednotka Ohm, značka Ω). Dělí na pevné a proměnné. Pevné rezistory mají pevně danou hodnotu odporu, která se mírně mění pouze v závislosti na teplotě a životnosti rezistoru.

U proměnných rezistorů můžeme měnit jeho fyzikální veličinu (odpor) v určitém rozsahu. Ty se používají k plynulému upravení činnosti dalších částí obvodu – potenciometr nebo odporový trimr (např. nastavení hlasitosti, stmívání svítidel, nastavení teploty apod.), nebo jako senzory teploty (termistor), napětí (varistor), světla (fotorezistor), ...

Pokud chceme předřadným rezistorem regulovat např. jas světla, je třeba počítat s jeho aktuálním příkonem a příkonem zapojení - proud světlem je v sériovém zapojení společný  pro obě komponenty a v závislosti na velikosti odporu rezistoru způsobí požadovaný úbytek napětí.

Rezistory jsou prakticky nejpoužívanějšími elektronickými součástkami. Jedná se o pasivní součástky, u kterých se projevuje v elektrickém obvodu vlastnost - elektrický odpor R (Ω). Rezistory nejčastěji používáme pro snížení velikosti elektrického proudu nebo získání určitého úbytku napětí.

![Značení odporů](https://cz.mouser.com/images/technical-resources/resistor-color-code--chart.jpg)

U rezistorů se v nevhodných podmínkách (vůči jejich konstrukci) - např.: použití výkonového rezistoru pro vysokofrekvenční aplikace, kde může docházet k parazitní indukčnosti.

Hodnoty běžně dostupných rezistorů spadají většinou do řady E24.

Další informace: [Rezistory - Wikipedie](https://cs.wikipedia.org/wiki/Rezistor).

## Sériové/Paralelní zapojení a Kirchhoffovy zákony
V případě, že zapojujeme mezi napájecí svorky dvě a více komponent, máme možnost zapojení těchto komponent
1. za sebe (do [série](https://cs.wikipedia.org/wiki/S%C3%A9riov%C3%A9_zapojen%C3%AD))
2. vedle sebe ([paralelně](https://cs.wikipedia.org/wiki/Paraleln%C3%AD_zapojen%C3%AD))
