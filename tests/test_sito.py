"""Controlli sul sito generato: pagine presenti, lingua giusta, collegamenti interni validi."""
import html
import re
from pathlib import Path

import pytest

import build


@pytest.fixture(scope="module")
def sito(tmp_path_factory):
    cartella = tmp_path_factory.mktemp("sito")
    build.genera_sito(cartella, url_base="/xei-addons-store")
    return cartella


def _pagine_attese():
    config = build.carica_config()
    pagine = ["index.html", "404.html"]
    for lingua in config["lingue"]:
        pagine += [
            f"{lingua}/index.html",
            f"{lingua}/download.html",
            f"{lingua}/manuali.html",
            f"{lingua}/privacy.html",
        ]
        pagine += [f"{lingua}/addons/{addon['id']}.html" for addon in build.carica_addons()]
    return pagine


def test_tutte_le_pagine_vengono_generate(sito):
    mancanti = [pagina for pagina in _pagine_attese() if not (sito / pagina).exists()]
    assert not mancanti, mancanti


def test_ogni_pagina_dichiara_la_sua_lingua(sito):
    for lingua in build.carica_config()["lingue"]:
        for pagina in (sito / lingua).rglob("*.html"):
            assert f'<html lang="{lingua}"' in pagina.read_text(encoding="utf-8"), pagina


def test_nessun_segnaposto_rimasto(sito):
    for pagina in sito.rglob("*.html"):
        testo = pagina.read_text(encoding="utf-8")
        assert "{{" not in testo and "{%" not in testo, pagina


def test_i_collegamenti_interni_portano_a_file_esistenti(sito):
    url_base = "/xei-addons-store"
    rotti = []
    for pagina in sito.rglob("*.html"):
        for destinazione in re.findall(r'(?:href|src)="([^"#?]+)', pagina.read_text(encoding="utf-8")):
            if not destinazione.startswith(url_base + "/"):
                continue
            file = sito / destinazione[len(url_base) + 1:]
            if destinazione.endswith("/"):
                file = file / "index.html"
            if not file.exists():
                rotti.append(f"{pagina.relative_to(sito)} -> {destinazione}")
    assert not rotti, rotti


def test_la_pagina_download_mostra_pacchetto_controllo_e_registrazione(sito):
    config = build.carica_config()
    testo = (sito / "it" / "download.html").read_text(encoding="utf-8")
    for addon in build.carica_addons():
        url = (f"https://github.com/{config['repository']}/releases/download/"
               f"{addon['tag_pubblico']}/{addon['file']}")
        assert url in testo
        assert addon["sha256"] in testo
        assert addon["versione"] in testo
    assert config["email_licenze"] in testo


def test_senza_modulo_la_richiesta_di_prova_va_per_email(tmp_path):
    config = build.carica_config()
    config["modulo_registrazione"] = ""
    build.genera_sito(tmp_path, url_base="", config=config)
    testo = (tmp_path / "en" / "download.html").read_text(encoding="utf-8")
    assert f"mailto:{config['email_licenze']}" in testo


def test_con_modulo_la_richiesta_di_prova_apre_il_modulo(tmp_path):
    config = build.carica_config()
    config["modulo_registrazione"] = "https://forms.office.com/r/esempio"
    build.genera_sito(tmp_path, url_base="", config=config)
    testo = (tmp_path / "de" / "download.html").read_text(encoding="utf-8")
    assert "https://forms.office.com/r/esempio" in testo


def test_testo_non_tradotto_usa_l_italiano_con_avviso(sito):
    # Finché manca la traduzione, la pagina mostra l'italiano e lo dice.
    addon = build.carica_addons()[0]
    traduzione = build.CARTELLA_SITO / "content" / "tr" / "addons" / f"{addon['id']}.md"
    if traduzione.exists():
        pytest.skip("traduzione turca già presente")
    testo = (sito / "tr" / "addons" / f"{addon['id']}.html").read_text(encoding="utf-8")
    assert build.carica_testi("tr")["avviso_traduzione"] in testo


def test_la_pagina_principale_rimanda_alle_lingue(sito):
    testo = (sito / "index.html").read_text(encoding="utf-8")
    for lingua in build.carica_config()["lingue"]:
        assert f'href="/xei-addons-store/{lingua}/"' in testo


