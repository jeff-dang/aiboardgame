from env.command import Command
from env.check import Check
from env.actions import *


def get_actions(player, engine):
    #TODO: define player and board properly
    actions = [cls(player, engine) for cls in Command.__subclasses__()]
    return actions

def get_legal_actions(player, engine):
    legal_actions = [cls(player, engine) for cls in Check.__subclasses__()]
    return legal_actions