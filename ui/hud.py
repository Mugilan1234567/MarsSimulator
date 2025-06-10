import pygame
from config import WINDOW_WIDTH, HUD_HEIGHT

def get_color(val):
    if val <= 20:
        return (255, 100, 100)  # red
    elif val <= 50:
        return (255, 210, 100)  # yellow
    else:
        return (150, 255, 150)  # green

def draw_hud(surface, selected_module=None, hour=0, sol=1, resources=None, colonists=0):
    hud_rect = pygame.Rect(0, 0, WINDOW_WIDTH, HUD_HEIGHT)
    pygame.draw.rect(surface, (20, 20, 20), hud_rect)

    font = pygame.font.SysFont(None, 24)

    # Top line: Sol and Time
    base_text = f'Sol {sol} | Hour {hour:02d}:00'
    time_text = "Daytime" if 6 <= hour <= 17 else "Nighttime"
    select_text = f"Selected: {selected_module}" if selected_module else "No module selected"

    base_label = font.render(base_text, True, (255, 255, 255))
    surface.blit(base_label, (10, 10))

    select_label = font.render(select_text, True, (180, 180, 180))
    surface.blit(select_label, (350, 10))

    time_label = font.render(time_text, True, (100, 200, 255) if time_text == "Daytime" else (180, 180, 255))
    surface.blit(time_label, (650, 10))

    # Bottom line: Resources
    resource_keys = ["Power", "Water", "Oxygen", "Food", "Materials"]
    labels = ["Pwr", "H2O", "O2", "Food", "Mats"]
    x = 10

    for key, label_text in zip(resource_keys, labels):
        val = resources[key]
        color = get_color(val)
        text = f"{label_text}:{val:.0f}"
        rendered = font.render(text, True, color)
        surface.blit(rendered, (x, 30))
        x += rendered.get_width() + 10

    # Colonist count
    pop_text = f'Colonists: {colonists}'
    pop_label = font.render(pop_text, True, (255, 160, 160))
    surface.blit(pop_label, (650, 30))
