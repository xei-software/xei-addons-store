---
title: XEI Rate Updater für SAP Business One 1.0.0 – Versionshinweise
lang: de
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater für SAP Business One 1.0.0 – Versionshinweise

## Funktionen dieser Version

- **Wechselkurse in SAP Business One** mit den Kursen der Europäischen Zentralbank, der Banca d'Italia oder von Open
  Exchange Rates: für die Wechselkurse eines Tages gelten die am Vortag veröffentlichten Kurse.
- **Nur die Währungen der Firma**, in der Notierung der Firma (direkter oder indirekter Kurs), abgeschnitten auf sechs
  Dezimalstellen.
- **Andere Hauswährung als der Euro**: Kreuzkurse zur Hauswährung.
- **Aktualisierung von Hand** auf der Seite Wechselkurse, mit dem Ergebnis jeder Währung.
- **Automatische Aktualisierung** jeden Tag zur gewählten Uhrzeit oder über die Windows-Aufgabenplanung mit dem Befehl
  `XEI.RateUpdater.exe aggiorna`.
- **Verlauf** der Durchläufe jeder Firma, mit den Kursen und dem Ergebnis jeder Währung.
- **XEI-Lizenz** frei, für den ganzen Server oder pro Firma; kostenloser Test für 30 Tage.
- **Sprachen des Programms**: Italienisch, Englisch, Deutsch, Französisch, Spanisch und Türkisch.

## Installation

- Programm für Windows 10 und 11 und Windows Server 2016 und höher, 64 Bit: Ordner aus der ZIP-Datei entpacken und
  `XEI.RateUpdater.exe` starten; .NET ist bereits enthalten.
- Erforderlich sind Microsoft Edge WebView2 Runtime, die meist bereits vorhanden ist, und der Service Layer von
  SAP Business One 10.0 oder höher.
