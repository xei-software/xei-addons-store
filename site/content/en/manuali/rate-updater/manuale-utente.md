---
title: XEI Rate Updater for SAP Business One – User manual
description: "Currency exchange rates in SAP Business One: installation, first start, manual and automatic update, history and license."
lang: en
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater for SAP Business One – User manual

| | |
|---|---|
| SAP Business One | 10.0 or later, with the Service Layer |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA a test during installation is recommended) |
| System | Windows 10 and 11, Windows Server 2016 and later, 64-bit; Microsoft Edge WebView2 Runtime |
| Program languages | Italian, English, German, French, Spanish, Turkish |

## 1. What it does

XEI Rate Updater for SAP Business One updates the **currency exchange rates** in SAP Business One with the rates
published by an official source:

1. it takes the rates of the chosen **source** for the requested date;
2. it reads from the SAP company the **local currency** and the **direction** of the exchange rates: direct rate (local
   currency per one unit of foreign currency) or indirect rate (foreign currency per one unit of local currency);
3. if the local currency is not the euro, it calculates the **cross rates** against it;
4. for each **currency managed by the company** it writes to SAP the exchange rate for the date, in the company's
   direction, truncated to six decimals;
5. it saves the run in the **history**.

An error on one currency does not stop the others.

### The date of the rates

The rates of a day are published at the end of the day. For the SAP exchange rates of a day, the rates published
**the day before** are therefore used. On days without publication (weekends, holidays) the latest day published
before applies.

*Example*: the exchange rates of Monday 24 February 2025 are the rates of Friday 21 February. The date of the exchange
rates cannot be in the future.

### The rate sources

| Source | Notes |
|---|---|
| European Central Bank (ECB) | default, free, no key |
| Bank of Italy | official Italian exchange rates, many currencies |
| Open Exchange Rates | requires an Open Exchange Rates API key (Settings › Exchange rates) |

All sources publish the rates against the euro. With a local currency other than the euro, the source must quote it.

### The currencies

The program recognizes currencies by their **ISO code** (for example `USD`, `CHF`). In SAP, foreign currencies must use
the ISO code as their code. For the local currency, if it has another code in SAP (for example “Eu” or “€” for the
euro), enter the ISO code in *Settings › Exchange rates*.

## 2. Installation

1. Extract the folder from the zip file to the PC, for example to `C:\XEI\RateUpdater`.
2. Start **XEI.RateUpdater.exe**. The program already contains .NET. It requires **Microsoft Edge WebView2 Runtime**,
   which is usually already there: if it is missing, the program says so and offers to download it.

The program has no setup. Settings and history are stored in the Windows data folder of all users of the PC, so they
apply to anyone who uses the program on that PC and to the scheduled update.

## 3. First start

When it opens for the first time, the program shows the **First start** page: it is not connected to SAP yet. The
first-start code is already filled in.

1. **SAP connection**:
   - *Service Layer address*;
   - *SAP companies*: the databases that can be selected at sign-in;
   - **Test the connection**.
2. **Sign-in and first administrator**:
   - *Operator sign-in*: **Each person's SAP user** (everyone signs in with their own SAP user) or **Own users and
     technical SAP user**;
   - *SAP user of the first administrator* (for example `manager`);
   - *Technical SAP user* and its password: they are needed for the **automatic update**. A dedicated user is best,
     with only the permission to write exchange rates.
3. **Save and restart**: the program reopens on the sign-in page.

The same settings can be changed later in **Settings › SAP**.

![First start](../../_img/rateupdater/00b-primo-avvio.png)

*First start: SAP connection, license scope and first administrator.*

![Settings › SAP](../../_img/rateupdater/05-impostazioni-sap.png)

*Settings › SAP: Service Layer address, companies and operator sign-in.*

## 4. Sign-in

You sign in with your **SAP Business One user** and its password. The user and the company are shown at the top right.

![Sign-in](../../_img/rateupdater/00-accesso.png)

*Sign-in with the SAP Business One user.*

With *Each person's SAP user* the program writes the exchange rates with the user who is working: their SAP
authorizations on exchange rates apply.

### User functions

An administrator assigns the functions to each user from the **Users** page of the menu, the same for SAP users and for
own users:

| Function | What it allows |
|---|---|
| Exchange rate update | updating the exchange rates in SAP from the Exchange rates page |
| History | viewing the update runs, manual and automatic |

The administrator has all functions. The first administrator is the SAP user entered on the First start page.

## 5. Exchange rates

**Exchange rates** menu.

1. **Date of the exchange rates in SAP**: it starts from today and cannot be in the future. Below it you can read which
   rates are used and the configured source.
2. Press **Update the exchange rates in SAP**.
3. The **outcome** shows the date, the source, the day of the rates, how many currencies were written and the local
   currency. The table shows for each currency of the source:

| Column | What it shows |
|---|---|
| Currency | ISO code |
| Direct rate | local currency per one unit of foreign currency |
| Indirect rate | foreign currency per one unit of local currency |
| Outcome | **written to SAP**, **not managed** (the company does not use this currency) or refused, with the SAP error |

Below is the status of the **automatic update**, with the last run.

![Exchange rates](../../_img/rateupdater/01-cambi.png)

*Exchange rates: date, source and status of the automatic update.*

![Update outcome](../../_img/rateupdater/02-cambi-esito.png)

