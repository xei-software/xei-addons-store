---
title: XEI.ContoLavoro – Subcontracting
description: Manages in SAP Business One the processing entrusted to subcontractors, from the order and the shipment of the components to the return of the finished product.
lang: en
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro

**Subcontracting in SAP Business One.** One Subcontracting Job for each processing keeps together the order to the
subcontractor, the components sent, the returns and the receipt of the finished product, with the situation always up
to date.

## Description

Following subcontracting by hand means keeping purchase orders, transfers and receipts aligned, and knowing at any
moment what is at each subcontractor. With XEI.ContoLavoro SAP Business One does it:

- for each processing a **Subcontracting Job** is opened with the products to be obtained and their bill of materials:
  components to send and processing to pay;
- the **purchase order to the subcontractor** is created from the Subcontracting Job and stays aligned with every
  change;
- the **components** are sent to the subcontractor's warehouse, with returns and scrap;
- the **receipt** records in a single operation the receipt of the product and of the processing and the issue of the
  components consumed;
- the Subcontracting Job shows at any moment what has been shipped, what has been used, what remains at the
  subcontractor and what is missing, and closes by itself when it is finished.

## Main features

- **Subcontracting Job** with Products, Bill of Materials, Components and Documents tabs: all the linked SAP documents,
  grouped and ready to open.
- **Subcontracting from production orders**: the external phases of a production order become Subcontracting Jobs, the
  components are issued at each return and the finished product enters the warehouse when all the processing has
  returned.
- **Batches and serial numbers** proposed from the Subcontracting Job's batches at the subcontractor and by expiry date,
  editable by hand; batch of the incoming product calculated by a configurable script.
- **Costs** of the products recalculated at every save, with the **processing prices** by subcontractor and product.
- **Mass transfer** of components, **transfer between Subcontracting Jobs** at the same subcontractor and **mass
  closing** of goods receipts.

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA, a test during installation is recommended) |
| Program languages | Italian, English, German, French, Spanish, Turkish |
| System | Microsoft .NET Framework 4.8 on the SAP client PC |
| Installation | SAP Business One Extension Manager |
| License | XEI license code, entered in the **Licenza** (License) menu (30-day free trial) |

## Current version

**1.2.0** – see the [release notes](../../manuali/en/contolavoro/note-rilascio-1.2.0.md) and the user manual.
