"""Controlli sullo script che copia un pacchetto dalla Release privata dell'add-on a quella pubblica."""
import zipfile

import pytest
import yaml

from strumenti import copia_release


def _crea_zip(percorso, nomi):
    with zipfile.ZipFile(percorso, "w") as archivio:
        for nome in nomi:
            archivio.writestr(nome, "contenuto")
    return percorso


def test_pacchetto_pulito_accettato(tmp_path):
    zip_ = _crea_zip(tmp_path / "A.zip", ["A.ard", "X64Client/A.dll", "X64Client/lang/it.json"])
    assert copia_release.problemi_pacchetto(zip_) == []


@pytest.mark.parametrize("nome_vietato", [
    "X64Client/licenza.xei",
    "X64Client/A.pdb",
    "X64Client/A.obfuscation-map.xml",
    "src/Program.cs",
])
def test_pacchetto_con_file_vietati_rifiutato(tmp_path, nome_vietato):
    zip_ = _crea_zip(tmp_path / "A.zip", ["A.ard", nome_vietato])
    assert copia_release.problemi_pacchetto(zip_) == [nome_vietato]


def test_si_copia_solo_il_pacchetto_principale():
    with pytest.raises(ValueError):
        copia_release.controlla_nome_file("XEI.ItemGenerator_TEST.zip")
    with pytest.raises(ValueError):
        copia_release.controlla_nome_file("XEI.ItemGenerator.obfuscation-map.xml")
    copia_release.controlla_nome_file("XEI.ItemGenerator.zip")


def _voce(zip_):
    return copia_release.voce_addons(zip_, id_addon="prova", pacchetto="XEI.Prova", versione="2.0.1",
                                     data_rilascio="2026-11-02", origine="xei-software/xei-prova",
                                     tag_origine="v2.0.1")


def test_voce_per_addons_yml(tmp_path):
    zip_ = _crea_zip(tmp_path / "XEI.Prova.zip", ["XEI.Prova.ard"])
    voce = _voce(zip_)
    assert voce["tag_pubblico"] == "prova-v2.0.1"
    assert voce["file"] == "XEI.Prova.zip"
    assert voce["dimensione"] == zip_.stat().st_size
    assert len(voce["sha256"]) == 64
    assert voce["origine"] == "xei-software/xei-prova" and voce["tag_origine"] == "v2.0.1"


def test_pacchetto_identico_ad_addons_yml_verificato(tmp_path):
    zip_ = _crea_zip(tmp_path / "XEI.Prova.zip", ["XEI.Prova.ard"])
    copia_release.verifica_pacchetto(zip_, _voce(zip_))


def test_pacchetto_diverso_da_addons_yml_rifiutato(tmp_path):
    zip_ = _crea_zip(tmp_path / "XEI.Prova.zip", ["XEI.Prova.ard"])
    voce = _voce(zip_)
    _crea_zip(zip_, ["XEI.Prova.ard", "altro.txt"])  # il file cambia dopo aver scritto la voce
    with pytest.raises(SystemExit):
        copia_release.verifica_pacchetto(zip_, voce)


def test_pacchetto_con_file_vietati_non_verificato(tmp_path):
    zip_ = _crea_zip(tmp_path / "XEI.Prova.zip", ["XEI.Prova.ard", "licenza.xei"])
    with pytest.raises(SystemExit):
        copia_release.verifica_pacchetto(zip_, _voce(zip_))


def test_ogni_voce_di_addons_yml_indica_la_release_di_origine():
    for voce in yaml.safe_load(copia_release.ELENCO_ADDONS.read_text(encoding="utf-8")):
        assert voce["origine"].startswith("xei-software/")
        assert voce["tag_origine"] == f"v{voce['versione']}"
        assert copia_release.cerca_voce(voce["tag_pubblico"]) == voce
