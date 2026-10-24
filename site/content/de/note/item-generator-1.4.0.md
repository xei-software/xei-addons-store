---
title: XEI.ItemGenerator 1.4.0 – Versionshinweise
lang: de
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Versionshinweise

## Neu

- **Vererbung der Varianten als Vorschlag.** Mit *Varianten erben* werden die auf einer
  vorherigen Ebene gewählten Optionen vorgeschlagen, können aber auf der erbenden Ebene
  geändert werden. Das Kontextmenü bietet **Zurück zu den vorgeschlagenen Optionen**.
- **Vererbung erzwingen.** Neue Option für die Werte der Basen: Sie erzwingt die Auswahl
  der vorherigen Ebene, die beim Wert nicht geändert werden kann.
- **Benutzertabelle und Benutzerfeld bei Varianten.** In *Varianten und Optionen* lassen
  sich eine Benutzertabelle und ein Artikel-Benutzerfeld angeben: Beim Anlegen der
  Artikel werden die gewählten Optionen in die Tabelle aufgenommen und in das Feld
  übertragen.
- **Übersichtlicheres Fenster Artikel generieren.** Der Variantenbereich zeigt nur die
  Varianten des im Baum gewählten Werts; ein Kontrollkästchen aktiviert die vollständige
  Ansicht nach Ebene.
- **Liste der zu erzeugenden Artikel.** Neue Einstellung *Zur Liste hinzufügen leert
  zuerst die Liste der zu erzeugenden Artikel* (standardmäßig aktiv): Die Liste enthält
  nur die letzte Auswahl. Ist sie deaktiviert, sammeln sich die Artikel an.
- **Nummerierte Menüs.** Die Einträge des Code-Konfigurators sind in Arbeitsreihenfolge
  von 0 bis 7 nummeriert: Einstellungen, Basisdefinition, Varianten und Optionen,
  Variantenstrukturen, Artikel generieren, Konsistenzprüfung, Konfiguration prüfen,
  Excel-Import / -Export.
- **Unterebene mit Auswahlliste.** In der *Basisdefinition* wird die Spalte Unterebene
  über die Auswahlliste der Basen gefüllt, und der Pfeil öffnet die verknüpfte Basis. Ein
  von Hand eingegebener Code wird abgelehnt, wenn die Basis nicht existiert.

## Verbesserungen

- Konfigurationsprüfung und Excel-Import / -Export um die neuen Felder ergänzt.
- Kompaktere Fensterköpfe, angepasst an den Stil von SAP Business One.
- Übersetzungen ins Englische, Deutsche, Französische und Spanische aktualisiert.

## Aktualisierung

- Erfordert XEICore 1.1.1, im Paket enthalten.
- Beim ersten Start aktualisiert das Add-on die Datenstruktur selbstständig (Version 3).
- Der bereits eingegebene Lizenzcode bleibt gültig.
