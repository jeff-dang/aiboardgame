from enum import Enum

class EnergyActionToken():

    def __init__(self, transmuter_tiles: list, times: int) -> None:
        self.type = ActionType.RELEASE_ENERGY
        self.transmuter_tiles = transmuter_tiles #for energy release action_token, which transmuter tiles can release energy?
        self.times = times #how many times can it be used, you can release two vs 1 energy, you can move 1 or 2 times on the board etc.

class MoveActionToken():

    def __init__(self, times: int) -> None:
        self.type = ActionType.MOVE
        self.move_times = times

class FillTransformativeActionToken():
    def __init__(self, times: int) -> None:
        self.type = ActionType.FILL_TRANSFORMATIVE
        self.transformative_times = times

class FillSentinentActionToken():
    
    def __init__(self, times: int) -> None:
        self.type = ActionType.FILL_SENTINENT
        self.sentinent_times = times

#recharge let's you convey twice in the next turn
class RechargeActionToken():

    def __init__(self) -> None:
        self.type = ActionType.RECHARGE
        pass

    def take_action(self):
        # player.channel_marker = True #TODO: figure it out a way to pass the player here
        pass

#TODO: just pass this for now and implement if time left
class RepositionActionToken():

    def __init__(self) -> None:
        self.type = ActionType.REPOSITION
        pass

class ActionType(Enum):
    RELEASE_ENERGY = 1
    MOVE = 2
    FILL_TRANSFORMATIVE = 3
    FILL_SENTINENT = 4
    RECHARGE = 5
    REPOSITION = 6