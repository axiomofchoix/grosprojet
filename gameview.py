import arcade
from managers.mapManager import MapManager
from managers.soundManager import SoundManager

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
    wall_list: arcade.SpriteList[arcade.Sprite]
    coin_list: arcade.SpriteList[arcade.Sprite]

    physics_engine: arcade.PhysicsEnginePlatformer
    camera: arcade.camera.Camera2D

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
            center_x=64,
            center_y=128
        )
        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.append(self.player_sprite)

        
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        
        for i in range(0,1280,64):
            grass = arcade.Sprite(
                ":resources:images/tiles/grassMid.png",
                center_x=i,
                center_y=32,
                scale=0.5
            )
            self.wall_list.append(grass)



        for j in range(256,1024,256):
            box = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",
                center_x=j,
                center_y=96,
                scale=0.5
            )
            self.wall_list.append(box)

        for k in range(128, 1250, 256):
            coin = arcade.Sprite(
                ":resources:images/items/coinGold.png",
                center_x=k,
                center_y=96,
                scale=0.5
            )
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            walls=self.wall_list,
            gravity_constant=PLAYER_GRAVITY
        )

        self.camera = arcade.camera.Camera2D()

    def on_key_press(self, key: int, modifiers: int) -> None:
        """Called when the user presses a key on the keyboard."""
        match key:
            case arcade.key.RIGHT:
                # start moving to the right
                self.player_sprite.change_x +=PLAYER_MOVEMENT_SPEED
            case arcade.key.LEFT:
                # start moving to the left
                self.player_sprite.change_x -=PLAYER_MOVEMENT_SPEED
            case arcade.key.UP:
                # jump by giving an initial vertical speed, if the player is on the ground
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
                    arcade.play_sound(Sounds.sound_list["Jump"])
            case arcade.key.SPACE:
                # reset
                GameView.setup(self)



    def on_key_release(self, key: int, modifiers: int) -> None:
        """Called when the user releases a key on the keyboard."""
        match key:
            case arcade.key.RIGHT:
                # stop lateral movement
                self.player_sprite.change_x -=PLAYER_MOVEMENT_SPEED
            case arcade.key.LEFT:
                # stop lateral movement
                self.player_sprite.change_x += PLAYER_MOVEMENT_SPEED

    def on_update(self, delta_time: float) -> None:
        """Called once per frame, before drawing.

        This is where in-world time "advances", or "ticks".
        """
        self.physics_engine.update()

        for i in arcade.check_for_collision_with_list(self.player_sprite, self.coin_list):
            #self.coin_list.remove(i)
            i.remove_from_sprite_lists()
            arcade.play_sound(Sounds.sound_list["Coin"])


        # Waiting for a new version of mypy with https://github.com/python/mypy/pull/18510
        self.camera.position = self.player_sprite.position # type: ignore

        """if self.camera.bottom_right.x-self.player_sprite.center_x<384:
            self.camera.position = (self.camera.position.x + PLAYER_MOVEMENT_SPEED,self.camera.position.y)
        elif self.player_sprite.center_x-self.camera.bottom_left.x<512:
            self.camera.position = (self.camera.position.x - PLAYER_MOVEMENT_SPEED,self.camera.position.y)
        
        if self.camera.bottom_right.y-self.player_sprite.center_y<180:
            self.camera.position = (self.camera.position.x,self.player_sprite.center_y+PLAYER_JUMP_SPEED)
        elif self.player_sprite.center_y-self.camera.bottom_left.y<180:
            self.camera.position = (self.camera.position.x,self.player_sprite.center_y-60*PLAYER_GRAVITY)"""
    
    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()
        with self.camera.activate():
          self.wall_list.draw()
          self.coin_list.draw()
          self.player_sprite_list.draw()
          self.wall_list.draw_hit_boxes()
          self.player_sprite_list.draw_hit_boxes()



    

    