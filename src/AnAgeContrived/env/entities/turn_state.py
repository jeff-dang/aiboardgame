class TurnState():
    def __init__(self):
        # actionChoice can be convey or action
        self.turn_type = ""
        self.can_convey = False
        self.can_move = True

    def reset(self):
        self.turn_type = ""
        self.can_convey = False
        self.can_move = True

    def update_turn_type(self, turnType):
        self.turn_type = turnType
        if(turnType == "convey"):
            self.can_convey = True

    def conveyed(self):
        self.can_convey = False

    def get_turn_type(self):
        return self.turn_type

    def print_turn_state(self):
        print("Turn Type: ", self.turn_type)
        print("Can Convey: ", self.can_convey)
        print("Can Move:", self.can_move)
