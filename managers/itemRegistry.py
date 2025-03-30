import arcade

#Charge les items et simplifie leur accès

class ItemCollection:

    item_list: dict[str , str]

    def __init__(self) -> None:
        self.item_list={}
        self.item_list["Player"] = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.item_list["Grass"] = ":resources:images/tiles/grassMid.png"
        self.item_list["Box"] = ":resources:images/tiles/boxCrate_double.png"
        self.item_list["Coin"] = ":resources:images/items/coinGold.png"
        self.item_list["Lava"] = ":resources:/images/tiles/lava.png"
        self.item_list["Blob"] = ":resources:/images/enemies/slimeBlue.png"
        self.item_list["Grass2"] = ":resources:/images/tiles/grassHalf_mid.png"


    def place_item(self, item_name : str, x: float, y: float, Scale: float=0.5) -> arcade.Sprite:
        """Place the sprite at the right coordinates, with the right scale"""
        return arcade.Sprite(self.item_list[item_name], center_x=x, center_y=y, scale=Scale)
