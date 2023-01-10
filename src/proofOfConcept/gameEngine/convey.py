from functools import partial
#import Player

class Convey():

    #do we need init? we probably want to have actions as static rather than initializing each action class
    def __init__(self, gameboard, player):
        self.gameboard = gameboard
        self.player = player
        self.MAX_STEP_SIZE = 2
        return

    #probably also don't need the isLegalAction function. If necessary what to check?
    def isLegalAction(self, agent):
        #character = player.getCharacterType()
        #if charachter == 'Dragon':
        #   return False
        return True

    #@staticmethod
    # def convey(self, stepSize, order):
    #     if self.isLegalAction():
    #         if stepSize == 1:
    #             player.transmuter.convey(order)
    #         elif stepSize == 2:
    #             if order == 0:
    #                 player.transmuter.convey(0)
    #                 player.transmuter.convey(1)
    #             else:
    #                 player.transmuter.convey(1)
    #                 player.transmuter.convey(0)

    @staticmethod
    def convey(transmuter, stepSize, order):
        if stepSize == 1:
            transmuter.convey(order)
        elif stepSize == 2:
            if order == 0:
                transmuter.convey(0)
                transmuter.convey(1)
            else:
                transmuter.convey(1)
                transmuter.convey(0)

    # #if the functions are not static, available actions may not work globally but be player dependent
    # def availableActions(self):
    #     return [partial(self.convey, transmuter, 1, None), partial(self.convey, transmuter, 2, 1)]