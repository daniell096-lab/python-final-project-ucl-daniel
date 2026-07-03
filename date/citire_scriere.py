"""
Modul pentru operațiuni de citire și scriere în fișiere CSV (Tema 11).

- citeste_echipe_csv(): citește datele echipelor (nume, tara, buget)
  dintr-un fișier CSV, în locul unei liste hardcodate în cod.
- scrie_clasament_csv(): salvează clasamentul final al grupei
  într-un fișier CSV, pentru a putea fi păstrat/consultat ulterior.
"""

import csv
import os


class FisierEchipeInvalidError(Exception):
    """Excepție proprie: fișierul CSV cu echipe nu există sau e gol."""
    pass


def citeste_echipe_csv(cale_fisier):
    """Citește datele echipelor dintr-un fișier CSV.

    Fișierul trebuie să aibă coloanele: nume, tara, buget.
    Returnează o listă de tupluri (nume: str, tara: str, buget: float).
    """
    if not os.path.exists(cale_fisier):
        raise FisierEchipeInvalidError(f"Fisierul '{cale_fisier}' nu a fost gasit.")

    echipe = []
    with open(cale_fisier, mode="r", encoding="utf-8") as fisier_csv:
        cititor = csv.DictReader(fisier_csv)  # citește header-ul automat
        for rand in cititor:
            nume = rand["nume"]
            tara = rand["tara"]
            buget = float(rand["buget"])  # conversie string -> float
            echipe.append((nume, tara, buget))

    if not echipe:
        raise FisierEchipeInvalidError(f"Fisierul '{cale_fisier}' nu contine echipe.")

    return echipe


def scrie_clasament_csv(clasament, cale_fisier):
    """Salvează clasamentul final al grupei într-un fișier CSV.

    `clasament` este o listă de obiecte Echipa, deja sortată.
    Se scrie: poziție, nume, tara, puncte, goluri marcate/primite, golaveraj.
    """
    with open(cale_fisier, mode="w", newline="", encoding="utf-8") as fisier_csv:
        scriitor = csv.writer(fisier_csv)
        scriitor.writerow(
            ["pozitie", "nume", "tara", "puncte", "gol_marcate", "gol_primite", "golaveraj"]
        )

        pozitie = 1
        for echipa in clasament:
            scriitor.writerow(
                [
                    pozitie,
                    echipa.nume,
                    echipa.tara,
                    echipa.puncte,
                    echipa.gol_marcate,
                    echipa.gol_primite,
                    echipa.golaveraj(),
                ]
            )
            pozitie += 1

    print(f"Clasamentul a fost salvat in fisierul: {cale_fisier}")
