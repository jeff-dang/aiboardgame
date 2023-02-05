from env.entities.monument import Monument
from env.entities.energy import Energy


class FillMonument():

    # TODO: need to check the player location and get the closest monument to fill ,instead of currently just filling the monuments[0]
    @staticmethod
    def fill_monument_tile(player, engine, energy):
        if len(player.energies_on_char_board[energy.energy_type]) > 0:
            print(
                '------------- fillMonument.py - fill_monument_tile(): ----------------')
            print('player:', player.get_player_name(),
                  'Trying to fill section with energy:', energy.energy_type)

            monumentWall = engine.monuments[engine.monument_index].get_top_wall(
            )
            print('Monument supports energy types:', monumentWall.sections)
            result = monumentWall.fill_section(energy)
            if result == True:
                print(len(player.energies_on_char_board[energy.energy_type]))
                player.energies_on_char_board[energy.energy_type].pop()
                print(len(player.energies_on_char_board[energy.energy_type]))
                print('Remaining sections:', monumentWall.remaining_sections)
            print('***----------------------------------------***')

    def is_legal_to_fill_monument_tile(engine, energy_type):

        # Check turn is type action
        if(not engine.turn.get_turn_type() == "action"):
            return False

        # Check if current monument is completed, should never occur
        if(engine.monuments[engine.monument_index].is_completed()):
            return False

        current_player = engine.players[engine.current_player]
        current_monument = engine.monuments[engine.monument_index]

        # check if they even have that energy they want to fill
        if(len(current_player.energies_on_char_board[energy_type]) == 0):
            return False

        # check if energy they have fits on current monument
        if(not current_monument.get_top_wall().check_accept(energy_type)):
            return False

        return True
