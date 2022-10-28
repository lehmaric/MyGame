import pygame

class Game:

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode([500, 500])

    def run(self):
        pygame.init()
        self.screen.fill((0,0,0))

        while self.running:
            self.check_close_button_pressed()
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

        pygame.quit()

    def check_close_button_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
