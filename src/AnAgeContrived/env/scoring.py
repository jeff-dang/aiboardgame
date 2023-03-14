from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player
    # from env.entities.energy import EnergyTile
    pass

SCORE_PER_WALL = 100
SCORE_PER_MOVEMENT = 10
SCORE_PER_TRANSMUTER_EMPTY = 10


class Scoring:

    def get_monument_score(engine: Engine, agent_name: str) -> int:
        score: int = 0
        for monument in engine.monuments:
            for wall in monument.walls:
                if(not wall.owner is None):
                    if(wall.owner.agent == agent_name):
                        score += SCORE_PER_WALL
        return score

    def get_movement_score(player: Player) -> int:
        score = abs(player.location - player.initial_location) * \
            SCORE_PER_MOVEMENT
        return score

    def get_transumter_score(player: Player) -> int:
        score = player.get_transmuter().get_total_empty_cells() * \
            SCORE_PER_TRANSMUTER_EMPTY
        return score
