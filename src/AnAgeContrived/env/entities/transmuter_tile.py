from env.entities.energy import EnergyTile

class TransmuterTile:
    def __init__(self, top_size, bottom_size):
        self.top = [0, 0]  # put a max of 2 energies on top
        self.bottom = [0, 0]  # put a max of 2 energies on bottom
        self.top_size = top_size
        self.bottom_size = bottom_size
        self.available_top_positions = top_size
        self.available_bottom_positions = bottom_size

    # fill the energy at the given position: position: 1 == top, position: 2 == bottom
    def fill_tile(self, energy, position):
        if position > 2 or position < 1:
            print(
                'Position is wrong. Please enter a correct position between [1, 2]')
        elif position == 1:
            if self.top_size == 0:
                return print('No tile at the top')
            elif self.top_size == 1:
                if self.top[0] != 0:
                    return print('Tile already contains energy. Cannot fill this position')
                else:
                    self.top[0] = energy
            elif self.top_size == 2:
                if self.top[0] != 0:
                    if self.top[1] != 0:
                        return print('Tile already contains energy. Cannot fill this position')
                    else:
                        self.top[1] = energy
                else:
                    self.top[0] = energy
        elif position == 2:
            if self.bottom_size == 0:
                return print('No tile at the bottom')
            elif self.bottom_size == 1:
                if self.bottom[0] != 0:
                    return print('Tile already contains energy. Cannot fill this position')
                else:
                    self.bottom[0] = energy
            elif self.bottom_size == 2:
                if self.bottom[0] != 0:
                    if self.bottom[1] != 0:
                        return print('Tile already contains energy. Cannot fill this position')
                    else:
                        self.bottom[1] = energy
                else:
                    self.bottom[0] = energy

    def empty_tile(self, player):
        for i in self.top:
            print('i is:', i, 'and condition is:', i != 0)
            if i != 0:
                index = self.top.index(i)
                energy = self.top[index]
                self.top[index] = 0
                print('Energy at the top is:', energy)
                player.exhausted_energies[energy.energy_type].append(energy)
        for i in self.bottom:
            if i != 0:
                index = self.bottom.index(i)
                energy = self.bottom[index]
                self.bottom[index] = 0
                print('Energy at the bottom is:', energy)
                player.exhausted_energies[energy.energy_type].append(energy)
        self.top = [0, 0]
        self.bottom = [0, 0]

    #TODO: check to see whether the top and bottom has actually energy in them. do not release (pop) the 0s
    def release_bottom_energy(self):
        num_zeros = self.bottom.count(0)
        if num_zeros > 0:
            index = self.bottom.index(0)
            if index == 0:
                index = 1
            elif index == 1:
                index = 0
            energy = self.bottom[index]
            self.bottom[index] = 0
        else:
            energy = self.bottom.pop()
            self.bottom.append(0)
        return energy

    def release_top_energy(self):
        num_zeros = self.top.count(0)
        if num_zeros > 0:
            index = self.top.index(0)
            if index == 0:
                index = 1
            elif index == 1:
                index = 0
            energy = self.top[index]
            self.top[index] = 0
        else:
            energy = self.top.pop()
            self.top.append(0)
        return energy

    def print_tile(self):
        tile_string = ''
        tile_string += '---------------\n'
        tile_string += '|             |\n'
        if self.top_size == 0:
            tile_string += '|             |\n'
            tile_string += '|             |\n'
            tile_string += '|             |\n'
        elif self.top_size == 1:
            tile_string += '|     ---     |\n'
            tile_string += '|    | {} |    |\n'.format(self.top[0].energy_type.name[0] if type(self.top[0]) == EnergyTile else self.top[0])
            tile_string += '|     ---     |\n'
        elif self.top_size == 2:
            tile_string += '|  ---   ---  |\n'
            tile_string += '| | {} | | {} | |\n'.format(
                self.top[0].energy_type.name[0] if type(self.top[0]) == EnergyTile else self.top[0], self.top[0].energy_type.name[0] if type(self.top[1]) == EnergyTile else self.top[0])
            tile_string += '|  ---   ---  |\n'
        tile_string += '|             |\n'
        tile_string += '|             |\n'
        if self.bottom_size == 0:
            tile_string += '|             |\n'
            tile_string += '|             |\n'
            tile_string += '|             |\n'
        elif self.bottom_size == 1:
            tile_string += '|     ---     |\n'
            tile_string += '|    | {} |    |\n'.format(self.bottom[0].energy_type.name[0] if type(self.bottom[0]) == EnergyTile else self.bottom[0])
            tile_string += '|     ---     |\n'
        elif self.bottom_size == 2:
            tile_string += '|  ---   ---  |'
            tile_string += '| | {} | | {} | |\n'.format(
                self.bottom[0].energy_type.name[0] if type(self.bottom[0]) == EnergyTile else self.bottom[0], self.bottom[0].energy_type.name[0] if type(self.bottom[0]) == EnergyTile else self.bottom[0])
            tile_string += '|  ---   ---  |\n'
        tile_string += '|             |\n'
        tile_string += '---------------\n'

        return (
            tile_string
        ).format().splitlines()