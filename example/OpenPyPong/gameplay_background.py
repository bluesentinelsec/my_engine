import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene


class Background(ent.Entity):
    def __init__(self, ent_type: str, game: "game.Game", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/images/background.png")
        self.set_x_position(0)
        self.set_y_position(0)
