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
        if action_token == 'ANY':
            new_index = _get_random_token()
            action_token = player.transmuter.get_action_token(new_index)
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

def is_take_action_legal(player, engine, index):
    is_legal = False
    if(not engine.turn.get_turn_type() == "action"):
            return False
    if index < 0 or index > 4:
        print('index is suppose to be between [0, 4]. Current index is not valid:', index)
        return False
    action_token = player.transmuter.get_action_token(index)
    if action_token == 'ANY':
        new_index = _get_random_token()
        action_token = player.transmuter.get_action_token(new_index)
    transmuter_tile = player.transmuter.active_tiles[index] #this is TransmuterTile object
    bottom_energies = transmuter_tile.bottom #this is a list
    num_energies = len(bottom_energies) - bottom_energies.count(0)
    if action_token.type == ActionType.MOVE or action_token.type == ActionType.RECHARGE:
        if num_energies > 0:
            is_legal = True
    elif action_token.type == ActionType.RELEASE_ENERGY:
        if num_energies > 0:
            available_tiles = []
            for i in range(0, len(action_token.transmuter_tiles)):
                if action_token.transmuter_tiles[i] == 1 and ((len(player.transmuter.active_tiles[i].top) - player.transmuter.active_tiles[i].top.count(0)) > 0):
                    available_tiles.append(i)
            if len(available_tiles) > 0:
                is_legal = True
    return is_legal

def _take_move_action(action_token):
    #TODO: discuss how to implement this
    move_times = action_token.move_times
    pass

def _take_release_energy_action(player, action_token):
    available_tiles = []
    for i in range(0, len(action_token.transmuter_tiles)):
        if action_token.transmuter_tiles[i] == 1 and ((len(player.transmuter.active_tiles[i].top) - player.transmuter.active_tiles[i].top.count(0)) > 0):
            available_tiles.append(i)
    rand_num = randint(0, len(available_tiles))
    index = available_tiles[rand_num]
    transmuter_tile = player.transmuter.active_tiles[index]
    if (len(transmuter_tile.top) - transmuter_tile.top.count(0)) > 0:
        print('energies BEFORE:', player.energies_released)
        player.energies_released.append(transmuter_tile.release_top_energy())
        print('energies AFTER:', player.energies_released)
        return True

def _take_recharge_action(player):
    player.channel_marker = True

def _get_random_token():
    return randint(0,3)