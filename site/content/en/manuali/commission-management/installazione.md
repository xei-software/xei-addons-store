---
title: XEI.CommissionManagement – Installation, License, Menus and Authorizations
description: How to install XEI.CommissionManagement, activate the license, find the menus and assign the authorizations.
lang: en
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Installation, License, Menus and Authorizations

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA, a test during installation is recommended) |
| System | Microsoft .NET Framework 4.8 on the SAP client PC |
| Program languages | Italian, English, German, French, Spanish, Turkish |
| Mail | reachable SMTP mail server, only to send statements to agents by email (Configuration › Email) |

## Installation

1. Download the `XEI.CommissionManagement.zip` package.
2. In SAP Business One open the **Extension Manager**, import the package and assign it to the company.
3. On first start the add-on creates fields, tables, indexes and authorizations. Creating the fields on the document
   lines takes **a few minutes**: SAP shows the message *"The database structure has been modified... all open
   windows will be closed. Continue?"* several times: answer **Yes**.

Every update of the add-on is installed the same way.

After installation: fill in the **Configuration**, then the **Agents** (roles, superiors, percentages), then the
**Rules**. Only from then on do documents receive the percentages. Users who are not superusers must be given the
**authorizations** (below).

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

The items are in **XEI-Addon › Commissions**.

| Item | Function |
|---|---|
| Configuration | options (six tabs) and rule search order (user manual, chapter 5) |
| Agents | role, superiors, default %, % on invoicing, settlement, vendor, SAP user (chapter 6) |
| Percentage rules | % by customer, customer group, item, item group, price list (chapter 7) |
| Tiers and bonuses | bonuses on annual sales, if enabled in Configuration (chapter 15) |
| Check and assign % | comparison of documents with rules and bulk correction (chapter 9) |
| Commission calculation | calculation on invoices, down payment invoices and credit memos (chapter 10) |
| Calculated commissions | consultation, correction, recalculation, deletion (chapter 11) |
| Settlement | collected shares to settle, unpaid items to reverse (chapter 12) |
| Adjustments | manual amounts per agent and month, agent invoice drafts (chapter 13) |
| Commission statement | calculated, to settle, settled and adjustments; CSV, print/PDF, email (chapter 14) |
| Checks | issues to check (chapter 16) |
| Informazioni (About), Traduzioni (Translations), Licenza (License) | common items of XEI add-ons; Licenza: status and license code |

## Authorizations

In the SAP **General Authorizations** (Administration › System Initialization › Authorizations) the add-on creates
the **Provvigioni** (Commissions) node under *User Authorization*, with five sub-items. Superusers always have
everything; other users are assigned, for each item, *No Authorization*, *Read-Only* or *Full Authorization*.

![General Authorizations](../../_img/commissionmanagement/autorizzazioni.png)

*General Authorizations: the Provvigioni node with its five sub-items, for a user without authorizations.*

| Authorization | Read-only | Full |
|---|---|---|
| «Configurazione» (Configuration) | – | open and save the Configuration |
| «Agenti, regole e scaglioni» (agents, rules and tiers) | view | save agents, rules and tiers |
| «Controllo, calcolo e verifiche» (check, calculation and checks) | view Check, Calculation, Calculated commissions, Checks | apply the %, calculate, recalculate, save shares, delete |
| «Liquidazione, conguagli e bozze fatture» (settlement, adjustments and invoice drafts) | view Settlement and Adjustments | confirm settlements, save adjustments, post bonuses, generate drafts |
| «Estratto di tutti gli agenti» (statement of all agents) | see the statement of all agents (without it: only one's own) | also sending by email |

Without authorization the menu item answers in the status bar *"Function not allowed: requires the "…" authorization
(General Authorizations > Provvigioni)"*; with read-only access the window opens, but the buttons that make changes
answer *"Operation not allowed: requires full authorization on "…""*.

## Support

For licenses: [license@xeisrl.com](mailto:license@xeisrl.com). For support:
[info@xeisrl.com](mailto:info@xeisrl.com). In the request, state the add-on version (*Informazioni* (About) menu) and
a description of the problem.
