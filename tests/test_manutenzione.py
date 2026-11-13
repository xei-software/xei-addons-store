"""Manutenzione: tutto lo store diventa una sola pagina «Torna a trovarci il …», con lo stile del sito
(richiesta di Ivan del 13/11/2026). Si accende con «manutenzione: {fino_al: aaaa-mm-gg}» in site/config.yml."""
import datetime
import html

import pytest
import yaml

import build

ATTESI = {
    "it": "Torna a trovarci il 30 novembre 2026",
    "en": "Come back and visit us on 30 November 2026",
    "fr": "Revenez nous voir le 30 novembre 2026",
    "de": "Besuchen Sie uns wieder am 30. November 2026",
    "es": "Vuelva a visitarnos el 30 de noviembre de 2026",
    "tr": "30 Kasım 2026'da tekrar bekleriz",
}


@pytest.fixture(scope="module")
def sito(tmp_path_factory):
    cartella = tmp_path_factory.mktemp("manutenzione")
    build.genera_sito(cartella, config={**build.carica_config(),
                                        "manutenzione": {"fino_al": datetime.date(2026, 11, 30)}})
    return cartella


def test_ogni_lingua_mostra_solo_il_messaggio(sito):
    for lingua, messaggio in ATTESI.items():
        testo = html.unescape((sito / lingua / "index.html").read_text(encoding="utf-8"))
        assert messaggio in testo, lingua
        assert f'<html lang="{lingua}">' in testo
        assert '<body class="pagina-scura">' in testo and 'src="/static/img/logo-xei-bianco.png"' in testo
        assert 'href="https://xeisrl.com/"' in testo
        assert "download.html" not in testo and "manuali.html" not in testo  # nessun link a pagine spente


def test_non_resta_nessun_altra_pagina(sito):
    pagine = sorted(str(p.relative_to(sito)) for p in sito.rglob("*.html") if "static" not in p.parts)
    attese = sorted(["index.html", "404.html"] + [f"{lingua}/index.html" for lingua in ATTESI])
    assert pagine == attese
    # ogni altro indirizzo (vecchi link, preferiti) finisce nella 404, che dice lo stesso in tutte le lingue
    pagina_404 = html.unescape((sito / "404.html").read_text(encoding="utf-8"))
    for messaggio in ATTESI.values():
        assert messaggio in pagina_404
    assert (sito / "CNAME").exists() and (sito / "static" / "css" / "sito.css").exists()
    assert not (sito / "static" / "manuali").exists()  # niente immagini o file dei manuali


def test_l_elenco_delle_prove_resta(sito):
    # il servizio delle prove lo legge comunque: niente errori lato servizio durante la manutenzione
    assert (sito / "prodotti-prova.json").exists()


def test_la_configurazione_pubblicata_ha_la_manutenzione_fino_al_30_novembre():
    config = yaml.safe_load((build.CARTELLA_SITO / "config.yml").read_text(encoding="utf-8"))
    assert config["manutenzione"]["fino_al"] == datetime.date(2026, 11, 30)
