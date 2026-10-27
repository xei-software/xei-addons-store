---
title: XEI.ItemGenerator – Benutzerhandbuch
description: So konfigurieren Sie Basen, Werte und Varianten und generieren die Artikel mit XEI.ItemGenerator.
lang: de
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Benutzerhandbuch

Installation, Lizenz, Menüs und Berechtigungen finden Sie im
[Installationshandbuch](installazione.md).

## 1. Was das Add-on macht

XEI.ItemGenerator legt in den Artikelstammdaten Artikel an, deren Codes sich **zusammensetzen**, indem
Sie Ebene für Ebene Werte auswählen: Produkttyp, Maß, Material... Den Auswahlbaum definieren Sie
einmal; danach erfinden Sie Codes und Beschreibungen nicht mehr von Hand, sondern stellen sie in einem
Fenster zusammen: Das Add-on berechnet Code, Beschreibung, Preis, Gewicht, Maße, Gruppe, Eigenschaften
und Stückliste und legt die Artikel als Kopie eines Vorlageartikels an.

- **Einheitliche Codes**: Der Code ist „sprechend“ (z. B. `PE090` = Hängeschrank 90) plus eine laufende
  Nummer, die die Varianten unterscheidet (Farbe, Griff...).
- **Keine Dubletten**: Dieselbe Zusammensetzung erzeugt immer denselben Artikel; ist er bereits
  vorhanden, findet ihn das Add-on.
- **Viele Artikel auf einmal**: Mehrere Maße und mehrere Optionen ergeben alle Kombinationen.
- **Vollständige Artikel**: Beschreibungen (auch in einer Fremdsprache), Stammdaten, Listenpreis und
  Stückliste stammen aus der Konfiguration.
- **Aus dem Beleg**: In Angeboten und Kundenaufträgen konfigurieren Sie den Artikel der Zeile, ohne den
  Beleg zu verlassen.

### Auf einen Blick

- Generierung in einem größenveränderbaren Fenster über SAP: Codebaum und Variantenbaum mit
  Kontrollkästchen (auch in verschiedenen Zweigen), Suche, Artikelliste mit Status, Preis und Ergebnis;
  SAP bleibt bedienbar. Aussehen des SAP-Clients, Meldungen im gleichen Stil, Texte über das
  Kontextmenü änderbar.
- Preis, Gewicht, Maße, Gruppen, Eigenschaften, Fremdname und Stückliste aus Werten und Optionen
  zusammengesetzt.
- Beschreibungsformel mit Codes, Optionen und optionalen Teilen.
- Artikel konfigurieren aus Angeboten und Kundenaufträgen; ähnliche Artikel aus einem generierten
  Artikel generieren.
- Konfigurationsprüfung mit Öffnen der zu korrigierenden Stammdaten; Import/Export mit Excel;
  Duplizieren.
- SAP-Berechtigungen je Funktion; Texte in fünf Sprachen.

## 2. Konzepte: Basen, Werte, Varianten und Strukturen

Der Code eines Artikels besteht aus **Neutralcode** + **Suffix**:

- Der **Neutralcode** ist der sprechende Teil: die Verkettung der Codes der Ebene für Ebene gewählten
  **Werte**. Jede Ebene ist eine **Basis** (z. B. *Tipo mobile*, *Larghezza*) mit einer festen Länge und
  ihren Werten; jeder Wert führt zur nächsten **Unterebene** oder ist der letzte;
- Das **Suffix** ist eine laufende Nummer mit N Stellen (Einstellungen), die Artikel mit demselben
  Neutralcode und unterschiedlichen **Varianten** unterscheidet; bei 0 Stellen ist der Code gleich dem
  Neutralcode;
- Eine **Variante** (z. B. *Colore*) hat **Optionen** (z. B. weiß, Eiche). Die Varianten, die für einen
  Wert abgefragt werden, sind in einer **Variantenstruktur** zusammengefasst, die mit dem Wert verknüpft
  ist.

Im gesamten Handbuch wird dieses Beispiel verwendet. Es ist in der Datei
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx) enthalten, die Sie mit
*Excel-Import / -Export* importieren:

```
Tipo mobile cucina (CU, 2 Zeichen)            Struktur CUSC: Colore
├── BA Mobile base     → Larghezza
└── PE Mobile pensile  → Larghezza
Larghezza (CL, 3 Zeichen)                     Struktur CUSM: Colore anta + Maniglia, erbt Varianten
├── 060 Larghezza 60 cm
└── 090 Larghezza 90 cm
Colore (CUCOL)     BI Bianco · RO Rovere
Maniglia (CUMAN)   AL Maniglia alluminio · NE Maniglia nera
```

Der Hängeschrank mit 90 cm Breite und Aluminiumgriff hat den Neutralcode `PE090`; werden weiß und
Eiche zusammen generiert, wird bei einem 3-stelligen Suffix der weiße (BI kommt vor RO) zu `PE090001`
und der Eichenschrank zu `PE090002`.

Die **Zusammensetzung** (Werte jeder Ebene + gewählte Optionen) identifiziert den Artikel: Wird
dieselbe Zusammensetzung erneut generiert, findet das Add-on den vorhandenen Artikel, statt einen
weiteren anzulegen.

## 3. Einstellungen

![Einstellungen](../../_img/itemgenerator/02_configurazione.png)

*Das Fenster Einstellungen.*

