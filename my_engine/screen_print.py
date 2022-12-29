import pygame


class ScreenPrinter():
    def __init__(self, backbuffer: pygame.Surface) -> None:
        self.font = pygame.font.Font(None, 30)
        self.color = pygame.Color(255, 255, 255, 255)
        self.x_pos = 10
        self.y_pos = 10
        self.backbuffer = backbuffer

    def print(self, text, x_pos=10, y_pos=10):
        self.x_pos = x_pos
        self.y_pos = y_pos
        text_bmp = self.font.render(text, False, self.color)
        self.backbuffer.blit(text_bmp, (self.x_pos, self.y_pos))


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 200))
    screen_printer = ScreenPrinter(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen.fill((0,0,0))
        screen_printer.print("this is a test")
        pygame.display.flip()
        pygame.time.delay(3000)
        break

if __name__ == "__main__":
    main()
