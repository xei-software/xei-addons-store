---
title: XEI.CommissionManagement – Provvigioni agenti
description: Calcola e liquida in SAP Business One le provvigioni di agenti, capi zona, capi area e direttori, dalle regole fino all'estratto per agente.
lang: it
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement

**Provvigioni degli agenti di vendita in SAP Business One.** Le percentuali arrivano da sole sulle righe dei
documenti, l'add-on calcola le provvigioni, le liquida man mano che i clienti pagano e prepara l'estratto di ogni
agente.

## Descrizione

Calcolare le provvigioni a mano o su fogli di calcolo vuol dire riprendere ogni mese fatture, incassi e accordi con
gli agenti, con il rischio di errori e di estratti diversi da quello che dice il gestionale.

Con XEI.CommissionManagement tutto resta in SAP Business One:

- ogni riga di fattura porta fino a **quattro percentuali**: agente, capo zona, capo area e direttore;
- le percentuali vengono dalle **regole** per cliente, gruppo clienti, articolo, gruppo articoli, listino, periodo e
  sconto, oppure dalle percentuali predefinite dell'agente, e si possono correggere a mano;
- la provvigione si divide in una quota **al fatturato** e in quote **all'incasso**, rata per rata o sul totale del
  documento;
- la **liquidazione** propone le quote incassate e storna quelle delle rate tornate insolute;
- l'**estratto** di ogni agente si esporta in CSV, si stampa in PDF o si invia per email.

## Funzioni principali

- **Agenti e gerarchia**: ruolo, capo zona, capo area, direttore, percentuali predefinite, parte al fatturato e tipo
  di liquidazione per ogni addetto alle vendite.
- **Regole percentuali** con ordine di ricerca configurabile, sconto minimo e periodo di validità, esportabili e
  importabili in CSV.
- **Percentuali sui documenti di vendita** mentre si compilano, con stima della provvigione al salvataggio e righe
  corrette a mano protette.
- **Controllo e assegnazione %**: confronta le percentuali dei documenti con le regole e le corregge in blocco.
- **Calcolo** su fatture, fatture d'anticipo e note di credito, anche in automatico alla registrazione della fattura.
- **Liquidazione** delle quote incassate, anche in proporzione agli incassi parziali, con periodo chiuso.
- **Conguagli**, **scaglioni e premi** sul fatturato annuo e **bozze delle fatture** degli agenti.
- **Verifiche** delle anomalie e **autorizzazioni** dedicate in Autorizzazioni generali di SAP.

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |
| Sistema | Microsoft .NET Framework 4.8 sul PC del client SAP |
| Posta | server di posta SMTP raggiungibile, solo per inviare gli estratti agli agenti via email (Configurazione › Email) |
| Installazione | Extension Manager di SAP Business One |
| Licenza | codice di licenza XEI, da inserire nel menu **Licenza** dell'add-on (prova gratuita 30 giorni) |

## Versione attuale

**1.1.1** – vedi le [note di rilascio](../../manuali/it/commissionmanagement/note-rilascio-1.1.1.md) e il
[manuale d'uso](../../manuali/it/commissionmanagement/manuale-utente.md).
