"""
Modul care definește clasa Echipa.

O echipă din UEFA Champions League are un nume, o țară, un buget (folosit
pentru simularea forței echipei) și statistici acumulate pe parcursul
grupei: puncte, goluri marcate, goluri primite, meciuri jucate.
"""


class BugetInvalidError(Exception):
    """Excepție proprie (custom).

    Se ridică atunci când se încearcă crearea unei echipe cu un buget
    invalid (mai mic sau egal cu 0), situație care nu are sens din punct
    de vedere logic - o echipă din Champions League nu poate avea un
    buget nul sau negativ.
    """
    pass


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
        # Vulnerabilitate: fara aceasta verificare, un buget <= 0 ar trece
        # neobservat si ar produce mai tarziu o ZeroDivisionError greu de
        # depistat in meciuri/simulator.py (la calculul raportului bugetelor)
        if buget <= 0:
            raise BugetInvalidError(
                f"Bugetul echipei '{nume}' trebuie sa fie pozitiv, primit: {buget}"
            )

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
        # Vulnerabilitate: fara aceasta verificare s-ar putea introduce
        # scoruri negative, imposibile intr-un meci real de fotbal
        if goluri_marcate < 0 or goluri_primite < 0:
            raise ValueError("Numarul de goluri nu poate fi negativ.")

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

    def medie_puncte(self):
        """Returnează media de puncte pe meci disputat.

        Vulnerabilitate: daca echipa nu a jucat inca niciun meci,
        impartirea self.puncte / self.meciuri_jucate ridica in mod
        natural excepția standard ZeroDivisionError. Functia nu prinde
        aceasta eroare intern, ci o lasa sa se propage - apelantul este
        responsabil sa o trateze (vezi exemplu in main.py).
        """
        return self.puncte / self.meciuri_jucate

    def __repr__(self):
        return f"{self.nume} ({self.tara}) - {self.puncte} pct"

