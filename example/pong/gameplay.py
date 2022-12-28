import my_engine.game
import my_engine.entity
import my_engine.scene
import my_engine.transitions

import background
import player
import opponent
import ball

from typing import List
import pygame

class Scene(my_engine.scene.Scene):
    def __init__(self, game: "my_engine.game.MyGame") -> None:
        super().__init__(game)

    def on_load(self):
        my_engine.transitions.fade_in(self.game)
        
        # load entities
        self.add_entity(background.Background(
            ent_type="background", game=self.game, parent_scene=self))

        self.add_entity(player.Player(
            ent_type="player", game=self.game, parent_scene=self))

        self.add_entity(opponent.Opponent(
            ent_type="opponent", game=self.game, parent_scene=self))

        self.add_entity(
            ball.Ball(ent_type="ball", game=self.game, parent_scene=self))
        

    def on_exit(self):
        my_engine.transitions.fade_out(self.game)