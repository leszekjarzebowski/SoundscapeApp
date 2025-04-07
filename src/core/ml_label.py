# TODO: Klasa MLLabel
# - Reprezentuje jedną etykietę przypisaną do nagrania przez model ML

# Atrybuty:
# - id (opcjonalnie, do bazy)
# - recording_id – ID nagrania (FK do Recording.id)
# - label – np. "bird", "traffic", "silence"
# - confidence – pewność predykcji (0.0–1.0, opcjonalne)
# - model – identyfikator modelu, który przypisał etykietę (np. "birdnet_v2")
# - timestamp – data i godzina przypisania etykiety (opcjonalnie, np. do wersjonowania)

# Metody:
# - from_prediction(recording_id, label, confidence=None, model=None) – fabryka z predykcji ML
# - to_dict() – do serializacji i zapisu w bazie
