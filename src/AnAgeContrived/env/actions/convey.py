from actions import ActionBase
from functools import partial
#import Player

MAX_STEP_SIZE = 2


class Convey(ActionBase):

    # probably also don't need the isLegalAction function. If necessary what to check?
    def isLegalAction(self, transmuter, stepSize, order):
        #character = player.getCharacterType()
        # if charachter == 'Dragon':
        #   return False
        return True

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

    # if the functions are not static, available actions may not work globally but be player dependent
    def availableActions(self):
        return []
