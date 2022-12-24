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
        self.speed = 0.5
        self.image: pygame.Surface = None
        self.rect: pygame.Rect = None
    

    def on_enter(self):
        image_bytes = self.game.media_manager.get_file("media/paddle.png")
        self.image = pygame.image.load(image_bytes)
        self.rect = self.image.get_rect()

    
    def on_exit(self):
        self.parent_scene.queue_free(self)

    
    def update(self, delta_time: int):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_UP]:
            self.y_pos -= self.speed * delta_time
        if key_state[pygame.K_DOWN]:
            self.y_pos += self.speed * delta_time

        if self.y_pos < 0:
            self.y_pos = 0

        if self.y_pos > 168:
            self.y_pos = 168

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def draw(self, back_buffer: pygame.Surface):
        self.game.back_buffer.blit(self.image, (self.x_pos, self.y_pos))
