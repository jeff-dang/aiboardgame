from transmuter import Transmuter


class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.transmuter = Transmuter()

    def set_transmuter(self, transmuter):
        self.transmuter = transmuter

    def get_transmuter(self):
        return self.transmuter

    def set_player_name(self, name):
        self.name = name

    def get_player_name(self):
        return self.name
