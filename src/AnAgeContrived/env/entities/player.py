from .transmuter import Transmuter
from env.entities.energy import EnergyTile, Energy


class Player():

    def __init__(self, agent, character) -> None:
        self.agent = agent
        self.character = character
        self.transmuter = Transmuter() #TODO: let the player to fill the transmuter.
        self.energies = {
                            'CONSTRUCTIVE': [EnergyTile(Energy.CONSTRUCTIVE, self), EnergyTile(Energy.CONSTRUCTIVE, self)],
                            'INVERTIBLE': [EnergyTile(Energy.INVERTIBLE, self), EnergyTile(Energy.INVERTIBLE, self)],
                            'GENERATIVE': [EnergyTile(Energy.GENERATIVE, self), EnergyTile(Energy.GENERATIVE, self)],
                            'PRIMAL': [EnergyTile(Energy.PRIMAL, self), EnergyTile(Energy.PRIMAL, self)]
                        }
        #TODO: need to track the energies on the board, on his hand (done) and the remaining energies

    def set_transmuter(self, transmuter):
        self.transmuter = transmuter

    def get_transmuter(self):
        return self.transmuter

    def get_player_name(self):
        return self.agent