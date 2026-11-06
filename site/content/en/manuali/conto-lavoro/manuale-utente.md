---
title: XEI.ContoLavoro – User Manual
description: How to manage Subcontracting Jobs, component shipments, product receipts and subcontracting from production orders with XEI.ContoLavoro.
lang: en
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – User Manual

Installation, license and menus are also described in the
[installation guide](installazione.md).

## 1. What the add-on does

XEI.ContoLavoro manages the processing entrusted to **subcontractors** (outside suppliers) who receive components
from the company, process them and return a finished or semi-finished product. For each processing job a
**Subcontracting Job** is opened that keeps together:

- the **products** to be obtained, with their bill of materials (components to ship and processing to pay for);
- the **purchase order** to the subcontractor, automatically aligned with the Subcontracting Job;
- the **component shipments** to the subcontractor's warehouse, the **returns** and the **scrap**;
- the **receipt** of the products: goods receipt of products and processing, goods issue of the consumed components,
  receipt from production for products that come from a production order (chapter 6);
- the real-time situation: how much has been shipped and used, what remains at the subcontractor and what is missing.

The Subcontracting Job closes by itself when all products have been received and no components remain at the
subcontractor.

### Highlights

- Header like an inventory transfer, with warehouses propagated to the rows and the subcontractor warehouse
  protected after the first movements.
- Batches and serial numbers chosen in the add-on: proposal from the Subcontracting Job's batches at the subcontractor
  (traceability) and FEFO, editable by hand; batch of the incoming product from a configurable SQL script; product
  receipt in a single transaction.
- Documents folder with all linked documents, grouped and ready to open.
- Product costs recalculated at every save; purchase order aligned automatically.
- Subcontracting Jobs from production orders, mass transfer and transfer between jobs, mass closing of goods receipts.
- Same behavior on SQL Server and SAP HANA; translatable texts.

## 2. Installation and menus

### Installation

- The `XEI.ContoLavoro.zip` package is imported in the Extension Manager of SAP Business One.
- On first start the add-on creates tables, fields, the object (UDO) `XEI_CL_COMMESSA` and the formatted search of
  the subcontractor vendor on the warehouse. SAP asks you to confirm that *"the database structure has been
  modified"*: answer and wait for it to finish before using the client.

### Menus

**Modules › Administration › Add-Ons › XEI-Addon › Subcontracting**:

| Item | Function |
|---|---|
| Subcontracting Job | opening, search and creation of Subcontracting Jobs |
| Create Jobs from Production Orders | Subcontracting Jobs from the external processing of production orders (chapter 6) |
| Receipt from Subcontractor | a subcontractor's delivery note with products of several Subcontracting Jobs: you choose the vendor, enter the quantities received on the open products of its Subcontracting Jobs (*Propose* = open quantity) and *Post* performs the product receipt job by job, with receipt of the products and issue of the components |
| Mass Component Transfer | shipment of components for several Subcontracting Jobs (enabled with the related option) |
| Component Transfer Between Jobs | moves the stock already at the subcontractor from one Subcontracting Job to another |
| Mass Closing of Product Goods Receipts | closes the goods receipts of the products that are still open |
| Subcontractor Processing Prices | processing prices by vendor and product |
| Configuration | options of the add-on |
| Informazioni (About), Traduzioni (Translations), Licenza (License) | items common to the XEI add-ons; Licenza: status and license code |

The same items, except *Configuration*, *Informazioni*, *Traduzioni* and *Licenza*, are also in the SAP module chosen
in Configuration (chapter 3), in the chosen position: **Modules › Purchasing - A/P › Subcontracting** (default) or
**Modules › Production › Subcontracting**.

### License

The add-on works with a **license code** issued by XEI. After requesting the trial you receive by email a **trial
code**, valid for 30 days from sending in any company; to purchase, you send XEI the two codes of the **Licenza**
(License) window and receive the license code.

- Without a valid code the add-on is **locked**: its menu contains only *Informazioni* (About) and *Licenza*
  (License), and at startup the **Licenza** window opens by itself with the status and the reason.
- The window shows the **company code** and the **server code**: to purchase the license, with *Copia* (Copy) you send
  them to [license@xeisrl.com](mailto:license@xeisrl.com).
