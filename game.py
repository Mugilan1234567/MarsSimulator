# game.py

import pygame
from grid import Grid
from ui.hud import draw_hud
from ui.sidebar import draw_sidebar, check_sidebar_click
from module import MODULE_TYPES
from module import PlacedModule
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, TILE_SIZE, SIDEBAR_WIDTH, HUD_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Mars Colony Engineering Simulator")
        self.clock = pygame.time.Clock()
        self.running = True

        self.grid = Grid()
        self.selected_module = None
        self.placed_modules = {}  # (row, col): module
        self.module_anchors = []  # [(row, col, module)
        self.mouse_tile_pos = None

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if event.pos[0] >= WINDOW_WIDTH - SIDEBAR_WIDTH:
                        name = check_sidebar_click(event.pos)
                        if name in MODULE_TYPES:
                            self.selected_module = name
                    else:
                        self.try_place_module(event.pos)
                elif event.button == 3:  # Right-click
                    print("Selection canceled.")
                    self.selected_module = None

    def update(self):
        mx, my = pygame.mouse.get_pos()
        col = mx // TILE_SIZE
        row = (my - HUD_HEIGHT) // TILE_SIZE
        if 0 <= row < len(self.grid.tiles) and 0 <= col < len(self.grid.tiles[0]):
            self.mouse_tile_pos = (row, col)
        else:
            self.mouse_tile_pos = None

    def try_place_module(self, mouse_pos):
        if not self.selected_module or not self.mouse_tile_pos:
            return

        module_type = MODULE_TYPES[self.selected_module]
        row, col = self.mouse_tile_pos

        # Bounds check
        if row + module_type.height > len(self.grid.tiles) or col + module_type.width > len(self.grid.tiles[0]):
            print("Rejected: Out of bounds")
            return

        # Validate footprint
        for dy in range(module_type.height):
            for dx in range(module_type.width):
                r, c = row + dy, col + dx
                tile = self.grid.tiles[r][c]

                if (r, c) in self.placed_modules:
                    print(f"Rejected: Overlaps at ({r}, {c})")
                    return

                if tile.type == "mountain":
                    print(f"Rejected: Mountain at ({r}, {c})")
                    return

                if module_type.name == "H2O Extract":
                    if tile.type != "ice":
                        print(f"Rejected: Must be on ice at ({r}, {c})")
                        return
                else:
                    if tile.type == "ice":
                        print(f"Rejected: Can't build on ice at ({r}, {c})")
                        return

        # Place only the anchor and mark occupied tiles
        for dy in range(module_type.height):
            for dx in range(module_type.width):
                self.placed_modules[(row + dy, col + dx)] = True

        self.module_anchors.append(PlacedModule(module_type, row, col))
        print(f"Placed module: {module_type.name} at ({row}, {col})")

    def draw(self):
        self.screen.fill((10, 10, 10))
        self.grid.draw(self.screen)
        self.draw_modules()
        self.draw_ghost()
        draw_hud(self.screen, selected_module=self.selected_module)
        draw_sidebar(self.screen, selected=self.selected_module)

    def draw_modules(self):
        font = pygame.font.SysFont(None, 16)

        for mod in self.module_anchors:
            module = mod.type
            row = mod.row
            col = mod.col

            x = col * TILE_SIZE
            y = row * TILE_SIZE + HUD_HEIGHT
            width = module.width * TILE_SIZE
            height = module.height * TILE_SIZE

            if x + width > WINDOW_WIDTH - SIDEBAR_WIDTH or y + height > WINDOW_HEIGHT:
                continue

            rect = pygame.Rect(x, y, width, height)
            pygame.draw.rect(self.screen, module.color, rect, border_radius=6)

            # Text rendering
            max_label_width = width - 6
            font_size = 16
            while font_size >= 10:
                font = pygame.font.SysFont(None, font_size)
                label = font.render(module.name, True, (0, 0, 0))
                if label.get_width() <= max_label_width:
                    break
                font_size -= 1

            label_text = module.name
            while label.get_width() > max_label_width and len(label_text) > 3:
                label_text = label_text[:-1] + "…"
                label = font.render(label_text, True, (0, 0, 0))

            label_x = x + (width - label.get_width()) // 2
            label_y = y + (height - label.get_height()) // 2

            if 0 <= label_x <= WINDOW_WIDTH - SIDEBAR_WIDTH - label.get_width() and 0 <= label_y <= WINDOW_HEIGHT - label.get_height():
                self.screen.blit(label, (label_x, label_y))

    def draw_ghost(self):
        if not self.selected_module or not self.mouse_tile_pos:
            return

        module = MODULE_TYPES[self.selected_module]
        row, col = self.mouse_tile_pos
        font = pygame.font.SysFont(None, 16)

        # Bounds check first
        if row + module.height > len(self.grid.tiles) or col + module.width > len(self.grid.tiles[0]):
            return

        # Validation
        for dy in range(module.height):
            for dx in range(module.width):
                r = row + dy
                c = col + dx
                tile = self.grid.tiles[r][c]

                if (r, c) in self.placed_modules or tile.type == "mountain":
                    return
                if module.name == "H2O Extract" and tile.type != "ice":
                    return
                if module.name != "H2O Extract" and tile.type == "ice":
                    return

        # Draw ghost
        alpha = 100
        ghost_surface = pygame.Surface((module.width * TILE_SIZE, module.height * TILE_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(ghost_surface, (*module.color, alpha), ghost_surface.get_rect(), border_radius=4)
        self.screen.blit(ghost_surface, (col * TILE_SIZE, row * TILE_SIZE + HUD_HEIGHT))

        label = font.render(module.name, True, (0, 0, 0))
        self.screen.blit(label, (col * TILE_SIZE + 4, row * TILE_SIZE + HUD_HEIGHT + 2))
