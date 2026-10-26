---
title: XEI.ItemGenerator – Manuale d'uso
description: Come configurare basi, valori e varianti e generare gli articoli con XEI.ItemGenerator.
lang: it
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Manuale d'uso

Installazione, licenza, menu e autorizzazioni sono nel
[manuale di installazione](installazione.md).

## 1. Cosa fa l'add-on

XEI.ItemGenerator crea in anagrafica articoli i cui codici si **compongono** scegliendo, livello per
livello, dei valori: tipo di prodotto, misura, materiale... Si definisce una volta l'albero delle
scelte; poi, invece di inventare codici e descrizioni a mano, li si compone in una finestra:
l'add-on calcola codice, descrizione, prezzo, peso, misure, gruppo, proprietà e distinta base e
crea gli articoli copiando un articolo modello.

- **Codici coerenti**: il codice è "parlante" (es. `PE090` = pensile da 90) più un progressivo che
  distingue le varianti (colore, maniglia...).
- **Niente doppioni**: la stessa composizione genera sempre lo stesso articolo; se esiste già,
  l'add-on lo trova.
- **Tanti articoli in un colpo**: più misure e più opzioni danno tutte le combinazioni.
- **Articoli completi**: descrizioni (anche in lingua straniera), dati di anagrafica, prezzo di
  listino e distinta base vengono dalla configurazione.
- **Dal documento**: in offerte e ordini cliente si configura l'articolo della riga senza uscire
  dal documento.

### In evidenza

- Generazione in una finestra ridimensionabile sopra SAP: albero dei codici e albero delle varianti
  con spunte (anche su rami diversi), ricerca, elenco degli articoli con stato, prezzo ed esito; SAP
  resta utilizzabile. Aspetto del client SAP, messaggi nello stesso stile, testi modificabili con il
  tasto destro.
- Prezzo, peso, misure, gruppi, proprietà, nome straniero e distinta base composti da valori e
  opzioni.
- Formula della descrizione con codici, opzioni e parti facoltative.
- Configura articolo da offerte e ordini cliente; genera articoli simili da un articolo generato.
- Verifica della configurazione con apertura dell'anagrafica da correggere; import/export con
  Excel; duplicazione.
- Autorizzazioni SAP per funzione; testi in cinque lingue.

## 2. Concetti: basi, valori, varianti e strutture

Il codice di un articolo è composto da **neutro** + **suffisso**:

- il **neutro** è la parte parlante: la concatenazione dei codici dei **valori** scelti livello per
  livello. Ogni livello è una **base** (es. *Tipo mobile*, *Larghezza*) con una lunghezza fissa e i
  suoi valori; ogni valore porta al **sotto livello** successivo o è l'ultimo;
- il **suffisso** è un progressivo di N cifre (configurazione) che distingue gli articoli con lo
  stesso neutro e **varianti** diverse; con 0 cifre il codice è il neutro;
- una **variante** (es. *Colore*) ha delle **opzioni** (es. bianco, rovere). Le varianti da chiedere
  per un valore sono raccolte in una **struttura varianti** collegata al valore.

In tutto il manuale si usa questo esempio, contenuto nel file
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx), da importare con
*Importa / esporta Excel*:

```
Tipo mobile cucina (CU, 2 caratteri)          struttura CUSC: Colore
├── BA Mobile base     → Larghezza
└── PE Mobile pensile  → Larghezza
Larghezza (CL, 3 caratteri)                   struttura CUSM: Colore anta + Maniglia, eredita varianti
├── 060 Larghezza 60 cm
└── 090 Larghezza 90 cm
Colore (CUCOL)     BI Bianco · RO Rovere
Maniglia (CUMAN)   AL Maniglia alluminio · NE Maniglia nera
```

Il pensile da 90 con maniglia in alluminio ha neutro `PE090`; generando insieme bianco e rovere, con
un suffisso di 3 cifre, il bianco (BI viene prima di RO) diventa `PE090001` e il rovere `PE090002`.

La **composizione** (valori di ogni livello + opzioni scelte) identifica l'articolo: generando di
nuovo la stessa composizione l'add-on trova l'articolo esistente invece di crearne un altro.

## 3. Configurazione

![Configurazione](../../_img/itemgenerator/02_configurazione.png)

*La finestra di configurazione.*

