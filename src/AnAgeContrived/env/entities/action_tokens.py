# Author: Jonah Ada
# Date: February 4th, 2023
# Description: 
# Module to define fill action tokens of transmuter device

from enum import Enum

# defines the action token for energy releasing
class EnergyActionToken():

    def __init__(self, transmuter_tiles: list, times: int) -> None:
        self.type = ActionType.RELEASE_ENERGY
        self.transmuter_tiles = transmuter_tiles #for energy release action_token, which transmuter tiles can release energy?
        self.times = times #how many times can it be used, you can release two vs 1 energy, you can move 1 or 2 times on the board etc.

# defines the action token for player movement
class MoveActionToken():

    def __init__(self, times: int) -> None:
        self.type = ActionType.MOVE
        self.move_times = times

# defines the action token for transformative track
class FillTransformativeActionToken():
    def __init__(self) -> None:
        self.type = ActionType.FILL_TRANSFORMATIVE

# defines the action token for sentient track
class FillSentinentActionToken():
    
    def __init__(self) -> None:
        self.type = ActionType.FILL_SENTINENT

# defines the action token for recharging the player's channel marker 
# recharge let's you convey twice in the next turn
class RechargeActionToken():

    def __init__(self) -> None:
        self.type = ActionType.RECHARGE

    def take_action(self):
        # player.channel_marker = True
        pass

# defines the action token for repositioning an energy on the map
class RepositionActionToken():

    def __init__(self) -> None:
        self.type = ActionType.REPOSITION

# Enum for different action token types
class ActionType(Enum):
    RELEASE_ENERGY = 1
    MOVE = 2
    FILL_TRANSFORMATIVE = 3
    FILL_SENTINENT = 4
    RECHARGE = 5
    REPOSITION = 6