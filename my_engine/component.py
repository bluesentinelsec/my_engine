"""
Component defines a base component class used in an
entity component system. All components extend
the base component class with new attributes
and methods.
"""

import my_engine.entity as ent

import logging
import uuid


class Component:
    """
    Component defines the base attributes and methods
    for all component types.
    """
    def __init__(self, component_type: str, owner: "ent.Entity") -> None:

        # set a pointer to the owning entity, so we can
        # query it for state
        self.owner = owner

        # uniquely identify each component
        self.component_id = uuid.uuid4()

        self.component_type = component_type
        if self.component_type == "":
            raise "tried to create component without specifying its type"

        self.is_enabled = True

        logging.info(f"initialized component: '{self.component_type}' - {self.component_id}")

    def get_id(self) -> str:
        return str(self.component_id)

    def get_type(self) -> str:
        return self.component_type

    def is_enabled(self):
        return self.is_enabled

    def enable(self):
        self.is_enabled = True

    def disable(self):
        self.is_enabled = False

    def on_load(self):
        """
        called when first loading a scene
        """
        pass

    def update(self):
        """
        called each frame during update sequence
        """
        if not self.is_enabled:
            return

    def draw(self):
        """
        called each frame during draw sequence
        """
        if not self.is_enabled:
            return

    def on_exit(self):
        """
        called when exiting a scene
        """
        pass
