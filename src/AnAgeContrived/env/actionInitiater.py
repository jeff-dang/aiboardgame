from env.command import Command
from env.actions import *


def get_actions(player, board):
    #TODO: define player and board properly
    actions = [cls(player, board) for cls in Command.__subclasses__()]
    return actions