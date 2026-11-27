"""Anteprima interna: lo stesso sito di produzione, pubblicato su Azure Static Web Apps (piano gratuito) e visibile solo
agli utenti GitHub invitati con il ruolo «interno» (richiesta di Ivan del 27/11/2026: verificare prima di pubblicare
e uso interno, senza costi né account nuovi)."""
import json

import pytest

import build


@pytest.fixture(scope="module")
def anteprima(tmp_path_factory):
    cartella = tmp_path_factory.mktemp("anteprima")
    build.genera_sito(cartella, config={**build.carica_config(), "manutenzione": {"fino_al": __import__("datetime").date(2026, 11, 30)}},
                      anteprima=True)
    return cartella


def test_l_anteprima_e_riservata_agli_utenti_con_il_ruolo_interno(anteprima):
    regole = json.loads((anteprima / "staticwebapp.config.json").read_text(encoding="utf-8"))
    tutte = next(r for r in regole["routes"] if r["route"] == "/*")
    assert tutte["allowedRoles"] == ["interno"]
    # si entra solo con GitHub: gli altri fornitori di login di Azure sono chiusi
    chiusi = {r["route"] for r in regole["routes"] if r.get("statusCode") == 404}
    assert {"/.auth/login/aad", "/.auth/login/twitter"} <= chiusi
    accesso = regole["responseOverrides"]["401"]
    assert accesso["redirect"].startswith("/.auth/login/github") and accesso["statusCode"] == 302


def test_l_anteprima_mostra_il_sito_vero_anche_durante_la_manutenzione(anteprima):
    # serve a controllare quello che andrà online alla riapertura
    for lingua in build.carica_config()["lingue"]:
        assert (anteprima / lingua / "download.html").exists(), lingua


def test_ogni_pagina_dice_che_e_l_anteprima_e_non_va_nei_motori_di_ricerca(anteprima):
    for pagina in anteprima.rglob("*.html"):
        testo = pagina.read_text(encoding="utf-8")
        assert '<meta name="robots" content="noindex">' in testo, pagina
        assert 'class="anteprima-avviso"' in testo, pagina


def test_l_anteprima_non_usa_il_dominio_dello_store(anteprima):
    assert not (anteprima / "CNAME").exists()


def test_il_sito_di_produzione_non_ha_niente_dell_anteprima(tmp_path):
    build.genera_sito(tmp_path)
    assert not (tmp_path / "staticwebapp.config.json").exists()
    for pagina in tmp_path.rglob("*.html"):
        assert "anteprima-avviso" not in pagina.read_text(encoding="utf-8"), pagina
