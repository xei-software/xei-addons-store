"""Pagina download: pannello di ogni applicazione, schermate di anteprima, pulsanti «Scarica gratis» e «Acquista»,
accettazione delle condizioni d'uso."""
import html
import re
from urllib.parse import parse_qs, urlsplit

import pytest
import yaml

import build


@pytest.fixture(scope="module")
def sito(tmp_path_factory):
    cartella = tmp_path_factory.mktemp("sito")
    build.genera_sito(cartella)
    return cartella


def _pannello(testo, addon_id):
    """HTML del pannello di un'applicazione nella pagina download."""
    trovato = re.search(rf'<article class="scheda download" id="{addon_id}">(.*?)</article>', testo, re.DOTALL)
    assert trovato, addon_id
    return trovato.group(1)


def _con_condizioni_approvate(tmp_path, monkeypatch):
    """Copia di site/ con le condizioni d'uso approvate in italiano (il testo vero può essere ancora in bozza)."""
    import shutil
    copia = tmp_path / "site"
    shutil.copytree(build.CARTELLA_SITO, copia)
    (copia / "content" / "it" / "pagine" / "condizioni.md").write_text(
        "---\ntitle: Condizioni d'uso\ndescription: Prova\nlang: it\nstato: approvato\n---\n\n"
        "# Condizioni d'uso\n\nTesto delle condizioni.\n", encoding="utf-8")
    monkeypatch.setattr(build, "CARTELLA_SITO", copia)
    return copia


def test_il_pannello_non_mostra_piu_il_controllo_sha256(sito):
    # Al cliente non serve; l'impronta resta in addons.yml per il workflow delle Release.
    for lingua in build.carica_config()["lingue"]:
        testo = (sito / lingua / "download.html").read_text(encoding="utf-8")
        for addon in build.carica_addons():
            assert addon["sha256"] not in testo, lingua
        assert "SHA-256" not in testo, lingua


def test_i_pulsanti_si_chiamano_scarica_gratis_e_acquista(sito):
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        testo = html.unescape((sito / lingua / "download.html").read_text(encoding="utf-8"))
        for addon in build.carica_addons():
            pannello = html.unescape(_pannello(testo, addon["id"]))
            assert f">{testi['download_scarica_gratis']}</a>" in pannello, lingua
            assert f">{testi['download_acquista']}</a>" in pannello, lingua


def test_scarica_gratis_apre_il_modulo_e_porta_il_pacchetto(sito):
    config = build.carica_config()
    testo = (sito / "it" / "download.html").read_text(encoding="utf-8")
    for addon in build.carica_addons():
        pannello = html.unescape(_pannello(testo, addon["id"]))
        pacchetto = (f"https://github.com/{config['repository']}/releases/download/"
                     f"{addon['tag_pubblico']}/{addon['file']}")
        assert f'data-pacchetto="{pacchetto}"' in pannello
        assert 'data-azione="prova"' in pannello and 'data-azione="acquisto"' in pannello
        assert "forms.cloud.microsoft" in pannello


def test_acquista_senza_domanda_richiesta_nel_modulo_apre_un_email_di_acquisto():
    # Finché il modulo non ha la domanda «Richiesta» ({richiesta}), l'acquisto non deve finire tra le prove.
    config = {**build.carica_config(), "modulo_registrazione": "https://forms.office.com/r/x?a=%22{addon}%22"}
    testi = build.carica_testi("it")
    link = build.link_acquisto({"titolo": "XEI Prova", "pacchetto": "XEI.Prova"}, testi, config)
    parametri = parse_qs(urlsplit(link).query)
    assert link.startswith(f"mailto:{config['email_licenze']}?")
    assert parametri["subject"] == [f"{testi['email_oggetto_acquisto']} - XEI Prova"]


def test_con_la_domanda_richiesta_entrambi_i_pulsanti_usano_il_modulo():
    config = {**build.carica_config(),
              "modulo_registrazione": "https://forms.office.com/r/x?a=%22{addon}%22&r=%22{richiesta}%22"}
    testi = build.carica_testi("en")
    addon = {"titolo": "XEI Prova", "pacchetto": "XEI.Prova"}
    prova = parse_qs(urlsplit(build.link_richiesta_prova(addon, testi, config)).query)
    acquisto = parse_qs(urlsplit(build.link_acquisto(addon, testi, config)).query)
    assert prova["r"] == [f'"{config["richiesta_prova"]}"']
    assert acquisto["r"] == [f'"{config["richiesta_acquisto"]}"']
    assert prova["a"] == acquisto["a"] == ['"XEI.Prova"']


