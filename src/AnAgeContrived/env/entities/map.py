from env.helpers.logger import Logger
from .map_data import map, bridges, areas
from .bridge import Bridge
from env.helpers.constants import STARTING_PLAYER_BRIDGES


class Map:
    def __init__(self):
        self.map = map
        self.bridge_locations = bridges
        self.areas = areas
        self.starting_positions = [1, 8, 15, 22, 28]
        self.player_bridges = []

    def get_path(self, start, finish):
        # Base case start to finiish is 1 move
        if(finish in self.map[start]):
            return [start, finish]

        # Case player hops over another player to get over bridge
        path = [start]
        for location in self.map[start]:
            if(finish in self.map[location]):
                path.append(location)
                path.append(finish)
                break
        return path

    def check_crossed_bridge(self, path):
        for bridge in self.bridge_locations.items():
            if(set(bridge[1]).issubset(set(path))):
                return bridge[0]

        return False

    def check_bridge_exists(self, bridge):
        for b in self.player_bridges:
            if b.location == bridge:
                return True
        return False

    def get_player_bridge(self, bridge_num):
        for b in self.player_bridges:
            if b.location == bridge_num:
                return b
        return False

    def build_bridge(self, player, reward, location):

        tier = (STARTING_PLAYER_BRIDGES-player.num_bridges_left) + 1
        b = Bridge(player.agent, reward, location, tier)
        player.num_bridges_left -= 1
        self.player_bridges.append(b)

    def get_reward_type(self, player, reward):
        pass
