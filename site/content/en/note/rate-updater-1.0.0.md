---
title: XEI Rate Updater for SAP Business One 1.0.0 – Release notes
lang: en
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater for SAP Business One 1.0.0 – Release notes

## Features of this version

- **Currency exchange rates in SAP Business One** with the rates of the European Central Bank, the Bank of Italy or
  Open Exchange Rates: for the exchange rates of a day, the rates published the day before apply.
- **Only the company's currencies**, in the company's direction (direct or indirect rate), truncated to six decimals.
- **Local currency other than the euro**: cross rates against the local currency.
- **Manual update** from the Exchange rates page, with the outcome of each currency.
- **Automatic update** every day at the chosen time, or from the Windows Task Scheduler with the
  `XEI.RateUpdater.exe aggiorna` command.
- **History** of the runs of each company, with the rates and the outcome of each currency.
- **XEI license** with the scope Free, Server or Single company; 30-day free trial.
- **Program languages**: Italian, English, German, French, Spanish and Turkish.

## Installation

- Program for Windows 10 and 11 and Windows Server 2016 and later, 64-bit: extract the folder from the zip file and start
  `XEI.RateUpdater.exe`; .NET is already included.
- It requires Microsoft Edge WebView2 Runtime, usually already present, and the Service Layer of SAP Business One 10.0
  or later.
