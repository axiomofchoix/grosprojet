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
one_pixel_texture = arcade.make_soft_square_texture(1, arcade.color.WHITE, outer_alpha=255)

class GameView(arcade.View):
    """Main in-game view."""
    player_sprite: arcade.Sprite
    player_sprite_list: arcade.SpriteList[arcade.Sprite](use_spatial_hash=True)
    wall: arcade.Sprite
    wall_list: arcade.SpriteList[arcade.Sprite](use_spatial_hash=True)
    box: arcade.Sprite
    physics_engine: arcade.PhysicsEnginePlatformer
    camera: arcade.camera.Camera2D
    bas: arcade.Sprite
    gauche: arcade.Sprite
    droite: arcade.Sprite
    BOOL_TIMER: bool
    TIMER: float
    DROITE: bool
    GAUCHE: bool
    #bench_sprite: arcade.Sprite
    #bench_sprite_list: arcade.SpriteList[arcade.Sprite](use_spatial_hash=True)
    lava_sprite: arcade.Sprite
    lava_sprite_list: arcade.SpriteList[arcade.Sprite](use_spatial_hash=True)
    blob_sprite: arcade.Sprite
    blob_sprite_list: arcade.SpriteList[arcade.Sprite](use_spatial_hash=True)
    blob_left_edge: arcade.Sprite
    blob_right_edge: arcade.Sprite
    blob_bool: bool
    coin_sound = arcade.load_sound(
        ":resources:sounds/coin1.wav",
        streaming = False
        )
    jump_sound = arcade.load_sound(
        ":resources:sounds/jump3.wav",
        streaming = False
        )
    death_sound = arcade.load_sound(
        ":resources:sounds/gameover1.wav",
        streaming=False
    )
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
            case arcade.key.D:
                # start moving to the right
                self.player_sprite.change_x += PLAYER_MOVEMENT_SPEED
                self.DROITE=True
            case arcade.key.A:
                # start moving to the left
                self.player_sprite.change_x -= PLAYER_MOVEMENT_SPEED
                self.GAUCHE=True
            case arcade.key.SPACE:
                # jump by giving an initial vertical speed
                if len(arcade.check_for_collision_with_list(self.bas, self.wall_list))!=0:
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
                    arcade.play_sound(self.jump_sound, loop = False,volume=0.1)
                if len(arcade.check_for_collision_with_list(self.gauche, self.wall_list))!=0:
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
                    self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
                    arcade.play_sound(self.jump_sound, loop = False,volume=0.1)
                    self.BOOL_TIMER = True
                    #print('a')
                if len(arcade.check_for_collision_with_list(self.droite, self.wall_list))!=0:
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
                    self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
                    arcade.play_sound(self.jump_sound, loop = False,volume=0.1)
                    self.BOOL_TIMER = True
                    #print('b')
                #self.player_sprite.width*=1.1
                #self.bas.width*=1.1
            case arcade.key.ESCAPE:
                # jump by giving an initial vertical speed
                self.player_sprite.center_x=64
                self.player_sprite.center_y=64
                self.player_sprite.change_x=0
                self.player_sprite.change_y=0

    def on_key_release(self, key: int, modifiers: int) -> None:
        """Called when the user releases a key on the keyboard."""
        match key:
            case arcade.key.D:
                # stop lateral movement
                self.player_sprite.change_x -=PLAYER_MOVEMENT_SPEED
                self.DROITE=False
            case arcade.key.A:
                # stop lateral movement
                self.player_sprite.change_x += PLAYER_MOVEMENT_SPEED
                self.GAUCHE=False


    def setup(self) -> None:
        """Set up the game here."""
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            center_x=64,
            center_y=102,
            #angle=2
        )
        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.append(self.player_sprite)
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        #self.bench_sprite_list = arcade.SpriteList()
        self.lava_sprite_list = arcade.SpriteList()
        self.blob_sprite_list = arcade.SpriteList()
        for i in range(0,11281,64):
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
        for i in range(96,672,64):
            self.box = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",
                center_x=800,
                center_y=i,
                scale=0.5
            )
            self.wall_list.append(self.box)
            
        self.box = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",
                center_x=512,
                center_y=384,
                scale=0.5
        )
        self.wall_list.append(self.box)
        self.box = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",
                center_x=512,
                center_y=320,
                scale=0.5
        )
        self.wall_list.append(self.box)
        for i in range(256,769,256):
            self.coin = arcade.Sprite(
                ":resources:images/items/coinGold.png",
                center_x=i,
                center_y=144,
                scale=0.5
            )
            self.coin_list.append(self.coin)
        self.bas = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            center_x=self.player_sprite.center_x,
            center_y=self.player_sprite.center_y-1,
        )
        self.gauche = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            center_x=self.player_sprite.center_x-1,
            center_y=self.player_sprite.center_y,
        )
        self.droite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            center_x=self.player_sprite.center_x+1,
            center_y=self.player_sprite.center_y,
        )
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            walls=self.wall_list,
            gravity_constant=PLAYER_GRAVITY
        )
        self.camera = arcade.camera.Camera2D()
        self.BOOL_TIMER = False
        self.TIMER = 0
        self.GAUCHE=False
        self.DROITE=False
        #self.bench_sprite = arcade.Sprite(
            #"hkbench.webp",
            #center_x=90,
            #center_y=95,
            #scale=0.8
        #)
        #self.bench_sprite_list.append(self.bench_sprite)
        for i in range(350,450,64):
            self.lava_sprite = arcade.Sprite(
                ":resources:images/tiles/lava.png",
                center_x=i,
                center_y=0
            )
            self.lava_sprite_list.append(self.lava_sprite)
        self.blob_sprite = arcade.Sprite(
            ":resources:images/enemies/slimePurple.png",
            center_x=495,
            center_y=160,
            scale=0.5
        )
        self.blob_sprite_list.append(self.blob_sprite)
        self.blob_left_edge = arcade.Sprite(
            one_pixel_texture,
            center_x=self.blob_sprite.center_x-20,
            center_y=self.blob_sprite.center_y-34,
            scale=0.5
        )
        self.blob_right_edge = arcade.Sprite(
            one_pixel_texture,
            center_x=self.blob_sprite.center_x+20,
            center_y=self.blob_sprite.center_y-34,
            scale=0.5
        )
        self.blob_bool=True
        
    def on_update(self, delta_time: float) -> None:
        """Called once per frame, before drawing.

        This is where in-world time "advances", or "ticks".
        """
        self.physics_engine.update()
        if self.camera.bottom_right.x-self.player_sprite.center_x<125:
            self.camera.position = (self.player_sprite.center_x-520,360)
        elif self.player_sprite.center_x-self.camera.bottom_left.x<125:
            self.camera.position = (self.player_sprite.center_x+520,360)
        #self.player_sprite.angle+=5
        r, g, b, a = self.player_sprite.color
        self.player_sprite.color = ((r+5)%255, (g+2)%255, (b+1)%255, a)
        for i in arcade.check_for_collision_with_list(self.player_sprite, self.coin_list):
            self.coin_list.remove(i)
            arcade.play_sound(self.coin_sound, loop=False, volume=0.1)
        self.bas.position=(self.player_sprite.center_x,self.player_sprite.center_y-1)
        self.gauche.position=(self.player_sprite.center_x-5,self.player_sprite.center_y)
        self.droite.position=(self.player_sprite.center_x+5,self.player_sprite.center_y)
        if self.BOOL_TIMER==True and self.TIMER<10:
            self.TIMER+=1
        elif self.TIMER>=10:
            self.TIMER=0
            self.BOOL_TIMER=False
            if self.GAUCHE and self.DROITE:
                self.player_sprite.change_x = 0
            elif self.GAUCHE:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif self.DROITE:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            else:
                self.player_sprite.change_x = 0
        if arcade.check_for_collision_with_list(self.bas,self.lava_sprite_list):
            arcade.play_sound(self.death_sound, loop = False,volume=0.1)
            self.setup()
        if arcade.check_for_collision_with_list(self.blob_left_edge,self.wall_list) and arcade.check_for_collision_with_list(self.blob_right_edge,self.wall_list) and not(arcade.check_for_collision_with_list(self.blob_sprite,self.wall_list)):
            print('a')
            if self.blob_bool:
                self.blob_sprite.center_x+=1
                self.blob_left_edge.center_x+=1
                self.blob_right_edge.center_x+=1
            else:
                self.blob_sprite.center_x-=1
                self.blob_left_edge.center_x-=1
                self.blob_right_edge.center_x-=1
        elif not(arcade.check_for_collision_with_list(self.blob_left_edge,self.wall_list)):
            print('b')
            self.blob_bool=True
            if self.blob_bool:
                self.blob_sprite.center_x+=1
                self.blob_left_edge.center_x+=1
                self.blob_right_edge.center_x+=1
            else:
                self.blob_sprite.center_x-=1
                self.blob_left_edge.center_x-=1
                self.blob_right_edge.center_x-=1
        elif not(arcade.check_for_collision_with_list(self.blob_right_edge,self.wall_list)):
            print('c')
            self.blob_bool=False
            if self.blob_bool:
                self.blob_sprite.center_x+=1
                self.blob_left_edge.center_x+=1
                self.blob_right_edge.center_x+=1
            else:
                self.blob_sprite.center_x-=1
                self.blob_left_edge.center_x-=1
                self.blob_right_edge.center_x-=1
        elif arcade.check_for_collision_with_list(self.blob_sprite,self.wall_list):
            print('d')
            self.blob_bool=not(self.blob_bool)
            if self.blob_bool:
                self.blob_sprite.center_x+=1
                self.blob_left_edge.center_x+=1
                self.blob_right_edge.center_x+=1
            else:
                self.blob_sprite.center_x-=1
                self.blob_left_edge.center_x-=1
                self.blob_right_edge.center_x-=1
        #print(len(arcade.check_for_collision_with_list(self.blob_left_edge,self.wall_list)))




    
    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()
        with self.camera.activate():
            #self.bench_sprite_list.draw()
            self.wall_list.draw()
            self.player_sprite_list.draw()
            self.coin_list.draw()
            self.lava_sprite_list.draw()
            self.blob_sprite_list.draw()
        self.player_sprite.draw_hit_box()
        self.wall_list.draw_hit_boxes()
        self.bas.draw_hit_box()
        self.gauche.draw_hit_box()
        self.droite.draw_hit_box()  
        self.blob_sprite.draw_hit_box()
        self.blob_left_edge.draw_hit_box()
        self.blob_right_edge.draw_hit_box()


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
