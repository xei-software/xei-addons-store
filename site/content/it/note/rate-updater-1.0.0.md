---
title: XEI Rate Updater per SAP Business One 1.0.0 – Note di rilascio
lang: it
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater per SAP Business One 1.0.0 – Note di rilascio

## Funzioni di questa versione

- **Cambi delle valute in SAP Business One** con i tassi della Banca centrale europea, della Banca d'Italia o di Open
  Exchange Rates: per i cambi di un giorno valgono i tassi pubblicati il giorno prima.
- **Solo le valute della società**, nel verso della società (tasso diretto o indiretto), troncate a sei decimali.
- **Valuta locale diversa dall'euro**: tassi incrociati rispetto alla valuta locale.
- **Aggiornamento a mano** dalla pagina Cambi, con l'esito di ogni valuta.
- **Aggiornamento automatico** ogni giorno all'ora scelta, oppure dall'Utilità di pianificazione di Windows con il
  comando `XEI.RateUpdater.exe aggiorna`.
- **Storico** delle esecuzioni di ogni società, con i tassi e l'esito di ogni valuta.
- **Licenza XEI** libera, per server o per società; prova gratuita di 30 giorni.
- **Lingue del programma**: italiano, inglese, tedesco, francese, spagnolo e turco.

## Installazione

- Programma per Windows 10 e 11 e Windows Server 2016 e successivi, a 64 bit: si estrae la cartella dello zip e si avvia
  `XEI.RateUpdater.exe`; .NET è già incluso.
- Serve Microsoft Edge WebView2 Runtime, di solito già presente, e il Service Layer di SAP Business One 10.0 o successive.
