# import fnmatch
# import os
# import imp
# import inspect
from gameEngine.command import Command
#import gameEngine.actions.conveyCommand
from gameEngine.actions import *
#from gameEngine.actions import conveyOnceFirstCard, conveyOnceSecondCard, conveyTwiceFirstOrder, conveyTwiceSecondOrder

#TODO need to import all the classes in the commands somehow
def get_actions(player, board):
    #TODO: define player and board properly
    actions = [cls(player, board) for cls in Command.__subclasses__()]
    return actions

# l = get_actions()
# print('list is: ', l)