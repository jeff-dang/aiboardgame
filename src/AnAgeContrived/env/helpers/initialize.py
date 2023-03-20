from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    # from env.engine import Engine
    from env.entities.energy import EnergyTile
    pass

from env.entities.action_tokens import ActionType
from env.entities.turn_state import TurnType
from random import randint
from env.helpers.logger import Logger
from env.entities.energy import Energy

def initialize_transmuter(player: Player, energy: EnergyTile):
    tile = ''
    for i in range(0, 3):
        tile = player.transmuter.active_tiles[i]
        if tile.is_top_empty():
            tile.fill_tile(energy, 1)
            break
        elif tile.is_bottom_empty():
            tile.fill_tile(energy, 2)
            break

def is_legal_fill_single(player: Player):
    return not player.get_is_initialized() and TurnType.INITIALIZATION_TURN and len(player.exhausted_energies[Energy.SINGLE]) > 0 

# def is_legal_fill_constructive(player: Player):
#     return not player.get_is_initialized() and TurnType.INITIALIZATION_TURN and len(player.exhausted_energies[Energy.CONSTRUCTIVE]) > 0

# def is_legal_fill_invertible(player: Player):
#     return not player.get_is_initialized() and TurnType.INITIALIZATION_TURN and len(player.exhausted_energies[Energy.INVERTIBLE]) > 0

# def is_legal_fill_generative(player: Player):
#     return not player.get_is_initialized() and TurnType.INITIALIZATION_TURN and len(player.exhausted_energies[Energy.GENERATIVE]) > 0

# def is_legal_fill_primal(player: Player):
#     return not player.get_is_initialized() and TurnType.INITIALIZATION_TURN and len(player.exhausted_energies[Energy.PRIMAL]) > 0