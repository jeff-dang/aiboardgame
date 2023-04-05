# Author: Jonah Ada
# Date: February 6th, 2023
# Description: 
# Helper module to define fill monument actions

from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player
    from env.entities.energy import EnergyTile

#real imports start here
from env.entities.energy import Energy
from env.entities.turn_state import TurnType
from env.helpers.logger import Logger

# Defines functions for fill monument actions
class FillMonument():

    # given the energy and the player, it will fill monument and update the state in the game engine
    @staticmethod
    def fill_monument_tile(player: Player, engine: Engine, energy: EnergyTile):
        if len(player.energies_released[energy.energy_type]) > 0:
            Logger.log('player:' + player.get_player_name() +
                  'Trying to fill section with energy:' + str(energy.energy_type), 'ACTION_LOGS')
            monument_wall = engine.monuments[engine.monument_index].get_top_wall()
            Logger.log('Monument supports energy types:' + str(monument_wall.sections), 'ACTION_LOGS')
            result = monument_wall.fill_section(energy)
            if result == True:
                Logger.log(str(len(player.energies_released[energy.energy_type])), 'ACTION_LOGS')
                player.energies_released[energy.energy_type].pop()
                Logger.log(str(len(player.energies_released[energy.energy_type])), 'ACTION_LOGS')
                Logger.log('Remaining sections:' + str(monument_wall.remaining_sections), 'ACTION_LOGS')

    # next two functions define the game rules for action mask on whether the fill monument action is actually available to be taken
    @staticmethod
    def is_legal_to_fill_monument_tile(engine: Engine, energy_type: Energy) -> bool:
        # Check turn is type action
        if(not engine.turn.get_turn_type() == TurnType.ACTION_TURN):
            return False

        # Check if current monument is completed, should never occur
        if(engine.monuments[engine.monument_index].is_completed()):
            return False

        # check if they even have that energy they want to fill
        current_player = engine.players[engine.current_player]
        if(len(current_player.energies_released[energy_type]) == 0):
            return False
        
        return True

    @staticmethod
    def is_legal_single(engine: Engine, player: Player) -> bool:
        current_monument = engine.monuments[engine.monument_index]
        if(not engine.turn.get_turn_type() == TurnType.ACTION_TURN):
            Logger.log('1st condition, turn type', 'OTHER_LOGS')
            return False

        if(current_monument.is_completed()):
            Logger.log('2nd condition, monument complete', 'OTHER_LOGS')
            return False

        if(len(player.energies_released[Energy.SINGLE]) == 0):
            Logger.log('3rd condition, no released energy', 'OTHER_LOGS')
            Logger.log('player energies: ' + str(player.energies_released), 'OTHER_LOGS')
            return False
        
        if Energy.SINGLE in current_monument.get_top_wall().remaining_sections:
            Logger.log('4th condition, TRUE', 'OTHER_LOGS')
            return True

        Logger.log('no condition, FALSE', 'OTHER_LOGS')
        return False