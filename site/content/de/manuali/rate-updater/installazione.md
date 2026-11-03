---
title: XEI Rate Updater für SAP Business One – Installation, erster Start, Lizenz und geplante Aktualisierung
description: So installieren Sie XEI Rate Updater für SAP Business One, verbinden ihn mit SAP Business One, aktivieren die Lizenz und planen die tägliche Aktualisierung der Wechselkurse.
lang: de
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater für SAP Business One – Installation, erster Start, Lizenz und geplante Aktualisierung

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher, mit dem Service Layer |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| System | Windows 10 und 11, Windows Server 2016 und höher, 64 Bit; Microsoft Edge WebView2 Runtime |
| Netzwerk | Internetzugang zur gewählten Kursquelle |
| Sprachen des Programms | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |

## Installation

1. Laden Sie die ZIP-Datei des Programms von der Download-Seite herunter.
2. Entpacken Sie den Ordner aus der ZIP-Datei auf den PC, zum Beispiel nach `C:\XEI\RateUpdater`.
3. Starten Sie **XEI.RateUpdater.exe**. Das Programm enthält bereits .NET. Erforderlich ist **Microsoft Edge WebView2
   Runtime**, die meist bereits vorhanden ist: Fehlt sie, meldet das Programm dies und bietet den Download an.

Das Programm hat keine Installation. Einstellungen und Verlauf liegen im gemeinsamen Windows-Datenordner aller Benutzer
des PCs. Um das Programm zu aktualisieren, ersetzen Sie den Ordner durch den neuen: Einstellungen und Verlauf bleiben
erhalten.

## Erster Start

Beim ersten Öffnen erscheint die Seite **Erster Start**, mit dem bereits eingetragenen Code für den ersten Start.

1. **SAP-Verbindung**: *Adresse des Service Layers* und *SAP-Firmen*; danach **Verbindung testen**.
2. **Anmeldung und erster Administrator**:
   - *Anmeldung der Bediener*: **SAP-Benutzer jedes Einzelnen** oder **Eigene Benutzer und technischer SAP-Benutzer**;
   - *SAP-Benutzer des ersten Administrators* (zum Beispiel `manager`);
   - *Technischer SAP-Benutzer* und Passwort: Sie werden für die automatische Aktualisierung benötigt. Am besten ein
     eigener Benutzer, der nur die Berechtigung hat, Wechselkurse zu schreiben.
3. **Speichern und neu starten**.

Danach finden Sie dieselben Einstellungen unter **Einstellungen › SAP**. Die Kursquelle und die automatische
Aktualisierung finden Sie unter **Einstellungen › Wechselkurse**.

## Lizenz

Das Programm arbeitet mit einem **Lizenzcode**, den XEI ausstellt.

| Geltungsbereich | Gilt für |
|---|---|
| Pro Firma | eine SAP-Datenbank |
| Pro Server | alle Firmen der SQL-Server- oder SAP-HANA-Instanz |
| Frei | ist an keine Datenbank gebunden |

- **Test**: 30 Tage, frei.
- Menü **Lizenz**: Status, Ablauf und Geltungsbereich. Den von XEI erhaltenen Code fügen Sie in **Lizenzcode eingeben**
  ein; er gilt sofort, ohne Neustart.
- Für eine Lizenz pro Firma oder für den ganzen Server muss das Programm mit Nur-Lese-Zugriff mit der Lizenzdatenbank
  verbunden sein (*Einstellungen › Lizenz*, **Verbindung testen**): Dort und auf der Seite Lizenz erscheinen der
  Firmencode und der Servercode, die Sie an [license@xeisrl.com](mailto:license@xeisrl.com) senden.

## Geplante Aktualisierung mit Windows

So werden die Wechselkurse jeden Tag aktualisiert, auch wenn das Programm geschlossen ist.

1. Richten Sie den **technischen SAP-Benutzer** ein (Einstellungen › SAP).
2. Öffnen Sie in Windows die **Aufgabenplanung** und erstellen Sie eine einfache Aufgabe, zum Beispiel täglich um 7:00.
3. Aktion **Programm starten**: `XEI.RateUpdater.exe` im Programmordner, mit dem Argument `aggiorna`.
4. Wählen Sie in den Eigenschaften der Aufgabe **Unabhängig von der Benutzeranmeldung ausführen**.

Der Befehl aktualisiert die heutigen Wechselkurse und beendet sich ohne Fenster; der Durchlauf erscheint im **Verlauf**.
Bei mehreren Firmen fügen Sie `--societa <database SAP>` hinzu, eine Aufgabe pro Firma. Ergebnis für die
Aufgabenplanung: **0** erfolgreich, **1** fehlgeschlagen oder mit einer abgelehnten Währung, **2** falsche Argumente.

Alternativ genügt es, bei geöffnetem Programm die **Automatische Aktualisierung** unter *Einstellungen › Wechselkurse*
einzuschalten.

## Support

Für Lizenzen: [license@xeisrl.com](mailto:license@xeisrl.com). Für den Support:
[info@xeisrl.com](mailto:info@xeisrl.com). Geben Sie in Ihrer Anfrage die Programmversion (Menü *Info*) und eine
Beschreibung des Problems an.