| Option | Wirkung | Standard |
|---|---|---|
| Suffixstellen | laufende Nummer nach dem Neutralcode (0-10); 0 = Code gleich Neutralcode (nur ein Artikel je Neutralcode) | 0 |
| Beschreibungsformel | wie die Beschreibung zusammengesetzt wird (Kapitel 8); leer = Beschreibungen der Ebenen der Reihe nach | leer |
| Beschreibungen in Großbuchstaben | Beschreibung, erweiterte Beschreibung und Fremdname in Großbuchstaben | Nein |
| Preisliste | Preisliste, in die der Preis des Artikels geschrieben wird (Summe der Preise von Werten und Optionen), in Hauswährung | keine |
| Längeneinheit | Einheit der Maße (Länge, Breite, Höhe) von Werten und Artikeln; leer = Maße werden nicht übernommen | keine |
| Gewichtseinheit | Einheit des Gewichts von Werten und Optionen; leer = Gewicht wird nicht übernommen | keine |
| Stückliste | Typ der Stückliste, die mit den Komponenten angelegt wird: Keine, Produktion, Verkauf, Montage, Vorlage | Produktion |
| Menü nach Anlage | Menü, das für jeden angelegten Artikel aufgerufen wird (Integration mit anderen Add-ons, Kapitel 14) | leer |
| Bildvorschau | Bild des Artikels im Kopf der Artikelstammdaten (Kapitel 14) | Nein |
| Zur Liste hinzufügen leert zuerst die Liste | bei der Generierung ersetzt *Zur Liste hinzufügen* die Liste durch die letzte Auswahl; ohne die Option sammeln sich die Artikel an und werden mit *Liste leeren* entfernt (Kapitel 9) | Ja |
| Fensterdesign | Farben der Fenster des Add-ons (die Generierung), wie die beiden Designs des SAP-Clients: **SAP SQL** (dunkle Kopfzeile, goldene Schaltflächen) oder **SAP HANA** (blaue Kopfzeile, hellblaue Schaltflächen). Gilt für alle XEI-Add-ons der Firma; geöffnete Fenster ändern sich sofort | je nach Datenbank |

Die Optionen gelten für die gesamte Firma; ist die Generierung bereits geöffnet, verwendet sie die
Optionen beim nächsten Öffnen.

## 4. Varianten und Variantenstrukturen

### Varianten und Optionen definieren

Eine Variante hat einen Code, eine Beschreibung und ihre **Optionen** (Register *Optionen*). Im Kopf
können Sie, wie bei den Basen, eine **Benutzertabelle** und ein **Artikel-Benutzerfeld** angeben: Beim
Anlegen des Artikels wird die gewählte Option in die Tabelle aufgenommen (falls sie dort fehlt) und ihr
Code in das Benutzerfeld des Artikels geschrieben (Kapitel 6).

![Variante Colore mit den Optionen](../../_img/itemgenerator/03_varianti.png)

*Die Variante Colore mit den Optionen.*

| Spalte | Verwendung |
|---|---|
| Option, Beschreibung | Code und Beschreibung der Option; die Beschreibung ist der Text der Option in der Artikelbeschreibung |
| Fremdbeschr. | Text der Option im Fremdnamen (leer = der italienische Text) |
| Alias | freier Text |
| Preis | Beitrag zum Preis des Artikels |
| Gewicht | Beitrag zum Gewicht des Artikels |
| Eigenschaften | zu aktivierende Artikeleigenschaften: Zahlen von 1 bis 64, durch Komma getrennt (z. B. `2, 12`) |
| Aktiv | inaktive Optionen erscheinen nicht in der Generierung |

Im Register *Komponenten* geben Sie die Stücklistenkomponenten an, die die Optionen mitbringen
(Kapitel 7).

![Komponenten der Optionen](../../_img/itemgenerator/04_varianti_componenti.png)

*Komponenten der Optionen des Griffs: zwei Griffe aus Lager 01.*

### Variantenstrukturen

Eine Struktur fasst die Varianten zusammen, die für einen Wert einer Basis abgefragt werden, mit der
**Position** (Reihenfolge in der Generierung; alle verschieden) und der **Pos. Beschreibung**
(Reihenfolge der gewählten Option am Ende der Beschreibung; 0 = nicht am Ende). Die Beschreibung der
Zeile ersetzt, falls angegeben, die der Variante (z. B. „Colore anta“).

![Variantenstruktur](../../_img/itemgenerator/05_strutture.png)

*Die Struktur CUSM: Farbe der Tür und Griff.*

Eine Variante, die von einer Struktur verwendet wird, kann nicht gelöscht werden, ebenso wenig eine
Struktur, die von einer Basis verwendet wird.

## 5. Basen und Werte

Kopf der Basis: Code, Beschreibung, **Codelänge** (alle Werte haben diese Länge), Klassifizierung,
Benutzertabelle und Artikel-Benutzerfeld. Im Register *Werte* steht eine Zeile je Wert:

![Basis mit den Werten](../../_img/itemgenerator/06_basi_valori.png)

*Die Basis CU mit den Werten: Beschreibungen, Unterebene, Variantenstruktur.*

![Spalten der Werte](../../_img/itemgenerator/06b_basi_valori.png)

*Die weiteren Spalten: Daten für den Artikel (Gruppe, Eigenschaften, Preis, Maße, Gewicht).*

Es gibt viele Spalten: **Wenn Sie das Fenster maximieren**, wird die Tabelle breiter und alle Spalten
sind sichtbar.

