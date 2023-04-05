# Author: Michael Ilao
# Date: February 27th, 2023
# Description: 
# Module to define bridges in the game

from enum import Enum

# defines player bridges also known as link tokens in the game rule book
class Bridge:
    def __init__(self, owner, reward, location, tier):
        self.owner = owner
        self.reward = reward
        self.location = location
        # If a reward requires an action add here
        self.action_required = False
        self.tier = tier

    # setter to assign the player who owns the bridge
    def set_owner(self, player):
        self.owner = player

    # setter for rewards when building a bridge
    def set_reward(self, reward):
        self.reward = reward

    # setter for building location when player places it on the map
    def set_location(self, location):
        self.location = location

# Enum for different bridge reward types
class BridgeRewardType(Enum):
    BUILD_BRIDGE = 1
    PLACE_HOLDER_2 = 2
    PLACE_HOLDER_3 = 3
    PLACE_HOLDER_4 = 4
    VP_SCORING_1 = 5
    VP_SCORING_2 = 6
