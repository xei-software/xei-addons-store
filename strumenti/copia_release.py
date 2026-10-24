"""Pacchetti degli add-on: dalla Release del repository dell'add-on (privato) alla Release pubblica di questo repository.

Il file viene copiato identico, senza ricompilare. Due comandi:

    # 1) nuova versione: scarica il pacchetto, lo controlla e stampa la voce per site/addons.yml
    python -m strumenti.copia_release voce --origine xei-software/xei-itemgenerator --tag v1.4.0 \
        --file XEI.ItemGenerator.zip --id item-generator --data 2026-10-20

    # 2) usato dal workflow .github/workflows/release.yml al push del tag pubblico (es. item-generator-v1.4.0):
    #    scarica il pacchetto indicato in site/addons.yml e verifica che sia identico (SHA-256 e dimensione)
    python -m strumenti.copia_release prepara --tag-pubblico item-generator-v1.4.0 --out pacchetti

Controlli: si accetta solo il pacchetto principale (niente pacchetto _TEST né mappa di offuscamento) e dentro lo zip
non devono esserci codici di licenza, file di debug o sorgenti. Serve GitHub CLI con accesso in lettura al repository
dell'add-on (in Actions: segreto XEI_ADDON_READ_TOKEN).
"""
import argparse
import hashlib
import subprocess
import zipfile
from pathlib import Path

import yaml

ELENCO_ADDONS = Path(__file__).resolve().parent.parent / "site" / "addons.yml"
# File che non devono mai arrivare in un pacchetto pubblico.
ESTENSIONI_VIETATE_NELLO_ZIP = (".xei", ".pdb", ".cs", ".csproj", ".sln", ".pfx", ".snk")
PAROLE_VIETATE_NELLO_ZIP = ("obfuscation-map",)


def controlla_nome_file(nome_file):
    """Accetta solo il pacchetto principale dell'add-on (es. XEI.ItemGenerator.zip)."""
    if not nome_file.endswith(".zip") or nome_file.lower().endswith("_test.zip"):
        raise ValueError(f"{nome_file}: si pubblica solo il pacchetto principale .zip")


def problemi_pacchetto(percorso_zip):
    """Elenco dei file vietati trovati nello zip (vuoto se il pacchetto è pulito)."""
    with zipfile.ZipFile(percorso_zip) as archivio:
        nomi = archivio.namelist()
    return [nome for nome in nomi
            if nome.lower().endswith(ESTENSIONI_VIETATE_NELLO_ZIP)
            or any(parola in nome.lower() for parola in PAROLE_VIETATE_NELLO_ZIP)]


def impronta(percorso):
    return hashlib.sha256(Path(percorso).read_bytes()).hexdigest()


def voce_addons(percorso_zip, id_addon, pacchetto, versione, data_rilascio, origine, tag_origine):
    """Dati del pacchetto per site/addons.yml."""
    return {
        "id": id_addon,
        "pacchetto": pacchetto,
        "versione": versione,
        "data_rilascio": data_rilascio,
        "origine": origine,
        "tag_origine": tag_origine,
        "tag_pubblico": f"{id_addon}-v{versione}",
        "file": Path(percorso_zip).name,
        "dimensione": Path(percorso_zip).stat().st_size,
        "sha256": impronta(percorso_zip),
    }


def verifica_pacchetto(percorso_zip, voce):
    """Ferma la pubblicazione se il file non è quello di addons.yml o contiene file vietati."""
    controlla_nome_file(voce["file"])
    if Path(percorso_zip).stat().st_size != voce["dimensione"] or impronta(percorso_zip) != voce["sha256"]:
        raise SystemExit(f"{voce['file']}: SHA-256 o dimensione diversi da site/addons.yml, pacchetto NON pubblicato")
    problemi = problemi_pacchetto(percorso_zip)
    if problemi:
        raise SystemExit(f"{voce['file']}: contiene file vietati {problemi}, pacchetto NON pubblicato")


def cerca_voce(tag_pubblico, elenco=ELENCO_ADDONS):
    for voce in yaml.safe_load(Path(elenco).read_text(encoding="utf-8")) or []:
        if voce["tag_pubblico"] == tag_pubblico:
            return voce
    raise SystemExit(f"{tag_pubblico} non è in site/addons.yml")


def scarica_pacchetto(origine, tag, nome_file, cartella):
    """Scarica un file dalla Release <tag> del repository <origine> (API REST, tramite gh api)."""
    elenco = subprocess.run(
        ["gh", "api", f"repos/{origine}/releases/tags/{tag}", "--jq",
         f'.assets[] | select(.name == "{nome_file}") | .id'],
        check=True, capture_output=True, text=True).stdout.strip()
    if not elenco:
        raise SystemExit(f"{nome_file} non trovato nella Release {tag} di {origine}")
    percorso = Path(cartella) / nome_file
    percorso.parent.mkdir(parents=True, exist_ok=True)
    contenuto = subprocess.run(
        ["gh", "api", "-H", "Accept: application/octet-stream", f"repos/{origine}/releases/assets/{elenco}"],
        check=True, capture_output=True).stdout
    percorso.write_bytes(contenuto)
    return percorso


def comando_voce(argomenti):
    controlla_nome_file(argomenti.file)
    percorso = scarica_pacchetto(argomenti.origine, argomenti.tag, argomenti.file, argomenti.out)
    problemi = problemi_pacchetto(percorso)
    if problemi:
        raise SystemExit(f"Pacchetto NON pubblicabile, contiene file vietati: {problemi}")
    voce = voce_addons(percorso, argomenti.id, Path(argomenti.file).stem, argomenti.tag.lstrip("v"),
                       argomenti.data, argomenti.origine, argomenti.tag)
    print("Voce per site/addons.yml (aggiungere lingue_programma):")
    print(yaml.safe_dump([voce], sort_keys=False, allow_unicode=True))


def comando_prepara(argomenti):
    voce = cerca_voce(argomenti.tag_pubblico)
    percorso = scarica_pacchetto(voce["origine"], voce["tag_origine"], voce["file"], argomenti.out)
    verifica_pacchetto(percorso, voce)
    print(f"{percorso} verificato ({voce['sha256']})")


def main():
    parser = argparse.ArgumentParser(description="Pacchetti degli add-on per le Release pubbliche.")
    comandi = parser.add_subparsers(dest="comando", required=True)

    voce = comandi.add_parser("voce", help="controlla il pacchetto di una nuova versione e stampa la voce")
    voce.add_argument("--origine", required=True, help="repository dell'add-on, es. xei-software/xei-itemgenerator")
    voce.add_argument("--tag", required=True, help="tag della Release dell'add-on, es. v1.4.0")
    voce.add_argument("--file", required=True, help="nome del pacchetto, es. XEI.ItemGenerator.zip")
    voce.add_argument("--id", required=True, help="identificativo sul sito, es. item-generator")
    voce.add_argument("--data", required=True, help="data di rilascio, es. 2026-10-20")
    voce.add_argument("--out", default="pacchetti", help="cartella dove scaricare il pacchetto")
    voce.set_defaults(esegui=comando_voce)

    prepara = comandi.add_parser("prepara", help="scarica e verifica il pacchetto di un tag pubblico")
    prepara.add_argument("--tag-pubblico", required=True, help="es. item-generator-v1.4.0")
    prepara.add_argument("--out", default="pacchetti", help="cartella dove scaricare il pacchetto")
    prepara.set_defaults(esegui=comando_prepara)

    argomenti = parser.parse_args()
    argomenti.esegui(argomenti)


if __name__ == "__main__":
    main()
