import logging

import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene


class Player(ent.Entity):
    def __init__(self, ent_type: str, game: "game.MyGame", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/images/player.png")

        self.set_x_position(16)
        self.set_y_position(self.game.screen_h / 2)
        self.set_speed(0.45)

    def update(self):
        self.check_input()

        if self.get_y_position() < 0:
            self.set_y_position(0)

        if self.get_y_position() + self.rect.height > self.game.screen_h:
            self.set_y_position(self.game.screen_h - self.rect.height)

    def check_input(self):
        # if pressing up
        if self.game.action_handler.is_action_pressed(self.game.action_handler.action_up):
            self.rect.y -= self.speed * self.game.get_delta_time()

        # if pressing down
        if self.game.action_handler.is_action_pressed(self.game.action_handler.action_down):
            self.rect.y += self.speed * self.game.get_delta_time()

        # is escape
        if self.game.action_handler.is_action_pressed_once(self.game.action_handler.action_escape):
            self.game.quit_game()
