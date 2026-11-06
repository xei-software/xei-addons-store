---
title: XEI.ContoLavoro – Manuale d'uso
description: Come gestire con XEI.ContoLavoro le commesse terzista, gli invii di componenti, i versamenti e il conto lavoro da ordini di produzione.
lang: it
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Manuale d'uso

Installazione, licenza e menu sono descritti anche nella
[guida di installazione](installazione.md).

## 1. Cosa fa l'add-on

XEI.ContoLavoro gestisce le lavorazioni affidate a **terzisti** (subfornitori) che ricevono componenti
dall'azienda, li lavorano e restituiscono un prodotto finito o semilavorato. Per ogni lavorazione si apre una
**commessa terzista** che tiene insieme:

- i **prodotti** da ottenere, con la loro distinta base (componenti da spedire e lavorazioni da pagare);
- l'**ordine d'acquisto** al terzista, allineato automaticamente alla commessa;
- gli **invii di componenti** al magazzino del terzista, i **rientri** e gli **scarti**;
- il **versamento** dei prodotti: entrata merci di prodotti e lavorazioni, uscita dei componenti consumati,
  versamento di produzione per i prodotti che arrivano da un ordine di produzione (capitolo 6);
- la situazione in tempo reale: quanto è stato spedito, usato, cosa resta presso il terzista e cosa manca.

La commessa si chiude da sola quando tutti i prodotti sono versati e presso il terzista non restano componenti.

### In evidenza

- Testata come un trasferimento di stock, con propagazione dei magazzini alle righe e magazzino terzista protetto dopo
  i movimenti.
- Lotti e numeri di serie scelti nell'add-on: proposta dai lotti della commessa presso il terzista (tracciabilità) e
  FEFO, modificabile a mano; lotto del prodotto in entrata da script SQL configurabile; versamento in un'unica
  transazione.
- Cartella Documenti con tutti i documenti collegati, raggruppati e apribili.
- Costi dei prodotti ricalcolati a ogni salvataggio; ordine d'acquisto allineato automaticamente.
- Commesse da ordini di produzione, trasferimento massivo e tra commesse, chiusura massiva delle entrate merci.
- Stesso funzionamento su SQL Server e SAP HANA; testi traducibili.

## 2. Installazione e menu

### Installazione

- Il pacchetto `XEI.ContoLavoro.zip` si importa nell'Extension Manager di SAP Business One.
- Al primo avvio l'add-on crea tabelle, campi, oggetto (UDO) `XEI_CL_COMMESSA` e la ricerca formattata del fornitore
  terzista sul magazzino. SAP chiede di confermare che *"la struttura del database è stata modificata"*: rispondere e
  attendere la fine prima di usare il client.

### Menu

**Moduli › Amministrazione › Add-ons › XEI-Addon › Conto lavoro**:

