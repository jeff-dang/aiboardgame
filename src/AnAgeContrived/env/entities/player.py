from .transmuter import Transmuter
from env.entities.energy import EnergyTile, Energy


class Player():

    def __init__(self, agent, character, starting_location):
        self.agent = agent
        self.character = character
        # TODO: let the player to fill the transmuter.
        self.transmuter: Transmuter = Transmuter()
        self.exhausted_energies: dict[Energy, list[EnergyTile]] = {
            Energy.CONSTRUCTIVE: [EnergyTile(Energy.CONSTRUCTIVE, self), EnergyTile(Energy.CONSTRUCTIVE, self)],
            Energy.INVERTIBLE: [EnergyTile(Energy.INVERTIBLE, self), EnergyTile(Energy.INVERTIBLE, self)],
            Energy.GENERATIVE: [EnergyTile(Energy.GENERATIVE, self), EnergyTile(Energy.GENERATIVE, self)],
            Energy.PRIMAL: [EnergyTile(Energy.PRIMAL, self), EnergyTile(Energy.PRIMAL, self)]
        }
        self.energies_released: dict[Energy, list[EnergyTile]] = {
            Energy.CONSTRUCTIVE: [],
            Energy.INVERTIBLE: [],
            Energy.GENERATIVE: [],
            Energy.PRIMAL: []
        }
        # keep tracks of the player's location on the board
        self.location = starting_location
        self.initial_location = starting_location
        self.previous_location = 0
        self.channel_marker: bool = False #if it is true, player can convey twice #TODO: use this to adjust the action mask
        # TODO: need to track the energies on the board, on his hand (done) and the remaining energies
        self._initiate_fill_tranmuster_files()

    def set_transmuter(self, transmuter: Transmuter):
        self.transmuter = transmuter

    def get_transmuter(self) -> Transmuter:
        return self.transmuter

    def get_player_name(self) -> str:
        return self.agent

    def _initiate_fill_tranmuster_files(self):
        tile1 = self.transmuter.active_tiles[0]
        tile2 = self.transmuter.active_tiles[1]
        tile3 = self.transmuter.active_tiles[2]
        tile1.fill_tile(
            self.exhausted_energies[Energy.CONSTRUCTIVE].pop(), 1)
        tile1.fill_tile(
            self.exhausted_energies[Energy.INVERTIBLE].pop(), 2)
        tile2.fill_tile(
            self.exhausted_energies[Energy.PRIMAL].pop(), 1)
        tile2.fill_tile(self.exhausted_energies[Energy.GENERATIVE].pop(), 2)
        tile3.fill_tile(
            self.exhausted_energies[Energy.CONSTRUCTIVE].pop(), 1)
        tile3.fill_tile(
            self.exhausted_energies[Energy.INVERTIBLE].pop(), 2)
