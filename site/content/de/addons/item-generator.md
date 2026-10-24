---
title: XEI.ItemGenerator – Konfigurator für Artikelnummern
description: Legen Sie in SAP Business One Artikel mit Nummer, Beschreibungen, Daten, Preis und Stückliste nach Ihren eigenen Regeln an.
lang: de
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator

**Konfigurator für Artikelnummern für SAP Business One.** Wählen Sie die Merkmale des
Produkts, und das Add-on legt den Artikel in den Artikelstammdaten an – mit Nummer,
Beschreibungen, Daten, Preis und Stückliste bereits ausgefüllt.

## Beschreibung

Wer Produkte in vielen Kombinationen verkauft (Maße, Ausführungen, Farben, Zubehör),
verliert Zeit damit, für jede Kombination von Hand einen Artikel anzulegen, und riskiert
unterschiedliche Nummern und Beschreibungen für dasselbe Produkt.

Mit XEI.ItemGenerator definieren Sie die Regeln einmal, und das Add-on stellt die
Artikel zusammen:

- die **Artikelnummer** entsteht aus den Werten, die Ebene für Ebene gewählt werden (zum
  Beispiel `PE` Hängeschrank → `MU` Wandmontage → `070` Höhe 70 cm = `PEMU070`), plus
  einer laufenden Nummer, die die Varianten unterscheidet;
- **Varianten** (zum Beispiel Farbe oder Ausführung) haben eigene Optionen, die von den
  vorherigen Ebenen geerbt werden können;
- **Beschreibungen, Gruppen, Mengeneinheiten, Eigenschaften, Maße, Gewicht und Preis**
  des Artikels ergeben sich aus den gewählten Werten und Optionen;
- die **Stückliste** wird aus den Komponenten jedes Werts und jeder Option gebildet.

Gibt es eine Kombination bereits, findet das Add-on den vorhandenen Artikel, statt ein
Duplikat anzulegen.

## Hauptfunktionen

- **Definition von Basen, Varianten und Strukturen** mit den Stammdaten des Add-ons in SAP.
- **Artikelgenerierung** in einem größenveränderbaren Fenster mit dem Baum der Nummern und
  dem Baum der Varianten; SAP bleibt benutzbar, während das Fenster geöffnet ist.
- **Artikel konfigurieren aus Angeboten und Kundenaufträgen**: Rechtsklick auf die
  Belegzeile, Artikel zusammenstellen und in die Zeile übernehmen.
- **Ähnliche Artikel generieren** aus den Stammdaten eines bereits generierten Artikels:
  Es genügt, eine Option zu ändern.
- **Beschreibungsformel** für Beschreibung, erweiterte Beschreibung und fremdsprachliche
  Bezeichnung.
- **Konfigurationsprüfung** mit Fehlerliste und direktem Öffnen der zu korrigierenden Daten.
- **Excel-Import und -Export** der Konfiguration, auch zum Kopieren in eine andere Firma.
- Eigene **Berechtigungen** in den Allgemeinen Berechtigungen von SAP.
- **Bildvorschau** des Artikels in den Artikelstammdaten.

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server (SAP HANA noch nicht unterstützt) |
| Sprachen des Programms | Italienisch, Englisch, Deutsch, Französisch, Spanisch |
| System | Microsoft .NET Framework 4.8 auf dem PC des SAP-Clients |
| Installation | Extension Manager von SAP Business One |
| Lizenz | XEI-Lizenzcode, einzugeben im Menü **Lizenz** des Add-ons (30 Tage kostenlos testen) |

## Aktuelle Version

**1.4.0** – siehe [Versionshinweise](../../manuali/de/itemgenerator/note-rilascio-1.4.0.md).
