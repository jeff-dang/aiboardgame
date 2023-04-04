# Author: Jonah Ada
# Date: January 10th, 2023
# Description: 
# Module for defining the parent class of Command Design Pattern

# Parent class for Command Design Pattern
class Command():

    def __init__(self, player, engine):
        self.player = player
        self.engine = engine