| Spalte | Verwendung |
|---|---|
| Code, Beschreibung | Code des Werts (genau so lang wie in der Basis angegeben) und Beschreibung |
| Artikelbeschr. | Text des Werts in der Artikelbeschreibung |
| Fremdbeschr. | Text des Werts im Fremdnamen des Artikels (leer = der italienische Text) |
| Unterebene | Basis der nächsten Ebene (Auswahlliste; der Pfeil öffnet die Basis); leer = letzte Ebene |
| Variantenstruktur | Varianten, die für den Wert abgefragt werden (der Pfeil öffnet die Struktur) |
| Varianten erben | Varianten, die bereits auf einer vorherigen Ebene vorkommen, starten mit den dort gewählten Optionen als **Vorschlag**: Sie können beim Wert geändert werden (Kontextmenü in der Generierung, um zu den vorgeschlagenen zurückzukehren). Solange sie dem Vorschlag folgen, zählt die Option nur einmal |
| Vererbung erzwingen | mit Varianten erben: Es gilt die Auswahl der vorherigen Ebene, die beim Wert nicht geändert werden kann (die Variante erscheint nicht auf ihrer Ebene) |
| Aktiv | inaktive Werte erscheinen nicht in der Generierung |
| Lager-ME / Einkaufs-ME / Verkaufs-ME | Mengeneinheiten (als Text) des Artikels |
| Artikelgruppe, ME-Gruppe | Artikelgruppe und ME-Gruppe des Artikels |
| Eigenschaften | zu aktivierende Artikeleigenschaften (1-64) |
| Preis, Gewicht | Beiträge zu Preis und Gewicht des Artikels |
| Länge, Breite, Höhe | Maße des Artikels |

Wie diese Daten für den Artikel verwendet werden, erklärt Kapitel 6. Im Register *Komponenten* geben
Sie die Stücklistenkomponenten an, die die Werte mitbringen:

![Komponenten der Werte](../../_img/itemgenerator/07_basi_componenti.png)

*Der Hängeschrank bringt zwei Halterungen mit.*

- **Benutzertabelle** (eine Benutzertabelle ohne Objekt, zum Beispiel eine Farbtabelle): Beim Anlegen
  des Artikels wird der gewählte Wert (Code und Beschreibung) hinzugefügt, falls er fehlt.
- **Artikel-Benutzerfeld** (zum Beispiel ein Feld *Farbe* in den Artikelstammdaten): Beim Anlegen wird
  der Code des gewählten Werts hineingeschrieben.
- Basen der **ersten Ebene** sind die Basen, die bei keinem Wert Unterebene sind.

Beim Speichern prüft das Add-on Längen, doppelte Codes, eine Unterebene ungleich der Basis selbst,
Eigenschaften und Komponenten; der Grund eines Fehlers erscheint in der Statusleiste, und es wird nicht
gespeichert. Eine Basis, die von generierten Artikeln verwendet wird oder Unterebene einer anderen Basis
ist, kann nicht gelöscht werden.

> **Duplizieren** (bei Basen, Varianten und Strukturen): Bei geöffnetem Datensatz bereitet die Funktion
> einen neuen Datensatz mit denselben Daten und allen Zeilen vor; Sie geben den neuen Code ein und
> klicken auf *Hinzufügen*. Nützlich für ähnliche Basen (z. B. eine andere Maßreihe).

## 6. Daten des angelegten Artikels

Alle Daten des Artikels stammen aus den Werten der Zusammensetzung und den gewählten Optionen, nach zwei
Regeln:

- **Es gilt die letzte Ebene, die sie angibt**: Eine nachfolgende Ebene überschreibt die vorherigen
  Ebenen; ein leerer Wert oder null löscht den Wert einer vorherigen Ebene nicht;
- **Es wird summiert**: Alle Werte und gewählten Optionen tragen bei. Eine geerbte Option zählt nur
  einmal, auf der Ebene, auf der sie gewählt wurde, solange die erbende Ebene ihr folgt; eine eigene
  Auswahl auf dieser Ebene zählt auch dort (auch wenn es dieselbe Option ist).

| Artikeldaten | Aus | Regel |
|---|---|---|
| Code | Codes der Werte | Neutralcode + Suffix (max. 50 Zeichen) |
| Beschreibung, erweiterte Beschreibung | Artikelbeschr. der Werte, Beschreibungen der Optionen | Formel (Kapitel 8); die Beschreibung wird auf 200 Zeichen gekürzt, die erweiterte steht vollständig im Feld *Erweiterte Beschreibung* |
| Fremdname | Fremdbeschr. von Werten und Optionen | gleiche Formel; leer, wenn keiner eine Fremdbeschr. hat |
| Bemerkungen | Zusammensetzung | Baum mit den gewählten Werten und Optionen |
| Artikelgruppe | Werte | letzte Ebene; keine = die der Vorlage |
| ME-Gruppe | Werte | letzte Ebene; mit einer Gruppe werden die Text-ME nicht verwendet |
| Lager-ME / Einkaufs-ME / Verkaufs-ME | Werte | letzte Ebene, jede für sich |
| Eigenschaften | Werte und Optionen | werden summiert: alle werden aktiviert |
| Länge, Breite, Höhe | Werte | letzte Ebene, jede für sich; in Einkauf und Verkauf |
| Gewicht | Werte und Optionen | wird summiert; in Einkauf und Verkauf |
| Preis | Preis von Werten und Optionen | wird summiert; in der Preisliste der Einstellungen |
| Stückliste | Komponenten von Werten und Optionen | werden summiert (Kapitel 7) |

