from .transmuter import Transmuter


class Player():

    def __init__(self, agent, character) -> None:
        self.agent = agent
        self.character = character
        self.transmuter = Transmuter()

    def set_transmuter(self, transmuter):
        self.transmuter = transmuter

    def get_transmuter(self):
        return self.transmuter

    def get_player_name(self):
        return self.agent
