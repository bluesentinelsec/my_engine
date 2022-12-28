import my_engine.entity
import my_engine.scene

import background
import player
import opponent
import ball

from typing import List


class Scene(my_engine.scene.Scene):
    def __init__(self, game: my_engine.game.MyGame) -> None:
        super().__init__(game)

    def on_load(self):
        # create background entity
        self.add_entity(background.Background(game=self.game, parent_scene=self))
        self.add_entity(player.Player(game=self.game, parent_scene=self))
        self.add_entity(opponent.Opponent(game=self.game, parent_scene=self))
        self.add_entity(ball.Ball(game=self.game, parent_scene=self))