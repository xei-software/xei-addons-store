---
title: XEI.CommissionManagement – Installation, Lizenz, Menüs und Berechtigungen
description: So installieren Sie XEI.CommissionManagement, aktivieren die Lizenz, finden die Menüs und vergeben die Berechtigungen.
lang: de
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Installation, Lizenz, Menüs und Berechtigungen

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| System | Microsoft .NET Framework 4.8 auf dem PC des SAP-Clients |
| Programmsprachen | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |
| E-Mail | erreichbarer SMTP-Mailserver, nur für den E-Mail-Versand der Auszüge an die Vertreter (Konfiguration › E-Mail) |

## Installation

1. Laden Sie das Paket `XEI.CommissionManagement.zip` herunter.
2. Öffnen Sie in SAP Business One den **Extension Manager**, importieren Sie das Paket und ordnen Sie es der Firma zu.
3. Beim ersten Start legt das Add-on Felder, Tabellen, Indizes und Berechtigungen an. Das Anlegen der Felder in den
   Belegzeilen dauert **einige Minuten**: SAP zeigt mehrmals die Meldung, dass die Datenbankstruktur geändert wurde
   und alle geöffneten Fenster geschlossen werden: Antworten Sie mit **Ja**.

Jede Aktualisierung des Add-ons wird auf die gleiche Weise installiert.

Nach der Installation: zuerst die **Konfiguration** ausfüllen, dann die **Vertreter** (Rollen, Vorgesetzte,
Prozentsätze), dann die **Regeln**. Erst danach erhalten die Belege Prozentsätze. Benutzern ohne Superuser-Rechte sind
die **Berechtigungen** zu erteilen (siehe unten).

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

Die Einträge befinden sich unter **XEI-Addon › Provisionen**.

| Eintrag | Funktion |
|---|---|
| Konfiguration | Optionen (sechs Registerkarten) und Suchreihenfolge der Regeln (Benutzerhandbuch, Kapitel 5) |
| Vertreter | Rolle, Vorgesetzte, Standard-%, % bei Rechnung, Abrechnung, Lieferant, SAP-Benutzer (Kapitel 6) |
| Prozentregeln | % je Kunde, Kundengruppe, Artikel, Artikelgruppe, Preisliste (Kapitel 7) |
| Staffeln und Prämien | Prämien auf den Jahresumsatz, wenn in der Konfiguration aktiv (Kapitel 15) |
| Prüfung und Zuordnung % | Vergleich der Belege mit den Regeln und Korrektur in einem Schritt (Kapitel 9) |
| Provisionsberechnung | Berechnung für Rechnungen, Anzahlungsrechnungen und Gutschriften (Kapitel 10) |
| Berechnete Provisionen | Anzeige, Korrektur, Neuberechnung, Löschen (Kapitel 11) |
| Abrechnung | bezahlte Anteile abrechnen, unbezahlte stornieren (Kapitel 12) |
| Anpassungen | manuelle Beträge je Vertreter und Monat, Rechnungsentwürfe der Vertreter (Kapitel 13) |
| Provisionsauszug | berechnet, abzurechnen, abgerechnet und Anpassungen; CSV, Druck/PDF, E-Mail (Kapitel 14) |
| Prüfungen | zu prüfende Anomalien (Kapitel 16) |
| Informazioni (Informationen), Traduzioni (Übersetzungen), Licenza (Lizenz) | gemeinsame Einträge der XEI-Add-ons; Licenza: Status und Lizenzcode |

## Berechtigungen

In den **Allgemeinen Berechtigungen** von SAP (Administration › Systeminitialisierung › Berechtigungen) legt das
Add-on den Eintrag **Provvigioni** (Provisionen) unter *Benutzerberechtigungen* mit fünf Untereinträgen an. Superuser
haben immer alle Rechte; den anderen Benutzern wird für jeden Eintrag *Keine Berechtigung*, *Schreibgeschützt* oder
*Volle Berechtigung* zugewiesen.

![Allgemeine Berechtigungen](../../_img/commissionmanagement/autorizzazioni.png)

*Allgemeine Berechtigungen: der Eintrag Provvigioni mit den fünf Untereinträgen, für einen Benutzer ohne
Berechtigungen.*

| Berechtigung | Schreibgeschützt | Volle Berechtigung |
|---|---|---|
| Configurazione (Konfiguration) | – | die Konfiguration öffnen und speichern |
| Agenti, regole e scaglioni (Vertreter, Regeln und Staffeln) | anzeigen | Vertreter, Regeln und Staffeln speichern |
| Controllo, calcolo e verifiche (Kontrolle, Berechnung und Prüfungen) | Prüfung, Berechnung, Berechnete Provisionen, Prüfungen anzeigen | % übernehmen, berechnen, neu berechnen, Anteile speichern, löschen |
| Liquidazione, conguagli e bozze fatture (Abrechnung, Anpassungen und Rechnungsentwürfe) | Abrechnung und Anpassungen anzeigen | Abrechnungen bestätigen, Anpassungen speichern, Prämien buchen, Entwürfe erzeugen |
| Estratto di tutti gli agenti (Auszug aller Vertreter) | den Auszug aller Vertreter sehen (ohne: nur die eigenen) | auch der E-Mail-Versand |

Ohne Berechtigung antwortet der Menüeintrag in der Statusleiste mit *„Funktion nicht erlaubt: erfordert die
Berechtigung „…“ (Allgemeine Berechtigungen > Provvigioni)“*; mit Schreibschutz öffnet sich das Fenster, aber die
ändernden Schaltflächen antworten mit *„Vorgang nicht erlaubt: erfordert die volle Berechtigung für „…““*.

## Support

Für Lizenzen: [license@xeisrl.com](mailto:license@xeisrl.com). Für den Support:
[info@xeisrl.com](mailto:info@xeisrl.com). Geben Sie in der Anfrage die Version des Add-ons (Menü *Informazioni*)
und eine Beschreibung des Problems an.
