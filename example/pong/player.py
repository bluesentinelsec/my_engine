import my_engine.entity
import my_engine.game
import my_engine.scene
import my_engine.scene_manager
import my_engine.transitions
import my_engine.keyboard

import pygame


class Player(my_engine.entity.Entity):
    def __init__(self, ent_type: str, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/paddle.png")
        self.set_x_position(16)
        self.set_y_position(self.game.screen_h / 2)
        self.speed = 0.45

    def update(self):
        self.check_input()

        if self.get_y_position() < 0:
            self.set_y_position(0)

        if self.get_y_position() + self.rect.height > self.game.screen_h:
            move = self.game.screen_h - self.rect.height
            self.set_y_position(move)

    def check_input(self):

        if my_engine.keyboard.is_key_down(pygame.K_w):
            self.rect.y -= self.speed * self.game.delta_time

        if my_engine.keyboard.is_key_down(pygame.K_s):
            self.rect.y += self.speed * self.game.delta_time

        if my_engine.keyboard.is_key_down(pygame.K_ESCAPE):
            self.game.quit_game()
