"""Generatore del sito degli add-on XEI.

Legge i dati da site/ (configurazione, elenco add-on, testi dell'interfaccia, contenuti in Markdown)
e scrive le pagine HTML statiche per GitHub Pages, una cartella per lingua.

Uso:
    python build.py                       # genera in _site/ per https://xei-software.github.io/xei-addons-store/
    python build.py --out anteprima --url-base ""   # anteprima locale (python -m http.server -d anteprima)
"""
import argparse
import shutil
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

CARTELLA_SITO = Path(__file__).resolve().parent / "site"
URL_BASE_PREDEFINITO = "/xei-addons-store"


def _leggi_yaml(percorso):
    with open(percorso, encoding="utf-8") as file:
        return yaml.safe_load(file)


def carica_config():
    return _leggi_yaml(CARTELLA_SITO / "config.yml")


def carica_testi(lingua):
    """Testi dell'interfaccia (menu, pulsanti, etichette) in una lingua."""
    return _leggi_yaml(CARTELLA_SITO / "i18n" / f"{lingua}.yml")


def carica_addons():
    """Add-on pubblicati, nell'ordine in cui compaiono nel sito."""
    return _leggi_yaml(CARTELLA_SITO / "addons.yml") or []


def leggi_markdown(percorso):
    """Restituisce (intestazione, html) di un file Markdown con intestazione YAML tra due righe '---'."""
    testo = Path(percorso).read_text(encoding="utf-8")
    intestazione = {}
    if testo.startswith("---"):
        _, blocco, testo = testo.split("---", 2)
        intestazione = yaml.safe_load(blocco) or {}
    html = markdown.markdown(testo, extensions=["tables", "fenced_code", "toc"])
    return intestazione, html


def leggi_contenuto(lingua, percorso_relativo, lingua_predefinita):
    """Contenuto nella lingua chiesta; se manca, quello nella lingua predefinita.

    I testi del Coordinatore Documentazione hanno "stato: bozza" o "stato: approvato" nell'intestazione:
    un testo in bozza si considera mancante.
    Restituisce (intestazione, html, tradotto). Se il file non c'è in nessuna lingua restituisce None.
    """
    for lingua_cercata in (lingua, lingua_predefinita):
        percorso = CARTELLA_SITO / "content" / lingua_cercata / percorso_relativo
        if not percorso.exists():
            continue
        intestazione, html = leggi_markdown(percorso)
        if intestazione.get("stato") == "bozza":
            continue
        return intestazione, html, lingua_cercata == lingua
    return None


def formatta_dimensione(byte):
    return f"{byte / (1024 * 1024):.1f} MB" if byte >= 1024 * 1024 else f"{byte / 1024:.0f} KB"


def link_richiesta_prova(addon, testi, config):
    """Dove porta il pulsante "Richiedi la prova": il modulo di registrazione o, finché manca, un'email."""
    if config["modulo_registrazione"]:
        return config["modulo_registrazione"]
    oggetto = quote(f"{testi['email_oggetto_prova']} - {addon['titolo']}")
    return f"mailto:{config['email_licenze']}?subject={oggetto}"


def _prepara_addon(addon, lingua, config):
    """Unisce i dati dell'add-on (addons.yml) con la sua descrizione nella lingua della pagina."""
    contenuto = leggi_contenuto(lingua, f"addons/{addon['id']}.md", config["lingua_predefinita"])
    intestazione, html, tradotto = contenuto
    manuale = leggi_contenuto(lingua, f"manuali/{addon['id']}.md", config["lingua_predefinita"])
    return {
        **addon,
        "titolo": intestazione["title"],
        "sommario": intestazione["description"],
        "descrizione_html": html,
        "tradotto": tradotto,
        "manuale": manuale,
        "url_download": (f"https://github.com/{config['repository']}/releases/download/"
                         f"{addon['tag_pubblico']}/{addon['file']}"),
        "dimensione_leggibile": formatta_dimensione(addon["dimensione"]),
    }


def _ambiente_modelli():
    return Environment(
        loader=FileSystemLoader(CARTELLA_SITO / "templates"),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def _scrivi(cartella_uscita, percorso_relativo, html):
    destinazione = cartella_uscita / percorso_relativo
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(html, encoding="utf-8")


def genera_sito(cartella_uscita, url_base=URL_BASE_PREDEFINITO, config=None):
    """Genera tutto il sito in cartella_uscita, sostituendone il contenuto."""
    cartella_uscita = Path(cartella_uscita)
    config = config or carica_config()
    ambiente = _ambiente_modelli()
    lingue = config["lingue"]
    nomi_lingue = {lingua: carica_testi(lingua)["nome_lingua"] for lingua in lingue}

    if cartella_uscita.exists():
        shutil.rmtree(cartella_uscita)
    shutil.copytree(CARTELLA_SITO / "static", cartella_uscita / "static")
    (cartella_uscita / ".nojekyll").write_text("", encoding="utf-8")

    for lingua in lingue:
        addons = [_prepara_addon(addon, lingua, config) for addon in carica_addons()]
        testi = carica_testi(lingua)
        comuni = {
            "config": config,
            "url_base": url_base,
            "lingua": lingua,
            "lingue": lingue,
            "nomi_lingue": nomi_lingue,
            "t": testi,
            "addons": addons,
            # testo con i giorni di prova al posto di {giorni}
            "testo": lambda chiave: testi[chiave].replace("{giorni}", str(config["giorni_prova"])),
            "link_prova": lambda addon: link_richiesta_prova(addon, testi, config),
        }

        def pagina(modello, percorso_relativo, **dati):
            # percorso_pagina serve al selettore della lingua per restare sulla stessa pagina
            html = ambiente.get_template(modello).render(**comuni, percorso_pagina=percorso_relativo, **dati)
            _scrivi(cartella_uscita / lingua, percorso_relativo, html)

        pagina("home.html", "index.html")
        pagina("download.html", "download.html")
        pagina("manuali.html", "manuali.html")
        for addon in addons:
            pagina("addon.html", f"addons/{addon['id']}.html", addon=addon)
            if addon["manuale"]:
                pagina("manuale.html", f"manuali/{addon['id']}.html", addon=addon)
        privacy = leggi_contenuto(lingua, "pagine/privacy.md", config["lingua_predefinita"])
        pagina("testo.html", "privacy.html", contenuto=privacy)

    radice = {"config": config, "url_base": url_base, "lingue": lingue, "nomi_lingue": nomi_lingue,
              "lingua_predefinita": config["lingua_predefinita"]}
    _scrivi(cartella_uscita, "index.html", ambiente.get_template("scelta_lingua.html").render(**radice))
    _scrivi(cartella_uscita, "404.html", ambiente.get_template("404.html").render(**radice))


def main():
    parser = argparse.ArgumentParser(description="Genera il sito degli add-on XEI.")
    parser.add_argument("--out", default="_site", help="cartella di uscita (default: _site)")
    parser.add_argument("--url-base", default=URL_BASE_PREDEFINITO,
                        help='prefisso degli indirizzi (default: /xei-addons-store; "" per l\'anteprima locale)')
    argomenti = parser.parse_args()
    genera_sito(Path(argomenti.out), url_base=argomenti.url_base)
    print(f"Sito generato in {argomenti.out}")


if __name__ == "__main__":
    main()
