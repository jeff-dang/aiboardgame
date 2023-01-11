class MonumentTile:

    # acceptable_energy_types is a list of energy types that can be placed on this tile
    # num_sections is the number of sections on this tile
    # filled_sections is a list of the energy types that are currently placed on this tile
    # empty_sections is the number of sections that are currently empty
    # owner is the player that owns this tile --> TODO: May need multiple owners
    # monument_benefit_token is the benefit token that is placed on this tile, implementation of this is TBD
    def __init__(self, acceptable_energy_types, monument_benefit_token):
        self.sections = acceptable_energy_types
        self.num_sections = len(acceptable_energy_types) #TODO: May need to calculate it differently because there might be multiple tiles with the same energy type
        self.filled_sections = [0]*self.num_sections
        self.empty_sections = self.num_sections
        self.monument_benefit_token = monument_benefit_token
        self.owner = None

    # fills the section at the given index with the given energy type
    def fillSection(self, section_index, energy):
        if(self.empty_sections != 0):
            self.filled_sections[section_index] = energy
            self.empty_sections -= 1
    
    # assigns the owner of this tile
    def assignOwner(self, owner):
        if(self.isCompleted()):
            self.owner = owner
    
    # returns the owner of this tile
    def getOwner(self):
        return self.owner

    # returns the energy type that can be placed at the given section index
    def getAcceptableEnergyTypeAt(self, section_index):
        return self.sections[section_index]

    # returns the energy type that is currently placed at the given section index
    def getEnergyAtFilledSection(self, section_index):
        return self.filled_sections[section_index]

    # returns true if this tile is completed
    def isCompleted(self):
        return self.empty_sections == 0

    def getMonumentBenefitToken(self):
        return self.monument_benefit_token