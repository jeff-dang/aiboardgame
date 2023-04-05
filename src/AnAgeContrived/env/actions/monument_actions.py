# Author: Jonah Ada
# Date: January 13th, 2023
# Description: 
# Modules to convert entity & helper module funtions into a Command objects to utilize the Command design pattern
# the actions in this file are related to the monument filling (binding energy)
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

class FillMonumentWithSingleEnergy(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = action_family
        self.action_details = "Single Energy"

    def execute(self):
        energy = EnergyTile(Energy.SINGLE, self.player)
        FillMonument.fill_monument_tile(self.player, self.engine, energy)

    def check(self):
        return FillMonument.is_legal_single(self.engine, self.player)