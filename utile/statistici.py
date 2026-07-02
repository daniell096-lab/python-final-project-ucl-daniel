"""
Modul cu funcții auxiliare pentru afișarea clasamentului și a unor
statistici legate de țările prezente în grupă.
"""


def afiseaza_clasament(lista_echipe):
    """Afișează clasamentul echipelor, sortat după puncte și golaveraj."""
    clasament = sorted(
        lista_echipe,
        key=lambda echipa: (echipa.puncte, echipa.golaveraj()),
        reverse=True,
    )

    print("\n--- CLASAMENT GRUPĂ ---")
    pozitie = 1  # integer

    # Buclă FOR pentru afișarea fiecărei echipe din clasament
    for echipa in clasament:
        calificare_text = "DA" if echipa.calificata else "NU"
        print(
            f"{pozitie}. {echipa.nume:<18} "
            f"Pct: {echipa.puncte:<3} "
            f"GM: {echipa.gol_marcate:<3} "
            f"GP: {echipa.gol_primite:<3} "
            f"Golaveraj: {echipa.golaveraj():<3} "
            f"Calificată: {calificare_text}"
        )
        pozitie += 1

    return clasament


def echipe_calificate(lista_echipe):
    """Funcție Lambda (concept din Lecția 12) folosită împreună cu filter().

    filter() păstrează doar echipele pentru care funcția Lambda
    returnează True (adică echipele calificate mai departe).
    """
    calificate = filter(lambda echipa: echipa.calificata, lista_echipe)
    return list(calificate)


def nume_echipe_calificate(lista_echipe):
    """Funcție Lambda folosită împreună cu map().

    map() aplică funcția Lambda pe fiecare echipă calificată și
    extrage doar numele acesteia (string).
    """
    calificate = echipe_calificate(lista_echipe)
    return list(map(lambda echipa: echipa.nume, calificate))


def tari_participante(lista_echipe):
    """Returnează un SET cu țările unice prezente în grupă (fără duplicate)."""
    tari = set()
    for echipa in lista_echipe:
        tari.add(echipa.tara)
    return tari


def statistici_pe_tara(lista_echipe):
    """Construiește un DICTIONAR: țară -> lista echipelor din acea țară."""
    statistici = {}
    for echipa in lista_echipe:
        if echipa.tara not in statistici:
            statistici[echipa.tara] = []
        statistici[echipa.tara].append(echipa.nume)
    return statistici
