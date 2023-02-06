from env.entities.monument import Monument
from env.entities.monument_wall import MonumentWall
from env.entities.energy import Energy
from env.action_initiater import get_actions
from env.entities.map_data import Map_Areas
from env.entities.action_tokens import EnergyActionToken, MoveActionToken

CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne", "Aureon"]
AGENT_NAMES = ["player_0", "player_1", "player_2", "player_3", "player_4"]
NUM_MOVES = len(get_actions('self', 'eng'))
MAX_TURNS = 100
NUM_AGENTS = len(CHARACTER_NAMES)

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
TWO_ONE_ONE_MOVE = MoveActionToken(2, 1, 1)
TWO_TWO_ONE_MOVE = MoveActionToken(2, 2, 1)
ANY = 'ANY'

INITIAL_ACTION_TOKENS = [FORTH_FIFTH_TILES_ENERGY,
                         SECOND_THIRD_TILES_ENERGY, TWO_ONE_ONE_MOVE, TWO_TWO_ONE_MOVE, ANY]

# --------------- ACTION TOKENS END --------------------------
