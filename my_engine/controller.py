
import pygame
import pygame._sdl2
from pygame._sdl2.controller import Controller

import logging

last_button_state = 1234567


class ControllerWrapper:
    def __init__(self, controller_index=0) -> None:
        self.controller_index = controller_index
        pygame._sdl2.controller.init()
        self.controller_i = None
        try:
            self.controller_i = Controller.from_joystick(
                pygame.joystick.Joystick(0))
            self.controller_i.init()
        except:
            logging.error(
                f"unable to initialize controller: {self.controller_index}")

    def is_button_pressed(self, py_button: int):

        if not self.controller_i:
            return False

        if self.controller_i.get_button(py_button):
            return True
        return False

    def is_button_pressed_once(self, py_button: int):

        if not self.controller_i:
            return False

        global last_button_state
        if py_button == last_button_state:
            if self.is_button_pressed(py_button):
                # button is still pressed
                last_button_state = py_button
                return False
            else:
                # button was released
                last_button_state = 1234567
                return False
        else:
            if self.is_button_pressed(py_button):
                # button was just pressed
                last_button_state = py_button
                return True
            else:
                # nothing is pressed
                last_button_state = 1234567
                return False

    def is_axis_down(self, py_axis):
        axis_state = self.controller_i.get_axis(py_axis)


def main():

    pygame.init()
    screen = pygame.display.set_mode((320, 200))

    # create the controller object
    my_controller = ControllerWrapper(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # test controller
        if my_controller.is_button_pressed(pygame.CONTROLLER_BUTTON_A):
            print("pressed A")

        if my_controller.is_button_pressed_once(pygame.CONTROLLER_BUTTON_B):
            print("pressed B")


if __name__ == "__main__":
    main()