- An SAP **superuser** pastes the code received into *Inserisci un codice di licenza* (Enter a license code) and
  presses *Salva codice* (Save code): the add-on is unlocked immediately, without restarting SAP.
- The license code is valid for the company (database) or for the server of the codes sent.
- The same window opens at any time from the *Licenza* menu: status, expiry date, number and scope of the license.

## 3. Configuration

The options are set in a form with folders (the *Batches* folder is described in chapter 7). The options apply to the
whole company; forms that are already open use them when they are opened again.

![Prices](../../_img/contolavoro/11_config_prezzi.png)

*Prices*

![Inventory](../../_img/contolavoro/12_config_magazzino.png)

*Inventory*

| Option | Effect | Default |
|---|---|---|
| **General** | | |
| Source purchase order | field to link the Subcontracting Job to the purchase order it comes from | No |
| Source sales order | sales order column on the product rows | No |
| Products without bill of materials | allows products without a bill of materials: it is composed by hand | No |
| Close the product goods receipt | after the product receipt the goods receipt of the product is closed (it is not invoiced) | No |
| Recalculate the product goods receipt price | if the processing price changes, updates the goods receipt of the product | No |
| Vendor quotations from production orders | links the vendor quotations when creating from production orders | No |
| Mass transfer | enables the menu item | No |
| Subcontractor BOM | shows the "Subcontractor BOM" column in the bill of materials | Yes |
| Vendor agreements | processing prices from the agreements (SQL Server only) | No |
| Default price list | cost price list proposed on new Subcontracting Jobs | – |
| Menu Also in SAP Module | module with the *Subcontracting* submenu: Purchasing - A/P or Production | Purchasing - A/P |
| Position in Module Menu | at the bottom, at the top or after an item of the module | at the bottom |
| **Prices** | | |
| Processing / component price editable | prices editable in the bill of materials of the Subcontracting Job | No |
| Processing / component price from the bill of materials | the bill of materials price as first choice (component: production orders only) | No |
| Split the processing cost | splits the total cost across the products (from production orders only) | No |
| Do not block with zero prices | the product receipt is allowed even with zero prices | No |
| Revalue components | revaluation of the components in the production issue (perpetual inventory) | No |
| **Inventory** | | |
| Item default warehouse | the component rows start from the item's default warehouse | Yes |
| Stock as shipped | for the components indicated, the stock at the subcontractor counts as shipped | No |
| Components per row | components kept separate by product | No |
| Variable requirement | splits the shipped quantity across the products | No |
| Transfer requests | component shipment with an inventory transfer request instead of the inventory transfer | No |
| Pick list | also creates the pick list (enables the requests) | No |
| **Series and Reasons** | | |
| Series | purchase order, goods receipts of products and processing, transfers | SAP default |
| Transport Reasons | for transfers, order, goods receipt, issues, receipts (if the company uses transport reasons) | – |
| **Batches** | | |
| Incoming batch script | SQL with {ItemCode}, {WhsCode}, {DocEntry} that returns the batch of the received product (see chapter 7) | job-sequence number |

## 4. The Subcontracting Job

### Header

The header is organized like that of the inventory transfer: on the left vendor, vendor reference, project and linked
orders; on the right numbering, status, dates, cost price list and the two warehouses.

- **Vendor**: when chosen, it proposes the user's warehouse and the **subcontractor warehouse** linked to the vendor
  (*Fornitore terzista* (Subcontractor Vendor) field of the warehouse master data) or the one marked as default.
- **From Whse**: the company's warehouse; the components leave from here, the products come back here and the rows of
  the purchase order are created on this warehouse.
- **To Subc. Whse**: it can be changed only as long as the Subcontracting Job has no component movements; after that
  the field is disabled and saving rejects the change anyway.
- When a header warehouse is changed, as in the inventory transfer, you are offered to copy it to the bill of
  materials rows **that have no movements yet**.

### Products

You choose the item (also several items at once from the list) and the quantity to produce: the bill of materials is
copied from SAP and scaled to one piece (taking into account the base quantity of the bill of materials). The columns
show quantity to produce, received, open quantity, cost of the components and of the processing.

### Bill of Materials

For each product: components (inventory items to ship) and processing (services paid to the subcontractor). With
**Edit Bill of Materials** you change warehouses and prices of the rows that have no movements yet; with SAP's *Add
Row* / *Delete Row* you add components and processing or remove those without movements. From the context menu of the
product row: **Rework** (the product goes back to the subcontractor as a component with the new processing) and
**Rebuild Bill of Materials** (replaces the bill of materials with the chosen components).