| Opzione | Effetto | Predefinito |
|---|---|---|
| Cifre suffisso | progressivo dopo il neutro (0-10); 0 = codice uguale al neutro (un solo articolo per neutro) | 0 |
| Formula descrizione | come si compone la descrizione (capitolo 8); vuota = descrizioni dei livelli in ordine | vuota |
| Descrizioni in maiuscolo | descrizione, descrizione estesa e nome straniero in maiuscolo | No |
| Listino del prezzo | listino in cui scrivere il prezzo dell'articolo (somma dei prezzi di valori e opzioni), nella valuta locale | nessuno |
| Unità di lunghezza | unità delle misure (lunghezza, larghezza, altezza) di valori e articoli; vuota = misure non riportate | nessuna |
| Unità di peso | unità del peso di valori e opzioni; vuota = peso non riportato | nessuna |
| Distinta base | tipo di distinta creata con i componenti: Nessuna, Produzione, Vendita, Assemblaggio, Modello | Produzione |
| Menu dopo creazione | menu da lanciare per ogni articolo creato (integrazione con altri add-on, capitolo 14) | vuoto |
| Miniatura | immagine dell'articolo nella testata dell'anagrafica articoli (capitolo 14) | No |
| Aggiungi all'elenco svuota prima l'elenco | nella generazione *Aggiungi all'elenco* sostituisce l'elenco con l'ultima selezione; senza l'opzione gli articoli si accumulano e si tolgono con *Svuota elenco* (capitolo 9) | Sì |
| Tema finestre | colori delle finestre dell'add-on (la generazione), come i due temi del client SAP: **SAP SQL** (intestazione scura, pulsanti oro) o **SAP HANA** (intestazione blu, pulsanti azzurri). Vale per tutti gli add-on XEI della società; le finestre aperte cambiano subito | secondo il database |

Le opzioni valgono per tutta la società; se la generazione è già aperta le usa alla riapertura.

## 4. Varianti e strutture varianti

### Definizione varianti e opzioni

