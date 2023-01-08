import logging
import pygame


class KeyBoard:
    def __init__(self) -> None:
        self.last_key_state = -1

    def is_key_pressed_once(self, py_key: int) -> bool:
        """
        Returns true if the key is pressed one time.
        Will not return true until the user releases 
        the key and presses it again.
        The developer should pass in a pygame key
        value such as 'pygame.K_UP'.
        """

        key_state = pygame.key.get_pressed()

        if self.last_key_state == py_key:
            if key_state[py_key]:
                # key is still pressed
                self.last_key_state = py_key
                return False
            else:
                # key was just released
                logging.debug(f"key {py_key} was just released")
                self.last_key_state = -1
                return False
        else:
            if key_state[py_key]:
                # key was just pressed
                logging.debug(f"key {py_key} was just pressed")
                self.last_key_state = py_key
                return True
            else:
                # nothing is pressed
                return False


    def is_key_down(self, py_key: int) -> bool:
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


    def is_key_up(self, py_key: int) -> bool:
        """
        Returns true if a key is NOT being pressed.
        The developer should pass in a pygame key
        value such as 'pygame.K_UP'.
        """
        key_state = pygame.key.get_pressed()
        if key_state[py_key]:
            return False

        return False