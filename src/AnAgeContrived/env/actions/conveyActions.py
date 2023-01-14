from env.command import Command
from env.helpers.convey import Convey

class ConveyOnceFirstCard(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 1, 0)

    def check(self) -> bool:
        return Convey.convey1Legal(self.engine)

class ConveyOnceSecondCard(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 1, 1)

    def check(self) -> bool:
        return Convey.convey1Legal(self.engine)

class ConveyTwiceFirstOrder(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 2, 0)

    def check(self) -> bool:
        return Convey.convey2Legal(self.engine)

class ConveyTwiceSecondOrder(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 2, 1)

    def check(self) -> bool:
        return Convey.convey2Legal(self.engine)