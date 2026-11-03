---
title: XEI Rate Updater per SAP Business One – Manuale d'uso
description: "Cambi delle valute in SAP Business One: installazione, primo avvio, aggiornamento a mano e automatico, storico e licenza."
lang: it
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater per SAP Business One – Manuale d'uso

| | |
|---|---|
| SAP Business One | 10.0 o successive, con il Service Layer |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Sistema | Windows 10 e 11, Windows Server 2016 e successivi, a 64 bit; Microsoft Edge WebView2 Runtime |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |

## 1. Cosa fa

XEI Rate Updater per SAP Business One aggiorna i **cambi delle valute** in SAP Business One con i tassi pubblicati da una fonte ufficiale:

1. prende i tassi della **fonte** scelta per la data richiesta;
2. legge dalla società SAP la **valuta locale** e il **verso** dei cambi: tasso diretto (valuta locale per una unità di
   valuta estera) o tasso indiretto (valuta estera per una unità di valuta locale);
3. se la valuta locale non è l'euro, calcola i **tassi incrociati** rispetto a quella;
4. per ogni **valuta gestita dalla società** scrive in SAP il cambio alla data, nel verso della società, troncato a sei
   decimali;
5. salva l'esecuzione nello **storico**.

Un errore su una valuta non ferma le altre.

### La data dei tassi

I tassi di un giorno si pubblicano a fine giornata. Per i cambi in SAP di un giorno si usano quindi i tassi pubblicati
**il giorno prima**. Nei giorni senza pubblicazione (fine settimana, festivi) vale l'ultimo giorno pubblicato prima.

*Esempio*: i cambi di lunedì 24 febbraio 2025 sono i tassi di venerdì 21 febbraio. La data dei cambi non può essere nel
futuro.

### Le fonti dei tassi

| Fonte | Note |
|---|---|
| Banca centrale europea (BCE) | predefinita, gratuita, senza chiave |
| Banca d'Italia | cambi ufficiali italiani, molte valute |
| Open Exchange Rates | serve una chiave API di Open Exchange Rates (Impostazioni › Cambi) |

Tutte le fonti pubblicano i tassi rispetto all'euro. Con una valuta locale diversa dall'euro la fonte deve quotarla.

### Le valute

