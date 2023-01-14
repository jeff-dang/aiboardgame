
class FillMonument():

    @staticmethod
    def fill_monument_tile(player, engine, energy):
        if len(player.energies[energy.energy_type]) > 0:
            monumentWall = engine.monuments[0].get_top_tile()
            monumentWall.fill_section(energy)

