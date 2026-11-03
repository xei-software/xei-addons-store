---
title: XEI Rate Updater for SAP Business One – Installation, first start, license and scheduled update
description: How to install XEI Rate Updater for SAP Business One, connect it to SAP Business One, activate the license and schedule the daily exchange rate update.
lang: en
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater for SAP Business One – Installation, first start, license and scheduled update

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later, with the Service Layer |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA a test during installation is recommended) |
| System | Windows 10 and 11, Windows Server 2016 and later, 64-bit; Microsoft Edge WebView2 Runtime |
| Network | internet access to the chosen rate source |
| Program languages | Italian, English, German, French, Spanish, Turkish |

## Installation

1. Download the program zip file from the download page.
2. Extract the folder from the zip file to the PC, for example to `C:\XEI\RateUpdater`.
3. Start **XEI.RateUpdater.exe**. The program already contains .NET. It requires **Microsoft Edge WebView2 Runtime**,
   which is usually already there: if it is missing, the program says so and offers to download it.

The program has no setup. Settings and history are stored in the Windows data folder shared by all users of the PC.
To update the program, replace the folder with the new one: settings and history are kept.

## First start

When the program opens for the first time, the **First start** page appears, with the first-start code already filled in.

1. **SAP connection**: *Service Layer address* and *SAP companies*; then **Test the connection**.
2. **Sign-in and first administrator**:
   - *Operator sign-in*: **Each person's SAP user** or **Own users and technical SAP user**;
   - *SAP user of the first administrator* (for example `manager`);
   - *Technical SAP user* and password: they are needed for the automatic update. A dedicated user is best, with only
     the permission to write exchange rates.
3. **Save and restart**.

Afterwards, the same settings are in **Settings › SAP**. The rate source and the automatic update are in
**Settings › Exchange rates**.

## License

The program works with a **license code** issued by XEI.

| Scope | Applies to |
|---|---|
| Single company | one SAP database |
| Server | all the companies of the SQL Server or SAP HANA instance |
| Free | not tied to a database |

- **Trial**: 30 days, with the scope Free.
- **License** menu: status, expiry and scope. Paste the code received from XEI into **Enter a license code**: it takes
  effect immediately, without restarting.
- For a per-company or per-server license the program must be connected, read-only, to the license database
  (*Settings › License*, **Test connection**): there and on the License page the company and server codes appear, to be
  sent to [license@xeisrl.com](mailto:license@xeisrl.com).

## Scheduled update with Windows

This way the exchange rates are updated every day even with the program closed.

1. Set the **technical SAP user** (Settings › SAP).
2. In Windows open **Task Scheduler** and create a basic task, for example every day at 7:00.
3. Action **Start a program**: `XEI.RateUpdater.exe` in the program folder, with the argument `aggiorna`.
4. In the task properties choose **Run whether user is logged on or not**.

The command updates today's exchange rates and closes without a window; the run appears in the **History**. With
several companies add `--societa <database SAP>` (the SAP database), one task for each company. Result for Task Scheduler:
**0** succeeded, **1** failed or with a refused currency, **2** wrong arguments.

Alternatively, with the program open, just turn on **Automatic update** in *Settings › Exchange rates*.

## Support

For licenses: [license@xeisrl.com](mailto:license@xeisrl.com). For support:
[info@xeisrl.com](mailto:info@xeisrl.com). In your request, state the program version (*About* menu) and describe the
problem.
