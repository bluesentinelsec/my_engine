import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene
import my_engine.screen_print as screen_print


class Background(ent.Entity):
    def __init__(self, ent_type: str, game: "game.MyGame", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/images/background.png")
        self.set_x_position(0)
        self.set_y_position(0)

        # set title text
        self.title = screen_print.ScreenPrinter(game)
        self.title.set_font_size(32)
        self.title.set_font("media/font/retro_font.ttf")

        # set start text
        self.start_text = screen_print.ScreenPrinter(game)
        self.start_text.set_font_size(12)
        self.start_text.set_font("media/font/retro_font.ttf")
        


    def draw(self):
        super().draw()
        self.title.print("Open PyPong", x_pos=30, y_pos=30)
        self.start_text.print("Start Game", x_pos=30, y_pos=60)
        