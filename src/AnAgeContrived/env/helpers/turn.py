from env.entities.turn_state import TurnType
# Cant import from constatns.py since circular import
TOTAL_PLAYERS = 5


class Turn():

    @staticmethod
    def is_legal_action(agent):
        # Can always end turn, except when monument building
        return True

    @staticmethod
    def end_turn(engine):
        engine.current_player = (engine.current_player+1) % TOTAL_PLAYERS
        engine.turn_counter += 1
        engine.turn.reset()
        # Check for queued players before progressing in case of monument building

    @staticmethod
    def end_turn_legal(engine):
        if(engine.turn.turn_type == TurnType.CONVEY_TURN and engine.turn.can_convey == True):
            return False
        return engine.turn.turn_type != None

    @staticmethod
    def convey_turn(engine):
        engine.turn.update_turn_type(TurnType.CONVEY_TURN)

    @staticmethod
    def convey_turn_legal(engine):
        return engine.turn.turn_type == None

    @staticmethod
    def action_turn(engine):
        engine.turn.update_turn_type(TurnType.ACTION_TURN)

    @staticmethod
    def action_turn_legal(engine):
        return engine.turn.turn_type == None
