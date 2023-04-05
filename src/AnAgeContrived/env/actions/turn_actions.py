# Author: Jonah Ada
# Date: January 13th, 2023
# Description: 
# Modules to convert entity & helper module funtions into a Command objects to utilize the Command design pattern
# the actions in this file are related to the selecting and modifying the turn state action

from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine

from env.command import Command
from env.helpers.turn import Turn

class ActionTurn(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = "Action Turn"
        self.action_details = "Action Turn"

    def execute(self):
        Turn.action_turn(self.engine)

    def check(self) -> bool:
        return Turn.action_turn_legal(self.player, self.engine)


class ConveyTurn(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = "Convey Turn"
        self.action_details = "Convey Turn"

    def execute(self):
        Turn.convey_turn(self.engine)

    def check(self) -> bool:
        return Turn.convey_turn_legal(self.player, self.engine)


class EndTurn(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = "End Turn"
        self.action_details = "End Turn"

    def execute(self):
        Turn.end_turn(self.engine)

    def check(self) -> bool:
        return Turn.end_turn_legal(self.player, self.engine)
