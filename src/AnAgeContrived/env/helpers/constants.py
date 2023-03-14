from env.entities.monument import Monument
from env.entities.monument_wall import MonumentWall
from env.entities.energy import Energy
from env.action_initiater import get_actions
from env.entities.map_data import Map_Areas
from env.entities.action_tokens import EnergyActionToken, MoveActionToken, RechargeActionToken

# ********* GAME ENGINE CONSTANTS ********************

CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne", "Aureon"]
AGENT_NAMES = ["player_0", "player_1", "player_2", "player_3", "player_4"]
NUM_MOVES: int = len(get_actions('self', 'eng'))
MAX_TURNS: int = 750
NUM_AGENTS: int = len(CHARACTER_NAMES)

# ************ MONUMENTS START **************************
# Monuments From The Rule Book:
MONUMENT_DICT = [
    {
        'name': 'THE ANFIRIEN BEACON',
        'location': Map_Areas.PLAINS,
        'walls': [
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                'rewarded_energy':[Energy.CONSTRUCTIVE, Energy.INVERTIBLE]
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE, Energy.GENERATIVE],
                'rewarded_energy': [Energy.PRIMAL]
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                'rewarded_energy': [Energy.GENERATIVE]
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.CONSTRUCTIVE],
                'rewarded_energy': ['Any']
            }
        ]
    },
    {
        'name': 'THE LIBRARY OF VALDUIN',
        'location': Map_Areas.PLAINS,
        'walls': [
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE],
                'rewarded_energy':[Energy.GENERATIVE, Energy.INVERTIBLE],
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                'rewarded_energy': [Energy.CONSTRUCTIVE]
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.GENERATIVE, Energy.GENERATIVE],
                'rewarded_energy': [Energy.PRIMAL]
            },
            {
                'accepted_energy_types': [Energy.INVERTIBLE, Energy.GENERATIVE],
                'rewarded_energy': ['Any']
            }
        ]
    },
    {
        'name': 'THE ERIDONIC GATE',
        'location': Map_Areas.QUARRY,
        'walls': [
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                'rewarded_energy':[Energy.CONSTRUCTIVE, Energy.GENERATIVE],
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE],
                'rewarded_energy': [Energy.INVERTIBLE]
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE],
                'rewarded_energy': [Energy.GENERATIVE]
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
                'rewarded_energy': ['Any']
            }
        ]
    },
    {
        'name': 'THE NAMARILLION FORGE',
        'location': Map_Areas.MOUNTAIN,
        'walls': [
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.GENERATIVE, Energy.GENERATIVE],
                'rewarded_energy':[Energy.INVERTIBLE, Energy.GENERATIVE],
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE],
                'rewarded_energy': [Energy.PRIMAL]
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE],
                'rewarded_energy': [Energy.CONSTRUCTIVE]
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
                'rewarded_energy': ['Any']
            }
        ]
    },
    {
        'name': 'THE FORTRESS OF KOLYM THRIN',
        'location': Map_Areas.FOREST,
        'walls': [
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.GENERATIVE],
                'rewarded_energy':[Energy.CONSTRUCTIVE, Energy.PRIMAL],
            },
            {
                'accepted_energy_types': [Energy.INVERTIBLE, Energy.INVERTIBLE, Energy.GENERATIVE],
                'rewarded_energy': [Energy.GENERATIVE]
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.INVERTIBLE],
                'rewarded_energy': ['Any'],
            },
            {
                'accepted_energy_types': [Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE, Energy.GENERATIVE],
                'rewarded_energy': [Energy.INVERTIBLE],
            },
            {
                'accepted_energy_types': [Energy.PRIMAL],
                'rewarded_energy': [],
            },
        ],
    },
    {
        'name': 'THE SHIP OF TOLINTHRA',
        'location': Map_Areas.SEA,
        'walls': [
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.GENERATIVE, Energy.INVERTIBLE],
                'rewarded_energy':[Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.INVERTIBLE],
                'rewarded_energy': [Energy.GENERATIVE]
            },
            {
                'accepted_energy_types': [Energy.INVERTIBLE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE],
                'rewarded_energy': [Energy.PRIMAL],
            },
            {
                'accepted_energy_types': [Energy.GENERATIVE, Energy.CONSTRUCTIVE],
                'rewarded_energy':  ['Any']
            },
            {
                'accepted_energy_types': [Energy.PRIMAL],
                'rewarded_energy': [],
            },
        ]
    }
]

# --------------- MONUMENTS END --------------------------

# ************ ACTION TOKENS START **************************
FORTH_FIFTH_TILES_ENERGY = EnergyActionToken([0, 0, 0, 1, 1], 1)
SECOND_THIRD_TILES_ENERGY = EnergyActionToken([0, 1, 1, 0, 0], 1)
RECHARGE = RechargeActionToken()
MOVE_TWICE = MoveActionToken(2)
ANY = 'ANY'

INITIAL_ACTION_TOKENS = [MOVE_TWICE, FORTH_FIFTH_TILES_ENERGY, RECHARGE, SECOND_THIRD_TILES_ENERGY, ANY]

# --------------- ACTION TOKENS END --------------------------


THE_ANFIRIEN_BEACON = Monument('THE ANFIRIEN BEACON', Map_Areas.PLAINS, [
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE, Energy.INVERTIBLE], [
                 Energy.CONSTRUCTIVE, Energy.INVERTIBLE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE,
                 Energy.GENERATIVE], [Energy.PRIMAL]),
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE,
                 Energy.INVERTIBLE], [Energy.GENERATIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE], ['Any'])
])
THE_LIBRARY_OF_VALDUIN = Monument('THE LIBRARY OF VALDUIN', Map_Areas.PLAINS, [
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE, Energy.CONSTRUCTIVE], [
                 Energy.GENERATIVE, Energy.INVERTIBLE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE,
                 Energy.INVERTIBLE], [Energy.CONSTRUCTIVE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.GENERATIVE,
                 Energy.GENERATIVE], [Energy.PRIMAL]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.INVERTIBLE, Energy.GENERATIVE], ['Any'])
])
THE_ERIDONIC_GATE = Monument('THE ERIDONIC GATE', Map_Areas.QUARRY, [
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE, Energy.INVERTIBLE], [
                 Energy.CONSTRUCTIVE, Energy.GENERATIVE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE,
                 Energy.GENERATIVE], [Energy.INVERTIBLE]),
    MonumentWall([Energy.GENERATIVE, Energy.CONSTRUCTIVE,
                 Energy.CONSTRUCTIVE], [Energy.GENERATIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE], ['Any'])
])
THE_NAMARILLION_FORGE = Monument('THE NAMARILLION FORGE', Map_Areas.MOUNTAIN, [
    MonumentWall([Energy.CONSTRUCTIVE, Energy.GENERATIVE, Energy.GENERATIVE], [
                 Energy.INVERTIBLE, Energy.GENERATIVE]),
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE,
                 Energy.GENERATIVE], [Energy.PRIMAL]),
    MonumentWall([Energy.GENERATIVE, Energy.INVERTIBLE,
                 Energy.INVERTIBLE], [Energy.CONSTRUCTIVE]),
    # TODO: Need a mechanism to handle any energy reward
    MonumentWall([Energy.CONSTRUCTIVE, Energy.INVERTIBLE], ['Any'])
])
THE_FORTRESS_OF_KOLYM_THRIN = Monument('THE FORTRESS OF KOLYM THRIN', Map_Areas.FOREST, [
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
THE_SHIP_OF_TOLINTHRA = Monument('THE SHIP OF TOLINTHRA', Map_Areas.SEA, [
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
