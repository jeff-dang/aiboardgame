import transmuterTile
class Transmuter:
    def __init__(self):
        
        t1 = transmuterTile.TransmuterTile(1, 1)
        t2 = transmuterTile.TransmuterTile(1, 1)
        t3 = transmuterTile.TransmuterTile(1, 1)
        t4 = transmuterTile.TransmuterTile(1, 1)
        t5  = transmuterTile.TransmuterTile(2, 1)
        t6 = transmuterTile.TransmuterTile(2, 1)
        t7  = transmuterTile.TransmuterTile(2, 1)

        t1.fillTile(1, 1)
        t1.fillTile(1, 2)

        t2.fillTile(1, 1)
        t2.fillTile(1, 2)

        t3.fillTile(1, 1)
        t3.fillTile(1, 2)

        self.active_tiles = [t1, t2, t3, t4, t5]
        self.reserved_tiles = [t6, t7]
        self.action_tokens = []
        pass

    # gets all the tiles currently on the transmuter
    def getAllTiles(self):
        pass

    # returns the tile at the given position
    def getTile(self, position):
        pass

    # conveys the transmuter tiles by the given amount
    def convey(self, amount):
        pass

    # helper func to move the tiles after removing a tile
    def _moveAllTilesAhead(self):
        pass

    def isFull(self):
        pass
    