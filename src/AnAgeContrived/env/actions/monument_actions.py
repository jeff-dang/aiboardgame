from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    from env.entities.energy import EnergyTile
    pass

from env.command import Command
from env.helpers.fill_monument import FillMonument
from env.entities.energy import EnergyTile, Energy

action_family: str = "Fill Monument"


class FillMonumentWithConstructiveEnergy(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Constructive Energy"

    def execute(self):
        energy = EnergyTile(Energy.CONSTRUCTIVE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        # TODO: need to check whether the player has released energy on the board
        return FillMonument.is_legal_constructive(self.engine, self.player)


class FillMonumentWithInvertibleEnergy(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Invertible Energy"

    def execute(self):
        energy = EnergyTile(Energy.INVERTIBLE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_invertible(self.engine, self.player)


class FillMonumentWithGenerativeEnergy(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Generative Energy"

    def execute(self):
        energy = EnergyTile(Energy.GENERATIVE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_generative(self.engine, self.player)


class FillMonumentWithPrimalEnergy(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Primal Energy"

    def execute(self):
        energy = EnergyTile(Energy.PRIMAL, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_primal(self.engine)