"""Controlli sui dati del sito: lingue, testi dell'interfaccia, elenco add-on e dati vietati."""
import re
import subprocess
from pathlib import Path

import pytest

import build

RADICE = Path(__file__).resolve().parent.parent
LINGUE_ATTESE = ["it", "en", "fr", "de", "tr", "es"]


def test_il_sito_ha_le_sei_lingue_con_italiano_predefinito():
    config = build.carica_config()
    assert config["lingue"] == LINGUE_ATTESE
    assert config["lingua_predefinita"] == "it"


def test_ogni_lingua_ha_tutti_i_testi_dell_interfaccia():
    config = build.carica_config()
    testi_italiani = build.carica_testi("it")
    for lingua in config["lingue"]:
        testi = build.carica_testi(lingua)
        assert set(testi) == set(testi_italiani), f"chiavi diverse in i18n/{lingua}.yml"
        vuoti = [chiave for chiave, valore in testi.items() if not str(valore).strip()]
        assert not vuoti, f"testi vuoti in i18n/{lingua}.yml: {vuoti}"


def test_ogni_add_on_ha_i_dati_obbligatori():
    for addon in build.carica_addons():
        assert re.fullmatch(r"[a-z0-9-]+", addon["id"]), addon["id"]
        assert re.fullmatch(r"\d+\.\d+\.\d+", addon["versione"]), addon["versione"]
        assert addon["file"].endswith(".zip")
        assert re.fullmatch(r"[0-9a-f]{64}", addon["sha256"]), "sha256 non valido"
        assert addon["dimensione"] > 0
        assert addon["tag_pubblico"] == f"{addon['id']}-v{addon['versione']}"


def test_si_pubblicano_solo_add_on_commerciali():
    # Mai gli add-on di prova o dei clienti (indicazione del Coordinatore XEI).
    for addon in build.carica_addons():
        testo = f"{addon['id']} {addon['pacchetto']} {addon['file']}".lower()
        assert "addontest" not in testo
        assert "cliente" not in testo
        assert "_test" not in testo, "il pacchetto _TEST non va pubblicato"


def test_ogni_add_on_ha_la_descrizione_in_italiano():
    for addon in build.carica_addons():
        percorso = RADICE / "site" / "content" / "it" / "addons" / f"{addon['id']}.md"
        assert percorso.exists(), f"manca {percorso}"
        meta, _ = build.leggi_markdown(percorso)
        assert meta.get("title") and meta.get("description")


def test_i_testi_in_bozza_non_vengono_pubblicati(tmp_path, monkeypatch):
    # Front matter del Coordinatore Documentazione: si pubblica solo "stato: approvato".
    for lingua, stato in (("it", "approvato"), ("en", "bozza")):
        cartella = tmp_path / "content" / lingua / "pagine"
        cartella.mkdir(parents=True)
        (cartella / "prova.md").write_text(f"---\ntitle: T {lingua}\nstato: {stato}\n---\nTesto {lingua}\n",
                                           encoding="utf-8")
    monkeypatch.setattr(build, "CARTELLA_SITO", tmp_path)
    intestazione, html, tradotto = build.leggi_contenuto("en", "pagine/prova.md", "it")
    assert intestazione["title"] == "T it" and not tradotto
    (tmp_path / "content" / "it" / "pagine" / "prova.md").write_text("---\nstato: bozza\n---\nx", encoding="utf-8")
    assert build.leggi_contenuto("en", "pagine/prova.md", "it") is None


def _file_del_repository():
    risultato = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=RADICE, capture_output=True, text=True, check=True,
    )
    return [RADICE / riga for riga in risultato.stdout.splitlines() if riga]


# Dati che non devono mai finire nel repository pubblico.
SCHEMI_VIETATI = {
    "percorso interno Windows": re.compile(r"[A-Za-z]:\\\\?(SORGENTI|Users|xei)", re.IGNORECASE),
    "token GitHub": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "chiave privata": re.compile(r"BEGIN [A-Z ]*PRIVATE KEY|<D>[A-Za-z0-9+/=]{20,}</D>"),
    "mappa di offuscamento": re.compile(r"obfuscation-map", re.IGNORECASE),
    # Regola di Ivan: nessun riferimento a programmi di partenza, migrazioni o tabelle non XEI.
    "programma di partenza VBO": re.compile(r"VBO", re.IGNORECASE),
}
ESTENSIONI_VIETATE = {".xei", ".cs", ".csproj", ".sln", ".pfx", ".snk", ".zip", ".dll", ".exe"}
# File che contengono gli schemi vietati solo per poterli bloccare.
FILE_CON_GLI_ELENCHI_DEI_DIVIETI = {
    Path(__file__).resolve(),
    RADICE / "tests" / "test_copia_release.py",
    RADICE / "strumenti" / "copia_release.py",
}


@pytest.mark.parametrize("nome_schema", sorted(SCHEMI_VIETATI))
def test_nessun_dato_riservato_nel_repository(nome_schema):
    schema = SCHEMI_VIETATI[nome_schema]
    trovati = []
    for percorso in _file_del_repository():
        if percorso.resolve() in FILE_CON_GLI_ELENCHI_DEI_DIVIETI or not percorso.is_file():
            continue
        testo = percorso.read_text(encoding="utf-8", errors="ignore")
        if schema.search(testo):
            trovati.append(str(percorso.relative_to(RADICE)))
    assert not trovati, f"{nome_schema} trovato in: {trovati}"


def test_nessun_file_di_licenza_sorgente_o_binario_nel_repository():
    vietati = [str(p.relative_to(RADICE)) for p in _file_del_repository() if p.suffix.lower() in ESTENSIONI_VIETATE]
    assert not vietati, f"file vietati: {vietati}"
