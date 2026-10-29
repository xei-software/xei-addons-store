---
title: XEI.CommissionManagement – User Manual
description: "Sales agent commissions in SAP Business One: configuration, rules, calculation, settlement, adjustments and statements."
lang: en
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement – User Manual

| | |
|---|---|
| SAP Business One | 10.0 or later |
| Database | Microsoft SQL Server or SAP HANA (on SAP HANA a test during installation is recommended) |
| Program languages | Italian, English, German, French, Spanish, Turkish |

## 1. What the add-on does

XEI.CommissionManagement calculates and settles **sales agent commissions** starting from the SAP Business One
documents. Each invoice line (and each down payment invoice or credit memo line) carries up to four
percentages: one for the document's **agent** and one for each of the agent's superiors, **zone manager**, **area
manager** and **director**. The add-on:

- **assigns the percentages** to the lines while the documents are being entered, based on rules by customer,
  customer group, item, item group, price list, period and discount (or on the agent's default percentages);
- **calculates** the commissions of the documents of a period and splits them into **shares**: one part accrues
  with the invoice, the rest with the payment (installment by installment or when the whole document is paid);
- **settles** the shares as SAP records the incoming payments, and **reverses** those of installments that turn
  out unpaid;
- produces for each agent the **statement** of what has been calculated, of what is still to be settled and of what
  is due in the period (settled amount plus manual **adjustments**), which can be exported to CSV for Excel, printed
  to PDF and sent by email to each agent;
- optionally (options in Configuration): estimates the commission when a document is saved, automatically
  calculates invoices as soon as they are added, protects percentages corrected by hand, settles partial payments,
  closes periods already delivered, calculates **bonuses** on annual sales, prepares the agents' **invoice
  drafts** and reports issues (**Checks**).

Everything is in SAP: user fields on sales employees and on document lines, user tables for rules,
commissions and adjustments, no external database. It works the same way on Microsoft SQL Server and SAP HANA; on SAP HANA a test during installation is recommended.

## 2. The concepts: beneficiaries, percentages, shares, settlement

### Who receives the commission (beneficiaries)

The document's **sales employee** is the agent. In the Agents window a **zone manager**, an **area manager** and
a **director** can be set for each sales employee: they are the other beneficiaries of that employee's documents.
Each one has their own percentage on every line (the four columns *Provv. % agente / capo zona / capo area /
direttore* (commission % agent / zone manager / area manager / director)).

- A sales employee receives commissions only if they have a **role** (Agent, Zone manager, Area manager,
  Director). A sales employee without a role is "not managed": their documents generate no commissions and, if they
  are set as someone's superior, their share is not calculated.
- The "Agent" role applies to whoever appears as sales employee on the documents; "Zone manager", "Area manager"
  and "Director" are the titles with which a sales employee can be chosen as a superior. Someone with a superior
  role can still have documents of their own: on those, they are the agent.

### The percentages

The percentages of a line come from the **rules** (chapter 7) or, if no rule applies, from the **default
percentages** of the document's agent (chapter 6). They are assigned automatically while the document is entered
(chapter 8), can be corrected by hand and can be checked and fixed in bulk before the calculation
(chapter 9).

### The shares: on invoicing and on payment

The commission of a document is not due all at once. For each beneficiary the add-on splits it into shares:

- the **on invoicing** share (installment 0), equal to the sales employee's "% on invoicing", accrues on the posting
  date of the document;
- the rest accrues **on payment**: with settlement **by installment**, one share for each installment of the
  document, in proportion to the installment, which can be settled when that installment is paid; with settlement
  **on total**, a single share (installment -1), which can be settled when all installments are paid.

Example: invoice with a net amount of 1.350 and 5% commission = 63,00; agent with 30% on invoicing and settlement by
installment, document in two 50% installments: share 0 = 18,90 on posting, installment 1 = 22,05 and installment
2 = 22,05 on their respective due dates.

### Settlement

Settling a share means granting it to the agent with a settlement date. The add-on proposes the shares to
settle by reading SAP's incoming payments (payments, bills of exchange, reconciliations, credit memos) and proposes
the **reversal** of shares already settled whose installments are no longer paid (unpaid items). A **finalized**
share is definitive: it is not reversed and the commission is not recalculated any further.

## 3. Installation and first start

- Package for the Extension Manager: `XEI.CommissionManagement.zip`, from the download page of the XEI
  website. In SAP Business One open the **Extension Manager**, import the package and assign it to the company.
- On first start the add-on creates fields, tables, indexes and authorizations. Creating the fields on the document
  lines takes **a few minutes**: SAP shows the message *"The database structure has been modified... all open
  windows will be closed. Continue?"* several times — answer **Yes**.
- The menu is in **XEI-Addon › Commissions**:

    Commissions
      Configuration                     options (six tabs) and rule search order
      Agents                            role, superiors, default %, % on invoicing, settlement, vendor, SAP user
      Percentage rules                  % by customer / group / item / item group / price list
      Tiers and bonuses                 bonuses on annual sales (if enabled in Configuration)
      Check and assign %                comparison of documents / rules and bulk correction
      Commission calculation            calculation on invoices, down payments and credit memos
      Calculated commissions            consultation, correction, recalculation, deletion
      Settlement                        collected shares to settle, unpaid items to reverse
      Adjustments                       manual amounts per agent and month, agent invoice drafts
      Commission statement              calculated, to settle, settled + adjustments; CSV, print/PDF, email
      Checks                            issues to check
      Informazioni (About), Traduzioni (Translations), Licenza (License) (common items of XEI add-ons)

> After installation: fill in the **Configuration**, then the **Agents** (roles, superiors,
> percentages), then the **Rules**. Only from then on do documents receive the percentages. Users who are not
> superusers must be given the **authorizations** (chapter 17).

### License

The add-on works with a **license code** issued by XEI.

- **Trial**: after requesting the trial on the website, a **trial code** is sent by email, valid for 30
  days from sending in any company.
- **Purchase**: send XEI the two codes of the **Licenza** (License) window (company code and server
  code, with *Copia* (Copy)) and you receive the license code, valid for the company or the server of those codes.
- Without a valid code the add-on is **locked**: its menu keeps only *Informazioni* (About) and *Licenza*
  (License), and at startup the **Licenza** (License) window opens by itself with the status and the reason.
- A SAP **superuser** pastes the code into *Inserisci un codice di licenza* (Enter a license code) and presses
  *Salva codice* (Save code): the add-on is unlocked immediately, without restarting SAP.

### Languages

The add-on uses the language of the SAP client (in SAP: Users - Setup \> Display \> Language): Italian,
English, German, French, Spanish or Turkish; with other languages it stays in Italian. When the language changes, SAP
closes the open windows and the add-on restarts by itself. Individual texts can be adapted from **Commissions \>
Traduzioni** (Translations). The texts that SAP saves only once in the database stay in Italian in all languages:
the names of the authorizations (General Authorizations \> Provvigioni) and the titles of the fields added to
documents and sales employees (e.g. "Provv. % manuali" (commission % manual), "% agente" (% agent)); the messages
quote them with these names, so they can be found in SAP.

## 4. Each month's work, in brief

1.  **During the month** the documents receive the percentages automatically; whoever enters them can correct them.
2.  **Check and assign %** on the month's invoices: you see the lines whose percentages do not match the rules
    and correct them in bulk (optional but recommended).
3.  **Commission calculation** for the month: invoices, down payment invoices, credit memos.
4.  **Calculated commissions**: spot check, corrections of individual commissions.
5.  **Settlement** with cut-off date at the end of the month: confirmation of the collected shares and of any
    reversals.
6.  **Adjustments** of the month (bonuses, recoveries, manual corrections) and, if enabled, the agents' **invoice
    drafts**.
7.  **Commission statement** "Settled commissions and adjustments" for the month: this is the amount to grant to each
    agent; CSV for Excel, print/PDF or email to each agent.
8.  When the statements have been delivered, **closed period** up to the end of the month (if the option is used).

The **Checks** (chapter 16) can be run at any time, before the calculation or before the statements, to find
documents not calculated, changed agents, lines without percentages, collections not settled. At year end,
**Tiers and bonuses** (chapter 15) posts the bonuses on sales as December adjustments.

## 5. Configuration

The Configuration has six tabs. The **General** tab contains the basic options and the rule order; the
others (**Documents**, **Settlement**, **Agents**, **Email**, **Alerts**) contain the additional functions,
all **switched off** at the start: each one has an explanation and an example below it, and is enabled with the
checkbox when needed. The «Configurazione» (Configuration) authorization is required (chapter 17).

![Configuration, General tab](../../_img/commissionmanagement/cfg.png)

*Commission configuration, General tab*

### General tab

Assign the percentages to sales document lines while they are entered  
Enables the automatic assignment (chapter 8). When disabled, the percentages are entered by hand or with the Check.

Line discount used by the rules  
The discount the rules compare with their "minimum discount": the line's *Line discount %* or a percentage user
field of the lines (for example an "effective" discount calculated by another add-on).

Net prices  
For those who sell at net price without entering the discount: if the line has no discount, the add-on calculates the
**effective discount** as the difference between the customer's price list price and the line price (price list
100, price 80 = discount 20%), writes it in the *Provv. sconto effettivo* (commission effective discount) column and
uses it for the rules.

