from enum import Enum


class Bridge:

    def __init__(self, owner, reward, location):
        self.owner = owner
        self.reward = reward
        self.location = location
        self.action_required = False

    def set_owner(self, player):
        self.owner = player

    def set_reward(self, reward):
        self.reward = reward

    def set_location(self, location):
        self.location = location


class BridgeRewardType(Enum):
    PLACE_HOLDER = 1
