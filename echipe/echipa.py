"""
Modul care definește clasa Echipa.

O echipă din UEFA Champions League are un nume, o țară, un buget (folosit
pentru simularea forței echipei) și statistici acumulate pe parcursul
grupei: puncte, goluri marcate, goluri primite, meciuri jucate.
"""


class Echipa:
    """Reprezintă o echipă înscrisă în UEFA Champions League.

    Atribute:
        nume (str): numele echipei, ex: "Real Madrid".
        tara (str): țara din care provine echipa.
        buget (float): bugetul echipei, în milioane de euro.
        calificata (bool): dacă echipa e calificată în grupe.
        puncte (int): puncte acumulate in grupa.
        gol_marcate (int): goluri marcate.
        gol_primite (int): goluri primite.
        meciuri_jucate (int): numărul de meciuri disputate.
    """

    def __init__(self, nume, tara, buget, calificata=True):
        self.nume = nume                # string
        self.tara = tara                # string
        self.buget = buget              # float
        self.calificata = calificata    # boolean
        self.puncte = 0                 # integer
        self.gol_marcate = 0
        self.gol_primite = 0
        self.meciuri_jucate = 0

    def adauga_rezultat(self, goluri_marcate, goluri_primite):
        """Actualizează statisticile echipei după un meci disputat."""
        self.meciuri_jucate += 1
        self.gol_marcate += goluri_marcate
        self.gol_primite += goluri_primite

        # Se acordă puncte în funcție de rezultatul meciului
        if goluri_marcate > goluri_primite:
            self.puncte += 3
        elif goluri_marcate == goluri_primite:
            self.puncte += 1
        # dacă a pierdut, nu se adaugă puncte

    def golaveraj(self):
        """Returnează golaverajul echipei (int)."""
        return self.gol_marcate - self.gol_primite

    def __repr__(self):
        return f"{self.nume} ({self.tara}) - {self.puncte} pct"
