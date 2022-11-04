# Only point of entry
from board import Board
from enum import Enum


class Engine:
    def __init__(self):
        self.board = Board()
        self.currentTurn = 1

    def getState(self, player):
        # Depending on player given, state may differ
        self.board.printBoard()
        return {"board": self.board.getState(), "currentTurn": self.currentTurn, "isGameDone": self.isGameFinished()}

    def getMoveList(self):
        # Return vector of possible moves
        moveList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        return

    def isGameFinished(self):
        b = self.board.getState()
        # Turn to 2D array
        bNew = [b[0:3], b[3:6], b[6:9]]

        WINNERS = (
            [(0, 0), (0, 1), (0, 2)],  # Horizontal
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],  # Vertical
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],  # Diagonal
            [(0, 2), (1, 1), (2, 0)],
        )

        for indexes in WINNERS:
            row = [bNew[r][c] for r, c in indexes]
            if all(cell == 1 for cell in row):
                return 1
            if all(cell == 2 for cell in row):
                return 2
        return 0

    def makeMove(self, player, moveList):
        if(not self.validateMove(player, moveList)):
            return False

        # Get tile placement
        tilePlacement = moveList.index(1)
        self.board.placeTile(tilePlacement, player)
        self.currentTurn = self.currentTurn % 2 + 1
        return True

    def validateMove(self, player, moveList):
        # Check that it is the current players turn
        if(player != self.currentTurn):
            print("Not players turn")
            return False

        # Check that only 1 exact move is played
        counter = 0
        moveIndex = -1
        for index, move, in enumerate(moveList):
            if(move):
                counter += 1
                moveIndex = index

        if(counter != 1):
            print("More than 1 move is trying to be made or no moves made")
            return False

        # Check place is not already taken
        if(self.board.getPlace(moveIndex) != 0):
            print("Tile already placed in this spot")
            return False

        return True
