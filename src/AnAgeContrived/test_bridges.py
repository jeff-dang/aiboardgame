from .env.engine import Engine
from .env.entities.turn_state import TurnType
from .env.entities.bridge import BridgeRewardType


class TestBridges:
    def test_build_bridge_anywhere(self):
        e = Engine()

        build_bridge_location_1_reward_1_index = e.get_action_index("Location 1 Reward 1")
        action_turn_index = e.get_action_index("Action Turn")

        # Manually update to bridge building turn
        e.play_turn('player_0', action_turn_index)
        e.turn.update_turn_type(TurnType.BUILD_BRIDGE_TURN)

        # Assert building bridge in location 1 with reward 1 is legal move
        legal_moves = e.get_legal_action_names('player_0')
        assert(any("Location 1 Reward 1" in s for s in legal_moves))

        # Build Bridge with reward 1, assert game accepted legal move
        turn = e.play_turn('player_0', build_bridge_location_1_reward_1_index)
        assert(turn)

        for b in e.map.player_bridges:
            if(b.location == 1):
                assert((b.reward == 1))
                assert((b.owner == "player_0"))
                assert((b.tier == 1))

            # Manually go back to bridge turn, assert cannot build in same place
        e.turn.update_turn_type(TurnType.BUILD_BRIDGE_TURN)
        legal_moves = e.get_legal_action_names('player_0')
        assert(not any("Location 1 Reward 1" in s for s in legal_moves))

        # Build bridge in location 2 with reward 2 of tier 2
        build_bridge_location_2_reward_2_index = e.get_action_index("Location 2 Reward 2")
        turn = e.play_turn('player_0', build_bridge_location_2_reward_2_index)
        assert(turn)

        for b in e.map.player_bridges:
            if(b.location == 2):
                assert((b.reward == 4))
                assert((b.owner == "player_0"))
                assert((b.tier == 2))

        assert(e.turn.get_turn_type().value == TurnType.ACTION_TURN.value)

        end_turn_index = e.get_action_index("End Turn")
        turn = e.play_turn('player_0', end_turn_index)
