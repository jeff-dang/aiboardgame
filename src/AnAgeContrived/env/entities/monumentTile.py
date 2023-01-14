from env.entities.energy import Energy

class MonumentTile:

    # acceptable_energy_types is a list of energy types that can be placed on this tile
    # num_sections is the number of sections on this tile
    # filled_sections is a list of the energy types that are currently placed on this tile
    # empty_sections is the number of sections that are currently empty
    # owner is the player that owns this tile --> Can identify the owner of every energy tile using EnergyTile.owner
    # monument_benefit_token is the benefit token that is placed on this tile, implementation of this is TBD
    def __init__(self, acceptable_energy_types, monument_benefit_token):
        self.sections = acceptable_energy_types
        self.num_sections = len(acceptable_energy_types)
        self.filled_sections = [0]*self.num_sections
        self.empty_sections = self.num_sections
        self.monument_benefit_token = monument_benefit_token
        self.owner = None

    # fills the section at the given energy_type by macthing the first available matching section
    def fill_section(self, energy):
        if(self.empty_sections != 0):
            print('e type is: ', energy.energy_type)
            if energy.energy_type == Energy.PRIMAL.name:
                index = self.filled_sections.index(0)
                self.filled_sections[index] = energy
                self.sections[index] = 'Filled'
                self.empty_sections -= 1
            elif energy.energy_type in self.sections:
                index = self.sections.index(energy.energy_type)
                if self.filled_sections[index] == 0:
                    self.filled_sections[index] = energy
                    self.sections[index] = 'Filled'
                    self.empty_sections -= 1
                else:
                    print('All the sections with the matching energy type is filled')
            else:
                print('Energy type is not supported on this monument wall')
            if self.is_completed():
                self.assign_owner(energy.owner) #TODO: find a way to assign the owner who finished the wall
        else:
            print('All the sections are filled. Please try to fill the next wall of the monument')
    
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