import logging
import pygame

last_key_state = -1
last_release_state = -1


def is_key_pressed_once(py_key: int) -> bool:
    """
    check if a key has been pressed once
    """
    global last_key_state
    key_state = pygame.key.get_pressed()
    if last_key_state == py_key:
        if key_state[py_key]:
            # key is still pressed
            last_key_state = py_key
            return False
        else:
            # key was just released
            last_key_state = -1
            return False
    else:
        if key_state[py_key]:
            # key was just pressed
            last_key_state = py_key
            return True
        else:
            # nothing is pressed
            last_key_state = -1
            return False


def is_key_down(py_key: int) -> bool:
    """
    check if a key is being pressed
    """
    key_state = pygame.key.get_pressed()
    if key_state[py_key]:
        return True


def is_key_up(py_key: int) -> bool:
    """
    check if a key is NOT being pressed
    """
    key_state = pygame.key.get_pressed()
    if key_state[py_key]:
        return False

    return False
