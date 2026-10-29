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


def test_elenco_dei_tag_pubblici(tmp_path):
    elenco = tmp_path / "addons.yml"
    elenco.write_text("- tag_pubblico: a-v1.0.0\n- tag_pubblico: b-v2.1.0\n", encoding="utf-8")
    assert copia_release.tag_pubblici(elenco) == ["a-v1.0.0", "b-v2.1.0"]


def test_versione_xeicore_letta_dal_progetto():
    csproj = '<Project><ItemGroup><PackageReference Include="XEICore" Version="1.1.1" /></ItemGroup></Project>'
    assert copia_release.versione_xeicore(csproj) == "1.1.1"
    with pytest.raises(SystemExit):
        copia_release.versione_xeicore("<Project></Project>")


def test_xeicore_del_progetto_deve_coincidere(tmp_path):
    zip_ = _crea_zip(tmp_path / "XEI.Prova.zip", ["XEI.Prova.ard"])
    voce = {**_voce(zip_), "xeicore": "1.1.1"}
    copia_release.verifica_xeicore(voce, "1.1.1")
    with pytest.raises(SystemExit):
        copia_release.verifica_xeicore(voce, "1.0.7")


def test_il_progetto_si_legge_dal_tag_anche_se_esiste_un_ramo_con_lo_stesso_nome(monkeypatch):
    # Nei repository degli add-on può esistere un ramo "v1.5.0": con ref=v1.5.0 GitHub legge il ramo, non il tag.
    import subprocess
    from strumenti import copia_release
    chiamate = []

    def finto_run(argomenti, **opzioni):
        chiamate.append(argomenti)
        return subprocess.CompletedProcess(argomenti, 0, stdout="<Project />", stderr="")

    monkeypatch.setattr(copia_release.subprocess, "run", finto_run)
    copia_release.leggi_csproj("xei-software/xei-itemgenerator", "v1.5.0", "XEI.ItemGenerator")
    assert chiamate[0][-1] == "repos/xei-software/xei-itemgenerator/contents/XEI.ItemGenerator.csproj?ref=refs/tags/v1.5.0"


def test_versione_del_framework_delle_app():
    from strumenti import copia_release
    props = '<Project><PropertyGroup>\n    <XeiFrameworkVersion>0.7.0</XeiFrameworkVersion>\n</PropertyGroup></Project>'
    assert copia_release.versione_framework(props) == "0.7.0"
    with pytest.raises(SystemExit):
        copia_release.versione_framework("<Project />")


def test_per_un_app_si_controlla_il_framework_e_non_xeicore():
    from strumenti import copia_release
    voce = {"tag_pubblico": "rate-updater-v1.0.0", "tipo": "app", "framework": "0.7.0"}
    copia_release.verifica_framework(voce, "0.7.0")
    with pytest.raises(SystemExit):
        copia_release.verifica_framework(voce, "0.7.1")


def test_il_file_delle_versioni_dell_app_si_legge_dal_tag(monkeypatch):
    import subprocess
    from strumenti import copia_release
    chiamate = []
    monkeypatch.setattr(copia_release.subprocess, "run",
                        lambda argomenti, **opzioni: chiamate.append(argomenti) or
                        subprocess.CompletedProcess(argomenti, 0, stdout="<Project />", stderr=""))
    copia_release.leggi_file_del_tag("xei-software/xei-rateupdater", "v1.0.0", "Directory.Packages.props")
    assert chiamate[0][-1] == "repos/xei-software/xei-rateupdater/contents/Directory.Packages.props?ref=refs/tags/v1.0.0"


def test_nello_zip_di_un_app_non_vanno_dati_locali_e_segreti(tmp_path):
    from strumenti import copia_release
    zip_app = tmp_path / "XEI.RateUpdater.zip"
    vietati = ["appsettings.Development.json", "impostazioni.json", "XEI.RateUpdater.csproj.user", "logs/oggi.txt",
               "app.log", "chiavi/chiave.bin", "users.json", "sessions/a.json", "licenza.xei"]
    ammessi = ["XEI.RateUpdater.exe", "XEI.App.Server.dll", "wwwroot/index.html", "lang/it.json", "appsettings.json"]
    with zipfile.ZipFile(zip_app, "w") as archivio:
        for nome in vietati + ammessi:
            archivio.writestr(nome, "x")
    assert sorted(copia_release.problemi_pacchetto(zip_app)) == sorted(vietati)
