from env.command import Command
from env.helpers.turn import Turn

class ConveyTurn(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Turn.conveyTurn(self.engine)