Beispiel: Hängeschrank mit 90 cm Breite in Eiche mit Aluminiumgriff (die Farbe wird auf Ebene 1 gewählt
und von 090 geerbt).

| Ebene | Auswahl | Preis | Gewicht | Maße | Gruppe | Eigenschaften |
|---|---|---|---|---|---|---|
| 1 Tipo | PE Pensile | 100 | 10 | Breite 350, Höhe 720 | 101 | 1, 3 |
| 1 Colore | RO Rovere | 30 | 1,5 | | | 2 |
| 2 Larghezza | 090 L90 | 40 | 3 | Länge 900 | | 5 |
| 2 Maniglia | AL Alluminio | 5 | 0,2 | | | |
| **Artikel PE090002** | | **175** | **14,7** | **900 × 350 × 720** | **101** | **1, 2, 3, 5** |

Alles andere (Konten, Planungsdaten, Lieferant, Lager...) stammt aus dem in der Generierung gewählten
**Vorlageartikel**: Die neuen Artikel übernehmen dessen Daten, ohne Lagerbestände, Preise, Barcodes,
Stückliste, letzte Preise und Fremdname.

![Der angelegte Artikel](../../_img/itemgenerator/12_articolo.png)

*Der angelegte Artikel: Beschreibung, Fremdname, Gruppe, Preis in der Preisliste.*

![Eigenschaften](../../_img/itemgenerator/13_articolo_proprieta.png)

*Von Werten und Optionen aktivierte Eigenschaften.*

![Maße und Gewicht](../../_img/itemgenerator/14_articolo_misure.png)

*Maße und Gewicht in den Verkaufsdaten.*

## 7. Stückliste

Jeder Wert einer Basis und jede Option einer Variante kann **Komponenten** haben (Register *Komponenten*
der beiden Stammdatenfenster): den Komponentenartikel, die **Menge pro Einheit** des generierten
Artikels und optional das **Lager** für die Entnahme (leer = das Standardlager der Komponente). Beim
Anlegen erstellt das Add-on die Stückliste des Artikels mit den Komponenten der gesamten
Zusammensetzung:

1. für jede Ebene, von der ersten bis zur letzten, die Komponenten des gewählten Werts und danach die
   der gewählten Optionen;
2. **geerbte** Optionen bringen ihre Komponenten nicht erneut mit;
3. **derselbe Artikel mit demselben Lager** wird zu einer einzigen Zeile mit summierten Mengen;
4. die Stückliste hat die Menge 1 und den **Typ** aus den Einstellungen (Produktion, Verkauf, Montage,
   Vorlage); bei *Keine* oder wenn die Zusammensetzung keine Komponenten hat, wird keine Stückliste
   angelegt;
5. Artikel und Stückliste werden gemeinsam gespeichert: Kann die Stückliste nicht angelegt werden, bleibt
   auch der Artikel nicht bestehen, und der Grund steht in der Spalte *Ergebnis* der Generierung.

> SAP akzeptiert jeden Stücklistentyp nur bei passenden Artikeln (zum Beispiel die Produktionsstückliste
> bei einem Lagerartikel, Verkaufs- und Montagestücklisten bei einem Verkaufsartikel, der kein
> Lagerartikel ist): Der Vorlageartikel muss die richtigen Eigenschaften für den in den Einstellungen
> gewählten Typ haben.

Im Beispiel bringt der Hängeschrank 2 Halterungen mit, die Option Eiche 1 Tür, der Aluminiumgriff 2 Griffe
aus Lager 01. Der Hängeschrank mit 90 cm Breite in Eiche mit Aluminiumgriff hat diese Stückliste:

![Stückliste](../../_img/itemgenerator/15_distinta.png)

*Die mit dem Artikel angelegte Stückliste.*

In der Generierung zeigt die Spalte *Komponenten* der Liste, wie viele Zeilen die Stückliste haben wird;
nach dem Anlegen meldet das Ergebnis „Mit Stückliste (n Komponenten)“. Die Konfigurationsprüfung meldet
nicht vorhandene Komponenten, Komponenten mit Menge null oder mit nicht vorhandenen Lagern.

## 8. Beschreibungsformel

Die Formel (Einstellungen) bestimmt, wie Beschreibung, erweiterte Beschreibung und Fremdname
zusammengesetzt werden.

| Platzhalter | Wird zu |
|---|---|
| `{1}`, `{2}`... | die *Artikelbeschr.* des auf Ebene 1, 2... gewählten Werts |
| `{C:1}`, `{N:1}` | Code und Beschreibung des auf Ebene 1 gewählten Werts |
| `{V:CUCOL}` | die Beschreibung der für die Variante `CUCOL` gewählten Option |
| `{VC:CUCOL}` | der Code der für die Variante `CUCOL` gewählten Option |
| `{NEUTRO}` | der Neutralcode |
| `[ ... ]` | optionaler Teil: erscheint nur, wenn alle enthaltenen Platzhalter einen Wert haben |

- **Leere Formel**: die Artikelbeschr. der Ebenen der Reihe nach.
- **Am Ende** stehen die Beschreibungen der Optionen mit einer Pos. Beschreibung größer als null, in
  dieser Reihenfolge, sofern die Formel ihre Variante nicht bereits mit `{V:...}` oder `{VC:...}`
  verwendet.
- Ein Platzhalter ohne Wert wird leer; innerhalb von `[ ]` entfernt er den gesamten Teil, einschließlich
  der Trennzeichen.
