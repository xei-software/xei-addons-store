---
title: XEI Rate Updater für SAP Business One – Wechselkurse
description: Aktualisiert jeden Tag die Wechselkurse in SAP Business One mit den amtlichen Kursen der EZB, der Banca d'Italia oder von Open Exchange Rates.
lang: de
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater für SAP Business One

**Die Wechselkurse in SAP Business One, automatisch aktuell.** Jeden Tag holt das Programm die Kurse aus einer
amtlichen Quelle und schreibt sie in SAP Business One, in der Notierung und mit den Dezimalstellen, die SAP verwendet.

## Beschreibung

Wechselkurse von Hand zu pflegen heißt, jeden Morgen die Kurse von einer Website in die Wechselkurstabelle von SAP zu
übertragen, Währung für Währung, mit dem Risiko, einen Tag zu vergessen oder einen Kurs zu vertauschen.

XEI Rate Updater für SAP Business One übernimmt das für Sie:

- er holt die Kurse von der **Europäischen Zentralbank**, der **Banca d'Italia** oder von **Open Exchange Rates**;
- für die Wechselkurse eines Tages verwendet er die **am Vortag** veröffentlichten Kurse; an Wochenenden und Feiertagen
  den letzten Veröffentlichungstag;
- er schreibt in SAP nur die **von der Firma geführten Währungen**, in der Notierung der Firma (direkter oder indirekter
  Kurs), abgeschnitten auf sechs Dezimalstellen;
- bei einer **anderen Hauswährung als dem Euro** berechnet er die Kreuzkurse zu dieser Währung;
- er wird **von Hand** mit einem gewählten Datum verwendet oder **jeden Tag automatisch**;
- er führt einen **Verlauf** jeder Aktualisierung: wer sie ausgeführt hat, die Quelle, die Kurse und das Ergebnis jeder
  Währung.

## Hauptfunktionen

- **Wechselkurse**: Datum der Wechselkurse, Quelle und Schaltfläche *Wechselkurse in SAP aktualisieren*; das Ergebnis
  zeigt für jede Währung den direkten Kurs, den indirekten Kurs und ob sie in SAP geschrieben wurde.
- **Verlauf**: die Durchläufe der Firma, der neueste zuerst; jede Zeile lässt sich mit den Währungen aufklappen.
- **Automatische Aktualisierung**: jeden Tag zur gewählten Uhrzeit oder über die Windows-Aufgabenplanung.
- **Fehler im Griff**: ein Fehler bei einer Währung hält die anderen nicht auf; jeder Durchlauf zeigt, was schiefging.
- **Anmeldung mit dem SAP-Benutzer** jedes Einzelnen, mit seinen Berechtigungen für die Wechselkurse; der Administrator
  weist jedem Benutzer die Funktionen *Wechselkurse aktualisieren* und *Verlauf* zu.

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher, mit dem Service Layer |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| System | Windows 10 und 11, Windows Server 2016 und höher, 64 Bit; Microsoft Edge WebView2 Runtime |
| Netzwerk | Internetzugang zur gewählten Kursquelle (EZB, Banca d'Italia oder Open Exchange Rates mit eigenem API-Schlüssel) |
| Sprachen des Programms | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |
| Installation | Programmordner entpacken, ohne Installation; .NET ist bereits enthalten |
| Lizenz | XEI-Lizenzcode, frei, für den ganzen Server oder pro Firma (kostenloser Test für 30 Tage) |

## Aktuelle Version

**1.0.0** – siehe die [Versionshinweise](../../manuali/de/rateupdater/note-rilascio-1.0.0.md) und das
[Benutzerhandbuch](../../manuali/de/rateupdater/manuale-utente.md).
