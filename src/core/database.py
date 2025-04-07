# TODO: Klasa DatabaseManager:
# - connect() – połączenie z soundscape.db
# - init_schema() – tworzy tabele, jeśli nie istnieją
# - insert_recording(recording) – dodaje rekord do DB
# - get_all_recordings() – zwraca listę Recording z bazy
# - delete_recording(id)
# - check_if_exists(path) – sprawdza, czy plik już jest w bazie
# TODO: Tabela ml_labels
# - recording_id: INTEGER NOT NULL, FK do recordings(id)
# - label: TEXT
# - confidence: REAL (opcjonalnie)
# - model: TEXT (opcjonalnie)
# - timestamp: TEXT (opcjonalnie, ISO8601)

# Metody:
# - add_ml_label(ml_label: MLLabel) – dodaje etykietę do bazy
# - get_ml_labels_by_recording(recording_id) – zwraca listę etykiet dla nagrania
# - delete_ml_labels(recording_id) – usuwa etykiety powiązane z nagraniem (np. przy reanalizie)