- Doppelte Leerzeichen werden entfernt; mit *Beschreibungen in Großbuchstaben* steht alles in
  Großbuchstaben; Groß- und Kleinschreibung spielt bei den Platzhaltern keine Rolle.
- **Fremdname**: dieselbe Formel mit den Fremdbeschreibungen (wo sie fehlen, die italienischen); leer,
  wenn kein Wert und keine Option eine Fremdbeschr. hat.
- Ein unbekannter Platzhalter bleibt im Text stehen, damit er sichtbar ist; die Konfigurationsprüfung
  meldet ihn, ebenso nicht geschlossene oder verschachtelte eckige Klammern.

Beispiele mit dem Hängeschrank mit 60 cm Breite in Eiche mit Aluminiumgriff:

| Formel | Beschreibung |
|---|---|
| *(leer)* | `Pensile L60 Rovere Maniglia alluminio` |
| `{1} {V:CUCOL} {2}` | `Pensile Rovere L60 Maniglia alluminio` |
| `{N:1} {C:2} - {NEUTRO}` | `Mobile pensile 060 - PE060 Rovere Maniglia alluminio` |
| `{1} {2}[ con {V:CUMAN}]` | `Pensile L60 con Maniglia alluminio Rovere`; ohne Griff: `Pensile L60 Rovere` |
| *(leer)*, Großbuchstaben | `PENSILE L60 ROVERE MANIGLIA ALLUMINIO` |
| *(leer)*, Fremdname | `Wall unit L60 Oak Maniglia alluminio` |

## 9. Artikel generieren

Die Generierung ist ein **eigenes Fenster über SAP**: Es lässt sich wie jedes Windows-Fenster
maximieren, minimieren und in der Größe ändern (die Bereiche passen sich an; die Trennlinien zwischen den
Bereichen lassen sich ziehen). Position, Größe, Trennlinien und Spaltenbreiten werden je Benutzer
gespeichert; beim ersten Mal öffnet sich das Fenster im Vollbild. Solange es geöffnet ist, bleibt SAP
bedienbar, auch während die Artikel angelegt werden. Die Farben folgen dem **Fensterdesign** der
Einstellungen (Kapitel 3): In der Kopfzeile steht das Codeformat, darunter ein Bereich, der angibt, von wo
aus die Generierung geöffnet wurde (Zeile eines Belegs, ähnlicher Artikel) oder was nicht stimmt.

Lange Vorgänge (viele Ebenen öffnen, suchen, einen ganzen Zweig markieren, viele Artikel hinzufügen oder
anlegen) **zeigen am unteren Fensterrand, was sie gerade tun** (Meldung mit dem Fortschritt, Balken) und
werden mit *Abbrechen* gestoppt; währenddessen sind die Befehle gesperrt und das Fenster bleibt aktiv.
Die Ergebnisse stehen unten, mit einem Symbol (grün, orange, rot). Ein unerwarteter Fehler wird in einer
Meldung angezeigt, und das Fenster bleibt bedienbar.

![Generierung mit Varianten](../../_img/itemgenerator/09_genera_varianti.png)

*Breiten 060 und 090 von Unter- und Hängeschrank markiert (in zwei Zweigen), Farbe weiß und Eiche, Griff
Aluminium und schwarz: 16 zu bildende Artikel.*

1. **Vorlageartikel** (oben, optional, bleibt von Sitzung zu Sitzung gespeichert): Die neuen Artikel
   übernehmen dessen Daten (Kapitel 6). Die Schaltfläche *...* (oder F2) sucht den Artikel nach Code oder
   Beschreibung; neben dem Code steht die Beschreibung oder *Artikel nicht in den Artikelstammdaten
   gefunden*. Ohne Vorlage werden die Artikel nur mit den Daten der Konfiguration angelegt.
2. **Codebaum** (links): die Basen der ersten Ebene mit ihren Werten; das Zeichen **+** öffnet die
   Unterebene eines Werts. Blau dargestellt sind die Werte mit Varianten; wenn Sie mit der Maus über einen
   Wert fahren, sehen Sie Artikelbeschreibung, Varianten und Unterebene. Sie **markieren die Werte der
   letzten Ebene** (die einzigen mit Kontrollkästchen), auch mehrere und **auch in verschiedenen
   Zweigen**: Neben den Zweigen steht, wie viele Werte darunter markiert sind (*✓ 2*), und unter dem Baum
   stehen ihre Neutralcodes.
   - **Suchen**: Ein vollständiger Neutralcode (z. B. `PE090`) führt direkt zu seinem Wert; sonst führt
     die Suche zum nächsten Wert, der den Text im Code oder in der Beschreibung enthält (Eingabe für den
     nächsten, Strg+F zurück zur Suche). Die Suche gilt auch für noch nicht geöffnete Ebenen.
   - **Alle aufklappen**, **Zuklappen**, **Alle abwählen**; **Neutralcode** zeigt den Neutralcode neben
     jedem Wert.
   - Rechtsklick auf einen Zweig: *Werte der letzten Ebene darunter auswählen*, *Darunter abwählen*,
     *Darunter aufklappen*. Doppelklick oder Leertaste auf einen Wert der letzten Ebene: markiert ihn oder
     hebt die Markierung auf.
