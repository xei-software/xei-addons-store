"""Condizioni di download e licenza d'uso: la spunta degli artt. 1341 e 1342 c.c. deve citare articoli che esistono
davvero nel testo pubblicato, uguali in tutte le lingue; la prima spunta ricorda prova in ambiente di test e backup."""
import re
from pathlib import Path

import build

FILE_CONDIZIONI = build.CARTELLA_SITO / "content" / "it" / "pagine" / "condizioni.md"
ARTICOLI_CODICE_CIVILE = {"1341", "1342"}


def articoli_citati(testo_spunta):
    """Numeri degli articoli citati nella spunta (es. "3", "4.6"), senza gli artt. 1341 e 1342 del Codice civile."""
    numeri = re.findall(r"\b\d{1,2}(?:\.\d{1,2})?\b|\b\d{4}\b", testo_spunta)
    return {numero for numero in numeri if numero not in ARTICOLI_CODICE_CIVILE}


def articoli_del_testo(percorso):
    """Articoli («## Art. 3 – …») e commi («4.6 …» a inizio riga) presenti nel testo delle condizioni."""
    testo = Path(percorso).read_text(encoding="utf-8")
    articoli = set(re.findall(r"^## Art\. (\d{1,2})\b", testo, re.MULTILINE))
    commi = set(re.findall(r"^(\d{1,2}\.\d{1,2}) ", testo, re.MULTILINE))
    return articoli | commi


def test_articoli_citati_trova_articoli_e_commi_ma_non_il_codice_civile():
    spunta = "Ai sensi degli articoli 1341 e 1342 approvo gli articoli 3 (licenza), 4.6 (revoca) e 7.5 (foro)."
    assert articoli_citati(spunta) == {"3", "4.6", "7.5"}


def test_la_spunta_cita_solo_articoli_che_esistono_nel_testo():
    citati = articoli_citati(build.carica_testi("it")["condizioni_approvo"])
    assert citati, "la spunta non cita nessun articolo"
    if FILE_CONDIZIONI.exists():
        mancanti = citati - articoli_del_testo(FILE_CONDIZIONI)
        assert not mancanti, f"articoli citati nella spunta ma assenti dal testo: {sorted(mancanti)}"


def test_tutte_le_lingue_citano_gli_stessi_articoli():
    lingue = build.carica_config()["lingue"]
    attesi = articoli_citati(build.carica_testi("it")["condizioni_approvo"])
    for lingua in lingue:
        assert articoli_citati(build.carica_testi(lingua)["condizioni_approvo"]) == attesi, lingua


def test_le_clausole_da_approvare_sono_quelle_delle_condizioni_xei():
    # licenza e limiti, revoca, test e backup, esclusione di garanzia e responsabilità, risoluzione, foro
    citati = articoli_citati(build.carica_testi("it")["condizioni_approvo"])
    assert citati == {"3", "4.6", "5", "6", "7.1", "7.5"}


def test_la_prima_spunta_ricorda_ambiente_di_test_e_backup():
    testo = build.carica_testi("it")["condizioni_accetto"].lower()
    assert "ambiente di test" in testo and "backup" in testo


def test_il_testo_delle_condizioni_contiene_proprieta_test_e_backup():
    assert FILE_CONDIZIONI.exists()
    testo = FILE_CONDIZIONI.read_text(encoding="utf-8")
    for titolo in ("## Art. 4 – Proprietà del software e proprietà intellettuale",
                   "## Art. 5 – Obblighi del Cliente: test e backup",
                   "## Art. 6 – Esclusione di garanzia e limitazione di responsabilità"):
        assert titolo in testo, titolo
    # La spunta è nella finestra del sito: il testo non ripete le caselle da spuntare.
    assert "- [ ]" not in testo
