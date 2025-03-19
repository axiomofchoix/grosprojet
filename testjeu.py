import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"
PLAYER_MOVEMENT_SPEED = 5
"""Lateral speed of the player, in pixels per frame."""
PLAYER_GRAVITY = 1
"""Gravity applied to the player, in pixels per frame²."""
PLAYER_JUMP_SPEED = 18
"""Instant vertical speed for jumping, in pixels per frame."""

class GameView(arcade.View):
    """Main in-game view."""
    player_sprite: arcade.Sprite
    player_sprite_list: arcade.SpriteList[arcade.Sprite]
    wall: arcade.Sprite
    wall_list: arcade.SpriteList[arcade.Sprite]
    box: arcade.Sprite
    physics_engine: arcade.PhysicsEnginePlatformer
    camera: arcade.camera.Camera2D
    def __init__(self) -> None:
        # Magical incantion: initialize the Arcade view
        super().__init__()

        # Choose a nice comfy background color
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        arcade.SpriteList(use_spatial_hash=True)

        # Setup our game
        self.setup()
    
    def on_key_press(self, key: int, modifiers: int) -> None:
        """Called when the user presses a key on the keyboard."""
        match key:
            case arcade.key.RIGHT:
                # start moving to the right
                self.player_sprite.change_x = +PLAYER_MOVEMENT_SPEED
            case arcade.key.LEFT:
                # start moving to the left
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            case arcade.key.UP:
                # jump by giving an initial vertical speed
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
            case arcade.key.ESCAPE:
                # jump by giving an initial vertical speed
                self.player_sprite.center_x=64
                self.player_sprite.center_y=64

    def on_key_release(self, key: int, modifiers: int) -> None:
        """Called when the user releases a key on the keyboard."""
        match key:
            case arcade.key.RIGHT | arcade.key.LEFT:
                # stop lateral movement
                self.player_sprite.change_x = 0


    def setup(self) -> None:
        """Set up the game here."""
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            center_x=64,
            center_y=1024,
            angle=2
        )
        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.append(self.player_sprite)
        self.wall_list = arcade.SpriteList()
        for i in range(0,1281,64):
            self.wall = arcade.Sprite(
                ":resources:images/tiles/grassMid.png",
                center_x=i,
                center_y=32,
                scale=0.5
            )
            self.wall_list.append(self.wall)
        for i in range(256,769,256):
            self.box = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",
                center_x=i,
                center_y=96,
                scale=0.5
            )
            self.wall_list.append(self.box)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            walls=self.wall_list,
            gravity_constant=PLAYER_GRAVITY
        )
        self.camera = arcade.camera.Camera2D()
    def on_update(self, delta_time: float) -> None:
        """Called once per frame, before drawing.

        This is where in-world time "advances", or "ticks".
        """
        self.physics_engine.update()
        self.player_sprite.angle+=25
    
    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()
        self.player_sprite_list.draw()
        self.wall_list.draw()

class Window:
    view: GameView

    def __init__(self, width: int, height: int, title: str) -> None:
        ... # toutes sortes d'initialisations

    def show_view(self, view: GameView) -> None:
        self.view = view

def arcade_run() -> None:
    window.open() # open the window on the user's screen
    while True:
        window.view.on_draw()
        wait_for(1 / 60) # wait for 1/60 seconds

def main() -> None:
    """Main function."""

    # Create the (unique) Window, setup our GameView, and launch
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()