3. **Varianten und Optionen** (rechts): die **Struktur des im Baum ausgewählten Werts** (Klick oder
   Pfeiltasten), mit ihren Varianten in der Reihenfolge der Struktur, den zu markierenden Optionen und
   ihrem Beitrag zum Preis; der Titel nennt den betreffenden Wert. Eine geerbte Variante zeigt dies neben
   dem Namen an: *von Ebene 1, Tipo vorgeschlagen: änderbar* (folgt der Auswahl darüber), *eigene Wahl,
   anders als Ebene 1* (über das Kontextmenü *Zurück zu den vorgeschlagenen Optionen*), *wie Ebene 1:
   erzwungene Vererbung* (Kapitel 5). Dieselbe Variante auf derselben Ebene wird für alle markierten
   Werte **nur einmal** gewählt. Das Kontrollkästchen *Alle Varianten der markierten Werte, nach Ebene*
   zeigt dagegen alle Varianten der markierten Werte nach Ebene gruppiert, mit *nur für 060*, wenn eine
   Variante nur einige Werte betrifft. Mehrere Optionen derselben Variante ergeben mehrere Artikel; eine
   Variante ohne markierte Optionen geht nicht in die Zusammensetzung ein. Kontextmenü: *Alle Optionen
   auswählen* / *Alle Optionen abwählen*. Darunter steht, wie viele Artikel zusammengestellt werden.
4. **Zur Liste hinzufügen**: stellt alle Kombinationen in der Liste unten zusammen, mit Code,
   Beschreibung, Preis, Anzahl der Stücklistenkomponenten und Status. Standardmäßig (Option *Zur Liste
   hinzufügen leert zuerst die Liste*, Kapitel 3) wird die Liste geleert und enthält nur die letzte
   Auswahl; bei deaktivierter Option sammeln sich die Artikel an, und Artikel, die bereits in der Liste
   stehen, werden nicht wiederholt. Die Markierungen von Werten und Optionen bleiben erhalten (sie werden
   mit *Alle abwählen* entfernt): Sie ändern eine Option oder einen Wert und fügen erneut hinzu.
5. **Artikel generieren (n)**: legt die markierten Artikel der Liste an (n auf der Schaltfläche), einen
   nach dem anderen, mit dem Ergebnis Zeile für Zeile und dem Fortschrittsbalken. *Abbrechen* stoppt das
   Anlegen nach dem aktuellen Artikel. Am Ende steht unten im Fenster die Zusammenfassung: *Angelegte
   Artikel: n.*, danach, nur falls vorhanden, die Artikel, die inzwischen ein anderer Benutzer angelegt
   hat, und die Artikel mit Fehlern; die Liste springt auf den ersten angelegten Artikel.

![Liste der zusammengestellten Artikel](../../_img/itemgenerator/08_genera.png)

*Die 16 zusammengestellten Artikel (das Ende der Liste): 15 bereits in den Artikelstammdaten (gelb) und
einer anzulegen, PE060004, mit Preis und Anzahl der Komponenten.*

| Status | Bedeutung |
|---|---|
| Anzulegen | Code = Neutralcode + erstes freies Suffix (weder in den Artikelstammdaten noch bereits in der Liste) |
| Bereits vorhanden | dieselbe Zusammensetzung ist bereits in den Artikelstammdaten: der Code ist der des vorhandenen Artikels (gelb) |
| Angelegt | Artikel angelegt (grün); das Ergebnis gibt an, ob er eine Stückliste hat |
| Fehler | der Grund steht in der Spalte *Ergebnis* (rot): Code bereits verwendet, keine Suffixe mehr frei, Code zu lang, Fehler von SAP. Sie können korrigieren und erneut generieren |

![Ergebnis der Generierung](../../_img/itemgenerator/11_genera_esito.png)

*Ergebnis der Generierung: die Unterschränke mit 60 und 90 cm Breite in weiß angelegt (grün) und die
Zusammenfassung unten; ohne Komponenten haben sie keine Stückliste (mit Komponenten meldet das Ergebnis
„Mit Stückliste“).*

In der Liste entscheidet das Kontrollkästchen (nur bei anzulegenden oder fehlerhaften Artikeln), welche
Artikel angelegt werden. Ein **Doppelklick** (oder Eingabe) auf einen angelegten oder bereits vorhandenen
Artikel öffnet ihn in den Artikelstammdaten von SAP (die Generierung wird minimiert und über die
Taskleiste wieder geöffnet). Ein noch anzulegender Artikel öffnet nichts: Unten im Fenster steht *Artikel
... ist noch nicht in den Artikelstammdaten*; ebenso, wenn der Artikel inzwischen in SAP gelöscht wurde.
Kontextmenü: *In Artikelstammdaten öffnen*, *Code kopieren*, *Aus der Liste entfernen*, *Alle
auswählen*, *Alle abwählen*; Entf entfernt die ausgewählten Zeilen, Strg+C kopiert ihre Codes. *Liste
leeren* beginnt von vorn. Enthält die Liste noch nicht angelegte Artikel, fragt das Schließen oder
Leeren nach einer Bestätigung.

### Meldungen und Texte des Fensters

Fragen und Meldungen der Generierung (zum Beispiel *2 Artikel in den Artikelstammdaten anlegen?*) haben
das gleiche Aussehen wie das Fenster: Eingabe wählt die hervorgehobene Schaltfläche, Esc antwortet mit
Nein. Wer die Berechtigung **Modifica testi add-on XEI** (Texte der XEI-Add-ons bearbeiten) hat, kann die Texte des Fensters wie in
den SAP-Fenstern ändern: Rechtsklick auf eine Beschriftung, eine Schaltfläche, den Titel eines Bereichs,
die Überschrift einer Spalte oder den Text einer Meldung, dann **Modifica testo...** (Text bearbeiten); **Testi di
questa finestra...** (Texte dieses Fensters) (auch am Ende der Kontextmenüs der Bäume und der Liste) listet alle auf. Der angepasste
Text gilt für alle Benutzer in der verwendeten Sprache und ist sofort sichtbar.

