from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    pass

from env.command import Command
from env.helpers.convey import Convey
from env.entities.energy import Energy

action_family_1 = "Convey 1"
action_family_2 = "Convey 2"


class ConveyOnceFirstCard(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - Fill None"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [None, None])

    def check(self) -> bool:
        return Convey.convey_1_legal(self.engine)

class ConveyOnceFirstCardFillTop(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - Fill Top"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.SINGLE, None])

    def check(self) -> bool:
        return Convey.convey_1_fill_1_legal(self.player, self.engine)

class ConveyOnceFirstCardFillBottom(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - Fill Bottom"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [None, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_1_fill_1_legal(self.player, self.engine)

class ConveyOnceFirstCardFillBoth(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card - Fill Both"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 0, [Energy.SINGLE, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_1_fill_2_legal(self.player, self.engine)


class ConveyOnceSecondCard(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - Fill None"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [None, None])

    def check(self) -> bool:
        return Convey.convey_1_legal(self.engine)

class ConveyOnceSecondCardFillTop(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - Fill Top"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.SINGLE, None])

    def check(self) -> bool:
        return Convey.convey_1_fill_1_legal(self.player, self.engine)

class ConveyOnceSecondCardFillBottom(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - Fill Bottom"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [None, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_1_fill_1_legal(self.player, self.engine)

class ConveyOnceSecondCardFillBoth(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card - Fill Both"

    def execute(self):
        Convey.convey(self.engine, self.player, 1, 1, [Energy.SINGLE, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_1_fill_2_legal(self.player, self.engine)

class ConveyTwiceFirstOrder(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "First Order - Fill None"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 0, [None, None])

    def check(self) -> bool:
        return Convey.convey_2_legal(self.engine)

class ConveyTwiceFirstOrderFillTop(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "First Order - Fill Top"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 0, [Energy.SINGLE, None])

    def check(self) -> bool:
        return Convey.convey_2_fill_1_legal(self.player, self.engine)

class ConveyTwiceFirstOrderFillBottom(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "First Order - Fill Bottom"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 0, [None, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_2_fill_1_legal(self.player, self.engine)

class ConveyTwiceFirstOrderFillBoth(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "First Order - Fill Both"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 0, [Energy.SINGLE, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_2_fill_2_legal(self.player, self.engine)


class ConveyTwiceSecondOrder(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "Second Order"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 1, [None, None])

    def check(self) -> bool:
        return Convey.convey_2_legal(self.engine)

class ConveyTwiceSecondOrderFillTop(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "Second Order - Fill Top"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 1, [Energy.SINGLE, None])

    def check(self) -> bool:
        return Convey.convey_2_fill_1_legal(self.player, self.engine)

class ConveyTwiceSecondOrderFillBottom(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "Second Order - Fill Bottom"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 1, [None, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_2_fill_1_legal(self.player, self.engine)

class ConveyTwiceSecondOrderFillBoth(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "Second Order - Fill Both"

    def execute(self):
        Convey.convey(self.engine, self.player, 2, 1, [Energy.SINGLE, Energy.SINGLE])

    def check(self) -> bool:
        return Convey.convey_2_fill_2_legal(self.player, self.engine)