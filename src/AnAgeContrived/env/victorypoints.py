from __future__ import annotations

# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player

    # from env.entities.energy import EnergyTile
    pass

from env.entities.energy import Energy


class VictoryPoints:
    def calcFullyGainedEnergy(engine, player: Player):
        gainableEnergyList = player.remaining_energies
        fullyGainedEnergy = 0
        vp_allocation = {0: 0, 1: 3, 2: 6, 3: 10, 4: 15}
        if len(gainableEnergyList[Energy.CONSTRUCTIVE]) == 0:
            fullyGainedEnergy += 1
        if len(gainableEnergyList[Energy.INVERTIBLE]) == 0:
            fullyGainedEnergy += 1
        if len(gainableEnergyList[Energy.GENERATIVE]) == 0:
            fullyGainedEnergy += 1
        if len(gainableEnergyList[Energy.PRIMAL]) == 0:
            fullyGainedEnergy += 1
        vp_points = vp_allocation.get(fullyGainedEnergy)
        return vp_points * 1000

    def calcBridgesBuilt(engine: Engine, player: Player):
        if player.num_bridges_left == 0:
            return 500
        if player.num_bridges_left == 1:
            return 250
        if player.num_bridges_left == 2:
            return 100
        return 0

    # Jeffrey working on this
    def calcMonumentEnergy(engine: Engine, player: Player):
        monumentList = engine.monuments
        vp_points = 0
        vp_allocation = {
            0: 0,
            1: 3,
            2: 7,
            3: 12,
            4: 12
        }
        for monument in monumentList:
            num_energy = 0
            for tile in monument.get_top_wall().filled_sections:
                if (tile.owner == player):
                    num_energy += 1
            vp_points += vp_allocation.get(num_energy)
        return vp_points * 1000