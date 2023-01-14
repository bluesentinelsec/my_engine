import uuid

import my_engine.event
import my_engine.event_manager
import my_engine.game
import my_engine.scene
import my_engine.scene_manager
import my_engine.component as cmp

from typing import List


class Entity:
    """
    Entity is a base type for creating in-game actors,
    such as the player, enemies, objects, etc.
    Entities consist of components; components extend
    an entity with additional data and behaviors.
    """
    def __init__(self, ent_type: str, game: "my_engine.game.Game", parent_scene: "my_engine.scene.Scene") -> None:
        self.id = uuid.uuid4()  # uniquely identifies each entity
        self.entity_type: str = ent_type  # identifies the entity type
        self.groups = List[str]  # identifies groups the entity is a part of
        self.is_active = True  # used to pause/unpause the entity
        self.game = game
        self.parent_scene = parent_scene
        self.event_manager_ptr = my_engine.event_manager.EventManagerSingleton()
        self.components: List["cmp.Component"] = []

    def set_ent_type(self, ent_type: str):
        """
        assign the entity a type; the entity type
        can be used to check if an entity matches
        a specific type before performing additional logic,
        such as checking a collision between a player type
        entity and an enemy type entity.

        :param ent_type:
        :return:
        """
        self.entity_type = ent_type

    def get_ent_type(self):
        return self.entity_type

    def append_group(self, group: str):
        self.groups.append(group)

    def remove_group(self, group: str):
        for each_group in self.groups:
            if each_group == group:
                self.groups.remove(each_group)

    def get_groups(self):
        return self.groups

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def add_component(self, comp: "cmp.Component"):
        self.components.append(comp)

    def remove_component(self, cmp_id):
        for comp in self.components:
            if cmp_id == comp.get_id():
                self.components.remove(comp)

    def on_load(self):
        for comp in self.components:
            comp.on_load()

    def update(self):
        if not self.is_active:
            return
        for comp in self.components:
            comp.update()

    def draw(self):
        if not self.is_active:
            return
        for comp in self.components:
            comp.draw()

    def on_exit(self):
        for comp in self.components:
            comp.on_exit()
