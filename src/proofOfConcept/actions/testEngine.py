from player import Player
from transmuter import Transmuter
from convey import Convey
from actions import ActionBase
#from commands import *
# from commands.command import Command
import commands


t1 = Transmuter()
t2 = Transmuter()

p1 = Player()
p2 = Player()

p1.set_player_name('Player 1')
p1.set_transmuter(t1)
p2.set_transmuter(t2)

#actions = Convey.availableActions()
print('************* BEFORE ****************')
t1.printTransmuter()
print('************* END **************')
#actions[0](transmuter = p1.transmuter)
Convey.convey(p1.transmuter, 1, 1)
print('************* AFTER ****************')
t1.printTransmuter()
print('************* END **************')
print(p1.get_player_name())

print('************* BEFORE ****************')
t2.printTransmuter()
print('************* END **************')
#actions[0](transmuter = p1.transmuter)
Convey.convey(p2.transmuter, 2, 0)
print('************* AFTER ****************')
t2.printTransmuter()
print('************* END **************')
print(p2.get_player_name())

print(ActionBase.__subclasses__())
print(commands.Command.__subclasses__())