### Components

The components of all products grouped by item and warehouses: requirement, used, available in the company, stock in
the subcontractor's warehouse, requests and pick lists, shipped, remaining to ship, stock of the Subcontracting Job at
the subcontractor, returns and scrap. Movements are made with the buttons at the bottom of the Subcontracting Job:
**Send Components** and **Returns and Scrap** (*Return Components from Subcontractor*, *Transfer Scrap*, *Scrap Issue
at Subcontractor*). Each one opens a window with the quantities to move in the yellow cells: *Propose* fills them,
*Clear* empties them, and they can be changed by hand.

### Documents

All SAP documents linked to the Subcontracting Job, one per row in chronological order, with the link to open them;
*Show* filters by document type. Below, in *Document Lines*, the rows of the chosen document with batches, serial
numbers and bin locations.

## 5. Workflow

1. **Subcontracting Job**: vendor, warehouses, products and quantities; *Add*.
2. **Subcontractor Order**: the *Subcontractor Purchase Order* window creates the purchase order, with one row per
   product and one for each processing; if the order already exists, the button opens it. Later changes to the
   Subcontracting Job (new or deleted products, quantities, prices, dates) are carried over to the order when saving;
   rows already received change only in quantity.
3. **Send Components**: in the *Component Transfer* window the *To Ship* column proposes the quantity remaining to ship
   (it can be changed by hand); *OK* creates the inventory transfer to the subcontractor's warehouse. With the related
   option an inventory transfer request with a pick list is created.
4. **Receive Products**: in the *Product Receipt* window the *To Receive* column proposes the open quantity (it can be
   changed by hand) and *Movement Type* chooses between *Receive Products and Issue Components*, *Receive Products
   Only* and *Issue Components Only*; then *OK*. The following are created: goods receipt PO of the processing and of
   the products from the purchase order, goods issue of the components from the subcontractor's warehouse, receipts
   from production for the products from production orders (chapter 6).

> The product is received at full cost (components + processing); with the "Close the product goods receipt" option
> the goods receipt is closed and is not invoiced: the processing is invoiced.

If a component to be issued exceeds the stock of the Subcontracting Job at the subcontractor, you are asked whether to
issue the remaining stock (Yes / No / Yes to All).

## 6. Subcontracting from production orders

When some phases of a **production order** are carried out at subcontractors, the add-on creates the Subcontracting
Jobs from the rows of the production order. At every product receipt it issues to the production order the components
consumed by the subcontractor and, when all external processing has come back, it posts the receipt from production
of the finished product.

### Setup in SAP

> The external processing is a **non-inventory item** with the **Conto lavoro** (Subcontracting) field = Yes, not an
> SAP resource: a processing set up as a resource does not appear in the list of production orders.

| Where | What you set | In the example |
|---|---|---|
| Item Master Data of the processing item | non-inventory item, user field **Conto lavoro** (Subcontracting) = Yes; the **preferred vendor** is the subcontractor proposed in the list | `LAV-SALD` Frame welding, vendor `F-TER01`; `LAV-MONT` Axle assembly, vendor `F-TER02` |
| Bill of materials of the finished product | one row for each external processing, with the quantity per piece; on the rows of the components to send to the subcontractor the **Lavorazione terzista** (Subcontractor processing) field with the code of the processing and the **Manual** issue method | `CMP-01`, `CMP-02` → `LAV-SALD`; `CMP-03`, `CMP-04` → `LAV-MONT` |
| Bill of materials of the finished product | **Subcontractor BOM** = Yes if the finished product is complete when all external processing has come back: the add-on posts the receipt from production. With No you post the receipt from production yourself in SAP | `PF-100` = Yes |
| Warehouse master data of the subcontractor | **Fornitore terzista** (Subcontractor Vendor) field (chapter 4) | `T-TER01` → `F-TER01`; `T-TER02` → `F-TER02` |
| *Subcontractor Processing Prices* | price by subcontractor, finished product and processing (order in which the price is searched in chapter 9) | `F-TER01` / `PF-100` / `LAV-SALD` 12.00; `F-TER02` / `PF-100` / `LAV-MONT` 3.50 |

