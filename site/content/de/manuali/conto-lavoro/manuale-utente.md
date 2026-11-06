---
title: XEI.ContoLavoro – Benutzerhandbuch
description: Wie Sie mit XEI.ContoLavoro Lohnfertigungsaufträge, Komponentenversand, Produkteingänge und die Lohnfertigung aus Produktionsaufträgen verwalten.
lang: de
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Benutzerhandbuch

Installation, Lizenz und Menüs sind auch im
[Installationshandbuch](installazione.md) beschrieben.

## 1. Was das Add-on macht

XEI.ContoLavoro verwaltet die Bearbeitungen, die an **Lohnfertiger** (externe Zulieferer) vergeben werden: Sie
erhalten Komponenten vom Unternehmen, bearbeiten sie und liefern ein Fertig- oder Halbfertigprodukt zurück. Für jede
Bearbeitung wird ein **Lohnfertigungsauftrag** angelegt, der Folgendes zusammenführt:

- die herzustellenden **Produkte** mit ihrer Stückliste (zu versendende Komponenten und zu bezahlende Bearbeitungen);
- die **Bestellung** an den Lohnfertiger, automatisch mit dem Lohnfertigungsauftrag abgeglichen;
- den **Komponentenversand** an das Lager des Lohnfertigers, die **Rückholungen** und den **Ausschuss**;
- den **Produkteingang**: Wareneingang der Produkte und Bearbeitungen, Warenausgang der verbrauchten Komponenten,
  Eingang aus Produktion für Produkte, die aus einem Produktionsauftrag stammen (Kapitel 6);
- die aktuelle Situation in Echtzeit: wie viel versendet und verwendet wurde, was beim Lohnfertiger verbleibt und was
  fehlt.

Der Lohnfertigungsauftrag schließt sich von selbst, wenn alle Produkte eingegangen sind und beim Lohnfertiger keine
Komponenten mehr liegen.

### Auf einen Blick

- Kopfbereich wie bei einer Bestandsumlagerung, mit Übernahme der Lager in die Zeilen und geschütztem Lager des
  Lohnfertigers nach den ersten Bewegungen.
- Chargen und Seriennummern werden im Add-on ausgewählt: Vorschlag aus den Chargen des Auftrags beim Lohnfertiger
  (Rückverfolgbarkeit) und FEFO, von Hand änderbar; Charge des eingehenden Produkts aus einem konfigurierbaren
  SQL-Skript; Produkteingang in einer einzigen Transaktion.
- Registerkarte Belege mit allen verknüpften Belegen, gruppiert und direkt zu öffnen.
- Produktkosten bei jedem Speichern neu berechnet; Bestellung automatisch abgeglichen.
- Lohnfertigungsaufträge aus Produktionsaufträgen, Massenumlagerung und Umlagerung zwischen Aufträgen, massenweises
  Schließen der Wareneingänge.
- Gleiche Arbeitsweise unter SQL Server und SAP HANA; übersetzbare Texte.

## 2. Installation und Menüs

### Installation

- Das Paket `XEI.ContoLavoro.zip` wird im Extension Manager von SAP Business One importiert.
- Beim ersten Start legt das Add-on Tabellen, Felder, das Objekt (UDO) `XEI_CL_COMMESSA` und die formatierte Suche
  des Lohnfertiger-Lieferanten am Lager an. SAP fragt nach der Bestätigung, dass *„die Datenbankstruktur geändert
  wurde“*: antworten und das Ende abwarten, bevor Sie den Client verwenden.

### Menüs

**Module › Administration › Add-Ons › XEI-Addon › Lohnfertigung**:

| Eintrag | Funktion |
|---|---|
| Lohnfertigungsauftrag | Öffnen, Suchen und Anlegen der Lohnfertigungsaufträge |
| Aufträge aus Produktionsaufträgen anlegen | Lohnfertigungsaufträge aus den externen Bearbeitungen der Produktionsaufträge (Kapitel 6) |
| Eingang vom Lohnfertiger | ein Lieferschein des Lohnfertigers mit Produkten mehrerer Aufträge: Sie wählen den Lieferanten, geben die erhaltenen Mengen bei den offenen Produkten seiner Aufträge ein (*Vorschlagen* = offene Menge), und *Buchen* führt den Produkteingang Auftrag für Auftrag durch, mit Eingang der Produkte und Ausgang der Komponenten |
| Massenumlagerung Komponenten | Komponentenversand für mehrere Aufträge (aktiv mit der entsprechenden Option) |
| Komponenten zwischen Aufträgen umlagern | verschiebt den bereits beim Lohnfertiger liegenden Bestand von einem Auftrag in einen anderen |
| Wareneingänge Produkte massenweise schließen | schließt die noch offenen Wareneingänge der Produkte |
| Bearbeitungspreise Lohnfertiger | Preise der Bearbeitungen pro Lieferant und Produkt |
| Konfiguration | Optionen des Add-ons |
| Informazioni (Informationen), Traduzioni (Übersetzungen), Licenza (Lizenz) | gemeinsame Einträge der XEI-Add-ons; Licenza: Status und Lizenzcode |

Dieselben Einträge, außer *Konfiguration*, *Informazioni*, *Traduzioni* und *Licenza*, gibt es auch in dem in der
Konfiguration gewählten SAP-Modul (Kapitel 3), an der gewählten Position: **Module › Einkauf - Kreditoren ›
Lohnfertigung** (Standard) oder **Module › Produktion › Lohnfertigung**.

### Lizenz

