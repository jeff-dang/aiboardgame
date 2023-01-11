from env.entities.player import Player
from env.entities.transmuter import Transmuter
#from env.helpers.convey import Convey
from env.actionInitiater import get_actions
from env.engine import Engine
from env.entities.monument import Monument
from env.entities.monumentTile import MonumentTile
from env.entities.energy import Energy


def testMonumentEnergy():
    pass


def testConveying():
    t1 = Transmuter()
    t2 = Transmuter()

    e = Engine()

    p1 = Player('player_0', 'Freyith')
    p2 = Player('player_1', 'Ignotas')

    # p1.set_player_name('Player 1')
    p1.set_transmuter(t1)
    p2.set_transmuter(t2)

    print('ACTION LIST')
    actions = get_actions(p1, e)
    print(actions)

    print('************* BEFORE ****************')
    t1.printTransmuter()
    print('************* END **************')
    actions[3].execute()
    print('************* AFTER ****************')
    t1.printTransmuter()
    print('************* END **************')

testConveying()

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