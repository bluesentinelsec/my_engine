import logging
import pygame

from my_engine.media_manager import MediaManager
from my_engine.scene_manager import SceneManager
from my_engine.scenes import scene_base

class MyGame:
    def __init__(self, media_file: str) -> None:
        self.screen_width: int = 0
        self.screen_height: int = 0
        self.is_full_screen: bool = False
        self.game_is_running: bool = True
        self.back_buffer: pygame.Surface = None
        self.game_clock: pygame.time.Clock = None
        self.delta_time = 0
        self.fps = 60
        self.scene_manager: SceneManager = SceneManager()
        self.media_manager: MediaManager = MediaManager(media_file=media_file)
        
        pygame.init()
        self.game_clock = pygame.time.Clock()

    def set_window_size(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height

    def get_window_width(self) -> int:
        return self.screen_width

    def get_window_height(self) -> int:
        return self.screen_height

    def enable_fullscreen(self):
        self.is_full_screen = True

    def disable_fullscreen(self):
        self.is_full_screen = False

    def create_window(self):
        win_size = (self.screen_width, self.screen_height)
        win_flags = pygame.RESIZABLE | pygame.SCALED
        if self.is_full_screen:
            win_flags = pygame.RESIZABLE | pygame.SCALED | pygame.FULLSCREEN
        self.back_buffer = pygame.display.set_mode(win_size, win_flags, vsync=1)

    def close_window(self):
        pygame.display.quit()

    
    def easy_init(self, screen_width: int, screen_height: int, fullscreen: bool):
        self.screen_width = screen_width
        self.screen_height = screen_height
        win_size = (self.screen_width, self.screen_height)
        win_flags = pygame.RESIZABLE | pygame.SCALED
        
        if fullscreen:
            win_flags = win_flags | pygame.FULLSCREEN
            self.back_buffer = pygame.display.set_mode(win_size, win_flags)
        else:
            self.back_buffer = pygame.display.set_mode(win_size, win_flags)

    def set_starting_scene(self, the_scene: scene_base.Scene):
        self.scene_manager.change_scene(the_scene)

    def run_game(self):

        while self.game_is_running:

            self.delta_time = self.game_clock.tick(60)

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.game_is_running = False

                if event.type == pygame.WINDOWCLOSE:
                    self.game_is_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    

            # update game objects
            self.scene_manager.update_scene()

            # clear backbuffer
            self.back_buffer.fill((0, 0, 0))

            # draw game objects
            self.scene_manager.draw_scene()

            # flip back buffer
            pygame.display.update()

    def quit_game(self):
        pygame.quit()
