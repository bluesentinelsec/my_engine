from my_engine import my_game
from my_engine.entities.entity_base import Entity
from my_engine.scenes import scene_base
from my_engine.scenes import gameplay
from my_engine.media_manager import MediaManager

import logging
import pygame


class Cursor(Entity):

    def __init__(self, game: my_game.MyGame, parent_scene: scene_base.Scene):
        self.game = game
        self.parent_scene = parent_scene
        self.start_position_x = 54
        self.start_position_y = 112
        self.quit_position_x = 110
        self.quit_position_y = 143
        self.x_pos = self.start_position_x
        self.y_pos = self.start_position_y
        self.image: pygame.Surface = None
    

    def on_enter(self):
        image_bytes = self.game.media_manager.get_file("media/cursor.png")
        self.image = pygame.image.load(image_bytes)

    
    def on_exit(self):
        self.parent_scene.queue_free(self)

    
    def update(self, delta_time: int):
        key_state = pygame.key.get_pressed()
        
        # move cursor up
        if key_state[pygame.K_UP]:
            if self.y_pos == self.quit_position_y:
                self.y_pos = self.start_position_y

        # move cursor down
        if key_state[pygame.K_DOWN]:
            if self.y_pos == self.start_position_y:
                self.y_pos = self.quit_position_y
            
        # enter gameplay scene or quit game
        if key_state[pygame.K_RETURN]:
            if self.y_pos == self.start_position_y:
                self.game.scene_manager.change_scene(gameplay.GameplayScene(self.game))
                
            if self.y_pos == self.quit_position_y:
                ev = pygame.event.Event(pygame.QUIT)
                pygame.event.post(ev)

        # quit game
        if key_state[pygame.K_ESCAPE]:
            self.game.game_is_running = False


    def draw(self, back_buffer: pygame.Surface):
        self.game.back_buffer.blit(self.image, (self.x_pos, self.y_pos))
