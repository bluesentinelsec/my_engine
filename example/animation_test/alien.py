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
        self.printer = my_engine.screen_print.ScreenPrinter(self.game.screen)
        self.alien_animator = my_engine.animation.Animator(self.game)
        self.alien_animator.init_animation(self.get_image(), 16, 16, 2)
        self.kb = my_engine.keyboard.Keyboard()

    def update(self):


        if self.kb.is_key_pressed_once(pygame.K_ESCAPE):
            self.game.quit_game()

        if self.kb.is_key_pressed_once(pygame.K_RETURN):
            print("it worked!")

        
            #self.alien_animator.play_animation(frame_duration=500)
            

        
            #self.alien_animator.stop_animation()

    def draw(self):
        # self.game.screen.blit(self.get_image(), self.get_rect())
        self.alien_animator.draw_animation(self.get_rect())
        self.printer.print(f"Delta time: {self.game.delta_time}")
