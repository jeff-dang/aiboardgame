import sys
print(sys.path)
from actions.player import Player
from actions.transmuter import Transmuter
from actions.convey import Convey
from actions.actions import ActionBase
from actions.commands import *
#import commands
# import commands.command, commands.conveyCommand
# import commands.command, commands.conveyOnceFirstCard, commands.conveyOnceSecondCard
# import commands.conveyCommand
from actions.action_initiater import get_actions


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
print(actions.commands.command.Command.__subclasses__())
print(get_actions())