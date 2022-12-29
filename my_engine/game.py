# standard library
import logging
import random

# internal
import my_engine.scene_manager
import my_engine.scene
import my_engine.media
import my_engine.action

# external
import pygame


class MyGame:
    def __init__(self, width: int, height: int, fps_cap: int, fullscreen: bool, media_file: str):
        self.screen_w = width
        self.screen_h = height
        self.fps_cap = fps_cap
        self.media_file = media_file
        self.delta_time = 0
        self.game_clock = pygame.time.Clock()
        self.fullscreen = pygame.FULLSCREEN
        self.scale_scaled = pygame.SCALED
        self.resizeable = pygame.RESIZABLE
        self.screen: pygame.Surface = None
        self.should_quit_game = False

        self.flags = self.scale_scaled | self.resizeable

        if fullscreen:
            self.flags = self.scale_scaled | self.resizeable | self.fullscreen

        logging.info(
            f"setting video mode with settings: {self.screen_w}x{self.screen_h} - {self.flags}")
        self.screen = pygame.display.set_mode(
            (self.screen_w, self.screen_h), self.flags)

        self.scene_manager = my_engine.scene_manager.SceneManager()

        self.media_manager = my_engine.media.MediaManager(self.media_file)

        self.action_handler = my_engine.action.Action()

        pygame.font.init()
        
        random.seed()

    def get_screen_width(self):
        return self.screen_w

    def get_screen_height(self):
        return self.screen_h

    def get_delta_time(self):
        return self.delta_time

    def quit_game(self):
        self.should_quit_game = True

    def get_backbuffer(self):
        return self.screen

    def set_starting_scene(self, scene: "my_engine.scene.Scene"):
        self.scene_manager.change_scene(scene)

    def run(self):

        while not self.should_quit_game:
            self.delta_time = self.game_clock.tick(self.fps_cap)

            self.scene_manager.update_scene()

            self.scene_manager.draw_scene()

        self.scene_manager.pop_scene()