Percentages also on "tax only" lines  
Normally "tax only" lines have no commission (percentages at zero).

Commissions on down payment invoices  
With the option enabled, down payment invoices are calculated and their commission is then **deducted** from the
final invoice that closes them, so that the overall commission is that of the whole amount.

Default settlement when the whole document is collected  
Applies to sales employees with settlement "From configuration": yes = a single share when the whole document is
collected; no = one share per installment.

Credit memos settled on the due date  
Normally the (negative) commission of a credit memo is settled on the posting date. With the option, on the latest
due date among the credit memo and the invoices it refers to.

Rule search order  
The 16 possible field combinations for a rule, in the order in which they are tried. Change the number in the
*Order* column: order 1 is tried first. See chapter 7.

### Documents tab

![Configuration, Documents tab](../../_img/commissionmanagement/cfg_documenti.png)

*Documents tab: estimate, manual lines, automatic calculation*

Show the estimated commission when a sales document is saved  
After adding or updating an order, a quotation, a delivery or an invoice, the status bar shows how much each
beneficiary will earn with the current percentages of the lines. Example: *"Estimated commissions (Sales order 1250):
Rossi 63,00; Bianchi 9,00 - total 72,00"*. It is for information only: nothing is saved (chapter 8).

Protect percentages changed manually on document lines  
Changing a percentage on the line makes it "manual" (column *Provv. % manuali* (commission % manual)): if the
customer or agent changes, that line is not reassigned. Example: Rossi lowers the line from 5% to 4% for a deal with
the customer; then the customer changes: the other lines are reassigned, this one stays at 4%. Without the option the
reassignment overwrites all lines. Unchecking "manual" makes the line automatic again.

Calculate commissions as soon as an invoice, a down payment invoice or a credit memo is added  
The calculation runs when saving from the SAP client (with the last choice made on the document discount in the
Calculation): so there is no need to open Commission calculation every month. Example: when Rossi's invoice 1001 is
added, the status bar says *"Commissions calculated (Invoice 1001): Rossi 63,00; Bianchi 9,00"*. Documents created by
imports or by other programs (DI API) do not go through the client: for those, use Commission calculation and the
Checks.

### Settlement tab

![Configuration, Settlement tab](../../_img/commissionmanagement/cfg_liquidazione.png)

*Settlement tab: partial payments and closed period*

Partial payments: settle the part of the commission proportional to the amount collected on the installment  
Without the option a share is settled only when the installment is fully closed: with partial payments or write-offs
the commission stays on hold. Example: installment of 500 with share 22,05; the customer pays 250 → 11,03 is settled;
at full payment the other 11,02. If a payment is cancelled, only the excess is reversed (chapter 12).

Closed period: lock commissions up to (date)  
Up to that date inclusive, commissions cannot be recalculated or deleted, shares changed, settled, or adjustments
saved. Example: once the March statements are delivered, set 31/03: the March invoices can no longer be
recalculated (an invoice never calculated can still be calculated). To correct something in the closed period:
move the date back (or uncheck the option), correct, then set it again.

### Agents tab

