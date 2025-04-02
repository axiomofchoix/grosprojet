import arcade
from .itemRegistry import ItemCollection

#Gestion des listes de sprites

#3 idées:
#-créer une classe comme sound manager qui fait un dict et s'occuper de la création dans mapmanager
#-créer un classe qui recoit les positions et renvoie le sprite a mapmanager
#-créer un classe qui recoit les positions et fait les listes de sprites et renvoie a mapmanager

#je pars sur la 3e


class ItemManager:

    player_sprite_list: arcade.SpriteList[arcade.Sprite]
    wall_list: arcade.SpriteList[arcade.Sprite]
    coin_list: arcade.SpriteList[arcade.Sprite]
    no_go_list: arcade.SpriteList[arcade.Sprite]
    monster_list: arcade.SpriteList[arcade.Sprite]
    item_collection: ItemCollection



    def __init__(self) -> None:
        self.item_collection=ItemCollection()

        self.player_sprite_list = arcade.SpriteList()
        self.monster_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.no_go_list = arcade.SpriteList(use_spatial_hash=True)



    def add(self, sprite_name : str, x: float, y: float, scale: float=0.5) -> None:
        """Place the sprites in the right lists in order to draw them"""
        item=self.item_collection.place_item(sprite_name,x,y,scale)

        match sprite_name:
            case "Box" | "Grass" | "Grass2":
                self.wall_list.append(item)

            case "Coin":
                self.coin_list.append(item)
            
            case "Lava":
                self.no_go_list.append(item)
            
            case "Blob":
                self.monster_list.append(item)
            
            case "Player":
                self.player_sprite_list.append(item)

