from enum import Enum

class EnergyTile():

    def __init__(self, energy_type, player) -> None:
        # if energy_type not in Energy._value2member_map_ and energy_type not in Energy._member_names_ and energy_type not in Energy._member_map_:
        if energy_type not in Energy:
            print('Wrong energy_type. Please enter a correct energy type')
            self.energy_type = 'INVALID'
        else:
            self.energy_type = energy_type
        self.owner = player #initiate the energy with the correct player

    def get_energy_type(self):
        return self.energy_type.name

    def set_energy_type(self, energy_type):
        if energy_type not in Energy:
            print('Wrong energy_type. Please enter a correct energy type')
        else:
            self.energy_type = energy_type

class Energy(Enum):
    CONSTRUCTIVE = 1
    INVERTIBLE = 2
    GENERATIVE = 3
    PRIMAL = 4