import logging

import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene

import score
import scene_win
import scene_lose

import pygame


class Ball(ent.Entity):
    def __init__(self, ent_type: str, game: "game.MyGame", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/images/ball.png")

        self.set_x_position(self.game.screen_w / 2)
        self.set_y_position(self.game.screen_h / 2)

        self.move_up = -1
        self.move_down = 1
        self.move_left = -1
        self.move_right = 1
        self.direction_x = self.move_left
        self.direction_y = self.move_down
        self.starting_speed = 0.15
        self.speed = self.starting_speed

        self.players = self.parent_scene.get_entities_of_type("player")
        self.opponents = self.parent_scene.get_entities_of_type("opponent")
        self.player_score_ptr: score.Score = None
        self.opponent_score_ptr: score.Score = None

        self.reset_timer = 0  # milliseconds
        self.ball_is_offscreen = False

        self.should_increment_score = True
        self.on_first_frame = True

        self.win_scene: "scene_win.Scene" = scene_win.Scene(self.game)
        self.lose_scene: "scene_lose.Scene" = scene_lose.Scene(self.game)

        # load sounds
        self.launch_ball = self.game.media_manager.get_file(
            "media/sound/start_round.wav")
        self.bounce_wall = self.game.media_manager.get_file(
            "media/sound/bounce_wall.wav")
        self.bounce_paddle = self.game.media_manager.get_file(
            "media/sound/bounce_paddle.wav")

        self.launch_ball = pygame.mixer.Sound(self.launch_ball)
        self.bounce_wall = pygame.mixer.Sound(self.bounce_wall)
        self.bounce_paddle = pygame.mixer.Sound(self.bounce_paddle)

        self.launch_ball.set_volume(0.2)
        self.bounce_wall.set_volume(0.2)
        self.bounce_paddle.set_volume(0.2)
        self.launch_ball.play()

    def update(self):
        # delta time is erratic on first frame
        # and that screws up all ball mechanics
        # so we implement this hack to fix it
        if self.on_first_frame:
            self.on_first_frame = False
            return

        # check collision with player/opponent
        self.handle_collisions()

        self.update_scores()

        # check if ball if offscreen
        if self.get_x_position() < 0 or self.get_x_position() > self.game.get_screen_width():
            self.ball_is_offscreen = True

        # increment reset timer if ball is off screen
        if self.ball_is_offscreen:
            self.reset_timer += self.game.get_delta_time()

        # reset ball after 1 second off screen
        if self.reset_timer >= 1000:
            self.set_x_position(self.game.screen_w / 2)
            self.set_y_position(self.game.screen_h / 2)
            self.direction_x *= -1
            self.speed = self.starting_speed
            self.ball_is_offscreen = False
            self.reset_timer = 0
            self.should_increment_score = True
            self.check_win_lose()
            self.launch_ball.play()

            # Play reset ball sound

        # bounce ball if it hits top of screen
        if self.get_y_position() < 0:
            self.bounce_wall.play()
            self.direction_y = self.move_down

        # bounce ball if it hits bottom of screen
        if self.get_y_position() > self.game.screen_h:
            self.bounce_wall.play()
            self.direction_y = self.move_up

        # update ball position
        self.rect.x += self.direction_x * self.speed * self.game.delta_time
        self.rect.y += self.direction_y * self.speed * self.game.delta_time

    def handle_collisions(self):

        for player in self.players:
            if self.check_collision(player):
                self.direction_x = self.move_right
                self.speed += 0.05
                self.bounce_paddle.play()

        for opponent in self.opponents:
            if self.check_collision(opponent):
                self.direction_x = self.move_left
                self.speed += 0.05
                self.bounce_paddle.play()

    def get_entity_pointers(self):

        player_scores = self.parent_scene.get_entities_of_type("player_score")
        opponent_scores = self.parent_scene.get_entities_of_type(
            "opponent_score")

        for s in player_scores:
            self.player_score_ptr = s

        for s in opponent_scores:
            self.opponent_score_ptr = s

    def update_scores(self):

        # increment opponent score
        if self.get_x_position() < 0:
            if self.should_increment_score:
                self.opponent_score_ptr.inc_score()
                self.should_increment_score = False

        # increment player score
        if self.get_x_position() > self.game.screen_w:
            if self.should_increment_score:
                self.player_score_ptr.inc_score()
                self.should_increment_score = False

    def check_win_lose(self):
        if self.player_score_ptr.score_value == 10:
            self.game.scene_manager.change_scene(self.win_scene)

        if self.opponent_score_ptr.score_value == 10:
            self.game.scene_manager.change_scene(self.lose_scene)
