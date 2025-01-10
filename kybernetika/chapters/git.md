# GIT

Git je **distribuovaný systém pro správu verzí**, který umožňuje sledovat změny v kódu, spolupracovat na projektech a uchovávat historii změn. Používá se hlavně ve vývoji softwaru, ale může být využit i v jiných oblastech, kde je třeba verzovat soubory.

---

## Hlavní vlastnosti Gitu:
1. **Distribuovaný**:
   - Každý vývojář má kompletní kopii celého projektu včetně historie změn uloženou lokálně.
   - K základním operacím není potřeba připojení k internetu.

2. **Sledování historie změn**:
   - Uchovává záznamy o všech změnách provedených v projektu (co, kdo a kdy změnil).
   - Umožňuje vrátit se k jakémukoliv bodu v historii.

3. **Podpora větví (branches)**:
   - Vytváření větví pro práci na různých funkcích nebo opravách chyb bez ovlivnění hlavní (produkční) verze projektu.
   - Větve lze později sloučit (merge) zpět.

4. **Kolektivní práce**:
   - Více lidí může pracovat na stejném projektu současně.
   - Git řeší konflikty, když dva vývojáři provedou změny na stejných souborech.

5. **Rychlost a efektivita**:
   - Operace, jako je commit (uložení změn) nebo diff (zobrazení rozdílů), probíhají rychle, protože jsou lokální.

---

## Základní pojmy
- **Repository (repozitář)**:
  - Místo, kde je uložen projekt a jeho historie změn.
  - Repozitář může být lokální (na vašem počítači) nebo vzdálený (např. na GitHubu).

- **Commit**:
  - Záznam změn, který uchovává konkrétní stav projektu.

- **Branch (větev)**:
  - Paralelní linie vývoje. Nejčastější větev je `main` (dříve `master`).

- **Merge**:
  - Sloučení dvou větví dohromady.

- **Pull a Push**:
  - **Pull**: Stažení změn z vzdáleného repozitáře.
  - **Push**: Odeslání lokálních změn do vzdáleného repozitáře.

- **Clone**:
  - Zkopírování celého repozitáře na váš počítač.

---

## Typické využití
1. **Jednoduchý projekt**:
   - Sledování změn, ukládání historie a možnost návratu zpět k předchozím verzím.

2. **Týmová spolupráce**:
   - Rozdělení práce mezi různé vývojáře.
   - Organizovaná struktura projektu.

3. **Open Source**:
   - Git je široce využíván v komunitě open source, zejména na platformách jako GitHub, GitLab nebo Bitbucket.

---


## Základní příkazy v OS (windows)
- `<disk>:` - změní aktuální disk na požadovaný. Příkald: `C:` nebo `H:`.
- `cd <nazev adresare>` - změní aktuální adresář. Akceptuje realtivní nebo absolutní cestu. Symbol `..` označuje nadřazený adresář Příkald: `h:> cd kybernetika`, `h:\kybernetika> cd ..`.
- `mkdir <nazev adresare>` - vytvoří nový adresář.
- `dir`, `ls`, `ls -Force` - vypíše aktuální adresář.

## Základní příkazy GIT
- `git clone <url>` - naklonuje vzdálený repozitář. _Url repozitáře končí .git._
- `git add` - přidá soubor na seznam souborů připravených ke `commit`. Příklad: `git add soubor.txt`, `git add .` - znak `.` je symbol pro celý aktuální adresář.
- `git commit -m "commit message"` - Zapíše změnu do repozitáře, vytvoří nový `commit`.  
- `git push` - Synchronizuje vzdálený repozitář s lokálním. Směrem z lokálního do vzdáleného.
- `git pull` - Synchronizuje lokální repozitář se vzdáleným. Směrem ze vzdáleného do lokálního.
- `git fetch` - Aktulaizuje informace o vzdáleném repozitáři.
- `git log` - Vypíše seznam commitů. 
   - `git log --oneline` - Vypíše zkrácený seznam commitů.
   - `git log --graph --oneline --all` - Vypíše zkrácený seznam commitů s grafem větvení.
- `git checkout <commit-hash>` - Nastaví pohled repozitáře na zvolený commit nebo branch
- `git swith -` - Vrátí pohled na poslední pozici repozitáře (Na aktuální HEAD)
- `git reset` - Nastavá HEAD repozitáře
   - `git reset --soft <commit-hash>` - Nastaví HEAD repozitáře na zvolený commit.
   - `git reset --hard <commit-hash>` - Nastaví HEAD repozitáře na zvolený commit a odstraní následující commity.

## Github nastavení repozitáře na SPŠE

1. vytvořit repo na githubu
2. naklonovat repo na disk `H:/<cesta>`
3. odstranění "dubious ownership"
   ``` git config --global --add safe.directory '%(prefix)///SEPTIM/U/<username>/<cesta k repozitari>' ```
4. vytvoření "personal access token
   ``` profile > settings > Developer settings > Personal access tokens > Token (classic)```
   zkopírovat token !
5. nastavit origin pomocí tokenu   
  ``` git remote set-url origin https://<TOKEN>@github.com/<username>/<repository.git> ```
