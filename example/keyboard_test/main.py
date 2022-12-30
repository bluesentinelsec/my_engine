import pygame
import os
import sys

# gross hack to import from parent directories
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
import my_engine.screen_print
import my_engine.keyboard

def mock_update():
    if my_engine.keyboard.is_key_pressed_once(pygame.K_RETURN):
        print("it worked?")


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((320, 200))
    print_str = my_engine.screen_print.ScreenPrinter(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill((0, 0, 0))

        mock_update()

        pygame.display.flip()

if __name__ == "__main__":
    main()