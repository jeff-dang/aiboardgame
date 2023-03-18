from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    from env.entities.energy import EnergyTile
    pass

from env.entities.turn_state import TurnType
from env.helpers.logger import Logger
from env.entities.energy import Energy

MAX_STEP_SIZE = 2


class Convey():

    @staticmethod
    def convey(engine: Engine, player: Player, stepSize: int, order: int, fill_energies: list[EnergyTile] = [None, None]):
        Logger.log('Convey ' + str(stepSize), 'ACTION_LOGS')
        if stepSize == 1:
            player.transmuter.convey(player, order, fill_energies)
        elif stepSize == 2:
            if order == 0:
                player.transmuter.convey(player, 0, fill_energies)
                player.transmuter.convey(player, 1, fill_energies)
            else:
                player.transmuter.convey(player, 1, fill_energies)
                player.transmuter.convey(player, 0, fill_energies)
        engine.turn.conveyed()

    @staticmethod
    def convey_1_legal(engine: Engine) -> bool:
        return engine.turn.can_convey and engine.turn.get_turn_type() == TurnType.CONVEY_TURN

    @staticmethod
    def convey_1_fill_1_legal(player: Player, engine: Engine) -> bool:
        return engine.turn.can_convey and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and len(player.exhausted_energies[Energy.SINGLE]) > 0

    @staticmethod
    def convey_1_fill_2_legal(player: Player, engine: Engine) -> bool:
        return engine.turn.can_convey and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and len(player.exhausted_energies[Energy.SINGLE]) > 1

    @staticmethod
    def convey_2_legal(engine: Engine) -> bool:
        return engine.turn.can_convey and False and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and engine.current_player.channel_marker

    @staticmethod
    def convey_2_fill_1_legal(player: Player, engine: Engine) -> bool:
        return engine.turn.can_convey and False and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and engine.current_player.channel_marker and len(player.exhausted_energies[Energy.SINGLE]) > 0

    @staticmethod
    def convey_2_fill_2_legal(player: Player, engine: Engine) -> bool:
        return engine.turn.can_convey and False and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and engine.current_player.channel_marker and len(player.exhausted_energies[Energy.SINGLE]) > 1