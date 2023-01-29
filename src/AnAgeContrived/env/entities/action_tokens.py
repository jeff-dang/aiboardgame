
class ActionToken():

    def __init__(self) -> None:
        self.action_token_type = None
        self.transmuter_tiles = [0, 0, 0, 1, 1] #for energy release action_token, which transmuter tiles can release energy?
        self.times = 1 #how many times can it be used, you can release two vs 1 energy, you can move 1 or 2 times on the board etc.