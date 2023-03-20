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