from .mapChecker import MapChecker
from .itemManager import ItemManager

#lectures des cartes et vérification de la validité

#essayer de faire de la gestion d'erreurs



class MapManager:

    map_name: str
    item_manager: ItemManager
    map_checker: MapChecker



    def __init__(self, level: int) -> None:
        self.map_name=f"maps/map{level}.txt"
        self.item_manager=ItemManager()
        self.map_checker=MapChecker()

        #if not(self.map_checker.is_valid(self.map_name)):
            #raise ValueError
        
        #on considere que la carte est valide a partir d'ici

        with open(self.map_name, "r", encoding="utf-8", newline='') as f:
            
            line1: str = f.readline().strip("width: ")
            width=int(line1)
            line2 = f.readline().strip("height: ")
            height=int(line2)

            x: float=0
            y: float=64*height

            writing=False
            for line in f:
                line=line.rstrip()
                bord=False

                x=0

                if line=="---":
                    bord=True
                    writing=not writing
                    
                if not bord and writing:
                    for i in line:
                        if i!=" ":
                            item=self.map_checker.translate(i)
                            self.item_manager.add(item, x, y)
                        x=x+64

                y=y-64
            



#pourquoi pas essayer de renverser le fichier pour avoir les y initialisés à 0
