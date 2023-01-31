from env.entities.player import Player
from env.entities.transmuter import Transmuter
# from env.helpers.convey import Convey
from env.action_initiater import get_actions
from env.engine import Engine
from env.entities.monument import Monument
from env.entities.monument_wall import MonumentWall
from env.entities.energy import EnergyTile, Energy
from env.states import States
from env.helpers.move_player import MovePlayer
import numpy as np


def test_map():
    e = Engine()
    p0 = e.get_agent("player_0")
    p1 = e.get_agent("player_1")
    p2 = e.get_agent("player_2")

    p2.location = 35
    p1.location = 37

    print(MovePlayer.is_legal_move(p0, e, 38))
    print(e.get_reward("player_0"))


test_map()


def test_transmuter_state():
    e = Engine()
    e.render("player_0")
    print("RENDERING DONE")
    state = e.get_game_state()
    arr = np.array(state)
    print(np.shape(arr))


def test_monument_energy():
    # e1 = EnergyTile('Constructive', 'player')
    # e2 = EnergyTile('Constructive', 'player')
    # e3 = EnergyTile('Invertible', 'player')
    # e4 = EnergyTile('Primal', 'player')
    e1 = EnergyTile(Energy.CONSTRUCTIVE, 'player')
    e2 = EnergyTile(Energy.INVERTIBLE, 'player')
    e3 = EnergyTile(Energy.GENERATIVE, 'player')
    e4 = EnergyTile(Energy.PRIMAL, 'player')
    print('energy type is: ', e4.get_energy_type())
    m1 = MonumentWall([e1.get_energy_type(), e2.get_energy_type(),
                       e3.get_energy_type()], 'No benefit')
    m2 = MonumentWall([e1.get_energy_type(), e2.get_energy_type(),
                       e3.get_energy_type()], 'No benefit')
    m3 = MonumentWall([e1.get_energy_type(), e2.get_energy_type(),
                       e3.get_energy_type()], 'No benefit')
    mon = Monument('Test Monument', 'location', [m1, m2, m3])
    print('number of empty sections BEFORE filling: ', m1.empty_sections)
    print('monument tile sections: ', m1.sections)
    # m1.fill_section(e1)
    m1.fill_section(e4)
    print('number of empty sections AFTER filling: ', m1.empty_sections)
    print('energy in filled section is: ', m1.filled_sections)


def test_conveying():
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
