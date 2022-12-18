from actions import ActionBase
from functools import partial
#import Player

TOTAL_PLAYERS = 4


class Turn(ActionBase):

    @staticmethod
    def isLegalAction():
        # Can always end turn, except when monument building
        return True

    @staticmethod
    def endTurn(engine):
        (engine.current_player+1) % TOTAL_PLAYERS
        # Check for queued players before progressing in case of monument building

    @staticmethod
    def availableActions():
        return []
