# from scenes import scene_base

import pygame


class MyGame:
    def __init__(self) -> None:
        self.screen_width: int = 0
        self.screen_height: int = 0
        self.is_full_screen: bool = False
        self.game_is_running: bool = True
        self.back_buffer: pygame.Surface = None
        self.game_clock: pygame.time.Clock = None
        self.delta_time = 0
        self.fps = 60
        # pointer to scene manager
        # pointer to media manager

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
        self.back_buffer = pygame.display.set_mode(win_size, win_flags)

    def close_window(self):
        pygame.display.quit()

    def run_game(self):

        while self.game_is_running:

            self.delta_time = self.game_clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        is_game_running = False

            # update game objects

            # clear backbuffer
            self.back_buffer.fill((0, 0, 0))

            # draw game objects

            # flip back buffer
            pygame.display.update()

    def quit_game(self):
        pygame.quit()
