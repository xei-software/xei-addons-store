---
title: XEI.CommissionManagement – Benutzerhandbuch
description: "Provisionen der Vertreter in SAP Business One: Konfiguration, Regeln, Berechnung, Abrechnung, Anpassungen und Auszüge."
lang: de
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement – Benutzerhandbuch

| | |
|---|---|
| SAP Business One | 10.0 oder höher |
| Datenbank | Microsoft SQL Server oder SAP HANA (unter SAP HANA empfiehlt sich ein Test bei der Installation) |
| Sprachen des Programms | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |

## 1. Was das Add-on leistet

XEI.CommissionManagement berechnet die **Provisionen der Vertreter** aus den Belegen von SAP Business One und
rechnet sie ab. Jede Rechnungszeile (auch von Anzahlungsrechnungen und Gutschriften) trägt bis zu vier
Prozentsätze: einen für den **Vertreter** des Belegs und je einen für seine Vorgesetzten, **Gebietsleiter**,
**Bereichsleiter** und **Direktor**. Das Add-on:

- **ordnet die Prozentsätze** den Zeilen schon bei der Erfassung der Belege zu, nach Regeln je Kunde,
  Kundengruppe, Artikel, Artikelgruppe, Preisliste, Zeitraum und Rabatt (oder nach den Standardprozentsätzen des
  Vertreters);
- **berechnet** die Provisionen der Belege eines Zeitraums und teilt sie in **Anteile**: Ein Teil wird mit der
  Rechnung fällig, der Rest mit der Zahlung (Rate für Rate oder wenn der ganze Beleg bezahlt ist);
- **rechnet** die Anteile ab, sobald SAP die Zahlungen bucht, und **storniert** die Anteile von Raten, die
  unbezahlt zurückkommen;
- erstellt für jeden Vertreter den **Auszug** mit den berechneten Provisionen, den noch abzurechnenden Beträgen und
  dem, was ihm im Zeitraum zusteht (abgerechnet plus manuelle **Anpassungen**), als CSV für Excel exportierbar, als
  PDF druckbar und per E-Mail an jeden Vertreter versendbar;
- auf Wunsch (Optionen in der Konfiguration): schätzt die Provision beim Sichern eines Belegs, berechnet gerade
  gebuchte Rechnungen selbstständig, schützt manuell korrigierte Prozentsätze, rechnet Teilzahlungen ab, schließt
  bereits übergebene Perioden, berechnet **Prämien** auf den Jahresumsatz, bereitet die **Rechnungsentwürfe** der
  Vertreter vor und meldet Anomalien (**Prüfungen**).

Alles liegt in SAP: Benutzerfelder bei den Vertriebsmitarbeitern und in den Belegzeilen, Benutzertabellen für
Regeln, Provisionen und Anpassungen, keine externe Datenbank. Es arbeitet unter Microsoft SQL Server und SAP HANA gleich; unter SAP HANA empfiehlt sich ein Test bei der Installation.

## 2. Die Begriffe: Begünstigte, Prozentsätze, Anteile, Abrechnung

### Wer die Provision erhält (Begünstigte)

Der **Vertriebsmitarbeiter** des Belegs ist der Vertreter. Im Fenster Vertreter können ihm ein
**Gebietsleiter**, ein **Bereichsleiter** und ein **Direktor** zugeordnet werden: Sie sind die weiteren
Begünstigten seiner Belege. Jeder hat in jeder Zeile seinen eigenen Prozentsatz (die vier Spalten *Provv. % agente
/ capo zona / capo area / direttore*, Provision % Vertreter / Gebietsleiter / Bereichsleiter / Direktor).

- Ein Vertriebsmitarbeiter erhält nur dann Provisionen, wenn er eine **Rolle** hat (Vertreter, Gebietsleiter,
  Bereichsleiter, Direktor). Ein Mitarbeiter ohne Rolle ist „nicht verwaltet“: Seine Belege erzeugen keine
  Provisionen, und wenn er als Vorgesetzter eines anderen angegeben ist, wird sein Anteil nicht berechnet.
- Die Rolle „Vertreter“ gilt für die Mitarbeiter, die in den Belegen als Vertriebsmitarbeiter stehen;
  „Gebietsleiter“, „Bereichsleiter“ und „Direktor“ sind die Funktionen, mit denen ein Mitarbeiter als Vorgesetzter
  gewählt werden kann. Wer eine Vorgesetztenrolle hat, kann trotzdem eigene Belege haben: Bei diesen ist er der
  Vertreter.

### Die Prozentsätze

Die Prozentsätze einer Zeile stammen aus den **Regeln** (Kapitel 7) oder, wenn keine Regel greift, aus den
**Standardprozentsätzen** des Vertreters des Belegs (Kapitel 6). Sie werden bei der Erfassung des Belegs
automatisch zugeordnet (Kapitel 8), können manuell korrigiert und vor der Berechnung in einem Schritt geprüft und
bereinigt werden (Kapitel 9).

### Die Anteile: bei Rechnung und bei Zahlung

Die Provision eines Belegs ist nicht sofort vollständig fällig. Für jeden Begünstigten teilt das Add-on sie in
Anteile:

- der Anteil **bei Rechnung** (Rate 0) entspricht dem Wert „% bei Rechnung“ des Mitarbeiters und wird zum
  Buchungsdatum des Belegs fällig;
- der Rest wird **bei Zahlung** fällig: bei Abrechnung **nach Raten** ein Anteil je Rate des Belegs, im
  Verhältnis zur Rate, abrechenbar, sobald diese Rate bezahlt ist; bei Abrechnung **auf den Gesamtbetrag** ein
  einziger Anteil (Rate -1), abrechenbar, sobald alle Raten bezahlt sind.

Beispiel: Rechnung über 1.350 netto mit 5 % Provision = 63,00; Vertreter mit 30 % bei Rechnung und Abrechnung nach
Raten, Beleg mit zwei Raten zu je 50 %: Anteil 0 = 18,90 bei der Buchung, Rate 1 = 22,05 und Rate 2 = 22,05 zu den
jeweiligen Fälligkeiten.

### Die Abrechnung

Einen Anteil abrechnen heißt, ihn dem Vertreter mit einem Abrechnungsdatum gutzuschreiben. Das Add-on schlägt die
abzurechnenden Anteile anhand der Zahlungen in SAP vor (Zahlungen, Wechsel, Abstimmungen, Gutschriften) und schlägt
den **Storno** bereits abgerechneter Anteile vor, deren Raten wieder offen sind (unbezahlte Posten). Ein
**festgeschriebener** Anteil ist endgültig: Er wird nicht storniert, und die Provision wird nicht erneut berechnet.

## 3. Installation und erster Start

- Paket für den Extension Manager: `XEI.CommissionManagement.zip`, von der Download-Seite der XEI-Website. In SAP
  Business One öffnet man den **Extension Manager**, importiert das Paket und ordnet es der Firma zu.
- Beim ersten Start legt das Add-on Felder, Tabellen, Indizes und Berechtigungen an. Das Anlegen der Felder in den Belegzeilen dauert **einige
  Minuten**: SAP zeigt mehrmals die Meldung, dass die Datenbankstruktur geändert wurde und alle geöffneten Fenster
  geschlossen werden — mit **Ja** antworten.
- Das Menü befindet sich unter **XEI-Addon › Provisionen**:

    Provisionen
      Konfiguration                     Optionen (sechs Registerkarten) und Suchreihenfolge der Regeln
      Vertreter                         Rolle, Vorgesetzte, Standard-%, % bei Rechnung, Abrechnung, Lieferant, SAP-Benutzer
      Prozentregeln                     % je Kunde / Gruppe / Artikel / Artikelgruppe / Preisliste
      Staffeln und Prämien              Prämien auf den Jahresumsatz (wenn in der Konfiguration aktiv)
      Prüfung und Zuordnung %           Vergleich Belege / Regeln und Korrektur in einem Schritt
      Provisionsberechnung              Berechnung für Rechnungen, Anzahlungen und Gutschriften
      Berechnete Provisionen            Anzeige, Korrektur, Neuberechnung, Löschen
      Abrechnung                        bezahlte Anteile abrechnen, unbezahlte stornieren
      Anpassungen                       manuelle Beträge je Vertreter und Monat, Rechnungsentwürfe der Vertreter
      Provisionsauszug                  berechnet, abzurechnen, abgerechnet + Anpassungen; CSV, Druck/PDF, E-Mail
      Prüfungen                         zu prüfende Anomalien
      Informazioni, Traduzioni, Licenza (Informationen, Übersetzungen, Lizenz: gemeinsame Einträge der XEI-Add-ons)

> Nach der Installation: zuerst die **Konfiguration** ausfüllen, dann die **Vertreter** (Rollen, Vorgesetzte,
> Prozentsätze), dann die **Regeln**. Erst danach erhalten die Belege Prozentsätze. Benutzern ohne
> Superuser-Rechte sind die **Berechtigungen** zu erteilen (Kapitel 17).

### Lizenz

Das Add-on arbeitet mit einem **Lizenzcode**, den XEI ausstellt.

- **Test**: Nach der Anforderung des Tests auf der Website erhält man per E-Mail einen **Testcode**, der ab dem
  Versand 30 Tage in jeder Firma gilt.
- **Kauf**: Man sendet XEI die beiden Codes aus dem Fenster **Licenza** (Lizenz) (Firmencode und Servercode, mit
  *Copia* (Kopieren)) und erhält den Lizenzcode, der für die Firma oder den Server dieser Codes gilt.
- Ohne gültigen Code ist das Add-on **gesperrt**: In seinem Menü bleiben nur *Informazioni* (Informationen) und
  *Licenza* (Lizenz), und beim Start öffnet sich automatisch das Fenster **Licenza** mit dem Status und dem Grund.
- Ein SAP-Benutzer mit **Superuser**-Rechten fügt den Code in *Inserisci un codice di licenza* (Lizenzcode
  eingeben) ein und drückt *Salva codice* (Code speichern): Das Add-on wird sofort entsperrt, ohne SAP neu zu
  starten.

