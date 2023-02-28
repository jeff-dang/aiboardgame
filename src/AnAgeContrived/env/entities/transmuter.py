from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    # from env.entities.energy import EnergyTile
    pass

from env.entities.transmuter_tile import TransmuterTile
from env.helpers.constants import INITIAL_ACTION_TOKENS

class Transmuter:
    def __init__(self):

        # TODO: modify the transmuter to actually be filled with the energies
        t1: TransmuterTile = TransmuterTile(1, 1)
        t2: TransmuterTile = TransmuterTile(1, 1)
        t3: TransmuterTile = TransmuterTile(1, 1)
        t4: TransmuterTile = TransmuterTile(1, 1)
        t5: TransmuterTile = TransmuterTile(2, 1)
        t6: TransmuterTile = TransmuterTile(2, 1)
        t7: TransmuterTile = TransmuterTile(2, 1)

        self.active_tiles: list[TransmuterTile] = [t1, t2, t3, t4, t5]
        self.reserved_tiles: list[TransmuterTile] = [t6, t7]
        self.action_tokens: list = INITIAL_ACTION_TOKENS

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
    def convey(self, player: Player, reservedTileIndex: int):
        new_active_tiles: list[TransmuterTile] = [None, None, None, None, None]
        new_tile: TransmuterTile = self.reserved_tiles[reservedTileIndex]
        #FILL NEW TRANSMUTER TILE
        for i in player.exhausted_energies:
            if len(player.exhausted_energies[i]) > 0:
                num_empty_top_sections = new_tile.top.count(0)
                num_empty_bottom_sections = new_tile.bottom.count(0)
                if  num_empty_bottom_sections > 0:
                    new_tile.fill_tile(player.exhausted_energies[i].pop(), 2)
                    print('NEW TILE BOTTOM FILLED')
                elif num_empty_top_sections > 0:
                    new_tile.fill_tile(player.exhausted_energies[i].pop(), 1)
                    print('NEW TILE TOP FILLED')
        new_active_tiles[0] = new_tile                 
        for i in range(len(self.active_tiles)-1):
            new_active_tiles[i+1] = self.active_tiles[i]
        self.active_tiles[4].empty_tile(player)
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

    def print_energies(self):
        energies = {'top_energies': {0: [], 1: [], 2: [], 3: [], 4: []}, 'bottom_energies': {0: [], 1: [], 2: [], 3: [], 4: []}}
        for index in range(0, len(self.active_tiles)):
            for i in self.active_tiles[index].top:
                energies['top_energies'][index].append(i)
            for i in self.active_tiles[index].top:
                energies['bottom_energies'][index].append(i)
        return energies

    def get_total_energy_cells(self) -> int:
        sum = 0
        for tile in self.active_tiles:
            sum += tile.top.count(1)
            sum += tile.bottom.count(1)
        return sum

    def get_total_empty_cells(self) -> int:
        sum = 0
        for tile in self.active_tiles:
            sum += tile.top.count(0)
            sum += tile.bottom.count(0)
        return sum
