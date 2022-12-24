from my_engine import my_game
from my_engine.entities.entity_base import Entity
from my_engine.scenes import scene_base

import logging
import pygame


class Score(Entity):

    def __init__(self, game: my_game.MyGame, parent_scene: scene_base.Scene):
        self.game = game
        self.parent_scene = parent_scene
        self.x_pos = 112
        self.y_pos = 0
        self.game_score = 0
        self.font: pygame.font.Font = None
    

    def on_enter(self):
        font_bytes = self.game.media_manager.get_file("media/c64_font.ttf")
        self.font = pygame.font.Font(font_bytes, 32)

    
    def on_exit(self):
        self.parent_scene.queue_free(self)

    
    def update(self, delta_time: int):
        pass

    def draw(self, back_buffer: pygame.Surface):
        draw_font = self.font.render(str(self.game_score), False, (255,255,255))
        self.game.back_buffer.blit(draw_font, (self.x_pos, self.y_pos))

    def increment_score(self):
        self.game_score += 1
