from env.command import Command
from env.helpers.fill_monument import FillMonument
from env.entities.energy import EnergyTile, Energy

action_family = "Fill Monument"


class FillMonumentWithConstructiveEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Constructive Energy"

    def execute(self):
        energy = EnergyTile(Energy.CONSTRUCTIVE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        # TODO: need to check whether the player has released energy on the board
        return FillMonument.is_legal_to_fill_monument_tile(self.engine, Energy.CONSTRUCTIVE)


class FillMonumentWithInvertibleEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Invertible Energy"

    def execute(self):
        energy = EnergyTile(Energy.INVERTIBLE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_to_fill_monument_tile(self.engine, Energy.INVERTIBLE)


class FillMonumentWithGenerativeEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Generative Energy"

    def execute(self):
        energy = EnergyTile(Energy.GENERATIVE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_to_fill_monument_tile(self.engine, Energy.GENERATIVE)


class FillMonumentWithPrimalEnergy(Command):

    def __init__(self, player, engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Primal Energy"

    def execute(self):
        energy = EnergyTile(Energy.PRIMAL, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_to_fill_monument_tile(self.engine, Energy.PRIMAL)
