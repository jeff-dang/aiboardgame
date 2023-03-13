from env.entities.turn_state import TurnType
from env.entities.bridge import BridgeRewardType


class BridgeRewards:

    def give_reward(engine, reward):
        if(reward.value == BridgeRewardType.BUILD_BRIDGE.value):
            BridgeRewards.build_bridge_reward(engine)

    def build_bridge_reward(engine):
        engine.turn.update_turn_type(TurnType.BUILD_BRIDGE_TURN)
