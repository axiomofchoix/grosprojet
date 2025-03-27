import arcade

#lectures des cartes et vérification de la validité

class MapManager:

    map_name: str




    def __init__(self, name: str) -> None:
        self.map_name=name

        with open(self.map_name, "r", encoding="utf-8", newline='') as f:
            line = f.readline()
