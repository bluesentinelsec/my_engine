import my_engine.entity
import my_engine.game
import my_engine.scene
import my_engine.scene_manager

import pygame

class Opponent(my_engine.entity.Entity):
    def __init__(self, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        super().__init__(game, parent_scene)
        
        self.set_image("media/paddle.png")
        self.set_x_position(self.game.screen_w - 16 - self.rect.width)
        self.set_y_position(self.game.screen_h / 2)
        self.speed = 0.45
        self.group = "opponent"
        

    def update(self):
        self.check_keyboard()

        if self.get_y_position() < 0:
            self.set_y_position(0)

        if self.get_y_position() > self.game.screen_h:
            self.set_y_position(self.game.screen_h - self.rect.height)
        
    def check_keyboard(self):
        key_state = pygame.key.get_pressed()
        
        if key_state[pygame.K_UP]:
            self.rect.y -= self.speed * self.game.delta_time

        if key_state[pygame.K_DOWN]:
            self.rect.y += self.speed * self.game.delta_time

        if key_state[pygame.K_ESCAPE]:
            self.game.quit_game()