Backflush components linked to the processing are not sent to the subcontractor: the receipt from production issues
them from the warehouse of the production order row. The **Reason / warnings** column of the list reports it. The
other components of the bill of materials, which have no processing, stay as in any production order.

> **Check when saving the bill of materials.** When you save a bill of materials that has the **Lavorazione
> terzista** (Subcontractor processing) field filled in, the add-on checks the codes entered. If something is wrong,
> the warning *"Bill of materials PF-100, field "Lavorazione terzista":"* appears with one point for each case; the
> bill of materials remains saved.
>
> - Resource: *"LAV-SALD is a resource: the external processing must be created as a non-inventory item with "Conto
>   lavoro" = Yes, and the components must be linked to that code."*
> - Code that is not an item: *"LAV-SALD is not an item."*
> - Item without Conto lavoro: *"Item LAV-SALD does not have "Conto lavoro" = Yes in the item master data."*
> - Processing that is not a row of the bill of materials: *"LAV-SALD is not a row of the bill of materials: the
>   production order will not have the processing row and the subcontracting job cannot be created."*
> - Backflush components: *"Backflush components with processing LAV-SALD: they are not sent to the subcontractor
>   (they must use the manual issue method)."*

### Step-by-step example

The finished product `PF-100` Trolley has two external processing steps: the welding of the frame at `F-TER01`
«Example Subcontractor 1» and the assembly of the axles at `F-TER02` «Example Subcontractor 2». Each trolley has one
frame and two axles. Production order no. 500 is released for 100 trolleys in warehouse `01`:

| Row | Item | Quantity | Issue | Lavorazione terzista | Price |
|---|---|---|---|---|---|
| 1 | `LAV-SALD` Frame welding (processing) | 100 | | | 12.00 |
| 2 | `CMP-01` Tube (m) | 250 | Manual | `LAV-SALD` | 4.00 |
| 3 | `CMP-02` Plate | 400 | Manual | `LAV-SALD` | 1.50 |
| 4 | `LAV-MONT` Axle assembly (processing) | 200 | | | 3.50 |
| 5 | `CMP-03` Wheel | 400 | Manual | `LAV-MONT` | 5.00 |
| 6 | `CMP-04` Pin | 200 | Manual | `LAV-MONT` | 2.00 |
| 7 | `CMP-05` Screw | 1,600 | backflush | | |

| Step | SAP document created | Effect on the production order |
|---|---|---|
| 1. **Subcontracting › Create Jobs from Production Orders**: you select the two rows of production order 500 and press *Create Jobs* | no SAP document: Subcontracting Job 1001 (`F-TER01`, from `01` to `T-TER01`, product `LAV-SALD` 100, bill of materials `CMP-01` 2.5 and `CMP-02` 4 per piece) and Subcontracting Job 1002 (`F-TER02`, from `01` to `T-TER02`, product `LAV-MONT` 200, bill of materials `CMP-03` 2 and `CMP-04` 1 per piece) | none |
| 2. In each Subcontracting Job press *Subcontractor Order* and confirm the *Subcontractor Purchase Order* window | purchase order to `F-TER01`: `LAV-SALD` 100 × 12.00; purchase order to `F-TER02`: `LAV-MONT` 200 × 3.50 | none |
| 3. In each Subcontracting Job press *Send Components* and, with the proposed quantities, *OK* | inventory transfer from `01` to `T-TER01`: `CMP-01` 250, `CMP-02` 400; from `01` to `T-TER02`: `CMP-03` 400, `CMP-04` 200 | none |
| 4. 60 frames come back: in Subcontracting Job 1001 press *Receive Products*, in the *Product Receipt* window enter 60 in *To Receive* and press *OK* | goods receipt PO from the order: `LAV-SALD` 60 × 12.00; issue for production from `T-TER01`: `CMP-01` 150, `CMP-02` 240 | components of rows 2 and 3 issued; no receipt: the axles are missing, and a message says so (*"Production order 500: the finished product will be received into stock when processing LAV-MONT also comes back."*) |
| 5. 100 axles come back: Subcontracting Job 1002, *Receive Products*, 100 in *To Receive*, *OK* | goods receipt PO `LAV-MONT` 100 × 3.50; issue for production from `T-TER02`: `CMP-03` 200, `CMP-04` 100; receipt from production `PF-100` **50** | 60 frames and 100 axles are enough for 50 trolleys: 50 completed; SAP backflushes `CMP-05` 800 |
| 6. Another 100 axles come back: Subcontracting Job 1002, *Receive Products*, 100 in *To Receive*, *OK* | goods receipt PO `LAV-MONT` 100; issue for production `CMP-03` 200, `CMP-04` 100; receipt from production `PF-100` **10** | 60 completed, the others wait for the frames (*"Production order 500: 10 pieces of the finished product received; the others will be received when processing LAV-SALD also comes back."*); Subcontracting Job 1002 closes by itself |
| 7. The last 40 frames come back: Subcontracting Job 1001, *Receive Products*, 40 in *To Receive*, *OK* | goods receipt PO `LAV-SALD` 40; issue for production `CMP-01` 100, `CMP-02` 160; receipt from production `PF-100` **40** | 100 completed; Subcontracting Job 1001 closes by itself. You close the production order yourself in SAP |

