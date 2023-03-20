from env.action_initiater import get_actions
from env.entities.action_tokens import (
    EnergyActionToken,
    MoveActionToken,
    RechargeActionToken,
    FillTransformativeActionToken,
    FillSentinentActionToken
)
from env.entities.pillars_of_civilization import PillarsOfCivilization
from env.entities.map_data import MapAreas

# ********* GAME ENGINE CONSTANTS ********************

CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne", "Aureon"]
AGENT_NAMES = ["player_0", "player_1", "player_2", "player_3", "player_4"]
NUM_MOVES: int = len(get_actions("self", "eng"))
MAX_TURNS: int = 3000
NUM_AGENTS: int = len(CHARACTER_NAMES)
STARTING_PLAYER_BRIDGES = 3
# --------------- GAME ENGINE CONSTANTS END --------------------------

# ************ ACTION TOKENS START **************************
FORTH_FIFTH_TILES_ENERGY = EnergyActionToken([0, 0, 0, 1, 1], 1)
SECOND_THIRD_TILES_ENERGY = EnergyActionToken([0, 1, 1, 0, 0], 1)
RECHARGE = RechargeActionToken()
MOVE_TWICE = MoveActionToken(2)
TRANSFORMATIVE = FillTransformativeActionToken()
SENTIENT = FillSentinentActionToken()
ANY = "ANY"

INITIAL_ACTION_TOKENS = [
    MOVE_TWICE,
    TRANSFORMATIVE,
    SENTIENT,
    FORTH_FIFTH_TILES_ENERGY,
    RECHARGE,
    SECOND_THIRD_TILES_ENERGY,
    ANY,
]
# --------------- ACTION TOKENS END --------------------------

# ************ PILLARS OF CIVILIZATION START **************************
ECONOMICS = PillarsOfCivilization("ECONOMICS", MapAreas.PLAINS)
ENGINEERING = PillarsOfCivilization("ENGINEERING", MapAreas.QUARRY)
INSTITUTIONS = PillarsOfCivilization("INSTITUTIONS", MapAreas.SEA)
LITERATURE = PillarsOfCivilization("LITERATURE", MapAreas.MOUNTAIN)
MATHEMATICS = PillarsOfCivilization("MATHEMATICS", MapAreas.FOREST)
PHILOSOPHY = PillarsOfCivilization("PHILOSOPHY", MapAreas.SWAMP)

PILLARS_OF_CIVILIZATION = [ECONOMICS, ENGINEERING, INSTITUTIONS, LITERATURE, MATHEMATICS, PHILOSOPHY]
# --------------- ACTION TOKENS END --------------------------