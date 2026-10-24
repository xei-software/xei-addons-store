---
title: XEI.ItemGenerator 1.4.0 – Note di rilascio
lang: it
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Note di rilascio

## Novità

- **Ereditarietà delle varianti come proposta.** Con *Eredita varianti* le opzioni
  scelte su un livello precedente vengono proposte, ma si possono cambiare sul livello
  che le eredita. Il tasto destro offre **Torna alle opzioni proposte**.
- **Forza ereditarietà.** Nuova opzione sui valori delle basi: impone la scelta del
  livello precedente, che sul valore non si può cambiare.
- **Tabella e campo utente sulle varianti.** In *Definizione varianti e opzioni* si
  possono indicare una tabella utente e un campo utente dell'articolo: alla creazione
  le opzioni scelte vengono aggiunte alla tabella e riportate nel campo.
- **Genera articoli più leggibile.** Il riquadro delle varianti mostra solo le varianti
  del valore selezionato nell'albero; una casella attiva la vista completa per livello.
- **Elenco degli articoli da generare.** Nuova opzione di configurazione *Aggiungi
  all'elenco svuota prima l'elenco* (attiva per impostazione predefinita): l'elenco
  contiene solo l'ultima selezione. Disattivandola gli articoli si accumulano.
- **Menu numerati.** Le voci del Configuratore codici sono numerate da 0 a 7 nell'ordine
  di lavoro: Configurazione, Definizione basi, Definizione varianti e opzioni, Strutture
  varianti, Genera articoli, Controllo congruenze, Verifica configurazione,
  Importa / esporta Excel.
- **Sotto livello con lista di scelta.** In *Definizione basi* la colonna Sotto livello
  si compila con la lista di scelta delle basi e la freccia apre la base collegata. Un
  codice scritto a mano viene rifiutato se la base non esiste.

## Miglioramenti

- Verifica configurazione e importazione / esportazione Excel aggiornate con i nuovi
  campi.
- Testate delle finestre più compatte, allineate allo stile di SAP Business One.
- Traduzioni aggiornate in inglese, tedesco, francese e spagnolo.

## Aggiornamento

- Richiede XEICore 1.1.1, incluso nel pacchetto.
- Al primo avvio l'add-on aggiorna da solo la struttura dei dati (versione 3).
- Il codice di licenza già inserito resta valido.
