import sys
print(sys.path)
from gameEngine.player import Player
from gameEngine.transmuter import Transmuter
from gameEngine.convey import Convey
#from gameEngine.actions import ActionBase
#from gameEngine.actions import *
from gameEngine.action_initiater import get_actions
from gameEngine import command
from gameEngine.actions import conveyOnceFirstCard, conveyOnceSecondCard, conveyTwiceFirstOrder, conveyTwiceSecondOrder


t1 = Transmuter()
t2 = Transmuter()

p1 = Player()
p2 = Player()

p1.set_player_name('Player 1')
p1.set_transmuter(t1)
p2.set_transmuter(t2)

print('ACTION LIST')
actions = get_actions(p1, 'board')
print(actions)

print('************* BEFORE ****************')
t1.printTransmuter()
print('************* END **************')
actions[0].execute()
print('************* AFTER ****************')
t1.printTransmuter()
print('************* END **************')

# #actions = Convey.availableActions()
# print('************* BEFORE ****************')
# t1.printTransmuter()
# print('************* END **************')
# #actions[0](transmuter = p1.transmuter)
# Convey.convey(p1.transmuter, 1, 1)
# print('************* AFTER ****************')
# t1.printTransmuter()
# print('************* END **************')
# print(p1.get_player_name())

# print('************* BEFORE ****************')
# t2.printTransmuter()
# print('************* END **************')
# #actions[0](transmuter = p1.transmuter)
# Convey.convey(p2.transmuter, 2, 0)
# print('************* AFTER ****************')
# t2.printTransmuter()
# print('************* END **************')
# print(p2.get_player_name())

#print(ActionBase.__subclasses__())
#print(gameEngine.actions.command.Command.__subclasses__())
#print(get_actions())