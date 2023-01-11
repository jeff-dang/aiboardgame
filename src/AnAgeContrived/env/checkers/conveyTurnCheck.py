from env.check import Check
from env.helpers.turn import Turn

class ConveyTurnCheck(Check):

    def __init__(self, player, engine) -> None:
        super().__init__(player, engine)

    def execute(self):
        return Turn.conveyTurnLegal