> The receipt from production is valued at the cost of the external processing per piece: for each processing,
> components and processing price, multiplied by the quantity per piece. In the example one trolley is worth
> (2.5 × 4.00 + 4 × 1.50 + 12.00) + 2 × (2 × 5.00 + 1 × 2.00 + 3.50) = 28.00 + 31.00 = **59.00**.

### Special cases

- **Several production orders**: the rows with the same vendor and the same return warehouse (*Return Whse* column)
  go into the same Subcontracting Job, one product per row; with different return warehouses, different
  Subcontracting Jobs are created.
- **Subcontractor services**: a non-inventory component with **Lavorazione terzista** (Subcontractor processing) (for
  example a test) becomes a processing of the Subcontracting Job, with one more row in the order to the subcontractor.
- **Subcontractor BOM = No**: the add-on posts the goods receipt of the processing and the issue of the components;
  you post the receipt from production yourself in SAP, for example after an internal assembly.
- **Receipts from production posted in SAP** on the same production order: the add-on subtracts them, the finished
  product is not received twice.
- **Interrupted Subcontracting Job**: if you interrupt a Subcontracting Job, the processing goes back to the list and
  you can create another one.
- **Backflush components**: the backflush components linked to the processing are not sent to the subcontractor; the
  **Reason / warnings** column reports it.
- **Bill of materials of the Subcontracting Job**: for products from production orders it cannot be changed; you change
  the processing price (*Proc. Cost* column), which is carried over to the order to the subcontractor when saving.
  With the *Split the processing cost* option, the *Total Proc. Cost* of the header is split across the products in
  proportion to the quantity.
- The *Close the product goods receipt* option does not apply to Subcontracting Jobs from production orders: the goods
  receipt of the processing remains open, to be invoiced.
- **Vendor quotations**: with the *Vendor quotations from production orders* option, *Vendor Quotation* links a
  quotation row to the row, with its vendor, price and delivery date; the quotation rows not chosen are closed.

### Why a production order does not appear in the list

The list shows the processing ready to become a Subcontracting Job. Turn on **Also show rows that are not ready**: the
other ones appear too, with the reason and what to do in the **Reason / warnings** column. Rows that are not ready
cannot be selected; if you click their selection box, the reason also appears in the status bar.

| Reason (example on screen) | What to do |
|---|---|
| Already in subcontracting job no. 1001. | nothing: open the Subcontracting Job from the *Job* column |
| LAV-SALD is a resource: the external processing must be created as a non-inventory item with "Conto lavoro" = Yes, and the components must be linked to that code. | create the processing item and enter its code in **Lavorazione terzista** (Subcontractor processing) on the components |
| The components refer to processing LAV-SALD, which is not an item. | correct **Lavorazione terzista** on the components or create the item |
| Item LAV-SALD does not have "Conto lavoro" = Yes in the item master data. | set **Conto lavoro** (Subcontracting) = Yes in the item master data |
| The production order has no row for processing LAV-SALD: add it to the production order (or to the product bill of materials). | add the row to the production order, or to the bill of materials for the next production orders |
| No components to send: on the component rows enter "Lavorazione terzista" = LAV-SALD and the manual issue method. | fill in the components to send, with the Manual issue method |
| Production order not released: release it in SAP. | release the production order |

A processing set up as an SAP resource is a frequent cause: the external processing must be created as a
non-inventory item with **Conto lavoro** (Subcontracting) = Yes.

