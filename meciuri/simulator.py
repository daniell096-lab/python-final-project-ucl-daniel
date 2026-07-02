"""
Modul responsabil cu simularea meciurilor din grupa de Champions League.

Scorul unui meci este generat pseudo-aleator, dar influențat de bugetul
fiecărei echipe (o echipă cu buget mai mare are șanse mai mari să
marcheze mai multe goluri).
"""

import random


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
        # Se parcurg echipele două câte două (gazdă - oaspete)
        for i in range(len(lista_echipe) - 1):
            gazda = lista_echipe[i]
            oaspete = lista_echipe[i + 1]

            gg, go = simuleaza_meci(gazda, oaspete)
            gazda.adauga_rezultat(gg, go)
            oaspete.adauga_rezultat(go, gg)

        runda_curenta += 1

    return lista_echipe