### Sprachen

Das Add-on verwendet die Sprache des SAP-Clients (in SAP: Benutzer - Einstellungen \> Anzeige \> Sprache):
Italienisch, Englisch, Deutsch, Französisch, Spanisch oder Türkisch; bei anderen Sprachen bleibt es auf Italienisch.
Beim Sprachwechsel schließt SAP die geöffneten Fenster, und das Add-on startet von selbst neu. Einzelne Texte lassen
sich unter **Provisionen \> Traduzioni** (Übersetzungen) anpassen. In allen Sprachen auf Italienisch bleiben die
Texte, die SAP nur einmal in der Datenbank speichert: die Namen der Berechtigungen (Allgemeine Berechtigungen \>
Provvigioni) und die Titel der Felder, die zu Belegen und Vertriebsmitarbeitern hinzugefügt werden (z. B. „Provv. %
manuali“ (Provision % manuell), „% agente“ (% Vertreter)); die Meldungen nennen sie mit diesen Namen, damit man sie
in SAP wiederfindet.

## 4. Die monatliche Arbeit im Überblick

1.  **Während des Monats** erhalten die Belege ihre Prozentsätze automatisch; wer sie erfasst, kann sie korrigieren.
2.  **Prüfung und Zuordnung %** für die Rechnungen des Monats: Man sieht die Zeilen, deren Prozentsätze nicht den
    Regeln entsprechen, und korrigiert sie in einem Schritt (optional, aber empfohlen).
3.  **Provisionsberechnung** des Monats: Rechnungen, Anzahlungsrechnungen, Gutschriften.
4.  **Berechnete Provisionen**: Stichprobenkontrolle, Korrektur einzelner Provisionen.
5.  **Abrechnung** mit Stichtag Monatsende: Bestätigung der bezahlten Anteile und eventueller Stornos.
6.  **Anpassungen** des Monats (Prämien, Rückforderungen, manuelle Korrekturen) und, falls aktiv, die
    **Rechnungsentwürfe** der Vertreter.
7.  **Provisionsauszug** „Abgerechnete Provisionen und Anpassungen“ des Monats: Das ist der Betrag, der jedem
    Vertreter zusteht; CSV für Excel, Druck/PDF oder E-Mail an jeden Vertreter.
8.  Wenn die Auszüge übergeben sind, **geschlossene Periode** bis Monatsende (wenn die Option verwendet wird).

Die **Prüfungen** (Kapitel 16) lassen sich jederzeit starten, vor der Berechnung oder vor den Auszügen, um nicht
berechnete Belege, geänderte Vertreter, Zeilen ohne Prozentsätze und nicht abgerechnete Zahlungen zu finden. Am
Jahresende bucht **Staffeln und Prämien** (Kapitel 15) die Umsatzprämien als Anpassungen für Dezember.

## 5. Konfiguration

Die Konfiguration hat sechs Registerkarten. Die Registerkarte **Allgemein** enthält die Grundoptionen und die
Reihenfolge der Regeln; die übrigen (**Belege**, **Abrechnung**, **Vertreter**, **E-Mail**, **Hinweise**) enthalten
die Zusatzfunktionen, die anfangs alle **ausgeschaltet** sind: Unter jeder steht eine Erklärung mit einem Beispiel,
und sie wird bei Bedarf mit dem Haken aktiviert. Erforderlich ist die Berechtigung „Configurazione“ (Konfiguration)
(Kapitel 17).

![Configurazione, scheda Generale](../../_img/commissionmanagement/cfg.png)

*Provisionskonfiguration, Registerkarte Allgemein*

### Registerkarte Allgemein

Prozentsätze den Zeilen der Verkaufsbelege schon bei der Erfassung zuordnen  
Aktiviert die automatische Zuordnung (Kapitel 8). Ist sie deaktiviert, werden die Prozentsätze manuell oder mit der
Prüfung eingetragen.

Zeilenrabatt für die Regeln  
Der Rabatt, mit dem die Regeln ihren „Mindestrabatt“ vergleichen: der *Zeilenrabatt %* oder ein prozentuales
Benutzerfeld der Zeilen (zum Beispiel ein von einem anderen Add-on berechneter „effektiver“ Rabatt).

Nettopreise: ohne Zeilenrabatt ist der Rabatt die Differenz zum Preis der Kundenpreisliste  
Für den Verkauf zu Nettopreisen ohne Rabattangabe: Hat die Zeile keinen Rabatt, berechnet das Add-on den
**effektiven Rabatt** als Differenz zwischen dem Preislistenpreis des Kunden und dem Preis der Zeile (Preisliste
100, Preis 80 = Rabatt 20 %), schreibt ihn in die Spalte *Provv. sconto effettivo* (Provision effektiver Rabatt) und
verwendet ihn für die Regeln.

Prozentsätze auch für Zeilen „Nur Steuer“  
Normalerweise haben Zeilen „Nur Steuer“ keine Provision (Prozentsätze null).

Provisionen auf Anzahlungsrechnungen (später von der Schlussrechnung abgezogen)  
Mit aktiver Option werden Anzahlungsrechnungen berechnet, und ihre Provision wird von der Schlussrechnung, die sie
abschließt, **abgezogen**; so entspricht die Gesamtprovision der des vollen Betrags.

Standardmäßig Abrechnung bei Zahlung des ganzen Belegs (sonst Rate für Rate)  
Gilt für Mitarbeiter mit Abrechnung „Laut Konfiguration“: ja = ein einziger Anteil, wenn der ganze Beleg bezahlt
ist; nein = ein Anteil je Rate.

Gutschriften zur Fälligkeit abrechnen (auch die der Basisbelege), nicht bei der Buchung  
Normalerweise wird die (negative) Provision einer Gutschrift zum Buchungsdatum abgerechnet. Mit der Option zur
spätesten Fälligkeit der Gutschrift und der Rechnungen, auf die sie sich bezieht.

Suchreihenfolge der Regeln  
Die 16 möglichen Feldkombinationen einer Regel, in der Reihenfolge, in der sie geprüft werden. Geändert wird die
Zahl in der Spalte *Reihenfolge*: Reihenfolge 1 wird zuerst geprüft. Siehe Kapitel 7.

### Registerkarte Belege

![Configurazione, scheda Documenti](../../_img/commissionmanagement/cfg_documenti.png)

*Registerkarte Belege: Schätzung, manuelle Zeilen, automatische Berechnung*

Geschätzte Provision beim Sichern eines Verkaufsbelegs anzeigen  
Nach dem Hinzufügen oder Aktualisieren eines Auftrags, Angebots, einer Lieferung oder Rechnung zeigt die
Statusleiste, was jedem Begünstigten mit den aktuellen Prozentsätzen der Zeilen zustehen wird. Beispiel:
*„Geschätzte Provisionen (Kundenauftrag 1250): Rossi 63,00; Bianchi 9,00 - gesamt 72,00“*. Dies ist nur eine
Information: Es wird nichts gespeichert (Kapitel 8).

Manuell geänderte Prozentsätze in den Belegzeilen schützen  
Wer einen Prozentsatz in der Zeile korrigiert, macht die Zeile „manuell“ (Spalte *Provv. % manuali*, Provision %
manuell): Bei einem Wechsel von Kunde oder Vertreter wird diese Zeile nicht neu zugeordnet. Beispiel: Rossi setzt
die Zeile laut Absprache mit dem Kunden von 5 % auf 4 %; dann wechselt er den Kunden: Die anderen Zeilen werden neu
zugeordnet, diese bleibt bei 4 %. Ohne die Option überschreibt die Neuzuordnung alle Zeilen. Wird der Haken bei
„manuell“ entfernt, ist die Zeile wieder automatisch.

Provisionen berechnen, sobald eine Rechnung, Anzahlungsrechnung oder Gutschrift hinzugefügt wird  
Die Berechnung erfolgt beim Sichern im SAP-Client (mit der letzten Wahl zum Belegrabatt in der
Provisionsberechnung): So muss die Provisionsberechnung nicht jeden Monat geöffnet werden. Beispiel: Nach dem
Buchen der Rechnung 1001 von Rossi meldet die Statusleiste *„Provisionen berechnet (Rechnung 1001): Rossi 63,00;
Bianchi 9,00“*. Belege aus Importen oder anderen Programmen (DI API) laufen nicht über den Client: Für sie bleiben
die Provisionsberechnung und die Prüfungen.

### Registerkarte Abrechnung

![Configurazione, scheda Liquidazione](../../_img/commissionmanagement/cfg_liquidazione.png)

*Registerkarte Abrechnung: Teilzahlungen und geschlossene Periode*

Teilzahlungen: Provisionsanteil im Verhältnis zum auf die Rate gezahlten Betrag abrechnen  
Ohne die Option wird ein Anteil erst abgerechnet, wenn die Rate vollständig beglichen ist: Bei Teilzahlungen oder
Nachlässen bleibt die Provision stehen. Beispiel: Rate über 500 mit Anteil 22,05; der Kunde zahlt 250 → 11,03 werden
abgerechnet; bei der Restzahlung die übrigen 11,02. Wird eine Zahlung storniert, wird nur der Überschuss storniert
(Kapitel 12).

Geschlossene Periode: Provisionen sperren bis (Datum)  
Bis einschließlich zu diesem Datum können Provisionen weder neu berechnet noch gelöscht, Anteile weder geändert
noch abgerechnet und Anpassungen nicht gespeichert werden. Beispiel: Nach der Übergabe der März-Auszüge setzt man
31/03: Die März-Rechnungen werden von da an nicht neu berechnet (eine nie berechnete Rechnung lässt sich weiterhin
berechnen). Um etwas in der geschlossenen Periode zu korrigieren: das Datum zurücksetzen (oder den Haken entfernen),
korrigieren, wieder einstellen.

### Registerkarte Vertreter

