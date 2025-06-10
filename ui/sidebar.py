# ui/sidebar.py

import pygame
from config import SIDEBAR_WIDTH, HUD_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT

# Store clickable areas
clickable_modules = []

def draw_sidebar(surface, selected=None):
    global clickable_modules
    clickable_modules = []

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

    font = pygame.font.SysFont(None, 22)
    text_lines = [
        "Habitat", "Solar Panel", "Battery", "O2 Gen",
        "H2O Extract", "Greenhouse", "Mat. Harv", "Storage", "Med Bay"
    ]

    for i, name in enumerate(text_lines):
        y = HUD_HEIGHT + 10 + i * 28
        label = font.render(name, True, (255, 255, 255))
        label_rect = label.get_rect(topleft=(WINDOW_WIDTH - SIDEBAR_WIDTH + 10, y))
        clickable_modules.append((label_rect, name))

        # Highlight if selected
        if selected == name:
            pygame.draw.rect(surface, (80, 80, 80), label_rect.inflate(6, 6))

        surface.blit(label, label_rect)

def check_sidebar_click(mouse_pos):
    for rect, name in clickable_modules:
        if rect.collidepoint(mouse_pos):
            return name
    return None
