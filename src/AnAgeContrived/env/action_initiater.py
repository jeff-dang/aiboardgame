from env.command import Command
from env.actions import *


def get_actions(player, engine):
    actions = [cls(player, engine) for cls in Command.__subclasses__()]
    return actions