*Outcome: rates of the source, currencies written to SAP and currencies that the company does not manage.*

## 6. History

**History** menu: the company's runs, most recent first.

| Column | What it shows |
|---|---|
| Started | date and time of the run |
| By | the user, or *automatic* |
| Rates as of | the date of the exchange rates in SAP |
| Source | the rate source |
| Rates published on | the day of the rates used |
| Currencies written | how many currencies were written to SAP |
| Outcome | **succeeded** or **failed** |

A row opens on the currencies, with the rates and the outcome of each one. The history keeps the latest runs (100 by
default, in *Settings › Exchange rates*).

![History](../../_img/rateupdater/03-storico.png)

*History: manual and automatic updates of the company.*

![History with the currencies](../../_img/rateupdater/03b-storico-valute.png)

*An open row: rates and outcome of each currency.*

## 7. Settings › Exchange rates

For administrators only. After making changes press **Save settings**.

| Setting | What it does |
|---|---|
| Rate source | European Central Bank (default), Bank of Italy or Open Exchange Rates |
| ISO code of the local currency | only if in SAP the local currency has a code other than the ISO one; empty = taken from SAP |
| Open Exchange Rates API key | only with the Open Exchange Rates source; stored encrypted |
| Automatic update | every day the program updates today's exchange rates of each company on its own, with the technical SAP user |
| Automatic update time | in HH:mm format (default 07:00) |
| Runs kept in the history | how many runs to keep for each company, from 10 to 1000 (default 100) |

![Settings › Exchange rates](../../_img/rateupdater/04-impostazioni-cambi.png)

*Settings › Exchange rates: source, local currency, automatic update and history.*

## 8. Automatic update

Today's exchange rates are updated every day in two ways.

### With the program open

With **Automatic update** turned on, once the set time has passed the program updates today's exchange rates of each
company with the technical SAP user and saves the run in the history (*By*: automatic). If the program was closed at the
set time, it updates as soon as it is reopened. If the source or SAP does not respond, it tries again shortly after.

### With the Windows Task Scheduler

This way the exchange rates are updated even without opening the program.

1. Complete the first start and set the **technical SAP user** (Settings › SAP).

   ![Technical SAP user](../../_img/rateupdater/05b-impostazioni-sap-tecnico.png)

   *The technical SAP user in Settings › SAP.*

2. In Windows open **Task Scheduler** and create a basic task, for example every day at 7:00.
3. As the action choose **Start a program**:
   - program: `XEI.RateUpdater.exe` in the program folder;
   - arguments: `aggiorna`.
4. In the task properties choose **Run whether user is logged on or not**, with a Windows user of the PC.

The command updates today's exchange rates with the technical SAP user and closes, without a window. It uses the same
settings and the same history as the program. Optional arguments:

| Argument | Meaning |
|---|---|
| `--societa <database SAP>` | the company (SAP database) to update; not needed with only one company configured |
| `--data aaaa-mm-gg` | the date of the exchange rates (year-month-day), if it is not today |

Task Scheduler receives the result: **0** succeeded, **1** failed or with a refused currency, **2** wrong arguments.
The details are in the history. If the command has already updated today's exchange rates, the open program does not
update them again.

## 9. License

The program works with a **license code** issued by XEI, in three scopes:

| Scope | Applies to |
|---|---|
| Single company | one SAP database |
| Server | all the companies of the SQL Server or SAP HANA instance |
| Free | not tied to a database |

The **free trial** lasts 30 days, with the scope Free.

![License](../../_img/rateupdater/06-licenza.png)

*The License page: status, expiry, scope and field for the code.*

![Settings › License](../../_img/rateupdater/06b-impostazioni-licenza.png)

*Settings › License: the three license scopes.*

**License** menu: status, expiry and scope of the license. Paste the code received from XEI into **Enter a license
code**: it takes effect immediately, without restarting. For a per-company or per-server license the program must be
connected, read-only, to the license database (*Settings › License*, **Test connection**): the company and server codes
to send to XEI appear there and on the License page.

For licenses: [license@xeisrl.com](mailto:license@xeisrl.com).

## 10. Frequently asked questions and problems

| What you see | Why | What to do |
|---|---|---|
| A currency is *not managed* | The SAP company does not use that currency | Nothing: only the company's currencies are written |
| A currency of the company is not updated | In SAP the currency does not use the ISO code as its code | Use the ISO code in SAP (for example `USD`) |
| The run stops immediately with an error on the local currency | The source does not quote the local currency, or in SAP it has a non-ISO code | Enter the ISO code in *Settings › Exchange rates* or choose another source |
| The outcome of a currency is an SAP error | SAP refused the exchange rate (for example because of the user's authorizations) | Read the error; check the user's SAP authorizations on exchange rates |
| The automatic update does not start | It is turned off, or the technical SAP user is missing | Turn it on in *Settings › Exchange rates* and set the technical user in *Settings › SAP* |
| The program asks to install WebView2 | Microsoft Edge WebView2 Runtime is missing | Accept the suggested download, or install it from the Microsoft website |

## 11. Support

For licenses: [license@xeisrl.com](mailto:license@xeisrl.com). For support:
[info@xeisrl.com](mailto:info@xeisrl.com). In your request, state the program version (*About* menu) and describe the
problem.
