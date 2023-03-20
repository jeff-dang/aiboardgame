from ..env.engine import Engine
from ..env.entities.turn_state import TurnType
from ..env.entities.bridge import BridgeRewardType


class TestMovement:
    def test_normal_movement(self):
        position = 27
        e = Engine()
        e.players[0].location = 26
        move_pos_index = e.get_action_index("Position "+str(position))
        action_turn_index = e.get_action_index("Action Turn")
        move_turn_index = e.get_action_index("First Transmuter's Action Token")  # Movement Action Turn

        e.get_legal_action_names('player_0')
        e.play_turn('player_0', action_turn_index)

        # Assert Move Turn is triggered
        e.play_turn('player_0', move_turn_index)
        assert(e.turn.turn_type.value == TurnType.MOVE_TURN.value)

        # Assert moving to position 27 is legal
        legal_moves = e.get_legal_action_names('player_0')
        assert(any("Position "+str(position) in s for s in legal_moves))

        # Assert turn was accepted by the engine
        assert(e.play_turn('player_0', move_pos_index))

        # Assert player was moved to correct location
        assert(e.players[0].location == position)

    def test_player_jump_movement(self):
        position = 32
        e = Engine()
        e.players[0].location = 1
        e.players[1].location = 2

        move_pos_index = e.get_action_index("Position "+str(position))
        action_turn_index = e.get_action_index("Action Turn")
        move_turn_index = e.get_action_index("First Transmuter's Action Token")  # Movement Action Turn

        e.get_legal_action_names('player_0')
        e.play_turn('player_0', action_turn_index)

        # Assert Move Turn is triggered
        e.play_turn('player_0', move_turn_index)
        assert(e.turn.turn_type.value == TurnType.MOVE_TURN.value)

        # Assert moving to position 29 is legal
        legal_moves = e.get_legal_action_names('player_0')
        assert(any("Position "+str(position) in s for s in legal_moves))

        # Assert turn was accepted by the engine
        assert(e.play_turn('player_0', move_pos_index))

        # Assert player was moved to correct location
        assert(e.players[0].location == position)

    def test_player_normal_movement_over_built_bridge(self):
        position = 37
        e = Engine()
        e.map.build_bridge(e.players[0], BridgeRewardType.BUILD_BRIDGE, 3)
        e.players[0].location = 11

        move_pos_index = e.get_action_index("Position "+str(position))
        action_turn_index = e.get_action_index("Action Turn")
        move_turn_index = e.get_action_index("First Transmuter's Action Token")  # Movement Action Turn

        e.get_legal_action_names('player_0')
        e.play_turn('player_0', action_turn_index)

        # Assert Move Turn is triggered
        e.play_turn('player_0', move_turn_index)
        assert(e.turn.turn_type.value == TurnType.MOVE_TURN.value)

        # Assert bridge being crossed was bridge 3
        path = (e.map.get_path(e.players[0].location, position))
        bridge = e.map.check_crossed_bridge(path)
        assert(bridge == 3)

        # Assert moving to position 29 is legal
        legal_moves = e.get_legal_action_names('player_0')
        assert(any("Position "+str(position) in s for s in legal_moves))

        # Assert turn was accepted by the engine
        assert(e.play_turn('player_0', move_pos_index))

        # Assert player was moved to correct location
        assert(e.players[0].location == position)

    def test_player_normal_movement_over_unbuilt_bridge(self):
        start_position = 12
        end_position = 13
        e = Engine()
        e.map.build_bridge(e.players[0], BridgeRewardType.BUILD_BRIDGE, 3)
        e.players[0].location = start_position

        move_pos_index = e.get_action_index("Position "+str(end_position))
        action_turn_index = e.get_action_index("Action Turn")
        move_turn_index = e.get_action_index("First Transmuter's Action Token")  # Movement Action Turn

        e.get_legal_action_names('player_0')
        e.play_turn('player_0', action_turn_index)

        # Assert Move Turn is triggered
        e.play_turn('player_0', move_turn_index)
        assert(e.turn.turn_type.value == TurnType.MOVE_TURN.value)

        # Assert moving to position 13 is illegal
        legal_moves = e.get_legal_action_names('player_0')
        assert(not any("Position "+str(end_position) in s for s in legal_moves))

        # Assert rejected was accepted by the engine
        assert(not e.play_turn('player_0', move_pos_index))

        # Assert player was in same position
        assert(e.players[0].location == start_position)

    def test_player_jump_movement_over_built_bridge(self):
        position = 13
        e = Engine()
        e.map.build_bridge(e.players[0], BridgeRewardType.BUILD_BRIDGE, 4)
        e.players[0].location = 10
        e.players[1].location = 12

        move_pos_index = e.get_action_index("Position "+str(position))
        action_turn_index = e.get_action_index("Action Turn")
        move_turn_index = e.get_action_index("First Transmuter's Action Token")  # Movement Action Turn

        e.get_legal_action_names('player_0')
        e.play_turn('player_0', action_turn_index)

        # Assert Move Turn is triggered
        e.play_turn('player_0', move_turn_index)
        assert(e.turn.turn_type.value == TurnType.MOVE_TURN.value)

        # Assert bridge being crossed was bridge 3
        path = (e.map.get_path(e.players[0].location, position))
        bridge = e.map.check_crossed_bridge(path)
        assert(bridge == 4)

        # Assert moving to position 29 is legal
        legal_moves = e.get_legal_action_names('player_0')
        assert(any("Position "+str(position) in s for s in legal_moves))

        # Assert turn was accepted by the engine
        assert(e.play_turn('player_0', move_pos_index))

        # Assert player was moved to correct location
        assert(e.players[0].location == position)

    def test_player_jump_movement_over_unbuilt_bridge(self):
        start_position = 10
        end_position = 13
        e = Engine()
        e.players[0].location = start_position
        e.players[1].location = 12

        move_pos_index = e.get_action_index("Position "+str(end_position))
        action_turn_index = e.get_action_index("Action Turn")
        move_turn_index = e.get_action_index("First Transmuter's Action Token")  # Movement Action Turn

        e.get_legal_action_names('player_0')
        e.play_turn('player_0', action_turn_index)

        # Assert Move Turn is triggered
        e.play_turn('player_0', move_turn_index)
        assert(e.turn.turn_type.value == TurnType.MOVE_TURN.value)

        # Assert moving to position 13 is illegal
        legal_moves = e.get_legal_action_names('player_0')
        assert(not any("Position "+str(end_position) in s for s in legal_moves))

        # Assert rejected was accepted by the engine
        assert(not e.play_turn('player_0', move_pos_index))

        # Assert player was in same position
        assert(e.players[0].location == start_position)
