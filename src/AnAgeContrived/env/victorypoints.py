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
        vp_allocation = {
            0: 0,
            1: 3,
            2: 6,
            3: 10,
            4: 15
        }
        if (len(gainableEnergyList[Energy.CONSTRUCTIVE]) == 0):
            fullyGainedEnergy += 1
        if (len(gainableEnergyList[Energy.INVERTIBLE]) == 0):
            fullyGainedEnergy += 1
        if (len(gainableEnergyList[Energy.GENERATIVE]) == 0):
            fullyGainedEnergy += 1
        if (len(gainableEnergyList[Energy.PRIMAL]) == 0):
            fullyGainedEnergy += 1
        vp_points = vp_allocation.get(fullyGainedEnergy)
        return vp_points

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
        return vp_points

    # Won't be used
    def calcPillars(engine, player):
        vp_allocation = {
            1: 3,
            2: 8,
            3: 14,
            4: 21,
            5: 29,
            6: 38
        }
        num_tiles = 0
        for pillar in pillarList:  # insert pillar engine command here
            for tile in pillar.tiles:
                if (tile.owner == player):
                    num_tiles += 1
        vp_points = vp_allocation.get(num_tiles)
        return vp_points

    # Wont be used
    def calcAchievements(engine, player):
        # award 2 transformative
        vp_points = 0
        # assuming transformative.timestwo is the tile
        if achievements.transformative.timestwo.owner == player:
            vp_points += 2
            # check if consider tiles on board
            for monument in monument.list:
                top_wall = monument.get_top_wall()
                for tile in top_wall.filled_sections:
                    if tile.owner == player and achievements.transformative.timestwo == tile:
                        vp_points += 2
        if achievements.transformative.plusfive.owner == player:
            vp_points += 5

        # achievements under sentient
        if achievements.sentient.timestwo.owner == player:
            vp_points += 2
            # check if consider tiles on board
            for monument in monument.list:
                top_wall = monument.get_top_wall()
                for tile in top_wall.filled_sections:
                    if tile.owner == player and achievements.sentient.timestwo == tile:
                        vp_points += 2
        if achievements.sentient.plusfive.owner == player:
            vp_points += 5

         # achievements under journey icons
        if achievements.journey.timestwo.owner == player:
            vp_points += 2
            # check if consider tiles on board
            for monument in monument.list:
                top_wall = monument.get_top_wall()
                for tile in top_wall.filled_sections:
                    if tile.owner == player and achievements.journey.timestwo == tile:
                        vp_points += 2
        if achievements.journey.plusfive.owner == player:
            vp_points += 5

        if achievements.random1.timestwo.owner == player:
            vp_points += 2
            # check if consider tiles on board
            for monument in monument.list:
                top_wall = monument.get_top_wall()
                for tile in top_wall.filled_sections:
                    if tile.owner == player and achievements.random1.timestwo == tile:
                        vp_points += 2
        if achievements.random1.plusfive.owner == player:
            vp_points += 5

        if achievements.random2.timestwo.owner == player:
            vp_points += 2
            # check if consider tiles on board
            for monument in monument.list:
                top_wall = monument.get_top_wall()
                for tile in top_wall.filled_sections:
                    if tile.owner == player and achievements.random2.timestwo == tile:
                        vp_points += 2
        if achievements.random2.plusfive.owner == player:
            vp_points += 5

        return vp_points
