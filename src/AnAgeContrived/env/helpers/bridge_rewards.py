# Author: Michael Ilao
# Date: March 13th, 2023
# Description: 
# Helpers to give rewards for building bridges

from env.entities.turn_state import TurnType
from env.entities.bridge import BridgeRewardType

# Defines the rewards given for building bridges
class BridgeRewards:
    # When the bridge is build calls the other function of the class to change turn type 
    def give_reward(engine, reward):
        BridgeRewards.build_bridge_reward(engine)

    # updates turn type to build bridge reward
    def build_bridge_reward(engine):
        engine.turn.update_turn_type(TurnType.BUILD_BRIDGE_TURN)
