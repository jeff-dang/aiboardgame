from player import Player
from transmuter import Transmuter
from convey import Convey


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
p2.get_player_name()