---
title: XEI.ContoLavoro 1.2.0 – Note di rilascio
description: Funzioni e correzioni di XEI.ContoLavoro 1.2.0 per SAP Business One.
lang: it
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro 1.2.0 – Note di rilascio

## Funzioni di questa versione

- Nella lista «Crea commesse da ordini di produzione», con la casella «Mostra anche le righe non pronte», compaiono anche
  le lavorazioni che non possono diventare commessa, con il motivo e cosa fare nella colonna «Motivo / avvisi».
- Quando salvi una distinta base, un avviso segnala i codici da correggere nel campo «Lavorazione terzista»: risorse,
  codici che non sono articoli, articoli senza «Conto lavoro», lavorazioni che non sono righe della distinta, componenti a
  consuntivo.
- Licenza XEI con la finestra **Licenza** nel menu dell'add-on: stato, codici della società e del server, inserimento
  del codice; prova gratuita di 30 giorni.

## Correzioni di questa versione

- Una commessa interrotta non impedisce di creare un'altra commessa dalla stessa riga dell'ordine di produzione.
- I componenti a consuntivo collegati a una lavorazione esterna non si inviano al terzista e l'ordine di produzione li
  preleva una volta sola.
- Senza la serie di numerazione della commessa terzista, aprendo *Commessa terzista* l'add-on dice dove definirla.
- Il trasferimento massivo dei componenti è attivo nella configurazione predefinita; con l'opzione spenta la voce di menu avvisa che la funzione è disattivata.
- Le commesse create dagli ordini di produzione usano il listino predefinito delle commesse (Configurazione › Generale): senza, «Crea commesse» chiede di indicarlo.
- Nella lista «Crea commesse da ordini di produzione» le righe si selezionano e il fornitore si cambia.
