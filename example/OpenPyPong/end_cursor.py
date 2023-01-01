import logging

import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene

import scene_title
import scene_gameplay

import pygame


class Cursor(ent.Entity):
    def __init__(self, ent_type: str, game: "game.MyGame", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.start_position_x = 70
        self.start_position_y = 100

        self.exit_position_x = 30
        self.exit_position_y = 130

        self.set_image("media/images/cursor.png")

        self.set_x_position(self.start_position_x)
        self.set_y_position(self.start_position_y)

        # load sounds
        menu_select = self.game.media_manager.get_file(
            "media/sound/menu_select.wav")
        self.menu_select = pygame.mixer.Sound(menu_select)
        self.menu_select.set_volume(0.2)

        # load "start game" sound
        start_game_sound = self.game.media_manager.get_file(
            "media/sound/you_win.wav")
        self.start_game_sound = pygame.mixer.Sound(start_game_sound)
        self.start_game_sound.set_volume(0.2)

        # load "exit game" sound
        exit_game_sound = self.game.media_manager.get_file(
            "media/sound/you_lose.wav")
        self.exit_game_sound = pygame.mixer.Sound(exit_game_sound)
        self.exit_game_sound.set_volume(0.2)

    def update(self):
        # move to exit position if at start position
        if self.get_y_position() == self.start_position_y:
            if self.game.action_handler.is_action_pressed_once(self.game.action_handler.action_down):
                self.set_x_position(self.exit_position_x)
                self.set_y_position(self.exit_position_y)
                self.menu_select.play()

        # move to start position if at exit position
        if self.get_y_position() == self.exit_position_y:
            if self.game.action_handler.is_action_pressed_once(self.game.action_handler.action_up):
                self.set_x_position(self.start_position_x)
                self.set_y_position(self.start_position_y)
                self.menu_select.play()

        # quit if you press escape
        if self.game.action_handler.is_action_pressed_once(self.game.action_handler.action_escape):
            self.exit_game_sound.play()
            self.game.quit_game()

        # if cursor is at exit position and user presses enter
        if self.game.action_handler.is_action_pressed_once(self.game.action_handler.action_start):
            if self.get_y_position() == self.exit_position_y:
                self.exit_game_sound.play()
                self.game.scene_manager.change_scene(
                    scene_title.Scene(self.game))

        # if cursor is at start position and user presses enter
            if self.get_y_position() == self.start_position_y:
                self.start_game_sound.play()
                pygame.time.delay(1000)
                self.game.scene_manager.change_scene(
                    scene_gameplay.Scene(self.game))
