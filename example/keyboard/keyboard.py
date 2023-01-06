import logging
import my_engine.keyboard as kb

import pygame

RUNNING = True

def demo_keyboard():

    global RUNNING

    if kb.is_key_pressed_once(pygame.K_RETURN):
        logging.info("you pressed the enter key one time!")

    if kb.is_key_pressed_once(pygame.K_SPACE):
        logging.info("you pressed the space bar one time!")

    if kb.is_key_pressed_once(pygame.K_ESCAPE):
        logging.info("you pressed the escape key - exiting!")
        RUNNING = False

    if kb.is_key_down(pygame.K_UP):
        logging.info("you are pressing the up key")

    if kb.is_key_down(pygame.K_DOWN):
        logging.info("you are pressing the down key")

    if kb.is_key_down(pygame.K_LEFT):
        logging.info("you are pressing the left key")

    if kb.is_key_down(pygame.K_RIGHT):
        logging.info("you are pressing the right key")


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    pygame.init()
    screen = pygame.display.set_mode((320, 200))

    global RUNNING
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        demo_keyboard()

        screen.fill((0, 0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()
