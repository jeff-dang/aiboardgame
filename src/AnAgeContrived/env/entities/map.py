from env.helpers.logger import Logger
from .map_data import map, bridges, areas
from .bridge import Bridge


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
        if(self.check_bridge_exists(location)):
            Logger.log('BRIDGE ALREADY EXISTS', 'MAP_LOGS')
            return False
        b = Bridge(player.agent, reward, location)
        self.player_bridges.append(b)
