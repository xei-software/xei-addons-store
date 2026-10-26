---
title: XEI.ItemGenerator – Installation, Lizenz, Menüs und Berechtigungen
description: So installieren Sie XEI.ItemGenerator, aktivieren die Lizenz, finden die Menüs und vergeben die Berechtigungen.
lang: de
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Installation, Lizenz, Menüs und Berechtigungen

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| System | Microsoft .NET Framework 4.8 auf dem PC des SAP-Clients |
| Programmsprachen | Italienisch, Englisch, Deutsch, Französisch, Spanisch |

## Installation

1. Laden Sie das Paket `XEI.ItemGenerator.zip` herunter.
2. Öffnen Sie in SAP Business One den **Extension Manager**, importieren Sie das Paket und ordnen Sie es
   der Firma zu.
3. Beim ersten Start legt das Add-on Tabellen, Felder, Objekte und die Berechtigungseinträge selbst an.
4. Starten Sie danach **den SAP-Client einmal neu**: Die Fenster der Basen und der Varianten lesen die
   Felder des Add-ons beim Start von SAP.

Jede Aktualisierung des Add-ons wird auf die gleiche Weise installiert, mit demselben Neustart.

## Lizenz

Das Add-on arbeitet mit einem **Lizenzcode**, den XEI ausstellt. Nach der Anforderung des Tests erhalten Sie per
E-Mail einen Testcode, der 30 Tage gültig ist.

- Ohne gültigen Code ist das Add-on **gesperrt**: In seinem Menü bleiben nur *Informationen* und
  *Lizenz*, und beim Start öffnet sich automatisch das Fenster **Lizenz** mit dem Status und dem Grund.
- Das Fenster zeigt den **Firmencode** und den **Servercode**: Mit *Kopieren* senden Sie diese an
  [license@xeisrl.com](mailto:license@xeisrl.com), um den Lizenzcode zu erhalten.
- Ein SAP-Benutzer mit **Superuser**-Rechten fügt den erhaltenen Code in *Lizenzcode eingeben* ein und
  klickt auf *Code speichern*: Das Add-on wird sofort freigeschaltet, ohne SAP neu zu starten.
- Der Code gilt für die Firma (Datenbank), in die er eingefügt wird: Für jede Firma ist ein eigener Code
  erforderlich.
- Dasselbe Fenster öffnen Sie jederzeit über das Menü *Lizenz*: Status, Ablaufdatum, Nummer und
  Geltungsbereich der Lizenz.

![Das Fenster Lizenz bei gesperrtem Add-on](../../_img/itemgenerator/27_licenza.png)

*Das Fenster Lizenz bei gesperrtem Add-on: Grund, Firmen- und Servercode, Feld für den Code.*

## Menüs

Die Einträge befinden sich unter **Module › Administration › Add-Ons › XEI-Addon › Code-Konfigurator**
und, identisch, unter **Lagerverwaltung › Artikelverwaltung › Code-Konfigurator**.

| Eintrag | Funktion |
|---|---|
| 0. Einstellungen | Optionen des Add-ons (Benutzerhandbuch, Kapitel 3) |
| 1. Basisdefinition | Basen und Werte: der Baum des Codes (Kapitel 5) |
| 2. Varianten und Optionen | Varianten mit ihren Optionen (Kapitel 4) |
| 3. Variantenstrukturen | Gruppen von Varianten, die für einen Wert abgefragt werden (Kapitel 4) |
| 4. Artikel generieren | Zusammenstellung und Anlage der Artikel (Kapitel 9) |
| 5. Konsistenzprüfung | Neuberechnung der Zusammensetzungen der generierten Artikel (Kapitel 14) |
| 6. Konfiguration prüfen | Prüfung der gesamten Konfiguration (Kapitel 12) |
| 7. Excel-Import / -Export | Konfiguration in einer Excel-Datei (Kapitel 13) |
| Informationen, Übersetzungen, Lizenz | gemeinsame Einträge der XEI-Add-ons (nur unter XEI-Addon); Lizenz: Status und Lizenzcode |

Über das Kontextmenü (Rechtsklick) stehen außerdem **Artikel konfigurieren...** in den Zeilen von
Angeboten und Kundenaufträgen (Kapitel 10) und **Ähnliche Artikel generieren...** in den
Artikelstammdaten eines generierten Artikels (Kapitel 11) zur Verfügung.

## Berechtigungen

Unter **Administration › Systeminitialisierung › Berechtigungen › Allgemeine Berechtigungen** fügt das
Add-on den Zweig **Configuratore codici XEI** hinzu. Für jeden Eintrag können Sie *Vollständige
Berechtigung*, *Schreibgeschützt* oder *Keine Berechtigung* vergeben. Superuser haben immer vollen
Zugriff.

![Der Zweig des Konfigurators in den allgemeinen Berechtigungen](../../_img/itemgenerator/23_autorizzazioni.png)

*Der Zweig des Konfigurators in den allgemeinen Berechtigungen, für einen Benutzer ohne Berechtigungen.*

| Eintrag | Vollständig | Schreibgeschützt |
|---|---|---|
| Definizione basi | Basen ändern | anzeigen |
| Definizione varianti | Varianten ändern | anzeigen |
| Strutture varianti | Strukturen ändern | anzeigen |
| Generazione articoli | Artikel anlegen (auch aus Angeboten und Aufträgen) | Liste zusammenstellen, ohne anzulegen |
| Configurazione, verifica, import/export | Einstellungen speichern, aus Excel importieren, Konsistenzprüfung | Einstellungen ansehen, prüfen, exportieren |

Ohne Berechtigung zeigt der Menüeintrag in der Statusleiste „Funktion nicht berechtigt“.

## Support

Für Lizenzen: [license@xeisrl.com](mailto:license@xeisrl.com). Für den Support:
[info@xeisrl.com](mailto:info@xeisrl.com). Geben Sie in der Anfrage die Version des Add-ons (Menü
*Informationen*) und eine Beschreibung des Problems an.
