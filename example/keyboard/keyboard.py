import logging
import my_engine.keyboard as kb

import pygame

def demo_keyboard():
    space_pressed = False
    space_pressed = kb.is_key_pressed_once(pygame.K_SPACE)
    if space_pressed == True:
        logging.info("you pressed the space bar one time!")

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    pygame.init()
    screen = pygame.display.set_mode((320, 200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if kb.is_key_pressed_once(pygame.K_RETURN):
            logging.info("you pressed the enter key one time!")
        demo_keyboard()

        screen.fill((0, 0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()
