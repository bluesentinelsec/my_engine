import my_engine.entity
import my_engine.game
import my_engine.scene
import my_engine.scene_manager

import pygame

class Player(my_engine.entity.Entity):
    def __init__(self, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        super().__init__(game, parent_scene)
        
        super().set_image("media/paddle.png")
        self.speed = 0.45
        self.set_x_position(16)
        self.set_y_position(self.game.screen_h / 2)
        self.group = "player"

    def update(self):
        self.check_keyboard()

        if self.get_y_position() < 0:
            self.set_y_position(0)

        if self.get_y_position() > self.game.screen_h:
            move = self.game.screen_h - self.rect.height
            self.set_y_position(move)
        
    def check_keyboard(self):
        key_state = pygame.key.get_pressed()
        
        if key_state[pygame.K_w]:
            self.rect.y -= self.speed * self.game.delta_time

        if key_state[pygame.K_s]:
            self.rect.y += self.speed * self.game.delta_time

        if key_state[pygame.K_ESCAPE]:
            self.game.quit_game()