Das Add-on arbeitet mit einem von XEI ausgestellten **Lizenzcode**. Nach der Anforderung der Testphase erhalten Sie
per E-Mail einen **Testcode**, der 30 Tage ab Versand in jeder Firma gilt; für den Kauf senden Sie XEI die beiden
Codes des Fensters **Licenza** (Lizenz) und erhalten den Lizenzcode.

- Ohne gültigen Code ist das Add-on **gesperrt**: In seinem Menü bleiben nur *Informazioni* (Informationen) und
  *Licenza* (Lizenz), und beim Start öffnet sich von selbst das Fenster **Licenza** mit dem Status und dem Grund.
- Das Fenster zeigt den **Code der Firma** und den **Code des Servers**: Um die Lizenz zu kaufen, senden Sie sie mit
  *Copia* (Kopieren) an [license@xeisrl.com](mailto:license@xeisrl.com).
- Ein SAP-Benutzer mit **Superuser**-Rechten fügt den erhaltenen Code in *Inserisci un codice di licenza* (Lizenzcode
  eingeben) ein und klickt auf *Salva codice* (Code speichern): Das Add-on wird sofort entsperrt, ohne SAP neu zu
  starten.
- Der Lizenzcode gilt für die Firma (Datenbank) oder für den Server der gesendeten Codes.
- Dasselbe Fenster öffnet sich jederzeit über das Menü *Licenza*: Status, Ablaufdatum, Nummer und Geltungsbereich der
  Lizenz.

## 3. Konfiguration

Die Optionen werden in einem Formular mit Registerkarten eingestellt (die Registerkarte *Chargen* ist in Kapitel 7
beschrieben). Die Optionen gelten für die gesamte Firma; bereits geöffnete Formulare verwenden sie beim erneuten
Öffnen.

![Preise](../../_img/contolavoro/11_config_prezzi.png)

*Preise*

![Lager](../../_img/contolavoro/12_config_magazzino.png)

*Lager*

| Option | Wirkung | Standard |
|---|---|---|
| **Allgemein** | | |
| Ursprüngliche Bestellung | Feld, um den Auftrag mit der Bestellung zu verknüpfen, aus der er entsteht | Nein |
| Ursprünglicher Kundenauftrag | Spalte Kundenauftrag in den Produktzeilen | Nein |
| Produkte ohne Stückliste | erlaubt Produkte ohne Stückliste: Sie wird von Hand zusammengestellt | Nein |
| Wareneingang des Produkts schließen | nach dem Produkteingang wird der Wareneingang des Produkts geschlossen (er wird nicht fakturiert) | Nein |
| Preis des Produkt-Wareneingangs neu berechnen | wenn sich der Bearbeitungspreis ändert, wird der Wareneingang des Produkts aktualisiert | Nein |
| Lieferantenangebote aus Produktionsaufträgen | verknüpft beim Anlegen aus Produktionsaufträgen die Lieferantenangebote | Nein |
| Massenumlagerung | aktiviert den Menüeintrag | Nein |
| Stückliste Lohnfertiger | zeigt die Spalte „Stückliste Lohnfertiger“ in der Stückliste | Ja |
| Lieferantenrahmenverträge | Bearbeitungspreise aus den Rahmenverträgen (nur SQL Server) | Nein |
| Standardpreisliste | Kostenliste, die bei neuen Aufträgen vorgeschlagen wird | – |
| Menü auch im SAP-Modul | Modul mit dem Untermenü *Lohnfertigung*: Einkauf - Kreditoren oder Produktion | Einkauf - Kreditoren |
| Position im Modulmenü | am Ende, am Anfang oder nach einem Eintrag des Moduls | am Ende |
| **Preise** | | |
| Bearbeitungs- / Komponentenpreis änderbar | Preise in der Stückliste des Auftrags änderbar | Nein |
| Bearbeitungs- / Komponentenpreis aus der Stückliste | vorrangig der Preis der Stückliste (Komponente: nur Produktionsaufträge) | Nein |
| Bearbeitungskosten verteilen | verteilt die Gesamtkosten auf die Produkte (nur aus Produktionsaufträgen) | Nein |
| Bei Nullpreisen nicht sperren | der Produkteingang ist auch mit Nullpreisen erlaubt | Nein |
| Komponenten neu bewerten | Neubewertung der Komponenten bei der Produktionsentnahme (permanente Inventur) | Nein |
| **Lager** | | |
| Standardlager des Artikels | die Komponentenzeilen gehen vom Standardlager des Artikels aus | Ja |
| Bestand als versendet | für die angegebenen Komponenten gilt der Bestand beim Lohnfertiger als versendet | Nein |
| Komponenten pro Zeile | Komponenten pro Produkt getrennt gehalten | Nein |
| Variabler Bedarf | verteilt die versendete Menge auf die Produkte | Nein |
| Umlagerungsanforderungen | Komponentenversand mit einer Bestandsumlagerungsanforderung statt der Bestandsumlagerung | Nein |
| Pickliste | erstellt auch die Pickliste (aktiviert die Anforderungen) | Nein |
| **Serien und Gründe** | | |
| Serien | Bestellung, Wareneingänge der Produkte und Bearbeitungen, Umlagerungen | SAP-Standard |
| Transportgründe | für Umlagerungen, Bestellung, Wareneingang, Ausgänge, Eingänge (wenn die Firma Transportgründe verwendet) | – |
| **Chargen** | | |
| Skript für die eingehende Charge | SQL mit {ItemCode}, {WhsCode}, {DocEntry}, das die Charge des eingegangenen Produkts liefert (siehe Kapitel 7) | Auftrag-laufende Nummer |

## 4. Der Lohnfertigungsauftrag

### Kopfbereich

