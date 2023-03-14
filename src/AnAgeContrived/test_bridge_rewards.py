from .env.engine import Engine
from .env.entities.turn_state import TurnType
from .env.entities.bridge import BridgeRewardType


class TestBridgeRewards:

    def test_build_bridge_reward(self):
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
        e.play_turn('player_0', move_pos_index)

        print(e.turn.get_turn_type())
        print(e.get_legal_action_names('player_0'))
