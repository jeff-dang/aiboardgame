# Only point of entry
from board import Board
from enum import Enum


class MoveList(Enum):
    PlaceTile = 1


class Engine:
    def __init__(self):
        self.players = []
        self.board = Board()

    def getState(self, player):
        # Depending on player given, state may differ
        pass

    def getMoveList(self):
        # Return enum of possible moves
        return list(MoveList)

    def isGameFinished():
        pass

    def makeMove(self, player, move):

        pass

    def validateMove(self, player, move):
        pass
