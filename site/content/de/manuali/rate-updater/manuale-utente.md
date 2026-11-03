---
title: XEI Rate Updater für SAP Business One – Benutzerhandbuch
description: "Wechselkurse in SAP Business One: Installation, erster Start, Aktualisierung von Hand und automatisch, Verlauf und Lizenz."
lang: de
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater für SAP Business One – Benutzerhandbuch

| | |
|---|---|
| SAP Business One | 10.0 oder höher, mit dem Service Layer |
| Datenbank | Microsoft SQL Server oder SAP HANA (bei SAP HANA wird ein Test bei der Installation empfohlen) |
| System | Windows 10 und 11, Windows Server 2016 und höher, 64 Bit; Microsoft Edge WebView2 Runtime |
| Sprachen des Programms | Italienisch, Englisch, Deutsch, Französisch, Spanisch, Türkisch |

## 1. Was das Programm macht

XEI Rate Updater für SAP Business One aktualisiert die **Wechselkurse** in SAP Business One mit den Kursen, die eine
amtliche Quelle veröffentlicht:

1. er holt die Kurse der gewählten **Quelle** für das gewünschte Datum;
2. er liest aus der SAP-Firma die **Hauswährung** und die **Notierung** der Wechselkurse: direkter Kurs (Hauswährung
   für eine Einheit Fremdwährung) oder indirekter Kurs (Fremdwährung für eine Einheit Hauswährung);
3. ist die Hauswährung nicht der Euro, berechnet er die **Kreuzkurse** zu dieser Währung;
4. für jede **von der Firma geführte Währung** schreibt er den Wechselkurs zum Datum in SAP, in der Notierung der
   Firma, abgeschnitten auf sechs Dezimalstellen;
5. er speichert den Durchlauf im **Verlauf**.

Ein Fehler bei einer Währung hält die anderen nicht auf.

### Das Datum der Kurse

Die Kurse eines Tages werden am Ende des Tages veröffentlicht. Für die Wechselkurse eines Tages in SAP werden daher die
**am Vortag** veröffentlichten Kurse verwendet. An Tagen ohne Veröffentlichung (Wochenenden, Feiertage) gilt der letzte
Veröffentlichungstag davor.

*Beispiel*: Die Wechselkurse für Montag, 24. Februar 2025, sind die Kurse von Freitag, 21. Februar. Das Datum der
Wechselkurse darf nicht in der Zukunft liegen.

### Die Kursquellen

| Quelle | Hinweise |
|---|---|
| Europäische Zentralbank (EZB) | Standard, kostenlos, ohne Schlüssel |
| Banca d'Italia | amtliche italienische Wechselkurse, viele Währungen |
| Open Exchange Rates | erfordert einen API-Schlüssel von Open Exchange Rates (Einstellungen › Wechselkurse) |

Alle Quellen veröffentlichen die Kurse gegenüber dem Euro. Bei einer anderen Hauswährung als dem Euro muss die Quelle
diese notieren.

### Die Währungen

Das Programm erkennt die Währungen am **ISO-Code** (zum Beispiel `USD`, `CHF`). In SAP müssen die Fremdwährungen den
ISO-Code als Code haben. Hat die Hauswährung in SAP einen anderen Code (zum Beispiel „Eu“ oder „€“ für den Euro), geben
Sie den ISO-Code unter *Einstellungen › Wechselkurse* an.

## 2. Installation

1. Entpacken Sie den Ordner aus der ZIP-Datei auf den PC, zum Beispiel nach `C:\XEI\RateUpdater`.
2. Starten Sie **XEI.RateUpdater.exe**. Das Programm enthält bereits .NET. Erforderlich ist **Microsoft Edge WebView2
   Runtime**, die meist bereits vorhanden ist: Fehlt sie, meldet das Programm dies und bietet den Download an.

Das Programm hat keine Installation. Die Einstellungen und der Verlauf liegen im Windows-Datenordner für alle Benutzer
des PCs. Sie gelten daher für jeden, der das Programm auf diesem PC verwendet, und für die geplante Aktualisierung.

## 3. Erster Start