Der Kopfbereich ist wie der der Bestandsumlagerung aufgebaut: links Lieferant, Referenz des Lieferanten, Projekt und
verknüpfte Bestellungen; rechts Nummerierung, Status, Daten, Kostenliste und die beiden Lager.

- **Lieferant**: Bei der Auswahl werden das Lager des Benutzers und das mit dem Lieferanten verknüpfte **Lager des
  Lohnfertigers** vorgeschlagen (Feld *Fornitore terzista* (Lieferant Lohnfertiger) der Lagerstammdaten) oder das als
  Standard markierte.
- **Von Lager**: Lager des Unternehmens; von hier gehen die Komponenten ab, hierher kehren die Produkte zurück, und auf
  diesem Lager entstehen die Zeilen der Bestellung.
- **Lager LF**: kann nur geändert werden, solange der Auftrag keine Komponentenbewegungen hat; danach wird das Feld
  deaktiviert, und das Speichern lehnt die Änderung in jedem Fall ab.
- Wenn ein Lager im Kopfbereich geändert wird, wird wie bei der Bestandsumlagerung angeboten, es in die **noch nicht
  bewegten** Zeilen der Stückliste zu übernehmen.

### Produkte

Sie wählen den Artikel (auch mehrere Artikel gleichzeitig aus der Liste) und die zu produzierende Menge: Die Stückliste
wird aus SAP kopiert und auf ein Stück umgerechnet (unter Berücksichtigung der Basismenge der Stückliste). Die Spalten
zeigen zu produzierende Menge, eingegangene Menge, offene Menge, Kosten der Komponenten und der Bearbeitungen.

### Stückliste

Für jedes Produkt: Komponenten (zu versendende Lagerartikel) und Bearbeitungen (an den Lohnfertiger bezahlte
Dienstleistungen). Mit **Stückliste ändern** ändern Sie Lager und Preise der noch nicht bewegten Zeilen; mit *Zeile
hinzufügen* / *Zeile löschen* von SAP fügen Sie Komponenten und Bearbeitungen hinzu oder entfernen die nicht bewegten.
Im Kontextmenü der Produktzeile: **Nacharbeiten** (das Produkt geht als Komponente mit den neuen Bearbeitungen an den
Lohnfertiger zurück) und **Stückliste neu zusammenstellen** (ersetzt die Stückliste durch die gewählten Komponenten).

### Komponenten

Die Komponenten aller Produkte, gruppiert nach Artikel und Lagern: Bedarf, verwendet, verfügbar im Unternehmen,
Bestand im Lager des Lohnfertigers, Anforderungen und Picklisten, versendet, noch zu versenden, Bestand des Auftrags
beim Lohnfertiger, Rückholungen und Ausschuss. Die Bewegungen erfolgen mit den Schaltflächen unten im Auftrag:
**Komponenten versenden** und **Rückholung und Ausschuss** (*Komponenten vom Lohnfertiger zurückholen*, *Ausschuss
umlagern*, *Ausschuss beim Lohnfertiger ausbuchen*). Jede öffnet ein Fenster mit den zu bewegenden Mengen in den gelben
Zellen: *Vorschlagen* füllt sie, *Zurücksetzen* leert sie, und sie können von Hand geändert werden.

### Belege

Alle mit dem Auftrag verknüpften SAP-Belege, einer pro Zeile in zeitlicher Reihenfolge, mit der Verknüpfung zum
Öffnen; *Anzeigen* filtert nach Belegart. Darunter, in *Belegzeilen*, die Zeilen des gewählten Belegs mit Chargen,
Seriennummern und Lagerplätzen.

## 5. Ablauf

1. **Lohnfertigungsauftrag**: Lieferant, Lager, Produkte und Mengen; *Hinzufügen*.
2. **Bestellung Lohnfertiger**: Das Fenster *Bestellung an Lohnfertiger* legt die Bestellung an, mit einer Zeile pro
   Produkt und einer für jede Bearbeitung; wenn die Bestellung bereits existiert, öffnet die Schaltfläche sie. Spätere
   Änderungen am Auftrag (neue oder gelöschte Produkte, Mengen, Preise, Daten) werden beim Speichern in die Bestellung
   übernommen; bereits gelieferte Zeilen ändern sich nur in der Menge.
3. **Komponenten versenden**: Im Fenster *Umlagerung Komponenten* schlägt die Spalte *Zu versenden* die noch zu
   versendende Menge vor (von Hand änderbar); *OK* legt die Bestandsumlagerung zum Lager des Lohnfertigers an. Mit der
   entsprechenden Option wird eine Bestandsumlagerungsanforderung mit Pickliste angelegt.
4. **Produkte empfangen**: Im Fenster *Produkteingang* schlägt die Spalte *Einzugehen* die offene Menge vor (von Hand
   änderbar), und *Bewegungsart* wählt zwischen *Produkteingang und Komponentenausgang*, *Nur Produkteingang* und *Nur
   Komponentenausgang*; dann *OK*. Angelegt werden: Wareneingang der Bearbeitungen und der Produkte aus der
   Bestellung, Warenausgang der Komponenten aus dem Lager des Lohnfertigers, Eingänge aus Produktion für die Produkte
   aus Produktionsaufträgen (Kapitel 6).

> Das Produkt wird zu den vollen Kosten eingebucht (Komponenten + Bearbeitung); mit der Option „Wareneingang des
> Produkts schließen“ wird der Wareneingang geschlossen und nicht fakturiert: Fakturiert werden die Bearbeitungen.

Wenn eine auszubuchende Komponente den Bestand des Auftrags beim Lohnfertiger überschreitet, wird gefragt, ob der
restliche Bestand ausgebucht werden soll (Ja / Nein / Ja für alle).

