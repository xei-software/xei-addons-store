---
title: XEI.CommissionManagement – Sales commissions
description: Calculate and settle in SAP Business One the commissions of agents, zone managers, area managers and directors, from the rules to each agent's statement.
lang: en
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement

**Sales agent commissions in SAP Business One.** The percentages are set automatically on the document lines, the
add-on calculates the commissions, settles them as customers pay and prepares each agent's statement.

## Description

Calculating commissions by hand or in spreadsheets means going back over invoices, payments and agent agreements every
month, with the risk of errors and of statements that differ from what the ERP says.

With XEI.CommissionManagement everything stays in SAP Business One:

- each invoice line carries up to **four percentages**: agent, zone manager, area manager and director;
- the percentages come from the **rules** by customer, customer group, item, item group, price list, period and
  discount, or from the agent's default percentages, and can be corrected by hand;
- the commission is split into a share **on invoicing** and shares **on payment**, installment by installment or on
  the document total;
- the **settlement** proposes the paid shares and reverses those of installments that become unpaid;
- each agent's **statement** can be exported to CSV, printed to PDF or sent by email.

## Main features

- **Agents and hierarchy**: role, zone manager, area manager, director, default percentages, share on invoicing and
  settlement type for each sales employee.
- **Percentage rules** with a configurable search order, minimum discount and validity period, exportable and
  importable as CSV.
- **Percentages on sales documents** while they are filled in, with an estimate of the commission when saving and
  protection of lines corrected by hand.
- **Check and assignment of %**: compares the document percentages with the rules and corrects them in bulk.
- **Calculation** on A/R invoices, A/R down payment invoices and A/R credit memos, also automatically when the invoice
  is added.
- **Settlement** of paid shares, also in proportion to partial payments, with a closed period.
- **Adjustments**, **tiers and bonuses** on annual turnover and **draft invoices** of the agents.
- **Checks** for anomalies and dedicated **authorizations** in SAP General Authorizations.

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA, a test during installation is recommended) |
| Program languages | Italian, English, German, French, Spanish, Turkish |
| System | Microsoft .NET Framework 4.8 on the SAP client PC |
| Mail | reachable SMTP mail server, only to send statements to agents by email (Configuration › Email) |
| Installation | SAP Business One Extension Manager |
| License | XEI license code, entered in the add-on's **Licenza** (License) menu (30-day free trial) |

## Current version

**1.1.1** – see the [release notes](../../manuali/en/commissionmanagement/note-rilascio-1.1.1.md) and the
[user manual](../../manuali/en/commissionmanagement/manuale-utente.md).