Beim ersten Öffnen zeigt das Programm die Seite **Erster Start**: Es ist noch nicht mit SAP verbunden. Der Code für den
ersten Start ist bereits eingetragen.

1. **SAP-Verbindung**:
   - *Adresse des Service Layers*;
   - *SAP-Firmen*: die Datenbanken, die bei der Anmeldung wählbar sind;
   - **Verbindung testen**.
2. **Anmeldung und erster Administrator**:
   - *Anmeldung der Bediener*: **SAP-Benutzer jedes Einzelnen** (jeder meldet sich mit seinem eigenen SAP-Benutzer an)
     oder **Eigene Benutzer und technischer SAP-Benutzer**;
   - *SAP-Benutzer des ersten Administrators* (zum Beispiel `manager`);
   - *Technischer SAP-Benutzer* und sein Passwort: Sie werden für die **automatische Aktualisierung** benötigt. Am besten
     ein eigener Benutzer, der nur die Berechtigung hat, Wechselkurse zu schreiben.
3. **Speichern und neu starten**: Das Programm öffnet sich wieder auf der Anmeldeseite.

Dieselben Einstellungen ändern Sie später unter **Einstellungen › SAP**.

![Erster Start](../../_img/rateupdater/00b-primo-avvio.png)

*Erster Start: SAP-Verbindung, Geltungsbereich der Lizenz und erster Administrator.*

![Einstellungen › SAP](../../_img/rateupdater/05-impostazioni-sap.png)

*Einstellungen › SAP: Adresse des Service Layers, Firmen und Anmeldung der Bediener.*

## 4. Anmeldung

Sie melden sich mit dem **SAP-Business-One-Benutzer** und seinem Passwort an. Oben rechts sehen Sie Benutzer und Firma.

![Anmeldung](../../_img/rateupdater/00-accesso.png)

*Anmeldung mit dem SAP-Business-One-Benutzer.*

Mit *SAP-Benutzer jedes Einzelnen* schreibt das Programm die Wechselkurse mit dem Benutzer, der gerade arbeitet: Es
gelten seine SAP-Berechtigungen für die Wechselkurse.

### Funktionen der Benutzer

Ein Administrator weist jedem Benutzer die Funktionen auf der Seite **Benutzer** des Menüs zu, gleich für SAP-Benutzer
und eigene Benutzer:

| Funktion | Erlaubt |
|---|---|
| Wechselkurse aktualisieren | die Wechselkurse in SAP auf der Seite Wechselkurse aktualisieren |
| Verlauf | die Durchläufe der Aktualisierung ansehen, manuell und automatisch |

Der Administrator hat alle Funktionen. Der erste Administrator ist der SAP-Benutzer, der beim ersten Start angegeben
wurde.

## 5. Wechselkurse

Menü **Wechselkurse**.

1. **Datum der Wechselkurse in SAP**: Vorgabe ist heute, es darf nicht in der Zukunft liegen. Darunter steht, welche
   Kurse verwendet werden, und die eingestellte Quelle.
2. Klicken Sie auf **Wechselkurse in SAP aktualisieren**.
3. Das **Ergebnis** nennt Datum, Quelle, Tag der Kurse, die Anzahl der geschriebenen Währungen und die Hauswährung. Die
   Tabelle zeigt für jede Währung der Quelle:

| Spalte | Zeigt |
|---|---|
| Währung | ISO-Code |
| Direkter Kurs | Hauswährung für eine Einheit Fremdwährung |
| Indirekter Kurs | Fremdwährung für eine Einheit Hauswährung |
| Ergebnis | **in SAP geschrieben**, **nicht geführt** (die Firma verwendet diese Währung nicht) oder abgelehnt, mit dem Fehler von SAP |

Darunter steht der Status der **automatischen Aktualisierung** mit dem letzten Durchlauf.

![Wechselkurse](../../_img/rateupdater/01-cambi.png)

*Wechselkurse: Datum, Quelle und Status der automatischen Aktualisierung.*

![Ergebnis der Aktualisierung](../../_img/rateupdater/02-cambi-esito.png)

*Ergebnis: Kurse der Quelle, in SAP geschriebene Währungen und Währungen, die die Firma nicht führt.*

## 6. Verlauf

