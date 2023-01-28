from env.entities.player import Player
from env.entities.transmuter import Transmuter
#from env.helpers.convey import Convey
from env.action_initiater import get_actions
from env.engine import Engine
from env.entities.monument import Monument
from env.entities.monument_wall import MonumentWall
from env.entities.energy import EnergyTile, Energy


def testMonumentEnergy():
    # e1 = EnergyTile('Constructive', 'player')
    # e2 = EnergyTile('Constructive', 'player')
    # e3 = EnergyTile('Invertible', 'player')
    # e4 = EnergyTile('Primal', 'player')
    e1 = EnergyTile(Energy.CONSTRUCTIVE, 'player')
    e2 = EnergyTile(Energy.INVERTIBLE, 'player')
    e3 = EnergyTile(Energy.GENERATIVE, 'player')
    e4 = EnergyTile(Energy.PRIMAL, 'player')
    print('energy type is: ', e4.get_energy_type())
    m1 = MonumentWall([e1.get_energy_type(), e2.get_energy_type(), e3.get_energy_type()], 'No benefit')
    m2 = MonumentWall([e1.get_energy_type(), e2.get_energy_type(), e3.get_energy_type()], 'No benefit')
    m3 = MonumentWall([e1.get_energy_type(), e2.get_energy_type(), e3.get_energy_type()], 'No benefit')
    mon = Monument('Test Monument', 'location', [m1, m2, m3])
    print('number of empty sections BEFORE filling: ', m1.empty_sections)
    print('monument tile sections: ', m1.sections)
    # m1.fill_section(e1)
    m1.fill_section(e4)
    print('number of empty sections AFTER filling: ', m1.empty_sections)
    print('energy in filled section is: ', m1.filled_sections)


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
    t1.print_transmuter()
    print('************* END **************')
    actions[3].execute()
    print('************* AFTER ****************')
    t1.print_transmuter()
    print('************* END **************')

# testConveying()
testMonumentEnergy()
# print(Energy.CONSTRUCTIVE.value)

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