"""
UEFA Champions League - Simulator de grupă
===========================================

Punctul de intrare al aplicației. Creează echipele din grupă, simulează
meciurile și afișează clasamentul final, împreună cu câteva statistici
suplimentare (țările implicate și echipele grupate pe țară).
"""

from echipe.echipa import Echipa, BugetInvalidError
from meciuri.simulator import simuleaza_grupa
from utile.statistici import (
    afiseaza_clasament,
    tari_participante,
    statistici_pe_tara,
    echipe_calificate,
    nume_echipe_calificate,
)
from date.citire_scriere import citeste_echipe_csv, scrie_clasament_csv, FisierEchipeInvalidError


def creeaza_echipe(date_echipe):
    """Transformă lista de tupluri (nume, tara, buget) în obiecte Echipa.

    Tratează excepția proprie BugetInvalidError: dacă o echipă are un
    buget invalid, este ignorată, iar programul continuă cu restul.
    """
    echipe = []
    for nume, tara, buget in date_echipe:  # for peste o listă de tupluri
        try:
            echipa_noua = Echipa(nume, tara, buget)
            echipe.append(echipa_noua)
        except BugetInvalidError as eroare:
            print(f"Echipa ignorata din cauza unui buget invalid: {eroare}")
    return echipe


def verifica_calificare(lista_echipe, punctaj_minim=4):
    """Marchează cu bool True/False dacă o echipă s-a calificat mai departe."""
    for echipa in lista_echipe:
        # O echipă e considerată calificată dacă are cel puțin punctaj_minim puncte
        if echipa.puncte >= punctaj_minim:
            echipa.calificata = True
        else:
            echipa.calificata = False


def main():
    """Funcția principală a programului."""
    print("=== SIMULARE GRUPĂ UEFA CHAMPIONS LEAGUE ===")

    try:
        date_echipe = citeste_echipe_csv("date/echipe.csv")
    except FisierEchipeInvalidError as eroare:
        print(f"Eroare la citirea fisierului cu echipe: {eroare}")
        return

    echipe = creeaza_echipe(date_echipe)
    numar_runde = 3  # integer

    echipe = simuleaza_grupa(echipe, numar_runde)
    verifica_calificare(echipe)

    clasament = afiseaza_clasament(echipe)
    scrie_clasament_csv(clasament, "date/clasament_final.csv")

    tari = tari_participante(echipe)
    print(f"\nȚări prezente în grupă ({len(tari)}): {tari}")

    pe_tara = statistici_pe_tara(echipe)
    print("\nEchipe grupate pe țară:")
    for tara, nume_echipe in pe_tara.items():
        print(f"  {tara}: {nume_echipe}")

    # Concept L12 - Funcții Lambda (folosite intern cu filter() si map())
    nume_calificate = nume_echipe_calificate(echipe)
    print(f"\nEchipe calificate mai departe (Lambda + filter + map): {nume_calificate}")

    # Tratarea excepției standard ZeroDivisionError: se poate produce
    # daca o echipa nu a jucat niciun meci (impartire la 0 in medie_puncte())
    print("\nMedie puncte/meci:")
    for echipa in echipe:
        try:
            medie = echipa.medie_puncte()
            print(f"  {echipa.nume}: {medie:.2f}")
        except ZeroDivisionError:
            print(f"  {echipa.nume}: nu are meciuri jucate, media nu poate fi calculata")


if __name__ == "__main__":
    main()
