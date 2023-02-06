from env.entities.turn_state import TurnType

MAX_STEP_SIZE = 2


class Convey():

    # TODO: need to change the convey requiring engine as a parameter since we are calling the actions inside the Engine class
    # before Engine object is initiated
    @staticmethod
    def convey(engine, player, stepSize, order):
        print("Convey", stepSize)
        if stepSize == 1:
            player.transmuter.convey(player, order)
        elif stepSize == 2:
            if order == 0:
                player.transmuter.convey(player, 0)
                player.transmuter.convey(player, 1)
            else:
                player.transmuter.convey(player, 1)
                player.transmuter.convey(player, 0)
        engine.turn.conveyed()
    # if the functions are not static, available actions may not work globally but be player dependent

    @staticmethod
    def convey1Legal(engine):
        return engine.turn.can_convey and engine.turn.get_turn_type() == TurnType.CONVEY_TURN

    @staticmethod
    # TODO Need to check if player can convey twice
    def convey2Legal(engine):
        return engine.turn.can_convey and False and engine.turn.get_turn_type() == TurnType.CONVEY_TURN and engine.current_player.channel_marker
