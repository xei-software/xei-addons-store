---
title: XEI.ContoLavoro – Installation, License and Menus
description: How to install XEI.ContoLavoro, activate the license and find the menus.
lang: en
prodotto: XEI.ContoLavoro
versione: 1.2.1
stato: approvato
---

# XEI.ContoLavoro – Installation, License and Menus

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA, a test during installation is recommended) |
| System | Microsoft .NET Framework 4.8 on the SAP client PC |
| Program languages | Italian, English, German, French, Spanish, Turkish |

## Installation

1. Download the `XEI.ContoLavoro.zip` package.
2. In SAP Business One open the **Extension Manager**, import the package and assign it to the company.
3. On first start the add-on creates tables, fields, the Subcontracting Job object and the formatted search of the
   subcontractor vendor on the warehouse. SAP shows the message *"The database structure has been modified..."*:
   answer **Yes** and wait for it to finish before using the client.

Every update of the add-on is installed the same way.

Before creating jobs, define the numbering series of the Subcontracting Job, as for SAP documents: *Modules › Administration › System Initialization › Document Numbering*, item **Commessa terzista** (Subcontracting Job) at the bottom of the list. Without a series, when you open *Subcontracting Job* the add-on tells you to define it.

After installation: fill in the **Configuration**, then in SAP link each subcontractor warehouse to its vendor
(*Fornitore terzista* (Subcontractor vendor) field of the warehouse master data) and mark the subcontracting items
(user manual, chapters 3 and 6).

## License

The add-on works with a **license code** issued by XEI.

- **Trial**: after requesting the trial you receive by email a **trial code**, valid for 30 days from sending in any
  company.
- **Purchase**: you send XEI the two codes of the **Licenza** (License) window and receive the license code.

The **Licenza** (License) window:

- Without a valid code the add-on is **locked**: its menu contains only *Informazioni* (About) and *Licenza*
  (License), and at startup the **Licenza** window opens by itself with the status and the reason.
- The window shows the **company code** and the **server code**: to purchase the license, with *Copia* (Copy) you
  send them to [license@xeisrl.com](mailto:license@xeisrl.com).
- An SAP **superuser** pastes the code received into *Inserisci un codice di licenza* (Enter a license code) and
  presses *Salva codice* (Save code): the add-on is unlocked immediately, without restarting SAP.
- The trial code is valid in any company. The license code is valid for the company (database) or the server of the
  codes sent.
- The same window opens at any time from the *Licenza* menu: status, expiry date, number and scope of the license.

## Menus

The items are in **XEI-Addon › Subcontracting**. The **Subcontracting** submenu also appears in the SAP module chosen
in Configuration (*Purchasing* or *Production*).

| Item | Function |
|---|---|
| Subcontracting Job | opening, search and creation of Subcontracting Jobs (user manual, chapters 4 and 5) |
| Create Jobs from Production Orders | Subcontracting Jobs from the external processing of production orders (chapter 6) |
| Receipt from Subcontractor | receipt of the products of a subcontractor's delivery note across several Subcontracting Jobs (receipt of the products and issue of the components) |
| Mass Component Transfer | shipment of the components for several Subcontracting Jobs; can be disabled in Configuration (chapter 9) |
| Component Transfer Between Jobs | moves the stock already at the subcontractor from one Subcontracting Job to another (chapter 9) |
| Mass Closing of Product Goods Receipts | closes the goods receipts of the products that are still open (chapter 9) |
| Subcontractor Processing Prices | processing prices by subcontractor and product (chapter 9) |
| Configuration | options of the add-on (chapter 3) |
| Informazioni (About), Traduzioni (Translations), Licenza (License) | common items of XEI add-ons; Licenza: status and license code |
