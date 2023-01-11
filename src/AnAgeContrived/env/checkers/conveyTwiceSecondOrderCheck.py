from env.check import Check
from env.helpers.convey import Convey

class ConveyTwicesecondOrderCheck(Check):

    def __init__(self, player, engine) -> None:
        super().__init__(player, engine)

    def execute(self):
        return Convey.convey2Legal(self.engine)