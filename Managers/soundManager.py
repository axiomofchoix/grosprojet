import arcade

#peut etre faire un dictionnaire, pour charger les sons dans un seul contenant et avoir des noms adaptés et plus pratiques (GameOver pour le son de game over par exemple)

class SoundManager:

    sound_list: dict[str , arcade.Sound]

    def __init__(self) -> None:
        self.sound_list={}
        self.sound_list["Coin"] = arcade.load_sound(":resources:sounds/coin1.wav")
        self.sound_list["Jump"] = arcade.load_sound(":resources:sounds/jump1.wav")
        self.sound_list["GameOver"] = arcade.load_sound(":resources:sounds/gameover1.wav")
