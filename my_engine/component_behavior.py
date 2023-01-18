"""
TBD
"""

import my_engine.entity as ent
import my_engine.component as cmp


class BehaviorComponent(cmp.Component):
    def __init__(self, owner: "ent.Entity", component_type: str = "behavior") -> None:
        super().__init__(owner=owner, component_type=component_type)

        # read script file from data.dat
        # write script file to disk
        # import script file
    def on_load(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def on_exit(self):
        pass
