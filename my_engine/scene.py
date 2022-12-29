import my_engine.entity
import my_engine.game

from typing import List

import pygame


class Scene:
    def __init__(self, game: "my_engine.game.MyGame") -> None:
        self.game = game
        self.entities: List["my_engine.entity.Entity"] = []

    def on_load(self):
        # read persistent data from disk?
        # create needed entities
        # add entities to a list
        pass

    def on_exit(self):
        # delete all entities in the scene
        # write persistent data to disk?
        pass

    def update(self):
        # process event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit_game()

        # clear backbuffer
        self.game.screen.fill((0, 0, 0))

        # call each entitie's update method
        for each_ent in self.entities:
            each_ent.update()

    def draw(self):
        
        # draw each entity
        for each_ent in self.entities:
            each_ent.draw()

        # flip the backbuffer
        pygame.display.flip()

    def add_entity(self, ent: "my_engine.entity.Entity"):
        self.entities.append(ent)

    def remove_entity(self, id):
        for each_ent in self.entities:
            if each_ent.id == id:
                self.entities.remove(each_ent)

    def get_entities(self):
        return self.entities

    def get_entities_by_group(self, group: str):
        entities_in_group = []
        for each_ent in self.entities:
            if group in each_ent.groups:
                entities_in_group.append(each_ent)

        return entities_in_group

    def get_entities_of_type(self, ent_type: str):
        entities_of_type = []
        for each_ent in self.entities:
            if ent_type == each_ent.get_ent_type():
                entities_of_type.append(each_ent)

        return entities_of_type
