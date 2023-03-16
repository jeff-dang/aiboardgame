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
from env.helpers.bridge_rewards import BridgeRewards
from env.helpers.logger import Logger


class MovePlayer:
    @staticmethod
    def move_player(engine: Engine, player: Player, location):
        # Check if bridge is crossed, get path from player location to where they want to move
        path = engine.map.get_path(player.location, location)
        bridge = engine.map.check_crossed_bridge(path)
        if (
            len(engine.map.map[location]) == 1
        ):  # Check if moving into deadend, if so let them move in any direction after moving into dead end
            player.previous_location = 0
        if len(engine.map.map[location]) == 1:
            player.previous_location = 0
            Logger.log("moved into dead end", "ACTION_LOGS")
        else:
            player.previous_location = player.location
        player.location = location
        engine.turn.can_move = False

        if bridge:
            reward_bridge = engine.map.get_player_bridge(bridge)
            Logger.log("CROSSED BRIDGE YAY", "ACTION_LOGS")
            engine.turn.temp_rewards += 1
            BridgeRewards.give_reward(engine, reward_bridge.reward)

        else:
            engine.turn.update_turn_type(TurnType.ACTION_TURN)

    @staticmethod
    def is_legal_move(player: Player, engine: Engine, next_location) -> bool:
        current_location = player.location
        map = engine.map

        if not engine.turn.get_turn_type() == TurnType.MOVE_TURN:
            return False
        if not engine.turn.can_move:
            return False
        if current_location == next_location:
            return False
        if next_location == player.previous_location:
            return False

        path = engine.map.get_path(player.location, next_location)
        bridge = engine.map.check_crossed_bridge(path)
        if bridge and not engine.map.check_bridge_exists(
            bridge
        ):  # if they cross a bridge, check if its built, if not return false
            return False

        possible_locations = copy.deepcopy(map.map[current_location])
        for p in engine.players:
            if p.character != player.character:
                if p.location in map.map[current_location]:
                    possible_locations.extend(map.map[p.location])
        possible_locations = list(dict.fromkeys(possible_locations))
        return next_location in possible_locations
