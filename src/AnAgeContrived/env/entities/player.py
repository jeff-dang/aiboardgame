from env.entities.transmuter import Transmuter
from env.entities.energy import EnergyTile, Energy
from env.helpers.constants import STARTING_PLAYER_BRIDGES


class Player:
    def __init__(self, agent, character, starting_location):
        self.agent = agent
        self.character = character
        self.num_bridges_left = STARTING_PLAYER_BRIDGES
        self.transmuter: Transmuter = Transmuter()
        self.is_initialized: bool = False
        self.exhausted_energies: dict[Energy, list[EnergyTile]] = {
            Energy.SINGLE: [
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
            ]
        }
        self.energies_released: dict[Energy, list[EnergyTile]] = {  # rn, it is being used as anything, might have to separate it to monument vs. other things
            Energy.SINGLE: []
        }
        self.remaining_energies: dict[Energy, list[EnergyTile]] = {
            Energy.SINGLE: [
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
                EnergyTile(Energy.SINGLE, self),
            ]
        }
        self.location = starting_location # keep tracks of the player's location on the board
        self.initial_location = starting_location
        self.previous_location = 0
        self.channel_marker: bool = False  # if it is true, player can convey twice

    def set_transmuter(self, transmuter: Transmuter):
        self.transmuter = transmuter

    def get_transmuter(self) -> Transmuter:
        return self.transmuter

    def get_player_name(self) -> str:
        return self.agent

    def get_is_initialized(self) -> bool:
        return self.is_initialized

    def set_is_initialized(self):
        self.is_initialized = True

    def check_is_initialized(self) -> bool:
        tile1 = self.transmuter.active_tiles[0]
        tile2 = self.transmuter.active_tiles[1]
        tile3 = self.transmuter.active_tiles[2]
        total_filled_size = 0
        for i in range(0, 3):
            tile = self.transmuter.active_tiles[i]
            total_filled_size += tile.top_size - tile.top.count(0)
            total_filled_size += tile.bottom_size - tile.bottom.count(0)
        if total_filled_size == 6:
            self.set_is_initialized()
            return True
        return False
