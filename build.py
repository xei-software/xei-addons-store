"""Generatore del sito degli add-on XEI.

Legge i dati da site/ (configurazione, elenco add-on, testi dell'interfaccia, contenuti in Markdown)
e scrive le pagine HTML statiche per GitHub Pages, una cartella per lingua.

Uso:
    python build.py                       # genera in _site/ per https://xei-software.github.io/xei-addons-store/
    python build.py --out anteprima --url-base ""   # anteprima locale (python -m http.server -d anteprima)
"""
import argparse
import re
import shutil
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

CARTELLA_SITO = Path(__file__).resolve().parent / "site"
# Il sito sta alla radice del dominio personalizzato (dominio in config.yml): nessun prefisso negli indirizzi.
URL_BASE_PREDEFINITO = ""


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

    I testi del Coordinatore Documentazione hanno "stato: bozza", "interno" o "approvato" nell'intestazione:
    si pubblica solo "approvato", ogni altro testo si considera mancante.
    Restituisce (intestazione, html, tradotto). Se il file non c'è in nessuna lingua restituisce None.
    """
    for lingua_cercata in (lingua, lingua_predefinita):
        percorso = CARTELLA_SITO / "content" / lingua_cercata / percorso_relativo
        if not percorso.exists():
            continue
        intestazione, html = leggi_markdown(percorso)
        if intestazione.get("stato") != "approvato":  # bozza, interno o senza stato: mai pubblicato
            continue
        return intestazione, html, lingua_cercata == lingua
    return None


def formatta_dimensione(byte):
    return f"{byte / (1024 * 1024):.1f} MB" if byte >= 1024 * 1024 else f"{byte / 1024:.0f} KB"


def _link_modulo(addon, testi, config, richiesta):
    """Link precompilato del modulo di registrazione: {addon}, {lingua} e {richiesta} diventano le scelte del modulo
    (nome del pacchetto, nome della lingua della pagina, prova o acquisto), così il modulo si apre già compilato."""
    return (config["modulo_registrazione"]
            .replace("{addon}", quote(addon.get("pacchetto", "")))
            .replace("{lingua}", quote(testi["nome_lingua"]))
            .replace("{richiesta}", quote(richiesta)))


def _link_email(addon, testi, config, chiave):
    """Email a email_licenze con oggetto e testo già pronti (chiave: "prova" o "acquisto")."""
    oggetto = quote(f"{testi['email_oggetto_' + chiave]} - {addon['titolo']}")
    # testo già pronto con i dati da compilare; nelle email gli a capo sono \r\n
    corpo = (testi["email_corpo_" + chiave].strip()
             .replace("{addon}", addon["titolo"])
             .replace("{giorni}", str(config["giorni_prova"]))
             .replace("\n", "\r\n"))
    return f"mailto:{config['email_licenze']}?subject={oggetto}&body={quote(corpo)}"


def link_richiesta_prova(addon, testi, config):
    """Dove porta il pulsante "Scarica gratis": il modulo di registrazione o, finché manca, un'email."""
    if config["modulo_registrazione"]:
        return _link_modulo(addon, testi, config, config["richiesta_prova"])
    return _link_email(addon, testi, config, "prova")


def link_acquisto(addon, testi, config):
    """Dove porta il pulsante "Acquista": il modulo, se ha la domanda «Richiesta» ({richiesta}); altrimenti un'email.

    Senza quella domanda il modulo tratterebbe l'acquisto come una richiesta di prova.
    """
    if "{richiesta}" in config["modulo_registrazione"]:
        return _link_modulo(addon, testi, config, config["richiesta_acquisto"])
    return _link_email(addon, testi, config, "acquisto")


def carica_anteprime():
    """Schermate di anteprima di ogni applicazione (site/anteprime.yml): {id: {"cartella": ..., "immagini": [...]}}."""
    percorso = CARTELLA_SITO / "anteprime.yml"
    return (_leggi_yaml(percorso) or {}) if percorso.exists() else {}


def togli_primo_titolo(html):
    """Toglie il primo <h1>: nella scheda il titolo lo mette il modello, dal front matter."""
    return re.sub(r"<h1[^>]*>.*?</h1>\s*", "", html, count=1, flags=re.DOTALL)