Aus den Anpassungen Entwürfe von Eingangsrechnungen für Vertreter mit verknüpftem Lieferanten erzeugen  
In Anpassungen erstellt die Schaltfläche **Rechnungsentwürfe** für jeden Vertreter einen Entwurf einer
Eingangsrechnung (Eingangsgutschrift, wenn der Betrag negativ ist) mit einer Servicezeile: Betrag = im Monat
abgerechnete Anteile + Anpassungen und Prämien des Monats. Beispiel: Rossi (Lieferant F0010), April: 22,05 + 50,00 -
20,00 = 52,05. Das **Konto der Zeile** ist Pflicht (das Aufwandskonto der Provisionen, z. B. 7xxxx
Provisionsaufwand); das **Steuerkennzeichen** ist das der Rechnungen des Vertreters (leer = Standard des
Lieferanten). Kapitel 13.

Jahresumsatz-Staffeln mit Prämie (Menü Staffeln und Prämien)  
Aktiviert das Menü **Staffeln und Prämien**: Erreicht der Jahresnettoumsatz die Schwelle, erhält der Vertreter eine
Prämie (% vom Jahresumsatz oder Festbetrag), die als Anpassung gebucht wird. Beispiel: Staffeln 100.000 → 0,5 % und
200.000 → 1 %; Rossi fakturiert 2026 150.000: Prämie 750,00 in der Anpassung für Dezember. Kapitel 15.

Einbehalt (Richtwert) im Auszug der Abrechnungen: % und Beschreibung  
Nur informativ (ohne Mindest- und Höchstbeträge): Im Druck und in der E-Mail des Auszugs „Abgerechnete
Provisionen und Anpassungen“ erscheinen eine Zeile „Einbehalt“ und der Nettobetrag als Richtwert. Beispiel: 8,5 und
„Enasarco quota agente“: abgerechnet 1.000,00 → Einbehalt (Richtwert) -85,00, Netto (Richtwert) 915,00. Leer oder 0
= keine Zeile.

![Configurazione, scheda Agenti](../../_img/commissionmanagement/cfg_agenti.png)

*Registerkarte Vertreter: Rechnungsentwürfe, Staffeln und Einbehalt als Richtwert (8,5 % Enasarco)*

### Registerkarte E-Mail

![Configurazione, scheda Email](../../_img/commissionmanagement/cfg_email.png)

*Registerkarte E-Mail: Versand des Auszugs an die Vertreter*

Auszug per E-Mail an die Vertreter senden  
Aktiviert die Schaltfläche **An Vertreter senden** im Provisionsauszug: Jeder Vertreter erhält nur seinen eigenen
Auszug (HTML-Anhang, in jedem Browser zu öffnen und zu drucken) an die E-Mail-Adresse des Vertriebsmitarbeiters
(oder des verknüpften Lieferanten). Anzugeben sind SMTP-Server, Port, SSL/TLS, Benutzer und Kennwort des Postfachs
sowie der Absender; Beispiel: `smtp.azienda.it`, Port 587, SSL ja, Absender `provvigioni@azienda.it`. Das
Kennwort wird verschlüsselt gespeichert.

Testversand  
Sendet eine Testnachricht an die angegebene Adresse mit den in der Registerkarte eingetragenen Werten (auch wenn
sie noch nicht gespeichert sind): Wenn etwas nicht stimmt, erscheint sofort die Fehlermeldung des Servers.

### Registerkarte Hinweise

![Configurazione, scheda Avvisi](../../_img/commissionmanagement/cfg_avvisi.png)

*Registerkarte Hinweise*

Bezahlter, nicht abgerechneter Anteil: Anomalie nach (Tagen)  
In den Prüfungen meldet die Suche „Nicht abgerechnete Zahlungen“ die Anteile, deren Rate seit mehr als so vielen
Tagen bezahlt ist und die niemand abgerechnet hat. Beispiel: 30; Rate am 05/04 bezahlt, heute 10/05: Der Anteil
steht bei den Anomalien, bis er abgerechnet ist.

Beim Start des Add-ons die Anomalien der Schnellprüfung in der Statusleiste melden  
Schnelle Kontrollen bei jedem Start: zu berechnende Belege der letzten 90 Tage, stornierte Belege mit Provisionen,
nach der Berechnung geänderter Vertreter. Beispiel: *„Provisionen: 3 Anomalien zu prüfen (Provisionen \>
Prüfungen)“*. Kapitel 16.

> Beim Speichern prüft die Konfiguration, ob die aktiven Optionen vollständig sind: Datum der geschlossenen Periode,
> vorhandenes und bebuchbares Konto für die Entwürfe, Einbehalt zwischen 0 und 99,99, Server, Port und Absender für
> die E-Mail.

## 6. Vertreter

![Agenti](../../_img/commissionmanagement/agenti.png)

*Vertreter: alle Vertriebsmitarbeiter von SAP, im Raster änderbar*

Das Raster zeigt alle Vertriebsmitarbeiter von SAP. Man füllt die Spalten aus und drückt **Speichern**: Gespeichert
werden nur die geänderten Mitarbeiter (dieselben Felder sind auch im Standardformular der Vertriebsmitarbeiter,
Registerkarte Benutzerfelder, zu sehen).

| Spalte                                                       | Bedeutung                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rolle                                                        | Vertreter, Gebietsleiter, Bereichsleiter, Direktor oder *(nicht verwaltet)*: keine Provision.                                                                                                                                                                                                                                                                                                              |
| Gebietsleiter, Bereichsleiter, Direktor                      | Die Vorgesetzten dieses Mitarbeiters: Sie erhalten ihren Prozentsatz auf seine Belege. Die Auswahllisten zeigen die Mitarbeiter mit dieser Rolle: zuerst die Rollen zuordnen und speichern, dann die Vorgesetzten. Ein bereits zugeordneter Vorgesetzter mit einer anderen oder keiner Rolle erscheint als *„Name (andere Rolle)“*: Er erhält keine Provisionen, bis er die Rolle bekommt (das melden auch die Prüfungen). |
| % Vertreter, % Gebietsleiter, % Bereichsleiter, % Direktor   | **Standardprozentsätze** der Belege dieses Mitarbeiters, verwendet, wenn keine Regel für die Zeile greift.                                                                                                                                                                                                                                                                                                 |
| % bei Rechnung                                               | Teil der Provision **dieses Mitarbeiters** (als Begünstigter), der mit der Buchung des Belegs fällig wird; der Rest wird bei Zahlung fällig. 100 = alles bei Rechnung, 0 = alles bei Zahlung.                                                                                                                                                                                                              |
| Abrechnung                                                   | Für den Teil bei Zahlung: *Nach Raten*, *Auf Gesamtbetrag* oder *Laut Konfiguration* (folgt der Option der Konfiguration).                                                                                                                                                                                                                                                                                 |
| Lieferant                                                    | Der Lieferant (Geschäftspartner), mit dem der Vertreter die Provisionen in Rechnung stellt: Empfänger der **Rechnungsentwürfe** (Kapitel 13); seine E-Mail-Adresse wird für den Versand des Auszugs verwendet, wenn der Mitarbeiter keine hat.                                                                                                                                                             |
| SAP-Benutzer                                                 | Der SAP-Benutzer, der diesem Mitarbeiter entspricht. Ein Benutzer ohne die Berechtigung „Estratto di tutti gli agenti“ (Auszug aller Vertreter) sieht im Provisionsauszug nur sich selbst und die Mitarbeiter, deren Gebietsleiter, Bereichsleiter oder Direktor er ist (Kapitel 17).                                                                                                                     |
| E-Mail (Vertriebsmitarbeiter)                                | Die E-Mail-Adresse des Vertriebsmitarbeiters (SAP-Stammdaten, schreibgeschützt): Empfänger des Auszugs per E-Mail.                                                                                                                                                                                                                                                                                        |

Prüfungen beim Speichern: Prozentsätze zwischen 0 und 100, vorhandener Lieferant und SAP-Benutzer, ein Mitarbeiter
kann nicht sein eigener Vorgesetzter sein. In diesem Handbuch verwendetes Beispiel:

| Mitarbeiter | Rolle             | Gebietsleiter | Bereichsleiter | % Vertr. | % Geb.l. | % Ber.l. | % bei Rechn. | Abrechnung          |
|-------------|-------------------|---------------|----------------|----------|----------|----------|--------------|---------------------|
| Rossi       | Vertreter         | Bianchi       | Neri           | 2        | 0,5      | 0,2      | 30           | Nach Raten          |
| Bianchi     | Gebietsleiter     |               |                | 3        |          |          | 0            | Laut Konfiguration  |
| Neri        | (nicht verwaltet) |               |                |          |          |          |              |                     |
| Verdi       | Vertreter         |               |                | 1,5      |          |          | 100          | Laut Konfiguration  |

Auf den Belegen von Rossi sind die Begünstigten Rossi (Vertreter) und Bianchi (Gebietsleiter); Neri erhält, obwohl
als Bereichsleiter angegeben, nichts, solange er keine Rolle hat.

## 7. Prozentregeln

![Regole percentuali](../../_img/commissionmanagement/regole.png)

*Prozentregeln des Beispiels*

Eine Regel besagt: „Für Zeilen mit *diesen Merkmalen* gelten diese Prozentsätze“. Mögliche Merkmale sind Kunde,
Kundengruppe, Artikel, Artikelgruppe und Preisliste (die Preisliste des Kunden); man füllt **nur die benötigten
Felder** aus, und das Add-on erkennt die **Kombination** selbst (Spalte Kombination). Zulässig sind 16
Kombinationen:

| Typ  | Kombination                             | Typ  | Kombination                                 |
|------|-----------------------------------------|------|---------------------------------------------|
| 1    | Kunde / Artikel / Preisliste            | 9    | Kundengruppe / Artikelgruppe / Preisliste   |
| 2    | Kunde / Artikel                         | 10   | Kundengruppe / Artikelgruppe                |
| 3    | Kunde / Artikelgruppe / Preisliste      | 11   | Kundengruppe / Preisliste                   |
| 4    | Kunde / Artikelgruppe                   | 12   | Kundengruppe                                |
| 5    | Kunde / Preisliste                      | 13   | Artikel / Preisliste                        |
| 6    | Kunde                                   | 14   | Artikel                                     |
| 7    | Kundengruppe / Artikel / Preisliste     | 15   | Artikelgruppe / Preisliste                  |
| 8    | Kundengruppe / Artikel                  | 16   | Artikelgruppe                               |

