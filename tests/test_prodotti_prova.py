"""File /prodotti-prova.json: l'elenco dei prodotti con la prova che il servizio delle prove legge dal sito.
Per aggiungere un prodotto alle prove basta pubblicare la sua voce in addons.yml (richiesta di Ivan del 06/11/2026)."""
import json
import re

import pytest

import build


@pytest.fixture(scope="module")
def sito(tmp_path_factory):
    cartella = tmp_path_factory.mktemp("sito-prodotti")
    build.genera_sito(cartella)
    return cartella


def _elenco(sito):
    return json.loads((sito / "prodotti-prova.json").read_text(encoding="utf-8"))


def test_il_sito_pubblica_l_elenco_dei_prodotti_con_la_prova(sito):
    prodotti = {voce["nome"]: voce for voce in _elenco(sito)["prodotti"]}
    addons = build.addons_con_pacchetto()
    assert set(prodotti) == {addon["pacchetto"] for addon in addons}
    for addon in addons:
        voce = prodotti[addon["pacchetto"]]
        assert voce["versione"] == str(addon["versione"])  # la versione pubblicata
        if addon.get("xeicore"):
            assert voce["xeicore"] == str(addon["xeicore"])
        else:
            assert "xeicore" not in voce  # le app non hanno XEICore


def test_l_elenco_contiene_solo_nome_versione_e_xeicore(sito):
    for voce in _elenco(sito)["prodotti"]:
        assert set(voce) <= {"nome", "versione", "xeicore"}
        assert re.fullmatch(r"XEI\.[A-Za-z0-9]+", voce["nome"])
        assert re.fullmatch(r"\d+\.\d+\.\d+", voce["versione"])
        assert "xeicore" not in voce or re.fullmatch(r"\d+\.\d+\.\d+", voce["xeicore"])


def test_una_voce_con_prova_false_non_e_nell_elenco():
    addons = [{"pacchetto": "XEI.Uno", "versione": "1.0.0", "xeicore": "1.3.0"},
              {"pacchetto": "XEI.Due", "versione": "2.0.0", "prova": False}]
    assert build.prodotti_prova(addons) == {"prodotti": [{"nome": "XEI.Uno", "versione": "1.0.0", "xeicore": "1.3.0"}]}
