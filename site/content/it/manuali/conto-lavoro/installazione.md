---
title: XEI.ContoLavoro – Installazione, licenza e menu
description: Come installare XEI.ContoLavoro, attivare la licenza e trovare i menu.
lang: it
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Installazione, licenza e menu

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Sistema | Microsoft .NET Framework 4.8 sul PC del client SAP |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |

## Installazione

1. Scaricare il pacchetto `XEI.ContoLavoro.zip`.
2. In SAP Business One aprire l'**Extension Manager**, importare il pacchetto e assegnarlo alla società.
3. Al primo avvio l'add-on crea tabelle, campi, l'oggetto della commessa terzista e la ricerca formattata del fornitore
   terzista sul magazzino. SAP mostra il messaggio *"La struttura del database è stata modificata..."*: rispondere
   **Sì** e attendere la fine prima di usare il client.

Ogni aggiornamento dell'add-on si installa allo stesso modo.

Dopo l'installazione: compilare la **Configurazione**, poi in SAP collegare a ogni magazzino del terzista il suo
fornitore (campo *Fornitore terzista* dell'anagrafica del magazzino) e segnare gli articoli in conto lavoro (manuale
d'uso, capitoli 3 e 6).

## Licenza

L'add-on funziona con un **codice di licenza** rilasciato da XEI.

- **Prova**: dopo la richiesta della prova si riceve via email un **codice di prova**, valido 30 giorni dall'invio in
  qualsiasi società.
- **Acquisto**: si inviano a XEI i due codici della finestra **Licenza** e si riceve il codice di licenza.

La finestra Licenza:

- Senza un codice valido l'add-on è **bloccato**: nel suo menu restano solo *Informazioni* e *Licenza*, e all'avvio
  si apre da sola la finestra **Licenza** con lo stato e il motivo.
- La finestra mostra il **codice della società** e il **codice del server**: per acquistare la licenza, con *Copia*
  si inviano a [license@xeisrl.com](mailto:license@xeisrl.com).
- Un utente SAP **superutente** incolla il codice ricevuto in *Inserisci un codice di licenza* e preme *Salva
  codice*: l'add-on si sblocca subito, senza riavviare SAP.
- Il codice di prova vale in qualsiasi società. Il codice di licenza vale per la società (database) o per il server
  dei codici inviati.
- La stessa finestra si apre in ogni momento dal menu *Licenza*: stato, scadenza, numero e ambito della licenza.

## Menu

Le voci sono in **XEI-Addon › Conto lavoro**. Il sottomenu **Conto lavoro** compare anche nel modulo di SAP scelto in
Configurazione (*Acquisti - Fornitori* oppure *Produzione*).

| Voce | Funzione |
|---|---|
| Commessa terzista | apertura, ricerca e creazione delle commesse (manuale d'uso, capitoli 4 e 5) |
| Crea commesse da ordini di produzione | commesse dalle lavorazioni esterne degli ordini di produzione (capitolo 6) |
| Ricevimento dal terzista | versamento dei prodotti di un DDT del terzista su più commesse (carico dei prodotti e scarico dei componenti) |
| Trasferimento massivo componenti | invio dei componenti per più commesse, se attivo in Configurazione (capitolo 9) |
| Trasferimento componenti tra commesse | sposta la giacenza già presso il terzista da una commessa a un'altra (capitolo 9) |
| Chiusura massiva entrate merci prodotti | chiude le entrate merci dei prodotti rimaste aperte (capitolo 9) |
| Prezzi lavorazioni terzisti | prezzi delle lavorazioni per terzista e prodotto (capitolo 9) |
| Configurazione | opzioni dell'add-on (capitolo 3) |
| Informazioni, Traduzioni, Licenza | voci comuni agli add-on XEI; Licenza: stato e codice di licenza |
