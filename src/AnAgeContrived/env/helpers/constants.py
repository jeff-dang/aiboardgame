from env.action_initiater import get_actions
from env.entities.action_tokens import (
    EnergyActionToken,
    MoveActionToken,
    RechargeActionToken,
)

# ********* GAME ENGINE CONSTANTS ********************

CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne", "Aureon"]
AGENT_NAMES = ["player_0", "player_1", "player_2", "player_3", "player_4"]
NUM_MOVES: int = len(get_actions("self", "eng"))
MAX_TURNS: int = 10000
NUM_AGENTS: int = len(CHARACTER_NAMES)
STARTING_PLAYER_BRIDGES = 3

# ************ ACTION TOKENS START **************************
FORTH_FIFTH_TILES_ENERGY = EnergyActionToken([0, 0, 0, 1, 1], 1)
SECOND_THIRD_TILES_ENERGY = EnergyActionToken([0, 1, 1, 0, 0], 1)
RECHARGE = RechargeActionToken()
MOVE_TWICE = MoveActionToken(2)
ANY = "ANY"

INITIAL_ACTION_TOKENS = [
    MOVE_TWICE,
    FORTH_FIFTH_TILES_ENERGY,
    RECHARGE,
    SECOND_THIRD_TILES_ENERGY,
    ANY,
]
# --------------- ACTION TOKENS END --------------------------