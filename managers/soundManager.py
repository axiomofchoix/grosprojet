import arcade

#Charge les sons et simplifie leur accès

class SoundManager:

    sound_list: dict[str , arcade.Sound]

    def __init__(self) -> None:
        self.sound_list={}
        self.sound_list["Coin"] = arcade.load_sound(":resources:sounds/coin1.wav")
        self.sound_list["Jump"] = arcade.load_sound(":resources:sounds/jump1.wav")
        self.sound_list["GameOver"] = arcade.load_sound(":resources:sounds/gameover1.wav")
