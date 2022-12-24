from my_engine import my_game
from my_engine.entities.entity_base import Entity
from my_engine.scenes import scene_base

import logging
import pygame


class Player(Entity):

    def __init__(self, game: my_game.MyGame, parent_scene: scene_base.Scene):
        self.game = game
        self.parent_scene = parent_scene
        self.x_pos = 32
        self.y_pos = 200 / 2
        self.image: pygame.Surface = None
    

    def on_enter(self):
        image_bytes = self.game.media_manager.get_file("media/paddle.png")
        self.image = pygame.image.load(image_bytes)

    
    def on_exit(self):
        self.parent_scene.queue_free(self)

    
    def update(self, delta_time: int):
        pass

    def draw(self, back_buffer: pygame.Surface):
        self.game.back_buffer.blit(self.image, (self.x_pos, self.y_pos))
