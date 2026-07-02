"""
UEFA Champions League - Simulator de grupă
===========================================

Punctul de intrare al aplicației. Creează echipele din grupă, simulează
meciurile și afișează clasamentul final, împreună cu câteva statistici
suplimentare (țările implicate și echipele grupate pe țară).
"""

from echipe.echipa import Echipa
from meciuri.simulator import simuleaza_grupa
from utile.statistici import afiseaza_clasament, tari_participante, statistici_pe_tara
from date.echipe_date import ECHIPE_GRUPA


def creeaza_echipe(date_echipe):
    """Transformă lista de tupluri (nume, tara, buget) în obiecte Echipa."""
    echipe = []
    for nume, tara, buget in date_echipe:  # for peste o listă de tupluri
        echipa_noua = Echipa(nume, tara, buget)
        echipe.append(echipa_noua)
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

    echipe = creeaza_echipe(ECHIPE_GRUPA)
    numar_runde = 3  # integer

    echipe = simuleaza_grupa(echipe, numar_runde)
    verifica_calificare(echipe)

    afiseaza_clasament(echipe)

    tari = tari_participante(echipe)
    print(f"\nȚări prezente în grupă ({len(tari)}): {tari}")

    pe_tara = statistici_pe_tara(echipe)
    print("\nEchipe grupate pe țară:")
    for tara, nume_echipe in pe_tara.items():
        print(f"  {tara}: {nume_echipe}")


if __name__ == "__main__":
    main()
