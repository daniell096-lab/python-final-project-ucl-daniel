"""
Teste pytest pentru clasa Grupa (Tema 13 - refactorizare POO).
"""

from meciuri.grupa import Grupa
from echipe.echipa import Echipa


def test_grupa_se_creeaza_goala():
    """O grupă nou creată nu are echipe."""
    grupa = Grupa("Grupa Test")

    assert grupa.nume_grupa == "Grupa Test"
    assert len(grupa) == 0


def test_adauga_echipa_in_grupa():
    """adauga_echipa() adaugă o echipă în lista internă a grupei."""
    grupa = Grupa("Grupa Test")
    echipa = Echipa("Real Madrid", "Spania", buget=950.5)

    grupa.adauga_echipa(echipa)

    assert len(grupa) == 1
    assert grupa.echipe[0].nume == "Real Madrid"
