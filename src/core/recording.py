# TODO: Klasa Recording:
# - Atrybuty:
#   - path (ścieżka do pliku WAV)
#   - name (nazwa pliku)
#   - date (data nagrania)
#   - lat, lon (lokalizacja GPS)
#   - description (opis)
#   - category (np. ptaki, miasto, rozmowy)
#   - image_path (obrazek miejsca)

# - from_file(path) – tworzy obiekt z metadanych pliku
# - to_dict() – do zapisu w bazie

# src/core/recording.py


class Recording:
    def __init__(
        self,
        path,
        name,
        date,
        time,
        lat,
        lon,
        description,
        category,
        image_path=None,
        id=None,
    ):
        self.id = id  # opcjonalnie – nadawane przez bazę
        self.path = path
        self.name = name
        self.date = date
        self.time = time
        self.lat = lat
        self.lon = lon
        self.description = description
        self.category = category
        self.image_path = image_path

    @classmethod
    def from_file(cls, path):
        # TODO: pobieranie metadanych z pliku WAV (np. data nagrania)
        # i tworzenie Recording
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "path": self.path,
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "lat": self.lat,
            "lon": self.lon,
            "description": self.description,
            "category": self.category,
            "image_path": self.image_path,
        }
