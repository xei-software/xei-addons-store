---
title: XEI.CommissionManagement – Vertreterprovisionen
description: Berechnet und rechnet in SAP Business One die Provisionen von Vertretern, Gebietsleitern, Bereichsleitern und Direktoren ab, von den Regeln bis zur Abrechnung je Vertreter.
lang: de
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement

**Provisionen der Vertriebsmitarbeiter in SAP Business One.** Die Prozentsätze kommen automatisch auf die
Belegzeilen, das Add-on berechnet die Provisionen, rechnet sie ab, sobald die Kunden zahlen, und erstellt die
Abrechnung für jeden Vertreter.

## Beschreibung

Provisionen von Hand oder in Tabellenkalkulationen zu berechnen heißt, jeden Monat Rechnungen, Zahlungseingänge und
Vereinbarungen mit den Vertretern erneut durchzugehen, mit dem Risiko von Fehlern und Abrechnungen, die vom ERP
abweichen.

Mit XEI.CommissionManagement bleibt alles in SAP Business One:

- jede Rechnungszeile trägt bis zu **vier Prozentsätze**: Vertreter, Gebietsleiter, Bereichsleiter und Direktor;
- die Prozentsätze kommen aus den **Regeln** nach Kunde, Kundengruppe, Artikel, Artikelgruppe, Preisliste, Zeitraum
  und Rabatt oder aus den Standardprozentsätzen des Vertreters und lassen sich von Hand korrigieren;
- die Provision teilt sich in einen Anteil **bei Rechnungsstellung** und Anteile **bei Zahlungseingang**, Rate für
  Rate oder auf die Belegsumme;
- die **Abrechnung** schlägt die bezahlten Anteile vor und storniert die Anteile wieder offener Raten;
- die **Abrechnung je Vertreter** lässt sich als CSV exportieren, als PDF drucken oder per E-Mail senden.

## Hauptfunktionen

- **Vertreter und Hierarchie**: Rolle, Gebietsleiter, Bereichsleiter, Direktor, Standardprozentsätze, Anteil bei
  Rechnungsstellung und Abrechnungsart für jeden Vertriebsmitarbeiter.
- **Prozentregeln** mit einstellbarer Suchreihenfolge, Mindestrabatt und Gültigkeitszeitraum, als CSV exportierbar
  und importierbar.
- **Prozentsätze auf den Verkaufsbelegen** bei der Erfassung, mit geschätzter Provision beim Speichern und Schutz der
  von Hand korrigierten Zeilen.
- **Prüfung und Zuordnung der %**: vergleicht die Prozentsätze der Belege mit den Regeln und korrigiert sie gesammelt.
- **Berechnung** auf Ausgangsrechnungen, Anzahlungsrechnungen und Gutschriften, auch automatisch beim Hinzufügen der
  Rechnung.
- **Abrechnung** der bezahlten Anteile, auch anteilig zu Teilzahlungen, mit abgeschlossenem Zeitraum.
- **Anpassungen**, **Staffeln und Prämien** auf den Jahresumsatz und **Rechnungsentwürfe** der Vertreter.
- **Prüfungen** auf Auffälligkeiten und eigene **Berechtigungen** in den Allgemeinen Berechtigungen von SAP.

## Voraussetzungen

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| Sprachen des Programms | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |
| System | Microsoft .NET Framework 4.8 auf dem PC des SAP-Clients |
| E-Mail | erreichbarer SMTP-Mailserver, nur für den E-Mail-Versand der Abrechnungen an die Vertreter (Konfiguration › E-Mail) |
| Installation | Extension Manager von SAP Business One |
| Lizenz | XEI-Lizenzcode, einzugeben im Menü **Licenza** (Lizenz) des Add-ons (30 Tage kostenlos testen) |

## Aktuelle Version

**1.1.1** – siehe [Versionshinweise](../../manuali/de/commissionmanagement/note-rilascio-1.1.1.md) und
[Benutzerhandbuch](../../manuali/de/commissionmanagement/manuale-utente.md).
