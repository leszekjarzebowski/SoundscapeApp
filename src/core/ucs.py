# TODO: Klasa UCSLoader
# - odpowiedzialna za wczytywanie pliku UCS w formacie .xlsx
# - przetwarza dane do postaci listy obiektów kategorii (lub słowników)
# - zapisuje dane do formatu .json (np. db/ucs.json)

# TODO: Klasa UCSCategory (opcjonalna)
# - reprezentuje jedną kategorię UCS
# - zawiera: CatID, Category, SubCategory, Description, Synonyms, Translations
# - może mieć metodę do eksportu do dict (dla JSON)

# TODO: Metoda load_from_excel(filepath)
# - wczytuje arkusz XLSX z UCS (np. wersja 8.2.1)
# - odfiltrowuje nagłówki, nieistotne wiersze
# - zwraca listę UCSCategory lub słowników

# TODO: Metoda save_to_json(filepath)
# - zapisuje przetworzone dane do JSON (np. db/ucs.json)

# TODO: Metoda load_from_json(filepath)
# - ładuje zapisany wcześniej plik JSON z kategoriami
# - umożliwia pracę bez konieczności parsowania XLS za każdym razem

# TODO: Metoda get_category(cat_id)
# - zwraca dane jednej kategorii (lub None) na podstawie `CatID`

# TODO: Metoda get_all_categories()
# - zwraca listę wszystkich kategorii jako obiekty lub słowniki

# TODO: (opcjonalnie) Wersjonowanie
# - odczytaj wersję UCS z nagłówka arkusza lub podaj ręcznie
# - dodaj do JSON pole "version"
# TODO: Metoda get_catid_from_polish(category_pl, subcategory_pl)
# - umożliwia wybór kategorii po polsku
# - zwraca angielski CatID (np. AIRHiss)