def test_ogni_applicazione_ha_da_una_a_sei_schermate_di_anteprima(sito):
    anteprime = yaml.safe_load((build.CARTELLA_SITO / "anteprime.yml").read_text(encoding="utf-8"))
    for addon in build.carica_addons():
        voce = anteprime[addon["id"]]
        assert 1 <= len(voce["immagini"]) <= 6, addon["id"]
        for immagine in voce["immagini"]:
            # solo schermate già importate (e controllate) dai manuali di xei-model-docs
            assert (build.CARTELLA_SITO / "content" / "_img" / voce["cartella"] / immagine).exists(), immagine
            assert (sito / "static" / "manuali" / "_img" / voce["cartella"] / immagine).exists(), immagine


def test_il_pannello_mostra_l_anteprima_che_apre_la_galleria(sito):
    anteprime = yaml.safe_load((build.CARTELLA_SITO / "anteprime.yml").read_text(encoding="utf-8"))
    for lingua in build.carica_config()["lingue"]:
        testo = (sito / lingua / "download.html").read_text(encoding="utf-8")
        assert '<dialog class="galleria"' in testo, lingua
        assert 'src="/static/js/sito.js"' in testo, lingua
        for addon in build.carica_addons():
            voce = anteprime[addon["id"]]
            pannello = _pannello(testo, addon["id"])
            for immagine in voce["immagini"]:
                assert f"/static/manuali/_img/{voce['cartella']}/{immagine}" in pannello, (lingua, immagine)
            assert 'class="anteprima"' in pannello


def test_i_testi_dell_interfaccia_non_parlano_di_add_on_ne_di_sap(sito):
    # Il sito pubblica soluzioni software di ogni tipo: nell'interfaccia «applicazione», non «add-on».
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        for chiave, valore in testi.items():
            visibile = str(valore).replace("{addon}", "")  # segnaposto del nome dell'applicazione
            assert not re.search(r"add-?on|SAP|Extension Manager", visibile, re.IGNORECASE), (lingua, chiave)
    assert "add-on" not in build.carica_config()["nome_sito"].lower()


def test_la_versione_di_sap_non_si_chiede_piu():
    for lingua in build.carica_config()["lingue"]:
        assert "SAP" not in build.carica_testi(lingua)["email_corpo_prova"], lingua


def test_senza_condizioni_approvate_non_c_e_la_finestra_di_accettazione(sito):
    # Le condizioni d'uso si pubblicano solo approvate (Coordinatore Documentazione, revisione legale).
    if build.leggi_contenuto("it", "pagine/condizioni.md", "it") is not None:
        pytest.skip("condizioni già approvate")
    testo = (sito / "it" / "download.html").read_text(encoding="utf-8")
    assert 'class="condizioni"' not in testo
    assert not (sito / "it" / "condizioni.html").exists()


def test_con_condizioni_approvate_i_pulsanti_chiedono_l_accettazione(tmp_path, monkeypatch):
    _con_condizioni_approvate(tmp_path, monkeypatch)
    uscita = tmp_path / "uscita"
    build.genera_sito(uscita)
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        testo = html.unescape((uscita / lingua / "download.html").read_text(encoding="utf-8"))
        assert '<dialog class="condizioni"' in testo, lingua
        assert f'href="/{lingua}/condizioni.html"' in testo, lingua
        # due spunte: accettazione e approvazione specifica delle clausole (artt. 1341 e 1342 c.c.)
        assert testo.count('type="checkbox"') == 2, lingua
        assert testi["condizioni_approvo"] in testo and "1341" in testi["condizioni_approvo"], lingua
        assert (uscita / lingua / "condizioni.html").exists(), lingua


def test_la_pagina_download_ha_lo_sfondo_scuro_del_marchio(sito):
    # Sfondo notte come quello del logo XEI; le altre pagine restano chiare.
    for lingua in build.carica_config()["lingue"]:
        assert '<body class="pagina-scura">' in (sito / lingua / "download.html").read_text(encoding="utf-8"), lingua
        assert "pagina-scura" not in (sito / lingua / "index.html").read_text(encoding="utf-8"), lingua
    assert ".pagina-scura" in (sito / "static" / "css" / "sito.css").read_text(encoding="utf-8")
