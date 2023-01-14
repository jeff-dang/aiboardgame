
TOTAL_PLAYERS = 4


class Turn():

    @staticmethod
    def isLegalAction(agent):
        # Can always end turn, except when monument building
        return True

    @staticmethod
    def endTurn(engine):
        print("End Turn")
        engine.current_player = (engine.current_player+1) % TOTAL_PLAYERS
        engine.turnCounter += 1
        engine.turn.reset()
        # Check for queued players before progressing in case of monument building

    @staticmethod
    def endTurnLegal(engine):
        if(engine.turn.turnType == "convey" and engine.turn.canConvey == True):
            return False
        return len(engine.turn.turnType) > 0

    @staticmethod
    def conveyTurn(engine):
        print("Choose Convey Turn")
        engine.turn.updateTurnType('convey')

    @staticmethod
    def conveyTurnLegal(engine):
        return len(engine.turn.turnType) == 0

    @staticmethod
    def actionTurn(engine):
        print("Choose Action Turn")
        engine.turn.updateTurnType('action')

    @staticmethod
    def actionTurnLegal(engine):
        return len(engine.turn.turnType) == 0
