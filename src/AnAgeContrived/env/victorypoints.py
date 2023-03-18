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
        gainableEnergyList = player.remaining_energies[Energy.SINGLE]
        fullyGainedEnergy = 0
        vp_allocation = {0: 0, 1: 3, 2: 6, 3: 10, 4: 15}
        #single energy type checks
        if len(gainableEnergyList) > 5 and len(gainableEnergyList) < 8:
            fullyGainedEnergy += 1
        elif len(gainableEnergyList) > 3 and len(gainableEnergyList) < 6:
            fullyGainedEnergy += 1
        elif len(gainableEnergyList) > 1 and len(gainableEnergyList) < 4:
            fullyGainedEnergy += 1
        elif len(gainableEnergyList) >= 0 and len(gainableEnergyList) < 2:
            fullyGainedEnergy += 1

        vp_points = vp_allocation.get(fullyGainedEnergy)
        return vp_points

    def calcBridgesBuilt(engine: Engine, player: Player):
        if player.num_bridges_left == 0:
            return 30
        if player.num_bridges_left == 1:
            return 15
        if player.num_bridges_left == 2:
            return 10
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
            # num_energy = 0
            # for tile in monument.get_top_wall().filled_sections:
            #     if (tile.owner == player):
            #         num_energy += 1
            # vp_points += vp_allocation.get(num_energy)
            for wall in monument.walls:
                if (wall.owner == player):
                    vp_points += 20
        return vp_points
