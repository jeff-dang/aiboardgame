from env.command import Command
from env.helpers import take_action as TakeAction

class TakeAction1(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "First Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, 0)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 0)

class TakeAction2(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Second Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, 1)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 1)

class TakeAction3(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Third Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, 2)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 2)

class TakeAction4(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Forth Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, 3)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 3)

class TakeAction5(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Fifth Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, 4)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 4)
    