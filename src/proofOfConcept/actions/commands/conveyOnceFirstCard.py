from .command import Command
from ..convey import Convey

class ConveyOnceFirstCard(Command):

    def __init__(self, player, board):
        super().__init__(player, board)

    def execute(self):
        Convey.convey(self.player.transmuter, 1, 0)