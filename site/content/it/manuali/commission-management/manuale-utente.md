---
title: XEI.CommissionManagement – Manuale d'uso
description: Provvigioni degli agenti di vendita in SAP Business One: configurazione, regole, calcolo, liquidazione, conguagli ed estratti.
lang: it
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Manuale d'uso

| | |
|---|---|
| SAP Business One | 10.0 o successive |
| Database | Microsoft SQL Server o SAP HANA (su SAP HANA si consiglia una prova durante l'installazione) |
| Lingue del programma | italiano, inglese, tedesco, francese, spagnolo, turco |

## 1. Cosa fa l'add-on

XEI.CommissionManagement calcola e liquida le **provvigioni degli agenti di vendita** partendo dai documenti di
SAP Business One. Ogni riga di fattura (e di fattura d'anticipo o nota di credito) porta con sé fino a quattro
percentuali: una per l'**agente** del documento e una per ciascuno dei suoi superiori, **capo zona**, **capo
area** e **direttore**. L'add-on:

- **assegna le percentuali** alle righe mentre si compilano i documenti, in base a regole per cliente, gruppo
  clienti, articolo, gruppo articoli, listino, periodo e sconto (oppure alle percentuali predefinite dell'agente);
- **calcola** le provvigioni dei documenti di un periodo e le divide in **quote**: una parte matura alla
  fattura, il resto all'incasso (rata per rata o quando tutto il documento è incassato);
- **liquida** le quote man mano che SAP registra gli incassi, e **storna** quelle di rate che tornano insolute;
- produce per ogni agente l'**estratto** di quanto è stato calcolato, di quanto resta da liquidare e di quanto
  gli spetta nel periodo (liquidato più **conguagli** manuali), esportabile in CSV per Excel, stampabile in PDF e
  inviabile via email a ogni agente;
- a scelta (opzioni in Configurazione): stima la provvigione quando si salva un documento, calcola da solo le
  fatture appena registrate, protegge le percentuali corrette a mano, liquida gli incassi parziali, chiude i periodi
  già consegnati, calcola i **premi** sul fatturato annuo, prepara le **bozze delle fatture** degli agenti e
  segnala le anomalie (**Verifiche**).

Tutto sta in SAP: campi utente sugli addetti alle vendite e sulle righe dei documenti, tabelle utente per regole,
provvigioni e conguagli, nessun database esterno. Funziona allo stesso modo su Microsoft SQL Server e SAP HANA; su SAP HANA si consiglia una prova durante l'installazione.

## 2. I concetti: beneficiari, percentuali, quote, liquidazione

### Chi riceve la provvigione (beneficiari)

L'**addetto alle vendite** del documento è l'agente. In anagrafica Agenti gli si possono indicare un **capo
zona**, un **capo area** e un **direttore**: sono gli altri beneficiari dei suoi documenti. Ognuno ha la propria
percentuale su ogni riga (le quattro colonne *Provv. % agente / capo zona / capo area / direttore*).

- Un addetto riceve provvigioni solo se ha un **ruolo** (Agente, Capo zona, Capo area, Direttore). Un addetto senza
  ruolo non è "gestito": i suoi documenti non generano provvigioni e, se è indicato come superiore di qualcuno, la
  sua quota non viene calcolata.
- Il ruolo "Agente" vale per chi compare come addetto sui documenti; "Capo zona", "Capo area" e "Direttore" sono i
  titoli con cui un addetto può essere scelto come superiore. Chi ha un ruolo di superiore può comunque avere
  documenti propri: su quelli è l'agente.

### Le percentuali

Le percentuali di una riga vengono dalle **regole** (capitolo 7) o, se nessuna regola si applica, dalle
**percentuali predefinite** dell'agente del documento (capitolo 6). Si assegnano da sole mentre si compila il
documento (capitolo 8), si possono correggere a mano e si possono controllare e sistemare in blocco prima del calcolo
(capitolo 9).

### Le quote: al fatturato e all'incasso

La provvigione di un documento non è dovuta tutta subito. Per ogni beneficiario l'add-on la divide in quote:

- la quota **al fatturato** (rata 0), pari alla "% al fatturato" dell'addetto, matura alla data di registrazione del
  documento;
- il resto matura **all'incasso**: con la liquidazione **a rate** una quota per ogni rata del documento, in
  proporzione alla rata, liquidabile quando quella rata è incassata; con la liquidazione **sul totale** una quota
  sola (rata -1), liquidabile quando tutte le rate sono incassate.

Esempio: fattura da 1.350 di imponibile con 5% di provvigione = 63,00; agente con 30% al fatturato e liquidazione a
rate, documento in due rate al 50%: quota 0 = 18,90 alla registrazione, rata 1 = 22,05 e rata 2 = 22,05 alle rispettive
scadenze.

### La liquidazione

Liquidare una quota significa riconoscerla all'agente con una data di liquidazione. L'add-on propone le quote da
liquidare leggendo gli incassi di SAP (pagamenti, effetti, riconciliazioni, note di credito) e propone lo **storno**
delle quote già liquidate le cui rate non risultano più saldate (insoluti). Una quota **consolidata** è definitiva:
non si storna e la provvigione non si ricalcola più.

## 3. Installazione e primo avvio

- Pacchetto per l'Extension Manager: `XEI.CommissionManagement.zip`, dalla pagina di download del sito
  XEI. In SAP Business One si apre l'**Extension Manager**, si importa il pacchetto e lo si assegna alla società.
- Al primo avvio l'add-on crea campi, tabelle, indici e autorizzazioni. La creazione dei campi sulle righe dei documenti richiede **qualche
  minuto**: SAP mostra più volte il messaggio *"La struttura del database è stata modificata... verranno chiuse
  tutte le finestre aperte. Continuare?"* — rispondere **Sì**.
- Il menu è in **XEI-Addon › Provvigioni**:

    Provvigioni
      Configurazione                    opzioni (sei schede) e ordine di ricerca delle regole
      Agenti                            ruolo, superiori, % predefinite, % al fatturato, liquidazione, fornitore, utente SAP
      Regole percentuali                % per cliente / gruppo / articolo / gruppo articoli / listino
      Scaglioni e premi                 premi sul fatturato annuo (se attivi in Configurazione)
      Controllo e assegnazione %        confronto documenti / regole e correzione in blocco
      Calcolo provvigioni               calcolo su fatture, anticipi e note di credito
      Provvigioni calcolate             consultazione, correzione, ricalcolo, eliminazione
      Liquidazione                      quote incassate da liquidare, insoluti da stornare
      Conguagli                         importi manuali per agente e mese, bozze fatture agenti
      Estratto provvigioni              calcolate, da liquidare, liquidate + conguagli; CSV, stampa/PDF, email
      Verifiche                         anomalie da controllare
      Informazioni, Traduzioni, Licenza (voci comuni degli add-on XEI)

> Dopo l'installazione: compilare la **Configurazione**, poi gli **Agenti** (ruoli, superiori,
> percentuali), poi le **Regole**. Solo da quel momento i documenti ricevono le percentuali. Agli utenti non
> superutenti vanno date le **autorizzazioni** (capitolo 17).

### Licenza

L'add-on funziona con un **codice di licenza** rilasciato da XEI.

- **Prova**: dopo la richiesta della prova sul sito si riceve via email un **codice di prova**, valido 30
  giorni dall'invio in qualsiasi società.
- **Acquisto**: si mandano a XEI i due codici della finestra **Licenza** (codice della società e codice del
  server, con *Copia*) e si riceve il codice di licenza, che vale per la società o per il server di quei codici.
- Senza un codice valido l'add-on è **bloccato**: nel suo menu restano *Informazioni* e *Licenza*, e
  all'avvio si apre da sola la finestra **Licenza** con lo stato e il motivo.
- Un utente SAP **superutente** incolla il codice in *Inserisci un codice di licenza* e preme *Salva
  codice*: l'add-on si sblocca subito, senza riavviare SAP.

### Lingue

L'add-on usa la lingua del client SAP (in SAP: Utenti - Configurazione \> Visualizzare \> Lingua): italiano,
inglese, tedesco, francese, spagnolo o turco; con le altre lingue resta in italiano. Al cambio di lingua SAP chiude le
finestre aperte e l'add-on si riavvia da solo. I singoli testi si possono adattare da **Provvigioni \>
Traduzioni**. Restano in italiano in tutte le lingue i testi che SAP salva una sola volta nel database: i nomi
delle autorizzazioni (Autorizzazioni generali \> Provvigioni) e i titoli dei campi aggiunti a documenti e addetti
(es. "Provv. % manuali", "% agente"); i messaggi li citano con questi nomi, così si ritrovano in SAP.

## 4. Il lavoro di ogni mese, in breve

1.  **Durante il mese** i documenti ricevono le percentuali da soli; chi li inserisce può correggerle.
2.  **Controllo e assegnazione %** sulle fatture del mese: si vedono le righe le cui percentuali non corrispondono
    alle regole e si correggono in blocco (facoltativo ma consigliato).
3.  **Calcolo provvigioni** del mese: fatture, fatture d'anticipo, note di credito.
4.  **Provvigioni calcolate**: controllo a campione, correzioni di singole provvigioni.
5.  **Liquidazione** con data limite a fine mese: conferma delle quote incassate e degli eventuali storni.
6.  **Conguagli** del mese (premi, recuperi, rettifiche manuali) e, se attive, le **bozze fatture** degli agenti.
7.  **Estratto provvigioni** "liquidate e conguagli" del mese: è l'importo da riconoscere a ogni agente; CSV per
    Excel, stampa/PDF o email a ogni agente.
8.  Quando gli estratti sono consegnati, **periodo chiuso** fino a fine mese (se si usa l'opzione).

Le **Verifiche** (capitolo 16) si possono lanciare in qualunque momento, prima del calcolo o prima degli
estratti, per trovare documenti non calcolati, agenti cambiati, righe senza percentuali, incassi non liquidati. A fine
anno, **Scaglioni e premi** (capitolo 15) registra i premi sul fatturato come conguagli di dicembre.

## 5. Configurazione

La Configurazione ha sei schede. La scheda **Generale** contiene le opzioni di base e l'ordine delle regole; le
altre (**Documenti**, **Liquidazione**, **Agenti**, **Email**, **Avvisi**) contengono le funzioni
aggiuntive, tutte **spente** all'inizio: ognuna ha sotto di sé una spiegazione e un esempio, e si attiva con la
spunta quando serve. Serve l'autorizzazione "Configurazione" (capitolo 17).

![Configurazione, scheda Generale](../../_img/commissionmanagement/cfg.png)

*Configurazione provvigioni, scheda Generale*

### Scheda Generale

Assegna le percentuali alle righe dei documenti di vendita mentre si compilano  
Attiva l'assegnazione automatica (capitolo 8). Disattivandola le percentuali si scrivono a mano o con il Controllo.

Sconto di riga usato dalle regole  
Lo sconto con cui le regole confrontano il loro "sconto minimo": la *% sconto* della riga oppure un campo
utente percentuale delle righe (ad esempio uno sconto "effettivo" calcolato da un altro add-on).

Prezzi netti  
Per chi vende a prezzo netto senza indicare lo sconto: se la riga non ha sconto, l'add-on calcola lo **sconto
effettivo** come differenza tra il prezzo di listino del cliente e il prezzo della riga (listino 100, prezzo 80 =
sconto 20%), lo scrive nella colonna *Provv. sconto effettivo* e lo usa per le regole.

Percentuali anche sulle righe "solo imposta"  
Di norma le righe "solo imposta" non hanno provvigione (percentuali a zero).

Provvigioni sulle fatture d'anticipo  
Con l'opzione attiva le fatture d'anticipo si calcolano e la loro provvigione viene poi **detratta** dalla
fattura finale che le chiude, così la provvigione complessiva è quella dell'intero importo.

Liquidazione predefinita all'incasso dell'intero documento  
Vale per gli addetti con liquidazione "Da configurazione": sì = una sola quota quando tutto il documento è
incassato; no = una quota per rata.

Note di credito liquidate alla scadenza  
Di norma la provvigione (negativa) di una nota di credito si liquida alla data di registrazione. Con l'opzione
alla scadenza più lontana tra la nota e le fatture a cui si riferisce.

Ordine di ricerca delle regole  
Le 16 combinazioni di campi possibili per una regola, nell'ordine in cui vengono provate. Si cambia il numero nella
colonna *Ordine*: l'ordine 1 viene provato per primo. Vedere il capitolo 7.

### Scheda Documenti

![Configurazione, scheda Documenti](../../_img/commissionmanagement/cfg_documenti.png)

*Scheda Documenti: stima, righe manuali, calcolo automatico*

Mostra la provvigione stimata quando si salva un documento di vendita  
Aggiunto o aggiornato un ordine, un'offerta, una consegna o una fattura, la barra di stato dice quanto maturerà a
ogni beneficiario con le percentuali attuali delle righe. Esempio: *"Provvigioni stimate (Ordine cliente 1250):
Rossi 63,00; Bianchi 9,00 - totale 72,00"*. È solo un'informazione: non viene salvato nulla (capitolo 8).

Proteggi le percentuali modificate a mano sulle righe dei documenti  
Chi corregge una percentuale nella riga la rende "manuale" (colonna *Provv. % manuali*): cambiando cliente o
agente quella riga non viene riassegnata. Esempio: Rossi porta la riga dal 5% al 4% per un accordo col cliente; poi
cambia cliente: le altre righe si riassegnano, questa resta al 4%. Senza l'opzione la riassegnazione sovrascrive
tutte le righe. Togliendo la spunta "manuale" la riga torna automatica.

Calcola le provvigioni appena si registra una fattura, una fattura d'anticipo o una nota di credito  
Il calcolo avviene al salvataggio dal client SAP (con l'ultima scelta fatta sullo sconto di testata nel Calcolo):
così non serve aprire Calcolo provvigioni ogni mese. Esempio: registrata la fattura 1001 di Rossi, la barra di stato
dice *"Provvigioni calcolate (Fattura 1001): Rossi 63,00; Bianchi 9,00"*. I documenti creati da importazioni
o da altri programmi (DI API) non passano dal client: per quelli restano Calcolo provvigioni e le Verifiche.

### Scheda Liquidazione

![Configurazione, scheda Liquidazione](../../_img/commissionmanagement/cfg_liquidazione.png)

*Scheda Liquidazione: incassi parziali e periodo chiuso*

Incassi parziali: liquida la parte di provvigione proporzionale a quanto incassato sulla rata  
Senza l'opzione una quota si liquida solo quando la rata è chiusa del tutto: con acconti o abbuoni la provvigione
resta ferma. Esempio: rata da 500 con quota 22,05; il cliente paga 250 → si liquidano 11,03; al saldo gli altri
11,02. Se un incasso viene annullato si storna solo l'eccesso (capitolo 12).

Periodo chiuso: blocca le provvigioni fino al (data)  
Fino a quella data compresa non si possono ricalcolare o eliminare provvigioni, modificare quote, liquidare o
salvare conguagli. Esempio: consegnati gli estratti di marzo, si mette 31/03: le fatture di marzo non si
ricalcolano più (una fattura mai calcolata si può ancora calcolare). Per correggere qualcosa nel periodo chiuso:
spostare indietro la data (o togliere la spunta), correggere, rimetterla.

### Scheda Agenti

Genera dai conguagli le bozze delle fatture di acquisto degli agenti che hanno un fornitore collegato  
In Conguagli il pulsante **Bozze fatture agenti** crea per ogni agente una bozza di fattura di acquisto (nota
di credito se l'importo è negativo) con una riga di servizio: importo = quote liquidate nel mese + conguagli e
premi del mese. Esempio: Rossi (fornitore F0010), aprile: 22,05 + 50,00 - 20,00 = 52,05. Il **conto della riga**
è obbligatorio (il conto di costo delle provvigioni, es. 7xxxx Provvigioni passive); il **codice IVA** è quello
delle fatture dell'agente (vuoto = quello predefinito del fornitore). Capitolo 13.

Scaglioni di fatturato annuo con premio  
Attiva il menu **Scaglioni e premi**: raggiunta la soglia di imponibile annuo, l'agente riceve un premio (% sul
fatturato dell'anno o importo fisso) registrato come conguaglio. Esempio: scaglioni 100.000 → 0,5% e 200.000 → 1%;
Rossi fattura 150.000 nel 2026: premio 750,00 nel conguaglio di dicembre. Capitolo 15.

Ritenuta indicativa nell'estratto delle liquidate: % e descrizione  
Solo informativa (senza minimali né massimali): nella stampa e nell'email dell'estratto "liquidate e conguagli"
compare una riga "ritenuta" e il netto indicativo. Esempio: 8,5 e "Enasarco quota agente": liquidato 1.000,00 →
ritenuta indicativa -85,00, netto indicativo 915,00. Vuoto o 0 = nessuna riga.

![Configurazione, scheda Agenti](../../_img/commissionmanagement/cfg_agenti.png)

*Scheda Agenti: bozze fatture, scaglioni e ritenuta indicativa (8,5% Enasarco)*

### Scheda Email

![Configurazione, scheda Email](../../_img/commissionmanagement/cfg_email.png)

*Scheda Email: invio dell'estratto agli agenti*

Invio dell'estratto agli agenti via email  
Attiva il pulsante **Invia agli agenti** nell'Estratto provvigioni: ogni agente riceve solo il proprio estratto
(allegato HTML, apribile e stampabile da qualunque browser) all'indirizzo email dell'addetto alle vendite (o del
fornitore collegato). Vanno indicati server SMTP, porta, SSL/TLS, utente e password della casella e il mittente;
esempio: `smtp.office365.com`, porta 587, SSL sì, mittente `provvigioni@azienda.it`. La
password è salvata cifrata.

Prova invio  
Manda un messaggio di prova all'indirizzo indicato usando i valori scritti nella scheda (anche non ancora salvati):
se qualcosa non va, il messaggio d'errore del server compare subito.

### Scheda Avvisi

![Configurazione, scheda Avvisi](../../_img/commissionmanagement/cfg_avvisi.png)

*Scheda Avvisi*

Quota incassata e non liquidata: è un'anomalia dopo (giorni)  
Nelle Verifiche, la ricerca "incassi non liquidati" segnala le quote la cui rata è stata incassata da più di
questi giorni e nessuno ha liquidato. Esempio: 30; rata incassata il 05/04 e oggi 10/05: la quota compare tra le
anomalie finché non la si liquida.

All'avvio dell'add-on segnala nella barra di stato le anomalie rapide  
Controlli veloci a ogni avvio: documenti degli ultimi 90 giorni da calcolare, documenti annullati con provvigioni,
agente cambiato dopo il calcolo. Esempio: *"Provvigioni: 3 anomalie da controllare (Provvigioni \>
Verifiche)"*. Capitolo 16.

> Salvando, la Configurazione controlla che le opzioni attive siano complete: data del periodo chiuso,
> conto esistente e registrabile per le bozze, ritenuta tra 0 e 99,99, server, porta e mittente per l'email.

## 6. Agenti

![Agenti](../../_img/commissionmanagement/agenti.png)

*Agenti: tutti gli addetti alle vendite di SAP, modificabili nella griglia*

La griglia mostra tutti gli addetti alle vendite di SAP. Si compilano le colonne e si preme **Salva**: vengono
salvati solo gli addetti modificati (gli stessi campi si vedono anche nella form standard degli addetti, scheda campi
utente).

| Colonna                                         | Significato                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ruolo                                           | Agente, Capo zona, Capo area, Direttore oppure *(non gestito)*: nessuna provvigione.                                                                                                                                                                                                                                                                                                  |
| Capo zona, Capo area, Direttore                 | I superiori di questo addetto: ricevono la loro percentuale sui suoi documenti. Le tendine mostrano gli addetti che hanno quel ruolo: assegnare prima i ruoli e salvare, poi i superiori. Un superiore già assegnato che ha un altro ruolo, o nessuno, compare come *«nome (ruolo diverso)»*: non riceve provvigioni finché non gli si dà il ruolo (lo segnalano anche le Verifiche). |
| % agente, % capo zona, % capo area, % direttore | Percentuali **predefinite** dei documenti di questo addetto, usate quando nessuna regola si applica alla riga.                                                                                                                                                                                                                                                                        |
| % al fatturato                                  | Parte della provvigione **di questo addetto** (come beneficiario) che matura alla registrazione del documento; il resto matura all'incasso. 100 = tutto al fatturato, 0 = tutto all'incasso.                                                                                                                                                                                          |
| Liquidazione                                    | Per la parte all'incasso: *A rate*, *Sul totale* o *Da configurazione* (segue l'opzione della Configurazione).                                                                                                                                                                                                                                                                        |
| Fornitore                                       | Il fornitore (business partner) con cui l'agente fattura le provvigioni: intestatario delle **bozze fatture** (capitolo 13); la sua email è usata per l'invio dell'estratto se l'addetto non ne ha una.                                                                                                                                                                               |
| Utente SAP                                      | L'utente SAP che corrisponde a questo addetto. Un utente senza l'autorizzazione "Estratto di tutti gli agenti" vede nell'Estratto provvigioni solo sé stesso e gli addetti di cui è capo zona, capo area o direttore (capitolo 17).                                                                                                                                                   |
| Email                                           | L'email dell'addetto alle vendite (anagrafica SAP, sola lettura): destinatario dell'estratto via email.                                                                                                                                                                                                                                                                               |

Controlli al salvataggio: percentuali tra 0 e 100, fornitore e utente SAP esistenti, un addetto non può essere
superiore di se stesso. Esempio usato in questo manuale:

| Addetto | Ruolo         | Capo zona | Capo area | % ag. | % c.zona | % c.area | % al fatt. | Liquidazione      |
|---------|---------------|-----------|-----------|-------|----------|----------|------------|-------------------|
| Rossi   | Agente        | Bianchi   | Neri      | 2     | 0,5      | 0,2      | 30         | A rate            |
| Bianchi | Capo zona     |           |           | 3     |          |          | 0          | Da configurazione |
| Neri    | (non gestito) |           |           |       |          |          |            |                   |
| Verdi   | Agente        |           |           | 1,5   |          |          | 100        | Da configurazione |

Sui documenti di Rossi i beneficiari sono Rossi (agente) e Bianchi (capo zona); Neri, pur indicato come capo area,
non riceve nulla finché non ha un ruolo.

## 7. Regole percentuali

![Regole percentuali](../../_img/commissionmanagement/regole.png)

*Regole percentuali dell'esempio*

Una regola dice: "per le righe con *queste caratteristiche* le percentuali sono queste". Le caratteristiche
possibili sono cliente, gruppo clienti, articolo, gruppo articoli e listino (il listino prezzi del cliente); si
compilano **solo i campi che servono** e l'add-on riconosce da solo la **combinazione** (colonna Combinazione).
Le combinazioni ammesse sono 16:

| Tipo | Combinazione                        | Tipo | Combinazione                               |
|------|-------------------------------------|------|--------------------------------------------|
| 1    | Cliente / Articolo / Listino        | 9    | Gruppo clienti / Gruppo articoli / Listino |
| 2    | Cliente / Articolo                  | 10   | Gruppo clienti / Gruppo articoli           |
| 3    | Cliente / Gruppo articoli / Listino | 11   | Gruppo clienti / Listino                   |
| 4    | Cliente / Gruppo articoli           | 12   | Gruppo clienti                             |
| 5    | Cliente / Listino                   | 13   | Articolo / Listino                         |
| 6    | Cliente                             | 14   | Articolo                                   |
| 7    | Gruppo clienti / Articolo / Listino | 15   | Gruppo articoli / Listino                  |
| 8    | Gruppo clienti / Articolo           | 16   | Gruppo articoli                            |

Cliente e gruppo clienti insieme (o articolo e gruppo articoli insieme) non sono ammessi: la regola non si salva.

Gli altri campi della regola:

- **Agente**: la regola vale solo per i documenti di quell'addetto; *(tutti)* = per tutti;
- **Dal / Al**: periodo di validità confrontato con la data del documento; anche una sola delle due date;
- **Sconto minimo**: la regola vale se lo sconto della riga è almeno questo (0 = sempre). Serve a dare
  percentuali più basse alle vendite più scontate;
- **Attiva**: una regola disattivata resta in archivio ma non si applica.

### Come viene scelta la regola di una riga

1.  Le combinazioni si provano nell'**ordine della Configurazione** (predefinito 1 → 16, dalla più specifica alla
    più generica).
2.  Per ogni combinazione si cercano prima le regole dell'**agente del documento** (se ne ha almeno una), poi
    quelle per tutti. La prima combinazione che trova una regola valida vince: una regola "per tutti" più specifica
    (es. Cliente / Gruppo articoli) vince su una regola dell'agente più generica (es. Gruppo articoli).
3.  Tra più regole della stessa combinazione vince quella con la data di inizio più recente, poi con la scadenza più
    vicina, poi con lo sconto minimo più alto raggiunto.
4.  Se nessuna regola vale, si usano le percentuali predefinite dell'agente.

Esempio con le regole della figura (R1 cliente C001 + gruppo articoli GA100 → 6/1; R2 solo Rossi, gruppo GA100 → 7/1;
R3 articolo A1 → 4/0,5; R4 articolo A1 con sconto minimo 10 → 3/0,5; R5 gruppo clienti A, anno 2026 → 5/1):

| Riga                                            | Percentuali agente / capo zona | Perché                                                          |
|-------------------------------------------------|--------------------------------|-----------------------------------------------------------------|
| Rossi, cliente C001, articolo A9 (gruppo GA100) | 6 / 1                          | R1: Cliente / Gruppo articoli viene prima della regola di Rossi |
| Rossi, cliente C002, articolo A9                | 7 / 1                          | R2: regola dell'agente                                          |
| Verdi, cliente C002, articolo A9                | 1,5 / 0                        | nessuna regola: percentuali predefinite di Verdi                |
| Verdi, cliente C002, articolo A1, sconto 12     | 3 / 0,5                        | R4: sconto minimo 10 raggiunto (vince su R3)                    |
| Verdi, cliente C002, articolo A1, sconto 5      | 4 / 0,5                        | R3                                                              |
| Verdi, cliente C003 (gruppo A), articolo A1     | 5 / 1                          | R5: Gruppo clienti viene prima di Articolo                      |
| come sopra ma nel 2027                          | 4 / 0,5                        | R5 scaduta, resta R3                                            |

### La form

- **Filtri** (agente, cliente, articolo, solo attive) e **Cerca**.
- **Aggiungi riga**, **Duplica righe** ed **Elimina righe** sulle righe selezionate (clic sull'intestazione
  di riga, a sinistra); le modifiche diventano definitive con **Salva**. Tutti i campi si modificano nella
  griglia (le frecce aprono cliente e articolo).
- **Esporta CSV** salva le regole mostrate in un file con separatore ";" (si apre in Excel); **Importa CSV**
  aggiunge le righe di un file con le stesse colonne (Agente, Cliente, GruppoClienti, Articolo, GruppoArticoli,
  Listino, Dal, Al, ScontoMinimo, PercAgente, PercCapoZona, PercCapoArea, PercDirettore, Attiva): le righe importate
  vanno controllate e salvate.
- Chiudendo o cercando con modifiche non salvate l'add-on chiede conferma.

## 8. Le percentuali sui documenti di vendita

![Ordine cliente](../../_img/commissionmanagement/ordine.png)

*Ordine cliente: le colonne Provv. con le percentuali assegnate e, con i prezzi netti, lo sconto effettivo*

Con l'assegnazione attiva, su offerte, ordini, consegne, resi, fatture, note di credito e fatture d'anticipo:

- quando si inserisce o si cambia l'**articolo**, lo **sconto** o il **prezzo** di una riga, l'add-on scrive
  le quattro percentuali della riga (e lo sconto effettivo, con i prezzi netti);
- scegliendo più articoli dalla lista, vengono completate anche le righe aggiunte;
- cambiando il **cliente** o l'**addetto alle vendite** di un documento in inserimento, tutte le righe vengono
  riassegnate. Attenzione: cambiando il cliente SAP rimette l'addetto predefinito di quel cliente; se è "nessuno" le
  righe restano com'erano finché non si sceglie l'agente.

Le percentuali restano **modificabili a mano** e vengono salvate col documento; vengono riscritte solo se si
cambia di nuovo articolo, prezzo o sconto di quella riga. I documenti copiati (ordine → consegna → fattura) portano con
sé le percentuali delle righe.

> Le colonne *Provv. % agente*, *% capo zona*, *% capo area*, *% direttore* e
> *Provv. sconto effettivo* vengono rese visibili e modificabili dall'add-on quando si apre il documento; per
> averle sempre nella posizione preferita si possono sistemare una volta nelle impostazioni della form (icona in alto a
> destra della griglia). Nei documenti senza addetto alle vendite, o con un addetto senza ruolo, non viene scritto nulla.

La spunta "solo imposta" di una riga non genera un evento nel client: le percentuali si adeguano al successivo cambio
di articolo, prezzo o sconto della riga (o cambiando agente).

### Righe manuali (opzione "proteggi le percentuali modificate a mano")

![Ordine con riga manuale](../../_img/commissionmanagement/ordine_manuale.png)

*Ordine: la riga con la percentuale corretta a mano è segnata in "Provv. % manuali" e non viene più riassegnata*

Con l'opzione attiva l'add-on mostra anche la colonna *Provv. % manuali*. Appena si scrive a mano una delle
quattro percentuali di una riga, la riga viene **segnata manuale** e da quel momento non viene più riassegnata: né
cambiando articolo, prezzo o sconto della riga, né cambiando cliente o agente del documento, né scegliendo altri
articoli dalla lista. Le altre righe continuano a seguire le regole. Per tornare all'automatico basta togliere la
spunta: al prossimo cambiamento la riga riceve di nuovo le percentuali delle regole. Il flag passa ai documenti copiati
e si vede nel Controllo (colonna *% manuali*), dove le righe manuali non vengono proposte per la correzione.

### Stima e calcolo automatico alla registrazione

![Stima in barra di stato](../../_img/commissionmanagement/stima.png)

*Dopo l'aggiunta dell'ordine la barra di stato mostra la provvigione stimata per ogni beneficiario*

Due opzioni della scheda Documenti agiscono quando il documento viene **salvato** dal client SAP:

- **Stima**: per offerte, ordini, consegne, resi, fatture, note di credito e fatture d'anticipo, la barra di
  stato mostra quanto maturerebbe con le percentuali attuali delle righe, beneficiario per beneficiario, ad esempio
  *"Provvigioni stimate (Ordine cliente 1250): PRV Rossi 6,00; PRV Bianchi 1,00 - totale 7,00"*. Lo sconto di
  testata è considerato o no secondo l'ultima scelta fatta nel Calcolo. Non viene salvato nulla.
- **Calcolo automatico**: le fatture, le note di credito e (se attive) le fatture d'anticipo **aggiunte** dal
  client vengono calcolate subito, come se si fosse lanciato Calcolo provvigioni sul solo documento; la barra di
  stato dice *"Provvigioni calcolate (Fattura 1001): ..."*. In Provvigioni calcolate l'origine è "Automatico".
  Se il calcolo non è possibile (anticipo già detratto, periodo chiuso, agente non gestito) compare un avviso e il
  documento resta normalmente registrato: lo si calcola poi da Calcolo provvigioni, e le Verifiche lo segnalano tra
  i "da calcolare".

> I documenti creati da importazioni, dal Service Layer o dalla DI API non passano dal client SAP: per
> quelli vale sempre Calcolo provvigioni (o il calcolo di tutto il periodo, che prende solo i documenti non ancora
> calcolati).

## 9. Controllo e assegnazione %

![Controllo e assegnazione percentuali](../../_img/commissionmanagement/controllo.png)

*Controllo: percentuali del documento ("Doc.") e proposte dalle regole, righe diverse evidenziate*

Prima del calcolo conviene verificare che le percentuali sui documenti del periodo corrispondano alle regole (chi ha
inserito la fattura potrebbe averle cambiate, o le regole possono essere state aggiornate dopo).

1.  Scegliere agente (o tutti), periodo e tipi di documento: fatture, fatture d'anticipo, note di credito **non ancora
    calcolati** e, volendo, ordini cliente aperti. Premere **Verifica**.
2.  Per ogni riga la griglia mostra le percentuali attuali (*Doc.*), quelle che le regole darebbero oggi
    (*Proposta*) e l'*Origine proposta* (regola per tutti, regola dell'agente, percentuali predefinite). Le
    righe diverse sono evidenziate e già spuntate; con "Solo righe diverse da quanto proposto" si vedono solo quelle.
3.  Togliere la spunta alle righe da lasciare com'erano (le correzioni volute) e premere **Applica le % proposte**.

Cosa succede alle righe spuntate:

- **ordini cliente aperti**: l'ordine viene aggiornato; le nuove percentuali passano ai documenti che verranno
  copiati da esso;
- **fatture, fatture d'anticipo e note di credito**: sono documenti registrati e SAP non ne permette la modifica
  (nemmeno dei campi utente delle righe). Le percentuali corrette vengono salvate dall'add-on in una propria tabella
  e usate dal calcolo al posto di quelle del documento; il documento SAP resta com'è. La colonna *Già corretta*
  lo segnala e la colonna *Doc.* mostra da quel momento le percentuali corrette.

![Controllo con righe manuali](../../_img/commissionmanagement/controllo_manuale.png)

*Controllo sugli ordini aperti: le righe manuali diverse dalla proposta non vengono spuntate ("con % manuali: 3")*

Doppio clic su una riga apre il documento. I documenti con provvigioni già calcolate non compaiono: per correggerli si
usa Provvigioni calcolate (capitolo 11). La colonna *% manuali* mostra le righe le cui percentuali sono state
corrette a mano sul documento: con l'opzione "proteggi le percentuali modificate a mano" non vengono spuntate (si possono
spuntare apposta). Con il periodo chiuso attivo, i documenti registrati con data nel periodo non si correggono.

