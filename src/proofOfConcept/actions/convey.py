from actions import ActionBase
from functools import partial

class Convey(ActionBase):
    def isLegalAction(self):
        #character = player.getCharacterType()
        #if charachter == 'Dragon':
        #   return False
        return True

    def convey(self, stepSize):
        #transmuter = player.getTransmuter()
        if self.isLegalAction():
            if stepSize == 1:
                #transmuter.move(1)
                return
            elif stepSize == 2:
                #transmuter.move(2)
                return


    def availableActions(self):
        return [partial(self.convey, 1), partial(self.convey, 2)]