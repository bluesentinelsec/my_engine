import my_engine.entity
import my_engine.game

from typing import List

import pygame


class Scene:
    def __init__(self, game: "my_engine.game.MyGame", name: str = "undefined") -> None:
        self.game = game
        self.name = name
        self.entities: List["my_engine.entity.Entity"] = []

    def on_load(self):
        """
        on_load performs any needed initialization prior
        to running the scene's update method, for example,
        invoking screen transitions, spawning entities, reading
        files from disk, etc.
        """
        pass

    def on_exit(self):
        """
        on_exit performs any needed cleanup prior
        to exiting a scene
        """
        pass

    def update(self):
        """
        update is used to invoke each entitie's
        update method
        """
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
        """
        draw invokes each entitie's draw method
        """

        # draw each entity
        for each_ent in self.entities:
            each_ent.draw()

    def add_entity(self, ent: "my_engine.entity.Entity"):
        """
        add entity to scene
        """

        self.entities.append(ent)

    def remove_entity(self, id):
        """
        removes entity witch matching id from scene
        """
        for each_ent in self.entities:
            if each_ent.id == id:
                self.entities.remove(each_ent)

    def get_entities(self):
        """
        get list of all entities in scene
        """
        return self.entities

    def get_entities_by_group(self, group: str):
        """
        return a list of entities matching the specified group
        """
        entities_in_group = []
        for each_ent in self.entities:
            if group in each_ent.groups:
                entities_in_group.append(each_ent)

        return entities_in_group

    def get_entities_of_type(self, ent_type: str):
        """
        returns a list of entities matching the specified
        entity type
        """
        entities_of_type = []
        for each_ent in self.entities:
            if ent_type == each_ent.get_ent_type():
                entities_of_type.append(each_ent)

        return entities_of_type
