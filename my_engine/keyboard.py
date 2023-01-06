import logging
import pygame

# keeps track of key state between function invocations
last_key_state = -1


def is_key_pressed_once(py_key: int) -> bool:
    """
    Returns true if the key is pressed one time.
    Will not return true until the user releases 
    the key and presses it again.
    The developer should pass in a pygame key
    value such as 'pygame.K_UP'.
    """
    global last_key_state

    logging.debug("getting keyboard state")
    key_state = pygame.key.get_pressed()

    if last_key_state == py_key:
        if key_state[py_key]:
            # key is still pressed
            logging.debug(f"key {py_key} is still pressed")
            last_key_state = py_key
            return False
        else:
            # key was just released
            logging.debug(f"key {py_key} was just released")
            last_key_state = -1
            return False
    else:
        if key_state[py_key]:
            # key was just pressed
            logging.debug(f"key {py_key} was just pressed")
            last_key_state = py_key
            return True
        else:
            # nothing is pressed
            logging.debug(f"no key is pressed currently")
            last_key_state = -1
            return False


def is_key_down(py_key: int) -> bool:
    """
    Returns true if the key is held down.
    The developer should pass in a pygame key
    value such as 'pygame.K_UP'.
    """

    logging.debug("getting keyboard state")
    key_state = pygame.key.get_pressed()
    if key_state[py_key]:
        logging.debug(f"key {py_key} is currently held down")
        return True

    return False


def is_key_up(py_key: int) -> bool:
    """
    Returns true if a key is NOT being pressed.
    The developer should pass in a pygame key
    value such as 'pygame.K_UP'.
    """
    key_state = pygame.key.get_pressed()
    if key_state[py_key]:
        return False

    return False