Menü **Verlauf**: die Durchläufe der Firma, der neueste zuerst.

| Spalte | Zeigt |
|---|---|
| Gestartet | Datum und Uhrzeit des Durchlaufs |
| Von | den Benutzer oder *automatisch* |
| Kurse zum | das Datum der Wechselkurse in SAP |
| Quelle | die Kursquelle |
| Kurse vom | den Tag der verwendeten Kurse |
| Geschriebene Währungen | wie viele Währungen in SAP geschrieben wurden |
| Ergebnis | **erfolgreich** oder **fehlgeschlagen** |

Eine Zeile lässt sich mit den Währungen aufklappen, mit den Kursen und dem Ergebnis jeder Währung. Der Verlauf behält
die letzten Durchläufe (Vorgabe 100, unter *Einstellungen › Wechselkurse*).

![Verlauf](../../_img/rateupdater/03-storico.png)

*Verlauf: manuelle und automatische Aktualisierungen der Firma.*

![Verlauf mit den Währungen](../../_img/rateupdater/03b-storico-valute.png)

*Eine aufgeklappte Zeile: Kurse und Ergebnis jeder Währung.*

## 7. Einstellungen › Wechselkurse

Nur für Administratoren. Klicken Sie nach den Änderungen auf **Einstellungen speichern**.

| Einstellung | Wirkung |
|---|---|
| Kursquelle | Europäische Zentralbank (Standard), Banca d'Italia oder Open Exchange Rates |
| ISO-Code der Hauswährung | nur wenn die Hauswährung in SAP einen anderen Code als den ISO-Code hat; leer = wird aus SAP ermittelt |
| API-Schlüssel von Open Exchange Rates | nur mit der Quelle Open Exchange Rates; wird verschlüsselt gespeichert |
| Automatische Aktualisierung | jeden Tag aktualisiert das Programm selbst die heutigen Wechselkurse jeder Firma, mit dem technischen SAP-Benutzer |
| Uhrzeit der automatischen Aktualisierung | im Format HH:mm (Standard 07:00) |
| Durchläufe im Verlauf | wie viele Durchläufe pro Firma bleiben, von 10 bis 1000 (Standard 100) |

![Einstellungen › Wechselkurse](../../_img/rateupdater/04-impostazioni-cambi.png)

*Einstellungen › Wechselkurse: Quelle, Hauswährung, automatische Aktualisierung und Verlauf.*

## 8. Automatische Aktualisierung

Die heutigen Wechselkurse werden auf zwei Arten jeden Tag aktualisiert.

### Bei geöffnetem Programm

Ist die **Automatische Aktualisierung** eingeschaltet, aktualisiert das Programm nach der eingestellten Uhrzeit die
heutigen Wechselkurse jeder Firma mit dem technischen SAP-Benutzer und speichert den Durchlauf im Verlauf (*Von*:
automatisch). War das Programm zur festgelegten Uhrzeit geschlossen, aktualisiert es, sobald es wieder geöffnet wird.
Antworten die Quelle oder SAP nicht, versucht es es kurz darauf erneut.

### Mit der Windows-Aufgabenplanung

So werden die Wechselkurse auch aktualisiert, ohne das Programm zu öffnen.

1. Führen Sie den ersten Start durch und richten Sie den **technischen SAP-Benutzer** ein (Einstellungen › SAP).

   ![Technischer SAP-Benutzer](../../_img/rateupdater/05b-impostazioni-sap-tecnico.png)

   *Der technische SAP-Benutzer unter Einstellungen › SAP.*

2. Öffnen Sie in Windows die **Aufgabenplanung** und erstellen Sie eine einfache Aufgabe, zum Beispiel täglich um 7:00.
3. Wählen Sie als Aktion **Programm starten**:
   - Programm: `XEI.RateUpdater.exe` im Programmordner;
   - Argumente: `aggiorna`.
4. Wählen Sie in den Eigenschaften der Aufgabe **Unabhängig von der Benutzeranmeldung ausführen**, mit einem
   Windows-Benutzer des PCs.

Der Befehl aktualisiert die heutigen Wechselkurse mit dem technischen SAP-Benutzer und beendet sich, ohne Fenster. Er
verwendet dieselben Einstellungen und denselben Verlauf wie das Programm. Optionale Argumente:

