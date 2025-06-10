# game.py

import pygame
from grid import Grid
from ui.hud import draw_hud
from ui.sidebar import draw_sidebar
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Mars Colony Engineering Simulator")
        self.clock = pygame.time.Clock()
        self.running = True

        self.grid = Grid()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Phase B will add interactivity here

    def draw(self):
        self.screen.fill((10, 10, 10))
        self.grid.draw(self.screen)
        draw_hud(self.screen)
        draw_sidebar(self.screen)