Kunde und Kundengruppe zusammen (oder Artikel und Artikelgruppe zusammen) sind nicht zulässig: Die Regel wird nicht
gespeichert.

Die übrigen Felder der Regel:

- **Vertreter**: Die Regel gilt nur für die Belege dieses Mitarbeiters; *(alle)* = für alle;
- **Von / Bis**: Gültigkeitszeitraum, verglichen mit dem Belegdatum; auch nur eines der beiden Daten;
- **Mindestrabatt**: Die Regel gilt, wenn der Zeilenrabatt mindestens so hoch ist (0 = immer). So erhalten stärker
  rabattierte Verkäufe niedrigere Prozentsätze;
- **Aktiv**: Eine deaktivierte Regel bleibt gespeichert, wird aber nicht angewendet.

### Wie die Regel einer Zeile gewählt wird

1.  Die Kombinationen werden in der **Reihenfolge der Konfiguration** geprüft (Standard 1 → 16, von der
    spezifischsten zur allgemeinsten).
2.  Für jede Kombination werden zuerst die Regeln des **Vertreters des Belegs** gesucht (wenn er mindestens eine
    hat), dann die Regeln für alle. Die erste Kombination, die eine gültige Regel findet, gewinnt: Eine
    spezifischere Regel „für alle“ (z. B. Kunde / Artikelgruppe) gewinnt gegen eine allgemeinere Regel des
    Vertreters (z. B. Artikelgruppe).
3.  Unter mehreren Regeln derselben Kombination gewinnt die mit dem jüngsten Anfangsdatum, dann die mit der nächsten
    Fälligkeit, dann die mit dem höchsten erreichten Mindestrabatt.
4.  Greift keine Regel, gelten die Standardprozentsätze des Vertreters.

Beispiel mit den Regeln der Abbildung (R1 Kunde C001 + Artikelgruppe GA100 → 6/1; R2 nur Rossi, Gruppe GA100 → 7/1;
R3 Artikel A1 → 4/0,5; R4 Artikel A1 mit Mindestrabatt 10 → 3/0,5; R5 Kundengruppe A, Jahr 2026 → 5/1):

| Zeile                                                | Prozentsätze Vertreter / Gebietsleiter | Warum                                                           |
|------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------|
| Rossi, Kunde C001, Artikel A9 (Gruppe GA100)         | 6 / 1                                  | R1: Kunde / Artikelgruppe kommt vor der Regel von Rossi         |
| Rossi, Kunde C002, Artikel A9                        | 7 / 1                                  | R2: Regel des Vertreters                                        |
| Verdi, Kunde C002, Artikel A9                        | 1,5 / 0                                | keine Regel: Standardprozentsätze von Verdi                     |
| Verdi, Kunde C002, Artikel A1, Rabatt 12             | 3 / 0,5                                | R4: Mindestrabatt 10 erreicht (gewinnt gegen R3)                |
| Verdi, Kunde C002, Artikel A1, Rabatt 5              | 4 / 0,5                                | R3                                                              |
| Verdi, Kunde C003 (Gruppe A), Artikel A1             | 5 / 1                                  | R5: Kundengruppe kommt vor Artikel                              |
| wie oben, aber 2027                                  | 4 / 0,5                                | R5 abgelaufen, es bleibt R3                                     |

### Das Formular

- **Filter** (Vertreter, Kunde, Artikel, Nur aktive) und **Suchen**.
- **Zeile hinzufügen**, **Zeilen kopieren** und **Zeilen löschen** für die markierten Zeilen (Klick auf den
  Zeilenkopf links); die Änderungen werden mit **Speichern** endgültig. Alle Felder werden im Raster geändert (die
  Pfeile öffnen Kunde und Artikel).
- **CSV-Export** speichert die angezeigten Regeln in einer Datei mit Trennzeichen „;“ (lässt sich in Excel öffnen);
  **CSV-Import** fügt die Zeilen einer Datei mit denselben Spalten hinzu (Agente, Cliente, GruppoClienti, Articolo,
  GruppoArticoli, Listino, Dal, Al, ScontoMinimo, PercAgente, PercCapoZona, PercCapoArea, PercDirettore, Attiva):
  Die importierten Zeilen sind zu prüfen und zu speichern.
- Beim Schließen oder Suchen mit ungespeicherten Änderungen fragt das Add-on nach einer Bestätigung.

## 8. Die Prozentsätze in den Verkaufsbelegen

![Ordine cliente](../../_img/commissionmanagement/ordine.png)

*Kundenauftrag: die Provv.-Spalten mit den zugeordneten Prozentsätzen und, bei Nettopreisen, dem effektiven Rabatt*

Bei aktiver Zuordnung, in Angeboten, Aufträgen, Lieferungen, Retouren, Rechnungen, Gutschriften und
Anzahlungsrechnungen:

- wenn der **Artikel**, der **Rabatt** oder der **Preis** einer Zeile eingegeben oder geändert wird, schreibt das
  Add-on die vier Prozentsätze der Zeile (und bei Nettopreisen den effektiven Rabatt);
- bei der Auswahl mehrerer Artikel aus der Liste werden auch die hinzugefügten Zeilen ergänzt;
- wird bei einem Beleg in Erfassung der **Kunde** oder der **Vertriebsmitarbeiter** geändert, werden alle Zeilen
  neu zugeordnet. Achtung: Beim Wechsel des Kunden setzt SAP den Standard-Vertriebsmitarbeiter dieses Kunden ein;
  ist dieser „kein“, bleiben die Zeilen unverändert, bis der Vertreter gewählt wird.

Die Prozentsätze bleiben **manuell änderbar** und werden mit dem Beleg gespeichert; überschrieben werden sie nur,
wenn Artikel, Preis oder Rabatt dieser Zeile erneut geändert werden. Kopierte Belege (Auftrag → Lieferung →
Rechnung) übernehmen die Prozentsätze der Zeilen.

> Die Spalten *Provv. % agente*, *% capo zona*, *% capo area*, *% direttore* (Provision % Vertreter,
> Gebietsleiter, Bereichsleiter, Direktor) und *Provv. sconto effettivo* (Provision effektiver Rabatt) macht das
> Add-on beim Öffnen des Belegs sichtbar und änderbar; um sie immer an der gewünschten Position zu haben, kann man
> sie einmal in den Formulareinstellungen anordnen (Symbol oben rechts im Raster). In Belegen ohne
> Vertriebsmitarbeiter oder mit einem Mitarbeiter ohne Rolle wird nichts geschrieben.

Der Haken „Nur Steuer“ einer Zeile löst im Client kein Ereignis aus: Die Prozentsätze passen sich bei der nächsten
Änderung von Artikel, Preis oder Rabatt der Zeile an (oder bei einem Wechsel des Vertreters).

### Manuelle Zeilen (Option „Manuell geänderte Prozentsätze schützen“)

![Ordine con riga manuale](../../_img/commissionmanagement/ordine_manuale.png)

*Auftrag: Die Zeile mit dem manuell korrigierten Prozentsatz ist in „Provv. % manuali“ markiert und wird danach
nicht neu zugeordnet*

Mit aktiver Option zeigt das Add-on auch die Spalte *Provv. % manuali* (Provision % manuell). Sobald einer der vier
Prozentsätze einer Zeile manuell eingegeben wird, wird die Zeile **als manuell markiert** und von da an nicht neu
zugeordnet: weder bei Änderung von Artikel, Preis oder Rabatt der Zeile noch bei einem Wechsel von Kunde oder
Vertreter des Belegs noch bei der Auswahl weiterer Artikel aus der Liste. Die anderen Zeilen folgen weiter den
Regeln. Um zur automatischen Zuordnung zurückzukehren, genügt es, den Haken zu entfernen: Bei der nächsten Änderung
erhält die Zeile wieder die Prozentsätze der Regeln. Die Markierung geht auf kopierte Belege über und ist in der
Prüfung sichtbar (Spalte *Manuelle %*), wo manuelle Zeilen nicht zur Korrektur vorgeschlagen werden.

### Schätzung und automatische Berechnung beim Buchen

![Stima in barra di stato](../../_img/commissionmanagement/stima.png)

*Nach dem Hinzufügen des Auftrags zeigt die Statusleiste die geschätzte Provision je Begünstigtem*

Zwei Optionen der Registerkarte Belege wirken, wenn der Beleg im SAP-Client **gesichert** wird:

- **Schätzung**: Bei Angeboten, Aufträgen, Lieferungen, Retouren, Rechnungen, Gutschriften und
  Anzahlungsrechnungen zeigt die Statusleiste, was mit den aktuellen Prozentsätzen der Zeilen fällig würde,
  Begünstigter für Begünstigter, zum Beispiel *„Geschätzte Provisionen (Kundenauftrag 1250): PRV Rossi 6,00; PRV
  Bianchi 1,00 - gesamt 7,00“*. Der Belegrabatt wird je nach der letzten Wahl in der Provisionsberechnung
  berücksichtigt oder nicht. Es wird nichts gespeichert.
- **Automatische Berechnung**: Rechnungen, Gutschriften und (falls aktiv) Anzahlungsrechnungen, die im Client
  **hinzugefügt** werden, werden sofort berechnet, als wäre die Provisionsberechnung nur für diesen Beleg gestartet
  worden; die Statusleiste meldet *„Provisionen berechnet (Rechnung 1001): ...“*. In Berechnete Provisionen ist
  die Herkunft „Automatisch beim Buchen“. Ist die Berechnung nicht möglich (Anzahlung bereits abgezogen,
  geschlossene Periode, Vertreter nicht verwaltet), erscheint ein Hinweis, und der Beleg bleibt normal gebucht: Er
  wird dann über die Provisionsberechnung berechnet, und die Prüfungen melden ihn unter „Zu berechnen“.

