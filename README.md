# UEFA Champions League - Simulator de grupă

Proiect Python care simulează o grupă din UEFA Champions League: creează
echipe, simulează meciuri pe mai multe runde, calculează clasamentul și
afișează statistici despre echipele participante.

## Structura proiectului

```
ucl_project/
├── main.py                  # punctul de intrare al aplicației
├── echipe/
│   ├── __init__.py
│   └── echipa.py             # clasa Echipa + BugetInvalidError
├── meciuri/
│   ├── __init__.py
│   └── simulator.py          # simularea meciurilor / grupei
├── utile/
│   ├── __init__.py
│   └── statistici.py         # clasament, statistici pe țară
├── date/
│   ├── echipe.csv             # datele echipelor (citire CSV)
│   ├── clasament_final.csv    # clasament salvat (scriere CSV, generat la rulare)
│   └── citire_scriere.py      # funcțiile de citire/scriere CSV
└── tests/
    ├── __init__.py
    └── test_echipa.py         # teste pytest
```

## Rulare

```
python3 main.py
```

## Concepte folosite

- **Tipuri de date:** `int` (puncte, goluri), `float` (buget), `str` (nume,
  țară), `bool` (calificare).
- **Structuri de control:** `if/elif/else`, `while` (runde), `for`
  (parcurgerea echipelor).
- **Structuri de date:** `list` (echipe), `tuple` (date echipă, scor meci),
  `dict` (echipe pe țară), `set` (țări unice).

## Concepte din Lecția 12

1. **Funcții Lambda** — `utile/statistici.py`, funcțiile
   `echipe_calificate()` (folosește `filter(lambda ...)`) și
   `nume_echipe_calificate()` (folosește `map(lambda ...)`). De asemenea,
   `afiseaza_clasament()` folosește o funcție Lambda ca `key` pentru
   `sorted()`.
2. **Generator (`yield`)** — `meciuri/simulator.py`, funcția
   `genereaza_perechi()` produce perechile de echipe (gazdă, oaspete)
   pe rând, folosind `yield`, în loc să construiască o listă completă
   în memorie.

## Tema 10 - Excepții și teste

**Excepții folosite:**

1. **Excepție proprie: `BugetInvalidError`** (`echipe/echipa.py`) —
   ridicată la crearea unei `Echipa` cu buget invalid (≤ 0). Tratată în
   `main.py`, în `creeaza_echipe()`, printr-un bloc `try/except`.
2. **Excepție standard: `ZeroDivisionError`** — ridicată în mod natural
   de `Echipa.medie_puncte()` dacă echipa nu a jucat niciun meci
   (împărțire la 0). Tratată în `main.py` printr-un bloc `try/except`.

Bonus: `ValueError` (standard) este ridicată în `adauga_rezultat()`
dacă se introduc goluri negative.

**Teste `pytest`** — în `tests/test_echipa.py`:
- `test_buget_invalid_ridica_exceptie_proprie`
- `test_medie_puncte_fara_meciuri_ridica_zero_division_error`
- (plus 2 teste suplimentare de bonus)

Rulare teste:

```
pip install pytest
python3 -m pytest tests/ -v
```

## Tema 11 - Citire/scriere fișiere

Implementate în `date/citire_scriere.py`:

1. **Citire dintr-un fișier CSV** — `citeste_echipe_csv()` citește
   datele echipelor (nume, țară, buget) din `date/echipe.csv`, în locul
   unei liste hardcodate în cod sursă.
2. **Scriere într-un fișier CSV** — `scrie_clasament_csv()` salvează
   clasamentul final al grupei (poziție, echipă, puncte, goluri,
   golaveraj) în `date/clasament_final.csv`, la finalul fiecărei rulări
   a lui `main.py`.

Ambele operațiuni sunt protejate: dacă fișierul `echipe.csv` lipsește
sau e gol, se ridică excepția proprie `FisierEchipeInvalidError`,
tratată în `main.py`.
