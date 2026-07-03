"""
Teste pytest pentru clasa Echipa.

Testăm cele două excepții introduse:
    1. BugetInvalidError (excepție proprie) - la crearea unei echipe
       cu buget invalid.
    2. ZeroDivisionError (excepție standard) - la calculul mediei de
       puncte pentru o echipă fără meciuri jucate.
"""

import pytest

from echipe.echipa import Echipa, BugetInvalidError


def test_buget_invalid_ridica_exceptie_proprie():
    """Testează că se ridică BugetInvalidError pentru un buget <= 0."""
    with pytest.raises(BugetInvalidError):
        Echipa("Echipa Test", "Romania", buget=0)

    with pytest.raises(BugetInvalidError):
        Echipa("Echipa Test", "Romania", buget=-100.5)


def test_medie_puncte_fara_meciuri_ridica_zero_division_error():
    """Testează că se ridică ZeroDivisionError daca echipa nu a jucat meciuri."""
    echipa = Echipa("Echipa Test", "Romania", buget=100.0)

    assert echipa.meciuri_jucate == 0

    with pytest.raises(ZeroDivisionError):
        echipa.medie_puncte()


def test_echipa_valida_se_creeaza_corect():
    """Test suplimentar: o echipă cu date valide se creează fără erori."""
    echipa = Echipa("Real Madrid", "Spania", buget=950.5)

    assert echipa.nume == "Real Madrid"
    assert echipa.buget == 950.5
    assert echipa.puncte == 0


def test_adauga_rezultat_cu_goluri_negative_ridica_value_error():
    """Test suplimentar: goluri negative ridică ValueError (standard)."""
    echipa = Echipa("Real Madrid", "Spania", buget=950.5)

    with pytest.raises(ValueError):
        echipa.adauga_rezultat(-1, 2)
