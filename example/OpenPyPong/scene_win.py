import my_engine.game as engine
import my_engine.scene as parent
import my_engine.transitions as transitions

from typing import List

# import needed entities
import win_msg
import end_cursor

import pygame

class Scene(parent.Scene):
    def __init__(self, game: "engine.MyGame") -> None:
        super().__init__(game)

    def on_load(self):

        transitions.fade_in(self.game)

        # load entities and add to scene
        win_ent = win_msg.WinMsg("win_msg", self.game, parent_scene=self)
        self.add_entity(win_ent)

        cursor_ent = end_cursor.Cursor("cursor", self.game, parent_scene=self)
        self.add_entity(cursor_ent)

        win_sound = self.game.media_manager.get_file("media/sound/you_win.wav")
        win_sound = pygame.mixer.Sound(win_sound)
        win_sound.set_volume(0.4)
        win_sound.play()

    def on_exit(self):
        transitions.fade_out(self.game)
