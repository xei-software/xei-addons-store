---
title: XEI.ContoLavoro 1.2.0 – Versionshinweise
description: Funktionen und Korrekturen von XEI.ContoLavoro 1.2.0 für SAP Business One.
lang: de
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro 1.2.0 – Versionshinweise

## Funktionen dieser Version

- In der Liste „Aufträge aus Produktionsaufträgen anlegen“ erscheinen mit dem Kontrollkästchen „Auch nicht bereite Zeilen anzeigen“ auch die Bearbeitungen, die nicht zu einem Lohnfertigungsauftrag
  werden können, mit dem Grund und dem, was zu tun ist, in der Spalte „Grund / Hinweise“.
- Beim Speichern einer Stückliste meldet ein Hinweis die Codes, die im Feld „Lavorazione terzista“ (Bearbeitung
  Lohnfertiger) zu korrigieren sind: Ressourcen, Codes, die keine Artikel sind, Artikel ohne „Conto lavoro“
  (Lohnfertigung), Bearbeitungen, die keine Zeilen der Stückliste sind, Komponenten mit retrograder Entnahme.
- XEI-Lizenz mit dem Fenster **Licenza** (Lizenz) im Menü des Add-ons: Status, Firmen- und Servercode, Eingabe des
  Codes; 30 Tage kostenlos testen.

## Korrekturen dieser Version

- Ein unterbrochener Lohnfertigungsauftrag verhindert nicht, aus derselben Zeile des Produktionsauftrags einen anderen
  Lohnfertigungsauftrag anzulegen.
- Komponenten mit retrograder Entnahme, die mit einer externen Bearbeitung verknüpft sind, werden nicht an den
  Lohnfertiger gesendet, und der Produktionsauftrag entnimmt sie nur einmal.
- Ohne Nummernserie des Lohnfertigungsauftrags zeigt das Add-on beim Öffnen von *Lohnfertigungsauftrag*, wo sie definiert wird.
- Die Massenumlagerung der Komponenten ist in der Standardkonfiguration aktiv; bei ausgeschalteter Option weist der Menüeintrag darauf hin, dass die Funktion deaktiviert ist.
- Die aus Produktionsaufträgen angelegten Lohnfertigungsaufträge verwenden die Standardpreisliste der Aufträge (Konfiguration › Allgemein): ohne sie fordert „Aufträge anlegen“ dazu auf, sie anzugeben.
- In der Liste „Aufträge aus Produktionsaufträgen anlegen“ lassen sich die Zeilen markieren und der Lieferant ändern.
