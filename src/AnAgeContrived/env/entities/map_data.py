# Author: Michael Ilao
# Date: January 28th, 2023
# Description: 
# data that defines the game map in AI agent usable way

from enum import Enum

# Enum for different map areas on the map
class MapAreas(Enum):
    PLAINS = 0
    QUARRY = 1
    SEA = 2
    MOUNTAIN = 3
    FOREST = 4
    SWAMP = 5

# encodes the map as dictionary where keys are places on map and values are permissable places to move from that location
map = {
    1: [2],
    2: [1, 3, 32],
    3: [2, 4, 36, 32],
    4: [3, 5, 36],
    5: [4, 6],
    6: [5, 7, 9],
    7: [6, 8, 9],
    8: [7],
    9: [6, 7, 10, 11],
    10: [9, 11, 12],
    11: [9, 10, 37],
    12: [10, 13],
    13: [12, 14, 16],
    14: [13, 15, 16],
    15: [14],
    16: [13, 14, 17, 18],
    17: [16, 18, 38],
    18: [16, 17, 19],
    19: [18, 20],
    20: [19, 21, 23],
    21: [20, 22, 23],
    22: [21],
    23: [20, 21, 24, 40],
    24: [23, 25, 40],
    25: [24, 26],
    26: [25, 27, 29],
    27: [26, 28, 29],
    28: [27],
    29: [26, 27, 30, 33],
    30: [29, 31, 33],
    31: [32],
    32: [2, 3, 31],
    33: [29, 30, 34],
    34: [33, 35, 39],
    35: [34, 36, 37],
    36: [3, 4, 35],
    37: [11, 35, 38],
    38: [17, 37, 39],
    39: [34, 38, 40],
    40: [23, 24, 39]
}

# encodes the bridge spaces as dictionary where the keys are the bridge number and values are which map location they are connecting
bridges = {
    1: [31, 32],
    2: [35, 36],
    3: [11, 37],
    4: [12, 13],
    5: [17, 38],
    6: [19, 20],
    7: [39, 40],
    8: [25, 26],
    9: [33, 34],
    10: [5, 6]
}

# assignes the map locations to map areas
areas = {
    MapAreas.PLAINS: [26, 27, 28, 29, 30, 31, 33],  # Library, Beacon
    MapAreas.QUARRY: [1, 2, 3, 4, 5, 36, 32],  # Edrondic Gate
    MapAreas.SEA: [6, 7, 8, 9, 10, 11, 12],  # Ship
    MapAreas.MOUNTAIN: [13, 14, 15, 16, 17, 18, 19],  # Forge
    MapAreas.FOREST: [20, 21, 22, 23, 24, 25, 40],  # Fortress
    MapAreas.SWAMP: [34, 35, 37, 38, 39]
}