> Belege, die aus Importen, über den Service Layer oder die DI API erstellt werden, laufen nicht über den SAP-Client:
> Für sie gilt immer die Provisionsberechnung (oder die Berechnung des ganzen Zeitraums, die nur noch nicht
> berechnete Belege erfasst).

## 9. Prüfung und Zuordnung %

![Controllo e assegnazione percentuali](../../_img/commissionmanagement/controllo.png)

*Prüfung: Prozentsätze des Belegs („Bel.“) und von den Regeln vorgeschlagene, abweichende Zeilen hervorgehoben*

Vor der Berechnung empfiehlt es sich zu prüfen, ob die Prozentsätze in den Belegen des Zeitraums den Regeln
entsprechen (wer die Rechnung erfasst hat, könnte sie geändert haben, oder die Regeln wurden inzwischen angepasst).

1.  Vertreter (oder alle), Zeitraum und Belegarten wählen: **noch nicht berechnete** Rechnungen,
    Anzahlungsrechnungen, Gutschriften und auf Wunsch offene Kundenaufträge. **Prüfen** drücken.
2.  Für jede Zeile zeigt das Raster die aktuellen Prozentsätze (*Bel.*), die Prozentsätze, die die Regeln heute
    ergeben würden (*Vorschl.*), und die *Herkunft Vorschlag* (Regel für alle, Regel des Vertreters,
    Standardprozentsätze). Abweichende Zeilen sind hervorgehoben und bereits markiert; mit „Nur vom Vorschlag
    abweichende Zeilen“ sieht man nur diese.
3.  Den Haken bei den Zeilen entfernen, die unverändert bleiben sollen (gewollte Korrekturen), und **Vorgeschlagene
    % übernehmen** drücken.

Was mit den markierten Zeilen geschieht:

- **offene Kundenaufträge**: Der Auftrag wird aktualisiert; die geänderten Prozentsätze gehen auf die Belege über,
  die daraus kopiert werden;
- **Rechnungen, Anzahlungsrechnungen und Gutschriften**: Das sind gebuchte Belege, und SAP erlaubt keine Änderung
  (auch nicht der Benutzerfelder der Zeilen). Die korrigierten Prozentsätze speichert das Add-on in einer eigenen
  Tabelle, und die Berechnung verwendet sie anstelle der Werte des Belegs; der SAP-Beleg bleibt unverändert. Die
  Spalte *Bereits korrigiert* zeigt dies an, und die Spalte *Bel.* zeigt von da an die korrigierten Prozentsätze.

![Controllo con righe manuali](../../_img/commissionmanagement/controllo_manuale.png)

*Prüfung der offenen Aufträge: Manuelle Zeilen, die vom Vorschlag abweichen, werden nicht markiert („mit manuellen
%: 3“)*

Ein Doppelklick auf eine Zeile öffnet den Beleg. Belege mit bereits berechneten Provisionen erscheinen nicht: Zu
ihrer Korrektur dient Berechnete Provisionen (Kapitel 11). Die Spalte *Manuelle %* zeigt die Zeilen, deren
Prozentsätze im Beleg manuell korrigiert wurden: Mit der Option „Manuell geänderte Prozentsätze schützen“ werden sie
nicht markiert (man kann sie gezielt markieren). Bei aktiver geschlossener Periode werden gebuchte Belege mit Datum
in der Periode nicht korrigiert.

## 10. Provisionsberechnung

![Calcolo provvigioni](../../_img/commissionmanagement/calcolo.png)

*Provisionsberechnung mit dem Ergebnis je Beleg*

Den Zeitraum (Belegdatum), die Belegarten (Rechnungen, Anzahlungsrechnungen, wenn in der Konfiguration aktiv,
Gutschriften) wählen und festlegen, ob der **Belegrabatt bei der Berechnung berücksichtigt** wird (der Rabatt auf
den ganzen Beleg verringert den Nettobetrag jeder Zeile). **Berechnen** verarbeitet alle Belege des Zeitraums, die
**nicht storniert** sind, einen verwalteten Vertreter haben und **noch nicht berechnet** sind: zuerst die
Anzahlungsrechnungen, dann Rechnungen und Gutschriften. Das Raster zeigt für jeden Beleg, wie viele Begünstigte eine
Provision haben, die Summe und das Ergebnis; ein Doppelklick öffnet den Beleg.

Mit **Nur der Beleg** (Typ und Nummer) wird ein bestimmter Beleg berechnet oder **neu berechnet**, zum Beispiel
nach einer Korrektur der Prozentsätze; die Neuberechnung ist nur möglich, wenn keiner seiner Anteile abgerechnet
oder festgeschrieben ist.

### Wie gerechnet wird, Schritt für Schritt

Für jeden Begünstigten (Vertreter und Vorgesetzte mit Rolle):

1.  **Nettobetrag der Zeile** = Zeilensumme in Hauswährung, auf Wunsch um den Belegrabatt verringert; negativ bei
    Gutschriften. Zeilen mit Betrag null (Gratisartikel) zählen nicht.
2.  **Provision der Zeile** = Nettobetrag × Prozentsatz der Zeile für diese Rolle. Zeilen mit Prozentsatz 0 zählen
    nicht.
3.  **Summe** = Summe der Zeilenprovisionen. Bei Rechnungen, die eine Anzahlung abschließen, wird die bereits auf
    die Anzahlung berechnete Provision abgezogen (im Verhältnis zum abgezogenen Betrag).
4.  **Anteile**: der Anteil bei Rechnung (Rate 0) zum Buchungsdatum; der Rest nach Raten (Rate n zur Fälligkeit
    der Rate n, im Verhältnis zu ihrem Prozentsatz, die letzte Rate nimmt die Rundungsdifferenzen auf) oder auf den
    Gesamtbetrag (Rate -1 zur Fälligkeit der letzten Rate). Gutschriften haben einen einzigen negativen Anteil
    (Rate 0 zur Buchung oder, mit der Option, zur Fälligkeit).

Die Beträge werden auf 2 Dezimalstellen gerundet; die Summe der Provision ist immer die Summe der Anteile.

### Beispiel: Rechnung 1001

Rossi (30 % bei Rechnung, nach Raten), Kunde C001, **Belegrabatt 10 %**, zwei Raten zu je 50 % (31/03 und 30/04):

| Zeile          | Zeilensumme | Nettobetrag (−10 %) | % Vertreter | Prov. Vertreter | % Gebietsleiter | Prov. Gebietsleiter |
|----------------|-------------|---------------------|-------------|-----------------|-----------------|---------------------|
| A1             | 1.000,00    | 900,00              | 5           | 45,00           | 1               | 9,00                |
| A2             | 500,00      | 450,00              | 4           | 18,00           | 0               | \-                  |
| A3 (Gratis)    | 0,00        | \-                  | 5           | \-              |                 |                     |
| Summe          |             | 1.350,00            |             | 63,00           |                 | 9,00                |

| Begünstigter                              | Anteil                   | Fälligkeit            | Betrag  |
|-------------------------------------------|--------------------------|-----------------------|---------|
| Rossi (Vertreter, 30 % bei Rechnung)      | Rate 0 – bei Rechnung    | 10/03 (Buchung)       | 18,90   |
|                                           | Rate 1 (35 %)            | 31/03                 | 22,05   |
|                                           | Rate 2 (35 %)            | 30/04                 | 22,05   |
| Bianchi (Gebietsleiter, 0 % bei Rechnung) | Rate 1 (50 %)            | 31/03                 | 4,50    |
|                                           | Rate 2 (50 %)            | 30/04                 | 4,50    |

Neri (Bereichsleiter) erhält nichts, weil er keine Rolle hat, auch wenn die Zeile A1 in seiner Spalte 0,5 % hat.

### Anzahlungsrechnungen

SAP bucht eine Anzahlungsrechnung mit den vollständigen Zeilen des Auftrags und einem Belegrabatt, der dem
Komplement der Anzahlung entspricht (Anzahlung 30 % = Rabatt 70 %): Das Add-on verwendet immer diesen Rabatt, daher
ist der Nettobetrag der Anzahlungsanteil (10.000 × 30 % = 3.000 → 150,00 bei 5 %). Wenn die Schlussrechnung die
Anzahlung abzieht, werden von ihrer Provision (10.000 × 5 % = 500,00) die bereits berechneten 150,00 abgezogen: Es
bleiben 350,00, die wie üblich auf die Anteile verteilt werden. Solange die Schlussrechnung berechnete Provisionen
hat, kann die Anzahlung weder neu berechnet noch gelöscht werden (die Rechnung ist zu korrigieren).

### Was nicht neu berechnet wird

- Belege mit **abgerechneten oder festgeschriebenen** Anteilen (zuerst die Abrechnung entfernen, Kapitel 11);
- Anzahlungsrechnungen, die bereits von einer berechneten Rechnung abgezogen sind;
- stornierte Belege: Sie werden nicht berechnet; wurden sie vor dem Storno berechnet, ist ihre Provision manuell in
  Berechnete Provisionen zu löschen (die Abrechnung ignoriert sie).

## 11. Berechnete Provisionen: anzeigen und korrigieren

![Provvigioni calcolate](../../_img/commissionmanagement/provvigioni.png)

*Berechnete Provisionen: Liste, Belegzeilen mit dem % des Begünstigten und Anteile*

Die Liste oben zeigt eine Zeile je Beleg und Begünstigtem (Filter nach Vertreter, Typ, Zeitraum, Nummer, Nur nicht
abgerechnete): Nettobetrag, Provision, abgerechnet, abzurechnen, Berechnungsdatum. Klickt man eine Zeile an,
erscheinen darunter die **Belegzeilen** mit dem Prozentsatz dieses Begünstigten und die **Anteile**. Ein
Doppelklick öffnet den Beleg in SAP.

Mit geänderten % berechnen  
Man ändert den Prozentsatz in den Zeilen unten (Spalte *%*) und berechnet nur diese Provision neu. Der SAP-Beleg
bleibt unberührt: So lässt sich ein einzelner Fall korrigieren, ohne die Regeln zu ändern. Beispiel: Zeile A2 von
4 % auf 6 % → aus 63,00 wird 72,00, die Anteile werden 21,60 / 25,20 / 25,20.

