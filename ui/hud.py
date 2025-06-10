# ui/hud.py

import pygame
from config import WINDOW_WIDTH, HUD_HEIGHT

def draw_hud(surface, selected_module=None):
    hud_rect = pygame.Rect(0, 0, WINDOW_WIDTH, HUD_HEIGHT)
    pygame.draw.rect(surface, (20, 20, 20), hud_rect)

    font = pygame.font.SysFont(None, 24)
    base_text = 'Resources | Time | Colonists'
    select_text = f"Selected: {selected_module}" if selected_module else "No module selected"

    text = font.render(base_text, True, (255, 255, 255))
    surface.blit(text, (10, 10))

    select_label = font.render(select_text, True, (180, 180, 180))
    surface.blit(select_label, (350, 10))  # Adjust x if needed
