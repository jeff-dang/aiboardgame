from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    pass

from env.command import Command
from env.helpers import take_action as TakeAction

class TakeAction1Move(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "First Transmuter's Action Token - Move"

    def execute(self):
        TakeAction.take_action(self.player, self.engine, 0)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 0)
    
# class TakeAction1Transformative(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = 'Action Tokens'
#         self.action_details = "First Transmuter's Action Token - Transformative"

#     def execute(self):
#         TakeAction.take_action(self.player, self.engine, 1)

#     def check(self):
#         return TakeAction.is_take_action_legal(self.player, self.engine, 0)
    
# class TakeAction1Sentient(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = 'Action Tokens'
#         self.action_details = "First Transmuter's Action Token - Sentient"

#     def execute(self):
#         TakeAction.take_action(self.player, self.engine, 2)

#     def check(self):
#         return TakeAction.is_take_action_legal(self.player, self.engine, 0)

class TakeAction2(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Second Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, self.engine, 3)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 3)

class TakeAction3(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Third Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, self.engine, 4)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 4)

class TakeAction4(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Forth Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, self.engine, 5)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 5)

class TakeAction5(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = 'Action Tokens'
        self.action_details = "Fifth Transmuter's Action Token"

    def execute(self):
        TakeAction.take_action(self.player, self.engine, 6)

    def check(self):
        return TakeAction.is_take_action_legal(self.player, self.engine, 6)
    