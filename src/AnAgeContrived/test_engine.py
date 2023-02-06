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
from env.helpers.constants import THE_ERIDONIC_GATE
from env.helpers import take_action as TakeAction


import numpy as np

MAX_SIZE_EMBEDDED_ARRAY = 6


def test_action_tokens():
    player1 = Player('a', 'c', 1)
    player1.transmuter.print_transmuter()
    TakeAction.take_action(player1, 2)

test_action_tokens()



def build_2_walls(e):
    e.play_turn("player_0", 48)
    e.play_turn("player_0", 47)
    e.play_turn("player_0", 50)
    return
    e.play_turn("player_1", 48)
    e.play_turn("player_1", 44)
    e.play_turn("player_1", 50)
    return
    print(e.get_legal_action_names("player_0"))
    e.play_turn("player_0", 44)
    print(e.get_legal_action_names("player_0"))
    e.play_turn("player_0", 47)
    print(e.get_legal_action_names("player_0"))
    e.play_turn("player_0", 45)
    print(e.get_legal_action_names("player_0"))
    e.play_turn("player_0", 45)
    print(e.get_legal_action_names("player_0"))
    e.play_turn("player_0", 44)


def test_monument():
    e = Engine()
    current_player = "player_0"
    # e.get_action_names()
    # build_2_walls(e)
    e.monuments = e.monuments[0:1]
    for i, monument in enumerate(e.monuments):
        embedded_monument_num = [0]*MAX_SIZE_EMBEDDED_ARRAY
        embedded_monument_location = [0]*MAX_SIZE_EMBEDDED_ARRAY
        embedded_num_walls_completed = [0]*MAX_SIZE_EMBEDDED_ARRAY

        embedded_monument_num[i] = 1
        embedded_monument_location[monument.location.value] = 1
        embedded_num_walls_completed[monument.get_num_walls_completed()] = 1

        MAX_SIZE_WALL_TILE_SPOTS = 3
        embedded_top_wall_pos_accepts = [
            [0]*MAX_SIZE_EMBEDDED_ARRAY for _ in range(MAX_SIZE_WALL_TILE_SPOTS)]
        embedded_top_wall_pos_owner = [
            [0]*MAX_SIZE_EMBEDDED_ARRAY for _ in range(MAX_SIZE_WALL_TILE_SPOTS)]
        print(embedded_top_wall_pos_owner)

        # Does not have a third spot to fill, accepts none and owner is none
        if(monument.get_top_wall().num_sections < 3):
            embedded_top_wall_pos_accepts[MAX_SIZE_WALL_TILE_SPOTS-1][0] = 1
            embedded_top_wall_pos_owner[MAX_SIZE_WALL_TILE_SPOTS -
                                        1][len(e.players)] = 1

        # Assigns value based on filled sections and who owns them
        for i, pos in enumerate(monument.get_top_wall().filled_sections):
            # No player owns it assign it last index (index 5)
            if(pos == 0):
                embedded_top_wall_pos_owner[i][len(e.players)] = 1
            else:
                current_players_index = next(
                    (index for (index, d) in enumerate(e.players) if d.agent == current_player), None)

                owner_index = next(
                    (index for (index, d) in enumerate(e.players) if d.agent == pos.owner.agent), None)
                distance_between = (owner_index - current_players_index) % 5
                embedded_top_wall_pos_owner[i][distance_between] = 1

        # Assigns value based on remaining sections and their accepting energy
        for i, pos in enumerate(monument.get_top_wall().remaining_sections):
            if(pos is None):
                embedded_top_wall_pos_accepts[i][0] = 1
            else:
                embedded_top_wall_pos_accepts[i][pos.value] = 1

        MAX_SIZE_WALLS_PER_MONUMENT = 5  # Most have 4, one has 5
        embedded_top_wall_pos_accepts = [
            [0]*MAX_SIZE_EMBEDDED_ARRAY for _ in range(MAX_SIZE_WALL_TILE_SPOTS)]
        embedded_top_wall_pos_owner = [
            [0]*MAX_SIZE_EMBEDDED_ARRAY for _ in range(MAX_SIZE_WALL_TILE_SPOTS)]
        print(embedded_top_wall_pos_owner)
        for j, wall in enumerate(monument.walls):
            if(monument.get_num_walls_completed() > 0):
                print(j, wall)
                for etile in wall.filled_sections:
                    if(etile != 0):
                        print("energy", etile.owner.agent)
                if(wall.owner):
                    print("owner", wall.owner.agent)

                pass


# test_monument()


def get_all_actions():
    e = Engine()
    e.get_action_names()


# get_all_actions()


def test_map():
    e = Engine()
    p0 = e.get_agent("player_0")
    p1 = e.get_agent("player_1")
    p2 = e.get_agent("player_2")

    p2.location = 35
    p1.location = 37

    print(MovePlayer.is_legal_move(p0, e, 38))
    print(e.get_reward("player_0"))


def test_map_state():
    e = Engine()
    # e.render("player_0")
    print("RENDERING DONE")
    state = e.get_game_state()
    print(state)
    for i in state:
        print(i)
        print(len(i))
    arr = np.array(state)
    print(np.shape(arr))


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
    e1 = EnergyTile(Energy.CONSTRUCTIVE, 'player 0')
    e2 = EnergyTile(Energy.INVERTIBLE, 'player 0')
    e3 = EnergyTile(Energy.GENERATIVE, 'player 0')
    e4 = EnergyTile(Energy.CONSTRUCTIVE, 'player 0')
    e5 = EnergyTile(Energy.INVERTIBLE, 'player 1')
    e6 = EnergyTile(Energy.CONSTRUCTIVE, 'player 2')

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

    m1.fill_section(e4)
    m1.fill_section(e6)
    m1.fill_section(e5)

    print('number of empty sections AFTER filling: ', m1.empty_sections)
    print('energy in filled section is: ', m1.filled_sections)
    print(m1.is_completed())
    print(m1.owner)

    print(m1.remaining_sections)
    print(e5.energy_type)


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