## 10. Calcolo provvigioni

![Calcolo provvigioni](../../_img/commissionmanagement/calcolo.png)

*Calcolo provvigioni con l'esito per documento*

Scegliere il periodo (data documento), i tipi (fatture, fatture d'anticipo se attive in Configurazione, note di
credito) e se **considerare lo sconto di testata** (il documento intero scontato riduce l'imponibile di ogni riga).
**Calcola** elabora tutti i documenti del periodo **non annullati**, con un agente gestito e **non ancora
calcolati**: prima le fatture d'anticipo, poi fatture e note di credito. La griglia mostra per ogni documento quanti
beneficiari hanno provvigione, il totale e l'esito; doppio clic apre il documento.

Con **Solo il documento** (tipo e numero) si calcola o **ricalcola** un documento preciso, ad esempio dopo una
correzione delle percentuali; il ricalcolo è possibile solo se nessuna sua quota è liquidata o consolidata.

### Come si calcola, passo per passo

Per ogni beneficiario (agente e superiori con ruolo):

1.  **Imponibile di riga** = totale riga in valuta locale, ridotto dello sconto di testata se richiesto; negativo nelle
    note di credito. Le righe a zero (omaggi) non contano.
2.  **Provvigione di riga** = imponibile × percentuale della riga per quel ruolo. Le righe con percentuale 0 non
    contano.
3.  **Totale** = somma delle provvigioni di riga. Dalle fatture che chiudono un anticipo si toglie la provvigione
    già calcolata sull'anticipo (in proporzione all'importo detratto).
