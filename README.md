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
│   ├── simulator.py           # simularea meciurilor / grupei
│   └── grupa.py                # clasa Grupa (Tema 13)
├── utile/
│   ├── __init__.py
│   └── statistici.py         # clasament, statistici pe țară
├── date/
│   ├── echipe.csv             # datele echipelor (citire CSV)
│   ├── clasament_final.csv    # clasament salvat (scriere CSV, generat la rulare)
│   └── citire_scriere.py      # funcțiile de citire/scriere CSV
├── transport/
│   ├── __init__.py
│   └── mijloc_transport.py    # clasa abstractă MijlocDeTransport + Avion
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

## Tema 12 - Clasă abstractă și moștenire

Implementate în `transport/mijloc_transport.py`:

1. **Clasa abstractă `MijlocDeTransport`** — atribut de clasă
   `categorie = ""` și metoda abstractă `se_deplaseaza()`.
2. **Clasa copil `Avion`** — moștenește `MijlocDeTransport`, suprascrie
   `categorie = "aerian"` și metoda `se_deplaseaza()`; are în
   constructor atributele de instanță `denumire` și `kilometraj`.
3. **Demo** — la finalul fișierului se creează un obiect `Avion` și se
   apelează `se_deplaseaza()`.

Rulare:

```
python3 transport/mijloc_transport.py
```

## Tema 13 - Refactorizare POO

**Clasa creată: `Grupa`** (`meciuri/grupa.py`).

**Scopul ei:** înainte, o "grupă" din Champions League era doar o listă
simplă de obiecte `Echipa`, iar toată logica (simulare, clasament,
calificare, salvare CSV) exista sub formă de funcții separate, apelate
direct din `main.py` cu lista de echipe drept parametru. Clasa `Grupa`
încapsulează această listă ca stare internă (`self.echipe`) și oferă
metode dedicate care operează asupra ei: `incarca_echipe_din_csv()`,
`simuleaza()`, `clasament()`, `salveaza_clasament()`,
`echipe_calificate_nume()`, `tari()`, `echipe_pe_tara()`. Astfel,
`main.py` nu mai manipulează direct liste și funcții împrăștiate, ci
lucrează cu un singur obiect coerent, cu comportament propriu (inclusiv
metodele speciale `__len__` și `__repr__`).

`main.py` instanțiază clasa astfel:

```python
grupa_a = Grupa("Grupa A")
grupa_a.incarca_echipe_din_csv("date/echipe.csv")
grupa_a.simuleaza(numar_runde=3)
```
