import arcade

class GameView(arcade.View):
    """Main in-game view."""

    def __init__(self) -> None:
        # Magical incantion: initialize the Arcade view
        super().__init__()

        # Choose a nice comfy background color
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        # Setup our game
        self.setup()

    def setup(self) -> None:
        """Set up the game here."""
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            ter_x=64,
            ter_y=128
        )

    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()
        arcade.draw_sprite(self.player_sprite)