Aus Beleg neu berechnen  
Berechnet mit den aktuellen Prozentsätzen der Belegzeilen (oder den von der Prüfung korrigierten) neu: hebt die
Änderungen mit der vorigen Schaltfläche auf und übernimmt Korrekturen am Beleg.

Anteile speichern  
Abrechnungsdatum, abgerechneter Betrag und Haken *Festgeschrieben* der Anteile lassen sich manuell ändern
(Abrechnungen außerhalb des Verfahrens, Bereinigungen): Anteile speichern speichert sie und aktualisiert den
abgerechneten Betrag im Kopf.

Provision löschen  
Entfernt die Provision dieses Begünstigten auf dem Beleg; der Beleg kann danach wieder über die
Provisionsberechnung berechnet werden (nur der Beleg oder im Zeitraum).

Neuberechnung und Löschen sind gesperrt, wenn ein Anteil bereits abgerechnet oder festgeschrieben ist („Provisionen
bereits abgerechnet oder festgeschrieben: zuerst die Abrechnung entfernen“: in Anteile speichern den abgerechneten
Betrag auf null setzen), wenn der Beleg in der **geschlossenen Periode** liegt (Registerkarte Abrechnung der
Konfiguration) und, aus Vorsicht, wenn der Mitarbeiter nicht zur Hierarchie des Vertreters des Belegs gehört (die
Neuberechnung würde ihn löschen: wenn gewollt, Provision löschen verwenden).

**Nachvollziehbarkeit**: Jeder Kopf und jeder Anteil zeigt *Herkunft*, *Benutzer* und *Letzte Änderung*: wer
diesen Wert zuletzt geschrieben hat und wie. Herkunft der Köpfe: *Berechnung* (aus dem Menü), *Automatisch beim
Buchen* (beim Buchen der Rechnung), *Neuberechnung aus Beleg*, *Neuberechnung mit geänderten %*; der Anteile:
*Berechnung*, *Abrechnung*, *Storno unbezahlt*, *Manuell* (Anteile speichern).

## 12. Abrechnung

![Liquidazione](../../_img/commissionmanagement/liquidazione.png)

*Abrechnung: Vorschläge der abzurechnenden Anteile zum 31/03*

1.  Den **Stichtag** angeben (normalerweise Monatsende), ob Gutschriften einbezogen werden, und auf Wunsch die zu
    verarbeitenden Vertreter markieren (keiner = alle). **Verarbeiten**.
2.  Das Raster schlägt vor:
    - **Abrechnen** – noch nicht abgerechnete und nicht festgeschriebene Anteile mit Fälligkeit bis zum Stichtag:
      - den Anteil bei Rechnung (Rate 0) immer, zu seiner Fälligkeit (Buchungsdatum des Belegs);
      - den Anteil einer Rate, wenn diese Rate in SAP **geschlossen** ist; den Anteil auf den Gesamtbetrag (Rate -1),
        wenn alle Raten geschlossen sind;
      - das vorgeschlagene **Abrechnungsdatum** ist das spätere aus Fälligkeit der Rate und Zahlungsdatum. Das
        Zahlungsdatum berücksichtigt Zahlungen (Zahlungsdatum oder dessen Fälligkeit, wenn später), eingelöste
        Wechsel, Abstimmungen mit Journalbuchungen oder Gutschriften sowie Gutschriften zur Rechnung; lässt es sich
        nicht ermitteln, gilt die Fälligkeit.
    - **Stornieren** (rote Zeilen) – bereits abgerechnete, nicht festgeschriebene Anteile, deren Raten wieder offen
      sind (stornierte Zahlung, unbezahlter Posten): Die Abrechnung wird entfernt, und der Betrag ist
      wieder abzurechnen.
3.  Den Haken bei den Zeilen entfernen, die nicht gebucht werden sollen, bei Bedarf das Abrechnungsdatum
    korrigieren, **Festschreiben** bei den Anteilen markieren, die endgültig werden sollen. Die Summen unten werden
    mit den Haken aktualisiert.
4.  **Bestätigen** bucht die markierten Zeilen; der abgerechnete Betrag der Belege wird aktualisiert, und eine
    weitere Verarbeitung schlägt sie nicht erneut vor.

![Storno](../../_img/commissionmanagement/liquidazione_storno.png)

*Nach dem Storno einer Zahlung: Vorschlag zum Storno der abgerechneten Anteile*

Beispiel: Bei der Rechnung 1001 ist die erste Rate (Fälligkeit 31/03) am 05/04 bezahlt. Bei der Verarbeitung zum
30/04 werden der Anteil Rate 1 von Rossi (22,05) und von Bianchi (4,50) mit Abrechnungsdatum 05/04 vorgeschlagen.
Wird die Zahlung storniert, schlägt die nächste Verarbeitung den Storno der beiden Anteile vor; war der Anteil von
Rossi festgeschrieben, wird nur der Storno von Bianchi vorgeschlagen.

> Ein **festgeschriebener** Anteil ist endgültig: Er wird nicht storniert, und die Provision des Belegs wird nicht
> erneut berechnet. Festschreiben, wenn die Provisionen an den Vertreter ausgezahlt wurden.

### Teilzahlungen (Option)

![Liquidazione con incasso parziale](../../_img/commissionmanagement/liquidazione_parziale.png)

*Teilzahlung: gelbe Zeilen mit dem abrechenbaren Teil, dem vollen Anteil und dem bereits abgerechneten Betrag*

Normalerweise wird der Anteil einer Rate erst abgerechnet, wenn die Rate **geschlossen** ist: Zahlt der Kunde eine
Teilzahlung, bleibt die Provision stehen. Mit der Option **Teilzahlungen** wird der Anteil im Verhältnis zum
gezahlten Betrag abgerechnet: Rate über 816,75 mit Anteil 22,05, der Kunde zahlt 408,38 (die Hälfte) →
vorgeschlagen wird die Abrechnung von **11,03** (gelbe Zeile, mit den Spalten *Voller Anteil* 22,05 und *Bereits
abgerechnet* 0), zum Zahlungsdatum, wenn es nach der Fälligkeit liegt; bei der Restzahlung wird der Rest
vorgeschlagen, **11,02**. Wird eine Zahlung storniert, setzt der Storno den abgerechneten Betrag auf den noch
bezahlten Teil zurück (alles, wenn nichts bezahlt bleibt). Die Anteile bei Rechnung (Rate 0) ändern sich nicht; bei
Anteilen „auf den Gesamtbetrag“ bezieht sich das Verhältnis auf die Zahlungen aller Raten.

### Geschlossene Periode (Option)

Wenn die Auszüge eines Monats übergeben sind, kann man **die Periode** bis zu diesem Datum **schließen**
(Registerkarte Abrechnung der Konfiguration): Von da an werden für Belege mit Datum in der Periode keine Provisionen
neu berechnet oder gelöscht, keine Anteile geändert und keine Abrechnungen oder Stornos mit einem Datum in der
Periode gebucht, keine Anpassungen oder Prämien in geschlossenen Monaten gespeichert, und die Prüfung korrigiert
keine gebuchten Belege. In jedem Fall lautet die Meldung *„Periode bis TT/MM/JJJJ geschlossen“*, noch vor jeder
Bestätigungsfrage (sind die Anteile bereits abgerechnet, lautet sie stattdessen *„Provisionen bereits abgerechnet oder festgeschrieben“*). Eine nie berechnete Rechnung der Periode lässt sich weiterhin berechnen. Für eine
Korrektur: das Datum zurücksetzen (oder den Haken entfernen), korrigieren, wieder einstellen.

## 13. Anpassungen

![Conguagli](../../_img/commissionmanagement/conguagli.png)

*Anpassungen eines Monats*

Manuelle Beträge je Vertreter und Monat, positiv oder negativ (Prämien, Erstattungen, Rückforderungen,
Korrekturen), mit Reihenfolge und Beschreibung. Man wählt Jahr und Monat (Pfeile \< und \> zum Monatswechsel,
**Anzeigen**), fügt Zeilen hinzu oder löscht sie und drückt **Speichern**: Die Zeilen des Monats werden durch die des
Rasters ersetzt. Die Anpassungen erscheinen im Auszug „Abgerechnete Provisionen und Anpassungen“ des Monats. Die
Spalte *Typ* unterscheidet *manuelle* Anpassungen (*Manuell*) von den durch die Staffeln gebuchten *Prämien*
(*Staffelprämie*, Kapitel 15), die hier sichtbar, aber nicht änderbar sind. Bei aktiver geschlossener Periode
werden geschlossene Monate nicht gespeichert.

### Rechnungsentwürfe der Vertreter (Option)

![Bozze fatture agenti](../../_img/commissionmanagement/bozze.png)

*Anpassungen: unten die für den Monat erstellten Rechnungsentwürfe, mit Link zum Entwurf und zum Lieferanten*

Wenn der Vertreter dem Unternehmen die Provisionen in Rechnung stellt, bereitet die Schaltfläche
**Rechnungsentwürfe** den Beleg an seiner Stelle vor. Für den gewählten Monat, für jeden verwalteten Vertreter mit
verknüpftem **Lieferanten** (Kapitel 6):

- Betrag = **im Monat abgerechnete** Anteile (nach Abrechnungsdatum) + **Anpassungen und Prämien** des Monats;
- positiver Betrag → Entwurf einer **Eingangsrechnung**; negativer → Entwurf einer **Eingangsgutschrift**;
  null → nichts;
- der Entwurf hat eine Servicezeile auf dem in der Konfiguration angegebenen Konto, mit dem gewählten
  Steuerkennzeichen (oder dem Standard des Lieferanten) und dem Betrag als Zeilensumme.

