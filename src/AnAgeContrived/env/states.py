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


class States:

    def get_character_states(engine, player):
        transumter = States.get_transmuter_state(player.get_transmuter())
        return transumter

    def get_transmuter_state(transmuter):
        SIZE_OF_EMBEDDED_ARRAY = 5

        def get_state_active_tile_row(row):
            embedded_array_tile = []
            for i in range(len(row)):
                embedded_array_tile_position = [0]*SIZE_OF_EMBEDDED_ARRAY
                if(tile.top[i] == 0):
                    embedded_array_tile_position[0] = 1
                else:
                    # TODO when energies are properly implemented change to tile.top[i].value to get enum value of energy
                    energy_enum_value = tile.top[i]
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
            embedded_array_reserved_tile_top_size = [0]*SIZE_OF_EMBEDDED_ARRAY
            embedded_array_reserved_tile_bottom_size = [
                0]*SIZE_OF_EMBEDDED_ARRAY
            embedded_array_reserved_tile_top_size[tile.top_size-1] = 1
            embedded_array_reserved_tile_bottom_size[tile.bottom_size-1] = 1
            state.append(embedded_array_reserved_tile_top_size)
            state.append(embedded_array_reserved_tile_bottom_size)
        return state
