from actions import ActionBase
from functools import partial

class Convey(ActionBase):

    def __init__(self, gameboard, player):
        self.gameboard = gameboard
        self.player = player
        self.MAX_STEP_SIZE = 2
        return

    def isLegalAction(self, agent):
        #character = player.getCharacterType()
        #if charachter == 'Dragon':
        #   return False
        return True

    #TODO: which player? player.transmuter.move()
    def convey(self, stepSize, order):
        #transmuter = player.getTransmuter()
        if self.isLegalAction():
            if stepSize == 1:
                transmuter.convey(order)
            elif stepSize == 2:
                if order == 0:
                    transmuter.move(0)
                    transmuter.move(1)
                else:
                    transmuter.move(1)
                    transmuter.move(0)


    def availableActions(self):
        return [partial(self.convey, 1, None), partial(self.convey, 2, 1)]