## 6. Lohnfertigung aus Produktionsaufträgen

Wenn einige Arbeitsgänge eines **Produktionsauftrags** bei Lohnfertigern ausgeführt werden, legt das Add-on die
Lohnfertigungsaufträge aus den Zeilen des Produktionsauftrags an. Bei jedem Produkteingang entnimmt es für den
Produktionsauftrag die vom Lohnfertiger verbrauchten Komponenten und bucht, wenn alle externen Bearbeitungen
zurückgekommen sind, den Eingang aus Produktion des Fertigprodukts.

### Einrichtung in SAP

> Die externe Bearbeitung ist ein **Nicht-Lagerartikel** mit dem Feld **Conto lavoro** (Lohnfertigung) = Ja, keine
> SAP-Ressource: Eine als Ressource eingerichtete Bearbeitung erscheint nicht in der Liste der Produktionsaufträge.

| Wo | Was Sie einstellen | Im Beispiel |
|---|---|---|
| Artikelstammdaten des Bearbeitungsartikels | Nicht-Lagerartikel, Benutzerfeld **Conto lavoro** (Lohnfertigung) = Ja; der **bevorzugte Lieferant** ist der Lohnfertiger, der in der Liste vorgeschlagen wird | `LAV-SALD` Rahmen schweißen, Lieferant `F-TER01`; `LAV-MONT` Achse montieren, Lieferant `F-TER02` |
| Stückliste des Fertigprodukts | eine Zeile für jede externe Bearbeitung, mit der Menge pro Stück; in den Zeilen der Komponenten, die an den Lohnfertiger gehen, das Feld **Lavorazione terzista** (Bearbeitung Lohnfertiger) mit dem Code der Bearbeitung und die Ausgabemethode **Manuell** | `CMP-01`, `CMP-02` → `LAV-SALD`; `CMP-03`, `CMP-04` → `LAV-MONT` |
| Stückliste des Fertigprodukts | **Stückliste Lohnfertiger** = Ja, wenn das Fertigprodukt vollständig ist, sobald alle externen Bearbeitungen zurückgekommen sind: Das Add-on bucht den Eingang aus Produktion. Mit Nein buchen Sie den Eingang aus Produktion selbst in SAP | `PF-100` = Ja |
| Lagerstammdaten des Lohnfertigers | Feld **Fornitore terzista** (Lieferant Lohnfertiger) (Kapitel 4) | `T-TER01` → `F-TER01`; `T-TER02` → `F-TER02` |
| *Bearbeitungspreise Lohnfertiger* | Preis pro Lohnfertiger, Fertigprodukt und Bearbeitung (Reihenfolge der Preissuche in Kapitel 9) | `F-TER01` / `PF-100` / `LAV-SALD` 12,00; `F-TER02` / `PF-100` / `LAV-MONT` 3,50 |

Retrograde Komponenten, die mit der Bearbeitung verknüpft sind, werden nicht an den Lohnfertiger gesendet: Der Eingang
aus Produktion entnimmt sie aus dem Lager der Zeile des Produktionsauftrags. Die Spalte **Grund / Hinweise** der Liste
weist darauf hin. Die übrigen Komponenten der Stückliste, die keine Bearbeitung haben, bleiben wie in jedem
Produktionsauftrag.

> **Prüfung beim Speichern der Stückliste.** Wenn Sie eine Stückliste speichern, in der das Feld **Lavorazione
> terzista** (Bearbeitung Lohnfertiger) ausgefüllt ist, prüft das Add-on die angegebenen Codes. Wenn etwas nicht
> stimmt, erscheint der Hinweis *„Stückliste PF-100, Feld "Lavorazione terzista":“* mit einem Punkt für jeden Fall;
> die Stückliste bleibt gespeichert.
>
> - Ressource: *„LAV-SALD ist eine Ressource: Die externe Bearbeitung muss als Nicht-Lagerartikel mit "Conto lavoro"
>   = Ja angelegt und die Komponenten mit diesem Code verknüpft werden.“*
> - Code, der kein Artikel ist: *„LAV-SALD ist kein Artikel.“*
> - Artikel ohne Conto lavoro: *„Artikel LAV-SALD hat in den Artikelstammdaten nicht "Conto lavoro" = Ja.“*
> - Bearbeitung, die keine Zeile der Stückliste ist: *„LAV-SALD ist keine Zeile der Stückliste: Der Produktionsauftrag
>   hat dann keine Zeile für die Bearbeitung und der Lohnfertigungsauftrag kann nicht angelegt werden.“*
> - Retrograde Komponenten: *„Retrograde Komponenten mit der Bearbeitung LAV-SALD: Sie werden nicht an den
>   Lohnfertiger gesendet (manuelle Ausgabemethode erforderlich).“*

### Beispiel Schritt für Schritt

Das Fertigprodukt `PF-100` Wagen hat zwei externe Bearbeitungen: das Schweißen des Rahmens bei `F-TER01`
„Lohnfertiger Beispiel 1“ und die Montage der Achsen bei `F-TER02` „Lohnfertiger Beispiel 2“. Jeder Wagen hat einen
Rahmen und zwei Achsen. Der Produktionsauftrag Nr. 500 ist für 100 Wagen im Lager `01` freigegeben:

