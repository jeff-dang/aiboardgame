class Energy():

    def __init__(self) -> None:
        self.energy_type = 'default'

    def get_energy_type(self):
        return self.energy_type

    def set_energy_type(self, energy_type):
        self.energy_type = energy_type