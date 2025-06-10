# grid.py

import pygame
from tile import Tile
from config import GRID_ROWS, GRID_COLS
import random
from perlin_noise import PerlinNoise
seed = random.randint(0, 10000)

class Grid:
    def __init__(self):
        self.tiles = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.generate_terrain()
        self.seed = seed

    def generate_terrain(self):
        # Use fewer octaves for larger blobs, lower frequency
        noise = PerlinNoise(octaves=2, seed=seed)

        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                val = noise([r / 35, c / 35])  # 35 = larger features
                if val > 0.2:
                    tile_type = 'mountain'
                elif val < -0.1:
                    tile_type = 'ice'
                else:
                    tile_type = 'empty'

                self.tiles[r][c] = Tile(r, c, tile_type)


    def draw(self, surface):
        for row in self.tiles:
            for tile in row:
                tile.draw(surface)
