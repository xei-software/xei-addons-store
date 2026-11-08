---
title: XEI.ContoLavoro – Lohnfertigung
description: Verwaltet in SAP Business One die an Lohnfertiger vergebenen Bearbeitungen, vom Auftrag und dem Versand der Komponenten bis zur Rücklieferung des Fertigprodukts.
lang: de
prodotto: XEI.ContoLavoro
versione: 1.2.1
stato: approvato
---

# XEI.ContoLavoro

**Lohnfertigung in SAP Business One.** Ein Lohnfertigungsauftrag für jede Bearbeitung hält die Bestellung beim
Lohnfertiger, die versendeten Komponenten, die Rücklieferungen und den Eingang des Fertigprodukts zusammen, mit einem
stets aktuellen Stand.

## Beschreibung

Lohnfertigung von Hand zu verfolgen heißt, Bestellungen, Umlagerungen und Wareneingänge abgestimmt zu halten und
jederzeit zu wissen, was sich bei jedem Lohnfertiger befindet. Mit XEI.ContoLavoro übernimmt das SAP Business One:

- für jede Bearbeitung wird ein **Lohnfertigungsauftrag** mit den herzustellenden Produkten und ihrer Stückliste
  angelegt: zu versendende Komponenten und zu bezahlende Bearbeitungen;
- die **Bestellung beim Lohnfertiger** entsteht aus dem Lohnfertigungsauftrag und bleibt bei jeder Änderung
  abgestimmt;
- die **Komponenten** werden an das Lager des Lohnfertigers gesendet, mit Rücklieferungen und Ausschuss;
- der **Eingang** bucht in einem einzigen Vorgang den Zugang des Produkts und der Bearbeitungen und den Abgang der
  verbrauchten Komponenten;
- der Lohnfertigungsauftrag zeigt jederzeit, was versendet, was verbraucht wurde, was beim Lohnfertiger verbleibt und
  was fehlt, und schließt sich von selbst, wenn er erledigt ist.

## Hauptfunktionen

- **Lohnfertigungsauftrag** mit den Registerkarten Produkte, Stückliste, Komponenten und Belege: alle verknüpften
  SAP-Belege, gruppiert und direkt zu öffnen.
- **Lohnfertigung aus Produktionsaufträgen**: Die externen Arbeitsgänge eines Produktionsauftrags werden zu
  Lohnfertigungsaufträgen, die Komponenten werden bei jeder Rücklieferung entnommen und das Fertigprodukt geht ins
  Lager, wenn alle Bearbeitungen zurückgekommen sind.
- **Chargen und Seriennummern**, vorgeschlagen aus den Chargen des Lohnfertigungsauftrags beim Lohnfertiger und nach
  Verfallsdatum, von Hand änderbar; Charge des eingehenden Produkts, berechnet von einem konfigurierbaren Skript.
- **Kosten** der Produkte, bei jedem Speichern neu berechnet, mit den **Bearbeitungspreisen** je Lohnfertiger und
  Produkt.
- **Massenumlagerung** der Komponenten, **Umlagerung zwischen Lohnfertigungsaufträgen** beim selben Lohnfertiger und
  **massenweises Schließen** der Wareneingänge.

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| Programmsprachen | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |
| System | Microsoft .NET Framework 4.8 auf dem PC des SAP-Clients |
| Installation | Extension Manager von SAP Business One |
| Lizenz | XEI-Lizenzcode, einzugeben im Menü **Licenza** (Lizenz) (30 Tage kostenlos testen) |

## Aktuelle Version

**1.2.1** – siehe [Versionshinweise](../../manuali/de/contolavoro/note-rilascio-1.2.1.md) und Benutzerhandbuch.