On the rows that are ready, the same column gives the warnings that do not prevent selection:

| Warning | What to do |
|---|---|
| Backflush components with this processing: they are not sent to the subcontractor (they must use the manual issue method). | if they must be sent, set the Manual issue method |
| Enter the vendor. | choose the vendor in the *Vendor* column |
| Vendor F-TER01 has no linked subcontractor warehouse. | link the subcontractor's warehouse to the vendor (**Fornitore terzista** (Subcontractor Vendor) field): without it, the Subcontracting Job is not created |

## 7. Batches, serial numbers and bin locations

For transfers, returns, scrap and the issue of components in the product receipt, batches and serial numbers are
chosen in a window of the add-on, **before** the documents are created. All documents are then created in a single
operation.

- **Automatic proposal**: from the subcontractor's warehouse (component issue, return, scrap) first the batches
  **shipped to that Subcontracting Job** ("Of the Job" column, taken from SAP's batch transaction log), then by expiry
  date (FEFO); from the company's warehouse by expiry date (FEFO).
- **Manual choice**: the "To Use" column can be edited; the quantity is limited to the stock of the batch (net of
  other rows on the same batch) and to 1 for serial numbers. *Propose* makes the proposal again, *Clear* empties
  everything. Confirmation is possible only when each row has exactly the requested quantity.
- Only **released** batches and serial numbers are proposed (not locked or not accessible).
- Inventory transfer requests do not move batches: no selection opens for them.

### Batch of the incoming product

The batch of the received product is calculated by a configurable **SQL script** (Configuration › Batches), with three
fixed parameters: `{ItemCode}` item, `{WhsCode}` receiving warehouse, `{DocEntry}` Subcontracting Job. The default
script returns the Subcontracting Job number + a sequence number (e.g. `20160256-1`); *Test* runs it with test data.
The batch created appears in the message at the end of the product receipt.

![Incoming product batch script](../../_img/contolavoro/19_config_lotti.png)

*Incoming product batch script*

### Draft documents

The document is created as a draft, to be completed in the SAP form, with warehouses with **bin locations**, incoming
products with **serial numbers**, an empty batch script or one without result, and in the mass transfer. You complete
the document and press *Add*: the add-on deletes the draft and continues.

## 8. Returns and scrap

- **Returns and Scrap › Return Components from Subcontractor**: quantity in *To Return* (*Propose* = stock of the
  Subcontracting Job at the subcontractor), then *OK*: transfer from the subcontractor's warehouse to the company's
  warehouse.
- **Returns and Scrap › Transfer Scrap**: quantity in *To Scrap*; moves the scrap from the subcontractor to a warehouse
  of your choice.
- **Returns and Scrap › Scrap Issue at Subcontractor**: in the *Scrap Issue* window, goods issue of the scrap directly
  from the subcontractor's warehouse.

Scrapped components go back into the quantity remaining to ship.

## 9. Service functions

### Subcontracting Jobs from production orders

Lists the external processing of released production orders that is ready to become a Subcontracting Job, and creates
**one Subcontracting Job per vendor and return warehouse**. With *Also show rows that are not ready* it explains why a
processing is not ready. Setup, complete example and special cases in chapter 6.

### Mass Component Transfer

Analyzes the open Subcontracting Jobs (filters by dates, vendor, component) and proposes the components with a
quantity remaining to ship, respecting the availability shared among the Subcontracting Jobs if the company blocks
negative stock. Creates one transfer per vendor (as a draft if batches or bin locations are needed). Rows with a
missing subcontractor warehouse or one equal to the source warehouse are excluded and reported.

### Component Transfer Between Jobs

Moves the stock already at the subcontractor from one Subcontracting Job to another without inventory movements (only
a record). For this reason it is possible only between **open** Subcontracting Jobs with the **same subcontractor
warehouse**: the list proposes only those; with different warehouses the operation is blocked and the goods must be
returned and shipped again. The stock is read again at the moment of confirmation.

### Mass closing of product goods receipts and processing prices

*Mass Closing of Product Goods Receipts* lists the goods receipts of the products that are still open and closes the
chosen ones. *Subcontractor Processing Prices* is the table of processing prices by subcontractor and product.

Order in which the price of a processing is searched: vendor agreements (option, SQL Server only), prices by
subcontractor, bill of materials (option), SAP vendor price, price list of the Subcontracting Job.

## 10. Data, fields and movement types

| Table | Content |
|---|---|
| `@XEI_CL_OCNT` | Subcontracting Job header (UDO `XEI_CL_COMMESSA`, with series) |
| `@XEI_CL_CNT1` | products |
| `@XEI_CL_CNT2` | bill of materials (components and processing) |
| `@XEI_CL_PRZLAV` | processing prices by subcontractor and product |
| `@XEI_CL_TRCOMM` | transfers between Subcontracting Jobs |

Fields on the SAP tables (prefix `XEI_CL_`):

| Field | Tables | Content |
|---|---|---|
| `U_XEI_CL_ENTRY` | document rows | Subcontracting Job (DocEntry) |
| `U_XEI_CL_LINENUM` | document rows | product or bill of materials row |
| `U_XEI_CL_TYPE` | document rows | movement type (table below) |
| `U_XEI_CL_TXT`, `U_XEI_CL_OPIT`, `U_XEI_CL_ITEM`, `U_XEI_CL_WKEY`, `U_XEI_CL_ENBL` | document rows | text, reference item and production order, usable quotations |
| `U_XEI_CL_ICNT` | items | subcontracting item |
| `U_XEI_CL_TERZF`, `U_XEI_CL_DFTR` | warehouses | subcontractor vendor of the warehouse, default subcontractor warehouse |
| `U_XEI_CL_DISTTERZ` | bills of materials | Subcontractor BOM (receipt from production from production orders) |
| `U_XEI_CL_ILAV` | bill of materials and production order rows | processing to which the component belongs |

If the company uses them, the add-on also fills in the commercial code, transport reason, freight terms and carrier of
the documents.

| Type | Document | Meaning |
|---|---|---|
| EMP | purchase order, goods receipt PO | product |
| OAL | purchase order, goods receipt PO | processing |
| UMC | goods issue (issue for production if from a production order) | consumed components |
| TSO | inventory transfer or request | components sent to the subcontractor |
| TSI | inventory transfer | component return |
| TSS | inventory transfer | scrap transfer |
| UMR | goods issue | scrap at the subcontractor |
| EPR | receipt from production | finished product of the production order (chapter 6) |

Canceled documents are excluded from the calculations and returns are subtracted row by row.

## 11. Languages

The add-on follows the language of the SAP client. **Italian** (base language), **English**, **German**, **French**,
**Spanish** and **Turkish** are available: menus, forms, columns, buttons, messages and remarks of the documents
created. With a language that is not provided, Italian is used.

| SAP language | Add-on texts | Commessa terzista | Terzista |
|---|---|---|---|
| Italian (Italy) | Italian | Commessa terzista | terzista |
| English (United States / United Kingdom) | English | Subcontracting Job | subcontractor |
| German | German | Lohnfertigungsauftrag | Lohnfertiger |
| French | French | Ordre de sous-traitance | sous-traitant |
| Spanish (Spain / Latin America) | Spanish | Orden de subcontratación | subcontratista |
| Turkish | Turkish | Fason iş emri | fasoncu |

The terms follow those of SAP Business One in the same language (for example *Vendor*, *Posting Date*, *Inventory
Transfer*, *Bill of Materials*, *Batch* in English; *Tedarikçi*, *Kayıt tarihi*, *Stok nakli*, *Ürün ağacı*, *Parti*
in Turkish).

### Changing the language

1. **Administration › Setup › General › Users**, *Display* tab, *Language* field, then *Update*.
2. SAP warns that all open windows will be closed: answer *Yes*.
3. The add-on reloads the texts by itself and recreates the menus in the new language: there is no need to restart
   it.

### Customizing the texts

Each text can be changed for the individual customer from the **Traduzioni** (Translations) menu of the add-on or
with the right mouse button on the forms (*Modifica testo…* (Edit text…), *Testi di questa form…* (Texts of this
form…)). The `XEI_TEXTS` authorization is required (superusers always have it). Customizations are kept when the
add-on is updated.

Texts saved in the database by SAP remain in Italian, for example the descriptions of the user fields and the title of
the *Prezzi lavorazioni terzisti* (Subcontractor Processing Prices) table. The *Informazioni*, *Traduzioni* and
*Licenza* items of the framework, with their windows, are in Italian in all languages.
