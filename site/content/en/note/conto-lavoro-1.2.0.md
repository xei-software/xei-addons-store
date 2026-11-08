---
title: XEI.ContoLavoro 1.2.0 – Release notes
description: Features and corrections of XEI.ContoLavoro 1.2.0 for SAP Business One.
lang: en
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro 1.2.0 – Release notes

## Features of this version

- In the «Create Jobs from Production Orders» list, with the «Also show rows that are not ready» check box, the processing that cannot become a Subcontracting Job also appears, with the reason and what to do
  in the «Reason / warnings» column.
- When you save a bill of materials, a warning reports the codes to correct in the «Lavorazione terzista»
  (Subcontractor processing) field: resources, codes that are not items, items without «Conto lavoro»
  (Subcontracting), processing that is not a line of the bill of materials, components with backflush issue.
- XEI license with the **Licenza** (License) window in the add-on menu: status, company and server codes, code entry;
  30-day free trial.

## Corrections in this version

- An interrupted Subcontracting Job does not prevent creating another Subcontracting Job from the same production order
  line.
- Backflush components linked to an external processing are not sent to the subcontractor and the production order
  issues them only once.
- Without the numbering series of the Subcontracting Job, opening *Subcontracting Job* the add-on tells where to define it.
- The mass transfer of components is enabled in the default configuration; with the option off, the menu item warns that the function is disabled.
- The Subcontracting Jobs created from production orders use the default price list for jobs (Configuration › General): without it, «Create Jobs» asks you to enter it.
- In the «Create Jobs from Production Orders» list the rows can be selected and the vendor can be changed.
