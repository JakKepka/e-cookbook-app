# E-Cookbook - Ekspercki Asystent Kuchenny

Aplikacja desktopowa działająca jako system ekspercki do wyszukiwania przepisów kulinarnych na podstawie dostępnych składników i preferencji użytkownika.

## Wymagania systemowe

- Python 3.8+
- SWI-Prolog
- PyQt5
- pyswip

## Instalacja

1. Zainstaluj SWI-Prolog ze strony https://www.swi-prolog.org/download/stable

2. Utwórz wirtualne środowisko Python i aktywuj je:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# lub
venv\Scripts\activate  # Windows
```

3. Zainstaluj wymagane pakiety Python:
```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji

```bash
python main.py
```

## Funkcje

- Wyszukiwanie przepisów na podstawie dostępnych składników
- Filtrowanie według typu diety (wegańska, wegetariańska, bezglutenowa)
- Określanie preferencji smakowych (słodkość, ostrość)
- Wybór okazji (śniadanie, obiad, kolacja, przekąska, impreza)
- Wybór poziomu trudności przepisu

## Struktura projektu

```
e_cookbook/
├── main.py                    # Aplikacja główna PyQt5
├── interface/                 # GUI (formularze, layouty)
├── prolog/                   # Fakty i reguły w Prologu
│   └── baza_wiedzy.pl
├── logic/                    # Obsługa komunikacji z Prologiem
│   └── prolog_connector.py
└── assets/                   # Ikony, grafiki
```

## Rozwijanie bazy wiedzy

Baza wiedzy w Prologu (`e_cookbook/prolog/baza_wiedzy.pl`) zawiera:
- Definicje przepisów
- Reguły dopasowywania
- Alternatywne składniki
- Reguły dietetyczne

Aby dodać nowy przepis, należy dodać fakt w formacie:
```prolog
przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki).
```
