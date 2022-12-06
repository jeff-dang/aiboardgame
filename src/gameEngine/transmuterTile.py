class TransmuterTile:
    def __init__(self, top_size, bottom_size):
        self.top = [0, 0] # put a max of 2 energies on top
        self.bottom =[0, 0] # put a max of 2 energies on bottom
        self.top_size = top_size
        self.bottom_size = bottom_size
        self.available_top_positions = top_size
        self.available_bottom_positions = bottom_size

    # fill the energy at the given position
    def fillTile(self, energy, position):
        pass
        
    #have getter and setter methods for available positions

    