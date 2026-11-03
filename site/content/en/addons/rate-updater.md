---
title: XEI Rate Updater for SAP Business One – Currency exchange rates
description: Updates the currency exchange rates in SAP Business One every day with the official rates of the ECB, the Bank of Italy or Open Exchange Rates.
lang: en
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater for SAP Business One

**Currency exchange rates in SAP Business One, updated on their own.** Every day the program takes the rates from an
official source and writes them to SAP Business One, in the direction and with the decimals that SAP uses.

## Description

Updating exchange rates by hand means copying the rates from a website into the SAP exchange rate table every morning,
currency by currency, with the risk of missing a day or inverting a rate.

XEI Rate Updater for SAP Business One does it for you:

- it takes the rates from the **European Central Bank**, the **Bank of Italy** or **Open Exchange Rates**;
- for the exchange rates of a day it uses the rates published **the day before**; on weekends and holidays it uses the
  latest published day;
- it writes to SAP only the **currencies managed by the company**, in the direction the company uses (direct or
  indirect rate), truncated to six decimals;
- with a **local currency other than the euro** it calculates the cross rates against it;
- it runs **by hand**, choosing the date, or **automatically every day**;
- it keeps the **history** of every update: who ran it, the source, the rates and the outcome of each currency.

## Main features

- **Exchange rates**: date of the exchange rates, source and *Update the exchange rates in SAP* button; the outcome
  shows for each currency the direct rate, the indirect rate and whether it was written to SAP.
- **History**: the company's runs, most recent first; each row opens on the currencies.
- **Automatic update**: every day at the chosen time, or from the Windows Task Scheduler.
- **Errors under control**: an error on one currency does not stop the others; each run says what went wrong.
- **Sign-in with each person's SAP user**, with their own authorizations on exchange rates; the administrator assigns
  each user the *Exchange rate update* and *History* functions.

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later, with the Service Layer |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA a test during installation is recommended) |
| System | Windows 10 and 11, Windows Server 2016 and later, 64-bit; Microsoft Edge WebView2 Runtime |
| Network | internet access to the chosen rate source (ECB, Bank of Italy or Open Exchange Rates with its API key) |
| Program languages | Italian, English, German, French, Spanish, Turkish |
| Installation | the program folder is extracted, no installation needed; .NET is already included |
| License | XEI license code, with the scope Free, Server or Single company (30-day free trial) |

## Current version

**1.0.0** – see the [release notes](../../manuali/en/rateupdater/note-rilascio-1.0.0.md) and the
[user manual](../../manuali/en/rateupdater/manuale-utente.md).
