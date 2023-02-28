from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player

from enum import Enum

class Energy(Enum):
    CONSTRUCTIVE = 1
    INVERTIBLE = 2
    GENERATIVE = 3
    PRIMAL = 4

class EnergyTile():

    def __init__(self, energy_type: Energy, player: Player) -> None:
        # if energy_type not in Energy._value2member_map_ and energy_type not in Energy._member_names_ and energy_type not in Energy._member_map_:
        if energy_type not in Energy:
            print('Wrong energy_type. Please enter a correct energy type')
            self.energy_type: str = 'INVALID'
        else:
            self.energy_type: str = energy_type
        self.owner: Player = player #initiate the energy with the correct player

    def get_energy_type(self) -> str:
        return self.energy_type.name

    def set_energy_type(self, energy_type: Energy):
        if energy_type not in Energy:
            print('Wrong energy_type. Please enter a correct energy type')
        else:
            self.energy_type = energy_type

