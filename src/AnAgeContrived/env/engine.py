import numpy as np


class Engine:
    def __init__():
        game = 1
        current_player = 0

    def render():
        print("Rendering")

    def reset():
        print("Resetting")

    def get_agents():
        return ["Freyith", "Ignotas", "Multanec", "Rusne"]

    def get_action_space():
        print("Getting Action Space")

    def get_observation_space_shape():
        print("Getting Action Space")
        # index=0 will be all possible states, index=1 will be value for that state, index=2 is #of players,
        return(10, 10, 4)

    # Agent is the string of the player
    def get_legal_actions(self, agent):
        print("getting legal moves")

    def play_turn(self, agent, action):
        print("playing ", action, "for ", agent)

    def get_current_agents_turn(self):
        return self.get_agents[self.current_player]

    def get_game_state(self, agent):
        return []
