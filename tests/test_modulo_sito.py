"""Modulo «Richiedi la prova gratuita» del sito (senza Microsoft Forms): un normale modulo HTML nella pagina di ogni
applicazione che invia i dati al servizio delle prove (POST /api/richiesta). Decisione di Ivan del 06/11/2026."""
import html
import json
import re
import shutil
import subprocess

import pytest

import build

SERVIZIO = "https://xei-prove.example/api/richiesta"


@pytest.fixture(scope="module")
def sito(tmp_path_factory):
    cartella = tmp_path_factory.mktemp("sito-modulo")
    build.genera_sito(cartella, config={**build.carica_config(), "servizio_prove": SERVIZIO})
    return cartella


def _modulo(sito, lingua, addon_id):
    testo = (sito / lingua / "addons" / f"{addon_id}.html").read_text(encoding="utf-8")
    trovato = re.search(r'<form[^>]*id="modulo-prova".*?</form>', testo, re.S)
    assert trovato, (lingua, addon_id)
    return trovato.group(0)


def test_ogni_pagina_di_applicazione_ha_il_modulo_che_invia_al_servizio(sito):
    for lingua in build.carica_config()["lingue"]:
        for addon in build.carica_addons():
            modulo = _modulo(sito, lingua, addon["id"])
            assert f'action="{SERVIZIO}"' in modulo
            assert 'method="post"' in modulo
            assert f'name="prodotto" value="{addon["pacchetto"]}"' in modulo
            assert f'name="lingua" value="{lingua}"' in modulo
            for campo in ("nome", "azienda", "partitaIva", "paese", "email", "informativa"):
                assert re.search(rf'name="{campo}"[^>]*required', modulo), (lingua, campo)
            assert f'href="/{lingua}/privacy.html"' in modulo


def test_il_campo_trappola_e_nascosto_e_fuori_dalla_tastiera(sito):
    modulo = _modulo(sito, "it", build.carica_addons()[0]["id"])
    trappola = re.search(r'<div class="trappola"[^>]*>.*?</div>', modulo, re.S).group(0)
    assert 'aria-hidden="true"' in trappola
    assert 'name="sito_web"' in trappola and 'tabindex="-1"' in trappola and 'autocomplete="off"' in trappola
    css = (build.CARTELLA_SITO / "static" / "css" / "sito.css").read_text(encoding="utf-8")
    assert re.search(r"\.trappola\s*\{[^}]*left:\s*-\d+px", css)


def test_il_paese_si_sceglie_dall_elenco_del_modulo(sito):
    modulo = _modulo(sito, "de", build.carica_addons()[0]["id"])
    for paese in build.carica_testi("de")["modulo_paesi"]:
        assert f'<option value="{html.escape(paese)}">' in modulo or f'<option>{html.escape(paese)}</option>' in modulo


def test_il_codice_della_societa_solo_per_xeicore_130(tmp_path, monkeypatch):
    addons = [dict(voce) for voce in build.carica_addons()]
    addons[0]["xeicore"] = "1.3.0"
    monkeypatch.setattr(build, "carica_addons", lambda: addons)
    build.genera_sito(tmp_path, config={**build.carica_config(), "servizio_prove": SERVIZIO})
    con_codice = _modulo(tmp_path, "it", addons[0]["id"])
    assert re.search(r'name="codiceSocieta"[^>]*required', con_codice)
    assert 'pattern="' in con_codice
    for altro in addons[1:]:
        assert 'name="codiceSocieta"' not in _modulo(tmp_path, "it", altro["id"])


def test_il_pulsante_della_pagina_download_porta_al_modulo(sito):
    for lingua in build.carica_config()["lingue"]:
        testo = (sito / lingua / "download.html").read_text(encoding="utf-8")
        for addon in build.carica_addons():
            assert f'href="/{lingua}/addons/{addon["id"]}.html#prova" data-azione="prova"' in testo, (lingua, addon["id"])


def test_le_pagine_di_esito_esistono_in_ogni_lingua(sito):
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        ricevuta = html.unescape((sito / lingua / "richiesta-ricevuta.html").read_text(encoding="utf-8"))
        assert testi["ricevuta_testo"].replace("{email}", build.carica_config()["email_licenze"]) in ricevuta
        non_valida = html.unescape((sito / lingua / "richiesta-non-valida.html").read_text(encoding="utf-8"))
        assert testi["non_valida_testo"] in non_valida


def test_senza_servizio_resta_il_modulo_di_oggi(tmp_path):
    build.genera_sito(tmp_path, config={**build.carica_config(), "servizio_prove": ""})
    testo = (tmp_path / "it" / "addons" / f"{build.carica_addons()[0]['id']}.html").read_text(encoding="utf-8")
    assert 'id="modulo-prova"' not in testo
    assert not (tmp_path / "it" / "richiesta-ricevuta.html").exists()


