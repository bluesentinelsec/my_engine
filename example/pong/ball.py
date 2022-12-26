import my_engine.entity
import my_engine.game
import my_engine.scene
import my_engine.scene_manager


class Ball(my_engine.entity.Entity):
    def __init__(self, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        super().__init__(game, parent_scene)

        self.set_image("media/ball.png")
        self.set_x_position(self.game.screen_w / 2)
        self.set_y_position(self.game.screen_h / 2)
        self.group = "ball"

        self.move_up = -1
        self.move_down = 1
        self.move_left = -1
        self.move_right = 1
        self.direction_x = self.move_left
        self.direction_y = self.move_down
        self.speed = 0.15

    def update(self):
        self.handle_collisions()

        if self.get_y_position() < 0:
            self.direction_y = self.move_down

        if self.get_y_position() > self.game.screen_h:
            self.direction_y = self.move_up

        if self.get_x_position() < 0 or self.get_x_position() > self.game.get_screen_width():
            self.set_x_position(self.game.screen_w / 2)
            self.set_y_position(self.game.screen_h / 2)
            self.direction_x *= -1

        self.rect.x += self.direction_x * self.speed * self.game.delta_time
        self.rect.y += self.direction_y * self.speed * self.game.delta_time

        

    def handle_collisions(self):
        # get ptr to player
        players = self.parent_scene.get_entities_by_group("player")
        opponents = self.parent_scene.get_entities_by_group("opponent")

        for player in players:
            if self.check_collision(player):
                self.direction_x = self.move_right
        
        for opponent in opponents:
            if self.check_collision(opponent):
                self.direction_x = self.move_left
        