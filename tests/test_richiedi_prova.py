"""Pagina richiedi-prova.html: la apre il pulsante «Richiedi una prova» del menu Licenza (XEICore 1.3.0) con prodotto
e codice della società; manda al modulo di prova precompilato."""
import html
import json
import shutil
import subprocess

import pytest

import build

SCRIPT = build.CARTELLA_SITO / "static" / "js" / "richiedi-prova.js"
MODELLO = "https://forms.example/r?id=X&rA=%22{addon}%22&rL=%22Italiano%22&rC=%22{codice}%22"
AMMESSI = ["XEI.ItemGenerator", "XEI.CommissionManagement"]


def _indirizzo(ricerca, modello=MODELLO, ammessi=AMMESSI):
    if not shutil.which("node"):
        pytest.skip("node non installato")
    codice = (f"const r = require({json.dumps(str(SCRIPT))});"
              f"console.log(JSON.stringify(r.indirizzoModulo({json.dumps(modello)}, {json.dumps(ricerca)}, {json.dumps(ammessi)})));")
    uscita = subprocess.run(["node", "-e", codice], capture_output=True, text=True, check=True).stdout
    return json.loads(uscita)


def test_prodotto_e_codice_della_societa_vanno_nel_modulo():
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=7K3F-9QPA-2MXB") == \
        "https://forms.example/r?id=X&rA=%22XEI.ItemGenerator%22&rL=%22Italiano%22&rC=%227K3F-9QPA-2MXB%22"


def test_il_codice_si_accetta_maiuscolo_e_senza_spazi():
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=%207k3f-9qpa-2mxb%20").endswith("rC=%227K3F-9QPA-2MXB%22")


def test_senza_parametri_o_con_valori_non_ammessi_non_si_va_al_modulo():
    assert _indirizzo("") is None
    assert _indirizzo("?prodotto=XEI.ItemGenerator") is None
    assert _indirizzo("?codice=7K3F-9QPA-2MXB") is None
    assert _indirizzo("?prodotto=XEI.Altro&codice=7K3F-9QPA-2MXB") is None
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=7K3F9QPA2MXB") is None      # senza trattini
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=7K3F-9QPA-2MXI") is None    # I non è Base32 di Crockford
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=%22%3E%3Cscript%3E") is None


def test_la_pagina_esiste_in_ogni_lingua_con_il_modulo_della_sua_lingua(tmp_path):
    config = {**build.carica_config(), "modulo_registrazione": MODELLO.replace("Italiano", "{lingua}")}
    build.genera_sito(tmp_path, config=config)
    for lingua in config["lingue"]:
        testo = (tmp_path / lingua / "richiedi-prova.html").read_text(encoding="utf-8")
        nome = build.carica_testi(lingua)["nome_lingua"]
        assert f'rL=%22{build.quote(nome)}%22' in testo.replace("&amp;", "&"), lingua
        assert "{lingua}" not in testo
        assert '/static/js/richiedi-prova.js' in testo
        for pacchetto in AMMESSI:
            assert pacchetto in testo
        assert build.carica_testi(lingua)["richiedi_prova_senza_dati"] in testo.replace("&#39;", "'")


def test_con_xeicore_130_la_prova_si_chiede_dal_programma():
    assert build.prova_dal_programma({"xeicore": "1.3.0"})
    assert build.prova_dal_programma({"xeicore": "1.10.0"})
    assert not build.prova_dal_programma({"xeicore": "1.2.2"})
    assert not build.prova_dal_programma({"xeicore": "1.1.1"})


def test_la_pagina_download_spiega_la_prova_dal_programma(tmp_path, monkeypatch):
    addons = [dict(voce) for voce in build.carica_addons()]
    addons[0]["xeicore"] = "1.3.0"
    monkeypatch.setattr(build, "carica_addons", lambda: addons)
    build.genera_sito(tmp_path)
    testo = html.unescape((tmp_path / "it" / "download.html").read_text(encoding="utf-8"))
    assert build.carica_testi("it")["prova_dal_programma"] in testo
    # l'altro add-on (XEICore 1.2.x) mantiene il pulsante della prova
    assert testo.count(build.carica_testi("it")["download_richiedi_prova"]) == 1


def test_con_un_add_on_xeicore_130_sul_sito_il_modulo_deve_avere_il_codice():
    # Senza {codice} nel link, la prova dal menu Licenza arriverebbe al servizio senza codice e verrebbe rifiutata.
    config = build.carica_config()
    for addon in build.carica_addons():
        if build.prova_dal_programma(addon):
            assert "{codice}" in config["modulo_registrazione"], addon["id"]


def test_il_testo_approvato_si_divide_nelle_due_sezioni_della_pagina():
    html = ('<h1>Richiedi una prova</h1>\n<!-- nota -->\n<h2 id="a">Con i dati</h2>\n'
            '<p>Prova di <strong>{prodotto}</strong>.</p>\n<p>[Apri il modulo]</p>\n'
            '<h2 id="b">Senza i dati</h2>\n<p>Installa l\'add-on.</p>')
    con_dati, senza_dati = build.sezioni_richiedi_prova(html)
    assert '<strong><span class="prova-prodotto"></span></strong>' in con_dati
    assert '<a class="pulsante" id="prova-vai" href="#">Apri il modulo</a>' in con_dati
    assert "Richiedi una prova" not in con_dati and "nota" not in con_dati
    assert senza_dati.strip() == "<p>Installa l'add-on.</p>"


def test_senza_modulo_configurato_non_si_va_da_nessuna_parte():
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=7K3F-9QPA-2MXB", modello="") is None


def test_con_il_testo_approvato_la_pagina_usa_le_sue_sezioni_e_apre_subito_il_modulo(tmp_path, monkeypatch):
    sito = tmp_path / "site"
    shutil.copytree(build.CARTELLA_SITO, sito)
    (sito / "content" / "it" / "pagine" / "richiedi-prova.md").write_text(
        "---\ntitle: Richiedi una prova\nlang: it\nstato: approvato\n---\n\n# Richiedi una prova\n\n"
        "## Con i dati dell'add-on\n\nProva di **{prodotto}**.\n\n[Apri il modulo]\n\n"
        "## Senza i dati dell'add-on\n\nUsa il menu **Licenza**.\n", encoding="utf-8")
    monkeypatch.setattr(build, "CARTELLA_SITO", sito)
    build.genera_sito(tmp_path / "out")
    testo = (tmp_path / "out" / "it" / "richiedi-prova.html").read_text(encoding="utf-8")
    assert 'data-apri-subito="si"' in testo
    assert 'id="prova-vai" href="#">Apri il modulo</a>' in testo
    assert "Usa il menu <strong>Licenza</strong>." in testo
    # le altre lingue, finché manca la loro traduzione approvata, usano il testo italiano
    assert 'data-apri-subito="si"' in (tmp_path / "out" / "de" / "richiedi-prova.html").read_text(encoding="utf-8")
