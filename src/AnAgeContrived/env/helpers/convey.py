from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    # from env.entities.energy import EnergyTile
    pass

from env.entities.turn_state import TurnType
from env.helpers.logger import Logger

MAX_STEP_SIZE = 2


class Convey():

    @staticmethod
    def convey(engine: Engine, player: Player, stepSize: int, order: int):
        Logger.log('Convey ' + str(stepSize), 'ACTION_LOGS')
        if stepSize == 1:
            player.transmuter.convey(player, order)
        elif stepSize == 2:
            if order == 0:
                player.transmuter.convey(player, 0)
                player.transmuter.convey(player, 1)
            else:
                player.transmuter.convey(player, 1)
                player.transmuter.convey(player, 0)
        engine.turn.conveyed()

    @staticmethod
    def convey1Legal(engine: Engine) -> bool:
        return engine.turn.can_convey and engine.turn.get_turn_type() == TurnType.CONVEY_TURN

    @staticmethod
    def convey2Legal(engine: Engine) -> bool:
        return engine.turn.can_convey and False and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and engine.current_player.channel_marker
