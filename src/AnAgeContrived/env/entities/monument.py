from env.entities.monumentTile import MonumentTile

class Monument:
    def __init__(self, name, monumentTiles):
        self.name = name
        self.tiles = monumentTiles # list of MonumentTile objects
        self.completed_tiles = [] # list of completed MonumentTile objects
        self.location = None #TODO: need a way to know where the monument is located on the board

    def is_completed(self):
        return len(self.tiles) == 0 # if there are no tiles left, the monument is completed

    def get_top_tile(self):
        return self.tiles[len(self.tiles)-1] # returns the top tile

    #TODO: need to switch the top tile when the tile is filled