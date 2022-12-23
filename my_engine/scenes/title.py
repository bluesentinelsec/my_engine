from my_engine import my_game
from my_engine.scenes import scene_base
from my_engine.entities.entity_base import Entity
from typing import List


import logging

import pygame

class TitleScene(scene_base.Scene):

    def __init__(self, game: my_game.MyGame):
        self.game = game
        self.entities: List[Entity] = []
        self.entities_to_delete: List[Entity] = []
    

    def on_enter(self):
        logging.debug("TitleScene.on_enter")
        # create starting game entities
        # append starting entities to list


    def on_exit(self):
        self.clear_stale_entities()


    def update(self):
        self.clear_stale_entities()
        logging.debug("TitleScene.update")
        logging.debug(self.game.delta_time)
        
        # get input
        # update entities
        for ent in self.entities:
            ent.update()

        # check collisions
        # check elapsed time


    def draw(self):
        self.clear_stale_entities()
        logging.debug("TitleScene.draw")
        logging.debug(self.game.back_buffer)
        
        for ent in self.entities:
            ent.draw()

    def queue_free(self, entity_i: Entity):
        self.entities_to_delete.append(entity_i)

    def clear_stale_entities(self):
        if len(self.entities_to_delete) == 0:
            return

        for each_ent in self.entities_to_delete:
            del each_ent
        self.entities_to_delete = []