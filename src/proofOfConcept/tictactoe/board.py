class Board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def getState(self):
        return self.board

    def getPlace(self, place):
        return self.board[place]

    def placeTile(self, place, player):
        self.board[place] = player

    def printBoard(self):
        for idx, tile in enumerate(self.board):
            newTile = None
            if(tile == 1):
                newTile = 'X'
            elif(tile == 2):
                newTile = 'O'
            else:
                newTile = '_'
            print(" | " + newTile + " | ", end='')
            if((idx+1) % 3 == 0):
                print()
                print(" -------------------")