def riscrivi_link_note(html, addon_id, lingua, url_base):
    """I link alle note di rilascio della documentazione (note-rilascio-<versione>.md) puntano alla pagina del sito."""
    return re.sub(r'href="[^"]*note-rilascio-([\d.]+)\.md"',
                  lambda trovato: f'href="{url_base}/{lingua}/note/{addon_id}-{trovato.group(1)}.html"', html)


def riscrivi_link_scheda(html, addon_id, lingua, url_base):
    """Link della scheda dell'add-on: note di rilascio e manuali (manuali/<lingua>/<prodotto>/<nome>.md) -> pagine del sito."""
    html = riscrivi_link_note(html, addon_id, lingua, url_base)
    return re.sub(r'href="[^"]*manuali/[\w-]+/[\w-]+/([\w-]+)\.md"',
                  rf'href="{url_base}/{lingua}/manuali/{addon_id}/\1.html"', html)


def riscrivi_link_manuale(html, addon_id, lingua, url_base):
    """Link di un manuale della documentazione verso le pagine e le risorse del sito.

    - immagini e file di esempio (../../_img/..., ../../_file/...) -> static/manuali/_img/..., _file/...
    - altri manuali dello stesso add-on (installazione.md) -> pagina del sito nella stessa lingua
    """
    html = re.sub(r'(src|href)="(?:\.\./)+(_img|_file)/', rf'\1="{url_base}/static/manuali/\2/', html)
    html = re.sub(r'href="([\w-]+)\.md"', rf'href="{url_base}/{lingua}/manuali/{addon_id}/\1.html"', html)
    return riscrivi_link_note(html, addon_id, lingua, url_base)


# Ordine dei manuali nell'elenco; gli altri seguono in ordine alfabetico.
ORDINE_MANUALI = ["manuale-utente", "installazione"]


def elenco_manuali(addon_id, lingua, lingua_predefinita, url_base):
    """Manuali approvati di un add-on nella lingua della pagina (o nella lingua predefinita, se manca)."""
    nomi = set()
    for lingua_cercata in (lingua, lingua_predefinita):
        cartella = CARTELLA_SITO / "content" / lingua_cercata / "manuali" / addon_id
        if cartella.is_dir():
            nomi.update(file.stem for file in cartella.glob("*.md"))
    ordinati = sorted(nomi, key=lambda nome: (ORDINE_MANUALI.index(nome) if nome in ORDINE_MANUALI
                                               else len(ORDINE_MANUALI), nome))
    manuali = []
    for nome in ordinati:
        contenuto = leggi_contenuto(lingua, f"manuali/{addon_id}/{nome}.md", lingua_predefinita)
        if contenuto is None:  # solo in bozza
            continue
        intestazione, html, tradotto = contenuto
        lingua_del_testo = lingua if tradotto else lingua_predefinita
        pdf = CARTELLA_SITO / "content" / lingua_del_testo / "manuali" / addon_id / f"{nome}.pdf"
        manuali.append({
            "nome": nome,
            "titolo": intestazione["title"],
            "documento": (intestazione, riscrivi_link_manuale(html, addon_id, lingua, url_base), tradotto),
            "pdf": pdf if pdf.exists() else None,
        })
    return manuali


def _copia_risorse_manuali(cartella_uscita):
    """Immagini e file di esempio dei manuali (content/_img, content/_file), comuni a tutte le lingue."""
    for sotto in ("_img", "_file"):
        sorgente = CARTELLA_SITO / "content" / sotto
        if sorgente.is_dir():
            shutil.copytree(sorgente, cartella_uscita / "static" / "manuali" / sotto)


