import arcade

#gere les caractères, les traductions et les validités
#regarder si enum ne pourrait pas etre utile

class MapChecker:

    translation_table: dict[str , str]

    def __init__(self) -> None:
        self.translation_table={"=":"Grass", "-":"Grass2", "x":"Box", "*":"Coin", "o":"Blob", "£":"Lava", "S":"Player"}
        


    def is_valid(self,name : str) -> bool:

        #doit verifier: 
        # bons caractères, 
        # nombres valables et bonne présentation de hauteur et largeur, 
        # la carte commence et finit bien par ---, 
        # un seul sprite de joueur, 
        # la carte respecte la hauteur et largeur,
        # (bon format de fichier)

        return True

    def translate(self, symbol:str) -> str:
        return self.translation_table[symbol]
