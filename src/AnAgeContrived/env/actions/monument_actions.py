from env.command import Command
from env.helpers.fill_monument import FillMonument
from env.entities.energy import EnergyTile, Energy

class FillMonumentWithConstructiveEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(Energy.CONSTRUCTIVE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)


    def check(self):
        #TODO: need to check whether the player has released energy on the board
        return FillMonument.is_legal_to_fill_monument_tile(self.engine)

class FillMonumentWithInvertibleEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(Energy.INVERTIBLE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_to_fill_monument_tile(self.engine)

class FillMonumentWithGenerativeEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(Energy.GENERATIVE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_to_fill_monument_tile(self.engine)

class FillMonumentWithPrimalEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)

    def execute(self):
        energy = EnergyTile(Energy.PRIMAL, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_to_fill_monument_tile(self.engine)
