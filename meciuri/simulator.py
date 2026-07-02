"""
Modul responsabil cu simularea meciurilor din grupa de Champions League.

Scorul unui meci este generat pseudo-aleator, dar influențat de bugetul
fiecărei echipe (o echipă cu buget mai mare are șanse mai mari să
marcheze mai multe goluri).
"""

import random


def genereaza_perechi(lista_echipe):
    """Generator (concept din Lecția 12: Iterator vs. Generator).

    În loc să construim o listă completă cu toate perechile de echipe
    (gazdă, oaspete) și să o ținem în memorie, folosim `yield` pentru a
    "produce" o pereche la fiecare pas al iterării. Astfel valorile sunt
    generate una câte una, la cerere (lazy evaluation), nu toate deodată.
    """
    for i in range(len(lista_echipe) - 1):
        gazda = lista_echipe[i]
        oaspete = lista_echipe[i + 1]
        yield (gazda, oaspete)  # yield in loc de return -> functia devine generator


def simuleaza_meci(echipa_gazda, echipa_oaspete):
    """Simulează un meci între două obiecte de tip Echipa.

    Returnează un tuplu (goluri_gazda, goluri_oaspete).
    """
    # Raportul bugetelor influențează numărul maxim de goluri posibile
    raport = echipa_gazda.buget / echipa_oaspete.buget

    max_goluri_gazda = 4 if raport >= 1 else 3
    max_goluri_oaspete = 4 if raport < 1 else 3

    goluri_gazda = random.randint(0, max_goluri_gazda)
    goluri_oaspete = random.randint(0, max_goluri_oaspete)

    return (goluri_gazda, goluri_oaspete)  # tuplu


def simuleaza_grupa(lista_echipe, numar_runde=3):
    """Simulează mai multe runde de meciuri pentru o listă de echipe.

    Folosește o buclă WHILE pentru rundele jucate și o buclă FOR pentru
    a parcurge perechile de echipe din fiecare rundă.
    """
    runda_curenta = 0

    while runda_curenta < numar_runde:
        # Folosim generatorul genereaza_perechi() in locul unei liste
        # intermediare cu toate perechile - valorile sunt produse pe rand
        for gazda, oaspete in genereaza_perechi(lista_echipe):
            gg, go = simuleaza_meci(gazda, oaspete)
            gazda.adauga_rezultat(gg, go)
            oaspete.adauga_rezultat(go, gg)

        runda_curenta += 1

    return lista_echipe
