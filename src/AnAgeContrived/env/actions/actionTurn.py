from env.command import Command
from env.helpers.turn import Turn

class ActionTurn(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Turn.actionTurn(self.engine)

    def check(self) -> bool:
        return Turn.actionTurnLegal(self.engine)