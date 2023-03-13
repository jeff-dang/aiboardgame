from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player

from env.entities.energy import Energy
from env.helpers.logger import Logger


class MonumentWall():

    # acceptable_energy_types is a list of energy types that can be placed on this tile
    # num_sections is the number of sections on this tile
    # filled_sections is a list of the energy types that are currently placed on this tile
    # empty_sections is the number of sections that are currently empty
    # owner is the player that owns this tile --> Can identify the owner of every energy tile using EnergyTile.owner
    # monument_benefit_token is the benefit token that is placed on this tile, implementation of this is TBD
    def __init__(self, acceptable_energy_types: list[Energy], rewarded_energy: list[Energy], monument_benefit_token: list = None):
        Logger.log('monument_wall.py - INITIALIZING monuments with list: ' + str(acceptable_energy_types), 'INITIALIZATION_LOGS')
        self.sections: list[Energy] = acceptable_energy_types
        self.remaining_sections: list[Energy] = acceptable_energy_types
        self.num_sections: int = len(acceptable_energy_types)
        self.filled_sections: list[Energy] = [0]*self.num_sections
        self.empty_sections: int = self.num_sections
        # TODO: need to change it to one benefit token & one energy type
        self.monument_benefit_token: list = monument_benefit_token
        self.rewarded_energy: list[Energy] = rewarded_energy
        self.is_reward_given: bool = False
        self.owner: Player = None
    # fills the section at the given energy_type by macthing the first available matching section

    def check_accept(self, energy_type: Energy) -> bool:
        is_successful: bool = False
        if(self.empty_sections != 0):
            if energy_type == Energy.PRIMAL:
                is_successful = True
            elif energy_type in self.remaining_sections:
                Logger.log('ENERGY ACTION MASK IS ACCEPTABLE CHECK: ' + str(energy_type) + ' ' + str(self.remaining_sections), 'MONUMENT_LOGS')
                is_successful = True

        return is_successful

    def fill_section(self, energy: Energy) -> bool:
        is_successful = False
        if(self.empty_sections != 0):
            Logger.log('e type is: ' + str(energy.energy_type), 'MONUMENT_LOGS')
            Logger.log('self.sections is: ' + str(self.sections), 'MONUMENT_LOGS')
            if energy.energy_type == Energy.PRIMAL:
                # get the first empty section's index
                index = self.filled_sections.index(0)
                # fill the first empty section with energy
                self.filled_sections[index] = energy
                self.remaining_sections[index] = None
                self.empty_sections -= 1
                Logger.log('SECTION FILLED WITH ENERGY: ' + str(energy.energy_type), 'MONUMENT_LOGS')
                is_successful = True
            elif energy.energy_type in self.remaining_sections:
                index = self.remaining_sections.index(energy.energy_type)
                if self.filled_sections[index] == 0:
                    self.filled_sections[index] = energy
                    self.remaining_sections[index] = None
                    self.empty_sections -= 1
                    Logger.log('SECTION FILLED WITH ENERGY: ' + str(energy.energy_type), 'MONUMENT_LOGS')
                    is_successful = True
                else:
                    Logger.log('All the sections with the matching energy type is filled', 'MONUMENT_LOGS')
            else:
                Logger.log('Energy type is not supported on this monument wall - condition is: ' + str(energy.energy_type in self.sections) + ' where the supported sections are ' + str(self.sections), 'MONUMENT_LOGS')
            if self.is_completed():
                # TODO: find a way to assign the owner who finished the wall
                self.set_owner(energy.owner)
        else:
            Logger.log('All the sections are filled. Please try to fill the next wall of the monument', 'MONUMENT_LOGS')
        return is_successful

    # assigns the owner of this tile
    def set_owner(self, owner: Player):
        if(self.is_completed()):
            self.owner = owner

    # returns the owner of this tile
    def get_owner(self) -> Player:
        return self.owner

    # returns the energy type that can be placed at the given section index
    def get_acceptable_energy_type_at(self, section_index):
        return self.sections[section_index]

    # returns the energy type that is currently placed at the given section index
    def get_energy_at_filled_section(self, section_index):
        return self.filled_sections[section_index]

    # returns true if this tile is completed
    def is_completed(self) -> bool:
        return self.empty_sections == 0

    def get_monument_benefit_token(self):
        return self.monument_benefit_token
