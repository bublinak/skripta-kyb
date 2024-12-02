# Základy teorie informace

Teorie informace je matematická disciplína, která se zaměřuje na kvantifikaci, přenos a uchování informací. Původně byla vyvinuta pro účely komunikační techniky a zpracování signálů, ale její principy mají uplatnění v mnoha dalších oborech, od biologie po informatiku a statistiku. Obecně se jedná o pojem značně široký a často používaný v celé řadě definic, vymezujících nejen předmět kybernetiky.

Definice pojmu informace je velmi složitá. Obecně se tento pojem užívá často v intuitivně chápaném smyslu a vztahuje se k pojmům zpráva, sdělení, údaj, poznatek, apod. V kybernetice má širší význam a za informaci se zde považují podněty, které člověk přijímá prostřednictvím svých smyslových orgánů ze svého okolí. 

- Kybernetika říká, že informace je jakákoliv zpráva, kterou lze reálně (v přítomnosti) nebo potenciálně (v budoucnu) použít k řízení systému.

### Historie

Základy teorie informace položil v roce 1948 Claude Shannon ve své práci "A Mathematical Theory of Communication." Shannon vytvořil rámec pro měření a analýzu informací pomocí pravděpodobnosti a logaritmických funkcí. Tento přístup umožnil nejen kvantifikovat množství informace ve zprávě, ale i analyzovat efektivitu přenosových systémů.

## Základní pojmy

- **Zpráva** (sdělení): je jakýkoliv údaj nebo sdělení reprezentovaný textem, řečí, obrazem, čísly či jinou formou. Zpráva má jak kvantitativní, tak kvalitativní obsah, přičemž kvantitativní obsah je měřitelný a kvalitativní obsah odráží smysl a hodnotu zprávy.

- **Informace** je obsah zprávy, který přináší určité poznatky nebo odstranění neurčitosti. Shannon definoval informaci jako kvantitativní pojem, kde množství informace závisí na pravděpodobnosti výskytu dané zprávy – čím méně pravděpodobná je zpráva, tím větší informaci přináší.


- **Signál** je fyzikální reprezentace zprávy, například ve formě elektrického proudu, světla nebo zvuku. Při přenosu zprávy mezi vysílačem a příjemcem je signál často vystaven šumu, což může ovlivnit jeho kvalitu a srozumitelnost.

- **Šum** představuje náhodné rušení, které ovlivňuje signál při jeho přenosu. Šum může snížit přesnost nebo spolehlivost přenosu, a proto se teorie informace snaží šum minimalizovat nebo kompenzovat.

Zpráva nabývá svého významu v okamžiku, kdy je sdělena - přenesena od zdroje zprávy k jejímu příjemci. Úkolem teorie informace je zabezpečení účinného přenosu zprávy mezi dvěma systémy - zdrojem zprávy a příjemcem zprávy.

### Sdělovací soustava

Proces přenosu zprávy se typicky skládá z několika komponent:

1. Zdroj zprávy – původce zprávy 

    (například: lidský hlas - *signál: změna akustického tlaku*).

2. Kodér – zařízení, které převede zprávu do formátu vhodného pro přenos 

    (například: mikrofon - *signál: tlak / el. proud*).

3. Přenosový kanál – prostředek, kterým je signál přenášen 
    
    (například: telefonní vedení - *signál: el proud*).

4. Dekodér – zařízení, které rekonstruuje původní zprávu 

    (například: reproduktor - *signál: el. proud / tlak*).

5. Příjemce zprávy – cílový uživatel zprávy 

    ¨(například: lidské ucho - *signál: změna akustického tlaku*).

---

## Množství informace a informační entropie

### Množství informace

Množství informace vyjadřuje míru neurčitosti, kterou přijetí zprávy odstraní. Shannon ukázal, že čím je zpráva méně pravděpodobná (nebo neočekávaná), tím více informace přináší.

### Informační entropie

Informační entropie je míra nejistoty nebo neurčitosti spojené se souborem možných zpráv. Vyjadřuje průměrné množství informace, které lze očekávat od jednoho přenosu zprávy. Entropie se vypočítává podle Shannonova vzorce:

$H = - \sum\limits_{i=0}^{n} p_i \cdot log_2(p_i)$




