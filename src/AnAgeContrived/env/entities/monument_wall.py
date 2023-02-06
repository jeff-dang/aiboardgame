from env.entities.energy import Energy


class MonumentWall():

    # acceptable_energy_types is a list of energy types that can be placed on this tile
    # num_sections is the number of sections on this tile
    # filled_sections is a list of the energy types that are currently placed on this tile
    # empty_sections is the number of sections that are currently empty
    # owner is the player that owns this tile --> Can identify the owner of every energy tile using EnergyTile.owner
    # monument_benefit_token is the benefit token that is placed on this tile, implementation of this is TBD
    def __init__(self, acceptable_energy_types, rewarded_energy, monument_benefit_token=None):
        self.sections = acceptable_energy_types
        self.remaining_sections = acceptable_energy_types
        self.num_sections = len(acceptable_energy_types)
        self.filled_sections = [0]*self.num_sections
        self.empty_sections = self.num_sections
        # TODO: need to change it to one benefit token & one energy type
        self.monument_benefit_token = monument_benefit_token
        self.rewarded_energy = rewarded_energy
        self.owner = None
    # fills the section at the given energy_type by macthing the first available matching section

    def check_accept(self, energy_type):
        is_successful = False
        if(self.empty_sections != 0):
            if energy_type == Energy.PRIMAL:
                is_successful = True
            elif energy_type in self.remaining_sections:
                print(energy_type, self.remaining_sections)
                is_successful = True

        return is_successful

    def fill_section(self, energy: Energy):
        is_successful = False
        if(self.empty_sections != 0):
            print('e type is: ', energy.energy_type)
            print('self.sections is: ', self.sections)
            if energy.energy_type == Energy.PRIMAL:
                # get the first empty section's index
                index = self.filled_sections.index(0)
                # fill the first empty section with energy
                self.filled_sections[index] = energy
                self.remaining_sections[index] = None
                self.empty_sections -= 1
                print('SECTION FILLED WITH ENERGY: ',
                      energy.energy_type)  # DELETE LATER
                is_successful = True
            elif energy.energy_type in self.remaining_sections:
                # elif self._is_in_acceptable_energy_types(energy.energy_type):
                # index = self.get_acceptable_energy_types().index(energy.energy_type)
                index = self.remaining_sections.index(energy.energy_type)
                if self.filled_sections[index] == 0:
                    self.filled_sections[index] = energy
                    self.remaining_sections[index] = None
                    self.empty_sections -= 1
                    print('SECTION FILLED WITH ENERGY: ',
                          energy.energy_type)  # DELETE LATER
                    is_successful = True
                else:
                    print('All the sections with the matching energy type is filled')
            else:
                print('Energy type is not supported on this monument wall - condition is: ',
                      energy.energy_type in self.sections, 'where the supported sections are', self.sections)
            if self.is_completed():
                # TODO: find a way to assign the owner who finished the wall
                self.assign_owner(energy.owner)
        else:
            print(
                'All the sections are filled. Please try to fill the next wall of the monument')
        return is_successful

    # assigns the owner of this tile
    def assign_owner(self, owner):
        if(self.is_completed()):
            self.owner = owner

    # returns the owner of this tile
    def get_owner(self):
        return self.owner

    # returns the energy type that can be placed at the given section index
    def get_acceptable_energy_type_at(self, section_index):
        return self.sections[section_index]

    # returns the energy type that is currently placed at the given section index
    def get_energy_at_filled_section(self, section_index):
        return self.filled_sections[section_index]

    # returns true if this tile is completed
    def is_completed(self):
        return self.empty_sections == 0

    def get_monument_benefit_token(self):
        return self.monument_benefit_token

    # def _is_in_acceptable_energy_types(self, energy_type):
    #     acceptable_type_names = self.get_acceptable_energy_types()
    #     acceptable_type_numbers = self.sections
    #     return energy_type in acceptable_type_names or energy_type in acceptable_type_numbers

    # def get_acceptable_energy_types(self):
    #     acceptable_type_names = []
    #     for i in range(0, len(self.sections)):
    #         if self.sections[i] != 'Filled':
    #             acceptable_type_names.append(Energy(self.sections[i]).name)
    #         else:
    #             acceptable_type_names.append(self.filled_sections[i].energy_type)

    #     return acceptable_type_names

    # def print_wall(self):
    #     #TODO: print in a way to make sure the filled an unfilled sections are recognizable
    #     wall_string = ''
    #     wall_string += '---------------\n'
    #     wall_string += '|     ---     |\n'
    #     wall_string += '|    | {} |    |\n'.format(self.filled_sections[0])
    #     wall_string += '|     ---     |\n'
    #     wall_string += '|  ---   ---  |\n'
    #     wall_string += '| | {} | | {} | |\n'.format(
    #         self.filled_sections[1], self.filled_sections[2])
    #     wall_string += '|  ---   ---  |\n'
    #     wall_string += '|             |\n'
    #     wall_string += '|             |\n'
    #     wall_string += '|  ---   ---  |\n'
    #     wall_string += '| | {} | | {} | |\n'.format(
    #         self.rewarded_energy[0], self.rewarded_energy[1])
    #     wall_string += '|  ---   ---  |\n'
    #     wall_string += '|             |\n'
    #     wall_string += '---------------\n'

    #     return wall_string
