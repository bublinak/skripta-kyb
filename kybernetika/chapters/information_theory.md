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

Množství informace vyjadřuje míru neurčitosti, kterou přijetí zprávy odstraní. Množství informace $I$ se tedy rovná entropii $H$. Shannon ukázal, že čím je zpráva méně pravděpodobná (nebo neočekávaná), tím více informace přináší.

$I = H = f(\frac{1}{p})$ 

> Nechť se zpráva $X$ sestává ze dvou nezávislých zpráv $A$ a $B$. Pravděpodobnost zprávy $X$ tvořené dvěma nezávislými jevy je:
> 
> $P(X) = P(A) \cdot P(B)$
>
> Celková informace, kterou získáme ze zprávy X bude:
>
> I(X) = I(A) + I(B)
>
> Dosadíme-li do sebe s respektováním výše uvedených vztahů, dostaneme:
>
> $I(X) = f \left[ \frac{1}{P(A) \cdot P(B)} \right] = f \left[ \frac{1}{P(A)} \right] + f \left[ \frac{1}{P(B)} \right]$
>
> Z teorie funkcí víme, že tato rovnost bude splněna, pokud bude funkce funkcí logaritmickou. Tedy:
>
> $I(X) = \log \left[ \frac{1}{P(A) \cdot P(B)} \right] = \log \left[ \frac{1}{P(A)} \right] + \log \left[ \frac{1}{P(B)} \right]$
>
> Základ logaritmu je libovolný, ovlivňuje pouze výsledné jednotky. Shannon zavedl v definičním vztahu pro informaci logaritmus o základu 2, takže dosazením dostáváme:

$I(X) = H(X) = \log_2 \frac{1}{P(X)} = -\log_2 P(X) \qquad [bit, Sh]$

Jednotkou množství informace je tedy *bit* nebo později *Shannon*. 1 bit je nejměnší množství informace, kterou může zpráva obsahovat. Tuto informacei nese zpráva o jevu, který má dvě možnosti (dva stavy). Modelem tohoto jevu může být hod (férovou) mincí.

> Poznámka:
> Jednotka *bit* je používána v poněkud odlišném významu ve výpočetní technice k označení elementární paměťové kapacity, vyhcázející z odlišení dvou možných stavů logického zařízení při binárním zápisu.

---
>### *Příklad:*
>*Určete entropii náhodného jevu X, kterým je:*
>
>*a) hod mincí (při němž padne některá strana mince)*
>
>*b) hod kostkou (při níž padne jedna ze 6ti čísel kostky)*
>
>*c) tah šestice čísel Sportky (6 čísel z množiny <1, 49> bez opakování)*
>
>### a)
>$P(X) = \frac{1}{2}$
>
>$H(X) = -\log_2 P(X) = -log_2(\frac{1}{2}) = 1 [bit]$
>### b)
>
>$P(X) = \frac{1}{6}$
>
>$H(X) = -\log_2 P(X) = -log_2(\frac{1}{6}) = 2,58 [bit]$
>
>### c)
>
>$P(X) = \frac{1}{13983816} \doteq \frac{1}{14\cdot10^6} $
>
>$H(X) = -\log_2 P(X) = -log_2(\frac{1}{14\cdot10^6}) = 23,74 [bit]$

---

## Entropie Zdroje

Uvažujeme-li diskrétní zdroj zpráv, jehož abeceda je tvořena množinou $S$ prvků $(y_1, y_2, ... , y_s)$, přiřadíme-li každému prvku určitou pravděpodobnost jeho výskytu, dostaneme matici:

$$ \begin{bmatrix} 
   y_1 & y_2 & \dots & y_s \\
   P(y_1) & P(y_2) & \dots & P(y_s) \\
   \end{bmatrix} $$

Tato matice se nazývá **konečné schéma** nebo také **logické spektrum zdroje**.

> Předpokládejme, že zpráva je tvořená posloupností $n$ prvků abecedy zdroje $y$ tak, že obsahuje:
>
> $n_1$ prvků $y_1$, $n_2$ prvků $y_2$, ... , $n_s$ prvků $y_s$.
>
> Množství informace v této zprávě bude podle definice:
>
> $I(Z) = - \log_2 P(Z) = - \sum_{i=1}^s n_i \cdot \log_2P(y_i)$
>
> Protože pro dostatečně dlouhou zprávu $(n \rightarrow \infty)$ je pravděpodobnost výskytu jednotlivých prvků abecedy dána jejich relativní četností $P(y_i) = \frac{n_i}{n}$, bude množství informace ve zprávě
>
> I(Z)=-n \cdot \sum_{i=0}^s P(y_i) \log_2 P(y_i)
>
> Průměrné množství informace připadající na jeden symbol zprávy bude potom:

$\overline{I(Z)} = \frac{I(Z)}{n} = H(Z) = - \sum_{i=0}^{n}{P(y_i) \cdot \log_2 (P(y_i)}$

a nazývá se **entropí zdroje** (entropií na jeden symbol).

> ### Příklad:
> Zdroj informace je charakterizován konečným schematem:
> 
>$$ \begin{bmatrix} 
>   y_1 & y_2 & y_3 & y_4 & y_5 \\
>   0,15 & 0,22 & 0,08 & 0,35 & 0,2 \\
>   \end{bmatrix} $$
>
> Určete:
> 
> a) entropii zdroje
>
> b) množství informace přenášené zprávou: $y = y_5, y_3, y_4, y_4, y_1, y_5, y_2, y_1, y_3, y_3$
>
> **Řešení:**
> bylo při hodině :)
>

## Jazyky a gramatiky

- **přirozené jazyky** - vznikly jako prostředek komunikace mezi lidmi
- **umělé jazyky** - byly vytvořeny pro speciální druhy komunikace a vznikly výslovnou dohodou

Jazyky se vyznačují tím, že existuje:
- množina všech **výrazů** používaných uživatelem - označíme *VYRA*
- množina všech **významů**, které jsou jazykem vyjadřovány - označíme *VYZN*
- funkce zvaná **sémantika** - označíme *SEM*, která každému výrazu $$x \in \textnormal{VYRA} $$ přiřazuje význam. $$\textnormal{SEM}(x) \in \textnormal{VYZN}$$.

Poznámka:
> a) V přirozeném jazyce je sémantika víceznačnou funkcí - jediný výraz může mít více významů - **homonymie**.
> 
> b) U umělých jazyků vyžadujeme vždy **jednoznačnost sémantiky**.
> 
> c) Mohou existovat dva různé výrazy $$x, y \in \textnormal{VYRA}$$, pro které platí: $$\textnormal{SEM}(x) = \textnormal{SEM}(y) \in \textnormal{VYRA}$$. Výrazy $x$ a $y$ mají tedy stejný význam - **synonimie**.
