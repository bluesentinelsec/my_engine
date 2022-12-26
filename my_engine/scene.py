import my_engine.entity

from typing import List


class Scene:
    def __init__(self) -> None:
        self.entities: List["my_engine.entity.Entity"] = []

    def on_enter(self):
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

        # for each entity:
        # update entity
        pass

    def draw(self):
        # for each entity
        # draw entity
        pass

    def add_entity(self):
        pass

    def remove_entity(self):
        pass

    def get_entities(self):
        pass

    def get_entities_by_group(self):
        pass
