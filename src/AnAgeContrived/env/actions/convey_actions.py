from env.command import Command
from env.helpers.convey import Convey

action_family_1 = "Convey 1"
action_family_2 = "Convey 2"


class ConveyOnceFirstCard(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "First Card"

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 1, 0)

    def check(self) -> bool:
        return Convey.convey1Legal(self.engine)


class ConveyOnceSecondCard(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family_1
        self.action_details = "Second Card"

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 1, 1)

    def check(self) -> bool:
        return Convey.convey1Legal(self.engine)


class ConveyTwiceFirstOrder(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "First Order"

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 2, 0)

    def check(self) -> bool:
        return Convey.convey2Legal(self.engine)


class ConveyTwiceSecondOrder(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family_2
        self.action_details = "Second Order"

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 2, 1)

    def check(self) -> bool:
        return Convey.convey2Legal(self.engine)