def test_la_pagina_richiedi_prova_porta_al_modulo_dell_applicazione_con_il_codice():
    if not shutil.which("node"):
        pytest.skip("node non installato")
    script = build.CARTELLA_SITO / "static" / "js" / "richiedi-prova.js"
    pagine = {"XEI.ItemGenerator": "/it/addons/item-generator.html"}
    codice = (f"const r = require({json.dumps(str(script))});"
              f"console.log(JSON.stringify([r.paginaModulo({json.dumps(pagine)}, '?prodotto=XEI.ItemGenerator&codice=7k3f-9qpa-2mxb'),"
              f" r.paginaModulo({json.dumps(pagine)}, '?prodotto=XEI.Altro&codice=7K3F-9QPA-2MXB')]))")
    uscita = json.loads(subprocess.run(["node", "-e", codice], capture_output=True, text=True, check=True).stdout)
    assert uscita == ["/it/addons/item-generator.html?codice=7K3F-9QPA-2MXB#prova", None]


def test_il_menu_licenza_si_scrive_con_il_separatore_dei_menu():
    # Indicazione del Coordinatore Documentazione: «Licenza › Richiedi una prova», non «>».
    for lingua in build.carica_config()["lingue"]:
        testo = build.carica_testi(lingua)["prova_dal_programma"]
        assert "›" in testo and ">" not in testo, lingua


def test_la_pagina_non_valida_torna_al_modulo_dell_applicazione(sito):
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        testo = html.unescape((sito / lingua / "richiesta-non-valida.html").read_text(encoding="utf-8"))
        pulsante = re.search(r'<a [^>]*id="torna-modulo"[^>]*>([^<]*)</a>', testo)
        assert pulsante and pulsante.group(1) == testi["non_valida_torna"], lingua
        # senza JavaScript o con un prodotto sconosciuto si torna alla pagina download
        assert f'href="/{lingua}/download.html"' in pulsante.group(0), lingua
        pagine = json.loads(re.search(r"data-pagine='([^']*)'", pulsante.group(0)).group(1))
        for addon in build.carica_addons():
            assert pagine[addon["pacchetto"]] == f"/{lingua}/addons/{addon['id']}.html", (lingua, addon["id"])
        assert 'src="/static/js/richiedi-prova.js"' in testo, lingua


def test_il_ritorno_al_modulo_usa_il_prodotto_dell_indirizzo():
    if not shutil.which("node"):
        pytest.skip("node non installato")
    script = build.CARTELLA_SITO / "static" / "js" / "richiedi-prova.js"
    pagine = {"XEI.ItemGenerator": "/it/addons/item-generator.html"}
    codice = (f"const r = require({json.dumps(str(script))});"
              f"console.log(JSON.stringify([r.paginaRitorno({json.dumps(pagine)}, '?prodotto=XEI.ItemGenerator'),"
              f" r.paginaRitorno({json.dumps(pagine)}, '?prodotto=XEI.Altro'), r.paginaRitorno({json.dumps(pagine)}, '')]))")
    uscita = json.loads(subprocess.run(["node", "-e", codice], capture_output=True, text=True, check=True).stdout)
    assert uscita == ["/it/addons/item-generator.html#prova", None, None]


def test_il_paese_parte_da_una_voce_che_chiede_di_sceglierlo(sito):
    # Una prima voce vuota sembrava un campo rotto: «Scegli il paese…», disabilitata e già selezionata.
    for lingua in build.carica_config()["lingue"]:
        testi = build.carica_testi(lingua)
        modulo = html.unescape(_modulo(sito, lingua, build.carica_addons()[0]["id"]))
        prima = re.search(r'<select name="paese" required>\s*(<option[^>]*>[^<]*</option>)', modulo)
        assert prima, lingua
        assert prima.group(1) == f'<option value="" disabled selected>{testi["modulo_scegli_paese"]}</option>', lingua


def test_invia_la_richiesta_ha_lo_stile_dei_pulsanti_principali(sito):
    foglio = (sito / "static" / "css" / "sito.css").read_text(encoding="utf-8")
    # stesso aspetto di «Scarica gratis» in tutte le pagine, anche per i <button>
    assert ".pagina-scura .pulsante {" in foglio
    assert re.search(r"button\.pulsante \{[^}]*font: inherit", foglio)
    modulo = _modulo(sito, "it", build.carica_addons()[0]["id"])
    assert '<button type="submit" class="pulsante">' in modulo
