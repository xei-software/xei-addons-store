---
title: XEI Rate Updater per SAP Business One – Cambi delle valute
description: Aggiorna ogni giorno i cambi delle valute in SAP Business One con i tassi ufficiali della BCE, della Banca d'Italia o di Open Exchange Rates.
lang: it
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater per SAP Business One

**I cambi delle valute in SAP Business One, aggiornati da soli.** Ogni giorno il programma prende i tassi da una fonte
ufficiale e li scrive in SAP Business One, nel verso e con i decimali che SAP usa.

## Descrizione

Aggiornare i cambi a mano vuol dire copiare ogni mattina i tassi da un sito nella tabella dei cambi di SAP, valuta per
valuta, con il rischio di dimenticare un giorno o di invertire un tasso.

XEI Rate Updater per SAP Business One lo fa al posto tuo:

- prende i tassi dalla **Banca centrale europea**, dalla **Banca d'Italia** oppure da **Open Exchange Rates**;
- per i cambi di un giorno usa i tassi pubblicati **il giorno prima**; nei fine settimana e nei festivi usa l'ultimo
  giorno pubblicato;
- scrive in SAP solo le **valute gestite dalla società**, nel verso che la società usa (tasso diretto o indiretto),
  troncate a sei decimali;
- con una **valuta locale diversa dall'euro** calcola i tassi incrociati rispetto a quella;
- si usa **a mano**, scegliendo la data, oppure **ogni giorno in automatico**;
- tiene lo **storico** di ogni aggiornamento: chi l'ha fatto, la fonte, i tassi e l'esito di ogni valuta.

## Funzioni principali

- **Cambi**: data dei cambi, fonte e pulsante *Aggiorna i cambi in SAP*; l'esito mostra per ogni valuta tasso diretto,
  tasso indiretto e se è stata scritta in SAP.
- **Storico**: le esecuzioni della società, dalla più recente; ogni riga si apre sulle valute.
- **Aggiornamento automatico**: ogni giorno all'ora scelta, oppure dall'Utilità di pianificazione di Windows.
- **Errori sotto controllo**: un errore su una valuta non ferma le altre; ogni esecuzione dice cosa è andato storto.
- **Accesso con l'utente SAP** di ognuno, con le sue autorizzazioni sui cambi; l'amministratore assegna a ogni utente le funzioni *Aggiornamento cambi* e *Storico*.

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive, con il Service Layer |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Sistema | Windows 10 e 11, Windows Server 2016 e successivi, a 64 bit; Microsoft Edge WebView2 Runtime |
| Rete | accesso a internet verso la fonte dei tassi scelta (BCE, Banca d'Italia oppure Open Exchange Rates con la sua chiave API) |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |
| Installazione | si estrae la cartella del programma, senza installazione; .NET è già incluso |
| Licenza | codice di licenza XEI, libera, per server o per società (prova gratuita 30 giorni) |

## Versione attuale

**1.0.0** – vedi le [note di rilascio](../../manuali/it/rateupdater/note-rilascio-1.0.0.md) e il
[manuale d'uso](../../manuali/it/rateupdater/manuale-utente.md).
