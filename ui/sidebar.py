# ui/sidebar.py

import pygame
from config import SIDEBAR_WIDTH, HUD_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT

def draw_sidebar(surface):
    rect = pygame.Rect(
        WINDOW_WIDTH - SIDEBAR_WIDTH,
        HUD_HEIGHT,
        SIDEBAR_WIDTH,
        WINDOW_HEIGHT - HUD_HEIGHT
    )
    pygame.draw.rect(surface, (25, 25, 25), rect)
    pygame.draw.line(surface, (60, 60, 60),
                     (WINDOW_WIDTH - SIDEBAR_WIDTH, HUD_HEIGHT),
                     (WINDOW_WIDTH - SIDEBAR_WIDTH, WINDOW_HEIGHT))

    # Placeholder text content
    font = pygame.font.SysFont(None, 22)
    text_lines = [
        "BUILD MENU",
        "-------------------",
        "Habitat     [80]",
        "Solar Panel [30]",
        "Battery     [20]",
        "O2 Gen      [50]",
        "H2O Extract [50]",
        "Greenhouse  [70]",
        "Mat. Harv   [90]",
        "Storage     [40]",
        "Med Bay     [60]"
    ]

    for i, line in enumerate(text_lines):
        label = font.render(line, True, (255, 255, 255))
        surface.blit(label, (WINDOW_WIDTH - SIDEBAR_WIDTH + 10, HUD_HEIGHT + 10 + i * 24))
