from .transmuter_tile import TransmuterTile
from env.helpers.constants import INITIAL_ACTION_TOKENS

class Transmuter:
    def __init__(self):

        # TODO: modify the transmuter to actually be filled with the energies
        t1 = TransmuterTile(1, 1)
        t2 = TransmuterTile(1, 1)
        t3 = TransmuterTile(1, 1)
        t4 = TransmuterTile(1, 1)
        t5 = TransmuterTile(2, 1)
        t6 = TransmuterTile(2, 1)
        t7 = TransmuterTile(2, 1)

        self.active_tiles = [t1, t2, t3, t4, t5]
        self.reserved_tiles = [t6, t7]
        self.action_tokens = INITIAL_ACTION_TOKENS

    # gets all the tiles currently on the transmuter
    def get_all_tiles(self):
        pass

    # returns the tile at the given position
    def get_tile(self, position):
        pass

    def get_action_token(self, index):
        return self.action_tokens[index]

    # conveys the transmuter tiles only once, if convey 2 call method twice
    # Upgrade performance here
    def convey(self, reservedTileIndex):
        new_active_tiles = [None, None, None, None, None]
        new_active_tiles[0] = self.reserved_tiles[reservedTileIndex]
        for i in range(len(self.active_tiles)-1):
            new_active_tiles[i+1] = self.active_tiles[i]
        self.active_tiles[4].empty_tile()
        self.reserved_tiles[reservedTileIndex] = self.active_tiles[4]
        self.active_tiles = new_active_tiles

    # helper func to move the tiles after removing a tile

    def _move_all_tiles_ahead(self):
        pass

    def is_full(self):
        pass

    def print_transmuter(self):
        for lines in zip(*map(TransmuterTile.print_tile, self.active_tiles)):
            print(*lines)

    def get_total_energy_cells(self):
        sum = 0
        for tile in self.active_tiles:
            sum += tile.top.count(1)
            sum += tile.bottom.count(1)
        return sum

    def get_total_empty_cells(self):
        sum = 0
        for tile in self.active_tiles:
            sum += tile.top.count(0)
            sum += tile.bottom.count(0)
        return sum
