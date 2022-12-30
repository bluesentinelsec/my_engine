import my_engine.game as engine
import my_engine.media

import pygame


class ScreenPrinter():
    def __init__(self, engine: "engine.MyGame") -> None:
        self.font_size = 30
        self.font = pygame.font.Font(None, self.font_size)
        self.color = pygame.Color(255, 255, 255, 255)
        self.x_pos = 10
        self.y_pos = 10
        self.engine = engine

    def print(self, text, x_pos=10, y_pos=10):
        self.x_pos = x_pos
        self.y_pos = y_pos
        text_bmp = self.font.render(text, False, self.color)
        self.engine.screen.blit(text_bmp, (self.x_pos, self.y_pos))

    def set_font(self, font_file):
        font_bytes = self.engine.media_manager.get_file(font_file)
        self.font = pygame.font.Font(font_bytes, self.font_size)

    def set_font_size(self, font_size):
        self.font_size = font_size

    def set_font_color(self, color: pygame.Color):
        self.color = color


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 200))
    screen_printer = ScreenPrinter(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen.fill((0, 0, 0))
        screen_printer.print("this is a test")
        pygame.display.flip()
        pygame.time.delay(3000)
        break


if __name__ == "__main__":
    main()
