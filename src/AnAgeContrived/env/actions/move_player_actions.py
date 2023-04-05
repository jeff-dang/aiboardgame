# Author: Michael Ilao
# Date: January 30th, 2023
# Description: 
# Modules to convert entity & helper module funtions into a Command objects to utilize the Command design pattern
# the actions in this file are related to the player movement actions
from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    pass

from env.command import Command
from env.helpers.move_player import MovePlayer

action_family = "Move Player"


class MovePosition1(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 1
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition2(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 2
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition3(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 3
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition4(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 4
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition5(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 5
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition6(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 6
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition7(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 7
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition8(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 8
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition9(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 9
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition10(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 10
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition11(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 11
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition12(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 12
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition13(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 13
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition14(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 14
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition15(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 15
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition16(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 16
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition17(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 17
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition18(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 18
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition19(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 19
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition20(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 20
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition21(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 21
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition22(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 22
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition23(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 23
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition24(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 24
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition25(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 25
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition26(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 26
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition27(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 27
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition28(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 28
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition29(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 29
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition30(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 30
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition31(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 31
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition32(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 32
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition33(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 33
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition34(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 34
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition35(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 35
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition36(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 36
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition37(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 37
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition38(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 38
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition39(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 39
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)


class MovePosition40(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.position = 40
        self.action = action_family
        self.action_details = "Position " + str(self.position)

    def execute(self):
        MovePlayer.move_player(self.engine, self.player, self.position)

    def check(self):
        return MovePlayer.is_legal_move(self.player, self.engine, self.position)
