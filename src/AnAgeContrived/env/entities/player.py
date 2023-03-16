from env.entities.transmuter import Transmuter
from env.entities.energy import EnergyTile, Energy
from env.helpers.constants import STARTING_PLAYER_BRIDGES


class Player:
    def __init__(self, agent, character, starting_location):
        self.agent = agent
        self.character = character
        self.num_bridges_left = STARTING_PLAYER_BRIDGES
        # TODO: let the player to fill the transmuter.
        self.transmuter: Transmuter = Transmuter()
        self.is_initialized: bool = False
        self.exhausted_energies: dict[Energy, list[EnergyTile]] = {
            Energy.CONSTRUCTIVE: [
                EnergyTile(Energy.CONSTRUCTIVE, self),
                EnergyTile(Energy.CONSTRUCTIVE, self),
                EnergyTile(Energy.CONSTRUCTIVE, self),
                EnergyTile(Energy.CONSTRUCTIVE, self),
            ],
            Energy.INVERTIBLE: [
                EnergyTile(Energy.INVERTIBLE, self),
                EnergyTile(Energy.INVERTIBLE, self),
                EnergyTile(Energy.INVERTIBLE, self),
                EnergyTile(Energy.INVERTIBLE, self),
            ],
            Energy.GENERATIVE: [
                EnergyTile(Energy.GENERATIVE, self),
                EnergyTile(Energy.GENERATIVE, self),
                EnergyTile(Energy.GENERATIVE, self),
                EnergyTile(Energy.GENERATIVE, self),
            ],
            Energy.PRIMAL: [EnergyTile(Energy.PRIMAL, self)],
        }
        self.energies_released: dict[
            Energy, list[EnergyTile]
        ] = {  # rn, it is being used as anything, might have to separate it to monument vs. other things
            Energy.CONSTRUCTIVE: [],
            Energy.INVERTIBLE: [],
            Energy.GENERATIVE: [],
            Energy.PRIMAL: [],
        }
        self.remaining_energies: dict[Energy, list[EnergyTile]] = {
            Energy.CONSTRUCTIVE: [
                EnergyTile(Energy.CONSTRUCTIVE, self),
                EnergyTile(Energy.CONSTRUCTIVE, self),
            ],
            Energy.INVERTIBLE: [
                EnergyTile(Energy.INVERTIBLE, self),
                EnergyTile(Energy.INVERTIBLE, self),
            ],
            Energy.GENERATIVE: [
                EnergyTile(Energy.GENERATIVE, self),
                EnergyTile(Energy.GENERATIVE, self),
            ],
            Energy.PRIMAL: [
                EnergyTile(Energy.PRIMAL, self),
                EnergyTile(Energy.PRIMAL, self),
            ],
        }
        # keep tracks of the player's location on the board
        self.location = starting_location
        self.initial_location = starting_location
        self.previous_location = 0
        # TODO: need to track the energies on the board, on his hand (done) and the remaining energies
        # self._initiate_fill_tranmuster_files()
        self.channel_marker: bool = False  # if it is true, player can convey twice
        # self._initiate_fill_tranmuster_tiles()

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

    # def _initiate_fill_tranmuster_files(self):
    #     tile1 = self.transmuter.active_tiles[0]
    #     tile2 = self.transmuter.active_tiles[1]
    #     tile3 = self.transmuter.active_tiles[2]
    #     tile1.fill_tile(self.exhausted_energies[Energy.GENERATIVE].pop(), 1)
    #     tile1.fill_tile(self.exhausted_energies[Energy.INVERTIBLE].pop(), 2)
    #     tile2.fill_tile(self.exhausted_energies[Energy.PRIMAL].pop(), 1)
    #     tile2.fill_tile(self.exhausted_energies[Energy.CONSTRUCTIVE].pop(), 2)
    #     tile3.fill_tile(self.exhausted_energies[Energy.GENERATIVE].pop(), 1)
    #     tile3.fill_tile(self.exhausted_energies[Energy.INVERTIBLE].pop(), 2)
