# Author: Jeffrey Dang
# Date: November 13th, 2022
# Description: 
# Module defining the victory points of An Age Contrived game
from __future__ import annotations

# these imports will not be imported in the runtime, it is just to help coding to do type_checking
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from env.engine import Engine
    from env.entities.player import Player
    from env.entities.transmuter import Transmuter

    # from env.entities.energy import EnergyTile
    pass


# TODO Make it automatiacally change to max array length
MAX_SIZE_EMBEDDED_ARRAY = 40  # Size of the biggest entity state
from env.entities.energy import Energy


class States:
    def get_character_states(engine: Engine, player: Player):
        character_state = []
        transumter: Transmuter = States.get_transmuter_state(player.get_transmuter())
        location = States.get_map_state(player)
        monuments = States.get_monument_state(engine, player)
        bridge = States.get_bridge_state(engine, player)
        energies = States.get_energies_state(engine, player)
        character_state.extend(transumter)
        character_state.extend(location)
        character_state.extend(monuments)
        character_state.extend(bridge)
        character_state.extend(energies)

        return character_state

    def get_map_state(player: Player):
        embedded_map_state = [0] * MAX_SIZE_EMBEDDED_ARRAY
        embedded_map_state[player.location - 1] = 1

        embedded_initial_map_state = [0] * MAX_SIZE_EMBEDDED_ARRAY
        embedded_initial_map_state[player.initial_location - 1] = 1

        return [embedded_map_state, embedded_initial_map_state]

    def get_transmuter_state(transmuter: Transmuter):
        SIZE_OF_TRANSMUTER_ARRAY = 5

        def get_state_active_tile_row(row):
            embedded_array_tile = []
            for i in range(len(row)):
                embedded_array_tile_position = [0] * MAX_SIZE_EMBEDDED_ARRAY
                if row[i] == 0:
                    embedded_array_tile_position[0] = 1
                else:
                    energy_enum_value = row[i].energy_type.value
                    embedded_array_tile_position[energy_enum_value] = 1
                embedded_array_tile.append(embedded_array_tile_position)
            return embedded_array_tile

        state = []
        for i, tile in enumerate(transmuter.active_tiles):
            top = get_state_active_tile_row(tile.top)
            bottom = get_state_active_tile_row(tile.bottom)

            state.append(top[0])
            if len(top) > 1:
                state.append(top[1])
            else:
                state.append(bottom[0])
            state.append(bottom[0])
            if len(bottom) > 1:
                state.append(bottom[1])
            else:
                state.append(bottom[0])

        for i, tile in enumerate(transmuter.reserved_tiles):
            embedded_array_reserved_tile_top_size = [0] * MAX_SIZE_EMBEDDED_ARRAY
            embedded_array_reserved_tile_bottom_size = [0] * MAX_SIZE_EMBEDDED_ARRAY
            embedded_array_reserved_tile_top_size[tile.top_size - 1] = 1
            embedded_array_reserved_tile_bottom_size[tile.bottom_size - 1] = 1
            state.append(embedded_array_reserved_tile_top_size)
            state.append(embedded_array_reserved_tile_bottom_size)

        return state

    # TODO CLEAN THIS UP LOL
    def get_monument_state(engine, player):
        monument_state = []
        for i, monument in enumerate(engine.monuments):
            embedded_monument_num = [0] * MAX_SIZE_EMBEDDED_ARRAY
            embedded_monument_location = [0] * MAX_SIZE_EMBEDDED_ARRAY
            embedded_num_walls_completed = [0] * MAX_SIZE_EMBEDDED_ARRAY

            embedded_monument_num[i] = 1
            embedded_monument_location[monument.location.value] = 1
            embedded_num_walls_completed[monument.get_num_walls_completed()] = 1

            monument_state.append(embedded_monument_num)
            monument_state.append(embedded_monument_location)
            monument_state.append(embedded_num_walls_completed)

            MAX_SIZE_WALL_TILE_SPOTS = 3
            embedded_top_wall_pos_accepts = [
                [0] * MAX_SIZE_EMBEDDED_ARRAY for _ in range(MAX_SIZE_WALL_TILE_SPOTS)
            ]
            embedded_top_wall_pos_owner = [
                [0] * MAX_SIZE_EMBEDDED_ARRAY for _ in range(MAX_SIZE_WALL_TILE_SPOTS)
            ]

            # Does not have a third spot to fill, accepts none and owner is none
            if monument.get_top_wall().num_sections < 3:
                embedded_top_wall_pos_accepts[MAX_SIZE_WALL_TILE_SPOTS - 1][0] = 1
                embedded_top_wall_pos_owner[MAX_SIZE_WALL_TILE_SPOTS - 1][
                    len(engine.players)
                ] = 1

            # Assigns value based on filled sections and who owns them
            for i, pos in enumerate(monument.get_top_wall().filled_sections):
                # No player owns it assign it last index (index 5)
                if pos == 0:
                    embedded_top_wall_pos_owner[i][len(engine.players)] = 1
                else:
                    current_players_index = next(
                        (
                            index
                            for (index, d) in enumerate(engine.players)
                            if d.agent == player.agent
                        ),
                        None,
                    )

                    owner_index = next(
                        (
                            index
                            for (index, d) in enumerate(engine.players)
                            if d.agent == pos.owner.agent
                        ),
                        None,
                    )
                    distance_between = (owner_index - current_players_index) % 5
                    embedded_top_wall_pos_owner[i][distance_between] = 1

            monument_state.extend(embedded_top_wall_pos_owner)
            # Assigns value based on remaining sections and their accepting energy
            for i, pos in enumerate(monument.get_top_wall().remaining_sections):
                if pos is None:
                    embedded_top_wall_pos_accepts[i][0] = 1
                else:
                    embedded_top_wall_pos_accepts[i][pos.value] = 1

            monument_state.extend(embedded_top_wall_pos_accepts)

            MAX_SIZE_WALLS_PER_MONUMENT = 5  # Most have 4, one has 5
            embedded_top_wall_owner = [
                [0] * MAX_SIZE_EMBEDDED_ARRAY
                for _ in range(MAX_SIZE_WALLS_PER_MONUMENT)
            ]

            if len(monument.walls) < 5:
                embedded_top_wall_owner[MAX_SIZE_WALLS_PER_MONUMENT - 1][
                    len(engine.players)
                ] = 1

            embedded_wall_rewards = [
                [0] * MAX_SIZE_EMBEDDED_ARRAY
                for _ in range(MAX_SIZE_WALLS_PER_MONUMENT * 2)
            ]

            # If only 4 walls then last two are empty
            MAX_REWARD_SIZE = 5
            if len(monument.walls) < 5:
                embedded_wall_rewards[MAX_SIZE_WALLS_PER_MONUMENT * 2 - 1][
                    MAX_REWARD_SIZE
                ] = 1
                embedded_wall_rewards[MAX_SIZE_WALLS_PER_MONUMENT * 2 - 2][
                    MAX_REWARD_SIZE
                ] = 1

            for j, wall in enumerate(monument.walls):
                if wall.owner is None:
                    embedded_top_wall_owner[j][len(engine.players)] = 1
                else:
                    current_players_index = next(
                        (
                            index
                            for (index, d) in enumerate(engine.players)
                            if d.agent == player.agent
                        ),
                        None,
                    )

                    owner_index = next(
                        (
                            index
                            for (index, d) in enumerate(engine.players)
                            if d.agent == wall.owner.agent
                        ),
                        None,
                    )
                    distance_between = (owner_index - current_players_index) % 5
                    embedded_top_wall_owner[j][distance_between] = 1

                for k, reward in enumerate(wall.rewarded_energy):
                    if reward == "Any":
                        ANY_INDEX = 0
                        embedded_wall_rewards[j * 2 + k][ANY_INDEX] = 1
                    else:
                        embedded_wall_rewards[j * 2 + k][reward.value] = 1

                    if len(wall.rewarded_energy) < 2:
                        embedded_wall_rewards[j * 2 + 1][MAX_REWARD_SIZE] = 1

            monument_state.extend(embedded_top_wall_owner)
            monument_state.extend(embedded_wall_rewards)
        return monument_state

    def get_bridge_state(engine, player):
        # Check if bridge is built and by who 10 arrays of size 6, 0,1,2,3,4 player index and 5 is not built
        num_players = len(engine.players)
        embedded_bridge_array = []
        for i in engine.map.bridge_locations:
            embedded_bridge_owner_array = [0] * MAX_SIZE_EMBEDDED_ARRAY

            if engine.map.check_bridge_exists(i):
                player_bridge = engine.map.get_player_bridge(i)
                current_players_index = next(
                    (
                        index
                        for (index, d) in enumerate(engine.players)
                        if d.agent == player.agent
                    ),
                    None,
                )

                owner_index = next(
                    (
                        index
                        for (index, d) in enumerate(engine.players)
                        if d.agent == player_bridge.owner
                    ),
                    None,
                )
                distance_between = (owner_index - current_players_index) % 5
                embedded_bridge_owner_array[distance_between] = 1
            else:
                embedded_bridge_owner_array[num_players] = 1
            embedded_bridge_array.append(embedded_bridge_owner_array)

        # Another 10 arrays with size 7, 0-5 for rewards 6 for no bridge for reward
        embedded_bridge_all_rewards = []
        MAX_REWARD_VALUE = 6
        for i in engine.map.bridge_locations:
            embedded_bridge_reward = [0] * (MAX_SIZE_EMBEDDED_ARRAY)

            if engine.map.check_bridge_exists(i):
                player_bridge = engine.map.get_player_bridge(i)
                reward_value = player_bridge.reward.value
                embedded_bridge_reward[reward_value] = 1
            else:
                embedded_bridge_reward[MAX_REWARD_VALUE] = 1
            embedded_bridge_all_rewards.append(embedded_bridge_reward)

        state = []
        state.extend(embedded_bridge_array)
        state.extend(embedded_bridge_all_rewards)
        return state

    def get_energies_state(engine, player):
        embedded_exhausted_energies = [0]*MAX_SIZE_EMBEDDED_ARRAY
        embedded_energies_released = [0]*MAX_SIZE_EMBEDDED_ARRAY
        embedded_remaining_energies = [0]*MAX_SIZE_EMBEDDED_ARRAY

        
        num_exausted_energies = len(player.exhausted_energies[Energy.SINGLE])
        num_energies_released = len(player.energies_released[Energy.SINGLE])
        num_remaining_energies = len(player.remaining_energies[Energy.SINGLE])

        embedded_exhausted_energies[num_exausted_energies] = 1
        embedded_energies_released[num_energies_released] = 1
        embedded_remaining_energies[num_remaining_energies] = 1

        state = []
        state.append(embedded_exhausted_energies)
        state.append(embedded_energies_released)
        state.append(embedded_remaining_energies)

        return state