import pygame

from my_engine import my_game


def test_set_window_size():
    game = my_game.MyGame()
    width = 320
    height = 200
    game.set_window_size(width, height)
    x = game.get_window_width()
    y = game.get_window_height()
    assert width == x
    assert height == y
    game.quit_game()

def test_create_window():
    game = my_game.MyGame()
    game.set_window_size(320, 200)
    game.create_window()
    pygame.time.delay(50)
    game.close_window()
    game.quit_game()

def test_create_window_full_screen():
    game = my_game.MyGame()
    game.set_window_size(320, 200)
    game.enable_fullscreen()
    game.create_window()
    pygame.time.delay(50)
    game.close_window()
    game.quit_game()

def test_easy_init():
    game = my_game.MyGame()
    game.easy_init(320, 200, False)
    pygame.time.delay(50)
    game.quit_game()