| Zeile | Artikel | Menge | Ausgabe | Lavorazione terzista | Preis |
|---|---|---|---|---|---|
| 1 | `LAV-SALD` Rahmen schweißen (Bearbeitung) | 100 | | | 12,00 |
| 2 | `CMP-01` Rohr (m) | 250 | Manuell | `LAV-SALD` | 4,00 |
| 3 | `CMP-02` Platte | 400 | Manuell | `LAV-SALD` | 1,50 |
| 4 | `LAV-MONT` Achse montieren (Bearbeitung) | 200 | | | 3,50 |
| 5 | `CMP-03` Rad | 400 | Manuell | `LAV-MONT` | 5,00 |
| 6 | `CMP-04` Bolzen | 200 | Manuell | `LAV-MONT` | 2,00 |
| 7 | `CMP-05` Schraube | 1.600 | retrograd | | |

| Schritt | Angelegter SAP-Beleg | Wirkung auf den Produktionsauftrag |
|---|---|---|
| 1. **Lohnfertigung › Aufträge aus Produktionsaufträgen anlegen**: Sie markieren die beiden Zeilen des Produktionsauftrags 500 und klicken auf *Aufträge anlegen* | kein SAP-Beleg: Lohnfertigungsauftrag 1001 (`F-TER01`, von `01` nach `T-TER01`, Produkt `LAV-SALD` 100, Stückliste `CMP-01` 2,5 und `CMP-02` 4 pro Stück) und Auftrag 1002 (`F-TER02`, von `01` nach `T-TER02`, Produkt `LAV-MONT` 200, Stückliste `CMP-03` 2 und `CMP-04` 1 pro Stück) | keine |
| 2. Klicken Sie in jedem Auftrag auf *Bestellung Lohnfertiger* und bestätigen Sie das Fenster *Bestellung an Lohnfertiger* | Bestellung an `F-TER01`: `LAV-SALD` 100 × 12,00; Bestellung an `F-TER02`: `LAV-MONT` 200 × 3,50 | keine |
| 3. Klicken Sie in jedem Auftrag auf *Komponenten versenden* und, mit den vorgeschlagenen Mengen, auf *OK* | Bestandsumlagerung von `01` nach `T-TER01`: `CMP-01` 250, `CMP-02` 400; von `01` nach `T-TER02`: `CMP-03` 400, `CMP-04` 200 | keine |
| 4. 60 Rahmen kommen zurück: Klicken Sie im Auftrag 1001 auf *Produkte empfangen*, geben Sie im Fenster *Produkteingang* 60 in *Einzugehen* ein und klicken Sie auf *OK* | Wareneingang aus der Bestellung: `LAV-SALD` 60 × 12,00; Ausgabe für Produktion aus `T-TER01`: `CMP-01` 150, `CMP-02` 240 | Komponenten der Zeilen 2 und 3 entnommen; kein Eingang: Die Achsen fehlen, und eine Meldung weist darauf hin (*„Produktionsauftrag 500: Das Fertigprodukt wird eingelagert, sobald auch die Bearbeitung LAV-MONT zurückkommt.“*) |
| 5. 100 Achsen kommen zurück: Auftrag 1002, *Produkte empfangen*, 100 in *Einzugehen*, *OK* | Wareneingang `LAV-MONT` 100 × 3,50; Ausgabe für Produktion aus `T-TER02`: `CMP-03` 200, `CMP-04` 100; Eingang aus Produktion `PF-100` **50** | 60 Rahmen und 100 Achsen reichen für 50 Wagen: 50 fertiggestellt; SAP entnimmt retrograd `CMP-05` 800 |
| 6. Weitere 100 Achsen kommen zurück: Auftrag 1002, *Produkte empfangen*, 100 in *Einzugehen*, *OK* | Wareneingang `LAV-MONT` 100; Ausgabe für Produktion `CMP-03` 200, `CMP-04` 100; Eingang aus Produktion `PF-100` **10** | 60 fertiggestellt, die übrigen warten auf die Rahmen (*„Produktionsauftrag 500: 10 Stück des Fertigprodukts eingelagert; die übrigen folgen, sobald auch die Bearbeitung LAV-SALD zurückkommt.“*); der Auftrag 1002 schließt sich von selbst |
| 7. Die letzten 40 Rahmen kommen zurück: Auftrag 1001, *Produkte empfangen*, 40 in *Einzugehen*, *OK* | Wareneingang `LAV-SALD` 40; Ausgabe für Produktion `CMP-01` 100, `CMP-02` 160; Eingang aus Produktion `PF-100` **40** | 100 fertiggestellt; der Auftrag 1001 schließt sich von selbst. Den Produktionsauftrag schließen Sie selbst in SAP |

> Der Eingang aus Produktion wird mit den Kosten der externen Bearbeitungen pro Stück bewertet: für jede Bearbeitung
> Komponenten und Preis der Bearbeitung, multipliziert mit der Menge pro Stück. Im Beispiel ist ein Wagen
> (2,5 × 4,00 + 4 × 1,50 + 12,00) + 2 × (2 × 5,00 + 1 × 2,00 + 3,50) = 28,00 + 31,00 = **59,00** wert.

### Sonderfälle

- **Mehrere Produktionsaufträge**: Die Zeilen mit demselben Lieferanten und demselben Rückgabelager (Spalte
  *Rückgabelager*) kommen in denselben Auftrag, ein Produkt pro Zeile; bei unterschiedlichen Rückgabelagern entstehen
  unterschiedliche Aufträge.
- **Dienstleistungen des Lohnfertigers**: Eine Nicht-Lager-Komponente mit **Lavorazione terzista** (Bearbeitung
  Lohnfertiger) (zum Beispiel eine Prüfung) wird zu einer Bearbeitung des Auftrags, mit einer zusätzlichen Zeile in
  der Bestellung an den Lohnfertiger.
