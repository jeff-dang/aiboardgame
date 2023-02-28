from enum import Enum
from env.helpers.logger import Logger

class TurnType(Enum):
    CONVEY_TURN = 1
    ACTION_TURN = 2
    MOVE_TURN = 3
    END_TURN = 4

class TurnState():
    def __init__(self):
        # actionChoice can be convey or action
        self.turn_type: TurnType = None
        self.can_convey: bool = False
        self.can_move: bool = True

    def reset(self):
        self.turn_type = None
        self.can_convey = False
        self.can_move = True

    def update_turn_type(self, turnType: TurnType):
        self.turn_type = turnType
        if(turnType == TurnType.CONVEY_TURN):
            self.can_convey = True

    def conveyed(self):
        self.can_convey = False

    def get_turn_type(self) -> TurnType:
        return self.turn_type

    def print_turn_state(self):
        Logger.log("Turn Type: " + str(self.turn_type), 'TURN_LOGS')
        Logger.log("Can Convey: " + str(self.can_convey), 'TURN_LOGS')
        Logger.log("Can Move: " + str(self.can_move), 'TURN_LOGS')