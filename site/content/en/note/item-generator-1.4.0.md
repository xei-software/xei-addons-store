---
title: XEI.ItemGenerator 1.4.0 – Release notes
lang: en
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Release notes

## Features of this version

- **Variant inheritance as a proposal.** With *Inherit variants* the options chosen on a previous level are proposed
  and can be changed on the level that inherits them. The right-click menu offers **Back to the proposed options**.
- **Force inheritance.** Option on base values: it imposes the choice made on the previous level, which cannot be
  changed on the value.
- **User table and user field on variants.** In *Variants and Options* you set a user table and an item user field:
  when items are created, the chosen options are added to the table and copied to the field.
- **Generate Items.** The variants panel shows the variants of the value selected in the tree; a check box turns on
  the full view by level.
- **List of items to generate.** With the setting *Add to list clears the list of items to generate first* (on by
  default) the list contains only the last selection; with the setting off, items accumulate.
- **Numbered menus.** The Code Configurator entries are numbered 0 to 7 in working order: Settings, Base Definition,
  Variants and Options, Variant Structures, Generate Items, Consistency Check, Check Configuration, Excel Import /
  Export.
- **Sub-level with choose-from list.** In *Base Definition* the Sub-level column is filled from the choose-from list
  of bases, and the link arrow opens the linked base. A code typed by hand that is not a base is rejected.
- **Check Configuration and Excel** cover inheritance and the user tables and fields of variants.
- **Windows** with compact headers, in the SAP Business One style.
- **Program languages**: Italian, English, German, French and Spanish.

## Installation

- Requires XEICore 1.1.1, included in the package.
- On first start the add-on sets up its data structure by itself.
