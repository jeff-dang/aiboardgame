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

class PillarsOfCivilization():

    def __init__(self, name: str, map_area: MapAreas):
        self.name: str = name
        self.location = map_area
        self.binded_energies: list[EnergyTile] = [None, None]

    def get_binded_energies(self) -> list[EnergyTile]:
        return self.binded_energies
    
    def set_bind_energy(self, energy: EnergyTile):
        index = self.get_empty_space()
        if index != -1:
            self.binded_energies[index] = energy

    def get_empty_space(self) -> int:
        try:
            index = self.binded_energies.index(None)
            return index
        except:
            Logger.log("No empty space.", "PILLARS_OF_CIVILIZATION_LOGS")
            return -1
        
    def get_area(self) -> MapAreas:
        return self.location
    
    def is_player_present(self, player: Player) -> bool:
        for energy in self.binded_energies:
            if energy != None:
                if energy.owner == player:
                    return True
        return False
    
    def is_player_in_same_area(self, player: Player) -> bool:
        return player.location in areas[self.location]