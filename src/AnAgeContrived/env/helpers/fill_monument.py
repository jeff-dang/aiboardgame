from env.entities.monument import Monument


class FillMonument():

    # TODO: need to check the player location and get the closest monument to fill ,instead of currently just filling the monuments[0]
    @staticmethod
    def fill_monument_tile(player, engine, energy):
        if len(player.energies_on_char_board[energy.energy_type]) > 0:
            print(
                '------------- fillMonument.py - fill_monument_tile(): ----------------')
            print('player:', player.get_player_name(),
                  'Trying to fill section with energy:', energy.energy_type)
            monumentWall = engine.monuments[0].get_top_wall()
            print('Monument supports energy types:', monumentWall.sections)
            result = monumentWall.fill_section(energy)
            if result == True:
                player.energies_on_char_board[energy.energy_type].pop()
                print('Remaining sections:', monumentWall.remaining_sections)
            print('***----------------------------------------***')

    @staticmethod
    def is_legal_to_fill_monument_tile(engine):
        # TODO: if the player has no energy type, mask the action
        return not engine.monuments[0].is_completed()
