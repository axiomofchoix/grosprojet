import arcade
from .mapManager import MapManager

PLAYER_MOVEMENT_SPEED = 5 
"""Lateral speed of the player, in pixels per frame."""

PLAYER_GRAVITY = 1
"""Gravity applied to the player, in pixels per frame²."""

PLAYER_JUMP_SPEED = 18
"""Instant vertical speed for jumping, in pixels per frame."""

class PlayerManager:

    player_sprite: arcade.Sprite
    player_sprite_list: arcade.SpriteList[arcade.Sprite]
    physics_engine: arcade.PhysicsEnginePlatformer