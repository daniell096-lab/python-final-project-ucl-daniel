"""
Modul cu datele "brute" ale echipelor din grupa simulată.

Fiecare echipă este reprezentată printr-un tuplu:
    (nume: str, tara: str, buget: float)

Folosim un tuplu deoarece aceste date sunt fixe și nu trebuie
modificate pe parcursul programului (sunt imutabile).
"""

ECHIPE_GRUPA = [
    ("Real Madrid", "Spania", 950.5),
    ("Manchester City", "Anglia", 900.0),
    ("Bayern Munchen", "Germania", 800.25),
    ("Inter Milano", "Italia", 650.75),
]
