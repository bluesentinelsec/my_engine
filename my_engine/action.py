import my_engine.keyboard
import my_engine.controller
import my_engine.screen_print

import logging
import pygame


class Action:
    def __init__(self, controller_index=0) -> None:
        self.action_up = 1
        self.action_down = 2
        self.action_left = 3
        self.action_right = 4
        self.action_a = 5
        self.action_b = 6
        self.action_x = 7
        self.action_y = 8
        self.action_start = 9
        self.action_select = 10
        self.action_escape = 11
        self.action_left_shoulder = 12
        self.action_right_shoulder = 13

        self.controller_index = controller_index
        self.controller_ptr = my_engine.controller.ControllerWrapper(
            self.controller_index)

    def is_action_pressed(self, action: int):
        key_is_pressed = False
        button_is_pressed = False

        if action == self.action_up:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_UP)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_UP)

        elif action == self.action_down:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_DOWN)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_DOWN)

        elif action == self.action_left:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_LEFT)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_LEFT)

        elif action == self.action_right:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_RIGHT)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_RIGHT)

        elif action == self.action_a:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_z)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_A)

        elif action == self.action_b:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_x)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_B)

        elif action == self.action_x:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_a)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_X)

        elif action == self.action_y:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_s)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_Y)

        elif action == self.action_start:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_RETURN)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_START)

        elif action == self.action_select:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_RSHIFT)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_BACK)

        elif action == self.action_escape:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_ESCAPE)
            button_is_pressed = False

        elif action == self.action_left_shoulder:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_c)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_LEFTSHOULDER)

        elif action == self.action_right_shoulder:
            key_is_pressed = my_engine.keyboard.is_key_down(pygame.K_d)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_RIGHTSHOULDER)

        else:
            logging.error(
                f"invalid action: {action} - see 'my_engine/action.py' for valid actions")

        if button_is_pressed:
            return True

        if key_is_pressed:
            return True

        return False

    def is_action_pressed_once(self, action: int):
        key_is_pressed = False
        button_is_pressed = False

        if action == self.action_up:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_UP)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_UP)

        elif action == self.action_down:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_DOWN)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_DOWN)

        elif action == self.action_left:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_LEFT)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_LEFT)

        elif action == self.action_right:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_RIGHT)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_RIGHT)

        elif action == self.action_a:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(pygame.K_z)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_A)

        elif action == self.action_b:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(pygame.K_x)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_B)

        elif action == self.action_x:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(pygame.K_a)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_X)

        elif action == self.action_y:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(pygame.K_s)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_Y)

        elif action == self.action_start:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_RETURN)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_START)

        elif action == self.action_select:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_RSHIFT)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_BACK)

        elif action == self.action_escape:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(
                pygame.K_ESCAPE)
            button_is_pressed = False

        elif action == self.action_left_shoulder:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(pygame.K_c)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_LEFTSHOULDER)

        elif action == self.action_right_shoulder:
            key_is_pressed = my_engine.keyboard.is_key_pressed_once(pygame.K_d)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_RIGHTSHOULDER)

        else:
            logging.error(
                f"invalid action: {action} - see 'my_engine/action.py' for valid actions")

        if button_is_pressed:
            return True

        if key_is_pressed:
            return True

        return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 200))
    screen_printer = my_engine.screen_print.ScreenPrinter(screen)
    action = Action()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen.fill((0, 0, 0))

        if action.is_action_pressed(action.action_up):
            screen_printer.print("pressed up")

        elif action.is_action_pressed(action.action_down):
            screen_printer.print("pressed down")

        elif action.is_action_pressed(action.action_left):
            screen_printer.print("pressed left")

        elif action.is_action_pressed(action.action_right):
            screen_printer.print("pressed right")

        elif action.is_action_pressed(action.action_a):
            screen_printer.print("pressed a")

        elif action.is_action_pressed(action.action_b):
            screen_printer.print("pressed b")

        elif action.is_action_pressed(action.action_x):
            screen_printer.print("pressed x")

        elif action.is_action_pressed(action.action_y):
            screen_printer.print("pressed y")

        elif action.is_action_pressed(action.action_start):
            screen_printer.print("pressed start")

        elif action.is_action_pressed(action.action_select):
            screen_printer.print("pressed select")

        elif action.is_action_pressed_once(action.action_escape):
            screen_printer.print("pressed escape")
            break

        elif action.is_action_pressed(action.action_left_shoulder):
            screen_printer.print("pressed left shoulder")

        elif action.is_action_pressed(action.action_right_shoulder):
            screen_printer.print("pressed right shoulder")

        else:
            pass

        pygame.display.flip()


if __name__ == "__main__":
    main()
