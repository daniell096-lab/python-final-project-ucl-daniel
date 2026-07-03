"""
UEFA Champions League - Simulator de grupă
===========================================

Punctul de intrare al aplicației. Creează un obiect Grupa, îl populează
cu echipe citite dintr-un fișier CSV, simulează meciurile și afișează
clasamentul final, împreună cu câteva statistici suplimentare.

Tema 13 - Refactorizare POO: logica specifică unei grupe (echipe,
simulare, clasament, calificare, salvare) este încapsulată în clasa
Grupa (meciuri/grupa.py), în loc să fie împrăștiată în funcții
independente apelate direct aici.
"""

from meciuri.grupa import Grupa
from date.citire_scriere import FisierEchipeInvalidError


def main():
    """Funcția principală a programului."""
    print("=== SIMULARE GRUPĂ UEFA CHAMPIONS LEAGUE ===")

    # Instanțierea clasei Grupa (Tema 13)
    grupa_a = Grupa("Grupa A")

    try:
        grupa_a.incarca_echipe_din_csv("date/echipe.csv")
    except FisierEchipeInvalidError as eroare:
        print(f"Eroare la citirea fisierului cu echipe: {eroare}")
        return

    print(grupa_a)  # foloseste __repr__ din clasa Grupa

    grupa_a.simuleaza(numar_runde=3, punctaj_calificare=4)
    grupa_a.salveaza_clasament("date/clasament_final.csv")

    tari = grupa_a.tari()
    print(f"\nȚări prezente în grupă ({len(tari)}): {tari}")

    pe_tara = grupa_a.echipe_pe_tara()
    print("\nEchipe grupate pe țară:")
    for tara, nume_echipe in pe_tara.items():
        print(f"  {tara}: {nume_echipe}")

    # Concept L12 - Funcții Lambda (folosite intern cu filter() si map())
    nume_calificate = grupa_a.echipe_calificate_nume()
    print(f"\nEchipe calificate mai departe (Lambda + filter + map): {nume_calificate}")

    # Tratarea excepției standard ZeroDivisionError: se poate produce
    # daca o echipa nu a jucat niciun meci (impartire la 0 in medie_puncte())
    print("\nMedie puncte/meci:")
    for echipa in grupa_a.echipe:
        try:
            medie = echipa.medie_puncte()
            print(f"  {echipa.nume}: {medie:.2f}")
        except ZeroDivisionError:
            print(f"  {echipa.nume}: nu are meciuri jucate, media nu poate fi calculata")


if __name__ == "__main__":
    main()
