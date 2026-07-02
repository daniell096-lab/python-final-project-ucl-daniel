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
│   └── echipa.py             # clasa Echipa
├── meciuri/
│   ├── __init__.py
│   └── simulator.py          # simularea meciurilor / grupei
├── utile/
│   ├── __init__.py
│   └── statistici.py         # clasament, statistici pe țară
└── date/
    └── echipe_date.py        # datele echipelor (nume, țară, buget)
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