From adjustments, generate A/P invoice drafts for the agents linked to a vendor  
In Adjustments the **Agent invoice drafts** button creates for each agent an A/P invoice draft (A/P credit memo if
the amount is negative) with one service line: amount = shares settled in the month + adjustments and bonuses of the
month. Example: Rossi (vendor F0010), April: 22,05 + 50,00 - 20,00 = 52,05. The **line account** is required (the
commission expense account, e.g. 7xxxx Commissions paid); the **tax code** is the one of the agent's invoices
(empty = the vendor's default). Chapter 13.

Annual sales tiers with bonus  
Enables the **Tiers and bonuses** menu: when the annual net amount reaches the threshold, the agent receives a bonus
(% of the year's sales or fixed amount) posted as an adjustment. Example: tiers 100.000 → 0,5% and 200.000 → 1%;
Rossi invoices 150.000 in 2026: bonus 750,00 in the December adjustment. Chapter 15.

Indicative withholding in the settled statement: % and description  
Informational only (no minimums or maximums): the printed and emailed "Settled commissions and adjustments" statement
shows a "withholding" line and the indicative net. Example: 8,5 and "Enasarco quota agente": settled 1.000,00 →
indicative withholding -85,00, indicative net 915,00. Empty or 0 = no line.

![Configuration, Agents tab](../../_img/commissionmanagement/cfg_agenti.png)

*Agents tab: invoice drafts, tiers and indicative withholding (8,5% Enasarco)*

### Email tab

![Configuration, Email tab](../../_img/commissionmanagement/cfg_email.png)

*Email tab: sending the statement to the agents*

Send the statement to agents by email  
Enables the **Send to agents** button in the Commission statement: each agent receives only their own statement
(HTML attachment, which can be opened and printed from any browser) at the email address of the sales employee (or of
the linked vendor). SMTP server, port, SSL/TLS, mailbox user and password and the sender must be entered;
example: `smtp.azienda.it`, port 587, SSL yes, sender `provvigioni@azienda.it`. The
password is saved encrypted.

Test send  
Sends a test message to the address given, using the values entered in the tab (even if not saved yet):
if something is wrong, the server's error message appears immediately.

### Alerts tab

![Configuration, Alerts tab](../../_img/commissionmanagement/cfg_avvisi.png)

*Alerts tab*

Share collected but not settled: it is an issue after (days)  
In the Checks, the "Unsettled collections" search reports the shares whose installment was collected more than
these days ago and that nobody has settled. Example: 30; installment collected on 05/04 and today is 10/05: the share
is listed among the issues until it is settled.

When the add-on starts, report the quick-check issues in the status bar  
Quick checks at each start: documents of the last 90 days to calculate, cancelled documents with commissions,
agent changed after the calculation. Example: *"Commissions: 3 issues to check (Commissions \>
Checks)"*. Chapter 16.

> When saving, the Configuration checks that the enabled options are complete: closed period date,
> existing G/L account that allows postings for the drafts, withholding between 0 and 99,99, server, port and sender
> for the email.

## 6. Agents

![Agents](../../_img/commissionmanagement/agenti.png)

*Agents: all SAP sales employees, editable in the grid*

The grid shows all SAP sales employees. Fill in the columns and press **Save**: only the changed sales employees are
saved (the same fields can also be seen in the standard Sales Employees form, user-defined fields).

| Column                                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Role                                            | Agent, Zone manager, Area manager, Director or *(not managed)*: no commission.                                                                                                                                                                                                                                                                                                                           |
| Zone manager, Area manager, Director            | The superiors of this sales employee: they receive their percentage on this employee's documents. The drop-down lists show the sales employees who have that role: assign the roles first and save, then the superiors. A superior already assigned who has another role, or none, appears as *«name (different role)»*: they receive no commissions until they are given the role (the Checks report it too). |
| % agent, % zone manager, % area manager, % director | **Default** percentages of this sales employee's documents, used when no rule applies to the line.                                                                                                                                                                                                                                                                                                   |
| % on invoicing                                  | Part of the commission **of this sales employee** (as beneficiary) that accrues when the document is posted; the rest accrues on payment. 100 = all on invoicing, 0 = all on payment.                                                                                                                                                                                                                    |
| Settlement                                      | For the part on payment: *By installment*, *On total* or *From configuration* (follows the Configuration option).                                                                                                                                                                                                                                                                                        |
| Vendor                                          | The vendor (business partner) with which the agent invoices the commissions: the business partner of the **invoice drafts** (chapter 13); its email is used to send the statement if the sales employee has none.                                                                                                                                                                                        |
| SAP user                                        | The SAP user corresponding to this sales employee. A user without the «Estratto di tutti gli agenti» (statement of all agents) authorization sees in the Commission statement only themselves and the sales employees of whom they are zone manager, area manager or director (chapter 17).                                                                                                               |
| Email (sales employee)                          | The email of the sales employee (SAP master data, read-only): recipient of the statement by email.                                                                                                                                                                                                                                                                                                       |

Checks on saving: percentages between 0 and 100, existing vendor and SAP user, a sales employee cannot be their own
superior. Example used in this manual:

| Sales employee | Role          | Zone manager | Area manager | % ag. | % zone mgr | % area mgr | % on inv. | Settlement          |
|----------------|---------------|--------------|--------------|-------|------------|------------|-----------|---------------------|
| Rossi          | Agent         | Bianchi      | Neri         | 2     | 0,5        | 0,2        | 30        | By installment      |
| Bianchi        | Zone manager  |              |              | 3     |            |            | 0         | From configuration  |
| Neri           | (not managed) |              |              |       |            |            |           |                     |
| Verdi          | Agent         |              |              | 1,5   |            |            | 100       | From configuration  |

On Rossi's documents the beneficiaries are Rossi (agent) and Bianchi (zone manager); Neri, although set as area
manager, receives nothing until he has a role.

## 7. Percentage rules

![Percentage rules](../../_img/commissionmanagement/regole.png)

*Percentage rules of the example*

A rule says: "for lines with *these characteristics* the percentages are these". The possible characteristics are
customer, customer group, item, item group and price list (the customer's price list); fill in **only the fields
you need** and the add-on recognizes the **combination** by itself (Combination column).
There are 16 allowed combinations:

| Type | Combination                         | Type | Combination                                |
|------|-------------------------------------|------|--------------------------------------------|
| 1    | Customer / Item / Price list        | 9    | Customer group / Item group / Price list   |
| 2    | Customer / Item                     | 10   | Customer group / Item group                |
| 3    | Customer / Item group / Price list  | 11   | Customer group / Price list                |
| 4    | Customer / Item group               | 12   | Customer group                             |
| 5    | Customer / Price list               | 13   | Item / Price list                          |
| 6    | Customer                            | 14   | Item                                       |
| 7    | Customer group / Item / Price list  | 15   | Item group / Price list                    |
| 8    | Customer group / Item               | 16   | Item group                                 |

Customer and customer group together (or item and item group together) are not allowed: the rule is not saved.

The other fields of the rule:

- **Agent**: the rule applies only to the documents of that sales employee; *(all)* = for everyone;
- **From / To**: validity period compared with the document date; even just one of the two dates;
- **Minimum discount**: the rule applies if the line discount is at least this (0 = always). It is used to give
  lower percentages to the most discounted sales;
- **Active**: a deactivated rule stays on file but is not applied.

### How the rule of a line is chosen

1.  The combinations are tried in the **order set in the Configuration** (default 1 → 16, from the most specific to
    the most generic).
2.  For each combination, the rules of the **document's agent** are searched first (if the agent has at least one),
    then those for all. The first combination that finds a valid rule wins: a more specific rule "for all"
    (e.g. Customer / Item group) wins over a more generic agent rule (e.g. Item group).
3.  Among several rules of the same combination, the one with the most recent start date wins, then the one with the
    nearest end date, then the one with the highest minimum discount reached.
4.  If no rule applies, the agent's default percentages are used.

Example with the rules in the figure (R1 customer C001 + item group GA100 → 6/1; R2 Rossi only, group GA100 → 7/1;
R3 item A1 → 4/0,5; R4 item A1 with minimum discount 10 → 3/0,5; R5 customer group A, year 2026 → 5/1):

| Line                                            | Percentages agent / zone manager | Why                                                          |
|-------------------------------------------------|----------------------------------|--------------------------------------------------------------|
| Rossi, customer C001, item A9 (group GA100)     | 6 / 1                            | R1: Customer / Item group comes before Rossi's rule          |
| Rossi, customer C002, item A9                   | 7 / 1                            | R2: agent rule                                               |
| Verdi, customer C002, item A9                   | 1,5 / 0                          | no rule: Verdi's default percentages                         |
| Verdi, customer C002, item A1, discount 12      | 3 / 0,5                          | R4: minimum discount 10 reached (wins over R3)               |
| Verdi, customer C002, item A1, discount 5       | 4 / 0,5                          | R3                                                           |
| Verdi, customer C003 (group A), item A1         | 5 / 1                            | R5: Customer group comes before Item                         |
| as above but in 2027                            | 4 / 0,5                          | R5 expired, R3 remains                                       |

### The form

- **Filters** (agent, customer, item, active only) and **Search**.
- **Add row**, **Duplicate rows** and **Delete rows** on the selected rows (click on the row header,
  on the left); the changes become final with **Save**. All fields are edited in the
  grid (the arrows open customer and item).
- **Export CSV** saves the rules shown in a file with ";" as separator (it opens in Excel); **Import CSV**
  adds the rows of a file with the same columns (Agente, Cliente, GruppoClienti, Articolo, GruppoArticoli,
  Listino, Dal, Al, ScontoMinimo, PercAgente, PercCapoZona, PercCapoArea, PercDirettore, Attiva): the imported rows
  must be checked and saved.
- When closing or searching with unsaved changes, the add-on asks for confirmation.

## 8. The percentages on sales documents

![Sales Order](../../_img/commissionmanagement/ordine.png)

*Sales Order: the Provv. columns with the assigned percentages and, with net prices, the effective discount*

With the assignment enabled, on sales quotations, sales orders, deliveries, returns, A/R invoices, A/R credit memos and
A/R down payment invoices:

- when the **item**, the **discount** or the **price** of a line is entered or changed, the add-on writes
  the four percentages of the line (and the effective discount, with net prices);
- when several items are chosen from the list, the added lines are completed too;
- when the **customer** or the **sales employee** of a document being added is changed, all lines are
  reassigned. Note: when the customer changes, SAP sets that customer's default sales employee again; if it is
  "-No Sales Employee-", the lines stay as they were until the agent is chosen.

The percentages remain **editable by hand** and are saved with the document; they are rewritten only if the item,
price or discount of that line is changed again. Copied documents (order → delivery → invoice) carry the line
percentages with them.

> The *Provv. % agente* (commission % agent), *% capo zona* (% zone manager), *% capo area* (% area manager),
> *% direttore* (% director) and *Provv. sconto effettivo* (commission effective discount) columns are made
> visible and editable by the add-on when the document is opened; to always have them in the preferred position, they
> can be arranged once in the form settings (icon at the top right of the grid). In documents without a sales
> employee, or with a sales employee without a role, nothing is written.

The "tax only" checkbox of a line does not raise an event in the client: the percentages adjust at the next change
of item, price or discount of the line (or when the agent is changed).

### Manual lines (option "protect percentages changed manually")

![Order with a manual line](../../_img/commissionmanagement/ordine_manuale.png)

*Order: the line with the percentage corrected by hand is flagged in "Provv. % manuali" and is not reassigned*

With the option enabled the add-on also shows the *Provv. % manuali* (commission % manual) column. As soon as one of
the four percentages of a line is entered by hand, the line is **flagged as manual** and from then on it is not
reassigned: neither when the item, price or discount of the line changes, nor when the customer or agent of the
document changes, nor when other items are chosen from the list. The other lines keep following the rules. To go back
to automatic, just uncheck it: at the next change the line receives the percentages of the rules again. The flag is
carried over to copied documents and can be seen in the Check (column *Manual %*), where manual lines are not
proposed for correction.

### Estimate and automatic calculation on posting

![Estimate in the status bar](../../_img/commissionmanagement/stima.png)

*After the order is added, the status bar shows the estimated commission for each beneficiary*

Two options of the Documents tab act when the document is **saved** from the SAP client:

- **Estimate**: for sales quotations, sales orders, deliveries, returns, A/R invoices, A/R credit memos and A/R down
  payment invoices, the status bar shows how much would accrue with the current percentages of the lines,
  beneficiary by beneficiary, for example *"Estimated commissions (Sales order 1250): PRV Rossi 6,00; PRV Bianchi
  1,00 - total 7,00"*. The document discount is considered or not according to the last choice made in the
  Calculation. Nothing is saved.
- **Automatic calculation**: invoices, credit memos and (if enabled) down payment invoices **added** from the client
  are calculated immediately, as if Commission calculation had been run on that document only; the status bar
  says *"Commissions calculated (Invoice 1001): ..."*. In Calculated commissions the origin is "Automatic on
  posting". If the calculation is not possible (down payment already deducted, closed period, agent not managed) a
  warning appears and the document is posted normally: it is then calculated from Commission calculation, and the
  Checks list it among those "To calculate".

> Documents created by imports, by the Service Layer or by the DI API do not go through the SAP client: for
> those, Commission calculation always applies (or the calculation of the whole period, which takes only the
> documents not yet calculated).

## 9. Check and assign %

![Percentage check and assignment](../../_img/commissionmanagement/controllo.png)

*Check: percentages of the document ("Doc.") and proposed by the rules, differing lines highlighted*

Before the calculation it is advisable to verify that the percentages on the documents of the period match the rules
(whoever entered the invoice may have changed them, or the rules may have been updated afterwards).

1.  Choose agent (or all), period and document types: invoices, down payments, credit memos **not yet
    calculated** and, if desired, open sales orders. Press **Check**.
2.  For each line the grid shows the current percentages (*Doc.*), those the rules would give today
    (*Proposed*) and the *Proposal source* (rule for all, agent rule, default percentages). The
    differing lines are highlighted and already checked; with "Only lines that differ from the proposal" only those
    are shown.
3.  Uncheck the lines to be left as they are (intended corrections) and press **Apply proposed %**.

What happens to the checked lines:

- **open sales orders**: the order is updated; the new percentages are carried over to the documents that will be
  copied from it;
- **invoices, down payment invoices and credit memos**: they are posted documents and SAP does not allow changing them
  (not even the user fields of the lines). The corrected percentages are saved by the add-on in its own table
  and used by the calculation instead of those of the document; the SAP document stays as it is. The *Already
  corrected* column shows this and from then on the *Doc.* column shows the corrected percentages.

![Check with manual lines](../../_img/commissionmanagement/controllo_manuale.png)

*Check on open orders: manual lines that differ from the proposal are not checked ("with manual %: 3")*

Double-click a line to open the document. Documents with commissions already calculated are not shown: to correct
them use Calculated commissions (chapter 11). The *Manual %* column shows the lines whose percentages were
corrected by hand on the document: with the option "protect percentages changed manually" they are not checked (they
can be checked deliberately). With the closed period enabled, posted documents dated within the period are not
corrected.

## 10. Commission calculation

![Commission calculation](../../_img/commissionmanagement/calcolo.png)

*Commission calculation with the result per document*

Choose the period (document date), the types (invoices, down payment invoices if enabled in Configuration, credit
memos) and whether to **consider the document discount** (the discount on the whole document reduces the net amount
of each line). **Calculate** processes all documents of the period that are **not cancelled**, with a managed agent and
**not yet calculated**: first the down payment invoices, then invoices and credit memos. For each document the grid
shows how many beneficiaries have a commission, the total and the result; double-click opens the document.

With **Only the document** (type and number) a specific document is calculated or **recalculated**, for example after
a correction of the percentages; recalculation is possible only if none of its shares is settled or finalized.

### How it is calculated, step by step

For each beneficiary (agent and superiors with a role):

1.  **Line net amount** = line total in local currency, reduced by the document discount if requested; negative in
    credit memos. Zero lines (free items) do not count.
2.  **Line commission** = net amount × the line's percentage for that role. Lines with percentage 0 do not
    count.
3.  **Total** = sum of the line commissions. From invoices that close a down payment, the commission already
    calculated on the down payment is subtracted (in proportion to the amount deducted).
4.  **Shares**: the on-invoicing share (installment 0) on the posting date; the rest by installment (installment n on
    the due date of installment n, in proportion to its percentage, the last installment takes the roundings) or on
    total (installment -1 on the due date of the last installment). Credit memos have a single negative share
    (installment 0 on the posting date or, with the option, on the due date).

Amounts are rounded to 2 decimals; the total commission is always the sum of the shares.

### Example: invoice 1001

Rossi (30% on invoicing, by installment), customer C001, **document discount 10%**, two 50% installments (31/03 and
30/04):

| Line         | Line total  | Net amount (−10%) | % agent  | Agent comm.   | % zone mgr  | Zone mgr comm.   |
|--------------|-------------|-------------------|----------|---------------|-------------|------------------|
| A1           | 1.000,00    | 900,00            | 5        | 45,00         | 1           | 9,00             |
| A2           | 500,00      | 450,00            | 4        | 18,00         | 0           | \-               |
| A3 (free)    | 0,00        | \-                | 5        | \-            |             |                  |
| Total        |             | 1.350,00          |          | 63,00         |             | 9,00             |

| Beneficiary                              | Share                       | Due date          | Amount  |
|------------------------------------------|-----------------------------|-------------------|---------|
| Rossi (agent, 30% on invoicing)          | installment 0 – on invoicing | 10/03 (posting)  | 18,90   |
|                                          | installment 1 (35%)         | 31/03             | 22,05   |
|                                          | installment 2 (35%)         | 30/04             | 22,05   |
| Bianchi (zone manager, 0% on invoicing)  | installment 1 (50%)         | 31/03             | 4,50    |
|                                          | installment 2 (50%)         | 30/04             | 4,50    |

Neri (area manager) receives nothing because he has no role, even though line A1 has 0,5% in his column.

### Down payment invoices

SAP posts a down payment invoice with the full lines of the order and a document discount equal to the complement of
the down payment (30% down payment = 70% discount): the add-on always uses that discount, so the net amount is the
down payment share (10.000 × 30% = 3.000 → 150,00 at 5%). When the final invoice deducts the down payment, the 150,00
already calculated are subtracted from its commission (10.000 × 5% = 500,00): 350,00 remain, split into shares as
usual. As long as the final invoice has calculated commissions, the down payment can be neither recalculated nor
deleted (the invoice must be corrected).

### What is not recalculated

- documents with **settled or finalized** shares (the settlement must be removed first, chapter 11);
- down payment invoices already deducted from a calculated invoice;
- cancelled documents: they are not calculated; if they had been calculated before the cancellation, their commission
  must be deleted by hand from Calculated commissions (the Settlement ignores them).

## 11. Calculated commissions: viewing and correcting

![Calculated commissions](../../_img/commissionmanagement/provvigioni.png)

*Calculated commissions: list, document lines with the beneficiary's % and shares*

The list at the top shows one row per document and beneficiary (filters for agent, type, period, number, only
unsettled): net amount, commission, settled, to settle, calculation date. Clicking a row shows below it the
**document lines** with that beneficiary's percentage and the **shares**. Double-click opens the document in SAP.

Recalculate with changed %  
Change the percentage in the lines at the bottom (column *%*) and recalculate this commission only. The SAP document
is not touched: it is used to correct a single case without changing the rules. Example: line A2 from 4% to 6%
→ 63,00 becomes 72,00 and the shares 21,60 / 25,20 / 25,20.

Recalculate from document  
Recalculates with the current percentages of the document lines (or those corrected by the Check): it cancels the
changes made with the previous button and takes over corrections made on the document.

Save shares  
Settlement date, settled amount and the *Finalized* checkbox of the shares can be changed by hand
(settlements outside the procedure, adjustments): Save shares records them and updates the settled amount of the
header.

Delete commission  
Removes this beneficiary's commission on the document; the document can be calculated again from the Calculation (only
the document or in the period).

Recalculation and deletion are blocked if a share is already settled or finalized ("Commissions already settled or
finalized: remove the settlement first": in Save shares, set the settled amount to zero), if the document is in the
**closed period** (Settlement tab of the Configuration) and, as a precaution, if the sales employee is no longer in the
hierarchy of the document's agent (the recalculation would delete it: use Delete if that is intended).

**Traceability**: each header and each share shows *Origin*, *User* and *Last change*: who last wrote that data and
how. Origins of the headers: *Calculation* (from the menu), *Automatic on posting* (when the invoice is posted),
*Recalculation from document*, *Recalculation with changed %*; of the shares: *Calculation*, *Settlement*, *Unpaid
reversal*, *Manual* (Save shares).

## 12. Settlement

![Settlement](../../_img/commissionmanagement/liquidazione.png)

*Settlement: proposals of the shares to settle as of 31/03*

1.  Enter the **cut-off date** (usually the end of the month), whether to include credit memos and, if desired, check
    the agents to process (none = all). **Process**.
2.  The grid proposes:
    - **Settle** – shares not yet settled and not finalized with a due date up to the cut-off date:
      - the on-invoicing share (installment 0) always, on its due date (posting date of the document);
      - the share of an installment when that installment is **closed** in SAP; the on-total share (installment -1)
        when all installments are closed;
      - the proposed **settlement date** is the latest between the installment due date and the collection date.
        The collection date takes into account incoming payments (payment date or its due date if later), bills of
        exchange deposited and cleared, reconciliations with journal entries or credit memos, credit memos issued
        on the invoice; if it cannot be determined, the due date applies.
    - **Reverse** (red rows) – shares already settled and not finalized whose installments are no longer paid
      (payment cancelled, unpaid): the settlement is removed and the amount is to be settled again.
3.  Uncheck the rows not to be posted, correct the settlement date if needed, check **Finalize** on the shares
    to be made definitive. The totals at the bottom are updated with the checkboxes.
4.  **Confirm** posts the checked rows; the settled amount of the documents is updated and a new processing does not
    propose them again.

![Reversal](../../_img/commissionmanagement/liquidazione_storno.png)

*After a payment is cancelled: proposal to reverse the settled shares*

Example: invoice 1001 has the first installment (due date 31/03) collected on 05/04. Processing as of 30/04 proposes
the installment 1 shares of Rossi (22,05) and of Bianchi (4,50) with settlement date 05/04. If the payment is
cancelled, the next processing proposes the reversal of the two shares; if Rossi's share had been finalized, only
Bianchi's reversal is proposed.

> A **finalized** share is definitive: it is not reversed and the document's commission is not recalculated
> any further. Finalize when the commissions have been paid to the agent.

### Partial payments (option)

![Settlement with partial payment](../../_img/commissionmanagement/liquidazione_parziale.png)

*Partial payment: yellow rows with the part that can be settled, the full share and the amount already settled*

Normally the share of an installment is settled only when the installment is **closed**: if the customer pays on
account, the commission stays on hold. With the **Partial payments** option the share is settled in proportion to the
amount collected: installment of 816,75 with share 22,05, the customer pays 408,38 (half) → settlement of **11,03** is
proposed (yellow row, with the columns *Full share* 22,05 and *Already settled* 0), on the payment date if it is
after the due date; at full payment the rest, **11,02**, is proposed. If a payment is cancelled, the reversal brings
the settled amount back to the part still collected (all of it, if nothing collected remains). The on-invoicing shares
(installment 0) do not change; for the "on total document" shares the proportion is on the amount collected over all
installments.

### Closed period (option)

When the statements of a month have been delivered, the period can be **closed** up to that date (Settlement tab of
the Configuration): from then on, for documents dated within the period, commissions are neither recalculated nor
deleted, shares are not changed, nothing is settled or reversed with a date in the period, adjustments and bonuses are
not saved in closed months, and the Check does not correct posted documents. In every case the message says
*"Period closed up to dd/mm/yyyy"*, before any confirmation question (if the shares are already settled it says
instead *"Commissions already settled or finalized"*). An invoice of the period never calculated can still be
calculated. To correct something: move the date back (or uncheck the option), correct, then set it again.

## 13. Adjustments

![Adjustments](../../_img/commissionmanagement/conguagli.png)

*Adjustments of a month*

Manual amounts per agent and month, positive or negative (bonuses, refunds, recoveries, corrections), with an order
and a description. Choose year and month (arrows \< and \> to change month, **Show**), add or delete
rows and press **Save**: the rows of the month are replaced with those of the grid. The adjustments appear
in the "Settled commissions and adjustments" statement of the month. The *Type* column distinguishes *Manual*
adjustments from the *Tier bonus* rows posted by the tiers (chapter 15), which can be seen here but not changed. With
the closed period enabled, closed months cannot be saved.

### Agent invoice drafts (option)

![Agent invoice drafts](../../_img/commissionmanagement/bozze.png)

*Adjustments: at the bottom the invoice drafts generated for the month, with the link to the draft and to the vendor*

When the agent invoices the commissions to the company, the **Agent invoice drafts** button prepares the document on
the agent's behalf. For the chosen month, for each managed agent with a linked **vendor** (chapter 6):

- amount = shares **settled in the month** (by settlement date) + **adjustments and bonuses** of the month;
- positive amount → **A/P invoice** draft; negative → **A/P credit memo** draft;
  zero → nothing;
- the draft has one service line on the account set in Configuration, with the chosen tax code (or the vendor's
  default) and the amount as line total.

Example: Rossi (vendor V20000), April: installment settled on 05/04 of 22,05 + adjustments +50,00 and -20,00 = A/P
invoice draft of **52,05**. At the end a message summarizes agent by agent (draft created, no vendor,
zero amount, draft already present). The drafts of the month are in the grid at the bottom with the **status** (open,
closed i.e. already turned into an invoice, deleted), the date and the user; the yellow arrow opens the draft or the
vendor. An agent with a draft still existing for that month is skipped: to generate it again, delete the draft in SAP.
The draft must then be completed and posted in SAP like any other draft (number and date of the agent's invoice).

## 14. Commission statement

![Commission statement](../../_img/commissionmanagement/estratto.png)

*"Settled commissions and adjustments" statement for April, grouped by agent*

Three statements, for a period and for one agent or all, grouped by agent (arrows to expand and collapse),
with the total at the bottom and **Export CSV** (one "Total" row for each agent, to open in Excel):

| Statement                           | What it shows                                                                                    | Period refers to       |
|-------------------------------------|--------------------------------------------------------------------------------------------------|------------------------|
| Calculated commissions              | one row per document and beneficiary: net amount, commission, settled                            | document date          |
| Commissions to settle               | the shares not yet settled (or partly settled) and not finalized                                 | due date of the share  |
| Settled commissions and adjustments | the settled shares plus the adjustments of the months of the period: **it is what to grant to the agent** | settlement date |

### Print / PDF

![Printed statement](../../_img/commissionmanagement/estratto_stampa.png)

*The statement opened in the browser: one block per agent, totals and indicative withholding*

The **Print / PDF** button opens the statement shown in the browser, laid out for printing: header with company,
statement type and period, one block for each agent with their rows and the total. From there it can be printed or
saved as PDF (Print → "Save as PDF"). If the **indicative withholding** is set in Configuration (e.g. 8,5 "Enasarco
quota agente"), the "Settled commissions and adjustments" statement also shows, for each agent, the withholding row
and the **indicative net**: this is convenience information for the agent, without minimums or maximums.

### Send to agents (option)

With sending by email enabled (Email tab of the Configuration), the **Send to agents** button sends each agent of
the statement shown a message with **only their own statement** attached in HTML (which can be opened and printed from
any browser). The address is that of the sales employee or, if missing, that of the linked vendor. At the
end a summary says for each agent whether the sending succeeded, whether the address is missing or which error the
server returned. The button is enabled only for those with full authorization on the statement of all agents.

### Each manager sees their own agents

A SAP user linked to a sales employee (column *SAP user* in Agents) who does not have the «Estratto di tutti gli
agenti» (statement of all agents) authorization finds in the drop-down list only *(my agents)* and the names of
themselves and their subordinates (the sales employees of whom they are zone manager, area manager or director): a
zone manager can view the statement of their own agents without seeing the others. A user not linked to any sales
employee, without the authorization, sees nothing.

## 15. Tiers and bonuses

![Tiers and bonuses](../../_img/commissionmanagement/scaglioni.png)

*Tiers and bonuses: the tiers at the top, the bonuses calculated for the year at the bottom*

With the option "annual sales tiers with bonus" (Agents tab of the Configuration) the **Tiers and bonuses** menu
manages the year-end bonuses linked to sales. A **tier** has: agent (or *all*), year (or *every year*), annual net
amount threshold, bonus type (*% of annual sales* or *Fixed amount*), bonus, description, active. Rows are added,
changed and deleted in the grid at the top, then press **Save tiers**.

| Agent   | Year         | Threshold | Type               | Bonus  | Description       |
|---------|--------------|-----------|--------------------|--------|-------------------|
| (all)   | (every year) | 1.000     | % of annual sales  | 0,5    | Premio base       |
| (all)   | (every year) | 10.000    | % of annual sales  | 1      | Premio 10.000     |
| Rossi   | 2026         | 12.000    | Fixed amount       | 500,00 | Premio Rossi 2026 |

**Calculate bonuses** for a year: each agent's sales are the sum of the net amounts of their calculated commissions
(invoices and credit memos dated in the year; not down payment invoices, already included in the final invoices).
The tier reached is the one with the **highest threshold** not above the sales; the agent's tiers prevail over those
for all and the specific year over "every year". Bonus = sales × % or fixed amount.
Example with the tiers above: Rossi 13.150 → agent's 12.000 tier → **500,00**; Bianchi 2.900 →
1.000 tier → 0,5% = **14,50**; Verdi 1.488 → **7,44**. The *Already posted* column shows the bonus of the
same year already posted.

**Post checked bonuses**: the checked rows become adjustments of type *Tier bonus* in the chosen month (usually
December): from there they enter the "Settled commissions and adjustments" statement, the invoice drafts and the
month's totals like the other adjustments. Posting the same year again replaces the bonus posted earlier (no
duplicate); a zero bonus removes it. With the closed period enabled, closed months cannot be posted.

## 16. Checks and alerts at startup

![Checks](../../_img/commissionmanagement/verifiche.png)

*Checks: issues of the period, errors in red*

The **Checks** menu searches a period for anything that can cause a commission to be missing or wrong. Enter the
period, whether to also look for unsettled collections (the slowest search) and press **Check**: each issue has
a severity (**Error** in red, **Warning**), the check that found it, the agent, the document and the
explanation with what to do. Double-click opens the document.

| Check                   | What it reports                                                                                                                  | What to do                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| To calculate            | invoices, down payments and credit memos of the period with a managed agent and without commissions                              | Commission calculation                          |
| No agent                | documents without a sales employee or with a sales employee without a role                                                       | check whether it is intended; give the role in Agents |
| Lines without %         | documents with a managed agent whose lines all have zero percentages                                                             | Check and assign % or missing rules             |
| Agent changed           | calculated documents whose sales employee in SAP is no longer the one of the commission                                          | Recalculate in Calculated commissions           |
| Cancelled               | cancelled documents with calculated commissions                                                                                  | Delete commission                               |
| Agent hierarchy         | superior without a role (their part does not accrue), default percentage of a role without the superior, non-existent SAP user   | fix in Agents                                   |
| Overlapping rules       | two identical active rules (same fields, discount and sales employee) with overlapping periods: only one of the two applies      | correct the rules                               |
| Unsettled collections   | shares whose installment was collected more than the days set in Configuration ago and not yet settled                           | Settlement                                      |

With the **alerts at startup** option, every time the add-on starts it runs the quick checks (documents of the
last 90 days to calculate, agent changed and cancelled in the last year) and, if it finds something, reports it in the
status bar a few seconds after startup, i.e. after any license messages: *"Commissions: 3 issues
to check (Commissions \> Checks)"*. Without issues it writes nothing.

## 17. Authorizations and traceability

The add-on creates in the SAP **General Authorizations** (Administration › System Initialization ›
Authorizations) the **Provvigioni** (Commissions) node under *User Authorization*, with five sub-items. Superusers
always have everything; other users are assigned, for each item, *No Authorization*, *Read-Only* or
*Full Authorization*:

![General Authorizations](../../_img/commissionmanagement/autorizzazioni.png)

*General Authorizations: the Provvigioni node with its five sub-items, for a user without authorizations*

| Authorization                                                                   | Read-only                                                                      | Full                                                                         |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| «Configurazione» (Configuration)                                                     | –                                                                              | open and save the Configuration                                              |
| «Agenti, regole e scaglioni» (agents, rules and tiers)                          | view                                                                           | save agents, rules and tiers                                                 |
| «Controllo, calcolo e verifiche» (check, calculation and checks)                | view Check, Calculation, Calculated commissions, Checks                        | apply the %, calculate, recalculate, save shares, delete                     |
| «Liquidazione, conguagli e bozze fatture» (settlement, adjustments and invoice drafts) | view Settlement and Adjustments                                         | confirm settlements, save adjustments, post bonuses, generate drafts         |
| «Estratto di tutti gli agenti» (statement of all agents)                        | see the statement of all agents (without it: only one's own, chapter 14)       | also sending by email                                                        |

Without authorization the menu item answers in the status bar *"Function not allowed: requires the "…"
authorization (General Authorizations \> Provvigioni)"*; with read-only access the window opens but the
buttons that make changes answer *"Operation not allowed: requires full authorization on "…""*.

**Traceability**: headers and shares of the commissions record origin, user and date of the last write
(chapter 11); the adjustments the user and the change date; the invoice drafts who generated them and when. The
add-on log (chapter 19) records errors and updates of the data structure.

## 18. Frequently asked questions and problems

The percentages are not written on the document  
Check: the option in Configuration; that the document has a sales employee with a role; that the
customer is filled in. After a change of customer, choose the agent again.

I corrected a percentage on the invoice but SAP does not let me save it  
Posted invoices cannot be changed. Use Check and assign % (before the calculation) or Calculated
commissions → Recalculate with changed % (after).

"Commissions already settled or finalized"  
To recalculate or delete, in Calculated commissions set the settled amount of the shares to zero (Save shares) and
remove the finalization. If the shares have really been paid to the agent, better not to touch them: post the
difference as an adjustment.

"Down payment already deducted from an invoice with calculated commissions"  
First correct or delete the commission of the final invoice, then the down payment, then recalculate the invoice.

A share is not proposed for settlement  
The installment is not closed in SAP (partial payment or not yet posted), the due date is after the cut-off date, or
the share is already settled/finalized. Shares of cancelled documents are not proposed: delete the commission.

On first start SAP asks to close all windows  
This is normal when user fields are created: answer Yes until the creation is complete (a few minutes). This also
applies when an update of the add-on adds fields; if the client is closed halfway, the creation resumes when the
add-on is restarted.

"Period closed up to..."  
The operation concerns a date within the closed period (Configuration, Settlement tab). If the correction is
really necessary: move the lock date back, correct, then set it again.

"Function not allowed"  
The SAP user does not have the authorization (chapter 17): assign it in General Authorizations, Provvigioni node.

The invoice was posted but the status bar says "Commissions not calculated"  
The automatic calculation was not possible (down payment already deducted, closed period, agent not managed): the
document is posted normally; calculate it from Commission calculation (the Checks list it among those "To
calculate").

Sending by email gives an error  
Use "Test send" in the Email tab of the Configuration: the server message says whether server, port, SSL or
credentials are wrong. Agents "without email" must be completed in the master data of the sales employee or of the
linked vendor.

A document line does not take the percentages of the rules  
With the option "protect percentages changed manually" the line is flagged as manual (column Provv. % manuali):
uncheck it and change item, price or discount, or correct it by hand.

While the add-on is processing, SAP does not respond  
During Check, Calculate, Process and Apply, SAP waits for the add-on (status bar "Please wait..."): do not close
the window and do not terminate the add-on, otherwise the client remains waiting and must be restarted.

## 19. Data and technical notes

| Where                                                        | What                                                                                                                                                                                                |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLP (sales employees)                                       | fields `U_XEI_PRV_Ruolo`, `_CapoZona`, `_CapoArea`, `_Direttore`, `_PercAg`, `_PercCZ`, `_PercCA`, `_PercDI`, `_Fatturato`, `_Liquida`, `_Fornitore`, `_Utente` (SAP user)                          |
| Marketing document lines (RDR1, INV1, RIN1, DPI1...)         | `U_XEI_PRV_Ag`, `_CZ`, `_CA`, `_DI` (percentages), `_ScEff` (effective discount), `_Man` (manual line)                                                                                              |
| `@XEI_PRV_REGOLE`                                            | percentage rules                                                                                                                                                                                    |
| `@XEI_PRV_DOC`, `@XEI_PRV_RIGHE`, `@XEI_PRV_RATE`            | calculated commissions: header per document and beneficiary, lines, shares (code = type-DocEntry-employee\[-line/installment\], e.g. `13-386-61-2`); headers and shares with origin, user and change date |
| `@XEI_PRV_PERC`                                              | percentages corrected by the Check for lines of posted documents                                                                                                                                    |
| `@XEI_PRV_CONG`                                              | adjustments (type M manual / P bonus, reference year of the bonus)                                                                                                                                  |
| `@XEI_PRV_SCAG`, `@XEI_PRV_BOZZE`                            | tiers; generated invoice drafts (agent, month, draft, vendor, amount)                                                                                                                               |
| `@XEI_SETTINGS` (scope XEI.CommissionManagement)             | Configuration options (encrypted SMTP password) and version of the data structure                                                                                                                   |
| Authorizations (OUPT)                                        | `XEI_PRV` and sub-items `XEI_PRV_P_CFG`, `_ANAG`, `_CALC`, `_LIQ`, `_EST`                                                                                                                           |

- Document types: 13 invoice, 203 down payment invoice, 14 credit memo, 17 order (only in the check).
- Everything goes through the SAP DI API (no direct connection to the database).
- Performance: on documents the lines are read in bulk (a single call) and only the cells that change are written;
  customers, items and price lists are read once per window. In the settlement, the collection dates
  (the heaviest search) are calculated only for the shares that can actually be settled.
- Log: `%LOCALAPPDATA%\XEI\logs\XEI.CommissionManagement.log`.
