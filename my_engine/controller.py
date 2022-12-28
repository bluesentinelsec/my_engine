
import pygame
import pygame._sdl2
from pygame._sdl2.controller import Controller


last_button_state = 1234567


class ControllerWrapper:
    def __init__(self, controller_index=0) -> None:
        self.controller_index = controller_index
        pygame._sdl2.controller.init()
        self.controller_i = Controller.from_joystick(
            pygame.joystick.Joystick(0))
        self.controller_i.init()

    def is_button_pressed(self, py_button: int):
        if self.controller_i.get_button(py_button):
            return True
        return False

    def is_button_pressed_once(self, py_button: int):
        global last_button_state
        if py_button == last_button_state:
            if self.is_button_pressed(py_button):
                return False
            else:
                last_button_state = 1234567
                return False
        else:
            if self.is_button_pressed(py_button):
                last_button_state = py_button
                return True
            else:
                last_button_state = 1234567
                return False


def main():


    pygame.init()
    screen = pygame.display.set_mode((320,200))

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
