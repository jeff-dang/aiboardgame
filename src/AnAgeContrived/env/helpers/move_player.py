from __future__ import annotations
# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from env.entities.player import Player
    from env.engine import Engine
    # from env.entities.energy import EnergyTile
    pass

import copy
from env.entities.turn_state import TurnType


class MovePlayer():

    @staticmethod
    def move_player(engine: Engine, player: Player, location):
        if(len(engine.map.map[location]) == 1):
            player.previous_location = 0
            print('moved into dead end')
        else:
            player.previous_location = player.location
        player.location = location
        engine.turn.can_move = False
        engine.turn.turn_type = TurnType.ACTION_TURN

    @staticmethod
    def is_legal_move(player: Player, engine: Engine, next_location) -> bool:
        current_location = player.location
        map = engine.map

        if(not engine.turn.get_turn_type() == TurnType.MOVE_TURN):
            return False
        if(not engine.turn.can_move):
            return False
        if(current_location == next_location):
            return False
        if(next_location == player.previous_location):
            return False

        possible_locations = copy.deepcopy(map.map[current_location])
        for p in engine.players:
            if(p.character != player.character):
                if(p.location in map.map[current_location]):
                    possible_locations.extend(map.map[p.location])
        possible_locations = list(dict.fromkeys(possible_locations))
        return next_location in possible_locations

    @staticmethod
    def check_cross_bridge(start, end):
        pass
