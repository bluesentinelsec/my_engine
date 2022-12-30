# standard library
import logging
import random
import sys

# internal
import my_engine.scene_manager
import my_engine.scene
import my_engine.media
import my_engine.action

# external
import pygame


class MyGame:
    def __init__(self, width: int = 320, height: int = 200, fps_cap: int = 60, fullscreen: bool = True, media_file: str = "data.dat"):
        """
        initialize key game engine components
        """

        logging.debug(
            f"initializing game engine with settings: screen size: {width}x{height} fps: {fps_cap}, fullscreen: {fullscreen}, media file: {media_file}")

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

        try:
            self.screen = pygame.display.set_mode(
                (self.screen_w, self.screen_h), self.flags)
        except Exception as e:
            logging.fatal(e)
            sys.exit(-1)

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
        logging.debug(f"setting starting scene: {scene.name}")
        self.scene_manager.change_scene(scene)

    def run(self):
        """
        run the main game loop
        """

        logging.debug("starting game loop")

        while not self.should_quit_game:

            self.delta_time = self.game_clock.tick(self.fps_cap)

            self.scene_manager.update_scene()

            self.scene_manager.draw_scene()

            # flip the backbuffer
            pygame.display.flip()

        logging.debug("exiting game loop")
        self.scene_manager.pop_scene()