def _prepara_addon(addon, lingua, config, url_base, anteprime):
    """Unisce i dati dell'add-on (addons.yml) con la sua descrizione nella lingua della pagina."""
    predefinita = config["lingua_predefinita"]
    intestazione, html, tradotto = leggi_contenuto(lingua, f"addons/{addon['id']}.md", predefinita)
    manuali = elenco_manuali(addon["id"], lingua, predefinita, url_base)
    note = leggi_contenuto(lingua, f"note/{addon['id']}-{addon['versione']}.md", predefinita)
    voce_anteprime = anteprime.get(addon["id"], {"immagini": []})
    return {
        **addon,
        "titolo": intestazione["title"],
        "sommario": intestazione["description"],
        "descrizione_html": riscrivi_link_scheda(togli_primo_titolo(html), addon["id"], lingua, url_base),
        "note": note,
        "tradotto": tradotto,
        "manuali": manuali,
        "installazione": next((m for m in manuali if m["nome"] == "installazione"), None),
        "url_download": (f"https://github.com/{config['repository']}/releases/download/"
                         f"{addon['tag_pubblico']}/{addon['file']}"),
        "dimensione_leggibile": formatta_dimensione(addon["dimensione"]),
        # copiate da content/_img in static/manuali/_img con le immagini dei manuali
        "anteprime": [f"{url_base}/static/manuali/_img/{voce_anteprime['cartella']}/{immagine}"
                      for immagine in voce_anteprime["immagini"]],
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
    _copia_risorse_manuali(cartella_uscita)
    (cartella_uscita / ".nojekyll").write_text("", encoding="utf-8")
    (cartella_uscita / "CNAME").write_text(config["dominio"] + "\n", encoding="utf-8")

    anteprime = carica_anteprime()
    for lingua in lingue:
        addons = [_prepara_addon(addon, lingua, config, url_base, anteprime) for addon in carica_addons()]
        testi = carica_testi(lingua)
        # condizioni d'uso da accettare prima di scaricare o acquistare: solo se approvate
        condizioni = leggi_contenuto(lingua, "pagine/condizioni.md", config["lingua_predefinita"])
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
            "link_acquisto": lambda addon: link_acquisto(addon, testi, config),
            "condizioni": condizioni,
        }

        def pagina(modello, percorso_relativo, **dati):
            # percorso_pagina serve al selettore della lingua per restare sulla stessa pagina
            html = ambiente.get_template(modello).render(**comuni, percorso_pagina=percorso_relativo, **dati)
            _scrivi(cartella_uscita / lingua, percorso_relativo, html)

        pagina("home.html", "index.html",
               presentazione=leggi_contenuto(lingua, "pagine/home.md", config["lingua_predefinita"]))
        pagina("download.html", "download.html")
        pagina("manuali.html", "manuali.html")
        for addon in addons:
            pagina("addon.html", f"addons/{addon['id']}.html", addon=addon)
            for manuale in addon["manuali"]:
                percorso = f"manuali/{addon['id']}/{manuale['nome']}"
                pdf_url = None
                if manuale["pdf"]:
                    destinazione = cartella_uscita / lingua / f"{percorso}.pdf"
                    destinazione.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(manuale["pdf"], destinazione)
                    pdf_url = f"{url_base}/{lingua}/{percorso}.pdf"
                pagina("documento.html", f"{percorso}.html", documento=manuale["documento"],
                       titolo_pagina=f"{manuale['titolo']} · {addon['titolo']}", pdf_url=pdf_url)
            if addon["note"]:
                pagina("documento.html", f"note/{addon['id']}-{addon['versione']}.html", documento=addon["note"],
                       titolo_pagina=addon["note"][0]["title"], pdf_url=None)
        privacy = leggi_contenuto(lingua, "pagine/privacy.md", config["lingua_predefinita"])
        pagina("testo.html", "privacy.html", contenuto=privacy, titolo_pagina=testi["privacy_titolo"])
        if condizioni:
            pagina("testo.html", "condizioni.html", contenuto=condizioni, titolo_pagina=condizioni[0]["title"])

    radice = {"config": config, "url_base": url_base, "lingue": lingue, "nomi_lingue": nomi_lingue,
              "lingua_predefinita": config["lingua_predefinita"]}
    _scrivi(cartella_uscita, "index.html", ambiente.get_template("scelta_lingua.html").render(**radice))
    _scrivi(cartella_uscita, "404.html", ambiente.get_template("404.html").render(**radice))


def main():
    parser = argparse.ArgumentParser(description="Genera il sito degli add-on XEI.")
    parser.add_argument("--out", default="_site", help="cartella di uscita (default: _site)")
    parser.add_argument("--url-base", default=URL_BASE_PREDEFINITO,
                        help='prefisso degli indirizzi (predefinito: nessuno, il sito sta alla radice del dominio)')
    argomenti = parser.parse_args()
    genera_sito(Path(argomenti.out), url_base=argomenti.url_base)
    print(f"Sito generato in {argomenti.out}")


if __name__ == "__main__":
    main()