Una variante ha un codice, una descrizione e le sue **opzioni** (cartella *Opzioni*). In testata,
come nelle basi, si possono indicare una **tabella utente** e un **campo utente articolo**: alla
creazione dell'articolo l'opzione scelta viene aggiunta alla tabella (se non c'è) e il suo codice
scritto nel campo utente dell'articolo (capitolo 6).

![Variante Colore con le opzioni](../../_img/itemgenerator/03_varianti.png)

*La variante Colore con le opzioni.*

| Colonna | Uso |
|---|---|
| Opzione, Descrizione | codice e descrizione dell'opzione; la descrizione è il testo dell'opzione nella descrizione dell'articolo |
| Desc. straniera | testo dell'opzione nel nome straniero (vuoto = quello italiano) |
| Alias | testo libero |
| Prezzo | contributo al prezzo dell'articolo |
| Peso | contributo al peso dell'articolo |
| Proprietà | proprietà articolo da attivare: numeri da 1 a 64 separati da virgola (es. `2, 12`) |
| Attivo | le opzioni disattivate non compaiono nella generazione |

Nella cartella *Componenti* si indicano i componenti della distinta portati dalle opzioni
(capitolo 7).

![Componenti delle opzioni](../../_img/itemgenerator/04_varianti_componenti.png)

*Componenti delle opzioni della maniglia: due maniglie dal magazzino 01.*

### Strutture varianti

Una struttura raccoglie le varianti da chiedere per un valore di base, con la **posizione** (ordine
nella generazione; tutte diverse) e la **posizione descrizione** (ordine dell'opzione scelta in coda
alla descrizione; 0 = non va in coda). La descrizione della riga, se indicata, sostituisce quella
della variante (es. "Colore anta").

![Struttura varianti](../../_img/itemgenerator/05_strutture.png)

*La struttura CUSM: colore dell'anta e maniglia.*

Non si elimina una variante usata da una struttura, né una struttura usata da una base.

## 5. Basi e valori

Testata della base: codice, descrizione, **lunghezza dei codici** (tutti i valori sono lunghi
così), classificazione, tabella utente e campo utente articolo. Nella cartella *Valori* c'è una riga
per valore:

![Base con i valori](../../_img/itemgenerator/06_basi_valori.png)

*La base CU con i valori: descrizioni, sotto livello, struttura varianti.*

![Colonne dei valori](../../_img/itemgenerator/06b_basi_valori.png)

*Le colonne successive: dati per l'articolo (gruppo, proprietà, prezzo, misure, peso).*

Le colonne sono molte: **massimizzando la finestra** la tabella si allarga e si vedono tutte.

| Colonna | Uso |
|---|---|
| Codice, Descrizione | codice del valore (lungo esattamente quanto indicato nella base) e descrizione |
| Desc. articolo | testo del valore nella descrizione dell'articolo |
| Desc. straniera | testo del valore nel nome straniero dell'articolo (vuoto = quello italiano) |
| Sotto livello | base del livello successivo (lista di scelta; la freccia apre la base); vuoto = ultimo livello |
| Struttura varianti | varianti da chiedere per il valore (la freccia apre la struttura) |
| Eredita varianti | le varianti già presenti in un livello precedente partono con le opzioni scelte lassù, **proposte**: si possono cambiare sul valore (tasto destro nella generazione per tornare a quelle proposte). Finché seguono la proposta, l'opzione conta una volta sola |
| Forza ereditarietà | con Eredita varianti: vale la scelta del livello precedente e sul valore non si cambia (la variante non compare sul suo livello) |
| Attivo | i valori disattivati non compaiono nella generazione |
| UM magazzino / acquisti / vendite | unità di misura testuali dell'articolo |
| Gruppo articoli, Gruppo UM | gruppo articoli e gruppo unità di misura dell'articolo |
| Proprietà | proprietà articolo da attivare (1-64) |
| Prezzo, Peso | contributi a prezzo e peso dell'articolo |
| Lunghezza, Larghezza, Altezza | misure dell'articolo |

Come si usano questi dati per l'articolo è spiegato nel capitolo 6. Nella cartella *Componenti* si
indicano i componenti della distinta portati dai valori:

![Componenti dei valori](../../_img/itemgenerator/07_basi_componenti.png)

*Il pensile porta due staffe.*

- **Tabella utente** (una tabella utente senza oggetto, per esempio una tabella dei colori): alla
  creazione dell'articolo il valore scelto vi viene aggiunto (codice e descrizione), se non c'è.
- **Campo utente articolo** (per esempio un campo *Colore* dell'anagrafica articoli): alla creazione
  vi viene scritto il codice del valore scelto.
- Le basi di **primo livello** sono quelle che non sono sotto livello di nessun valore.

Al salvataggio l'add-on controlla lunghezze, codici ripetuti, sotto livello diverso dalla base
stessa, proprietà e componenti; il motivo di un errore compare nella barra di stato e il salvataggio
non parte. Non si elimina una base usata da articoli generati o sotto livello di un'altra base.

> **Duplica** (in basi, varianti e strutture): con un record aperto prepara un record nuovo con gli
> stessi dati e tutte le righe; si scrive il codice nuovo e si preme *Aggiungi*. Utile per basi
> simili (es. un'altra gamma di misure).

## 6. Dati dell'articolo creato

Ogni dato dell'articolo viene dai valori della composizione e dalle opzioni scelte, con due regole:

- **vale l'ultimo livello che lo indica**: un livello successivo ridefinisce i livelli precedenti; un
  dato vuoto o zero non cancella quello di un livello precedente;
- **si somma**: tutti i valori e le opzioni scelte contribuiscono. Un'opzione ereditata conta una
  volta sola, sul livello in cui è stata scelta, finché il livello che la eredita la segue; una
  scelta propria su quel livello conta anche lì (anche se è la stessa opzione).

| Dato dell'articolo | Da | Regola |
|---|---|---|
| Codice | codici dei valori | neutro + suffisso (max 50 caratteri) |
| Descrizione, descrizione estesa | desc. articolo dei valori, descrizioni delle opzioni | formula (capitolo 8); la descrizione è troncata a 200 caratteri, quella estesa è intera nel campo *Descrizione estesa* |
| Nome straniero | desc. straniera di valori e opzioni | stessa formula; vuoto se nessuno ha la desc. straniera |
| Note | composizione | albero con i valori e le opzioni scelte |
| Gruppo articoli | valori | ultimo livello; nessuno = quello del modello |
| Gruppo UM | valori | ultimo livello; con un gruppo le UM testuali non si usano |
| UM magazzino / acquisti / vendite | valori | ultimo livello, ognuna per conto suo |
| Proprietà | valori e opzioni | si sommano: si attivano tutte |
| Lunghezza, larghezza, altezza | valori | ultimo livello, ognuna per conto suo; in acquisto e vendita |
| Peso | valori e opzioni | si somma; in acquisto e vendita |
| Prezzo | prezzo di valori e opzioni | si somma; nel listino della configurazione |
| Distinta base | componenti di valori e opzioni | si sommano (capitolo 7) |

Esempio: pensile da 90 in rovere con maniglia in alluminio (il colore è scelto al livello 1 ed
ereditato dal 090).

| Livello | Scelta | Prezzo | Peso | Misure | Gruppo | Proprietà |
|---|---|---|---|---|---|---|
| 1 Tipo | PE Pensile | 100 | 10 | larghezza 350, altezza 720 | 101 | 1, 3 |
| 1 Colore | RO Rovere | 30 | 1,5 | | | 2 |
| 2 Larghezza | 090 L90 | 40 | 3 | lunghezza 900 | | 5 |
| 2 Maniglia | AL Alluminio | 5 | 0,2 | | | |
| **Articolo PE090002** | | **175** | **14,7** | **900 × 350 × 720** | **101** | **1, 2, 3, 5** |

Tutto il resto (conti, dati di pianificazione, fornitore, magazzini...) viene dall'**articolo
modello** scelto nella generazione: i nuovi articoli ne copiano i dati, senza giacenze, prezzi,
codici a barre, distinta, ultimi prezzi e nome straniero.

![L'articolo creato](../../_img/itemgenerator/12_articolo.png)

*L'articolo creato: descrizione, nome straniero, gruppo, prezzo nel listino.*

![Proprietà](../../_img/itemgenerator/13_articolo_proprieta.png)

*Proprietà attivate da valori e opzioni.*

![Misure e peso](../../_img/itemgenerator/14_articolo_misure.png)

*Misure e peso nei dati di vendita.*

## 7. Distinta base

Ogni valore di base e ogni opzione di variante può avere dei **componenti** (cartella *Componenti*
delle due anagrafiche): l'articolo componente, la **quantità per un'unità** dell'articolo generato
e, facoltativo, il **magazzino** di prelievo (vuoto = quello predefinito del componente). Alla
creazione l'add-on crea la distinta dell'articolo con i componenti di tutta la composizione:

1. per ogni livello, dal primo all'ultimo, i componenti del valore scelto e poi quelli delle opzioni
   scelte;
2. le opzioni **ereditate** non portano di nuovo i loro componenti;
3. lo **stesso articolo con lo stesso magazzino** diventa una riga sola con le quantità sommate;
4. la distinta ha quantità 1 e il **tipo** della configurazione (produzione, vendita, assemblaggio,
   modello); con *Nessuna*, o se la composizione non ha componenti, la distinta non si crea;
5. articolo e distinta si salvano insieme: se la distinta non si può creare non resta neanche
   l'articolo e il motivo è nella colonna *Esito* della generazione.

> SAP accetta ogni tipo di distinta solo su articoli adatti (per esempio la distinta di produzione
> su un articolo di magazzino, quelle di vendita e di assemblaggio su un articolo di vendita non di
> magazzino): l'articolo modello deve avere le caratteristiche giuste per il tipo scelto in
> configurazione.

Nell'esempio il pensile porta 2 staffe, l'opzione rovere 1 anta, la maniglia in alluminio 2
maniglie dal magazzino 01. Il pensile da 90 in rovere con maniglia in alluminio ha questa distinta:

![Distinta base](../../_img/itemgenerator/15_distinta.png)

*La distinta base creata con l'articolo.*

Nella generazione la colonna *Componenti* dell'elenco mostra quante righe avrà la distinta; dopo la
creazione l'esito dice "Con distinta base (n componenti)". La verifica della configurazione segnala
componenti inesistenti, con quantità zero o con magazzini inesistenti.

## 8. Formula della descrizione

La formula (configurazione) decide come si compongono descrizione, descrizione estesa e nome
straniero.

| Segnaposto | Diventa |
|---|---|
| `{1}`, `{2}`... | la *desc. articolo* del valore scelto al livello 1, 2... |
| `{C:1}`, `{N:1}` | il codice e la descrizione del valore scelto al livello 1 |
| `{V:CUCOL}` | la descrizione dell'opzione scelta per la variante `CUCOL` |
| `{VC:CUCOL}` | il codice dell'opzione scelta per la variante `CUCOL` |
| `{NEUTRO}` | il codice neutro |
| `[ ... ]` | parte facoltativa: compare solo se tutti i segnaposto che contiene hanno un valore |

- **Formula vuota**: le desc. articolo dei livelli in ordine.
- **In coda** vanno le descrizioni delle opzioni con posizione descrizione maggiore di zero, in
  quell'ordine, se la formula non cita già la loro variante con `{V:...}` o `{VC:...}`.
- Un segnaposto senza valore diventa vuoto; dentro `[ ]` toglie tutta la parte, separatori compresi.
- Gli spazi doppi si tolgono; con *Descrizioni in maiuscolo* tutto è in maiuscolo; maiuscole e
  minuscole non contano nei segnaposto.
- **Nome straniero**: la stessa formula con le desc. straniere (quelle italiane dove mancano); vuoto
  se nessun valore e nessuna opzione ha la desc. straniera.
- Un segnaposto sconosciuto resta nel testo, così si vede; la verifica della configurazione lo
  segnala, come le parentesi quadre non chiuse o una dentro l'altra.

Esempi con il pensile da 60 in rovere con maniglia in alluminio:

| Formula | Descrizione |
|---|---|
| *(vuota)* | `Pensile L60 Rovere Maniglia alluminio` |
| `{1} {V:CUCOL} {2}` | `Pensile Rovere L60 Maniglia alluminio` |
| `{N:1} {C:2} - {NEUTRO}` | `Mobile pensile 060 - PE060 Rovere Maniglia alluminio` |
| `{1} {2}[ con {V:CUMAN}]` | `Pensile L60 con Maniglia alluminio Rovere`; senza maniglia: `Pensile L60 Rovere` |
| *(vuota)*, maiuscolo | `PENSILE L60 ROVERE MANIGLIA ALLUMINIO` |
| *(vuota)*, nome straniero | `Wall unit L60 Oak Maniglia alluminio` |

## 9. Generazione degli articoli

La generazione è una **finestra a parte, sopra SAP**: si ingrandisce, si riduce a icona e si
ridimensiona come ogni finestra di Windows (i riquadri si adattano; i divisori tra i riquadri si
trascinano). Posizione, dimensioni, divisori e larghezza delle colonne si ricordano per utente; la
prima volta si apre a tutto schermo. Mentre è aperta SAP resta utilizzabile, anche durante la
creazione degli articoli. I colori seguono il **Tema finestre** della configurazione (capitolo 3):
nell'intestazione c'è il formato del codice, sotto un riquadro che dice da dove si è aperta la
generazione (riga di un documento, articolo simile) o cosa non va.

Le operazioni lunghe (aprire molti livelli, cercare, spuntare un ramo intero, aggiungere o creare
molti articoli) **mostrano cosa stanno facendo** in fondo alla finestra (messaggio con
l'avanzamento, barra) e si fermano con *Interrompi*; intanto i comandi sono bloccati e la finestra
resta attiva. Gli esiti si leggono in fondo, con un'icona (verde, arancio, rosso). Un errore
imprevisto si mostra in un messaggio e la finestra resta utilizzabile.

![Generazione con varianti](../../_img/itemgenerator/09_genera_varianti.png)

*Larghezze 060 e 090 della base e del pensile spuntate (su due rami), colore bianco e rovere,
maniglia in alluminio e nera: 16 articoli da comporre.*

1. **Articolo modello** (in alto, facoltativo, ricordato tra una sessione e l'altra): i nuovi
   articoli ne copiano i dati (capitolo 6). Il pulsante *...* (o F2) cerca l'articolo per codice o
   descrizione; accanto al codice si vede la descrizione, o *Articolo non trovato in anagrafica*.
   Senza modello gli articoli si creano con i soli dati della configurazione.
2. **Albero dei codici** (a sinistra): le basi del primo livello con i loro valori; il segno **+**
   apre il sotto livello di un valore. In blu i valori con varianti; passando con il mouse su un
   valore si vedono descrizione dell'articolo, varianti e sotto livello. Si **spuntano i valori
   dell'ultimo livello** (gli unici con la casella), anche più di uno e **anche su rami diversi**:
   accanto ai rami si vede quanti valori sono spuntati sotto (*✓ 2*) e sotto l'albero i loro codici
   neutri.
   - **Trova**: un codice neutro intero (es. `PE090`) porta direttamente al suo valore; altrimenti
     porta al valore successivo che ha il testo nel codice o nella descrizione (Invio per il
     successivo, Ctrl+F per tornare alla ricerca). La ricerca vale anche per i livelli non ancora
     aperti.
   - **Espandi tutto**, **Comprimi**, **Togli spunte**; **Codice neutro** mostra il neutro accanto a
     ogni valore.
   - Tasto destro su un ramo: *Spunta i valori dell'ultimo livello qui sotto*, *Togli le spunte qui
     sotto*, *Espandi qui sotto*. Doppio clic o barra spaziatrice su un valore dell'ultimo livello:
     spunta o toglie la spunta.
3. **Varianti e opzioni** (a destra): la **struttura del valore selezionato** nell'albero (clic o
   frecce), con le sue varianti nell'ordine della struttura, le opzioni da spuntare e il loro
   contributo al prezzo; il titolo dice di quale valore si tratta. Una variante ereditata lo dice
   accanto al nome: *proposta dal livello 1, Tipo: modificabile* (segue la scelta fatta sopra),
   *scelta propria, diversa dal livello 1* (con il tasto destro *Torna alle opzioni proposte*),
   *come il livello 1: eredità forzata* (capitolo 5). La stessa variante allo stesso livello si
   sceglie **una volta sola** per tutti i valori spuntati. La casella *Tutte le varianti dei valori
   spuntati, per livello* mostra invece tutte le varianti dei valori spuntati raggruppate per
   livello, con *solo per 060* se una variante riguarda solo alcuni valori. Più opzioni della stessa
   variante danno più articoli; una variante senza opzioni spuntate non entra nella composizione.
   Tasto destro: *Spunta tutte le opzioni* / *Togli tutte le opzioni*. Sotto si vede quanti articoli
   verranno composti.
4. **Aggiungi all'elenco**: compone tutte le combinazioni nell'elenco in basso, con codice,
   descrizione, prezzo, numero di componenti della distinta e stato. Di serie (opzione *Aggiungi
   all'elenco svuota prima l'elenco*, capitolo 3) l'elenco viene svuotato e contiene solo l'ultima
   selezione; con l'opzione disattivata gli articoli si accumulano e quelli già nell'elenco non si
   ripetono. Le spunte di valori e opzioni restano (si tolgono con *Togli spunte*): si cambia
   un'opzione o un valore e si aggiunge di nuovo.
5. **Genera articoli (n)**: crea gli articoli spuntati dell'elenco (n sul pulsante), uno alla volta,
   con l'esito riga per riga e la barra di avanzamento. *Interrompi* ferma la creazione dopo
   l'articolo in corso. Alla fine, in fondo alla finestra, c'è il riepilogo: *Articoli creati: n.*,
   poi, solo se ce ne sono, quelli che nel frattempo aveva già creato un altro utente e quelli con
   errori; l'elenco si posiziona sul primo articolo creato.

![Elenco degli articoli composti](../../_img/itemgenerator/08_genera.png)

*I 16 articoli composti (la fine dell'elenco): 15 già in anagrafica (in giallo) e uno da creare,
PE060004, con prezzo e numero di componenti.*

| Stato | Significato |
|---|---|
| Da creare | codice = neutro + primo suffisso libero (né in anagrafica né già nell'elenco) |
| Già esistente | la stessa composizione è già in anagrafica: il codice è quello dell'articolo esistente (giallo) |
| Creato | articolo creato (verde); l'esito dice se ha la distinta base |
| Errore | il motivo è nella colonna *Esito* (rosso): codice già usato, suffissi esauriti, codice troppo lungo, errore di SAP. Si può correggere e generare di nuovo |

![Esito della generazione](../../_img/itemgenerator/11_genera_esito.png)

*Esito della generazione: le basi da 60 e da 90 in bianco create (in verde) e il riepilogo in fondo;
senza componenti non hanno distinta base (con i componenti l'esito dice "Con distinta base").*

Nell'elenco la casella (solo sugli articoli da creare o in errore) decide quali articoli creare.
**Doppio clic** (o Invio) su un articolo creato o già esistente lo apre nell'anagrafica di SAP (la
generazione si riduce a icona e si riapre dalla barra delle applicazioni). Un articolo ancora da
creare non apre niente: in fondo alla finestra si legge *L'articolo ... non è ancora in anagrafica*;
lo stesso se nel frattempo l'articolo è stato eliminato in SAP. Tasto destro: *Apri in anagrafica*,
*Copia codice*, *Togli dall'elenco*, *Spunta tutti*, *Togli tutte le spunte*; Canc toglie le righe
selezionate, Ctrl+C ne copia i codici. *Svuota elenco* riparte da zero. Se nell'elenco ci sono
articoli non ancora creati, chiudere o svuotare chiede conferma.

### Messaggi e testi della finestra

Domande e messaggi della generazione (per esempio *Creare 2 articoli in anagrafica?*) hanno lo stesso
aspetto della finestra: Invio sceglie il pulsante evidenziato, Esc risponde No. Chi ha
l'autorizzazione **Modifica testi add-on XEI** può cambiare i testi della finestra come nelle
finestre di SAP: tasto destro su un'etichetta, un pulsante, il titolo di un riquadro, l'intestazione
di una colonna o il testo di un messaggio, poi **Modifica testo...**; **Testi di questa finestra...**
(anche in fondo ai menu degli alberi e dell'elenco) li elenca tutti. Il testo personalizzato vale per
tutti gli utenti nella lingua in uso e si vede subito.

![Domanda prima della creazione](../../_img/itemgenerator/25_messaggio.png)

*La domanda prima della creazione, con lo stile della finestra.*

![Modifica testo](../../_img/itemgenerator/26_modifica_testo.png)

*Modifica testo dal tasto destro sul pulsante Trova: testo di partenza e testo personalizzato.*

Prima di creare ogni articolo l'add-on ricontrolla che nel frattempo nessuno abbia creato la stessa
composizione o usato il codice. Ogni articolo si crea in un'unica operazione (articolo, distinta,
tabelle utente, composizione): un errore non lascia dati a metà.

## 10. Articoli da offerte e ordini cliente

Nelle **offerte cliente** e negli **ordini cliente**, tasto destro su una riga › **Configura
articolo...**:

![Configura articolo dalla riga](../../_img/itemgenerator/17_ordine_menu.png)

*Configura articolo dalla riga dell'ordine.*

La generazione si apre per quella riga (lo dicono il titolo della finestra e il riquadro in alto).
Si compone e si crea l'articolo come sempre; poi **Usa nella riga** mette nella riga del documento
l'articolo selezionato nell'elenco (creato o già esistente; se l'elenco ne ha uno solo non serve
selezionarlo), chiude la generazione e riporta in primo piano il documento. SAP compila la riga come
se il codice fosse stato scritto a mano: descrizione, prezzo del listino del cliente, magazzino.

![Generazione aperta dalla riga](../../_img/itemgenerator/18_genera_documento.png)

*Generazione aperta dalla riga 2 dell'ordine: l'articolo appena creato selezionato e "Usa nella
riga".*

![Articolo nella riga](../../_img/itemgenerator/19_ordine_riga.png)

*L'articolo nella riga dell'ordine.*

- Se la riga ha già un articolo generato dal configuratore, la generazione parte dalla sua
  configurazione: basta cambiare un'opzione per avere la variante giusta.
- Se la generazione è già aperta passa alla nuova riga; l'elenco resta, così si può riusare un
  articolo composto prima.
- Il documento deve restare aperto; un documento chiuso o non modificabile non cambia (il motivo
  compare in fondo alla finestra).

## 11. Articoli simili

Nell'anagrafica di un articolo creato dal configuratore, tasto destro › **Genera articoli
simili...**: la generazione si apre con la configurazione dell'articolo già impostata (il suo valore
finale spuntato nell'albero, già aperto fino a lui, e le opzioni scelte) e con l'articolo stesso
come modello. Si cambiano valori e opzioni e si aggiungono gli articoli all'elenco. Se la
generazione è già aperta (anche ridotta a icona) torna in primo piano con la configurazione
dell'articolo; l'elenco resta.

![Tasto destro su un articolo generato](../../_img/itemgenerator/16_simili_menu.png)

*Il tasto destro su un articolo generato.*

![Generazione di articoli simili](../../_img/itemgenerator/20_simili.png)

*Generazione dalla configurazione di PE090002 (tema SAP HANA): pensile da 90, rovere e maniglia in
alluminio già spuntati; modello l'articolo stesso.*

Se nel frattempo la configurazione è cambiata (valori tolti o disattivati, sotto livelli diversi) la
generazione parte da zero, con un avviso; le opzioni che non esistono più si ignorano.

## 12. Verifica della configurazione

Controlla tutta la configurazione (anche valori e opzioni disattivati) e mostra i problemi, prima
gli errori e poi gli avvisi. **Doppio clic** su una riga apre l'anagrafica da correggere sul record;
*Verifica di nuovo* ripete il controllo dopo le correzioni. Ingrandendo la finestra (anche a tutto
schermo) l'elenco dei problemi la segue.

![Verifica della configurazione](../../_img/itemgenerator/21_verifica.png)

*Verifica: una struttura varianti che non esiste e un valore che eredita senza varianti da
ereditare.*

| Tipo | Controllo |
|---|---|
| Errore | base senza lunghezza; codice lungo diversamente dalla base; codice ripetuto |
| Errore | sotto livello, struttura varianti, gruppo articoli, gruppo UM inesistenti; proprietà non valide |
| Errore | variante inesistente in una struttura; opzione ripetuta |
| Errore | componente senza articolo, con articolo o magazzino inesistenti, con quantità zero, per un valore o un'opzione che non c'è |
| Errore | base sotto livello di se stessa (ciclo, con il percorso); nessuna base di primo livello |
| Avviso | base senza valori attivi; struttura senza varianti; variante senza opzioni attive |
| Avviso | base che non si raggiunge dal primo livello (sotto livello solo di valori disattivati) |
| Avviso | percorso che dà codici più lunghi di 50 caratteri, suffisso compreso |
| Avviso | valore che eredita le varianti senza varianti uguali nei livelli precedenti; Forza ereditarietà senza Eredita varianti |
| Avviso | formula con segnaposto sconosciuti o parentesi quadre sbagliate |

## 13. Importazione ed esportazione con Excel

![Importazione da Excel](../../_img/itemgenerator/22_excel.png)

*Importazione del file di esempio riuscita.*

**Esporta...** chiede dove salvare e scrive tutta la configurazione in un file .xlsx, un foglio per
anagrafica, con l'intestazione in grassetto e bloccata. **Importa** legge il file indicato
(*Sfoglia...*). Ingrandendo la finestra, il nome del file e l'elenco dell'esito si allargano.

| Foglio | Una riga per | Colonne |
|---|---|---|
| Basi | valore (i dati della base si ripetono) | Base, Descrizione base, Lunghezza, Classificazione, Tabella utente, Campo utente, Codice, Descrizione, Desc. articolo, Desc. straniera, Sotto livello, Struttura varianti, Eredita varianti, Forza ereditarietà, Attivo, UM magazzino, UM acquisti, UM vendite, Valore, Dim. 1, Dim. 2, Dim. 3, Peso, Gruppo articoli, Gruppo UM, Proprietà, Note |
| Componenti basi | componente | Base, Valore, Componente, Descrizione, Quantità, Magazzino, Note |
| Varianti | opzione | Variante, Descrizione variante, Tabella utente, Campo utente, Opzione, Descrizione, Desc. straniera, Alias, Valore, Peso, Proprietà, Note, Attivo |
| Componenti varianti | componente | Variante, Opzione, Componente, Descrizione, Quantità, Magazzino, Note |
| Strutture | variante | Struttura, Descrizione struttura, Variante, Descrizione variante, Posizione, Pos. descrizione |

- Le colonne si riconoscono dal **titolo**: l'ordine non conta e quelle sconosciute si ignorano. Il
  file può avere anche solo alcuni fogli.
- Numeri all'italiana (`1.234,5`) o all'inglese (`1234.5`); sì/no con Y, S, Sì, X, 1, Vero.
- I codici con zeri iniziali (`060`) vanno scritti come testo (in Excel con l'apostrofo: `'060`),
  altrimenti Excel li trasforma in numeri.
- L'importazione **prima controlla tutto** il file: con un errore non scrive niente e l'elenco
  mostra foglio, riga e motivo di ogni errore.
- Poi scrive tutto insieme: ogni base, variante o struttura del file viene aggiunta o aggiornata e
  le sue righe **sostituiscono** quelle esistenti; i componenti cambiano solo per le basi e varianti
  presenti nei fogli dei componenti; quello che non è nel file resta com'è.

Usi tipici: esportare, modificare in Excel (nuovi valori, prezzi aggiornati) e reimportare; copiare
la configurazione in un'altra società; partire da un esempio come
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx).

## 14. Anagrafica articoli, controllo congruenze, altri add-on

### Miniatura dell'immagine

Con l'opzione *Miniatura* l'anagrafica articoli mostra l'immagine dell'articolo (campo Immagine,
nella cartella immagini di SAP) nello spazio libero della testata, a sinistra delle caselle Articolo
magazzino/vendite/acquisti. Il riquadro prende le proporzioni dell'immagine e si nasconde se
l'articolo non ha immagine. L'anagrafica non rallenta.

![Miniatura nell'anagrafica articoli](../../_img/itemgenerator/24_miniatura.png)

*La miniatura nell'anagrafica articoli.*

### Controllo congruenze

Ricalcola la composizione di tutti gli articoli generati. Serve se i dati della configurazione sono
stati modificati fuori dall'add-on; toglie anche le composizioni degli articoli eliminati da SAP.

### Integrazione con altri add-on

Con un *menu dopo creazione* in configurazione, per ogni articolo creato l'add-on lancia quel menu
dopo averne registrato il codice nella tabella XEI `@XEI_IG_EVENTS`: un altro add-on in ascolto su
quel menu può completare l'articolo.