| Argument | Bedeutung |
|---|---|
| `--societa <database SAP>` | die zu aktualisierende Firma; bei nur einer konfigurierten Firma nicht nötig |
| `--data aaaa-mm-gg` | das Datum der Wechselkurse, wenn es nicht heute ist |

Die Aufgabenplanung erhält das Ergebnis: **0** erfolgreich, **1** fehlgeschlagen oder mit einer abgelehnten Währung,
**2** falsche Argumente. Die Einzelheiten stehen im Verlauf. Hat der Befehl die heutigen Wechselkurse bereits
aktualisiert, wiederholt das geöffnete Programm dies nicht.

## 9. Lizenz

Das Programm arbeitet mit einem **Lizenzcode**, den XEI ausstellt, in drei Geltungsbereichen:

| Geltungsbereich | Gilt für |
|---|---|
| Pro Firma | eine SAP-Datenbank |
| Pro Server | alle Firmen der SQL-Server- oder SAP-HANA-Instanz |
| Frei | ist an keine Datenbank gebunden |

Der **kostenlose Test** dauert 30 Tage und ist frei.

![Lizenz](../../_img/rateupdater/06-licenza.png)

*Die Seite Lizenz: Status, Ablauf, Geltungsbereich und Feld für den Code.*

![Einstellungen › Lizenz](../../_img/rateupdater/06b-impostazioni-licenza.png)

*Einstellungen › Lizenz: die drei Geltungsbereiche der Lizenz.*

Menü **Lizenz**: Status, Ablauf und Geltungsbereich der Lizenz. Den von XEI erhaltenen Code fügen Sie in **Lizenzcode
eingeben** ein; er gilt sofort, ohne Neustart. Für eine Lizenz pro Firma oder für den ganzen Server muss das Programm
mit Nur-Lese-Zugriff mit der Lizenzdatenbank verbunden sein (*Einstellungen › Lizenz*, **Verbindung testen**): Der
Firmencode und der Servercode, die Sie an XEI senden, erscheinen dort und auf der Seite Lizenz.

Für Lizenzen: [license@xeisrl.com](mailto:license@xeisrl.com).

## 10. Häufige Fragen und Probleme

| Was Sie sehen | Ursache | Was zu tun ist |
|---|---|---|
| Eine Währung ist *nicht geführt* | Die SAP-Firma verwendet diese Währung nicht | Nichts: Es werden nur die Währungen der Firma geschrieben |
| Eine Währung der Firma wird nicht aktualisiert | Die Währung hat in SAP nicht den ISO-Code als Code | Verwenden Sie in SAP den ISO-Code (zum Beispiel `USD`) |
| Der Durchlauf bricht sofort mit einem Fehler zur Hauswährung ab | Die Quelle notiert die Hauswährung nicht, oder sie hat in SAP keinen ISO-Code | Geben Sie den ISO-Code unter *Einstellungen › Wechselkurse* an oder wählen Sie eine andere Quelle |
| Das Ergebnis einer Währung ist ein Fehler von SAP | SAP hat den Wechselkurs abgelehnt (zum Beispiel wegen der Berechtigungen des Benutzers) | Lesen Sie den Fehler; prüfen Sie die SAP-Berechtigungen des Benutzers für die Wechselkurse |
| Die automatische Aktualisierung startet nicht | Sie ist ausgeschaltet, oder der technische SAP-Benutzer fehlt | Schalten Sie sie unter *Einstellungen › Wechselkurse* ein und richten Sie den technischen Benutzer unter *Einstellungen › SAP* ein |
| Das Programm fordert zur Installation von WebView2 auf | Microsoft Edge WebView2 Runtime fehlt | Nehmen Sie den angebotenen Download an oder installieren Sie sie von der Microsoft-Website |

## 11. Support

Für Lizenzen: [license@xeisrl.com](mailto:license@xeisrl.com). Für den Support:
[info@xeisrl.com](mailto:info@xeisrl.com). Geben Sie in Ihrer Anfrage die Programmversion (Menü *Info*) und eine
Beschreibung des Problems an.