![Frage vor dem Anlegen](../../_img/itemgenerator/25_messaggio.png)

*Die Frage vor dem Anlegen, im Stil des Fensters.*

![Modifica testo](../../_img/itemgenerator/26_modifica_testo.png)

*Modifica testo (Text bearbeiten) über das Kontextmenü der Schaltfläche Suchen: Ausgangstext und angepasster Text.*

Vor dem Anlegen jedes Artikels prüft das Add-on erneut, dass inzwischen niemand dieselbe Zusammensetzung
angelegt oder den Code verwendet hat. Jeder Artikel wird in einem einzigen Vorgang angelegt (Artikel,
Stückliste, Benutzertabellen, Zusammensetzung): Ein Fehler hinterlässt keine halben Daten.

## 10. Artikel aus Angeboten und Kundenaufträgen

In **Angeboten** und **Kundenaufträgen** klicken Sie mit der rechten Maustaste auf eine Zeile ›
**Artikel konfigurieren...**:

![Artikel konfigurieren aus der Zeile](../../_img/itemgenerator/17_ordine_menu.png)

*Artikel konfigurieren aus der Zeile des Auftrags.*

Die Generierung öffnet sich für diese Zeile (das zeigen der Fenstertitel und der Bereich oben). Sie
stellen den Artikel wie gewohnt zusammen und legen ihn an; danach übernimmt **In Zeile übernehmen** den
in der Liste ausgewählten Artikel (angelegt oder bereits vorhanden; enthält die Liste nur einen, müssen
Sie ihn nicht auswählen) in die Belegzeile, schließt die Generierung und holt den Beleg wieder in den
Vordergrund. SAP füllt die Zeile so, als wäre der Code von Hand eingegeben worden: Beschreibung, Preis
aus der Preisliste des Kunden, Lager.

![Aus der Zeile geöffnete Generierung](../../_img/itemgenerator/18_genera_documento.png)

*Aus Zeile 2 des Auftrags geöffnete Generierung: der soeben angelegte Artikel ausgewählt und „In Zeile
übernehmen“.*

![Artikel in der Zeile](../../_img/itemgenerator/19_ordine_riga.png)

*Der Artikel in der Zeile des Auftrags.*

- Enthält die Zeile bereits einen vom Konfigurator generierten Artikel, startet die Generierung mit
  dessen Konfiguration: Sie ändern nur eine Option, um die richtige Variante zu erhalten.
- Ist die Generierung bereits geöffnet, wechselt sie zur neuen Zeile; die Liste bleibt erhalten, sodass
  Sie einen zuvor zusammengestellten Artikel wiederverwenden können.
- Der Beleg muss geöffnet bleiben; ein geschlossener oder nicht änderbarer Beleg wird nicht geändert (der
  Grund erscheint unten im Fenster).

## 11. Ähnliche Artikel

In den Artikelstammdaten eines vom Konfigurator angelegten Artikels klicken Sie mit der rechten Maustaste
› **Ähnliche Artikel generieren...**: Die Generierung öffnet sich mit der bereits eingestellten
Konfiguration des Artikels (sein Endwert im Baum markiert, der Baum bis dorthin aufgeklappt, und die
gewählten Optionen) und mit dem Artikel selbst als Vorlage. Sie ändern Werte und Optionen und fügen die
Artikel der Liste hinzu. Ist die Generierung bereits geöffnet (auch minimiert), kommt sie mit der
Konfiguration des Artikels in den Vordergrund; die Liste bleibt erhalten.

![Rechtsklick auf einen generierten Artikel](../../_img/itemgenerator/16_simili_menu.png)

*Das Kontextmenü eines generierten Artikels.*

![Generierung ähnlicher Artikel](../../_img/itemgenerator/20_simili.png)

*Generierung aus der Konfiguration von PE090002 (Design SAP HANA): Hängeschrank 90, Eiche und
Aluminiumgriff bereits markiert; Vorlage ist der Artikel selbst.*

Hat sich die Konfiguration inzwischen geändert (Werte entfernt oder deaktiviert, andere Unterebenen),
startet die Generierung leer, mit einem Hinweis; Optionen, die nicht mehr existieren, werden ignoriert.

## 12. Konfigurationsprüfung

Prüft die gesamte Konfiguration (auch inaktive Werte und Optionen) und zeigt die Probleme an, zuerst die
Fehler, dann die Warnungen. Ein **Doppelklick** auf eine Zeile öffnet die zu korrigierenden Stammdaten
auf dem betreffenden Datensatz; *Erneut prüfen* wiederholt die Prüfung nach den Korrekturen. Wenn Sie das
Fenster vergrößern (auch auf Vollbild), passt sich die Problemliste an.

![Konfigurationsprüfung](../../_img/itemgenerator/21_verifica.png)

*Prüfung: eine Variantenstruktur, die nicht existiert, und ein Wert, der erbt, ohne dass es Varianten zu
erben gibt.*

