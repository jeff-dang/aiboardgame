
TOTAL_PLAYERS = 4


class Turn():

    @staticmethod
    def is_legal_action(agent):
        # Can always end turn, except when monument building
        return True

    @staticmethod
    def end_turn(engine):
        print("End Turn")
        engine.current_player = (engine.current_player+1) % TOTAL_PLAYERS
        engine.turn_counter += 1
        engine.turn.reset()
        # Check for queued players before progressing in case of monument building

    @staticmethod
    def end_turn_legal(engine):
        if(engine.turn.turn_type == "convey" and engine.turn.can_convey == True):
            return False
        return len(engine.turn.turn_type) > 0

    @staticmethod
    def convey_turn(engine):
        print("Choose Convey Turn")
        engine.turn.update_turn_type('convey')

    @staticmethod
    def convey_turn_legal(engine):
        return len(engine.turn.turn_type) == 0

    @staticmethod
    def action_turn(engine):
        print("Choose Action Turn")
        engine.turn.update_turn_type('action')

    @staticmethod
    def action_turn_legal(engine):
        return len(engine.turn.turn_type) == 0
