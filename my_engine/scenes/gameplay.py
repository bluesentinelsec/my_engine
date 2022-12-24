from my_engine import my_game
from my_engine.scenes import scene_base
from my_engine.entities.entity_base import Entity
from my_engine.media_manager import MediaManager

from my_engine.entities.ball import Ball
from my_engine.entities.opponent import Opponent
from my_engine.entities.player import Player

from typing import List


import logging

import pygame


class GameplayScene(scene_base.Scene):

    def __init__(self, game: my_game.MyGame):
        self.game = game
        self.entities: List[Entity] = []
        self.entities_to_delete: List[Entity] = []
        self.background: pygame.Surface = None

    def on_enter(self):
        background_bytes = self.game.media_manager.get_file("media/gameplay_background.png")
        self.background = pygame.image.load(background_bytes)
        
        # create starting game entities
        ball_i = Ball(game=self.game, parent_scene=self)
        opponent_i = Opponent(game=self.game, parent_scene=self)
        player_i = Player(game=self.game, parent_scene=self)

        self.entities.append(ball_i)
        self.entities.append(opponent_i)
        self.entities.append(player_i)

        # append starting entities to list
        for ent in self.entities:
            ent.on_enter()

    def on_exit(self):
        self.clear_stale_entities()
        for ent in self.entities:
            ent.on_exit()
        del self.background

    def update(self):
        self.clear_stale_entities()

        # update entities
        for ent in self.entities:
            ent.update(self.game.delta_time)

        # check collisions
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
