from env.command import Command
from env.helpers.turn import Turn

class EndTurn(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Turn.endTurn(self.engine)

    def check(self) -> bool:
        return Turn.endTurnLegal(self.engine)