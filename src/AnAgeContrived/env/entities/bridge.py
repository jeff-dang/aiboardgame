from enum import Enum


class Bridge:
    def __init__(self, owner, reward, location, tier):
        self.owner = owner
        self.reward = reward
        self.location = location

        # If a reward requires an action add here
        self.action_required = False
        self.tier = tier

    def set_owner(self, player):
        self.owner = player

    def set_reward(self, reward):
        self.reward = reward

    def set_location(self, location):
        self.location = location


class BridgeRewardType(Enum):
    BUILD_BRIDGE = 1
    PLACE_HOLDER_2 = 2
    PLACE_HOLDER_3 = 3
    PLACE_HOLDER_4 = 4
    VP_SCORING_1 = 5
    VP_SCORING_2 = 6