4.  **Quote**: la quota al fatturato (rata 0) alla data di registrazione; il resto a rate (rata n alla scadenza
    della rata n, in proporzione alla sua percentuale, l'ultima rata prende gli arrotondamenti) oppure sul totale
    (rata -1 alla scadenza dell'ultima rata). Le note di credito hanno una sola quota negativa (rata 0 alla
    registrazione o, con l'opzione, alla scadenza).

Gli importi sono arrotondati a 2 decimali; il totale della provvigione è sempre la somma delle quote.

### Esempio: fattura 1001

Rossi (30% al fatturato, a rate), cliente C001, **sconto di testata 10%**, due rate al 50% (31/03 e 30/04):

| Riga         | Totale riga | Imponibile (−10%) | % agente | Provv. agente | % capo zona | Provv. capo zona |
|--------------|-------------|-------------------|----------|---------------|-------------|------------------|
| A1           | 1.000,00    | 900,00            | 5        | 45,00         | 1           | 9,00             |
| A2           | 500,00      | 450,00            | 4        | 18,00         | 0           | \-               |
| A3 (omaggio) | 0,00        | \-                | 5        | \-            |             |                  |
| Totale       |             | 1.350,00          |          | 63,00         |             | 9,00             |

| Beneficiario                         | Quota                 | Scadenza              | Importo |
|--------------------------------------|-----------------------|-----------------------|---------|
| Rossi (agente, 30% al fatturato)     | rata 0 – al fatturato | 10/03 (registrazione) | 18,90   |
|                                      | rata 1 (35%)          | 31/03                 | 22,05   |
|                                      | rata 2 (35%)          | 30/04                 | 22,05   |
| Bianchi (capo zona, 0% al fatturato) | rata 1 (50%)          | 31/03                 | 4,50    |
|                                      | rata 2 (50%)          | 30/04                 | 4,50    |

Neri (capo area) non riceve nulla perché non ha un ruolo, anche se la riga A1 ha lo 0,5% nella sua colonna.

### Fatture d'anticipo

SAP registra una fattura d'anticipo con le righe intere dell'ordine e uno sconto di testata pari al complemento
dell'anticipo (anticipo del 30% = sconto 70%): l'add-on usa sempre quello sconto, quindi l'imponibile è la quota di
anticipo (10.000 × 30% = 3.000 → 150,00 al 5%). Quando la fattura finale detrae l'anticipo, dalla sua provvigione
(10.000 × 5% = 500,00) si tolgono i 150,00 già calcolati: restano 350,00, divisi nelle quote come al solito. Finché la
fattura finale ha provvigioni calcolate, l'anticipo non si può ricalcolare né eliminare (va corretta la fattura).

### Cosa non si ricalcola

- documenti con quote **liquidate o consolidate** (prima va tolta la liquidazione, capitolo 11);
- fatture d'anticipo già detratte da una fattura calcolata;
- documenti annullati: non si calcolano; se erano stati calcolati prima dell'annullamento la loro provvigione va
  eliminata a mano da Provvigioni calcolate (la Liquidazione li ignora).

## 11. Provvigioni calcolate: consultare e correggere

![Provvigioni calcolate](../../_img/commissionmanagement/provvigioni.png)

*Provvigioni calcolate: elenco, righe del documento con la % del beneficiario e quote*

L'elenco in alto mostra una riga per documento e beneficiario (filtri per agente, tipo, periodo, numero, solo non
liquidate): imponibile, provvigione, liquidato, da liquidare, data di calcolo. Cliccando una riga, sotto compaiono le
**righe del documento** con la percentuale di quel beneficiario e le **quote**. Doppio clic apre il documento in SAP.

Ricalcola con le % modificate  
Si cambia la percentuale nelle righe in basso (colonna *%*) e si ricalcola questa sola provvigione. Il documento
SAP non viene toccato: serve a correggere un singolo caso senza modificare le regole. Esempio: riga A2 da 4% a 6%
→ 63,00 diventa 72,00 e le quote 21,60 / 25,20 / 25,20.

Ricalcola dal documento  
Ricalcola con le percentuali attuali delle righe del documento (o corrette dal Controllo): annulla le modifiche
fatte con il pulsante precedente e recepisce correzioni fatte sul documento.

Salva quote  
Data di liquidazione, importo liquidato e spunta *Consolidata* delle quote si possono modificare a mano
(liquidazioni fuori dalla procedura, sistemazioni): Salva quote le registra e aggiorna il liquidato della testata.

Elimina provvigione  
Toglie la provvigione di questo beneficiario sul documento; il documento torna calcolabile dal Calcolo (solo il
documento o nel periodo).

Ricalcolo ed eliminazione sono bloccati se una quota è già liquidata o consolidata ("Provvigioni già liquidate o
consolidate: prima togliere la liquidazione": in Salva quote azzerare il liquidato), se il documento è nel **periodo
chiuso** (scheda Liquidazione della Configurazione) e, per prudenza, se l'addetto non è più nella gerarchia dell'agente
del documento (il ricalcolo lo cancellerebbe: usare Elimina se è voluto).

**Tracciabilità**: ogni testata e ogni quota mostrano *Origine*, *Utente* e *Ultima modifica*: chi ha
scritto l'ultima volta quel dato e come. Origini delle testate: *Calcolo* (dal menu), *Automatico alla
registrazione*, *Ricalcolo dal documento*, *Ricalcolo con % modificate*; delle quote:
*Calcolo*, *Liquidazione*, *Storno insoluto*, *Manuale* (Salva quote).

## 12. Liquidazione

![Liquidazione](../../_img/commissionmanagement/liquidazione.png)

*Liquidazione: proposte delle quote da liquidare al 31/03*

1.  Indicare la **data limite** (di norma fine mese), se includere le note di credito e, volendo, spuntare gli
    agenti da elaborare (nessuno = tutti). **Elabora**.
2.  La griglia propone:
    - **Liquida** – quote non ancora liquidate e non consolidate con scadenza entro la data limite:
      - la quota al fatturato (rata 0) sempre, alla sua scadenza (data di registrazione del documento);
      - la quota di una rata quando quella rata risulta **chiusa** in SAP; la quota sul totale (rata -1) quando
        tutte le rate sono chiuse;
      - la **data di liquidazione** proposta è la più recente tra la scadenza della rata e la data d'incasso.
        La data d'incasso tiene conto di incassi (data del pagamento o sua scadenza se successiva), effetti
        versati a buon fine, riconciliazioni con prima nota o note di credito, note di credito emesse sulla
        fattura; se non si riesce a determinarla vale la scadenza.
    - **Storna** (righe rosse) – quote già liquidate e non consolidate le cui rate non risultano più saldate
      (incasso annullato, insoluto): la liquidazione viene tolta e l'importo torna da liquidare.
3.  Togliere la spunta alle righe da non registrare, correggere se serve la data di liquidazione, spuntare
    **Consolida** sulle quote da rendere definitive. I totali in fondo si aggiornano con le spunte.
4.  **Conferma** registra le righe spuntate; il liquidato dei documenti si aggiorna e una nuova elaborazione non le
    ripropone.

![Storno](../../_img/commissionmanagement/liquidazione_storno.png)

*Dopo l'annullamento di un incasso: proposta di storno delle quote liquidate*

Esempio: la fattura 1001 ha la prima rata (scadenza 31/03) incassata il 05/04. Elaborando al 30/04 vengono proposte
la quota rata 1 di Rossi (22,05) e di Bianchi (4,50) con data di liquidazione 05/04. Se l'incasso viene annullato, la
successiva elaborazione propone lo storno delle due quote; se la quota di Rossi era stata consolidata, viene proposto
solo lo storno di Bianchi.

> Una quota **consolidata** è definitiva: non si storna e la provvigione del documento non si ricalcola
> più. Consolidare quando le provvigioni sono state pagate all'agente.

### Incassi parziali (opzione)

![Liquidazione con incasso parziale](../../_img/commissionmanagement/liquidazione_parziale.png)

*Incasso parziale: righe gialle con la parte liquidabile, la quota intera e il già liquidato*

Di norma la quota di una rata si liquida solo quando la rata è **chiusa**: se il cliente paga un acconto, la
provvigione resta ferma. Con l'opzione **Incassi parziali** la quota si liquida in proporzione a quanto incassato:
rata da 816,75 con quota 22,05, il cliente paga 408,38 (la metà) → viene proposta la liquidazione di **11,03** (riga
gialla, con le colonne *Quota intera* 22,05 e *Già liquidato* 0), alla data dell'incasso se è dopo la
scadenza; al saldo viene proposto il resto, **11,02**. Se un incasso viene annullato, lo storno riporta il liquidato
alla parte ancora incassata (tutto, se non resta nulla di incassato). Le quote al fatturato (rata 0) non cambiano; per
le quote "sul totale documento" la proporzione è sull'incassato di tutte le rate.

### Periodo chiuso (opzione)

Quando gli estratti di un mese sono stati consegnati, si può **chiudere il periodo** fino a quella data (scheda
Liquidazione della Configurazione): da quel momento, per i documenti con data nel periodo non si ricalcolano né si
eliminano provvigioni, non si modificano quote né si liquida o si storna con una data nel periodo, non si salvano
conguagli né premi nei mesi chiusi e il Controllo non corregge i documenti registrati. In ogni caso il messaggio dice
*"Periodo chiuso fino al gg/mm/aaaa"*, prima di qualunque domanda di conferma (se le quote sono già liquidate
dice invece *"Provvigioni già liquidate o consolidate"*). Una fattura del periodo mai calcolata si può ancora calcolare. Per
correggere qualcosa: spostare indietro la data (o togliere la spunta), correggere, rimetterla.

## 13. Conguagli

![Conguagli](../../_img/commissionmanagement/conguagli.png)

*Conguagli di un mese*

Importi manuali per agente e mese, positivi o negativi (premi, rimborsi, recuperi, rettifiche), con un ordine e una
descrizione. Si sceglie anno e mese (frecce \< e \> per cambiare mese, **Mostra**), si aggiungono o si eliminano
righe e si preme **Salva**: le righe del mese vengono sostituite con quelle della griglia. I conguagli compaiono
nell'estratto "liquidate e conguagli" del mese. La colonna *Tipo* distingue i conguagli *manuali* dai
*premi* registrati dagli scaglioni (capitolo 15), che qui si vedono ma non si modificano. Con il periodo chiuso
attivo i mesi chiusi non si salvano.

### Bozze fatture agenti (opzione)

![Bozze fatture agenti](../../_img/commissionmanagement/bozze.png)

*Conguagli: in basso le bozze di fattura generate per il mese, con il link alla bozza e al fornitore*

Quando l'agente fattura le provvigioni all'azienda, il pulsante **Bozze fatture agenti** prepara il documento al
posto suo. Per il mese scelto, per ogni agente gestito che ha un **fornitore** collegato (capitolo 6):

- importo = quote **liquidate nel mese** (per data di liquidazione) + **conguagli e premi** del mese;
- importo positivo → bozza di **fattura di acquisto**; negativo → bozza di **nota di credito di acquisto**;
  zero → niente;
- la bozza ha una riga di servizio sul conto indicato in Configurazione, con il codice IVA scelto (o quello
  predefinito del fornitore) e l'importo come totale riga.

Esempio: Rossi (fornitore V20000), aprile: rata liquidata il 05/04 di 22,05 + conguagli +50,00 e -20,00 = bozza di
fattura di acquisto da **52,05**. Al termine un messaggio riepiloga agente per agente (bozza creata, nessun fornitore,
importo zero, bozza già presente). Le bozze del mese stanno nella griglia in basso con lo **stato** (aperta, chiusa
cioè già trasformata in fattura, eliminata), la data e l'utente; la freccia gialla apre la bozza o il fornitore. Un
agente con una bozza ancora esistente per quel mese viene saltato: per rigenerarla eliminare la bozza in SAP.
La bozza va poi completata e registrata da SAP come qualunque altra bozza (numero e data della fattura dell'agente).

## 14. Estratto provvigioni

![Estratto provvigioni](../../_img/commissionmanagement/estratto.png)

*Estratto "liquidate e conguagli" di aprile, raggruppato per agente*

Tre estratti, per un periodo e per un agente o tutti, raggruppati per agente (frecce per espandere e comprimere),
con il totale in fondo ed **Esporta CSV** (una riga "Totale" con il nome di ogni agente, da aprire in Excel):

| Estratto                          | Cosa mostra                                                                                  | Periodo riferito a   |
|-----------------------------------|----------------------------------------------------------------------------------------------|----------------------|
| Provvigioni calcolate             | una riga per documento e beneficiario: imponibile, provvigione, liquidato                    | data del documento   |
| Provvigioni da liquidare          | le quote non ancora liquidate (o liquidate in parte) e non consolidate                       | scadenza della quota |
| Provvigioni liquidate e conguagli | le quote liquidate più i conguagli dei mesi del periodo: **è quanto riconoscere all'agente** | data di liquidazione |

### Stampa / PDF

![Estratto stampato](../../_img/commissionmanagement/estratto_stampa.png)

*L'estratto aperto nel browser: un blocco per agente, totali e ritenuta indicativa*

Il pulsante **Stampa / PDF** apre l'estratto mostrato nel browser, impaginato: intestazione con società, tipo di
estratto e periodo, un blocco per ogni agente con le sue righe e il totale. Da lì si stampa o si salva in PDF (Stampa →
"Salva come PDF"). Se in Configurazione è indicata la **ritenuta indicativa** (es. 8,5 "Enasarco quota agente"),
l'estratto "liquidate e conguagli" mostra per ogni agente anche la riga della ritenuta e il **netto indicativo**:
sono informazioni di comodo per l'agente, senza minimali né massimali.

### Invia agli agenti (opzione)

Con l'invio via email attivo (scheda Email della Configurazione), il pulsante **Invia agli agenti** manda a ogni
agente dell'estratto mostrato un messaggio con in allegato **il solo suo estratto** in HTML (apribile e stampabile da
qualunque browser). L'indirizzo è quello dell'addetto alle vendite o, se manca, quello del fornitore collegato. Alla
fine un riepilogo dice per ogni agente se l'invio è riuscito, se manca l'indirizzo o quale errore ha dato il server.
Il pulsante è attivo solo per chi ha l'autorizzazione completa sull'estratto di tutti gli agenti.

### Ogni capo vede i suoi agenti

Un utente SAP collegato a un addetto (colonna *Utente SAP* in Agenti) che non ha l'autorizzazione "Estratto di
tutti gli agenti" trova nella tendina solo *(i miei agenti)* e i nomi suoi e dei suoi sottoposti (gli addetti di
cui è capo zona, capo area o direttore): un capo zona può consultare l'estratto dei propri agenti senza vedere gli
altri. Chi non è collegato a nessun addetto, senza l'autorizzazione, non vede niente.

## 15. Scaglioni e premi

![Scaglioni e premi](../../_img/commissionmanagement/scaglioni.png)

*Scaglioni e premi: in alto gli scaglioni, in basso i premi calcolati per l'anno*

Con l'opzione "scaglioni di fatturato annuo con premio" (scheda Agenti della Configurazione) il menu **Scaglioni e
premi** gestisce i premi di fine anno legati al fatturato. Uno **scaglione** ha: agente (o *tutti*), anno (o
*ogni anno*), soglia di imponibile annuo, tipo di premio (*% sul fatturato* dell'anno o *importo fisso*),
premio, descrizione, attivo. Si aggiungono, modificano ed eliminano righe nella griglia in alto e si preme **Salva scaglioni**.

| Agente  | Anno        | Soglia | Tipo            | Premio | Descrizione       |
|---------|-------------|--------|-----------------|--------|-------------------|
| (tutti) | (ogni anno) | 1.000  | % sul fatturato | 0,5    | Premio base       |
| (tutti) | (ogni anno) | 10.000 | % sul fatturato | 1      | Premio 10.000     |
| Rossi   | 2026        | 12.000 | importo fisso   | 500,00 | Premio Rossi 2026 |

**Calcola premi** per un anno: il fatturato di ogni agente è la somma degli imponibili delle sue provvigioni
calcolate (fatture e note di credito con data nell'anno; non le fatture d'anticipo, già comprese nelle fatture finali).
Lo scaglione raggiunto è quello con la **soglia più alta** non superiore al fatturato; gli scaglioni dell'agente
prevalgono su quelli per tutti e l'anno specifico su "ogni anno". Premio = fatturato × % oppure importo fisso.
Esempio con gli scaglioni sopra: Rossi 13.150 → scaglione 12.000 dell'agente → **500,00**; Bianchi 2.900 →
scaglione 1.000 → 0,5% = **14,50**; Verdi 1.488 → **7,44**. La colonna *Già registrato* mostra il premio
dello stesso anno già registrato.

**Registra premi spuntati**: le righe spuntate diventano conguagli di tipo *Premio* nel mese scelto (di
norma dicembre): da lì entrano nell'estratto "liquidate e conguagli", nelle bozze fatture e nei totali del mese come
gli altri conguagli. Registrando di nuovo lo stesso anno il premio precedente viene sostituito (non duplicato); un
premio a zero lo toglie. Con il periodo chiuso attivo i mesi chiusi non si registrano.

## 16. Verifiche e avvisi all'avvio

![Verifiche](../../_img/commissionmanagement/verifiche.png)

*Verifiche: anomalie del periodo, errori in rosso*

Il menu **Verifiche** cerca in un periodo tutto ciò che può far mancare o sbagliare una provvigione. Si indica il
periodo, se cercare anche gli incassi non liquidati (è la ricerca più lenta) e si preme **Verifica**: ogni anomalia ha
una gravità (**errore** in rosso, **avviso**), la verifica che l'ha trovata, l'agente, il documento e la
spiegazione con cosa fare. Doppio clic apre il documento.

| Verifica              | Cosa segnala                                                                                                                    | Cosa fare                                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Da calcolare          | fatture, anticipi e note di credito del periodo con agente gestito e senza provvigioni                                          | Calcolo provvigioni                             |
| Senza agente          | documenti senza addetto alle vendite o con un addetto senza ruolo                                                               | verificare se è voluto; dare il ruolo in Agenti |
| Righe senza %         | documenti con agente gestito le cui righe hanno tutte le percentuali a zero                                                     | Controllo e assegnazione % o regole mancanti    |
| Agente cambiato       | documenti calcolati il cui addetto in SAP non è più quello della provvigione                                                    | Ricalcola in Provvigioni calcolate              |
| Annullato             | documenti annullati con provvigioni calcolate                                                                                   | Elimina provvigione                             |
| Gerarchia agenti      | superiore senza ruolo (la sua parte non matura), percentuale predefinita di un ruolo senza il superiore, utente SAP inesistente | sistemare in Agenti                             |
| Regole sovrapposte    | due regole attive uguali (stessi campi, sconto e addetto) con periodi che si sovrappongono: vale solo una delle due             | correggere le regole                            |
| Incassi non liquidati | quote la cui rata è incassata da più dei giorni indicati in Configurazione e non ancora liquidate                               | Liquidazione                                    |

Con l'opzione **avvisi all'avvio**, ogni volta che l'add-on parte esegue le verifiche rapide (documenti degli
ultimi 90 giorni da calcolare, agente cambiato e annullati nell'ultimo anno) e, se trova qualcosa, lo dice nella barra
di stato qualche secondo dopo l'avvio, cioè dopo gli eventuali messaggi della licenza: *"Provvigioni: 3 anomalie
da controllare (Provvigioni \> Verifiche)"*. Senza anomalie non scrive nulla.

## 17. Autorizzazioni e tracciabilità

L'add-on crea nelle **Autorizzazioni generali** di SAP (Amministrazione › Inizializzazione sistema ›
Autorizzazioni) la voce **Provvigioni** sotto *Autorizzazione utente*, con cinque sottovoci. I superutenti hanno
sempre tutto; agli altri utenti si assegna per ogni voce *Senza autorizzazione*, *Solo accesso di lettura* o
*Autorizzazione completa*:

![Autorizzazioni generali](../../_img/commissionmanagement/autorizzazioni.png)

*Autorizzazioni generali: la voce Provvigioni con le cinque sottovoci, per un utente senza autorizzazioni*

| Autorizzazione                          | Sola lettura                                                              | Completa                                                                     |
|-----------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Configurazione                          | –                                                                         | aprire e salvare la Configurazione                                           |
| Agenti, regole e scaglioni              | consultare                                                                | salvare agenti, regole e scaglioni                                           |
| Controllo, calcolo e verifiche          | consultare Controllo, Calcolo, Provvigioni calcolate, Verifiche           | applicare le %, calcolare, ricalcolare, salvare quote, eliminare             |
| Liquidazione, conguagli e bozze fatture | consultare Liquidazione e Conguagli                                       | confermare liquidazioni, salvare conguagli, registrare premi, generare bozze |
| Estratto di tutti gli agenti            | vedere l'estratto di tutti gli agenti (senza: solo i propri, capitolo 14) | anche l'invio email                                                          |

Senza autorizzazione la voce di menu risponde nella barra di stato *"Funzione non consentita: serve
l'autorizzazione «…» (Autorizzazioni generali \> Provvigioni)"*; con la sola lettura la finestra si apre ma i
pulsanti che modificano rispondono *"Operazione non consentita: serve l'autorizzazione completa su «…»"*.

**Tracciabilità**: testate e quote delle provvigioni registrano origine, utente e data dell'ultima scrittura
(capitolo 11); i conguagli l'utente e la data di modifica; le bozze fatture chi le ha generate e quando. Il log
dell'add-on (capitolo 19) registra errori e aggiornamenti della struttura.

## 18. Domande frequenti e problemi

Le percentuali non vengono scritte sul documento  
Controllare: l'opzione in Configurazione; che il documento abbia un addetto alle vendite con un ruolo; che il
cliente sia compilato. Dopo un cambio di cliente, scegliere di nuovo l'agente.

Ho corretto una percentuale sulla fattura ma SAP non me la fa salvare  
Le fatture registrate non si modificano. Usare Controllo e assegnazione % (prima del calcolo) o Provvigioni
calcolate → Ricalcola con le % modificate (dopo).

"Provvigioni già liquidate o consolidate"  
Per ricalcolare o eliminare, in Provvigioni calcolate azzerare il liquidato delle quote (Salva quote) e togliere il
consolidamento. Se le quote sono state davvero pagate all'agente, meglio non toccarle: registrare la differenza come
conguaglio.

"Anticipo già detratto da una fattura con provvigioni calcolate"  
Correggere o eliminare prima la provvigione della fattura finale, poi l'anticipo, poi ricalcolare la fattura.

Una quota non viene proposta in liquidazione  
La rata non è chiusa in SAP (pagamento parziale o non ancora registrato), la scadenza è dopo la data limite, o la
quota è già liquidata/consolidata. Le quote dei documenti annullati non vengono proposte: eliminare la provvigione.

Al primo avvio SAP chiede di chiudere tutte le finestre  
È normale quando si creano campi utente: rispondere Sì fino alla fine della creazione (qualche minuto). Vale anche
quando un aggiornamento dell'add-on aggiunge campi; se il client viene chiuso a metà, la creazione riprende al
riavvio dell'add-on.

"Periodo chiuso fino al..."  
L'operazione riguarda una data entro il periodo chiuso (Configurazione, scheda Liquidazione). Se la correzione è
davvero necessaria: spostare indietro la data del blocco, correggere, rimetterla.

"Funzione non consentita: serve l'autorizzazione «…»"  
L'utente SAP non ha l'autorizzazione (capitolo 17): assegnarla nelle Autorizzazioni generali, voce Provvigioni.

La fattura è stata registrata ma la barra di stato dice "Provvigioni non calcolate"  
Il calcolo automatico non era possibile (anticipo già detratto, periodo chiuso, agente non gestito): il documento
è registrato normalmente; calcolarlo da Calcolo provvigioni (le Verifiche lo elencano tra i "da calcolare").

L'invio email dà errore  
Usare "Prova invio" nella scheda Email della Configurazione: il messaggio del server dice se sono sbagliati
server, porta, SSL o credenziali. Gli agenti "senza email" vanno completati nell'anagrafica dell'addetto alle
vendite o del fornitore collegato.

Una riga del documento non prende le percentuali delle regole  
Con l'opzione "proteggi le percentuali modificate a mano" la riga è segnata manuale (colonna Provv. % manuali):
togliere la spunta e cambiare articolo, prezzo o sconto, oppure correggere a mano.

Mentre l'add-on elabora SAP non risponde  
Durante Verifica, Calcolo, Elabora e Applica SAP aspetta l'add-on (barra di stato "Attendere prego..."): non chiudere
la finestra e non terminare l'add-on, altrimenti il client resta in attesa e va riavviato.

## 19. Dati e note tecniche

| Dove                                                         | Cosa                                                                                                                                                                                                |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLP (addetti alle vendite)                                  | campi `U_XEI_PRV_Ruolo`, `_CapoZona`, `_CapoArea`, `_Direttore`, `_PercAg`, `_PercCZ`, `_PercCA`, `_PercDI`, `_Fatturato`, `_Liquida`, `_Fornitore`, `_Utente` (utente SAP)                         |
| Righe dei documenti di marketing (RDR1, INV1, RIN1, DPI1...) | `U_XEI_PRV_Ag`, `_CZ`, `_CA`, `_DI` (percentuali), `_ScEff` (sconto effettivo), `_Man` (riga manuale)                                                                                               |
| `@XEI_PRV_REGOLE`                                            | regole delle percentuali                                                                                                                                                                            |
| `@XEI_PRV_DOC`, `@XEI_PRV_RIGHE`, `@XEI_PRV_RATE`            | provvigioni calcolate: testata per documento e beneficiario, righe, quote (codice = tipo-DocEntry-addetto\[-riga/rata\], es. `13-386-61-2`); testate e quote con origine, utente e data di modifica |
| `@XEI_PRV_PERC`                                              | percentuali corrette dal Controllo per le righe di documenti registrati                                                                                                                             |
| `@XEI_PRV_CONG`                                              | conguagli (tipo M manuale / P premio, anno di riferimento del premio)                                                                                                                               |
| `@XEI_PRV_SCAG`, `@XEI_PRV_BOZZE`                            | scaglioni; bozze fatture generate (agente, mese, bozza, fornitore, importo)                                                                                                                         |
| `@XEI_SETTINGS` (ambito XEI.CommissionManagement)            | opzioni della Configurazione (password SMTP cifrata) e versione della struttura dei dati                                                                                                            |
| Autorizzazioni (OUPT)                                        | `XEI_PRV` e sottovoci `XEI_PRV_P_CFG`, `_ANAG`, `_CALC`, `_LIQ`, `_EST`                                                                                                                             |

- Tipi di documento: 13 fattura, 203 fattura d'anticipo, 14 nota di credito, 17 ordine (solo nel controllo).
- Tutto passa dalla DI API di SAP (nessuna connessione diretta al database).
- Prestazioni: sui documenti le righe si leggono in blocco (una sola chiamata) e si scrivono solo le celle che
  cambiano; clienti, articoli e listini vengono letti una volta per finestra. Nella liquidazione le date d'incasso
  (la ricerca più pesante) si calcolano solo per le quote effettivamente liquidabili.
- Log: `%LOCALAPPDATA%\XEI\logs\XEI.CommissionManagement.log`.
