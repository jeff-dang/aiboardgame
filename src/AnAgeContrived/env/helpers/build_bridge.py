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
        engine.turn.update_turn_type(TurnType.ACTION_TURN)


    @staticmethod
    def is_legal_move(engine, bridge_location):
        # Check if turn type is building a bridge
        if(engine.turn.get_turn_type() is None):
            return False

        if(not engine.turn.get_turn_type().value == TurnType.BUILD_BRIDGE_TURN.value):
            return False

        # Check if bridge is built already in this location
        if(engine.map.check_bridge_exists(bridge_location)):
            return False

        return True
