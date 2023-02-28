from env.entities.monument_wall import MonumentWall
from env.helpers.logger import Logger

class Monument:
    def __init__(self, name: str, location, monumentWalls: list[MonumentWall]):
        self.name: str = name
        self.walls: list[MonumentWall] = monumentWalls
        self.completed_walls: list[MonumentWall] = []
        self.location = location
        self.top_wall_index: int = 0

    def get_num_walls_completed(self) -> int:
        return len(self.walls) - (self.top_wall_index + 1)

    def is_completed(self) -> bool:
        if self.top_wall_index == 0 and self.is_top_wall_completed():
            return True
        else:
            return False

    def get_top_wall(self) -> MonumentWall:
        return self.walls[self.top_wall_index]  # returns the top tile

    def is_top_wall_completed(self) -> bool:
        return self.get_top_wall().is_completed()

    def change_top_wall(self):
        if self.top_wall_index < len(self.walls) - 1:
            self.top_wall_index += 1
            Logger.log('Index is: ' + str(self.top_wall_index), 'MONUMENT_LOGS')
            Logger.log('TOP WALL SWITCHED', 'MONUMENT_LOGS')
        else:
            Logger.log('MONUMENT COMPLETED', 'MONUMENT_LOGS')
