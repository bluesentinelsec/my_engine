from my_engine import my_game
from my_engine.scenes import scene_base
from my_engine.entities.entity_base import Entity
from my_engine.media_manager import MediaManager

from my_engine.entities.ball import Ball
from my_engine.entities.opponent import Opponent
from my_engine.entities.player import Player
from my_engine.entities.score import Score

from typing import List


import logging

import pygame
import random

class GameplayScene(scene_base.Scene):

    def __init__(self, game: my_game.MyGame):
        self.game = game
        self.entities: List[Entity] = []
        self.entities_to_delete: List[Entity] = []
        self.background: pygame.Surface = None

        self.ball_i = None
        self.opponent_i = None
        self.player_i = None
        self.player_score = None
        self.opponent_score = None
        self.cpu_timer = 0
        self.cpu_easy = 1
        self.cpu_medium = 2
        self.cpu_hard = 3
        self.cpu_behavior = self.cpu_hard

    def on_enter(self):
        background_bytes = self.game.media_manager.get_file("media/gameplay_background.png")
        self.background = pygame.image.load(background_bytes)
        
        # create starting game entities
        self.ball_i = Ball(game=self.game, parent_scene=self)
        self.opponent_i = Opponent(game=self.game, parent_scene=self)
        self.player_i = Player(game=self.game, parent_scene=self)
        self.player_score = Score(game=self.game, parent_scene=self)
        self.opponent_score = Score(game=self.game, parent_scene=self)
        self.opponent_score.x_pos = 192

        self.entities.append(self.ball_i)
        self.entities.append(self.opponent_i)
        self.entities.append(self.player_i)
        self.entities.append(self.player_score)
        self.entities.append(self.opponent_score)

        # append starting entities to list
        for ent in self.entities:
            ent.on_enter()

    def on_exit(self):
        for ent in self.entities:
            ent.on_exit()
        self.clear_stale_entities()
        del self.background

    def update(self):
        
        self.clear_stale_entities()
        
        self.handle_collisions()
        
        self.check_score()

        self.update_opponent()



        
        # update entities
        for ent in self.entities:
            ent.update(self.game.delta_time)

        
        # check elapsed time
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_ESCAPE]:
            self.game.game_is_running = False

    def draw(self):
        self.clear_stale_entities()
        self.game.back_buffer.blit(self.background, (0, 0))

        for ent in self.entities:
            ent.draw(self.game.back_buffer)

    def queue_free(self, entity_i: Entity):
        self.entities_to_delete.append(entity_i)

    def clear_stale_entities(self):
        if len(self.entities_to_delete) == 0:
            return

        for each_ent in self.entities_to_delete:
            del each_ent
        self.entities_to_delete = []

    
    def handle_collisions(self):
        if pygame.Rect.colliderect(self.ball_i.rect, self.player_i.rect):
            self.ball_i.direction_x = self.ball_i.move_right
        if pygame.Rect.colliderect(self.ball_i.rect, self.opponent_i.rect):
            self.ball_i.direction_x = self.ball_i.move_left
    
    
    def check_score(self):
        if self.ball_i.x_pos < -16:
            self.player_score.increment_score()
            self.ball_i.x_pos = self.game.screen_width / 2
            self.ball_i.y_pos = 10
            self.ball_i.direction_x = self.ball_i.move_right

        if self.ball_i.x_pos > self.game.screen_width + 16:
            self.opponent_score.increment_score()
            self.ball_i.x_pos = self.game.screen_width / 2
            self.ball_i.y_pos = 10
            self.ball_i.direction_x = self.ball_i.move_left

        if self.player_score.game_score >= 5:
            logging.info("stub - you win screen")

        if self.opponent_score.game_score >= 5:
            logging.info("stub - you lose screen")

    def update_opponent(self):
        self.cpu_timer += self.game.delta_time
        if self.cpu_timer >= 10000:
            self.cpu_timer = 0
            behavior = random.randint(1,3)
            if behavior == self.opponent_easy:
                self.cpu_behavior = self.opponent_easy
            if behavior == self.opponent_medium:
                self.cpu_behavior = self.opponent_medium
            if behavior == self.opponent_hard:
                self.cpu_behavior = self.opponent_hard
            
        if self.cpu_behavior == self.cpu_hard:
            self.opponent_hard()

        if self.cpu_behavior == self.cpu_medium:
            self.opponent_medium()

        if self.cpu_behavior == self.cpu_easy:
            self.opponent_easy()


    def opponent_easy(self):
        self.opponent_i.speed = 0.1

        # if ball is below opponent, move opponent down
        if self.ball_i.y_pos > self.opponent_i.y_pos:
            self.opponent_i.y_pos += self.opponent_i.speed * self.game.delta_time
        
        # if ball is above, move up
        if self.ball_i.y_pos < self.opponent_i.y_pos:
            self.opponent_i.y_pos -= self.opponent_i.speed * self.game.delta_time

    def opponent_medium(self):
        self.opponent_i.speed = 0.2
        
        # if ball is below opponent, move opponent down
        if self.ball_i.y_pos > self.opponent_i.y_pos:
            self.opponent_i.y_pos += self.opponent_i.speed * self.game.delta_time
        
        # if ball is above, move up
        if self.ball_i.y_pos < self.opponent_i.y_pos:
            self.opponent_i.y_pos -= self.opponent_i.speed * self.game.delta_time

    def opponent_hard(self):
        self.opponent_i.speed = 0.3
        
        # if ball is below opponent, move opponent down
        if self.ball_i.y_pos > self.opponent_i.y_pos:
            self.opponent_i.y_pos += self.opponent_i.speed * self.game.delta_time
        
        # if ball is above, move up
        if self.ball_i.y_pos < self.opponent_i.y_pos:
            self.opponent_i.y_pos -= self.opponent_i.speed * self.game.delta_time