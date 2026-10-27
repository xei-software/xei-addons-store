---
title: XEI.CommissionManagement – Installazione, licenza, menu e autorizzazioni
description: Come installare XEI.CommissionManagement, attivare la licenza, trovare i menu e assegnare le autorizzazioni.
lang: it
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement – Installazione, licenza, menu e autorizzazioni

## Requisiti

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Sistema | Microsoft .NET Framework 4.8 sul PC del client SAP |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |
| Posta | server di posta SMTP raggiungibile, solo per inviare gli estratti agli agenti via email (Configurazione › Email) |

## Installazione

1. Scaricare il pacchetto `XEI.CommissionManagement.zip`.
2. In SAP Business One aprire l'**Extension Manager**, importare il pacchetto e assegnarlo alla società.
3. Al primo avvio l'add-on crea campi, tabelle, indici e autorizzazioni. La creazione dei campi sulle righe dei
   documenti richiede **qualche minuto**: SAP mostra più volte il messaggio *"La struttura del database è stata
   modificata... verranno chiuse tutte le finestre aperte. Continuare?"*: rispondere **Sì**.

Ogni aggiornamento dell'add-on si installa allo stesso modo.

Dopo l'installazione: compilare la **Configurazione**, poi gli **Agenti** (ruoli, superiori, percentuali), poi le
**Regole**. Solo da quel momento i documenti ricevono le percentuali. Agli utenti che non sono superutenti vanno date
le **autorizzazioni** (più sotto).

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

Le voci sono in **XEI-Addon › Provvigioni**.

| Voce | Funzione |
|---|---|
| Configurazione | opzioni (sei schede) e ordine di ricerca delle regole (manuale d'uso, capitolo 5) |
| Agenti | ruolo, superiori, % predefinite, % al fatturato, liquidazione, fornitore, utente SAP (capitolo 6) |
| Regole percentuali | % per cliente, gruppo clienti, articolo, gruppo articoli, listino (capitolo 7) |
| Scaglioni e premi | premi sul fatturato annuo, se attivi in Configurazione (capitolo 15) |
| Controllo e assegnazione % | confronto tra documenti e regole e correzione in blocco (capitolo 9) |
| Calcolo provvigioni | calcolo su fatture, fatture d'anticipo e note di credito (capitolo 10) |
| Provvigioni calcolate | consultazione, correzione, ricalcolo, eliminazione (capitolo 11) |
| Liquidazione | quote incassate da liquidare, insoluti da stornare (capitolo 12) |
| Conguagli | importi manuali per agente e mese, bozze delle fatture degli agenti (capitolo 13) |
| Estratto provvigioni | calcolate, da liquidare, liquidate e conguagli; CSV, stampa/PDF, email (capitolo 14) |
| Verifiche | anomalie da controllare (capitolo 16) |
| Informazioni, Traduzioni, Licenza | voci comuni agli add-on XEI; Licenza: stato e codice di licenza |

## Autorizzazioni

Nelle **Autorizzazioni generali** di SAP (Amministrazione › Inizializzazione sistema › Autorizzazioni) l'add-on crea
la voce **Provvigioni** sotto *Autorizzazione utente*, con cinque sottovoci. I superutenti hanno sempre tutto; agli
altri utenti si assegna per ogni voce *Senza autorizzazione*, *Solo accesso di lettura* o *Autorizzazione completa*.

![Autorizzazioni generali](../../_img/commissionmanagement/autorizzazioni.png)

*Autorizzazioni generali: la voce Provvigioni con le cinque sottovoci, per un utente senza autorizzazioni.*

| Autorizzazione | Sola lettura | Completa |
|---|---|---|
| Configurazione | – | aprire e salvare la Configurazione |
| Agenti, regole e scaglioni | consultare | salvare agenti, regole e scaglioni |
| Controllo, calcolo e verifiche | consultare Controllo, Calcolo, Provvigioni calcolate, Verifiche | applicare le %, calcolare, ricalcolare, salvare quote, eliminare |
| Liquidazione, conguagli e bozze fatture | consultare Liquidazione e Conguagli | confermare liquidazioni, salvare conguagli, registrare premi, generare bozze |
| Estratto di tutti gli agenti | vedere l'estratto di tutti gli agenti (senza: solo i propri) | anche l'invio email |

Senza autorizzazione la voce di menu risponde nella barra di stato *"Funzione non consentita: serve l'autorizzazione
«…» (Autorizzazioni generali > Provvigioni)"*; con la sola lettura la finestra si apre, ma i pulsanti che modificano
rispondono *"Operazione non consentita: serve l'autorizzazione completa su «…»"*.

## Assistenza

Per le licenze: [license@xeisrl.com](mailto:license@xeisrl.com). Per l'assistenza:
[info@xeisrl.com](mailto:info@xeisrl.com). Nella richiesta indicare la versione dell'add-on (menu *Informazioni*) e
una descrizione del problema.
