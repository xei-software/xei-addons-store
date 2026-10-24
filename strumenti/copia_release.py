"""Copia il pacchetto di un add-on dalla Release del suo repository (privato) a una Release di questo repository.

Il file viene copiato identico, senza ricompilare. Prima della copia si controlla che:
- sia il pacchetto principale (niente pacchetto _TEST né mappa di offuscamento);
- dentro lo zip non ci siano codici di licenza, file di debug o sorgenti.

Uso (serve GitHub CLI con accesso in lettura al repository dell'add-on e in scrittura a questo):
    python -m strumenti.copia_release --origine xei-software/xei-itemgenerator --tag v1.4.0 \
        --file XEI.ItemGenerator.zip --id item-generator --data 2026-10-20

Alla fine stampa la voce da aggiungere (o aggiornare) in site/addons.yml.
"""
import argparse
import hashlib
import subprocess
import tempfile
import zipfile
from pathlib import Path

import yaml

REPOSITORY_PUBBLICO = "xei-software/xei-addons-store"
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


def voce_addons(percorso_zip, id_addon, pacchetto, versione, data_rilascio):
    """Dati del pacchetto per site/addons.yml."""
    contenuto = Path(percorso_zip).read_bytes()
    return {
        "id": id_addon,
        "pacchetto": pacchetto,
        "versione": versione,
        "data_rilascio": data_rilascio,
        "tag_pubblico": f"{id_addon}-v{versione}",
        "file": Path(percorso_zip).name,
        "dimensione": len(contenuto),
        "sha256": hashlib.sha256(contenuto).hexdigest(),
    }


def _gh(*argomenti):
    subprocess.run(["gh", *argomenti], check=True)


def main():
    parser = argparse.ArgumentParser(description="Copia il pacchetto di un add-on nella Release pubblica.")
    parser.add_argument("--origine", required=True, help="repository dell'add-on, es. xei-software/xei-itemgenerator")
    parser.add_argument("--tag", required=True, help="tag della Release dell'add-on, es. v1.4.0")
    parser.add_argument("--file", required=True, help="nome del pacchetto, es. XEI.ItemGenerator.zip")
    parser.add_argument("--id", required=True, help="identificativo sul sito, es. item-generator")
    parser.add_argument("--data", required=True, help="data di rilascio, es. 2026-10-20")
    argomenti = parser.parse_args()

    controlla_nome_file(argomenti.file)
    versione = argomenti.tag.lstrip("v")
    with tempfile.TemporaryDirectory() as cartella:
        _gh("release", "download", argomenti.tag, "--repo", argomenti.origine,
            "--pattern", argomenti.file, "--dir", cartella)
        percorso_zip = Path(cartella) / argomenti.file
        problemi = problemi_pacchetto(percorso_zip)
        if problemi:
            raise SystemExit(f"Pacchetto NON pubblicato, contiene file vietati: {problemi}")

        voce = voce_addons(percorso_zip, argomenti.id, Path(argomenti.file).stem, versione, argomenti.data)
        _gh("release", "create", voce["tag_pubblico"], str(percorso_zip),
            "--repo", REPOSITORY_PUBBLICO,
            "--title", f"{voce['pacchetto']} {versione}",
            "--notes", f"{voce['pacchetto']} {versione}. SHA-256: {voce['sha256']}")

    print("Voce per site/addons.yml (aggiungere lingue_programma):")
    print(yaml.safe_dump([voce], sort_keys=False, allow_unicode=True))


if __name__ == "__main__":
    main()
