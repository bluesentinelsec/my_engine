from my_engine import my_game
from my_engine.scenes import scene_base
from my_engine.entities.entity_base import Entity
from my_engine.media_manager import MediaManager

import pygame


class Cursor(Entity):

    def __init__(self, game: my_game.MyGame, parent_scene: scene_base.Scene):
        self.game = game
        self.parent_scene = parent_scene
        self.x_pos = 54
        self.y_pos = 112
        self.image: pygame.Surface = None
        # end position: 110x143
    

    def on_enter(self):
        image_bytes = self.game.media_manager.get_file("media/cursor.png")
        self.image = pygame.image.load(image_bytes)

    
    def on_exit(self):
        pass

    
    def update(self, delta_time: int):
        pass


    def draw(self, back_buffer: pygame.Surface):
        self.game.back_buffer.blit(self.image, (self.x_pos, self.y_pos))