- **Stückliste Lohnfertiger = Nein**: Das Add-on bucht den Wareneingang der Bearbeitung und den Ausgang der
  Komponenten; den Eingang aus Produktion buchen Sie selbst in SAP, zum Beispiel nach einer internen Montage.
- **In SAP gebuchte Eingänge aus Produktion** zum selben Produktionsauftrag: Das Add-on zieht sie ab, das
  Fertigprodukt wird nicht doppelt eingebucht.
- **Abgebrochener Auftrag**: Wenn Sie einen Lohnfertigungsauftrag abbrechen, kommt die Bearbeitung zurück in die Liste,
  und Sie können einen neuen anlegen.
- **Retrograde Komponenten**: Die mit der Bearbeitung verknüpften retrograden Komponenten werden nicht an den
  Lohnfertiger gesendet; die Spalte **Grund / Hinweise** weist darauf hin.
- **Stückliste des Auftrags**: Bei Produkten aus Produktionsaufträgen wird sie nicht geändert; Sie ändern den Preis
  der Bearbeitung (Spalte *Bearb.-Kosten*), der beim Speichern in die Bestellung an den Lohnfertiger übernommen wird.
  Mit der Option *Bearbeitungskosten verteilen* werden die *Bearb.-Kosten ges.* des Kopfbereichs im Verhältnis zur
  Menge auf die Produkte verteilt.
- Die Option *Wareneingang des Produkts schließen* gilt nicht für Aufträge aus Produktionsaufträgen: Der Wareneingang
  der Bearbeitung bleibt offen, zur Fakturierung.
- **Lieferantenangebote**: Mit der Option *Lieferantenangebote aus Produktionsaufträgen* verknüpft *Lieferantenangebot*
  eine Angebotszeile mit der Zeile, mit ihrem Lieferanten, Preis und Lieferdatum; die nicht gewählten Angebotszeilen
  werden geschlossen.

### Warum ein Produktionsauftrag nicht in der Liste erscheint

Die Liste zeigt die Bearbeitungen, die bereit sind, ein Lohnfertigungsauftrag zu werden. Aktivieren Sie **Auch nicht
bereite Zeilen anzeigen**: Dann erscheinen auch die übrigen, mit dem Grund und dem, was zu tun ist, in der Spalte
**Grund / Hinweise**. Nicht bereite Zeilen können nicht markiert werden; wenn Sie auf ihr Auswahlkästchen klicken,
erscheint der Grund auch in der Statusleiste.

| Grund (Beispiel am Bildschirm) | Was zu tun ist |
|---|---|
| Bereits im Lohnfertigungsauftrag Nr. 1001. | nichts: Öffnen Sie den Auftrag über die Spalte *Auftrag* |
| LAV-SALD ist eine Ressource: Die externe Bearbeitung muss als Nicht-Lagerartikel mit "Conto lavoro" = Ja angelegt und die Komponenten mit diesem Code verknüpft werden. | legen Sie den Artikel der Bearbeitung an und tragen Sie seinen Code in **Lavorazione terzista** (Bearbeitung Lohnfertiger) bei den Komponenten ein |
| Die Komponenten verweisen auf die Bearbeitung LAV-SALD, die kein Artikel ist. | korrigieren Sie **Lavorazione terzista** bei den Komponenten oder legen Sie den Artikel an |
| Artikel LAV-SALD hat in den Artikelstammdaten nicht "Conto lavoro" = Ja. | setzen Sie **Conto lavoro** (Lohnfertigung) = Ja in den Artikelstammdaten |
| Der Produktionsauftrag hat keine Zeile für die Bearbeitung LAV-SALD: sie im Produktionsauftrag (oder in der Stückliste des Produkts) hinzufügen. | fügen Sie die Zeile dem Produktionsauftrag hinzu oder der Stückliste für die nächsten Produktionsaufträge |
| Keine zu sendenden Komponenten: in den Komponentenzeilen "Lavorazione terzista" = LAV-SALD und die manuelle Ausgabemethode angeben. | füllen Sie die zu sendenden Komponenten aus, mit der Ausgabemethode Manuell |
| Produktionsauftrag nicht freigegeben: in SAP freigeben. | geben Sie den Produktionsauftrag frei |

Eine als SAP-Ressource eingerichtete Bearbeitung ist eine häufige Ursache: Die externe Bearbeitung muss als
Nicht-Lagerartikel mit **Conto lavoro** (Lohnfertigung) = Ja angelegt werden.

In den bereiten Zeilen gibt dieselbe Spalte die Hinweise, die die Auswahl nicht verhindern:

| Hinweis | Was zu tun ist |
|---|---|
| Retrograde Komponenten mit dieser Bearbeitung: Sie werden nicht an den Lohnfertiger gesendet (manuelle Ausgabemethode erforderlich). | wenn sie versendet werden sollen, stellen Sie die Ausgabemethode Manuell ein |
| Lieferanten angeben. | wählen Sie den Lieferanten in der Spalte *Lieferant* |
| Lieferant F-TER01 hat kein verknüpftes Lager des Lohnfertigers. | verknüpfen Sie das Lager des Lohnfertigers mit dem Lieferanten (Feld **Fornitore terzista** (Lieferant Lohnfertiger)): ohne dieses wird der Auftrag nicht angelegt |

## 7. Chargen, Seriennummern und Lagerplätze

Für Umlagerungen, Rückholungen, Ausschuss und den Komponentenausgang beim Produkteingang werden Chargen und
Seriennummern in einem Fenster des Add-ons ausgewählt, **bevor** die Belege angelegt werden. Alle Belege werden dann
in einem einzigen Vorgang angelegt.

