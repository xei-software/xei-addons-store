"""Fixture comuni dei test."""
import pytest

import build


@pytest.fixture(scope="module")
def tutti_attivi():
    """Riaccende le voci spente («attivo: false») di addons.yml.

    Serve ai test che provano il generatore con i programmi veri come esempio: restano validi anche quando un
    programma è spento sul sito (per esempio durante un controllo).
    """
    originale = build.carica_voci
    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(build, "carica_voci",
                      lambda: [{k: v for k, v in voce.items() if k != "attivo"} for voce in originale()])
        yield
