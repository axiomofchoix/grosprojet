import arcade

#Charge les sons et simplifie leur accès

class SoundCollection:

    sound_list: dict[str , arcade.Sound]

    def __init__(self) -> None:
        self.sound_list={}
        self.sound_list["Coin"] = arcade.load_sound(":resources:sounds/coin1.wav")
        self.sound_list["Jump"] = arcade.load_sound(":resources:sounds/jump1.wav")
        self.sound_list["GameOver"] = arcade.load_sound(":resources:sounds/gameover1.wav")

    def get_sound(self, sound_name : str) -> arcade.Sound:
        """Used to find a sound by its name in a SoundCollection"""
        return self.sound_list[sound_name]