- **Automatischer Vorschlag**: aus dem Lager des Lohnfertigers (Komponentenausgang, Rückholung, Ausschuss) zuerst die
  **an diesen Auftrag versendeten** Chargen (Spalte „Des Auftrags“, ermittelt aus dem Chargentransaktionsprotokoll von
  SAP), dann nach Verfallsdatum (FEFO); aus dem Lager des Unternehmens nach Verfallsdatum (FEFO).
- **Manuelle Auswahl**: Die Spalte „Zu verwenden“ ist änderbar; die Menge ist auf den Bestand der Charge (abzüglich
  anderer Zeilen mit derselben Charge) und bei Seriennummern auf 1 begrenzt. *Vorschlagen* erstellt den Vorschlag neu,
  *Zurücksetzen* leert alles. Die Bestätigung ist nur möglich, wenn jede Zeile genau die angeforderte Menge hat.
- Vorgeschlagen werden nur **freigegebene** Chargen und Seriennummern (weder gesperrt noch nicht zugänglich).
- Bestandsumlagerungsanforderungen bewegen keine Chargen: Für sie öffnet sich keine Auswahl.

### Charge des eingehenden Produkts

Die Charge des eingegangenen Produkts wird von einem konfigurierbaren **SQL-Skript** berechnet (Konfiguration ›
Chargen), mit drei festen Parametern: `{ItemCode}` Artikel, `{WhsCode}` Eingangslager, `{DocEntry}`
Lohnfertigungsauftrag. Das Standardskript liefert Auftragsnummer + laufende Nummer (z. B. `20160256-1`); *Prüfen*
führt es mit Testdaten aus. Die angelegte Charge erscheint in der Meldung am Ende des Produkteingangs.

![Skript für die Charge des eingehenden Produkts](../../_img/contolavoro/19_config_lotti.png)

*Skript für die Charge des eingehenden Produkts*

### Belege als Entwurf

Der Beleg wird als Entwurf angelegt, der im SAP-Formular zu vervollständigen ist, bei Lagern mit **Lagerplätzen**,
eingehenden Produkten mit **Seriennummern**, leerem Chargenskript oder einem ohne Ergebnis und bei der
Massenumlagerung. Sie vervollständigen den Beleg und klicken auf *Hinzufügen*: Das Add-on löscht den Entwurf und fährt
fort.

## 8. Rückholungen und Ausschuss

- **Rückholung und Ausschuss › Komponenten vom Lohnfertiger zurückholen**: Menge in *Zurückzuholen* (*Vorschlagen* =
  Bestand des Auftrags beim Lohnfertiger), dann *OK*: Umlagerung vom Lager des Lohnfertigers in das Lager des
  Unternehmens.
- **Rückholung und Ausschuss › Ausschuss umlagern**: Menge in *Auszusondern*; verschiebt den Ausschuss vom
  Lohnfertiger in ein Lager nach Wahl.
- **Rückholung und Ausschuss › Ausschuss beim Lohnfertiger ausbuchen**: im Fenster *Ausschuss-Warenausgang*
  Warenausgang des Ausschusses direkt aus dem Lager des Lohnfertigers.

Ausgesonderte Komponenten kehren in die noch zu versendende Menge zurück.

## 9. Hilfsfunktionen

### Aufträge aus Produktionsaufträgen

Listet die externen Bearbeitungen der freigegebenen Produktionsaufträge auf, die bereit sind, ein Auftrag zu werden,
und legt **einen Auftrag pro Lieferant und Rückgabelager** an. Mit *Auch nicht bereite Zeilen anzeigen* erklärt es,
warum eine Bearbeitung nicht bereit ist. Einrichtung, vollständiges Beispiel und Sonderfälle in Kapitel 6.

### Massenumlagerung Komponenten

Analysiert die offenen Aufträge (Filter nach Daten, Lieferant, Komponente) und schlägt die Komponenten mit noch zu
versendender Menge vor, unter Beachtung der zwischen den Aufträgen geteilten Verfügbarkeit, wenn die Firma negative
Bestände sperrt. Legt eine Umlagerung pro Lieferant an (als Entwurf, wenn Chargen oder Lagerplätze nötig sind). Zeilen
mit fehlendem Lager des Lohnfertigers oder einem, das dem Ausgangslager entspricht, werden ausgeschlossen und gemeldet.

### Komponenten zwischen Aufträgen umlagern

Verschiebt den bereits beim Lohnfertiger liegenden Bestand von einem Auftrag in einen anderen ohne Lagerbewegungen
(nur Erfassung). Deshalb ist es nur zwischen **offenen** Aufträgen mit **demselben Lager des Lohnfertigers** möglich:
Die Liste schlägt nur diese vor; bei unterschiedlichen Lagern ist der Vorgang gesperrt, und die Ware muss
zurückgeholt und erneut versendet werden. Der Bestand wird im Moment der Bestätigung neu gelesen.

### Wareneingänge Produkte massenweise schließen und Bearbeitungspreise

*Wareneingänge Produkte massenweise schließen* listet die noch offenen Wareneingänge der Produkte auf und schließt die
gewählten. *Bearbeitungspreise Lohnfertiger* ist die Tabelle der Bearbeitungspreise pro Lohnfertiger und Produkt.

Reihenfolge der Suche nach dem Preis einer Bearbeitung: Lieferantenrahmenverträge (Option, nur SQL Server), Preise pro
Lohnfertiger, Stückliste (Option), Lieferantenpreis aus SAP, Preisliste des Auftrags.

## 10. Daten, Felder und Bewegungsarten

