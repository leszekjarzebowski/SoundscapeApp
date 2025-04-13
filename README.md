------WAZNE------
Wytyczne dotyczące kodowania w projekcie:

1.  **Dokumentacja:** Kod piszemy wraz z dokumentacją w stylu Google Style.
2.  **Dobre praktyki:** Stosujemy ogólnie przyjęte zasady dobrego kodowania (np. SOLID, DRY, KISS), dbając o czystość, czytelność i utrzymywalność kodu.
3.  **Modularność i Niezależność:** Każda klasa powinna stanowić osobny, niezależny byt, odpowiedzialny za jedno konkretne zadanie (Zasada Pojedynczej Odpowiedzialności - SRP). Dążymy do minimalizowania powiązań między klasami.
4.  **Testowalność:** Niezależne klasy/moduły powinny być łatwe do testowania jednostkowego.
5.  **Separacja warstw:** Logika backendu (FastAPI, zarządzanie danymi, logika biznesowa) jest oddzielona od interfejsu użytkownika.
6.  **FastAPI jako "Dyspozytor":** Wykorzystujemy FastAPI jako "pomost" i "dyspozytora", który odbiera żądania i kieruje je do odpowiednich, niezależnych modułów/klas w celu wykonania operacji.
7.  **Walidacja danych:** Używamy Pydantic w FastAPI do definiowania schematów danych i ich walidacji.

---

🔄 UCS Integration – Plan i Ustalenia (2025-04-09)
Aplikacja soundscape_app będzie wykorzystywać system UCS (Universal Category System) do klasyfikacji dźwięków. Umożliwi to łatwe sortowanie, przeszukiwanie i przygotowanie danych do uczenia maszynowego.

✅ Główne ustalenia:
Aplikacja będzie mogła aktualizować UCS z pliku .xlsx (np. UCS v8.2.1 Full Translations.xlsx),

Plik UCS będzie przetwarzany do formatu .json i przechowywany w katalogu db/ucs.json,

W aplikacji będzie można wybierać kategorie po polsku, ale wewnętrznie system będzie używał angielskich nazw i CatID, zgodnie z UCS.

📁 Struktura projektu – bez zmian
Obecna struktura katalogów projektu soundscape_app pozostaje aktualna. Dodana zostanie tylko logika UCS.

📌 Plan TODO dla src/core/ucs.py:
UCSLoader – klasa do wczytywania i obsługi pliku UCS .xlsx

UCSCategory – opcjonalna klasa reprezentująca jedną kategorię

load_from_excel(filepath) – wczytanie i przetworzenie pliku Excel

save_to_json(filepath) – zapis przetworzonych danych do .json

load_from_json(filepath) – wczytanie danych z pliku .json

get_category(cat_id) – pobranie jednej kategorii po CatID

get_all_categories() – zwrócenie pełnej listy kategorii

get_catid_from_polish(category_pl, subcategory_pl) – mapowanie PL ➝ EN CatID (dla wygodnej pracy w języku polskim)
