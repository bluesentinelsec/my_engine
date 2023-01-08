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

        self.keyboard_ptr = my_engine.keyboard.KeyBoard()

    def is_action_pressed(self, action: int):
        key_is_pressed = False
        button_is_pressed = False

        if action == self.action_up:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_UP)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_UP)

        elif action == self.action_down:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_DOWN)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_DOWN)

        elif action == self.action_left:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_LEFT)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_LEFT)

        elif action == self.action_right:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_RIGHT)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_DPAD_RIGHT)

        elif action == self.action_a:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_z)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_A)

        elif action == self.action_b:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_x)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_B)

        elif action == self.action_x:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_a)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_X)

        elif action == self.action_y:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_s)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_Y)

        elif action == self.action_start:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_RETURN)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_START)

        elif action == self.action_select:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_RSHIFT)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_BACK)

        elif action == self.action_escape:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_ESCAPE)
            button_is_pressed = False

        elif action == self.action_left_shoulder:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_c)
            button_is_pressed = self.controller_ptr.is_button_pressed(
                pygame.CONTROLLER_BUTTON_LEFTSHOULDER)

        elif action == self.action_right_shoulder:
            key_is_pressed = self.keyboard_ptr.is_key_down(pygame.K_d)
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
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_UP)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_UP)

        elif action == self.action_down:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_DOWN)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_DOWN)

        elif action == self.action_left:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_LEFT)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_LEFT)

        elif action == self.action_right:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_RIGHT)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_DPAD_RIGHT)

        elif action == self.action_a:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(pygame.K_z)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_A)

        elif action == self.action_b:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(pygame.K_x)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_B)

        elif action == self.action_x:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(pygame.K_a)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_X)

        elif action == self.action_y:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(pygame.K_s)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_Y)

        elif action == self.action_start:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_RETURN)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_START)

        elif action == self.action_select:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_RSHIFT)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_BACK)

        elif action == self.action_escape:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(
                pygame.K_ESCAPE)
            button_is_pressed = False

        elif action == self.action_left_shoulder:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(pygame.K_c)
            button_is_pressed = self.controller_ptr.is_button_pressed_once(
                pygame.CONTROLLER_BUTTON_LEFTSHOULDER)

        elif action == self.action_right_shoulder:
            key_is_pressed = self.keyboard_ptr.is_key_pressed_once(pygame.K_d)
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
