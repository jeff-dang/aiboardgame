from env.entities.monumentWall import MonumentWall

class Monument:
    def __init__(self, name, location, monumentWalls):
        self.name = name
        self.walls = monumentWalls # list of MonumentTile objects
        self.completed_walls = [] # list of completed MonumentTile objects
        self.location = location #TODO: need a way to know where the monument is located on the board
        self.top_wall_index = len(self.walls)-1

    def is_completed(self):
        if self.top_wall_index == 0 and self.is_top_wall_completed():
            return True
        else:
            return False

    def get_top_wall(self):
        return self.walls[self.top_wall_index] # returns the top tile

    def is_top_wall_completed(self):
        return self.get_top_wall().is_completed()

    def change_top_wall(self):
        if self.top_wall_index >= 1:
            self.top_wall_index -= 1
            print('Index is: ', self.top_wall_index) #DELETE
            print('TOP WALL SWITCHED') #DELETE
        else:
            print('MONUMENT COMPLETED') #DELETE

