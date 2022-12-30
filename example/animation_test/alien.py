import my_engine.entity
import my_engine.game
import my_engine.scene
import my_engine.scene_manager
import my_engine.animation
import my_engine.screen_print
import my_engine.keyboard

import pygame


class Alien(my_engine.entity.Entity):
    def __init__(self, ent_type: str, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/alien_sheet.png")
        self.set_x_position(self.game.screen_w / 2)
        self.set_y_position(self.game.screen_h / 2)
        self.animation_should_play = False
        self.printer = my_engine.screen_print.ScreenPrinter(self.game.screen)
        self.animation = my_engine.animation.Animator(self.game)
        self.animation.init_animation(self.get_image(), 16, 16, 2)

    def update(self):


        if my_engine.keyboard.is_key_pressed_once(pygame.K_ESCAPE):
            self.game.quit_game()

        if my_engine.keyboard.is_key_pressed_once(pygame.K_RETURN):
            self.animation_should_play = True

        if my_engine.keyboard.is_key_pressed_once(pygame.K_RSHIFT):
            self.animation_should_play = False
        
        if self.animation_should_play:
            self.animation.play_animation(frame_duration=500)
            

    def draw(self):
        self.animation.draw_animation(self.get_rect())