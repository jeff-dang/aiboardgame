class TurnState():
    def __init__(self):
        # actionChoice can be convey or action
        self.turnType = ""
        self.canConvey = False

    def reset(self):
        self.turnType = ""
        self.canConvey = False

    def update_turn_type(self, turnType):
        self.turnType = turnType
        if(turnType == "convey"):
            self.canConvey = True

    def conveyed(self):
        self.canConvey = False

    def print_turn_state(self):
        print("Turn Type: ", self.turnType)
        print("Can Convey: ", self.canConvey)
