from env.command import Command
from env.helpers.turn import Turn

class ActionTurn(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Turn.action_turn(self.engine)

    def check(self) -> bool:
        return Turn.action_turn_legal(self.engine)

class ConveyTurn(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Turn.convey_turn(self.engine)

    def check(self) -> bool:
        return Turn.convey_turn_legal(self.engine)

class EndTurn(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Turn.end_turn(self.engine)

    def check(self) -> bool:
        return Turn.end_turn_legal(self.engine)