from .env.engine import Engine
from .env.states import States

class TestEnergy:
    def test_build_bridge_anywhere(self):
        e = Engine()

        player0 = e.players[0]

        state = (States.get_energies_state(e, player0))
        