def test_la_home_usa_il_testo_approvato(sito):
    percorso = build.CARTELLA_SITO / "content" / "it" / "pagine" / "home.md"
    intestazione, _ = build.leggi_markdown(percorso)
    assert intestazione["stato"] == "approvato"
    testo = (sito / "it" / "index.html").read_text(encoding="utf-8")
    assert "Perché scegliere gli add-on XEI" in testo


def test_nessun_collegamento_a_file_markdown(sito):
    # I link tra i file della documentazione (.md) vanno riscritti verso le pagine del sito.
    for pagina in sito.rglob("*.html"):
        assert not re.search(r'href="[^"]+\.md"', pagina.read_text(encoding="utf-8")), pagina


def test_le_note_di_rilascio_hanno_una_pagina(sito):
    for lingua in build.carica_config()["lingue"]:
        for addon in build.carica_addons():
            pagina = sito / lingua / "note" / f"{addon['id']}-{addon['versione']}.html"
            assert pagina.exists(), pagina
            scheda = (sito / lingua / "addons" / f"{addon['id']}.html").read_text(encoding="utf-8")
            assert f"/{lingua}/note/{addon['id']}-{addon['versione']}.html" in scheda


def test_il_titolo_della_scheda_non_si_ripete(sito):
    addon = build.carica_addons()[0]
    testo = (sito / "it" / "addons" / f"{addon['id']}.html").read_text(encoding="utf-8")
    assert testo.count("<h1") == 1


def test_logo_e_icona_ufficiali(sito):
    for file in ("static/img/logo-xei.png", "static/img/icona-x.png"):
        assert (sito / file).exists(), file
    testo = (sito / "it" / "index.html").read_text(encoding="utf-8")
    assert 'src="/xei-addons-store/static/img/logo-xei.png"' in testo
    assert 'rel="icon"' in testo


def test_l_email_di_richiesta_prova_e_gia_compilata():
    # Senza modulo il pulsante apre un'email con oggetto e testo già pronti, nella lingua della pagina.
    from urllib.parse import parse_qs, urlsplit
    config = {**build.carica_config(), "modulo_registrazione": ""}
    addon = {"titolo": "XEI Prova"}
    for lingua in config["lingue"]:
        testi = build.carica_testi(lingua)
        link = build.link_richiesta_prova(addon, testi, config)
        parametri = parse_qs(urlsplit(link).query)
        assert parametri["subject"] == [f"{testi['email_oggetto_prova']} - XEI Prova"]
        corpo = parametri["body"][0]
        assert "XEI Prova" in corpo and "\r\n" in corpo, lingua
        assert "{addon}" not in corpo and "{giorni}" not in corpo


def test_la_privacy_usa_il_testo_approvato(sito):
    for lingua in build.carica_config()["lingue"]:
        percorso = build.CARTELLA_SITO / "content" / lingua / "pagine" / "privacy.md"
        intestazione, _ = build.leggi_markdown(percorso)
        assert intestazione["stato"] == "approvato", lingua
        testo = (sito / lingua / "privacy.html").read_text(encoding="utf-8")
        assert build.carica_testi(lingua)["privacy_in_preparazione"] not in testo, lingua
    assert "GDPR" in (sito / "it" / "privacy.html").read_text(encoding="utf-8")


def test_nessun_contenuto_caricato_da_altri_siti(sito):
    # L'informativa dice che il sito non carica contenuti da altri siti: script, stili e immagini sono tutti locali.
    for pagina in sito.rglob("*.html"):
        testo = pagina.read_text(encoding="utf-8")
        assert not re.search(r'src="(?:https?:)?//', testo), pagina
        assert not re.search(r'<link[^>]+rel="stylesheet"[^>]+href="(?:https?:)?//', testo), pagina
    for foglio in sito.rglob("*.css"):
        assert not re.search(r"(?:@import|url\()\s*['\"]?(?:https?:)?//", foglio.read_text(encoding="utf-8")), foglio


def test_la_pagina_download_porta_alla_guida_di_installazione(sito):
    # L'email con il codice rimanda alla pagina download per programma, guida di installazione e codice.
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        testo = (sito / lingua / "download.html").read_text(encoding="utf-8")
        for addon in build.carica_addons():
            guida = f"/xei-addons-store/{lingua}/manuali/{addon['id']}/installazione"
            assert f'href="{guida}.html"' in testo, lingua
            assert f'href="{guida}.pdf"' in testo, lingua
            assert (sito / lingua / "manuali" / addon["id"] / "installazione.pdf").exists(), lingua
        assert html.escape(testi["download_guida_installazione"]) in testo
