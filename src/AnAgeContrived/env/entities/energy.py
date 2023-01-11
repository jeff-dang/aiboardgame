class Energy():

    ENERGY_TYPES = ['0', '1', '2', 'special']

    def __init__(self) -> None:
        self.energy_type = 'default'

    def get_energy_type(self):
        return self.energy_type

    def set_energy_type(self, energy_type):
        if energy_type not in self.ENERGY_TYPES:
            print('Wrong energy_type. Please enter a correct energy type')
        else:
            self.energy_type = energy_type