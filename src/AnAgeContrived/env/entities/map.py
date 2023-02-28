import random
from .map_data import map, bridges, areas


class Map:
    def __init__(self):
        self.map: map = map
        self.bridges: bridges = bridges
        self.areas: areas = areas
        self.starting_positions: list[int] = [1, 8, 15, 22, 28]
        random.shuffle(self.starting_positions)
