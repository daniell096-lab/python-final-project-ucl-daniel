"""
Modul pentru Tema 12: clasă abstractă și moștenire.

Context în proiectul UEFA Champions League: echipele călătoresc la
meciurile din deplasare cu diverse mijloace de transport. Modelăm acest
lucru printr-o clasă abstractă MijlocDeTransport și o clasă copil
concretă, Avion (cel mai folosit mijloc de transport de echipele de
fotbal pentru deplasările din cupele europene).
"""

from abc import ABC, abstractmethod


class MijlocDeTransport(ABC):
    """Clasă abstractă pentru un mijloc de transport.

    Atribute de clasă:
        categorie (str): categoria mijlocului de transport
            (ex: "aerian", "terestru", "naval"). Valoare implicită "".

    Metode abstracte:
        se_deplaseaza(): trebuie implementată de orice clasă copil.
    """

    categorie = ""  # atribut de clasa, valoare default empty string

    @abstractmethod
    def se_deplaseaza(self):
        """Metodă abstractă - descrie modul de deplasare al mijlocului de transport."""
        pass


class Avion(MijlocDeTransport):
    """Clasă copil - reprezintă un avion folosit de o echipă pentru deplasare."""

    categorie = "aerian"  # se suprascrie atributul de clasa mostenit

    def __init__(self, denumire, kilometraj):
        self.denumire = denumire      # atribut de instanta, string
        self.kilometraj = kilometraj  # atribut de instanta, float

    def se_deplaseaza(self):
        """Suprascrie metoda abstractă din clasa părinte MijlocDeTransport."""
        print(
            f"{self.denumire} (categorie: {self.categorie}) se deplaseaza "
            f"pe cale aeriana, parcurgand {self.kilometraj} km."
        )


if __name__ == "__main__":
    # Cerinta 3: cream un obiect al clasei copil si apelam metoda abstracta suprascrisa
    avion_echipa = Avion("Airbus A320 - Real Madrid", 1450.0)
    avion_echipa.se_deplaseaza()
