from .map_data import map, bridges, areas


class Map:
    def __init__(self):
        self.map = map
        self.bridges = bridges
        self.areas = areas
        self.starting_positions = [1, 8, 15, 22, 28]
