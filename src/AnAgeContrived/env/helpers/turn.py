from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.engine import Engine
    # from env.entities.energy import EnergyTile
    pass

from env.entities.turn_state import TurnType
from env.helpers.logger import Logger
# Cant import from constatns.py since circular import
TOTAL_PLAYERS: int = 5


class Turn():

    @staticmethod
    def is_legal_action(agent) -> bool:
        # Can always end turn, except when monument building
        return True

    @staticmethod
    def end_turn(engine: Engine):
        Logger.log('End Turn', 'TURN_LOGS')
        engine.current_player = (engine.current_player+1) % TOTAL_PLAYERS
        engine.turn_counter += 1
        engine.turn.reset()
        # Check for queued players before progressing in case of monument building

    @staticmethod
    def end_turn_legal(engine: Engine) -> bool:
        if(engine.turn.turn_type == TurnType.CONVEY_TURN and engine.turn.can_convey == True):
            return False
        return engine.turn.turn_type != None

    @staticmethod
    def convey_turn(engine: Engine):
        Logger.log('Choose Convey Turn', 'TURN_LOGS')
        engine.turn.update_turn_type(TurnType.CONVEY_TURN)

    @staticmethod
    def convey_turn_legal(engine: Engine) -> bool:
        return engine.turn.turn_type == None

    @staticmethod
    def action_turn(engine: Engine):
        Logger.log('Choose Action Turn', 'TURN_LOGS')
        engine.turn.update_turn_type(TurnType.ACTION_TURN)

    @staticmethod
    def action_turn_legal(engine: Engine) -> bool:
        return engine.turn.turn_type == None
