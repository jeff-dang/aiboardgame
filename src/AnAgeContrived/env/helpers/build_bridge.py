from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player
    from env.entities.energy import EnergyTile

import copy
from env.entities.turn_state import TurnType
from env.entities.bridge import BridgeRewardType


class BuildBridge():

    # 2 types per tier of bridges and 10 spots
    @staticmethod
    def build_bridge(engine, bridge_location, player, reward):
        bridge_reward = (player.num_bridges_left % 3) + reward

        engine.map.build_bridge(player, BridgeRewardType(bridge_reward), bridge_location)
        engine.turn.update_turn_type(TurnType.ACTION_TURN)

        engine.turn.turn_type = TurnType.ACTION_TURN
        engine.turn.can_build_bridge = False

    @staticmethod
    def is_legal_move(player: Player, engine: Engine, bridge_location):
        # Check if turn type is building a bridge
        if(not engine.turn.can_build_bridge):
            return False
        
        if(engine.turn.get_turn_type() is None):
            return False

        if(not engine.turn.get_turn_type().value == TurnType.BUILD_BRIDGE_TURN.value):
            return False

        # Check if bridge is built already in this location
        if(engine.map.check_bridge_exists(bridge_location)):
            return False
        
        if player.num_bridges_left == 0:
            return False

        return True
