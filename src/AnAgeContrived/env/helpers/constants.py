from env.entities.monument import Monument
from env.entities.monument_wall import MonumentWall
from env.entities.energy import Energy
from env.action_initiater import get_actions
from env.entities.action_tokens import EnergyActionToken, MoveActionToken

CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne", "Aureon"]
AGENT_NAMES = ["player_0", "player_1", "player_2", "player_3", "player_4"]
NUM_MOVES = len(get_actions('self', 'eng'))
MAX_TURNS = 50

# ************ MONUMENTS START **************************
# Monuments From The Rule Book:
THE_ANFIRIEN_BEACON = Monument('THE ANFIRIEN BEACON', 'location', [
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.INVERTIBLE], [
                 Energy.CONSTRUCTIVE, Energy.INVERTIBLE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE,
                 Energy.GENERATIVE], [Energy.PRIMAL]),
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE,
                 Energy.INVERTIBLE], [Energy.GENERATIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE], ['Any'])
])
THE_LIBRARY_OF_VALDUIN = Monument('THE LIBRARY OF VALDUIN', 'location', [
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE], [
                 Energy.GENERATIVE, Energy.INVERTIBLE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE,
                 Energy.INVERTIBLE], [Energy.CONSTRUCTIVE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.GENERATIVE,
                 Energy.GENERATIVE], [Energy.PRIMAL]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.INVERTIBLE, Energy.GENERATIVE], ['Any'])
])
THE_ERIDONIC_GATE = Monument('THE ERIDONIC GATE', 'location', [
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE], [
                 Energy.CONSTRUCTIVE, Energy.GENERATIVE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE,
                 Energy.GENERATIVE], [Energy.INVERTIBLE]),
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE,
                 Energy.CONSTRUCTIVE], [Energy.GENERATIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE], ['Any'])
])
THE_NAMARILLION_FORGE = Monument('THE NAMARILLION FORGE', 'location', [
    MonumentWall([Energy.CONSTRUCTIVE, Energy.GENERATIVE, Energy.GENERATIVE], [
                 Energy.INVERTIBLE, Energy.GENERATIVE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE,
                 Energy.GENERATIVE], [Energy.PRIMAL]),
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE,
                 Energy.INVERTIBLE], [Energy.CONSTRUCTIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE], ['Any'])
])
THE_FORTRESS_OF_KOLYM_THRIN = Monument('THE FORTRESS OF KOLYM THRIN', 'location', [
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE], [
                 Energy.CONSTRUCTIVE, Energy.PRIMAL]),
    MonumentWall([Energy.INVERTIBLE, Energy.INVERTIBLE,
                 Energy.GENERATIVE], [Energy.GENERATIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE], ['Any']),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE,
                 Energy.GENERATIVE], [Energy.INVERTIBLE]),
    MonumentWall([Energy.PRIMAL], []),
])
THE_SHIP_OF_TOLINTHRA = Monument('THE SHIP OF TOLINTHRA', 'location', [
    MonumentWall([Energy.GENERATIVE, Energy.GENERATIVE, Energy.INVERTIBLE], [
                 Energy.CONSTRUCTIVE, Energy.INVERTIBLE]),
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE,
                 Energy.INVERTIBLE], [Energy.GENERATIVE]),
    MonumentWall([Energy.INVERTIBLE, Energy.CONSTRUCTIVE,
                 Energy.CONSTRUCTIVE], [Energy.PRIMAL]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE], ['Any'])
])

MONUMENTS = [THE_ANFIRIEN_BEACON, THE_LIBRARY_OF_VALDUIN, THE_ERIDONIC_GATE,
             THE_NAMARILLION_FORGE, THE_FORTRESS_OF_KOLYM_THRIN, THE_SHIP_OF_TOLINTHRA]

# --------------- MONUMENTS END --------------------------

# ************ ACTION TOKENS START **************************
FORTH_FIFTH_TILES_ENERGY = EnergyActionToken([0, 0, 0, 1, 1], 1)
SECOND_THIRD_TILES_ENERGY = EnergyActionToken([0, 1, 1, 0, 0], 1)
TWO_ONE_ONE_MOVE = MoveActionToken(2, 1, 1)
TWO_TWO_ONE_MOVE = MoveActionToken(2, 2, 1)
ANY = 'ANY'

INITIAL_ACTION_TOKENS = [FORTH_FIFTH_TILES_ENERGY, SECOND_THIRD_TILES_ENERGY, TWO_ONE_ONE_MOVE, TWO_TWO_ONE_MOVE, ANY]

# --------------- ACTION TOKENS END --------------------------

