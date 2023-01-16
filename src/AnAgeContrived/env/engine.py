from functools import partial

from .helpers.convey import Convey
from .helpers.turn import Turn

from .entities.turnState import TurnState
from .entities.player import Player
from env.entities.monument import Monument
from env.entities.monumentTile import MonumentTile
from .actionInitiater import get_actions


CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne"]
AGENT_NAMES = ["player_0", "player_1", "player_2", "player_3"]

NUM_MOVES = len(get_actions('self', 'eng')) #TODO: may fail but should make this number automatic perhaps inside the engine class

class Engine:
    def __init__(self):
        self.turnCounter = 0
        self.actionCounter = 0
        self.game = 1
        self.current_player = 0
        self.player_turn_queue = []
        self.players = []
        self.turn = TurnState()
        self.monuments = [
                            Monument('1', [MonumentTile([1, 2, 3], 'None'), MonumentTile([3, 2, 3], 'None'), MonumentTile([2, 2, 3], 'None'), MonumentTile([1, 3, 3], 'None')]), 
                            Monument('2', [MonumentTile([1, 2, 3], 'None'), MonumentTile([3, 2, 3], 'None'), MonumentTile([2, 2, 3], 'None'), MonumentTile([1, 3, 3], 'None')]), 
                            Monument('3', [MonumentTile([1, 2, 3], 'None'), MonumentTile([3, 2, 3], 'None'), MonumentTile([2, 2, 3], 'None'), MonumentTile([1, 3, 3], 'None')]), 
                            Monument('4', [MonumentTile([1, 2, 3], 'None'), MonumentTile([3, 2, 3], 'None'), MonumentTile([2, 2, 3], 'None'), MonumentTile([1, 3, 3], 'None')]), 
                            Monument('5', [MonumentTile([1, 2, 3], 'None'), MonumentTile([3, 2, 3], 'None'), MonumentTile([2, 2, 3], 'None'), MonumentTile([1, 3, 3], 'None')]), 
                            Monument('6', [MonumentTile([1, 2, 3], 'None'), MonumentTile([3, 2, 3], 'None'), MonumentTile([2, 2, 3], 'None'), MonumentTile([1, 3, 3], 'None')]) 
                         ]
        for i in range(4):
            self.players.append(Player(AGENT_NAMES[i], CHARACTER_NAMES[i]))

    def check_over(self):
        return self.turnCounter == 4*5

    def reset(self):
        self.turnCounter = 0
        self.actionCounter = 0
        self.game = 1
        self.current_player = 0
        self.player_turn_queue = []
        self.players = []
        self.turn = TurnState()
        for i in range(4):
            self.players.append(Player(AGENT_NAMES[i], CHARACTER_NAMES[i]))

    def get_agents(self):
        return AGENT_NAMES

    def get_characters(self):
        return CHARACTER_NAMES

    def get_agent(self, name):
        for player in self.players:
            if player.get_player_name() == name:
                return player

    # Gets number of total actions
    def get_action_space(self):
        return NUM_MOVES

    def get_observation_space_shape(self):
        # index=0 will be all possible states, index=1 will be value for that state, index=2 is #of players,
        return(7, 4, 1)

    def get_legal_actions(self, agent_name):
        # legal_actions = {
        #     0: Turn.endTurnLegal(self),
        #     1: Turn.conveyTurnLegal(self),
        #     2: Turn.actionTurnLegal(self),
        #     3: Convey.convey1Legal(self),
        #     4: Convey.convey2Legal(self),
        #     5: Convey.convey2Legal(self),
        # }
        # return list(legal_actions.values())
        actions = get_actions(self.players[self.current_player], self)
        legal_actions = []
        for action in actions:
            isLegal = action.check()
            legal_actions.append(isLegal)
        return legal_actions

    def play_turn(self, agent_name, action):
        agent = self.get_agent(agent_name)

        if(not self.get_legal_actions(self.current_player)[action]):
            print("ILLEGAL MOVE")
            return

        actions = get_actions(self.players[self.current_player], self)
        actions[action].execute()
        self.actionCounter += 1
        # switch = {
        #     0: partial(Turn.endTurn, engine=self),
        #     1: partial(Turn.conveyTurn, engine=self),
        #     2: partial(Turn.actionTurn, engine=self),
        #     3: partial(Convey.convey, engine=self, transmuter=agent.get_transmuter(), stepSize=1, order=0),
        #     4: partial(Convey.convey, engine=self, transmuter=agent.get_transmuter(), stepSize=2, order=0),
        #     5: partial(Convey.convey, engine=self, transmuter=agent.get_transmuter(), stepSize=2, order=1),
        # }
        # switch[action]()

    def get_current_agents_turn(self):
        return self.get_agents()[self.current_player]

    def get_current_characters_turn(self):
        return CHARACTER_NAMES[self.current_player]

    def get_game_state_others(self, agent_name):
        others_game_state = []
        for agent in AGENT_NAMES:
            if(agent != agent_name):
                others_game_state.append(self.get_game_state(agent_name))
        return others_game_state

    def get_game_state(self, agent_name):
        return self.get_agent(agent_name).get_transmuter().getState()

    def get_reward(self, agent_name):
        return self.get_agent(agent_name).get_transmuter().getTotalEmptyCells() * 10

    def get_winner(self):
        max = 0
        winner = ""
        for agent in AGENT_NAMES:
            if self.get_agent(agent).get_transmuter().getTotalEmptyCells() > max:
                winner = agent
        return winner

    def render(self, agent_name):
        agent = self.get_agent(agent_name)
        print(agent.character)
        agent.get_transmuter().printTransmuter()
        self.turn.printTurnState()
