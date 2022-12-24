from my_engine import my_game
from my_engine.entities.entity_base import Entity
from my_engine.scenes import scene_base

import logging
import pygame


class Ball(Entity):

    def __init__(self, game: my_game.MyGame, parent_scene: scene_base.Scene):
        self.game = game
        self.parent_scene = parent_scene
        self.x_pos = 320 / 2
        self.y_pos = 200 / 2
        self.image: pygame.Surface = None
        self.rect: pygame.Rect = None
        self.move_up = -1
        self.move_down = 1
        self.move_left = -1
        self.move_right = 1
        self.direction_x = self.move_left
        self.direction_y = self.move_down
        self.speed = 0.15
    

    def on_enter(self):
        image_bytes = self.game.media_manager.get_file("media/ball.png")
        self.image = pygame.image.load(image_bytes)
        self.rect = self.image.get_rect()

    
    def on_exit(self):
        self.parent_scene.queue_free(self)

    
    def update(self, delta_time: int):
        
        self.x_pos += self.direction_x * self.speed * delta_time
        self.y_pos += self.direction_y * self.speed * delta_time

        if self.y_pos < 0:
            self.direction_y = self.move_down

        if self.y_pos > self.game.screen_height:
            self.direction_y = self.move_up

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos


    def draw(self, back_buffer: pygame.Surface):
        self.game.back_buffer.blit(self.image, (self.x_pos, self.y_pos))

    def rebound_player(self):
        self.direction_x *= -1

    def rebound_opponent(self):
        self.direction_x = self.move_left