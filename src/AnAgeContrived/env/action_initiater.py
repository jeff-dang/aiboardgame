# Author: Jonah Ada
# Date: January 11th, 2023
# Description: 
# Module for automating the generation of action space by going through the env/actions folder and finding all defined actions

from env.command import Command
from env.actions import *

# goes through the env/actions folder, finds all defined action by the game engine and outputs them as a list
def get_actions(player, engine):
    actions = [cls(player, engine) for cls in Command.__subclasses__()]
    return actions