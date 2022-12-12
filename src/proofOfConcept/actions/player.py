class Player():

    number_of_players = 0
    def __init__(self) -> None:
        self.name = 'Player ' + str(self.number_of_players)
        self.transmuter = None
        self.number_of_players += 1

    def set_transmuter(self, transmuter):
        self.transmuter = transmuter

    def get_transmuter(self):
        return self.transmuter

    def set_player_name(self, name):
        self.name = name

    def get_player_name(self):
        return self.name