| Tabelle | Inhalt |
|---|---|
| `@XEI_CL_OCNT` | Kopf des Auftrags (UDO `XEI_CL_COMMESSA`, mit Serien) |
| `@XEI_CL_CNT1` | Produkte |
| `@XEI_CL_CNT2` | Stückliste (Komponenten und Bearbeitungen) |
| `@XEI_CL_PRZLAV` | Bearbeitungspreise pro Lohnfertiger und Produkt |
| `@XEI_CL_TRCOMM` | Umlagerungen zwischen Aufträgen |

Felder in den SAP-Tabellen (Präfix `XEI_CL_`):

| Feld | Tabellen | Inhalt |
|---|---|---|
| `U_XEI_CL_ENTRY` | Belegzeilen | Lohnfertigungsauftrag (DocEntry) |
| `U_XEI_CL_LINENUM` | Belegzeilen | Produkt- oder Stücklistenzeile |
| `U_XEI_CL_TYPE` | Belegzeilen | Bewegungsart (Tabelle unten) |
| `U_XEI_CL_TXT`, `U_XEI_CL_OPIT`, `U_XEI_CL_ITEM`, `U_XEI_CL_WKEY`, `U_XEI_CL_ENBL` | Belegzeilen | Text, Bezugsartikel und Bezugsproduktionsauftrag, verwendbare Angebote |
| `U_XEI_CL_ICNT` | Artikel | Artikel in Lohnfertigung |
| `U_XEI_CL_TERZF`, `U_XEI_CL_DFTR` | Lager | Lohnfertiger-Lieferant des Lagers, Standardlager des Lohnfertigers |
| `U_XEI_CL_DISTTERZ` | Stücklisten | Stückliste Lohnfertiger (Eingang aus Produktion aus Produktionsaufträgen) |
| `U_XEI_CL_ILAV` | Zeilen von Stückliste und Produktionsauftrag | Bearbeitung, zu der die Komponente gehört |

Wenn die Firma sie verwendet, füllt das Add-on auch Handelscode, Transportgrund, Frachtbedingungen und Spediteur der
Belege aus.

| Typ | Beleg | Bedeutung |
|---|---|---|
| EMP | Bestellung, Wareneingang | Produkt |
| OAL | Bestellung, Wareneingang | Bearbeitung |
| UMC | Warenausgang (Ausgabe für Produktion, wenn aus Produktionsauftrag) | verbrauchte Komponenten |
| TSO | Bestandsumlagerung oder Anforderung | an den Lohnfertiger gesendete Komponenten |
| TSI | Bestandsumlagerung | Rückholung Komponenten |
| TSS | Bestandsumlagerung | Umlagerung Ausschuss |
| UMR | Warenausgang | Ausschuss beim Lohnfertiger |
| EPR | Eingang aus Produktion | Fertigprodukt des Produktionsauftrags (Kapitel 6) |

Stornierte Belege werden in den Berechnungen nicht berücksichtigt, und Rücksendungen werden Zeile für Zeile abgezogen.

## 11. Sprachen

Das Add-on folgt der Sprache des SAP-Clients. Verfügbar sind **Italienisch** (Basissprache), **Englisch**,
**Deutsch**, **Französisch**, **Spanisch** und **Türkisch**: Menüs, Formulare, Spalten, Schaltflächen, Meldungen und
Bemerkungen der angelegten Belege. Bei einer nicht vorgesehenen Sprache wird Italienisch verwendet.

| SAP-Sprache | Texte des Add-ons | Commessa terzista | Terzista |
|---|---|---|---|
| Italian (Italy) | Italienisch | Commessa terzista | terzista |
| English (United States / United Kingdom) | Englisch | Subcontracting Job | subcontractor |
| German | Deutsch | Lohnfertigungsauftrag | Lohnfertiger |
| French | Französisch | Ordre de sous-traitance | sous-traitant |
| Spanish (Spain / Latin America) | Spanisch | Orden de subcontratación | subcontratista |
| Turkish | Türkisch | Fason iş emri | fasoncu |

Die Begriffe folgen denen von SAP Business One in derselben Sprache (zum Beispiel *Vendor*, *Posting Date*,
*Inventory Transfer*, *Bill of Materials*, *Batch* auf Englisch; *Tedarikçi*, *Kayıt tarihi*, *Stok nakli*, *Ürün
ağacı*, *Parti* auf Türkisch).

### Sprache wechseln

1. **Administration › Einstellungen › Allgemein › Benutzer**, Registerkarte *Anzeige*, Feld *Sprache*, dann
   *Aktualisieren*.
2. SAP weist darauf hin, dass alle geöffneten Fenster geschlossen werden: mit *Ja* antworten.
3. Das Add-on lädt die Texte von selbst neu und erstellt die Menüs in der neuen Sprache: Ein Neustart ist nicht nötig.

### Texte anpassen

Jeder Text kann für den einzelnen Kunden über das Menü **Traduzioni** (Übersetzungen) des Add-ons oder mit der rechten
Maustaste in den Formularen geändert werden (*Modifica testo…* (Text bearbeiten…), *Testi di questa form…* (Texte
dieses Formulars…)). Dafür ist die Berechtigung `XEI_TEXTS` nötig (Superuser haben sie immer). Die Anpassungen bleiben
bei Updates des Add-ons erhalten.

Auf Italienisch bleiben die Texte, die SAP in der Datenbank speichert, zum Beispiel die Beschreibungen der
Benutzerfelder und der Titel der Tabelle *Prezzi lavorazioni terzisti* (Bearbeitungspreise Lohnfertiger). Die Einträge
*Informazioni*, *Traduzioni* und *Licenza* des Frameworks sind mit ihren Fenstern in allen Sprachen auf Italienisch.
