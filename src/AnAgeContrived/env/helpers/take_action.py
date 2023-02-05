from env.entities.action_tokens import ActionType
from random import randint

#index is the index of the transmuter tile that you want to take action on
def take_action(player, index: int):
    if index < 0 or index > 4:
        print('index is suppose to be between [0, 4]. Current index is not valid:', index)
        return False
    transmuter_tile = player.transmuter.active_tiles[index] #this is TransmuterTile object
    bottom_energies = transmuter_tile.bottom #this is a list
    num_energies = len(bottom_energies) - bottom_energies.count(0)
    if num_energies > 0:
        player.exhausted_energies.append(transmuter_tile.release_bottom_energy())
        action_token = player.transmuter.get_action_token(index)
        if action_token.type == ActionType.MOVE:
            if _take_move_action(action_token):
                print('Move action completed successfuly')
                return True
            else:
                print('Move action could NOT be completed')
                return False
        elif action_token.type == ActionType.RELEASE_ENERGY:
            if _take_release_energy_action(player, action_token):
                print('Release energy action completed successfuly')
                return True
            else:
                print('Release energy action could NOT be completed')
                return False
        elif action_token.type == ActionType.RECHARGE:
            _take_recharge_action(player)
        else:
            print('Not a valid action')
            return False
    else:
        print('No energy in the bottom tiles')
        return False


def _take_move_action(action_token):
    #TODO: discuss how to implement this
    move_times = action_token.move_times
    pass

def _take_release_energy_action(player, action_token):
    num_available_tiles = action_token.transmuter_tiles.count(1)
    index = randint(0, num_available_tiles) #TODO: find a way to ask the ai to select which index it wants to release the energy from
    transmuter_tile = player.transmuter.active_tiles[index]
    if 0 not in transmuter_tile.top: #TODO: find a way to check if there are energies in the top tiles
        player.energies_released.append(transmuter_tile.release_top_energy())
        return True
    pass

def _take_recharge_action(player):
    player.channel_marker = True