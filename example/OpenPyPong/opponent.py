import logging

import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene


class Opponent(ent.Entity):
    def __init__(self, ent_type: str, game: "game.MyGame", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/images/opponent.png")

        self.set_x_position(self.game.screen_w - 16 - self.get_rect().width)
        self.set_y_position(self.game.screen_h / 2)
        self.set_speed(0.18)

        self.ball_ptr: ent.Entity = None

    def update(self):
        if self.get_y_position() < 0:
            self.set_y_position(0)

        if self.get_y_position() + self.rect.height > self.game.screen_h:
            self.set_y_position(self.game.screen_h - self.rect.height)

        # if ball is higher than opponent, move up
        if self.ball_ptr.get_y_position() < self.get_y_position():
            self.rect.y -= 1 * self.speed * self.game.delta_time

        # if ball is lower, move down
        if self.ball_ptr.get_y_position() > self.get_y_position():
            self.rect.y += 1 * self.speed * self.game.delta_time

    def set_ball_ptr(self, ball: ent.Entity):
        self.ball_ptr = ball
