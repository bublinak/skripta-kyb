# Základní pojmy a principy teorie informace

Jedním ze stěžejních pojmů kybernetiky je informace. Lze vykládat velice široce, obecně je vztahována k pojmům, jako jsou zpráva, sdělení, údaj, opznatek, apod.

Z pohledu kybernetiky je informace jakákoliv zpráva, kterou lze reálně (nyní) nebo potenciálně (v budoucnu) použít k řízení systému.

Zákonitostmi vzniku, přenosu a zpracování zpráv se zabývá vědní disciplína nazvaná Teorie informace. Její základy formuloval v roce 1948 Claude E. Shannon. Nezávisle se podbnými problémi zabýval N. Wiener.

## Základní pojmy
- **Zpráva:** (sdělení) je libovolný údaj reprezentovaný ve formě textu, řeči, posloupnosti čísel, obrazu, zvuku, apod. Zpráva je materiální nositel informace a má kvalitativní i kvantitativní obsah.
- **Informace:** kvantitativní obsah zprávy. Informace je abstraktní pojem nehmotné podstaty.
- **Signál:** fyzikální realizace zprávy ve formě nějaké fyzikální veličiny - elektrický proud, světlo, zvuk, apod.
- **Zpráva:** nabývá svého významu v okamžiku, kdy je sdělena. Přenesena od zdroje zprávy k jejímu příjemci. Úkolem teorie informace je zabezpečení účinného přenosu zprávy mezi dvěma systémy - zdrojem zprávy a příjemcem zprávy.
- **Šum:** je jakákoliv (náhodné) rušení působící na sinál během jeho přenosu sdělovací soustavou.

  TODO: obrázek: Sdělovací soustava

## Množství informace a entropie
Princip stanovení množství informcae ve zprávě se zakládá na tom, jak velká neurčitost nějakého jevu se odstraňuje.
Poznamenejme, že z hlediska příjemce představuje generování zprávy náhodný proces. Příjemce musí předem znát, jaké zprávy mohou být zdrojem produkovány , neví však která z možných zpráv bude zdrojem vysílána
- **Množství informace:** je dána množstvím neurčitosti, kterou příjemce o daném jevu měl před přijetím zprávya která se přijetím zprávy odstranila.

> Množství informace $I(X)$ obsažené ve zprávě $X$ je rovno míře neurčitosti zprávy - entropii $H(X)$, která se přijetím zprávy odstraní. Je tedy nepřímo úměrná pravděpodobnosti $P(x)$ výskytu daného jevu obsaženého ve zprávě.
  
$I(X) = H(X) = f\[\frac{1}{P(X)}\]$  

*(odvození, kdo chce - viz. skripta Kyberntika, F. Tůma)*

> Základ logaritmu je libovolný a ovlivňuje pouze jednotky, ve kterých je informace vyjadřována. Shannon zavedl v definičním vztahu pro informaci logaritmus o základu 2.

$I(X) = H(X) = log_2 \frac{1}{P(X)} = -log_2P(X)$


