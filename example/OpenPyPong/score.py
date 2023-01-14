import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene
import my_engine.screen_print as sp

import pygame

class Score(ent.Entity):
    def __init__(self, ent_type: str, game: "game.Game", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.score_value = 0
        self.xpos = 0
        self.ypos = 0

        self.title = sp.ScreenPrinter(game)
        self.title.set_font_size(28)
        self.title.set_font("media/font/retro_font.ttf")

        self.tick_score_sound = self.game.media_manager.get_file("media/sound/menu_select.wav")
        self.tick_score_sound = pygame.mixer.Sound(self.tick_score_sound)
        self.tick_score_sound.set_volume(0.2)

    def draw(self):
        self.title.print(f"{self.score_value}", self.xpos, self.ypos)

    def set_x_position(self, x_pos):
        self.xpos = x_pos

    def set_y_position(self, y_pos):
        self.ypos = y_pos

    def inc_score(self):
        self.score_value += 1
        self.tick_score_sound.play()