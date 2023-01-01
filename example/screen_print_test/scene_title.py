import my_engine.game as engine
import my_engine.scene as parent
import my_engine.transitions as transitions

import background

from typing import List


class Scene(parent.Scene):
    def __init__(self, game: "engine.MyGame") -> None:
        super().__init__(game)

    def on_load(self):
        transitions.fade_in(self.game)

        # load entities and add to scene
        background_ent = background.Background(
            "background", self.game, parent_scene=self)

        self.add_entity(background_ent)

    def on_exit(self):
        transitions.fade_out(self.game)
