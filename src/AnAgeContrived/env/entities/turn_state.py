# Author: Jonah Ada
# Date: January 10th, 2023
# Description: 
# Module to define the turn order and type related logic
from enum import Enum
from env.helpers.logger import Logger

# Enum for turn types
class TurnType(Enum):
    INITIALIZATION_TURN = 0
    CONVEY_TURN = 1
    ACTION_TURN = 2
    MOVE_TURN = 3
    END_TURN = 4
    BRIDGE_REWARD_TURN = 5
    BUILD_BRIDGE_TURN = 6

# defines the turn state as an object
class TurnState:
    def __init__(self):
        # actionChoice can be convey or action
        self.turn_type: TurnType = None
        self.can_convey: bool = False
        self.can_move: bool = True
        self.temp_rewards: int = 0
        self.can_build_bridge = True

    # resets the all turn state to start a new game
    def reset(self):
        self.turn_type = None
        self.can_convey = False
        self.can_move = True
        self.temp_rewards: int = 0
        self.can_build_bridge = True

    # updates the turn state given the turn type
    def update_turn_type(self, turnType: TurnType):
        self.turn_type = turnType
        if turnType == TurnType.CONVEY_TURN:
            self.can_convey = True

    # if conveyed, sets the flag to false to avoid changing the turn type to convey again
    def conveyed(self):
        self.can_convey = False

    # returns the current turn type
    def get_turn_type(self) -> TurnType:
        return self.turn_type

    # returns temperary rewards to punish AI for excessive number of turns: reward is set to 0 after the original game reward logic was
    # implemented, this function was used before
    def get_temp_reward(self):
        returned_rewards = self.temp_rewards
        self.temp_rewards = 0
        return returned_rewards

    # prints the turn state in human readable way to be used in the render function of the game engine
    def print_turn_state(self):
        Logger.log("Turn Type: " + str(self.turn_type), "TURN_LOGS")
        Logger.log("Can Convey: " + str(self.can_convey), "TURN_LOGS")
        Logger.log("Can Move: " + str(self.can_move), "TURN_LOGS")
