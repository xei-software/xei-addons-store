"""Manuali degli add-on: più documenti per add-on, immagini, file di esempio e PDF, con i link riscritti per il sito.

Si usa una copia di site/ con manuali di prova, perché quelli veri arrivano solo quando sono approvati.
"""
import shutil

import pytest

import build

ID = "item-generator"


def _manuale(titolo, corpo, stato="approvato"):
    return f"---\ntitle: {titolo}\nlang: it\nstato: {stato}\n---\n\n# {titolo}\n\n{corpo}\n"


@pytest.fixture()
def sito_con_manuali(tmp_path, monkeypatch):
    sorgente = tmp_path / "site"
    shutil.copytree(build.CARTELLA_SITO, sorgente)
    cartella = sorgente / "content" / "it" / "manuali" / ID
    cartella.mkdir(parents=True, exist_ok=True)
    (cartella / "manuale-utente.md").write_text(_manuale(
        "Manuale utente",
        "Prima leggi [l'installazione](installazione.md).\n\n"
        "![Finestra](../../_img/itemgenerator/finestra.png)\n\n"
        "Scarica [l'esempio](../../_file/itemgenerator/esempio.xlsx)."), encoding="utf-8")
    (cartella / "manuale-utente.pdf").write_bytes(b"%PDF-1.4 prova")
    (cartella / "installazione.md").write_text(_manuale("Installazione", "Usa l'Extension Manager."),
                                               encoding="utf-8")
    (cartella / "bozza.md").write_text(_manuale("Bozza", "Non pubblicare.", stato="bozza"), encoding="utf-8")
    for sotto, nome in (("_img", "finestra.png"), ("_file", "esempio.xlsx")):
        risorsa = sorgente / "content" / sotto / "itemgenerator"
        risorsa.mkdir(parents=True, exist_ok=True)
        (risorsa / nome).write_bytes(b"dati")
    monkeypatch.setattr(build, "CARTELLA_SITO", sorgente)
    uscita = tmp_path / "uscita"
    build.genera_sito(uscita, url_base="")
    return uscita


def test_ogni_manuale_approvato_ha_la_sua_pagina_in_ogni_lingua(sito_con_manuali):
    for lingua in build.carica_config()["lingue"]:
        for nome in ("manuale-utente", "installazione"):
            assert (sito_con_manuali / lingua / "manuali" / ID / f"{nome}.html").exists()
        assert not (sito_con_manuali / lingua / "manuali" / ID / "bozza.html").exists()


def test_i_link_del_manuale_puntano_alle_risorse_del_sito(sito_con_manuali):
    testo = (sito_con_manuali / "it" / "manuali" / ID / "manuale-utente.html").read_text(encoding="utf-8")
    assert 'href="/it/manuali/item-generator/installazione.html"' in testo
    assert 'src="/static/manuali/_img/itemgenerator/finestra.png"' in testo
    assert 'href="/static/manuali/_file/itemgenerator/esempio.xlsx"' in testo
    assert (sito_con_manuali / "static" / "manuali" / "_img" / "itemgenerator" / "finestra.png").exists()
    assert (sito_con_manuali / "static" / "manuali" / "_file" / "itemgenerator" / "esempio.xlsx").exists()


def test_il_pdf_accanto_al_manuale_si_scarica(sito_con_manuali):
    assert (sito_con_manuali / "it" / "manuali" / ID / "manuale-utente.pdf").exists()
    testo = (sito_con_manuali / "it" / "manuali" / ID / "manuale-utente.html").read_text(encoding="utf-8")
    assert 'href="/it/manuali/item-generator/manuale-utente.pdf"' in testo


def test_l_elenco_dei_manuali_mostra_i_titoli(sito_con_manuali):
    testo = (sito_con_manuali / "it" / "manuali.html").read_text(encoding="utf-8")
    assert "Manuale utente" in testo and "Installazione" in testo
    assert testo.index("Manuale utente") < testo.index("Installazione")


def test_i_link_della_scheda_ai_manuali_portano_alle_pagine_del_sito():
    # La scheda della documentazione collega il manuale con il percorso del repository della documentazione.
    html = '<a href="../../manuali/de/commissionmanagement/manuale-utente.md">Handbuch</a>'
    assert build.riscrivi_link_scheda(html, "commission-management", "de", "") == \
        '<a href="/de/manuali/commission-management/manuale-utente.html">Handbuch</a>'
