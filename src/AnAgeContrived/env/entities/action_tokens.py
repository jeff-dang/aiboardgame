
class EnergyActionToken():

    def __init__(self, transmuter_tiles: list, times: int) -> None:
        self.transmuter_tiles = transmuter_tiles #for energy release action_token, which transmuter tiles can release energy?
        self.times = times #how many times can it be used, you can release two vs 1 energy, you can move 1 or 2 times on the board etc.

class MoveActionToken():

    def __init__(self, move_times: int, transformative_times: int, sentinent_times: int) -> None:
        self.move_time = move_times
        self.transformative_times = transformative_times
        self.sentinent_times = sentinent_times

#TODO: just pass this for now and implement if time left
class RechargeActionToken():

    def __init__(self) -> None:
        pass

#TODO: just pass this for now and implement if time left
class RepositionActionToken():

    def __init__(self) -> None:
        pass