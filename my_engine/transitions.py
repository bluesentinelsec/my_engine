import random

import my_engine.game

import pygame


def fade_in(game: my_engine.game.MyGame, color: pygame.color.Color = pygame.color.Color(128, 128, 128, 255)):
    width = game.get_screen_width()
    height = game.get_screen_height()
    t_surface = pygame.Surface((width, height))
    t_surface.fill(color)

    while color.a > 0:
        game.screen.fill((0, 0, 0, 255))
        t_surface.set_alpha(color.a)
        game.screen.blit(t_surface, (0, 0))
        pygame.display.flip()
        color.a -= 1
        pygame.time.delay(2)


def fade_out(game: my_engine.game.MyGame, color: pygame.color.Color = pygame.color.Color(0, 0, 0, 0)):
    width = game.get_screen_width()
    height = game.get_screen_height()
    t_surface = pygame.Surface((width, height))
    t_surface.fill(color)

    for i in range(100):
        t_surface.set_alpha(i)
        game.screen.blit(t_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(5)


def plot_pixels(game: my_engine.game.MyGame):

    width = game.get_screen_width()
    height = game.get_screen_height()
    counter = 0
    cap = 3000
    while counter != cap:

        xpos = random.randint(0, width)
        ypos = random.randint(0, height)
        game.screen.set_at((xpos, ypos), (255, 255, 255))
        counter += 1
        pygame.display.flip()
        # pygame.time.delay(10)

    game.screen.fill((0, 0, 0))
