from env.command import Command
from env.helpers.fillMonument import FillMonument
from env.entities.energy import EnergyTile

class FillMonumentWithConstructiveEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(1, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)


    def check(self):
        #TODO: need to check whether the player has released energy on the board
        return True

class FillMonumentWithInvertibleEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(2, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return True

class FillMonumentWithGenerativeEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(3, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return True

class FillMonumentWithPrimalEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(4, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return True
