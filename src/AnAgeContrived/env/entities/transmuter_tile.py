# Author: Jonah Ada
# Date: December 12th, 2022
# Description: 
# Module to define the "transmuter tile" entity of the game
from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player

from env.entities.energy import EnergyTile
from env.helpers.logger import Logger

# defines transmuter tile as an object
class TransmuterTile:
    def __init__(self, top_size: int, bottom_size: int):
        self.top: list[EnergyTile] = [0] * top_size
        self.bottom: list[EnergyTile] = [0] * bottom_size
        self.top_size: int = top_size
        self.bottom_size: int = bottom_size
        self.available_top_positions: int = top_size
        self.available_bottom_positions: int = bottom_size

    # checks whether the top tiles are empty
    def is_top_empty(self) -> bool:
        return (not (self.top_size - self.top.count(0)) > 0)
    
    # checks whether the bottom tiles are empty
    def is_bottom_empty(self) -> bool:
        return (not (self.bottom_size - self.bottom.count(0)) > 0)

    # fill the energy at the given position: position: 1 == top, position: 2 == bottom
    def fill_tile(self, energy: EnergyTile, position):
        if position > 2 or position < 1:
            Logger.log('Position is wrong. Please enter a correct position between [1, 2]', 'TRANSMUTER_LOGS')
        elif position == 1:
            if self.top_size == 0:
                return Logger.log('No tile at the top', 'TRANSMUTER_LOGS')
            elif self.top_size == 1:
                if self.top[0] != 0:
                    return Logger.log('Tile already contains energy. Cannot fill this position', 'TRANSMUTER_LOGS')
                else:
                    self.top[0] = energy
            elif self.top_size == 2:
                if self.top[0] != 0:
                    if self.top[1] != 0:
                        return Logger.log('Tile already contains energy. Cannot fill this position', 'TRANSMUTER_LOGS')
                    else:
                        self.top[1] = energy
                else:
                    self.top[0] = energy
        elif position == 2:
            if self.bottom_size == 0:
                return Logger.log('No tile at the bottom', 'TRANSMUTER_LOGS')
            elif self.bottom_size == 1:
                if self.bottom[0] != 0:
                    return Logger.log('Tile already contains energy. Cannot fill this position', 'TRANSMUTER_LOGS')
                else:
                    self.bottom[0] = energy
            elif self.bottom_size == 2:
                if self.bottom[0] != 0:
                    if self.bottom[1] != 0:
                        return Logger.log('Tile already contains energy. Cannot fill this position', 'TRANSMUTER_LOGS')
                    else:
                        self.bottom[1] = energy
                else:
                    self.bottom[0] = energy

    # empties the tiles of the transmuter tile object
    def empty_tile(self, player: Player):
        for i in self.top:
            Logger.log('i is: ' + str(i) + ' and condition is: ' + str(i != 0), 'TRANSMUTER_LOGS')
            if i != 0:
                index = self.top.index(i)
                energy = self.top[index]
                self.top[index] = 0
                Logger.log('Energy at the top is: ' +  str(energy), 'TRANSMUTER_LOGS')
                player.exhausted_energies[energy.energy_type].append(energy)
        for i in self.bottom:
            if i != 0:
                index = self.bottom.index(i)
                energy = self.bottom[index]
                self.bottom[index] = 0
                Logger.log('Energy at the bottom is: ' +  str(energy), 'TRANSMUTER_LOGS')
                player.exhausted_energies[energy.energy_type].append(energy)
        self.top = [0, 0]
        self.bottom = [0, 0]

    # releases the energies binded in the bottom tile of the transmuter tile
    def release_bottom_energy(self) -> EnergyTile:
        num_zeros = self.bottom.count(0)
        if num_zeros > 0:
            index = self.bottom.index(0)
            if index == 0:
                index = 1
            elif index == 1:
                index = 0
            energy = self.bottom[index]
            self.bottom[index] = 0
        else:
            energy = self.bottom.pop()
            self.bottom.append(0)
        return energy

    # releases the energies binded in the top tile of the transmtuer tile
    def release_top_energy(self) -> EnergyTile:
        num_zeros = self.top.count(0)
        if num_zeros > 0:
            index = self.top.index(0)
            if index == 0:
                index = 1
            elif index == 1:
                index = 0
            energy = self.top[index]
            self.top[index] = 0
        else:
            energy = self.top.pop()
            self.top.append(0)
        return energy

    # prints the transmuter tile and the energies binded to it in a human readable way to be used in the game engine's render method
    def print_tile(self) -> str:
        tile_string = ''
        tile_string += '---------------\n'
        tile_string += '|             |\n'
        if self.top_size == 0:
            tile_string += '|             |\n'
            tile_string += '|             |\n'
            tile_string += '|             |\n'
        elif self.top_size == 1:
            tile_string += '|     ---     |\n'
            tile_string += '|    | {} |    |\n'.format(self.top[0].energy_type.name[0] if type(self.top[0]) == EnergyTile else self.top[0])
            tile_string += '|     ---     |\n'
        elif self.top_size == 2:
            tile_string += '|  ---   ---  |\n'
            tile_string += '| | {} | | {} | |\n'.format(
                self.top[0].energy_type.name[0] if type(self.top[0]) == EnergyTile else self.top[0], self.top[0].energy_type.name[0] if type(self.top[1]) == EnergyTile else self.top[0])
            tile_string += '|  ---   ---  |\n'
        tile_string += '|             |\n'
        tile_string += '|             |\n'
        if self.bottom_size == 0:
            tile_string += '|             |\n'
            tile_string += '|             |\n'
            tile_string += '|             |\n'
        elif self.bottom_size == 1:
            tile_string += '|     ---     |\n'
            tile_string += '|    | {} |    |\n'.format(self.bottom[0].energy_type.name[0] if type(self.bottom[0]) == EnergyTile else self.bottom[0])
            tile_string += '|     ---     |\n'
        elif self.bottom_size == 2:
            tile_string += '|  ---   ---  |'
            tile_string += '| | {} | | {} | |\n'.format(
                self.bottom[0].energy_type.name[0] if type(self.bottom[0]) == EnergyTile else self.bottom[0], self.bottom[0].energy_type.name[0] if type(self.bottom[0]) == EnergyTile else self.bottom[0])
            tile_string += '|  ---   ---  |\n'
        tile_string += '|             |\n'
        tile_string += '---------------\n'

        return (
            tile_string
        ).format().splitlines()