---
title: XEI.ItemGenerator – Configuratore di codici articolo
description: Crea in SAP Business One articoli con codice, descrizioni, dati, prezzo e distinta base composti da regole che definisci tu.
lang: it
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator

**Configuratore di codici articolo per SAP Business One.** Scegli le caratteristiche
del prodotto e l'add-on crea l'articolo in anagrafica con codice, descrizioni, dati,
prezzo e distinta base già compilati.

## Descrizione

Chi vende prodotti in molte combinazioni (misure, finiture, colori, accessori)
perde tempo a creare a mano un articolo per ogni combinazione e rischia codici e
descrizioni diversi per lo stesso prodotto.

Con XEI.ItemGenerator definisci una volta le regole e l'add-on compone gli articoli:

- il **codice** nasce dai valori scelti livello per livello (per esempio
  `PE` Pensile → `MU` a muro → `070` altezza 70 cm = `PEMU070`), più un progressivo
  che distingue le varianti;
- le **varianti** (per esempio colore o finitura) hanno le loro opzioni, che possono
  essere ereditate dai livelli precedenti;
- **descrizioni, gruppi, unità di misura, proprietà, misure, peso e prezzo**
  dell'articolo si ricavano dai valori e dalle opzioni scelte;
- la **distinta base** si compone con i componenti di ogni valore e opzione.

Se una combinazione esiste già, l'add-on trova l'articolo esistente invece di
crearne un doppione.

## Funzioni principali

- **Definizione di basi, varianti e strutture** con le anagrafiche dell'add-on in SAP.
- **Generazione degli articoli** in una finestra ridimensionabile, con gli alberi dei
  codici e delle varianti; SAP resta utilizzabile mentre la finestra è aperta.
- **Configura articolo da offerte e ordini cliente**: dal tasto destro sulla riga del
  documento si compone l'articolo e lo si inserisce nella riga.
- **Genera articoli simili** dall'anagrafica di un articolo già generato: basta
  cambiare un'opzione.
- **Formula della descrizione** per comporre descrizione, descrizione estesa e nome
  straniero.
- **Verifica della configurazione**, con l'elenco degli errori e l'apertura diretta
  del dato da correggere.
- **Importazione ed esportazione Excel** della configurazione, anche per copiarla in
  un'altra società.
- **Autorizzazioni** dedicate in Autorizzazioni generali di SAP.
- **Miniatura dell'immagine** dell'articolo nell'anagrafica articoli.

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server (SAP HANA non ancora supportato) |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo |
| Sistema | Microsoft .NET Framework 4.8 sul PC del client SAP |
| Installazione | Extension Manager di SAP Business One |
| Licenza | codice di licenza XEI, da inserire nel menu **Licenza** dell'add-on (prova gratuita 30 giorni) |

## Versione attuale

**1.4.0** – vedi le [note di rilascio](../../manuali/it/itemgenerator/note-rilascio-1.4.0.md).
