"""
Modul cu clasa Grupa (Tema 13 - Refactorizare POO).

Înainte, logica unei grupe din Champions League era împrăștiată în mai
multe funcții independente, apelate una câte una din main.py, iar lista
de echipe circula liber între ele ca parametru. Clasa Grupa încapsulează
toate acestea: își gestionează propria listă de echipe (self.echipe) ca
stare internă și oferă metode care operează asupra acestei stări
(încarcă echipe, simulează meciuri, calculează clasament, salvează
rezultate) - unul dintre principiile de bază ale POO: încapsularea.
"""

from echipe.echipa import Echipa, BugetInvalidError
from meciuri.simulator import simuleaza_grupa
from utile.statistici import (
    afiseaza_clasament,
    tari_participante,
    statistici_pe_tara,
    nume_echipe_calificate,
)
from date.citire_scriere import citeste_echipe_csv, scrie_clasament_csv


class Grupa:
    """Reprezintă o grupă din UEFA Champions League.

    Atribute:
        nume_grupa (str): identificatorul grupei, ex: "Grupa A".
        echipe (list): lista obiectelor Echipa din grupă (stare internă,
            encapsulată - restul aplicației nu manipulează direct listele
            de echipe, ci doar prin metodele clasei Grupa).
    """

    def __init__(self, nume_grupa):
        self.nume_grupa = nume_grupa  # string
        self.echipe = []              # listă de obiecte Echipa

    def adauga_echipa(self, echipa):
        """Adaugă o echipă (obiect Echipa) în grupă."""
        self.echipe.append(echipa)

    def incarca_echipe_din_csv(self, cale_fisier):
        """Populează grupa citind echipele dintr-un fișier CSV.

        Tratează excepția proprie BugetInvalidError: echipele cu buget
        invalid sunt ignorate, restul grupei rămâne neafectat.
        """
        date_echipe = citeste_echipe_csv(cale_fisier)
        for nume, tara, buget in date_echipe:
            try:
                self.adauga_echipa(Echipa(nume, tara, buget))
            except BugetInvalidError as eroare:
                print(f"Echipa ignorata din cauza unui buget invalid: {eroare}")

    def simuleaza(self, numar_runde=3, punctaj_calificare=4):
        """Simulează meciurile grupei și stabilește echipele calificate."""
        self.echipe = simuleaza_grupa(self.echipe, numar_runde)
        self._verifica_calificare(punctaj_calificare)

    def _verifica_calificare(self, punctaj_minim):
        """Metodă internă: marchează echipele calificate mai departe."""
        for echipa in self.echipe:
            echipa.calificata = echipa.puncte >= punctaj_minim

    def clasament(self):
        """Afișează și returnează clasamentul grupei, sortat."""
        return afiseaza_clasament(self.echipe)

    def salveaza_clasament(self, cale_fisier):
        """Salvează clasamentul curent al grupei într-un fișier CSV."""
        clasament_curent = self.clasament()
        scrie_clasament_csv(clasament_curent, cale_fisier)

    def echipe_calificate_nume(self):
        """Returnează numele echipelor calificate (Lambda + filter + map)."""
        return nume_echipe_calificate(self.echipe)

    def tari(self):
        """Returnează setul de țări prezente în grupă."""
        return tari_participante(self.echipe)

    def echipe_pe_tara(self):
        """Returnează dicționarul cu echipele grupate pe țară."""
        return statistici_pe_tara(self.echipe)

    def __len__(self):
        """Permite folosirea len(grupa) pentru numărul de echipe."""
        return len(self.echipe)

    def __repr__(self):
        return f"Grupa '{self.nume_grupa}' - {len(self.echipe)} echipe"
