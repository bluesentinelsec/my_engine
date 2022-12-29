import my_engine.game
import my_engine.entity
import my_engine.scene
import my_engine.transitions

import alien

from typing import List
import pygame

class Scene(my_engine.scene.Scene):
    def __init__(self, game: "my_engine.game.MyGame") -> None:
        super().__init__(game)

    def on_load(self):
        my_engine.transitions.fade_in(self.game)
        
        # load entities
        self.add_entity(alien.Alien(ent_type="alien", game=self.game, parent_scene=self))
        

    def on_exit(self):
        my_engine.transitions.fade_out(self.game)