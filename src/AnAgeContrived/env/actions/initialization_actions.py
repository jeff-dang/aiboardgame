from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine

from env.command import Command
import env.helpers.initialize as Initialize
from env.entities.energy import Energy

class InitializeWithSingle(Command):

    def __init__(self, player: Player, engine: Engine):
        super().__init__(player, engine)
        self.action = 'Initialization Actions'
        self.action_details = "Fill Transmuter With Single Energy"

    def execute(self):
        energy = self.player.exhausted_energies[Energy.SINGLE].pop()
        Initialize.initialize_transmuter(self.player, energy)

    def check(self):
        return Initialize.is_legal_fill_single(self.player)


# class InitializeWithConstructive(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = 'Initialization Actions'
#         self.action_details = "Fill Transmuter With Constructive Energy"

#     def execute(self):
#         energy = self.player.exhausted_energies[Energy.CONSTRUCTIVE].pop()
#         Initialize.initialize_transmuter(self.player, energy)

#     def check(self):
#         return Initialize.is_legal_fill_constructive(self.player)
    
# class InitializeWithInvertible(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = 'Initialization Actions'
#         self.action_details = "Fill Transmuter With Invertible Energy"

#     def execute(self):
#         energy = self.player.exhausted_energies[Energy.INVERTIBLE].pop()
#         Initialize.initialize_transmuter(self.player, energy)

#     def check(self):
#         return Initialize.is_legal_fill_invertible(self.player)
    
# class InitializeWithGenerative(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = 'Initialization Actions'
#         self.action_details = "Fill Transmuter With Generative Energy"

#     def execute(self):
#         energy = self.player.exhausted_energies[Energy.GENERATIVE].pop()
#         Initialize.initialize_transmuter(self.player, energy)

#     def check(self):
#         return Initialize.is_legal_fill_generative(self.player)
    
# class InitializeWithPrimal(Command):

#     def __init__(self, player: Player, engine: Engine):
#         super().__init__(player, engine)
#         self.action = 'Initialization Actions'
#         self.action_details = "Fill Transmuter With Primal Energy"

#     def execute(self):
#         energy = self.player.exhausted_energies[Energy.PRIMAL].pop()
#         Initialize.initialize_transmuter(self.player, energy)

#     def check(self):
#         return Initialize.is_legal_fill_primal(self.player)