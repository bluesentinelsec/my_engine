import my_engine.game as engine
import my_engine.scene as parent
import my_engine.transitions as transitions

from typing import List

# import needed entities
import lose_msg
import end_cursor

import pygame

class Scene(parent.Scene):
    def __init__(self, game: "engine.MyGame") -> None:
        super().__init__(game)

    def on_load(self):

        transitions.fade_in(self.game)

        # load entities and add to scene
        lose_ent = lose_msg.LoseMsg("lose_msg", self.game, parent_scene=self)
        self.add_entity(lose_ent)

        cursor_ent = end_cursor.Cursor("cursor", self.game, parent_scene=self)
        self.add_entity(cursor_ent)

        lose_sound = self.game.media_manager.get_file("media/sound/you_lose.wav")
        lose_sound = pygame.mixer.Sound(lose_sound)
        lose_sound.set_volume(0.4)
        lose_sound.play()

    def on_exit(self):
        transitions.fade_out(self.game)