| Voce | Funzione |
|---|---|
| Commessa terzista | apertura, ricerca e creazione delle commesse |
| Crea commesse da ordini di produzione | commesse dalle lavorazioni esterne degli ODP (capitolo 6) |
| Ricevimento dal terzista | un DDT del terzista con prodotti di più commesse: si sceglie il fornitore, si indicano le quantità ricevute sui prodotti aperti delle sue commesse (*Proponi* = residuo) e *Registra* fa il versamento commessa per commessa, con carico dei prodotti e scarico dei componenti |
| Trasferimento massivo componenti | invio componenti per più commesse (attivo con l'opzione relativa) |
| Trasferimento componenti tra commesse | sposta la giacenza già presso il terzista da una commessa a un'altra |
| Chiusura massiva entrate merci prodotti | chiude le entrate merci dei prodotti rimaste aperte |
| Prezzi lavorazioni terzisti | prezzi delle lavorazioni per fornitore e prodotto |
| Configurazione | opzioni dell'add-on |
| Informazioni, Traduzioni, Licenza | voci comuni agli add-on XEI; Licenza: stato e codice di licenza |

Le stesse voci, tranne *Configurazione*, *Informazioni*, *Traduzioni* e *Licenza*, ci sono anche nel modulo SAP
scelto in configurazione (capitolo 3), nella posizione scelta: **Moduli › Acquisti - Fornitori › Conto lavoro**
(predefinito) oppure **Moduli › Produzione › Conto lavoro**.

### Licenza

L'add-on funziona con un **codice di licenza** rilasciato da XEI. Dopo la richiesta della prova si riceve via email
un **codice di prova**, valido 30 giorni dall'invio in qualsiasi società; per l'acquisto si inviano a XEI i due codici
della finestra **Licenza** e si riceve il codice di licenza.

- Senza un codice valido l'add-on è **bloccato**: nel suo menu restano solo *Informazioni* e *Licenza*, e all'avvio si
  apre da sola la finestra **Licenza** con lo stato e il motivo.
- La finestra mostra il **codice della società** e il **codice del server**: per acquistare la licenza, con *Copia* si
  inviano a [license@xeisrl.com](mailto:license@xeisrl.com).
- Un utente SAP **superutente** incolla il codice ricevuto in *Inserisci un codice di licenza* e preme *Salva codice*:
  l'add-on si sblocca subito, senza riavviare SAP.
- Il codice di licenza vale per la società (database) o per il server dei codici inviati.
- La stessa finestra si apre in ogni momento dal menu *Licenza*: stato, scadenza, numero e ambito della licenza.

## 3. Configurazione

Le opzioni si impostano in una form a cartelle (la cartella *Lotti* è descritta nel capitolo 7). Le opzioni valgono
per tutta la società; le form già aperte le usano alla riapertura.

![Prezzi](../../_img/contolavoro/11_config_prezzi.png)

*Prezzi*

![Magazzino](../../_img/contolavoro/12_config_magazzino.png)

*Magazzino*

| Opzione | Effetto | Predef. |
|---|---|---|
| **Generale** | | |
| Ordine d'acquisto di origine | campo per collegare la commessa all'ordine d'acquisto da cui nasce | No |
| Ordine cliente di origine | colonna ordine cliente sulle righe prodotto | No |
| Prodotti senza distinta | consente prodotti senza distinta: si compone a mano | No |
| Chiudi l'entrata merci del prodotto | dopo il versamento l'entrata del prodotto viene chiusa (non va in fattura) | No |
| Ricalcola prezzo entrata prodotto | se cambia il prezzo della lavorazione aggiorna l'entrata del prodotto | No |
| Offerte fornitore da ODP | nella creazione da ODP collega le offerte fornitore | No |
| Trasferimento massivo | attiva la voce di menu | No |
| Distinta terzista | mostra la colonna "Distinta terzista" nella distinta base | Sì |
| Contratti fornitore | prezzi lavorazioni dai contratti (solo SQL Server) | No |
| Listino predefinito | listino dei costi proposto sulle nuove commesse | – |
| Menu anche nel modulo SAP | modulo con il sottomenu *Conto lavoro*: Acquisti - Fornitori o Produzione | Acquisti - Fornitori |
| Posizione nel menu del modulo | in fondo, in cima o dopo una voce del modulo | in fondo |
| **Prezzi** | | |
| Prezzo lavorazioni / componenti modificabile | prezzi modificabili nella distinta della commessa | No |
| Prezzo lavorazione / componente da distinta | prima scelta il prezzo della distinta base (componente: solo ODP) | No |
| Ripartisci costo lavorazione | ripartisce il costo totale sui prodotti (solo da ODP) | No |
| Non bloccare con prezzi a zero | il versamento è consentito anche con prezzi a zero | No |
| Rivaluta componenti | rivalutazione dei componenti nello scarico di produzione (stock continuo) | No |
| **Magazzino** | | |
| Magazzino predefinito dell'articolo | le righe componente partono dal magazzino predefinito dell'articolo | Sì |
| Giacenza come spedito | per i componenti indicati la giacenza presso il terzista vale come spedito | No |
| Componenti per riga | componenti tenuti separati per prodotto | No |
| Fabbisogno variabile | ripartisce lo spedito sui prodotti | No |
| Richieste di trasferimento | invio componenti con richiesta di trasferimento invece del trasferimento | No |
| Lista di prelievo | crea anche la lista di prelievo (attiva le richieste) | No |
| **Serie e causali** | | |
| Serie | ordine d'acquisto, entrate merci prodotti e lavorazioni, trasferimenti | predefinita SAP |
| Causali di trasporto | per trasferimenti, ordine, entrata merci, uscite, carichi (se la società usa le causali di trasporto) | – |
| **Lotti** | | |
| Script lotto in entrata | SQL con {ItemCode}, {WhsCode}, {DocEntry} che restituisce il lotto del prodotto versato (vedi capitolo 7) | commessa-progressivo |

## 4. La commessa terzista

### Testata

La testata è organizzata come quella del trasferimento di stock: a sinistra fornitore, riferimento del fornitore,
progetto e ordini collegati; a destra numerazione, stato, date, listino dei costi e i due magazzini.

- **Fornitore**: alla scelta propone il magazzino dell'utente e il **magazzino terzista** collegato al fornitore
  (campo "Fornitore terzista" dell'anagrafica magazzino) o quello marcato come predefinito.
- **Da magazzino**: magazzino dell'azienda; da qui partono i componenti, qui rientrano i prodotti e su questo
  magazzino nascono le righe dell'ordine d'acquisto.
- **A mag. terzista**: si può cambiare solo finché la commessa non ha movimenti di componenti; dopo il campo si
  disattiva e il salvataggio rifiuta comunque la modifica.
- Cambiando un magazzino di testata viene proposto, come nel trasferimento di stock, di riportarlo sulle righe della
  distinta **non ancora movimentate**.

### Prodotti

Si sceglie l'articolo (anche più articoli insieme dalla lista) e la quantità da produrre: la distinta base viene
copiata da SAP rapportandola a un pezzo (considerando la quantità base della distinta). Le colonne mostrano quantità
da produrre, versata, saldo, costo dei componenti e delle lavorazioni.

### Distinta base

Per ogni prodotto: componenti (articoli di magazzino da spedire) e lavorazioni (servizi pagati al terzista). Con
**Modifica distinta** si cambiano magazzini e prezzi delle righe non ancora movimentate; con *Aggiungi riga* /
*Elimina riga* di SAP si aggiungono componenti e lavorazioni o si tolgono quelli non movimentati. Dal menu contestuale
della riga prodotto: **Rilavora** (il prodotto torna al terzista come componente con le nuove lavorazioni) e
**Ricomponi distinta** (sostituisce la distinta con i componenti scelti).

### Componenti

I componenti di tutti i prodotti raggruppati per articolo e magazzini: fabbisogno, usato, disponibile in azienda,
giacenza nel magazzino del terzista, richieste e liste di prelievo, spedito, saldo da spedire, giacenza della commessa
presso il terzista, rientri e scarti. I movimenti si fanno con i pulsanti in fondo alla commessa: **Invia componenti**
e **Rientro e scarti** (*Rientro componenti dal terzista*, *Trasferisci scarti*, *Uscita scarti presso il
terzista*). Ognuno apre una finestra con le quantità da movimentare nelle celle gialle: *Proponi* le compila,
*Azzera* le svuota, e si possono cambiare a mano.

### Documenti

Tutti i documenti SAP collegati alla commessa, uno per riga in ordine di tempo, con il collegamento per aprirli;
*Mostra* filtra per tipo di documento. Sotto, in *Righe del documento*, le righe del documento scelto con lotti,
numeri di serie e ubicazioni.

## 5. Flusso operativo

1. **Commessa**: fornitore, magazzini, prodotti e quantità; *Aggiungi*.
2. **Ordine al terzista**: la finestra *Ordine d'acquisto terzista* crea l'ordine d'acquisto, con una riga per
   prodotto e una per ogni lavorazione; se l'ordine c'è già, il pulsante lo apre. Le modifiche successive della
   commessa (prodotti nuovi o eliminati, quantità, prezzi, date) si riportano sull'ordine al salvataggio; le righe già
   ricevute cambiano solo di quantità.
3. **Invia componenti**: nella finestra *Trasferimento componenti* la colonna *Da spedire* propone il saldo da
   spedire (si cambia a mano); *OK* crea il trasferimento di stock al magazzino del terzista. Con l'opzione relativa
   si crea una richiesta di trasferimento con lista di prelievo.
4. **Ricevi prodotti**: nella finestra *Versamento prodotti* la colonna *Da versare* propone il residuo (si cambia a
   mano) e *Tipo movimento* sceglie tra *Carico prodotti e scarico componenti*, *Solo carico prodotti* e *Solo scarico
   componenti*; poi *OK*. Vengono creati: entrata merci delle lavorazioni e dei prodotti dall'ordine d'acquisto, uscita
   merci dei componenti dal magazzino del terzista, versamenti di produzione per i prodotti da ODP (capitolo 6).

> Il prodotto entra al costo pieno (componenti + lavorazione); con l'opzione "Chiudi l'entrata merci del prodotto"
> l'entrata viene chiusa e non va in fattura: si fatturano le lavorazioni.

Se un componente da scaricare supera la giacenza della commessa presso il terzista viene chiesto se scaricare la
giacenza rimanente (Sì / No / Sì per tutti).

## 6. Conto lavoro da ordini di produzione

Quando alcune fasi di un **ordine di produzione (ODP)** si fanno presso terzisti, l'add-on crea le commesse terzista
dalle righe dell'ODP. A ogni versamento preleva per l'ODP i componenti consumati dal terzista e, quando sono rientrate
tutte le lavorazioni esterne, registra il versamento di produzione del prodotto finito.

### Impostazione in SAP

> La lavorazione esterna è un **articolo non gestito a magazzino** con il campo **Conto lavoro** = Sì, non una
> risorsa di SAP: una lavorazione impostata come risorsa non compare nella lista degli ODP.

| Dove | Cosa imposti | Nell'esempio |
|---|---|---|
| Anagrafica dell'articolo della lavorazione | articolo non gestito a magazzino, campo utente **Conto lavoro** = Sì; il **fornitore preferito** è il terzista proposto nella lista | `LAV-SALD` Saldatura telaio, fornitore `F-TER01`; `LAV-MONT` Montaggio assale, fornitore `F-TER02` |
| Distinta base del prodotto finito | una riga per ogni lavorazione esterna, con la quantità per pezzo; sulle righe dei componenti da inviare al terzista il campo **Lavorazione terzista** con il codice della lavorazione e il metodo di prelievo **Manuale** | `CMP-01`, `CMP-02` → `LAV-SALD`; `CMP-03`, `CMP-04` → `LAV-MONT` |
| Distinta base del prodotto finito | **Distinta terzista** = Sì se il prodotto finito è completo quando rientrano tutte le lavorazioni esterne: l'add-on registra il versamento di produzione. Con No il versamento di produzione lo registri tu in SAP | `PF-100` = Sì |
| Anagrafica del magazzino del terzista | campo **Fornitore terzista** (capitolo 4) | `T-TER01` → `F-TER01`; `T-TER02` → `F-TER02` |
| *Prezzi lavorazioni terzisti* | prezzo per terzista, prodotto finito e lavorazione (ordine di ricerca del prezzo nel capitolo 9) | `F-TER01` / `PF-100` / `LAV-SALD` 12,00; `F-TER02` / `PF-100` / `LAV-MONT` 3,50 |

I componenti a consuntivo collegati alla lavorazione non si inviano al terzista: li preleva il versamento di
produzione dal magazzino della riga ODP. La colonna **Motivo / avvisi** della lista lo segnala. Gli altri componenti
della distinta, che non hanno la lavorazione, restano come in ogni ODP.

> **Controllo al salvataggio della distinta.** Quando salvi una distinta base che ha il campo **Lavorazione
> terzista** compilato, l'add-on controlla i codici indicati. Se qualcosa non va compare l'avviso *"Distinta PF-100,
> campo "Lavorazione terzista":"* con un punto per ogni caso; la distinta resta salvata.
>
> - Risorsa: *"LAV-SALD è una risorsa: la lavorazione esterna va creata come articolo non gestito a magazzino con
>   "Conto lavoro" = Sì, e i componenti vanno collegati a quel codice."*
> - Codice che non è un articolo: *"LAV-SALD non è un articolo."*
> - Articolo senza Conto lavoro: *"L'articolo LAV-SALD non ha "Conto lavoro" = Sì nell'anagrafica."*
> - Lavorazione che non è riga della distinta: *"LAV-SALD non è una riga della distinta: l'ordine di produzione non
>   avrà la riga della lavorazione e non si potrà creare la commessa."*
> - Componenti a consuntivo: *"Componenti a consuntivo con la lavorazione LAV-SALD: non vengono inviati al terzista
>   (servono con prelievo manuale)."*

### Esempio passo per passo

Il prodotto finito `PF-100` Carrello ha due lavorazioni esterne: la saldatura del telaio presso `F-TER01` «Terzista
Esempio 1» e il montaggio degli assali presso `F-TER02` «Terzista Esempio 2». Ogni carrello ha un telaio e due
assali. L'ODP n. 500 è rilasciato per 100 carrelli nel magazzino `01`:

| Riga | Articolo | Quantità | Prelievo | Lavorazione terzista | Prezzo |
|---|---|---|---|---|---|
| 1 | `LAV-SALD` Saldatura telaio (lavorazione) | 100 | | | 12,00 |
| 2 | `CMP-01` Tubo (m) | 250 | Manuale | `LAV-SALD` | 4,00 |
| 3 | `CMP-02` Piastra | 400 | Manuale | `LAV-SALD` | 1,50 |
| 4 | `LAV-MONT` Montaggio assale (lavorazione) | 200 | | | 3,50 |
| 5 | `CMP-03` Ruota | 400 | Manuale | `LAV-MONT` | 5,00 |
| 6 | `CMP-04` Perno | 200 | Manuale | `LAV-MONT` | 2,00 |
| 7 | `CMP-05` Vite | 1.600 | a consuntivo | | |

| Passo | Documento SAP creato | Effetto sull'ODP |
|---|---|---|
| 1. **Conto lavoro › Crea commesse da ordini di produzione**: selezioni le due righe dell'ODP 500 e premi *Crea commesse* | nessun documento SAP: commessa terzista 1001 (`F-TER01`, da `01` a `T-TER01`, prodotto `LAV-SALD` 100, distinta `CMP-01` 2,5 e `CMP-02` 4 per pezzo) e commessa 1002 (`F-TER02`, da `01` a `T-TER02`, prodotto `LAV-MONT` 200, distinta `CMP-03` 2 e `CMP-04` 1 per pezzo) | nessuno |
| 2. In ogni commessa premi *Ordine al terzista* e conferma la finestra *Ordine d'acquisto terzista* | ordine d'acquisto a `F-TER01`: `LAV-SALD` 100 × 12,00; ordine d'acquisto a `F-TER02`: `LAV-MONT` 200 × 3,50 | nessuno |
| 3. In ogni commessa premi *Invia componenti* e, con le quantità proposte, *OK* | trasferimento di stock da `01` a `T-TER01`: `CMP-01` 250, `CMP-02` 400; da `01` a `T-TER02`: `CMP-03` 400, `CMP-04` 200 | nessuno |
| 4. Rientrano 60 telai: nella commessa 1001 premi *Ricevi prodotti*, nella finestra *Versamento prodotti* scrivi 60 in *Da versare* e premi *OK* | entrata merci dall'ordine: `LAV-SALD` 60 × 12,00; uscita merci per produzione da `T-TER01`: `CMP-01` 150, `CMP-02` 240 | prelevati i componenti delle righe 2 e 3; nessun versamento: mancano gli assali, e un messaggio lo dice (*"ODP 500: il prodotto finito entrerà in magazzino quando rientrerà anche la lavorazione LAV-MONT."*) |
| 5. Rientrano 100 assali: commessa 1002, *Ricevi prodotti*, 100 in *Da versare*, *OK* | entrata merci `LAV-MONT` 100 × 3,50; uscita merci per produzione da `T-TER02`: `CMP-03` 200, `CMP-04` 100; versamento di produzione `PF-100` **50** | 60 telai e 100 assali bastano per 50 carrelli: 50 completati; SAP preleva a consuntivo `CMP-05` 800 |
| 6. Rientrano altri 100 assali: commessa 1002, *Ricevi prodotti*, 100 in *Da versare*, *OK* | entrata merci `LAV-MONT` 100; uscita merci per produzione `CMP-03` 200, `CMP-04` 100; versamento di produzione `PF-100` **10** | 60 completati, gli altri aspettano i telai (*"ODP 500: entrati 10 pezzi del prodotto finito; gli altri entreranno quando rientrerà anche la lavorazione LAV-SALD."*); la commessa 1002 si chiude da sola |
| 7. Rientrano gli ultimi 40 telai: commessa 1001, *Ricevi prodotti*, 40 in *Da versare*, *OK* | entrata merci `LAV-SALD` 40; uscita merci per produzione `CMP-01` 100, `CMP-02` 160; versamento di produzione `PF-100` **40** | 100 completati; la commessa 1001 si chiude da sola. L'ODP lo chiudi tu in SAP |

> Il versamento di produzione vale il costo delle lavorazioni esterne per pezzo: per ogni lavorazione, componenti e
> prezzo della lavorazione, per la quantità per pezzo. Nell'esempio un carrello vale
> (2,5 × 4,00 + 4 × 1,50 + 12,00) + 2 × (2 × 5,00 + 1 × 2,00 + 3,50) = 28,00 + 31,00 = **59,00**.

### Casi particolari

- **Più ODP**: le righe con lo stesso fornitore e lo stesso magazzino di rientro (colonna *Mag. rientro*) vanno nella
  stessa commessa, un prodotto per riga; con magazzini di rientro diversi nascono commesse diverse.
- **Servizi del terzista**: un componente non gestito a magazzino con **Lavorazione terzista** (per esempio un
  collaudo) diventa una lavorazione della commessa, con una riga in più nell'ordine al terzista.
- **Distinta terzista = No**: l'add-on registra l'entrata merci della lavorazione e l'uscita dei componenti; il
  versamento di produzione lo registri tu in SAP, per esempio dopo un montaggio interno.
- **Versamenti di produzione registrati in SAP** sullo stesso ODP: l'add-on li sottrae, il prodotto finito non entra
  due volte.
- **Commessa interrotta**: se interrompi una commessa, la lavorazione torna nella lista e puoi crearne un'altra.
- **Componenti a consuntivo**: i componenti a consuntivo collegati alla lavorazione non si inviano al terzista; la
  colonna **Motivo / avvisi** lo segnala.
- **Distinta della commessa**: nei prodotti da ODP non si modifica; cambi il prezzo della lavorazione (colonna
  *Costo lav.*), che si riporta sull'ordine al terzista al salvataggio. Con l'opzione *Ripartisci costo lavorazione*
  il *Costo lav. totale* della testata si divide sui prodotti in proporzione alla quantità.
- L'opzione *Chiudi l'entrata merci del prodotto* non vale per le commesse da ODP: l'entrata merci della lavorazione
  resta aperta, da fatturare.
- **Offerte fornitore**: con l'opzione *Offerte fornitore da ODP*, *Offerta fornitore* collega alla riga una riga
  d'offerta, con il suo fornitore, prezzo e data di consegna; le righe d'offerta non scelte si chiudono.

### Perché un ODP non compare nella lista

La lista mostra le lavorazioni pronte per diventare commessa. Accendi **Mostra anche le righe non pronte**: compaiono
anche le altre, con il motivo e cosa fare nella colonna **Motivo / avvisi**. Le righe non pronte non si selezionano;
se fai clic sulla loro casella di selezione il motivo compare anche nella barra di stato.

| Motivo (esempio a video) | Cosa fare |
|---|---|
| Già nella commessa n. 1001. | niente: apri la commessa dalla colonna *Commessa* |
| LAV-SALD è una risorsa: la lavorazione esterna va creata come articolo non gestito a magazzino con "Conto lavoro" = Sì, e i componenti vanno collegati a quel codice. | crea l'articolo della lavorazione e scrivi il suo codice in **Lavorazione terzista** sui componenti |
| I componenti indicano la lavorazione LAV-SALD, che non è un articolo. | correggi **Lavorazione terzista** sui componenti o crea l'articolo |
| L'articolo LAV-SALD non ha "Conto lavoro" = Sì nell'anagrafica. | imposta **Conto lavoro** = Sì nell'anagrafica dell'articolo |
| L'ODP non ha la riga della lavorazione LAV-SALD: aggiungerla all'ODP (o alla distinta del prodotto). | aggiungi la riga all'ODP, o alla distinta per i prossimi ODP |
| Nessun componente da inviare: sulle righe dei componenti indicare "Lavorazione terzista" = LAV-SALD e il prelievo manuale. | compila i componenti da inviare, con metodo di prelievo Manuale |
| ODP non rilasciato: rilasciarlo in SAP. | rilascia l'ODP |

Una lavorazione impostata come risorsa di SAP è una causa frequente: la lavorazione esterna va creata come articolo
non gestito a magazzino con **Conto lavoro** = Sì.

Sulle righe pronte la stessa colonna dà gli avvisi che non impediscono la selezione:

| Avviso | Cosa fare |
|---|---|
| Componenti a consuntivo con questa lavorazione: non vengono inviati al terzista (servono con prelievo manuale). | se vanno inviati, metti il metodo di prelievo Manuale |
| Indicare il fornitore. | scegli il fornitore nella colonna *Fornitore* |
| Il fornitore F-TER01 non ha un magazzino terzista collegato. | collega il magazzino del terzista al fornitore (campo **Fornitore terzista**): senza, la commessa non si crea |

## 7. Lotti, numeri di serie e ubicazioni

Per trasferimenti, rientri, scarti e uscita dei componenti nel versamento, i lotti e i numeri di serie si scelgono in
una finestra dell'add-on, **prima** di creare i documenti. Tutti i documenti vengono poi creati in un'unica
operazione.

- **Proposta automatica**: dal magazzino del terzista (uscita componenti, rientro, scarti) prima i lotti **spediti a
  quella commessa** (colonna "Della commessa", ricavata dal registro movimenti lotti di SAP), poi per scadenza
  (FEFO); dal magazzino dell'azienda per scadenza (FEFO).
- **Scelta manuale**: la colonna "Da usare" è modificabile; la quantità è limitata alla giacenza del lotto (al netto
  di altre righe sullo stesso lotto) e a 1 per i numeri di serie. *Proponi* rifà la proposta, *Azzera* svuota tutto.
  La conferma è possibile solo quando ogni riga ha esattamente la quantità richiesta.
- Sono proposti solo lotti e numeri di serie **rilasciati** (non bloccati né non accessibili).
- Le richieste di trasferimento non movimentano lotti: per loro non si apre nessuna selezione.

### Lotto del prodotto in entrata

Il lotto del prodotto versato viene calcolato da uno **script SQL** configurabile (Configurazione › Lotti), con tre
parametri fissi: `{ItemCode}` articolo, `{WhsCode}` magazzino di carico, `{DocEntry}` commessa. Lo script
predefinito restituisce numero commessa + progressivo (es. `20160256-1`); *Verifica* lo esegue con dati di prova. Il
lotto creato compare nel messaggio di fine versamento.

![Script del lotto in entrata](../../_img/contolavoro/19_config_lotti.png)

*Script del lotto in entrata*

### Documenti in bozza

Il documento nasce in bozza, da completare nella form SAP, con magazzini a **ubicazioni**, prodotti in entrata con
**numeri di serie**, script del lotto vuoto o senza risultato e nel trasferimento massivo. Si completa il documento e
si preme *Aggiungi*: l'add-on elimina la bozza e prosegue.

## 8. Rientri e scarti

- **Rientro e scarti › Rientro componenti dal terzista**: quantità in *Da far rientrare* (*Proponi* = giacenza della
  commessa presso il terzista), poi *OK*: trasferimento dal magazzino del terzista al magazzino dell'azienda.
- **Rientro e scarti › Trasferisci scarti**: quantità in *Da scartare*; sposta gli scarti dal terzista a un
  magazzino a scelta.
- **Rientro e scarti › Uscita scarti presso il terzista**: nella finestra *Uscita scarti*, uscita merci degli scarti
  direttamente dal magazzino del terzista.

I componenti scartati tornano nel saldo da spedire.

## 9. Funzioni di servizio

### Commesse da ordini di produzione

Elenca le lavorazioni esterne degli ODP rilasciati, pronte per diventare commessa, e crea **una commessa per
fornitore e magazzino di rientro**. Con *Mostra anche le righe non pronte* spiega perché una lavorazione non è pronta.
Impostazione, esempio completo e casi particolari nel capitolo 6.

### Trasferimento massivo componenti

Analizza le commesse aperte (filtri per date, fornitore, componente) e propone i componenti con saldo da spedire,
rispettando la disponibilità condivisa tra le commesse se la società blocca le giacenze negative. Crea un
trasferimento per fornitore (in bozza se servono lotti o ubicazioni). Le righe con magazzino terzista mancante o
uguale a quello di partenza vengono escluse e segnalate.

### Trasferimento componenti tra commesse

Sposta la giacenza già presso il terzista da una commessa a un'altra senza movimenti di magazzino (solo
registrazione). Per questo è possibile solo tra commesse **aperte** con lo **stesso magazzino terzista**: la lista
propone solo quelle; con magazzini diversi l'operazione è bloccata e la merce va rientrata e rispedita. La giacenza
viene riletta al momento della conferma.

### Chiusura massiva entrate merci prodotti e prezzi lavorazioni

*Chiusura massiva entrate merci prodotti* elenca le entrate merci dei prodotti ancora aperte e chiude quelle scelte.
*Prezzi lavorazioni terzisti* è la tabella dei prezzi delle lavorazioni per terzista e prodotto.

Ordine di ricerca del prezzo di una lavorazione: contratti fornitore (opzione, solo SQL Server), prezzi per terzista,
distinta base (opzione), prezzo del fornitore SAP, listino della commessa.

## 10. Dati, campi e tipi di movimento

| Tabella | Contenuto |
|---|---|
| `@XEI_CL_OCNT` | testata commessa (UDO `XEI_CL_COMMESSA`, con serie) |
| `@XEI_CL_CNT1` | prodotti |
| `@XEI_CL_CNT2` | distinta (componenti e lavorazioni) |
| `@XEI_CL_PRZLAV` | prezzi lavorazioni per terzista e prodotto |
| `@XEI_CL_TRCOMM` | trasferimenti tra commesse |

Campi sulle tabelle SAP (prefisso `XEI_CL_`):

| Campo | Tabelle | Contenuto |
|---|---|---|
| `U_XEI_CL_ENTRY` | righe dei documenti | commessa (DocEntry) |
| `U_XEI_CL_LINENUM` | righe dei documenti | riga prodotto o di distinta |
| `U_XEI_CL_TYPE` | righe dei documenti | tipo di movimento (tabella sotto) |
| `U_XEI_CL_TXT`, `U_XEI_CL_OPIT`, `U_XEI_CL_ITEM`, `U_XEI_CL_WKEY`, `U_XEI_CL_ENBL` | righe dei documenti | testo, articolo e ODP di riferimento, offerte utilizzabili |
| `U_XEI_CL_ICNT` | articoli | articolo in conto lavoro |
| `U_XEI_CL_TERZF`, `U_XEI_CL_DFTR` | magazzini | fornitore terzista del magazzino, magazzino terzista predefinito |
| `U_XEI_CL_DISTTERZ` | distinte base | distinta terzista (versamento di produzione da ODP) |
| `U_XEI_CL_ILAV` | righe distinta e ODP | lavorazione a cui appartiene il componente |

Se la società li usa, l'add-on compila anche codice commerciale, causale di trasporto, porto e vettore dei
documenti.

| Tipo | Documento | Significato |
|---|---|---|
| EMP | ordine d'acquisto, entrata merci | prodotto |
| OAL | ordine d'acquisto, entrata merci | lavorazione |
| UMC | uscita merci (per produzione se da ODP) | componenti consumati |
| TSO | trasferimento o richiesta | componenti inviati al terzista |
| TSI | trasferimento | rientro componenti |
| TSS | trasferimento | trasferimento scarti |
| UMR | uscita merci | scarti presso il terzista |
| EPR | versamento di produzione | prodotto finito dell'ODP (capitolo 6) |

Nei calcoli sono esclusi i documenti annullati e i resi vengono sottratti riga per riga.

## 11. Lingue

L'add-on segue la lingua del client SAP. Sono disponibili **italiano** (lingua di base), **inglese**, **tedesco**,
**francese**, **spagnolo** e **turco**: menu, form, colonne, pulsanti, messaggi e commenti dei documenti creati. Con
una lingua non prevista si usa l'italiano.

| Lingua SAP | Testi dell'add-on | Commessa terzista | Terzista |
|---|---|---|---|
| Italian (Italy) | italiano | Commessa terzista | terzista |
| English (United States / United Kingdom) | inglese | Subcontracting Job | subcontractor |
| German | tedesco | Lohnfertigungsauftrag | Lohnfertiger |
| French | francese | Ordre de sous-traitance | sous-traitant |
| Spanish (Spain / Latin America) | spagnolo | Orden de subcontratación | subcontratista |
| Turkish | turco | Fason iş emri | fasoncu |

I termini seguono quelli di SAP Business One nella stessa lingua (per esempio *Vendor*, *Posting Date*, *Inventory
Transfer*, *Bill of Materials*, *Batch* in inglese; *Tedarikçi*, *Kayıt tarihi*, *Stok nakli*, *Ürün ağacı*, *Parti*
in turco).

### Cambiare lingua

1. **Amministrazione › Configurazione › Generale › Utenti**, cartella *Visualizzare*, campo *Lingua*, poi *Aggiorna*.
2. SAP avvisa che tutte le finestre aperte verranno chiuse: rispondere *Sì*.
3. L'add-on ricarica da solo i testi e ricrea i menu nella nuova lingua: non serve riavviarlo.

### Personalizzare i testi

Ogni testo si può cambiare per il singolo cliente dal menu **Traduzioni** dell'add-on o con il tasto destro sulle
form (*Modifica testo…*, *Testi di questa form…*). Serve l'autorizzazione `XEI_TEXTS` (i superuser l'hanno sempre).
Le personalizzazioni restano negli aggiornamenti dell'add-on.

Restano in italiano i testi salvati nel database da SAP, per esempio le descrizioni dei campi utente e il titolo
della tabella *Prezzi lavorazioni terzisti*. Le voci *Informazioni*, *Traduzioni* e *Licenza* del framework, con le
loro finestre, sono in italiano in tutte le lingue.
