from env.engine import Engine


def TestEngine():
    e = Engine()

    current_player = e.get_current_agents_turn()
    print(e.get_legal_actions(current_player))
    state = (e.get_game_state(current_player))
    e.play_turn(current_player, 1)
    print(e.get_legal_actions(current_player))
    e.play_turn(current_player, 3)
    print(e.get_legal_actions(current_player))
    e.play_turn(current_player, 0)

    e.render(current_player)
    e.play_turn(current_player, 3)
    e.render(current_player)
    state = (e.get_game_state(current_player))
    print(state[0])
    print(state[1])
    print(state[2])
    print(state[3])


TestEngine()
