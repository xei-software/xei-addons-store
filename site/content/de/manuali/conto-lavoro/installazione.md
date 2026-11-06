---
title: XEI.ContoLavoro – Installation, Lizenz und Menüs
description: So installieren Sie XEI.ContoLavoro, aktivieren die Lizenz und finden die Menüs.
lang: de
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Installation, Lizenz und Menüs

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| System | Microsoft .NET Framework 4.8 auf dem PC des SAP-Clients |
| Programmsprachen | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |

## Installation

1. Laden Sie das Paket `XEI.ContoLavoro.zip` herunter.
2. Öffnen Sie in SAP Business One den **Extension Manager**, importieren Sie das Paket und ordnen Sie es der Firma zu.
3. Beim ersten Start legt das Add-on Tabellen, Felder, das Objekt des Lohnfertigungsauftrags und die formatierte Suche
   des Lohnfertiger-Lieferanten im Lager an. SAP zeigt die Meldung, dass die Datenbankstruktur geändert wurde:
   Antworten Sie mit **Ja** und warten Sie das Ende ab, bevor Sie den Client verwenden.

Jede Aktualisierung des Add-ons wird auf die gleiche Weise installiert.

Nach der Installation: die **Konfiguration** ausfüllen, dann in SAP jedem Lager des Lohnfertigers seinen Lieferanten
zuordnen (Feld *Fornitore terzista* (Lieferant Lohnfertiger) in den Lagerstammdaten) und die Artikel in Lohnfertigung
kennzeichnen (Benutzerhandbuch, Kapitel 3 und 6).

## Lizenz

Das Add-on arbeitet mit einem **Lizenzcode**, den XEI ausstellt.

- **Test**: Nach der Anforderung des Tests erhalten Sie per E-Mail einen **Testcode**, der ab dem Versand 30 Tage in
  jeder Firma gültig ist.
- **Kauf**: Sie senden XEI die beiden Codes aus dem Fenster **Licenza** (Lizenz) und erhalten den Lizenzcode.

Das Fenster **Licenza** (Lizenz):

- Ohne gültigen Code ist das Add-on **gesperrt**: In seinem Menü bleiben nur *Informazioni* (Informationen) und
  *Licenza* (Lizenz), und beim Start öffnet sich automatisch das Fenster **Licenza** mit dem Status und dem Grund.
- Das Fenster zeigt den **Firmencode** und den **Servercode**: Für den Kauf der Lizenz senden Sie diese mit *Copia*
  (Kopieren) an [license@xeisrl.com](mailto:license@xeisrl.com).
- Ein SAP-Benutzer mit **Superuser**-Rechten fügt den erhaltenen Code in *Inserisci un codice di licenza*
  (Lizenzcode eingeben) ein und klickt auf *Salva codice* (Code speichern): Das Add-on wird sofort freigeschaltet,
  ohne SAP neu zu starten.
- Der Testcode gilt in jeder Firma. Der Lizenzcode gilt für die Firma (Datenbank) oder den Server der gesendeten
  Codes.
- Dasselbe Fenster öffnen Sie jederzeit über das Menü *Licenza*: Status, Ablaufdatum, Nummer und Geltungsbereich der
  Lizenz.

## Menüs

Die Einträge befinden sich unter **XEI-Addon › Lohnfertigung**. Das Untermenü **Lohnfertigung** erscheint auch in dem
SAP-Modul, das in der Konfiguration gewählt ist (*Einkauf - Kreditoren* oder *Produktion*).

| Eintrag | Funktion |
|---|---|
| Lohnfertigungsauftrag | Öffnen, Suchen und Anlegen der Lohnfertigungsaufträge (Benutzerhandbuch, Kapitel 4 und 5) |
| Aufträge aus Produktionsaufträgen anlegen | Lohnfertigungsaufträge aus den externen Bearbeitungen der Produktionsaufträge (Kapitel 6) |
| Eingang vom Lohnfertiger | Eingang der Produkte eines Lieferscheins des Lohnfertigers auf mehrere Lohnfertigungsaufträge (Zugang der Produkte und Abgang der Komponenten) |
| Massenumlagerung Komponenten | Versand der Komponenten für mehrere Lohnfertigungsaufträge, wenn in der Konfiguration aktiviert (Kapitel 9) |
| Komponenten zwischen Aufträgen umlagern | verschiebt den Bestand, der sich bereits beim Lohnfertiger befindet, von einem Lohnfertigungsauftrag auf einen anderen (Kapitel 9) |
| Wareneingänge Produkte massenweise schließen | schließt die noch offenen Wareneingänge der Produkte (Kapitel 9) |
| Bearbeitungspreise Lohnfertiger | Preise der Bearbeitungen je Lohnfertiger und Produkt (Kapitel 9) |
| Konfiguration | Optionen des Add-ons (Kapitel 3) |
| Informazioni (Informationen), Traduzioni (Übersetzungen), Licenza (Lizenz) | gemeinsame Einträge der XEI-Add-ons; Licenza: Status und Lizenzcode |
