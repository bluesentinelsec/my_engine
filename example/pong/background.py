import my_engine.entity
import my_engine.game
import my_engine.scene
import my_engine.scene_manager

class Background(my_engine.entity.Entity):
    def __init__(self, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        super().__init__(game, parent_scene)
        
        super().set_image("media/background.png")
        self.group = "background"