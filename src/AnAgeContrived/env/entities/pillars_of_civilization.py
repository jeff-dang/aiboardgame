# Author: Jonah Ada
# Date: January 10th, 2023
# Description: 
# Module to define the "pillars of civilizations" entity of the game

from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # from env.engine import Engine
    from env.entities.energy import EnergyTile
    from env.entities.map_data import MapAreas
    from env.entities.player import Player

from env.helpers.logger import Logger
from env.entities.map_data import areas

# defines the pillars of civilization as an object
class PillarsOfCivilization():

    def __init__(self, name: str, map_area: MapAreas):
        self.name: str = name
        self.location = map_area
        self.binded_energies: list[EnergyTile] = [None, None]

    # returns the energies binded to the instance of the pillar of civilization
    def get_binded_energies(self) -> list[EnergyTile]:
        return self.binded_energies
    
    # binds an energy to the pillars of civilization
    def set_bind_energy(self, energy: EnergyTile):
        index = self.get_empty_space()
        if index != -1:
            self.binded_energies[index] = energy

    # finds the empty space on the pillars of civilization that not yet has anergy binded to it
    def get_empty_space(self) -> int:
        try:
            index = self.binded_energies.index(None)
            return index
        except:
            Logger.log("No empty space.", "PILLARS_OF_CIVILIZATION_LOGS")
            return -1
        
    # returns the map area the pillar is placed on the map
    def get_area(self) -> MapAreas:
        return self.location
    
    # checks whether the player has already binded an energy to the pillar, if yes, player cannot bind another energy to the same pillar
    def is_player_present(self, player: Player) -> bool:
        for energy in self.binded_energies:
            if energy != None:
                if energy.owner == player:
                    return True
        return False
    
    # checks whether the player is in the same area as the pillar, if not player cannot bind an energy
    def is_player_in_same_area(self, player: Player) -> bool:
        return player.location in areas[self.location]