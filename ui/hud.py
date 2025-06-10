# ui/hud.py

import pygame
from config import WINDOW_WIDTH, HUD_HEIGHT

def draw_hud(surface):
    hud_rect = pygame.Rect(0, 0, WINDOW_WIDTH, HUD_HEIGHT)
    pygame.draw.rect(surface, (20, 20, 20), hud_rect)

    font = pygame.font.SysFont(None, 24)
    text = font.render('Resources | Time | Colonists', True, (255, 255, 255))
    surface.blit(text, (10, 10))