Il programma riconosce le valute dal **codice ISO** (per esempio `USD`, `CHF`). In SAP le valute estere devono avere
il codice ISO come codice. Per la valuta locale, se in SAP ha un altro codice (per esempio «Eu» o «€» per l'euro), si
indica il codice ISO in *Impostazioni › Cambi*.

## 2. Installazione

1. Estrai la cartella dello zip sul PC, per esempio in `C:\XEI\RateUpdater`.
2. Avvia **XEI.RateUpdater.exe**. Il programma contiene già .NET. Serve **Microsoft Edge WebView2 Runtime**, che di
   solito c'è già: se manca, il programma lo dice e propone di scaricarlo.

Il programma non ha installazione. Le impostazioni e lo storico stanno nella cartella dei dati di Windows di tutti gli
utenti del PC, quindi valgono per chiunque usi il programma su quel PC e per l'aggiornamento pianificato.

## 3. Primo avvio

Alla prima apertura il programma mostra la pagina **Primo avvio**: non è ancora collegato a SAP. Il codice del primo
avvio è già scritto.

1. **Collegamento a SAP**:
   - *Indirizzo del Service Layer*;
   - *Società SAP*: i database selezionabili all'accesso;
   - **Prova la connessione**.
2. **Accesso e primo amministratore**:
   - *Accesso degli operatori*: **Utente SAP di ognuno** (ognuno entra con il proprio utente SAP) oppure **Utenti propri
     e utente SAP tecnico**;
   - *Utente SAP del primo amministratore* (per esempio `manager`);
   - *Utente SAP tecnico* e la sua password: servono per l'**aggiornamento automatico**. Meglio un utente dedicato, con
     il solo permesso di scrivere i cambi.
3. **Salva e riavvia**: il programma si riapre sulla pagina di accesso.

Le stesse impostazioni si cambiano poi in **Impostazioni › SAP**.

![Primo avvio](../../_img/rateupdater/00b-primo-avvio.png)

*Primo avvio: collegamento a SAP, ambito della licenza e primo amministratore.*

![Impostazioni › SAP](../../_img/rateupdater/05-impostazioni-sap.png)

*Impostazioni › SAP: indirizzo del Service Layer, società e accesso degli operatori.*

## 4. Accesso

Si entra con l'**utente SAP Business One** e la sua password. In alto a destra si vedono utente e società.

![Accesso](../../_img/rateupdater/00-accesso.png)

*Accesso con l'utente SAP Business One.*

Con *Utente SAP di ognuno* il programma scrive i cambi con l'utente di chi lavora: valgono le sue autorizzazioni SAP sui
cambi.

### Funzioni degli utenti

Un amministratore assegna a ogni utente le funzioni dalla pagina **Utenti** del menu, uguale per gli utenti SAP e per
gli utenti propri:

| Funzione | Cosa permette |
|---|---|
| Aggiornamento cambi | aggiornare i cambi in SAP dalla pagina Cambi |
| Storico | vedere le esecuzioni dell'aggiornamento, manuali e automatiche |

L'amministratore ha tutte le funzioni. Il primo amministratore è l'utente SAP indicato nel Primo avvio.

## 5. Cambi

Menu **Cambi**.

1. **Data dei cambi in SAP**: di partenza è oggi, non può essere nel futuro. Sotto si legge quali tassi si usano e la
   fonte impostata.
2. Premi **Aggiorna i cambi in SAP**.
3. L'**esito** dice data, fonte, giorno dei tassi, quante valute sono state scritte e la valuta locale. La tabella mostra
   per ogni valuta della fonte:

| Colonna | Cosa mostra |
|---|---|
| Valuta | codice ISO |
| Tasso diretto | valuta locale per una unità di valuta estera |
| Tasso indiretto | valuta estera per una unità di valuta locale |
| Esito | **scritta in SAP**, **non gestita** (la società non usa questa valuta) oppure rifiutata, con l'errore di SAP |

Sotto c'è lo stato dell'**aggiornamento automatico**, con l'ultima esecuzione.

![Cambi](../../_img/rateupdater/01-cambi.png)

*Cambi: data, fonte e stato dell'aggiornamento automatico.*

![Esito dell'aggiornamento](../../_img/rateupdater/02-cambi-esito.png)

*Esito: tassi della fonte, valute scritte in SAP e valute che la società non gestisce.*

## 6. Storico

Menu **Storico**: le esecuzioni della società, dalla più recente.

| Colonna | Cosa mostra |
|---|---|
| Avviata | data e ora dell'esecuzione |
| Da | l'utente, oppure *automatica* |
| Cambi al | la data dei cambi in SAP |
| Fonte | la fonte dei tassi |
| Tassi del | il giorno dei tassi usati |
| Valute scritte | quante valute sono state scritte in SAP |
| Esito | **riuscita** o **non riuscita** |

Una riga si apre sulle valute, con i tassi e l'esito di ognuna. Lo storico tiene le ultime esecuzioni (100 di partenza,
in *Impostazioni › Cambi*).

![Storico](../../_img/rateupdater/03-storico.png)

*Storico: aggiornamenti manuali e automatici della società.*

![Storico con le valute](../../_img/rateupdater/03b-storico-valute.png)

*Una riga aperta: tassi ed esito di ogni valuta.*

## 7. Impostazioni › Cambi

Solo per gli amministratori. Dopo le modifiche premi **Salva le impostazioni**.

| Impostazione | Cosa fa |
|---|---|
| Fonte dei tassi | Banca centrale europea (predefinita), Banca d'Italia oppure Open Exchange Rates |
| Codice ISO della valuta locale | solo se in SAP la valuta locale ha un codice diverso da quello ISO; vuoto = si ricava da SAP |
| Chiave API di Open Exchange Rates | solo con la fonte Open Exchange Rates; si salva cifrata |
| Aggiornamento automatico | ogni giorno il programma aggiorna da solo i cambi di oggi di ogni società, con l'utente SAP tecnico |
| Ora dell'aggiornamento automatico | nel formato HH:mm (predefinita 07:00) |
| Esecuzioni nello storico | quante esecuzioni tenere per ogni società, da 10 a 1000 (predefinito 100) |

![Impostazioni › Cambi](../../_img/rateupdater/04-impostazioni-cambi.png)

*Impostazioni › Cambi: fonte, valuta locale, aggiornamento automatico e storico.*

## 8. Aggiornamento automatico

I cambi di oggi si aggiornano ogni giorno in due modi.

### Con il programma aperto

Con **Aggiornamento automatico** acceso, passata l'ora impostata il programma aggiorna i cambi di oggi di ogni società
con l'utente SAP tecnico e salva l'esecuzione nello storico (*Da*: automatica). Se il programma era chiuso all'ora
stabilita, aggiorna appena si riapre. Se la fonte o SAP non rispondono, riprova poco dopo.

### Con l'Utilità di pianificazione di Windows

Così i cambi si aggiornano anche senza aprire il programma.

1. Fai il primo avvio e imposta l'**utente SAP tecnico** (Impostazioni › SAP).

   ![Utente SAP tecnico](../../_img/rateupdater/05b-impostazioni-sap-tecnico.png)

   *L'utente SAP tecnico in Impostazioni › SAP.*

2. In Windows apri **Utilità di pianificazione** e crea un'attività di base, per esempio ogni giorno alle 7:00.
3. Come azione scegli **Avvia programma**:
   - programma: `XEI.RateUpdater.exe` nella cartella del programma;
   - argomenti: `aggiorna`.
4. Nelle proprietà dell'attività scegli **Esegui indipendentemente dalla connessione dell'utente**, con un utente
   Windows del PC.

Il comando aggiorna i cambi di oggi con l'utente SAP tecnico e si chiude, senza finestra. Usa le stesse impostazioni e
lo stesso storico del programma. Argomenti facoltativi:

| Argomento | Significato |
|---|---|
| `--societa <database SAP>` | la società da aggiornare; con una sola società configurata non serve |
| `--data aaaa-mm-gg` | la data dei cambi, se non è oggi |

L'Utilità di pianificazione riceve il risultato: **0** riuscito, **1** non riuscito o con una valuta rifiutata, **2**
argomenti sbagliati. Il dettaglio è nello storico. Se il comando ha già aggiornato i cambi di oggi, il programma aperto
non li rifà.

## 9. Licenza

Il programma funziona con un **codice di licenza** rilasciato da XEI, in tre ambiti:

| Ambito | Vale per |
|---|---|
| Per singola società | un database SAP |
| Per server | tutte le società dell'istanza SQL Server o SAP HANA |
| Libera | non è legata a un database |

La **prova gratuita** dura 30 giorni ed è libera.

![Licenza](../../_img/rateupdater/06-licenza.png)

*La pagina Licenza: stato, scadenza, ambito e campo per il codice.*

![Impostazioni › Licenza](../../_img/rateupdater/06b-impostazioni-licenza.png)

*Impostazioni › Licenza: i tre ambiti della licenza.*

Menu **Licenza**: stato, scadenza e ambito della licenza. Il codice ricevuto da XEI si incolla in **Inserisci un codice
di licenza** e vale subito, senza riavviare. Per una licenza per società o per server il programma deve essere collegato,
in sola lettura, al database della licenza (*Impostazioni › Licenza*, **Prova il collegamento**): i codici della società e del server da
mandare a XEI compaiono lì e nella pagina Licenza.

Per le licenze: [license@xeisrl.com](mailto:license@xeisrl.com).

## 10. Domande frequenti e problemi

| Cosa vedi | Perché | Cosa fare |
|---|---|---|
| Una valuta è *non gestita* | La società SAP non usa quella valuta | Niente: si scrivono solo le valute della società |
| Una valuta della società non si aggiorna | In SAP la valuta non ha il codice ISO come codice | Usa in SAP il codice ISO (per esempio `USD`) |
| L'esecuzione si ferma subito con un errore sulla valuta locale | La fonte non quota la valuta locale, oppure in SAP ha un codice non ISO | Indica il codice ISO in *Impostazioni › Cambi* o scegli un'altra fonte |
| L'esito di una valuta è un errore di SAP | SAP ha rifiutato il cambio (per esempio per le autorizzazioni dell'utente) | Leggi l'errore; controlla le autorizzazioni SAP dell'utente sui cambi |
| L'aggiornamento automatico non parte | È spento, oppure manca l'utente SAP tecnico | Accendilo in *Impostazioni › Cambi* e imposta l'utente tecnico in *Impostazioni › SAP* |
| Il programma chiede di installare WebView2 | Manca Microsoft Edge WebView2 Runtime | Accetta il download proposto, oppure installalo dal sito di Microsoft |

## 11. Assistenza

Per le licenze: [license@xeisrl.com](mailto:license@xeisrl.com). Per l'assistenza:
[info@xeisrl.com](mailto:info@xeisrl.com). Nella richiesta indica la versione del programma (menu *Informazioni*) e una
descrizione del problema.
