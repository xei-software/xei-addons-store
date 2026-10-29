"""Pagina richiedi-prova.html: la apre il pulsante «Richiedi una prova» del menu Licenza (XEICore 1.3.0) con prodotto
e codice della società; manda al modulo di prova precompilato."""
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
    assert _indirizzo("?prodotto=XEI.ItemGenerator&codice=AB12-CD34-EF56") == \
        "https://forms.example/r?id=X&rA=%22XEI.ItemGenerator%22&rL=%22Italiano%22&rC=%22AB12-CD34-EF56%22"


def test_senza_parametri_o_con_valori_non_ammessi_non_si_va_al_modulo():
    assert _indirizzo("") is None
    assert _indirizzo("?prodotto=XEI.ItemGenerator") is None
    assert _indirizzo("?codice=AB12CD34EF56") is None
    assert _indirizzo("?prodotto=XEI.Altro&codice=AB12CD34EF56") is None
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
    testo = (tmp_path / "it" / "download.html").read_text(encoding="utf-8").replace("&#39;", "'")
    assert build.carica_testi("it")["prova_dal_programma"] in testo
    # l'altro add-on (XEICore 1.2.x) mantiene il pulsante della prova
    assert testo.count(build.carica_testi("it")["download_richiedi_prova"]) == 1
