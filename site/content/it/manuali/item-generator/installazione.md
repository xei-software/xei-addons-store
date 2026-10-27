---
title: XEI.ItemGenerator – Installazione, licenza, menu e autorizzazioni
description: Come installare XEI.ItemGenerator, attivare la licenza, trovare i menu e assegnare le autorizzazioni.
lang: it
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Installazione, licenza, menu e autorizzazioni

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Sistema | Microsoft .NET Framework 4.8 sul PC del client SAP |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo |

## Installazione

1. Scaricare il pacchetto `XEI.ItemGenerator.zip`.
2. In SAP Business One aprire l'**Extension Manager**, importare il pacchetto e assegnarlo alla
   società.
3. Al primo avvio l'add-on crea da solo tabelle, campi, oggetti e le voci delle autorizzazioni.
4. Al termine **riavviare il client SAP una volta**: le finestre delle basi e delle varianti
   leggono i campi dell'add-on all'avvio di SAP.

Ogni aggiornamento dell'add-on si installa allo stesso modo, con lo stesso riavvio.

## Licenza

L'add-on funziona con un **codice di licenza** rilasciato da XEI.

- **Prova**: dopo la richiesta della prova si riceve via email un **codice di prova**, valido 30 giorni
  dall'invio in qualsiasi società.
- **Acquisto**: si inviano a XEI i due codici della finestra **Licenza** e si riceve il codice di
  licenza.

La finestra Licenza:

- Senza un codice valido l'add-on è **bloccato**: nel suo menu restano solo *Informazioni* e
  *Licenza*, e all'avvio si apre da sola la finestra **Licenza** con lo stato e il motivo.
- La finestra mostra il **codice della società** e il **codice del server**: per acquistare la
  licenza, con *Copia* si inviano a [license@xeisrl.com](mailto:license@xeisrl.com).
- Un utente SAP **superuser** incolla il codice ricevuto in *Inserisci un codice di licenza* e preme
  *Salva codice*: l'add-on si sblocca subito, senza riavviare SAP.
- Il codice di prova vale in qualsiasi società. Il codice di licenza vale per la società (database)
  o per il server dei codici inviati.
- La stessa finestra si apre in ogni momento dal menu *Licenza*: stato, scadenza, numero e ambito
  della licenza.

![La finestra Licenza con l'add-on bloccato](../../_img/itemgenerator/27_licenza.png)

*La finestra Licenza con l'add-on bloccato: motivo, codici della società e del server, campo per il
codice.*

## Menu

Le voci sono in **Moduli › Amministrazione › Add-ons › XEI-Addon › Configuratore codici** e, uguali,
in **Magazzini e Logistica › Gestione articoli › Configuratore codici**.

| Voce | Funzione |
|---|---|
| 0. Configurazione | opzioni dell'add-on (manuale d'uso, capitolo 3) |
| 1. Definizione basi | basi e valori: l'albero del codice (capitolo 5) |
| 2. Definizione varianti e opzioni | varianti con le loro opzioni (capitolo 4) |
| 3. Strutture varianti | gruppi di varianti da chiedere per un valore (capitolo 4) |
| 4. Genera articoli | composizione e creazione degli articoli (capitolo 9) |
| 5. Controllo congruenze | ricalcolo delle composizioni degli articoli generati (capitolo 14) |
| 6. Verifica configurazione | controllo di tutta la configurazione (capitolo 12) |
| 7. Importa / esporta Excel | configurazione in un file Excel (capitolo 13) |
| Informazioni, Traduzioni, Licenza | voci comuni agli add-on XEI (solo sotto XEI-Addon); Licenza: stato e codice di licenza |

Con il tasto destro ci sono anche **Configura articolo...** sulle righe di offerte e ordini cliente
(capitolo 10) e **Genera articoli simili...** nell'anagrafica di un articolo generato (capitolo 11).

## Autorizzazioni

In **Gestione › Inizializzazione sistema › Autorizzazioni › Autorizzazioni generali** l'add-on
aggiunge il ramo **Configuratore codici XEI**. Per ogni voce si può assegnare *Autorizzazione
completa*, *Sola lettura* o *Nessuna autorizzazione*. I superuser hanno sempre accesso completo.

![Il ramo del configuratore nelle autorizzazioni generali](../../_img/itemgenerator/23_autorizzazioni.png)

*Il ramo del configuratore nelle autorizzazioni generali, per un utente senza autorizzazioni.*

| Voce | Completa | Sola lettura |
|---|---|---|
| Definizione basi | modificare le basi | consultare |
| Definizione varianti | modificare le varianti | consultare |
| Strutture varianti | modificare le strutture | consultare |
| Generazione articoli | creare articoli (anche da offerte e ordini) | comporre l'elenco senza creare |
| Configurazione, verifica, import/export | salvare la configurazione, importare da Excel, controllo congruenze | vedere la configurazione, verificare, esportare |

Senza autorizzazione la voce di menu mostra nella barra di stato "Funzione non autorizzata".

## Assistenza

Per le licenze: [license@xeisrl.com](mailto:license@xeisrl.com). Per l'assistenza:
[info@xeisrl.com](mailto:info@xeisrl.com). Nella richiesta indicare la versione dell'add-on (menu
*Informazioni*) e una descrizione del problema.
