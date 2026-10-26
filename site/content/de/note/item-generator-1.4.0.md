---
title: XEI.ItemGenerator 1.4.0 – Versionshinweise
lang: de
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Versionshinweise

## Funktionen dieser Version

- **Vererbung der Varianten als Vorschlag.** Mit *Varianten erben* werden die auf einer vorherigen Ebene gewählten
  Optionen vorgeschlagen und können auf der erbenden Ebene geändert werden. Das Kontextmenü bietet **Zurück zu den
  vorgeschlagenen Optionen**.
- **Vererbung erzwingen.** Option für die Werte der Basen: Sie erzwingt die Auswahl der vorherigen Ebene, die beim
  Wert nicht geändert werden kann.
- **Benutzertabelle und Benutzerfeld bei Varianten.** In *Varianten und Optionen* werden eine Benutzertabelle und ein
  Artikel-Benutzerfeld angegeben: Beim Anlegen der Artikel werden die gewählten Optionen in die Tabelle aufgenommen
  und in das Feld übertragen.
- **Artikel generieren.** Der Variantenbereich zeigt die Varianten des im Baum gewählten Werts; ein Kontrollkästchen
  aktiviert die vollständige Ansicht nach Ebene.
- **Liste der zu erzeugenden Artikel.** Mit der Einstellung *Zur Liste hinzufügen leert zuerst die Liste der zu
  erzeugenden Artikel* (standardmäßig aktiv) enthält die Liste nur die letzte Auswahl; ist sie deaktiviert, sammeln
  sich die Artikel an.
- **Nummerierte Menüs.** Die Einträge des Code-Konfigurators sind in Arbeitsreihenfolge von 0 bis 7 nummeriert:
  Einstellungen, Basisdefinition, Varianten und Optionen, Variantenstrukturen, Artikel generieren, Konsistenzprüfung,
  Konfiguration prüfen, Excel-Import / -Export.
- **Unterebene mit Auswahlliste.** In der *Basisdefinition* wird die Spalte Unterebene über die Auswahlliste der Basen
  gefüllt, und der Pfeil öffnet die verknüpfte Basis. Ein von Hand eingegebener Code, der keine Basis ist, wird
  abgelehnt.
- **Konfigurationsprüfung und Excel** umfassen die Vererbung sowie die Benutzertabellen und -felder der Varianten.
- **Fenster** mit kompakten Kopfbereichen im Stil von SAP Business One.
- **Sprachen des Programms**: Italienisch, Englisch, Deutsch, Französisch und Spanisch.

## Installation

- Erfordert XEICore 1.1.1, im Paket enthalten.
- Beim ersten Start richtet das Add-on die Datenstruktur selbstständig ein.
