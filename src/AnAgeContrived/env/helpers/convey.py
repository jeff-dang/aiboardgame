
MAX_STEP_SIZE = 2


class Convey():

    # TODO: need to change the convey requiring engine as a parameter since we are calling the actions inside the Engine class
    # before Engine object is initiated
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

    @staticmethod
    def convey1Legal(engine):
        return engine.turn.can_convey

    @staticmethod
    # TODO Need to check if player can convey twice
    def convey2Legal(engine):
        return engine.turn.can_convey and False
