# tile.py

import pygame
from config import TILE_SIZE, HUD_HEIGHT, SIDEBAR_WIDTH, WINDOW_WIDTH

class Tile:
    def __init__(self, row, col, tile_type='empty'):
        self.row = row
        self.col = col
        self.type = tile_type
        self.screen_x = col * TILE_SIZE
        self.screen_y = row * TILE_SIZE

    # tile.py

    def draw(self, surface):
        from config import HUD_HEIGHT, TILE_SIZE
        color = {
            'empty': (139, 69, 19),  # Martian red dirt
            'mountain': (90, 45, 20),  # Volcanic dark rock
            'ice': (200, 225, 235)  # Dusty white ice cap
        }.get(self.type, (60, 60, 60))

        draw_rect = pygame.Rect(
            self.screen_x,
            self.screen_y + HUD_HEIGHT,
            TILE_SIZE,
            TILE_SIZE
        )
        pygame.draw.rect(surface, color, draw_rect)
        pygame.draw.rect(surface, (30, 30, 30), draw_rect, 1)

