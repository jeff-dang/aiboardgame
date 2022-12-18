import numpy as np
from actions.convey import Convey
from actions.turn import Turn
from functools import partial
from entities import Player

CHARACTER_NAMES = ["Freyith", "Ignotas", "Multanec", "Rusne"]


class Engine:
    def __init__():
        game = 1
        current_player = 0
        player_turn_queue = []
        players = []
        for name in CHARACTER_NAMES:
            players.append(Player(name))

    def render():
        print("Rendering")

    def reset():
        print("Resetting")

    def get_agents():
        return CHARACTER_NAMES

    def get_agent(self, name):
        for player in self.players:
            if player.get_player_name() == name:
                return player

    # Gets number of total actions
    def get_action_space():
        return 3

    def get_observation_space_shape():
        print("Getting Action Space")
        # index=0 will be all possible states, index=1 will be value for that state, index=2 is #of players,
        return(10, 10, 4)

    # Agent is the string of the player
    def get_legal_actions(self, agent):
        print("getting legal moves")

    def play_turn(self, agent_name, action):
        print("playing ", action, "for ", agent)
        agent = self.get_agent(agent_name)

        switch = {
            0: Turn.endTurn(self),
            1: partial(Convey.convey,  agent.get_transmuter(), 1, 0),
            2: Convey.convey(agent.get_transmuter(), 2, 0),
            3: Convey.convey(agent.get_transmuter(), 2, 1)
        }

    def get_current_agents_turn(self):
        return self.get_agents[self.current_player]

    def get_game_state(self, agent):
        return []