| Typ | Prüfung |
|---|---|
| Fehler | Basis ohne Codelänge; Code mit anderer Länge als die Basis; doppelter Code |
| Fehler | Unterebene, Variantenstruktur, Artikelgruppe, ME-Gruppe nicht vorhanden; ungültige Eigenschaften |
| Fehler | nicht vorhandene Variante in einer Struktur; doppelte Option |
| Fehler | Komponente ohne Artikel, mit nicht vorhandenem Artikel oder Lager, mit Menge null, für einen Wert oder eine Option, die es nicht gibt |
| Fehler | Basis als Unterebene ihrer selbst (Zyklus, mit dem Pfad); keine Basis der ersten Ebene |
| Warnung | Basis ohne aktive Werte; Struktur ohne Varianten; Variante ohne aktive Optionen |
| Warnung | Basis, die von der ersten Ebene aus nicht erreichbar ist (nur Unterebene inaktiver Werte) |
| Warnung | Pfad, der Codes mit mehr als 50 Zeichen ergibt, einschließlich Suffix |
| Warnung | Wert, der die Varianten erbt, ohne gleiche Varianten auf den vorherigen Ebenen; Vererbung erzwingen ohne Varianten erben |
| Warnung | Formel mit unbekannten Platzhaltern oder fehlerhaften eckigen Klammern |

## 13. Import und Export mit Excel

![Import aus Excel](../../_img/itemgenerator/22_excel.png)

*Erfolgreicher Import der Beispieldatei.*

**Exportieren...** fragt nach dem Speicherort und schreibt die gesamte Konfiguration in eine
.xlsx-Datei, ein Blatt je Stammdatenart, mit fett gedruckter und fixierter Kopfzeile. **Importieren**
liest die angegebene Datei (*Durchsuchen...*). Wenn Sie das Fenster vergrößern, werden der Dateiname und
die Ergebnisliste breiter.

| Blatt | Eine Zeile je | Spalten |
|---|---|---|
| Basi | Wert (die Daten der Basis wiederholen sich) | Base, Descrizione base, Lunghezza, Classificazione, Tabella utente, Campo utente, Codice, Descrizione, Desc. articolo, Desc. straniera, Sotto livello, Struttura varianti, Eredita varianti, Forza ereditarietà, Attivo, UM magazzino, UM acquisti, UM vendite, Valore, Dim. 1, Dim. 2, Dim. 3, Peso, Gruppo articoli, Gruppo UM, Proprietà, Note |
| Componenti basi | Komponente | Base, Valore, Componente, Descrizione, Quantità, Magazzino, Note |
| Varianti | Option | Variante, Descrizione variante, Tabella utente, Campo utente, Opzione, Descrizione, Desc. straniera, Alias, Valore, Peso, Proprietà, Note, Attivo |
| Componenti varianti | Komponente | Variante, Opzione, Componente, Descrizione, Quantità, Magazzino, Note |
| Strutture | Variante | Struttura, Descrizione struttura, Variante, Descrizione variante, Posizione, Pos. descrizione |

- Die Spalten werden am **Titel** erkannt: Die Reihenfolge spielt keine Rolle, und unbekannte Spalten
  werden ignoriert. Die Datei kann auch nur einige Blätter enthalten.
- Zahlen im italienischen Format (`1.234,5`) oder im englischen Format (`1234.5`); Ja/Nein mit Y, S,
  Sì, X, 1, Vero.
- Codes mit führenden Nullen (`060`) müssen als Text geschrieben werden (in Excel mit Apostroph:
  `'060`), sonst wandelt Excel sie in Zahlen um.
- Der Import **prüft zuerst die gesamte Datei**: Bei einem Fehler schreibt er nichts, und die Liste zeigt
  Blatt, Zeile und Grund jedes Fehlers.
- Danach schreibt er alles gemeinsam: Jede Basis, Variante oder Struktur der Datei wird hinzugefügt oder
  aktualisiert, und ihre Zeilen **ersetzen** die vorhandenen; die Komponenten ändern sich nur für die
  Basen und Varianten, die in den Komponentenblättern enthalten sind; was nicht in der Datei steht, bleibt
  unverändert.

Typische Verwendungen: exportieren, in Excel bearbeiten (neue Werte, geänderte Preise) und wieder
importieren; die Konfiguration in eine andere Firma kopieren; mit einem Beispiel wie
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx) beginnen.

## 14. Artikelstammdaten, Konsistenzprüfung, andere Add-ons

### Bildvorschau

Mit der Option *Bildvorschau* zeigen die Artikelstammdaten das Bild des Artikels (Feld Bild, im
Bilderordner von SAP) im freien Bereich des Kopfs an, links neben den Kontrollkästchen Lagerartikel/
Verkaufsartikel/Einkaufsartikel. Der Rahmen übernimmt die Proportionen des Bilds und wird ausgeblendet,
wenn der Artikel kein Bild hat. Die Artikelstammdaten werden dadurch nicht langsamer.

![Bildvorschau in den Artikelstammdaten](../../_img/itemgenerator/24_miniatura.png)

*Die Bildvorschau in den Artikelstammdaten.*

### Konsistenzprüfung

Berechnet die Zusammensetzung aller generierten Artikel neu. Sie wird benötigt, wenn die Daten der
Konfiguration außerhalb des Add-ons geändert wurden; außerdem entfernt sie die Zusammensetzungen der in
SAP gelöschten Artikel.

### Integration mit anderen Add-ons

Ist in den Einstellungen ein *Menü nach Anlage* angegeben, ruft das Add-on für jeden angelegten Artikel
dieses Menü auf, nachdem es den Code in der XEI-Tabelle `@XEI_IG_EVENTS` erfasst hat: Ein anderes
Add-on, das auf dieses Menü reagiert, kann den Artikel vervollständigen.
