import copy


class MovePlayer():

    @staticmethod
    def move_player(engine, player, location):
        if(len(engine.map.map[location]) == 1):
            player.previous_location = 0
            print('moved into dead end')
        else:
            player.previous_location = player.location
        player.location = location
        engine.turn.can_move = False

    @staticmethod
    def is_legal_move(player, engine, next_location):
        current_location = player.location
        map = engine.map

        if(not engine.turn.get_turn_type() == "action"):
            return False
        if(not engine.turn.can_move):
            return False
        if(current_location == next_location):
            return False
        if(next_location == player.previous_location):
            return False

        possible_locations = copy.deepcopy(map.map[current_location])
        for p in engine.players:
            if(p.character != player.character):
                if(p.location in map.map[current_location]):
                    possible_locations.extend(map.map[p.location])
        possible_locations = list(dict.fromkeys(possible_locations))
        return next_location in possible_locations

    @staticmethod
    def check_cross_bridge(start, end):
        pass
