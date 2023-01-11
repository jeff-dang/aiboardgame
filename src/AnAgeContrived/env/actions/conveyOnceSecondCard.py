from env.command import Command
from env.helpers.convey import Convey

class ConveyOnceSecondCard(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        Convey.convey(self.engine, self.player.transmuter, 1, 1)