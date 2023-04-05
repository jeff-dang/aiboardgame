# Author: Jonah Ada
# Date: December 12th, 2022
# Description: 
# Module to define the "transmtuer device" entity of the game

from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.entities.energy import EnergyTile
    pass

from env.entities.transmuter_tile import TransmuterTile
from env.helpers.constants import INITIAL_ACTION_TOKENS
from env.helpers.logger import Logger
from random import randint
from env.entities.energy import Energy

# defines the transmuter as an object
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

    # returns theaction tokens associated with the transmtuer device
    def get_action_token(self, index):
        return self.action_tokens[index]

    # conveys the transmuter tiles only once, if convey 2 call method twice
    def convey(self, player: Player, reservedTileIndex: int, fill_energies: list[EnergyTile] = [None, None]):
        new_active_tiles: list[TransmuterTile] = [None, None, None, None, None]
        new_tile: TransmuterTile = self.reserved_tiles[reservedTileIndex]
        
        #FILL NEW TRANSMUTER TILE
        energy_type_top = None
        energy_type_bottom = None
        if fill_energies[0] != None:
            energy_type_top = fill_energies[0]
        if fill_energies[1] != None:
            energy_type_bottom = fill_energies[1]
        
        num_empty_top_sections = new_tile.top.count(0)
        num_empty_bottom_sections = new_tile.bottom.count(0)

        if energy_type_bottom != None:
            if  num_empty_bottom_sections > 0 and len(player.exhausted_energies[energy_type_bottom]) > 0:
                new_tile.fill_tile(player.exhausted_energies[energy_type_bottom].pop(), 2)
                Logger.log('NEW TILE BOTTOM FILLED', 'TRANSMUTER_LOGS')

        if energy_type_top != None:
            if num_empty_top_sections > 0 and len(player.exhausted_energies[energy_type_top]) > 0:
                new_tile.fill_tile(player.exhausted_energies[energy_type_top].pop(), 1)
                Logger.log('NEW TILE TOP FILLED', 'TRANSMUTER_LOGS')

        if energy_type_top != None:
            if num_empty_top_sections > 0 and len(player.energies_released[energy_type_top]) > 0:
                new_tile.fill_tile(player.energies_released[energy_type_top].pop(), 1)
                Logger.log('NEW TILE TOP FILLED', 'TRANSMUTER_LOGS')

        if energy_type_bottom != None:
            if  num_empty_bottom_sections > 0 and len(player.energies_released[energy_type_bottom]) > 0:
                new_tile.fill_tile(player.energies_released[energy_type_bottom].pop(), 2)
                Logger.log('NEW TILE BOTTOM FILLED', 'TRANSMUTER_LOGS')
                        
        new_active_tiles[0] = new_tile                 
        for i in range(len(self.active_tiles)-1):
            new_active_tiles[i+1] = self.active_tiles[i]
        self.active_tiles[4].empty_tile(player)
        self.reserved_tiles[reservedTileIndex] = self.active_tiles[4]
        self.active_tiles = new_active_tiles

    # prints all transmuter tiles of the transmuter in human readable way to be used in the game engine's render method
    def print_transmuter(self):
        for lines in zip(*map(TransmuterTile.print_tile, self.active_tiles)):
            print(*lines)

    # for JSON logging purposes, prints the top and bottom energies binded to the transmuter
    def print_energies(self):
        energies = {'top_energies': {0: [], 1: [], 2: [], 3: [], 4: []}, 'bottom_energies': {0: [], 1: [], 2: [], 3: [], 4: []}}
        for index in range(0, len(self.active_tiles)):
            for i in self.active_tiles[index].top:
                energies['top_energies'][index].append(i)
            for i in self.active_tiles[index].bottom:
                energies['bottom_energies'][index].append(i)
        return energies

    # finds the number of energies binded to the transmuter
    def get_total_energy_cells(self) -> int:
        sum = 0
        for tile in self.active_tiles:
            sum += tile.top.count(1)
            sum += tile.bottom.count(1)
        return sum

    # finds the number of total spaces empty (not binded any energy) on the transmuter
    def get_total_empty_cells(self) -> int:
        sum = 0
        for tile in self.active_tiles:
            sum += tile.top.count(0)
            sum += tile.bottom.count(0)
        return sum