Beispiel: Rossi (Lieferant V20000), April: am 05/04 abgerechnete Rate von 22,05 + Anpassungen +50,00 und -20,00 =
Entwurf einer Eingangsrechnung über **52,05**. Am Ende fasst eine Meldung Vertreter für Vertreter zusammen (Entwurf
erstellt, kein Lieferant, Betrag null, Entwurf bereits vorhanden). Die Entwürfe des Monats stehen im unteren Raster
mit dem **Status** (offen, geschlossen, also bereits in eine Rechnung umgewandelt, gelöscht), dem Datum und dem
Benutzer; der gelbe Pfeil öffnet den Entwurf oder den Lieferanten. Ein Vertreter mit einem noch vorhandenen Entwurf
für diesen Monat wird übersprungen: Zum erneuten Erstellen den Entwurf in SAP löschen. Der Entwurf wird dann in SAP
wie jeder andere Entwurf vervollständigt und gebucht (Nummer und Datum der Rechnung des Vertreters).

## 14. Provisionsauszug

![Estratto provvigioni](../../_img/commissionmanagement/estratto.png)

*Auszug „Abgerechnete Provisionen und Anpassungen“ für April, nach Vertreter gruppiert*

Drei Auszüge, für einen Zeitraum und für einen oder alle Vertreter, nach Vertreter gruppiert (Pfeile zum Auf- und
Zuklappen), mit der Summe am Ende und **CSV exportieren** (eine Zeile „Summe“ für jeden Vertreter, in Excel zu
öffnen):

| Auszug                                    | Was er zeigt                                                                                           | Zeitraum bezogen auf  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------|
| Berechnete Provisionen                    | eine Zeile je Beleg und Begünstigtem: Nettobetrag, Provision, abgerechnet                              | Belegdatum            |
| Abzurechnende Provisionen                 | die noch nicht (oder teilweise) abgerechneten und nicht festgeschriebenen Anteile                      | Fälligkeit des Anteils |
| Abgerechnete Provisionen und Anpassungen  | die abgerechneten Anteile plus die Anpassungen der Monate des Zeitraums: **was dem Vertreter zusteht** | Abrechnungsdatum      |

### Drucken / PDF

![Estratto stampato](../../_img/commissionmanagement/estratto_stampa.png)

*Der im Browser geöffnete Auszug: ein Block je Vertreter, Summen und Einbehalt als Richtwert*

Die Schaltfläche **Drucken / PDF** öffnet den angezeigten Auszug formatiert im Browser: Kopf mit Firma, Art des
Auszugs und Zeitraum, ein Block für jeden Vertreter mit seinen Zeilen und der Summe. Von dort wird gedruckt oder als
PDF gespeichert (Drucken → „Als PDF speichern“). Ist in der Konfiguration der **Einbehalt (Richtwert)** angegeben
(z. B. 8,5 „Enasarco quota agente“), zeigt der Auszug „Abgerechnete Provisionen und Anpassungen“ für jeden Vertreter
auch die Zeile des Einbehalts und das **Netto (Richtwert)**: Das sind Hilfsangaben für den Vertreter, ohne Mindest-
und Höchstbeträge.

### An Vertreter senden (Option)

Mit aktivem E-Mail-Versand (Registerkarte E-Mail der Konfiguration) sendet die Schaltfläche **An Vertreter
senden** jedem Vertreter des angezeigten Auszugs eine Nachricht mit **nur seinem eigenen Auszug** als HTML-Anhang
(in jedem Browser zu öffnen und zu drucken). Die Adresse ist die des Vertriebsmitarbeiters oder, falls sie fehlt,
die des verknüpften Lieferanten. Am Ende meldet eine Zusammenfassung für jeden Vertreter, ob der Versand
erfolgreich war, ob die Adresse fehlt oder welchen Fehler der Server gemeldet hat. Die Schaltfläche ist nur für
Benutzer mit voller Berechtigung für den Auszug aller Vertreter aktiv.

### Jeder Vorgesetzte sieht seine Vertreter

Ein SAP-Benutzer, der mit einem Mitarbeiter verknüpft ist (Spalte *SAP-Benutzer* in Vertreter) und nicht die
Berechtigung „Estratto di tutti gli agenti“ (Auszug aller Vertreter) hat, findet in der Auswahlliste nur *(meine
Vertreter)* sowie seinen Namen und die seiner Unterstellten (die Mitarbeiter, deren Gebietsleiter,
Bereichsleiter oder Direktor er ist): Ein Gebietsleiter kann den Auszug seiner Vertreter einsehen, ohne die anderen
zu sehen. Wer mit keinem Mitarbeiter verknüpft ist und die Berechtigung nicht hat, sieht nichts.

## 15. Staffeln und Prämien

![Scaglioni e premi](../../_img/commissionmanagement/scaglioni.png)

*Staffeln und Prämien: oben die Staffeln, unten die für das Jahr berechneten Prämien*

Mit der Option „Jahresumsatz-Staffeln mit Prämie“ (Registerkarte Vertreter der Konfiguration) verwaltet das Menü
**Staffeln und Prämien** die umsatzabhängigen Prämien zum Jahresende. Eine **Staffel** hat: Vertreter (oder
*alle*), Jahr (oder *jedes Jahr*), Schwelle des Jahresnettoumsatzes, Prämienart (*% vom Jahresumsatz* oder
*Festbetrag*), Prämie, Beschreibung, aktiv. Zeilen werden im oberen Raster hinzugefügt, geändert und gelöscht; dann
**Staffeln speichern** drücken.

| Vertreter | Jahr          | Schwelle | Typ                | Prämie | Beschreibung      |
|-----------|---------------|----------|--------------------|--------|-------------------|
| (alle)    | (jedes Jahr)  | 1.000    | % vom Jahresumsatz | 0,5    | Premio base       |
| (alle)    | (jedes Jahr)  | 10.000   | % vom Jahresumsatz | 1      | Premio 10.000     |
| Rossi     | 2026          | 12.000   | Festbetrag         | 500,00 | Premio Rossi 2026 |

**Prämien berechnen** für ein Jahr: Der Umsatz jedes Vertreters ist die Summe der Nettobeträge seiner berechneten
Provisionen (Rechnungen und Gutschriften mit Datum im Jahr; nicht die Anzahlungsrechnungen, die bereits in den
Schlussrechnungen enthalten sind). Die erreichte Staffel ist die mit der **höchsten Schwelle**, die den Umsatz nicht
übersteigt; die Staffeln des Vertreters haben Vorrang vor denen für alle, ein bestimmtes Jahr hat Vorrang vor „jedes
Jahr“. Prämie = Umsatz × % oder Festbetrag. Beispiel mit den obigen Staffeln: Rossi 13.150 → Staffel 12.000 des
Vertreters → **500,00**; Bianchi 2.900 → Staffel 1.000 → 0,5 % = **14,50**; Verdi 1.488 → **7,44**. Die Spalte
*Bereits gebucht* zeigt die bereits gebuchte Prämie desselben Jahres.

**Markierte Prämien buchen**: Die markierten Zeilen werden zu Anpassungen vom Typ *Staffelprämie* im gewählten Monat
(normalerweise Dezember): Von dort fließen sie wie die anderen Anpassungen in den Auszug „Abgerechnete Provisionen
und Anpassungen“, in die Rechnungsentwürfe und in die Summen des Monats ein. Wird dasselbe Jahr erneut gebucht, wird
die vorherige Prämie ersetzt (nicht verdoppelt); eine Prämie von null entfernt sie. Bei aktiver geschlossener
Periode werden geschlossene Monate nicht gebucht.

## 16. Prüfungen und Hinweise beim Start

![Verifiche](../../_img/commissionmanagement/verifiche.png)

*Prüfungen: Anomalien des Zeitraums, Fehler in Rot*

Das Menü **Prüfungen** sucht in einem Zeitraum alles, was eine Provision fehlen lassen oder verfälschen kann. Man
gibt den Zeitraum an, ob auch nicht abgerechnete Zahlungen gesucht werden sollen (die langsamste Suche), und drückt
**Prüfen**: Jede Anomalie hat einen Schweregrad (**Fehler** in Rot, **Warnung**), die Prüfung, die sie gefunden hat,
den Vertreter, den Beleg und eine Erklärung mit dem, was zu tun ist. Ein Doppelklick öffnet den Beleg.

| Prüfung                       | Was sie meldet                                                                                                                                  | Was zu tun ist                                    |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Zu berechnen                  | Rechnungen, Anzahlungen und Gutschriften des Zeitraums mit verwaltetem Vertreter und ohne Provisionen                                           | Provisionsberechnung                              |
| Ohne Vertreter                | Belege ohne Vertriebsmitarbeiter oder mit einem Mitarbeiter ohne Rolle                                                                          | prüfen, ob gewollt; Rolle in Vertreter vergeben   |
| Zeilen ohne %                 | Belege mit verwaltetem Vertreter, deren Zeilen alle Prozentsätze null haben                                                                     | Prüfung und Zuordnung % oder fehlende Regeln      |
| Vertreter geändert            | berechnete Belege, deren Vertriebsmitarbeiter in SAP nicht der der Provision ist                                                                | Aus Beleg neu berechnen (Berechnete Provisionen)  |
| Storniert                     | stornierte Belege mit berechneten Provisionen                                                                                                   | Provision löschen                                 |
| Vertreterhierarchie           | Vorgesetzter ohne Rolle (sein Anteil wird nicht fällig), Standardprozentsatz einer Rolle ohne Vorgesetzten, nicht vorhandener SAP-Benutzer      | in Vertreter bereinigen                           |
| Überlappende Regeln           | zwei gleiche aktive Regeln (gleiche Felder, gleicher Rabatt und Mitarbeiter) mit überlappenden Zeiträumen: Es gilt nur eine der beiden          | die Regeln korrigieren                            |
| Nicht abgerechnete Zahlungen  | Anteile, deren Rate seit mehr als den in der Konfiguration angegebenen Tagen bezahlt und noch nicht abgerechnet ist                             | Abrechnung                                        |

Mit der Option **Hinweise beim Start** führt das Add-on bei jedem Start die Schnellprüfungen aus (zu berechnende
Belege der letzten 90 Tage, geänderter Vertreter und stornierte Belege im letzten Jahr) und meldet, wenn es etwas
findet, dies einige Sekunden nach dem Start in der Statusleiste, also nach eventuellen Meldungen der Lizenz:
*„Provisionen: 3 Anomalien zu prüfen (Provisionen \> Prüfungen)“*. Ohne Anomalien wird nichts angezeigt.

