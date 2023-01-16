from env.entities.monument import Monument

class FillMonument():

    @staticmethod
    def fill_monument_tile(player, engine, energy):
        if len(player.energies[energy.energy_type]) > 0:
            print('------------- fillMonument.py - fill_monument_tile(): ----------------')
            print('player: ', player.get_player_name() ,'Trying to fill section with energy: ', energy.energy_type)
            monumentWall = engine.monuments[0].get_top_wall()
            print('Monument supports energy types: ', monumentWall.get_acceptable_energy_types())
            monumentWall.fill_section(energy)
            print('***----------------------------------------***')

    @staticmethod
    def is_legal_to_fill_monument_tile(engine):
        return not engine.monuments[0].is_completed()