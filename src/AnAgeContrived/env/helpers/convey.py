
MAX_STEP_SIZE = 2


class Convey():

    # probably also don't need the isLegalAction function. If necessary what to check?
    def isLegalAction(self, transmuter, stepSize, order):
        #character = player.getCharacterType()
        # if charachter == 'Dragon':
        #   return False
        return True

    @staticmethod
    def convey(engine, transmuter, stepSize, order):
        print("Convey", stepSize)
        if stepSize == 1:
            transmuter.convey(order)
        elif stepSize == 2:
            if order == 0:
                transmuter.convey(0)
                transmuter.convey(1)
            else:
                transmuter.convey(1)
                transmuter.convey(0)
        engine.turn.conveyed()
    # if the functions are not static, available actions may not work globally but be player dependent

    def convey1Legal(engine):
        return engine.turn.canConvey

    # TODO Need to check if player can convey twice
    def convey2Legal(engine):
        return engine.turn.canConvey and False

    def availableActions(self):
        return []
