---
title: XEI Rate Updater per SAP Business One – Installazione, primo avvio, licenza e aggiornamento pianificato
description: Come installare XEI Rate Updater per SAP Business One, collegarlo a SAP Business One, attivare la licenza e pianificare l'aggiornamento giornaliero dei cambi.
lang: it
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater per SAP Business One – Installazione, primo avvio, licenza e aggiornamento pianificato

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive, con il Service Layer |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Sistema | Windows 10 e 11, Windows Server 2016 e successivi, a 64 bit; Microsoft Edge WebView2 Runtime |
| Rete | accesso a internet verso la fonte dei tassi scelta |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |

## Installazione

1. Scarica lo zip del programma dalla pagina di download.
2. Estrai la cartella dello zip sul PC, per esempio in `C:\XEI\RateUpdater`.
3. Avvia **XEI.RateUpdater.exe**. Il programma contiene già .NET. Serve **Microsoft Edge WebView2 Runtime**, che di
   solito c'è già: se manca, il programma lo dice e propone di scaricarlo.

Il programma non ha un'installazione. Impostazioni e storico stanno nella cartella dei dati di Windows comune a tutti gli
utenti del PC. Per aggiornare il programma si sostituisce la cartella con quella nuova: impostazioni e storico restano.

## Primo avvio

Alla prima apertura si apre la pagina **Primo avvio**, con il codice del primo avvio già scritto.

1. **Collegamento a SAP**: *Indirizzo del Service Layer* e *Società SAP*; poi **Prova la connessione**.
2. **Accesso e primo amministratore**:
   - *Accesso degli operatori*: **Utente SAP di ognuno** oppure **Utenti propri e utente SAP tecnico**;
   - *Utente SAP del primo amministratore* (per esempio `manager`);
   - *Utente SAP tecnico* e password: servono per l'aggiornamento automatico. Meglio un utente dedicato, con il solo
     permesso di scrivere i cambi.
3. **Salva e riavvia**.

Dopo, le stesse impostazioni sono in **Impostazioni › SAP**. La fonte dei tassi e l'aggiornamento automatico sono in
**Impostazioni › Cambi**.

## Licenza

Il programma funziona con un **codice di licenza** rilasciato da XEI.

| Ambito | Vale per |
|---|---|
| Per singola società | un database SAP |
| Per server | tutte le società dell'istanza SQL Server o SAP HANA |
| Libera | non è legata a un database |

- **Prova**: 30 giorni, libera.
- Menu **Licenza**: stato, scadenza e ambito. Il codice ricevuto da XEI si incolla in **Inserisci un codice di
  licenza** e vale subito, senza riavviare.
- Per una licenza per società o per server il programma deve essere collegato, in sola lettura, al database della
  licenza (*Impostazioni › Licenza*, **Prova il collegamento**): lì e nella pagina Licenza compaiono i codici della
  società e del server, da mandare a [license@xeisrl.com](mailto:license@xeisrl.com).

## Aggiornamento pianificato con Windows

Così i cambi si aggiornano ogni giorno anche con il programma chiuso.

1. Imposta l'**utente SAP tecnico** (Impostazioni › SAP).
2. In Windows apri **Utilità di pianificazione** e crea un'attività di base, per esempio ogni giorno alle 7:00.
3. Azione **Avvia programma**: `XEI.RateUpdater.exe` nella cartella del programma, con l'argomento `aggiorna`.
4. Nelle proprietà dell'attività scegli **Esegui indipendentemente dalla connessione dell'utente**.

Il comando aggiorna i cambi di oggi e si chiude senza finestra; l'esecuzione compare nello **Storico**. Con più
società si aggiunge `--societa <database SAP>`, un'attività per ogni società. Risultato per l'Utilità di
pianificazione: **0** riuscito, **1** non riuscito o con una valuta rifiutata, **2** argomenti sbagliati.

In alternativa, con il programma aperto, basta accendere **Aggiornamento automatico** in *Impostazioni › Cambi*.

## Assistenza

Per le licenze: [license@xeisrl.com](mailto:license@xeisrl.com). Per l'assistenza:
[info@xeisrl.com](mailto:info@xeisrl.com). Nella richiesta indica la versione del programma (menu *Informazioni*) e una
descrizione del problema.
