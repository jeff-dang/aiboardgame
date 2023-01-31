from .entities.energy import Energy

test_state_initial_transmuter = [[0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0],
                                 [0, 1],
                                 [1, 0],
                                 [0, 1],
                                 [1, 0], ]

test_state_empty_transmuter = [[1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 1],
                               [1, 0],
                               [0, 1],
                               [1, 0], ]

# TODO Make it automatiacally change to max array length
MAX_SIZE_EMBEDDED_ARRAY = 40


class States:

    def get_character_states(engine, player):
        character_state = []
        transumter = States.get_transmuter_state(player.get_transmuter())
        location = States.get_map_state(player)
        character_state.extend(transumter)
        character_state.extend(location)
        return character_state

    def get_map_state(player):
        embedded_map_state = [0]*MAX_SIZE_EMBEDDED_ARRAY
        embedded_map_state[player.location-1] = 1

        embedded_initial_map_state = [0]*MAX_SIZE_EMBEDDED_ARRAY
        embedded_initial_map_state[player.initial_location-1] = 1

        return [embedded_map_state, embedded_initial_map_state]

    def get_transmuter_state(transmuter):
        SIZE_OF_TRANSMUTER_ARRAY = 5

        def get_state_active_tile_row(row):
            embedded_array_tile = []
            for i in range(len(row)):
                embedded_array_tile_position = [0]*MAX_SIZE_EMBEDDED_ARRAY
                if(row[i] == 0):
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

            state.append(top[1])

            state.append(bottom[0])

            state.append(bottom[1])

        for i, tile in enumerate(transmuter.reserved_tiles):
            embedded_array_reserved_tile_top_size = [0]*MAX_SIZE_EMBEDDED_ARRAY
            embedded_array_reserved_tile_bottom_size = [
                0]*MAX_SIZE_EMBEDDED_ARRAY
            embedded_array_reserved_tile_top_size[tile.top_size-1] = 1
            embedded_array_reserved_tile_bottom_size[tile.bottom_size-1] = 1
            state.append(embedded_array_reserved_tile_top_size)
            state.append(embedded_array_reserved_tile_bottom_size)
        return state
