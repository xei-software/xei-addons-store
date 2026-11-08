---
title: XEI.ContoLavoro – Conto lavoro presso terzisti
description: Gestisce in SAP Business One le lavorazioni affidate ai terzisti, dall'ordine e l'invio dei componenti fino al rientro del prodotto finito.
lang: it
prodotto: XEI.ContoLavoro
versione: 1.2.1
stato: approvato
---

# XEI.ContoLavoro

**Il conto lavoro presso i terzisti in SAP Business One.** Una commessa per ogni lavorazione tiene insieme l'ordine al
terzista, i componenti inviati, i rientri e il versamento del prodotto finito, con la situazione sempre aggiornata.

## Descrizione

Seguire il conto lavoro a mano vuol dire tenere allineati ordini d'acquisto, trasferimenti e carichi, e sapere in ogni
momento cosa c'è presso ogni terzista. Con XEI.ContoLavoro lo fa SAP Business One:

- per ogni lavorazione si apre una **commessa terzista** con i prodotti da ottenere e la loro distinta base: componenti
  da inviare e lavorazioni da pagare;
- l'**ordine d'acquisto al terzista** nasce dalla commessa e resta allineato a ogni modifica;
- i **componenti** si inviano al magazzino del terzista, con rientri e scarti;
- il **versamento** registra in una sola operazione l'entrata del prodotto e delle lavorazioni e l'uscita dei componenti
  consumati;
- la commessa mostra in ogni momento cosa è stato spedito, cosa è stato usato, cosa resta presso il terzista e cosa
  manca, e si chiude da sola quando è finita.

## Funzioni principali

- **Commessa terzista** con cartelle Prodotti, Distinta base, Componenti e Documenti: tutti i documenti SAP collegati,
  raggruppati e apribili.
- **Conto lavoro da ordini di produzione**: le fasi esterne di un ordine di produzione diventano commesse, i componenti
  si prelevano a ogni rientro e il prodotto finito entra in magazzino quando sono rientrate tutte le lavorazioni.
- **Lotti e numeri di serie** proposti dai lotti della commessa presso il terzista e per scadenza, modificabili a mano;
  lotto del prodotto in entrata calcolato da uno script configurabile.
- **Costi** dei prodotti ricalcolati a ogni salvataggio, con i **prezzi delle lavorazioni** per terzista e prodotto.
- **Trasferimento massivo** dei componenti, **trasferimento tra commesse** presso lo stesso terzista e **chiusura
  massiva** delle entrate merci.

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |
| Sistema | Microsoft .NET Framework 4.8 sul PC del client SAP |
| Installazione | Extension Manager di SAP Business One |
| Licenza | codice di licenza XEI, da inserire nel menu **Licenza** (prova gratuita 30 giorni) |

## Versione attuale

**1.2.1** – vedi le [note di rilascio](../../manuali/it/contolavoro/note-rilascio-1.2.1.md) e il manuale d'uso.
