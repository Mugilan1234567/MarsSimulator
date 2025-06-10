# module.py

import pygame

class ModuleType:
    def __init__(self, name, size, color, cost):
        self.name = name
        self.width, self.height = size
        self.color = color
        self.cost = cost

# Registry of module types
MODULE_TYPES = {
    "Habitat": ModuleType("Habitat", (3, 3), (255, 170, 0), 80),
    "Solar Panel": ModuleType("Solar Panel", (3, 2), (255, 255, 100), 30),
    "Battery": ModuleType("Battery", (3, 2), (100, 200, 255), 20),
    "O2 Gen": ModuleType("O2 Gen", (3, 3), (150, 255, 200), 50),
    "H2O Extract": ModuleType("H2O Extract", (3, 3), (120, 180, 255), 50),
    "Greenhouse": ModuleType("Greenhouse", (3, 3), (130, 255, 130), 70),
    "Mat. Harv": ModuleType("Mat. Harv", (3, 2), (200, 120, 255), 90),
    "Storage": ModuleType("Storage", (3, 3), (255, 120, 120), 40),
    "Med Bay": ModuleType("Med Bay", (3, 2), (255, 200, 180), 60)
}

class PlacedModule:
    def __init__(self, module_type, row, col):
        self.type = module_type  # ModuleType object
        self.row = row
        self.col = col