## 17. Berechtigungen und Nachvollziehbarkeit

Das Add-on legt in den **Allgemeinen Berechtigungen** von SAP (Administration › Systeminitialisierung ›
Berechtigungen) den Eintrag **Provvigioni** (Provisionen) unter *Benutzerberechtigungen* mit fünf Untereinträgen an.
Superuser haben immer alle Rechte; den anderen Benutzern wird für jeden Eintrag *Keine Berechtigung*,
*Schreibgeschützt* oder *Volle Berechtigung* zugewiesen:

![Autorizzazioni generali](../../_img/commissionmanagement/autorizzazioni.png)

*Allgemeine Berechtigungen: der Eintrag Provvigioni mit den fünf Untereinträgen, für einen Benutzer ohne
Berechtigungen*

| Berechtigung                                                                  | Schreibgeschützt                                                                   | Volle Berechtigung                                                              |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Configurazione (Konfiguration)                                                | –                                                                                  | die Konfiguration öffnen und speichern                                          |
| Agenti, regole e scaglioni (Vertreter, Regeln und Staffeln)                   | anzeigen                                                                           | Vertreter, Regeln und Staffeln speichern                                        |
| Controllo, calcolo e verifiche (Kontrolle, Berechnung und Prüfungen)            | Prüfung, Berechnung, Berechnete Provisionen, Prüfungen anzeigen                    | % übernehmen, berechnen, neu berechnen, Anteile speichern, löschen              |
| Liquidazione, conguagli e bozze fatture (Abrechnung, Anpassungen und Rechnungsentwürfe) | Abrechnung und Anpassungen anzeigen                                      | Abrechnungen bestätigen, Anpassungen speichern, Prämien buchen, Entwürfe erzeugen |
| Estratto di tutti gli agenti (Auszug aller Vertreter)                         | den Auszug aller Vertreter sehen (ohne: nur die eigenen, Kapitel 14)               | auch der E-Mail-Versand                                                         |

Ohne Berechtigung antwortet der Menüeintrag in der Statusleiste mit *„Funktion nicht erlaubt: erfordert die
Berechtigung „…“ (Allgemeine Berechtigungen \> Provvigioni)“*; mit Schreibschutz öffnet sich das Fenster, aber die
ändernden Schaltflächen antworten mit *„Vorgang nicht erlaubt: erfordert die volle Berechtigung für „…““*.

**Nachvollziehbarkeit**: Köpfe und Anteile der Provisionen speichern Herkunft, Benutzer und Datum des letzten
Schreibvorgangs (Kapitel 11); die Anpassungen Benutzer und Änderungsdatum; die Rechnungsentwürfe, wer sie wann
erstellt hat. Das Log des Add-ons (Kapitel 19) protokolliert Fehler und Aktualisierungen der Struktur.

## 18. Häufige Fragen und Probleme

Die Prozentsätze werden nicht in den Beleg geschrieben  
Prüfen: die Option in der Konfiguration; dass der Beleg einen Vertriebsmitarbeiter mit einer Rolle hat; dass der
Kunde ausgefüllt ist. Nach einem Kundenwechsel den Vertreter erneut wählen.

Ich habe einen Prozentsatz in der Rechnung korrigiert, aber SAP lässt mich nicht speichern  
Gebuchte Rechnungen lassen sich nicht ändern. Prüfung und Zuordnung % (vor der Berechnung) oder Berechnete
Provisionen → Mit geänderten % berechnen (danach) verwenden.

„Provisionen bereits abgerechnet oder festgeschrieben“  
Zum Neuberechnen oder Löschen in Berechnete Provisionen den abgerechneten Betrag der Anteile auf null setzen
(Anteile speichern) und die Festschreibung entfernen. Wurden die Anteile tatsächlich an den Vertreter ausgezahlt,
besser nicht ändern: die Differenz als Anpassung buchen.

„Anzahlung bereits von einer Rechnung mit berechneten Provisionen abgezogen“  
Zuerst die Provision der Schlussrechnung korrigieren oder löschen, dann die Anzahlung, dann die Rechnung neu
berechnen.

Ein Anteil wird bei der Abrechnung nicht vorgeschlagen  
Die Rate ist in SAP nicht geschlossen (Teilzahlung oder noch nicht gebucht), die Fälligkeit liegt nach dem
Stichtag, oder der Anteil ist bereits abgerechnet/festgeschrieben. Anteile stornierter Belege werden nicht
vorgeschlagen: die Provision löschen.

Beim ersten Start fordert SAP auf, alle Fenster zu schließen  
Das ist normal, wenn Benutzerfelder angelegt werden: mit Ja antworten, bis das Anlegen abgeschlossen ist (einige
Minuten). Das gilt auch, wenn eine Aktualisierung des Add-ons Felder hinzufügt; wird der Client mittendrin
geschlossen, wird das Anlegen beim Neustart des Add-ons fortgesetzt.

„Periode bis ... geschlossen“  
Der Vorgang betrifft ein Datum innerhalb der geschlossenen Periode (Konfiguration, Registerkarte Abrechnung). Ist
die Korrektur wirklich nötig: das Sperrdatum zurücksetzen, korrigieren, wieder einstellen.

„Funktion nicht erlaubt“  
Der SAP-Benutzer hat die Berechtigung nicht (Kapitel 17): sie in den Allgemeinen Berechtigungen, Eintrag
Provvigioni, zuweisen.

Die Rechnung wurde gebucht, aber die Statusleiste meldet „Provisionen nicht berechnet“  
Die automatische Berechnung war nicht möglich (Anzahlung bereits abgezogen, geschlossene Periode, Vertreter nicht
verwaltet): Der Beleg ist normal gebucht; ihn über die Provisionsberechnung berechnen (die Prüfungen führen ihn unter
„Zu berechnen“).

Der E-Mail-Versand meldet einen Fehler  
„Testversand“ in der Registerkarte E-Mail der Konfiguration verwenden: Die Meldung des Servers zeigt, ob Server,
Port, SSL oder Zugangsdaten falsch sind. Vertreter „ohne E-Mail“ sind in den Stammdaten des Vertriebsmitarbeiters
oder des verknüpften Lieferanten zu ergänzen.

Eine Belegzeile übernimmt die Prozentsätze der Regeln nicht  
Mit der Option „Manuell geänderte Prozentsätze schützen“ ist die Zeile als manuell markiert (Spalte Provv. %
manuali): den Haken entfernen und Artikel, Preis oder Rabatt ändern oder manuell korrigieren.

Während das Add-on arbeitet, reagiert SAP nicht  
Während Prüfen, Berechnen, Verarbeiten und Übernehmen wartet SAP auf das Add-on (Statusleiste „Bitte warten...“):
das Fenster nicht schließen und das Add-on nicht beenden, sonst bleibt der Client im Wartezustand und muss neu
gestartet werden.

## 19. Daten und technische Hinweise

| Wo                                                          | Was                                                                                                                                                                                                         |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLP (Vertriebsmitarbeiter)                                 | Felder `U_XEI_PRV_Ruolo`, `_CapoZona`, `_CapoArea`, `_Direttore`, `_PercAg`, `_PercCZ`, `_PercCA`, `_PercDI`, `_Fatturato`, `_Liquida`, `_Fornitore`, `_Utente` (SAP-Benutzer)                             |
| Zeilen der Marketingbelege (RDR1, INV1, RIN1, DPI1...)      | `U_XEI_PRV_Ag`, `_CZ`, `_CA`, `_DI` (Prozentsätze), `_ScEff` (effektiver Rabatt), `_Man` (manuelle Zeile)                                                                                                   |
| `@XEI_PRV_REGOLE`                                           | Prozentregeln                                                                                                                                                                                               |
| `@XEI_PRV_DOC`, `@XEI_PRV_RIGHE`, `@XEI_PRV_RATE`           | berechnete Provisionen: Kopf je Beleg und Begünstigtem, Zeilen, Anteile (Code = Typ-DocEntry-Mitarbeiter\[-Zeile/Rate\], z. B. `13-386-61-2`); Köpfe und Anteile mit Herkunft, Benutzer und Änderungsdatum |
| `@XEI_PRV_PERC`                                             | von der Prüfung korrigierte Prozentsätze für Zeilen gebuchter Belege                                                                                                                                        |
| `@XEI_PRV_CONG`                                             | Anpassungen (Typ M manuell / P Prämie, Bezugsjahr der Prämie)                                                                                                                                               |
| `@XEI_PRV_SCAG`, `@XEI_PRV_BOZZE`                           | Staffeln; erstellte Rechnungsentwürfe (Vertreter, Monat, Entwurf, Lieferant, Betrag)                                                                                                                        |
| `@XEI_SETTINGS` (Bereich XEI.CommissionManagement)          | Optionen der Konfiguration (SMTP-Kennwort verschlüsselt) und Version der Datenstruktur                                                                                                                      |
| Berechtigungen (OUPT)                                       | `XEI_PRV` und Untereinträge `XEI_PRV_P_CFG`, `_ANAG`, `_CALC`, `_LIQ`, `_EST`                                                                                                                               |

- Belegarten: 13 Rechnung, 203 Anzahlungsrechnung, 14 Gutschrift, 17 Auftrag (nur in der Prüfung).
- Alles läuft über die DI API von SAP (keine direkte Verbindung zur Datenbank).
- Leistung: In den Belegen werden die Zeilen in einem Block gelesen (ein einziger Aufruf), und nur die Zellen, die
  sich ändern, werden geschrieben; Kunden, Artikel und Preislisten werden einmal je Fenster gelesen. In der
  Abrechnung werden die Zahlungsdaten (die aufwendigste Suche) nur für die tatsächlich abrechenbaren Anteile
  berechnet.
- Log: `%LOCALAPPDATA%\XEI\logs\XEI.CommissionManagement.log`.
