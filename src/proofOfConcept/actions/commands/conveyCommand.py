from command import Command

class ConveyCommand(Command):

    def __init__(self, player ,board):
        super().__init__(player, board)

    def execute(self, step_size, order):
        if step_size == 1:
            self.player.transmuter.convey(order)
        elif step_size == 2:
            if order == 0:
                self.player.transmuter.convey(0)
                self.player.transmuter.convey(1)
            else:
                self.player.transmuter.convey(1)
                self.player.transmuter.convey(0)

print(Command.__subclasses__())                