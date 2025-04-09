------WAZNE------
Działające prototypy i testy znajdziesz w katalogu prototypes/
Opis prototypow w README_prototypes.md

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
