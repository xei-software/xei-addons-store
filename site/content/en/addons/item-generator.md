---
title: XEI.ItemGenerator – Item Code Configurator
description: Create items in SAP Business One with code, descriptions, data, price and bill of materials built from rules you define.
lang: en
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator

**Item code configurator for SAP Business One.** Choose the product's characteristics
and the add-on creates the item in Item Master Data with code, descriptions, data,
price and bill of materials already filled in.

## Description

Companies that sell products in many combinations (sizes, finishes, colors,
accessories) waste time creating one item per combination by hand and risk different
codes and descriptions for the same product.

With XEI.ItemGenerator you define the rules once and the add-on builds the items:

- the **code** is made of the values chosen level by level (for example
  `PE` wall cabinet → `MU` wall-mounted → `070` height 70 cm = `PEMU070`), plus a
  sequence number that tells the variants apart;
- **variants** (for example color or finish) have their own options, which can be
  inherited from the previous levels;
- the item's **descriptions, groups, units of measure, properties, dimensions, weight
  and price** are derived from the chosen values and options;
- the **bill of materials** is built from the components of each value and option.

If a combination already exists, the add-on finds the existing item instead of
creating a duplicate.

## Main features

- **Definition of bases, variants and structures** with the add-on's master data in SAP.
- **Item generation** in a resizable window with the code tree and the variant tree;
  SAP stays usable while the window is open.
- **Configure Item from sales quotations and sales orders**: right-click the document
  row, build the item and put it in the row.
- **Generate Similar Items** from the master data of an already generated item: just
  change an option.
- **Description formula** to build the description, the extended description and the
  foreign name.
- **Configuration check**, listing the errors and opening the record to correct directly.
- **Excel import and export** of the configuration, also to copy it to another company.
- Dedicated **authorizations** in SAP General Authorizations.
- **Picture thumbnail** of the item in Item Master Data.

## Requirements

| | |
|---|---|
| SAP Business One | 10.0 or later |
| Database | Microsoft SQL Server or SAP HANA |
| Program languages | Italian, English, German, French, Spanish |
| System | Microsoft .NET Framework 4.8 on the SAP client PC |
| Installation | SAP Business One Extension Manager |
| License | XEI license code, entered in the add-on's **License** menu (30-day free trial) |

## Current version

**1.4.0** – see the [release notes](../../manuali/en/itemgenerator/note-rilascio-1.4.0.md).
