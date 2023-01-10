# import fnmatch
# import os
# import imp
# import inspect
from commands.command import Command
import commands.conveyCommand

#TODO need to import all the classes in the commands somehow
def get_actions():
    #TODO: define player and board properly
    actions = [cls('player', 'board') for cls in Command.__subclasses__()]
    return actions

l = get_actions()
print('list is: ', l)