"""Disponibilità di un programma sul sito (richiesta di Ivan del 06/11/2026), in site/addons.yml:

- «su_richiesta: true»: nessun pacchetto da scaricare; al posto di «Scarica gratis» e «Acquista» un solo pulsante
  «Richiedi informazioni» che apre un'email a info@xeisrl.com; niente prova automatica;
- «attivo: false»: il programma sparisce da tutto il sito (pagine, link, manuali, elenco delle prove) e torna togliendo
  la riga.
"""
import html
import json
import re
import shutil
from urllib.parse import parse_qs, urlsplit

import pytest
import yaml

import build
from strumenti import copia_release

SU_RICHIESTA = "commission-management"
SPENTO = "rate-updater"
# dati del pacchetto che una voce su richiesta non ha
CAMPI_PACCHETTO = ("versione", "data_rilascio", "origine", "tag_origine", "tag_pubblico", "file", "dimensione", "sha256",
                   "xeicore", "lingue_programma")


@pytest.fixture(scope="module")
def sito(tmp_path_factory):
    """Sito generato da una copia di site/ con una voce su richiesta e una spenta."""
    cartella = tmp_path_factory.mktemp("disponibilita")
    copia = cartella / "site"
    shutil.copytree(build.CARTELLA_SITO, copia)
    voci = yaml.safe_load((copia / "addons.yml").read_text(encoding="utf-8"))
    for voce in voci:
        voce.pop("attivo", None)  # si parte da tutti i programmi accesi, anche se oggi qualcuno è spento sul sito
        if voce["id"] == SU_RICHIESTA:
            for campo in CAMPI_PACCHETTO:
                voce.pop(campo, None)
            voce["su_richiesta"] = True
        if voce["id"] == SPENTO:
            voce["attivo"] = False
    (copia / "addons.yml").write_text(yaml.safe_dump(voci, sort_keys=False, allow_unicode=True), encoding="utf-8")
    originale = build.CARTELLA_SITO
    build.CARTELLA_SITO = copia
    try:
        # con il modulo del sito acceso, per controllare che il programma su richiesta non abbia il modulo della prova
        build.genera_sito(cartella / "uscita",
                          config={**build.carica_config(), "servizio_prove": "https://prove.example/api/richiesta"})
        yield cartella / "uscita"
    finally:
        build.CARTELLA_SITO = originale


def _pannello(testo, addon_id):
    trovato = re.search(rf'<article class="scheda download" id="{addon_id}">(.*?)</article>', testo, re.DOTALL)
    assert trovato, addon_id
    return trovato.group(1)


def test_un_programma_spento_sparisce_da_tutto_il_sito(sito):
    assert not (sito / "it" / "addons" / f"{SPENTO}.html").exists()
    for lingua in build.carica_config()["lingue"]:
        assert not (sito / lingua / "manuali" / SPENTO).exists(), lingua
    for pagina in sito.rglob("*.html"):
        testo = pagina.read_text(encoding="utf-8")
        assert SPENTO not in testo and "XEI.RateUpdater" not in testo, pagina
    nomi = [voce["nome"] for voce in json.loads((sito / "prodotti-prova.json").read_text(encoding="utf-8"))["prodotti"]]
    assert "XEI.RateUpdater" not in nomi
    # niente schermate dei suoi manuali tra i file pubblicati
    assert not (sito / "static" / "manuali" / "_img" / "rateupdater").exists()
    assert (sito / "static" / "manuali" / "_img" / "itemgenerator").exists()


def test_un_programma_su_richiesta_ha_solo_richiedi_informazioni_verso_info(sito):
    config = build.carica_config()
    for lingua in config["lingue"]:
        testi = build.carica_testi(lingua)
        pannello = html.unescape(_pannello((sito / lingua / "download.html").read_text(encoding="utf-8"), SU_RICHIESTA))
        pagina = html.unescape((sito / lingua / "addons" / f"{SU_RICHIESTA}.html").read_text(encoding="utf-8"))
        pulsanti = re.search(r'<p class="azioni">(.*?)</p>', pagina, re.S).group(1)  # il piè di pagina ha license@
        assert 'id="modulo-prova"' not in pagina, lingua
        for testo in (pannello, pulsanti):
            assert f">{testi['richiedi_informazioni']}</a>" in testo, lingua
            assert f'href="mailto:{config["email_informazioni"]}?' in testo, lingua
            assert testi["download_scarica_gratis"] not in testo and f">{testi['download_acquista']}</a>" not in testo
            assert 'data-azione="prova"' not in testo and "releases/download" not in testo
            assert 'id="modulo-prova"' not in testo
            assert config["email_licenze"] not in testo, lingua
        assert testi["download_guida_installazione"] not in pannello, lingua  # niente da installare dal sito


def test_l_email_di_informazioni_e_gia_compilata():
    config = build.carica_config()
    assert config["email_informazioni"] == "info@xeisrl.com"
    testi = build.carica_testi("it")
    link = build.link_informazioni({"titolo": "XEI Prova", "pacchetto": "XEI.Prova"}, testi, config)
    parametri = parse_qs(urlsplit(link).query)
    assert link.startswith("mailto:info@xeisrl.com?")
    assert parametri["subject"] == [f"{testi['email_oggetto_informazioni']} - XEI Prova"]
    assert "XEI Prova" in parametri["body"][0]


def test_un_programma_su_richiesta_non_ha_prova_ne_release(sito, tmp_path):
    nomi = [voce["nome"] for voce in json.loads((sito / "prodotti-prova.json").read_text(encoding="utf-8"))["prodotti"]]
    assert "XEI.CommissionManagement" not in nomi
    elenco = tmp_path / "addons.yml"
    elenco.write_text(yaml.safe_dump([{"id": "x", "pacchetto": "XEI.X", "su_richiesta": True},
                                      {"id": "y", "pacchetto": "XEI.Y", "tag_pubblico": "y-v1.0.0"}]), encoding="utf-8")
    assert copia_release.tag_pubblici(elenco) == ["y-v1.0.0"]


def test_le_pagine_del_programma_su_richiesta_non_mostrano_versione_ne_pacchetto(sito):
    pagina = (sito / "it" / "addons" / f"{SU_RICHIESTA}.html").read_text(encoding="utf-8")
    testi = build.carica_testi("it")
    assert f"<dt>{testi['addon_versione']}</dt>" not in pagina
    home = (sito / "it" / "index.html").read_text(encoding="utf-8")
    assert f"/it/addons/{SU_RICHIESTA}.html" in home  # resta nella home, senza versione
