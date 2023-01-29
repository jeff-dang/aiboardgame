from .entities.turn_state import TurnState
from .entities.player import Player
from .action_initiater import get_actions
import env.helpers.constants as constants


class Engine:
    def __init__(self):
        self.turn_counter = 0
        self.action_counter = 0
        self.game = 1
        self.current_player = 0
        self.player_turn_queue = []
        self.players = []
        self.turn = TurnState()
        self.monument_index = 0
        self.monuments = constants.MONUMENTS
        for i in range(len(constants.CHARACTER_NAMES)):
            self.players.append(Player(constants.AGENT_NAMES[i], constants.CHARACTER_NAMES[i]))


    def check_over(self):
        if self._check_if_current_wall_filled():
            if self.monument_index < 5:
                self.monument_index += 1
        if self._check_if_last_wall_filled():
            print("MONUMENTS ALL BUILT")
            return True
        if(self.turn_counter == MAX_TURNS):
            print("MAX MOVES REACHED")
            return True
        return False

    def reset(self):
        self.__init__()

    def get_agents(self):
        return constants.AGENT_NAMES

    def get_characters(self):
        return constants.CHARACTER_NAMES

    def get_agent(self, name):
        for player in self.players:
            if player.get_player_name() == name:
                return player

    # Gets number of total actions
    def get_action_space(self):
        return constants.NUM_MOVES

    def get_legal_actions(self, agent_name):
        actions = get_actions(self.get_agent(agent_name), self)
        legal_actions = []
        for action in actions:
            isLegal = action.check()
            legal_actions.append(isLegal)
        return legal_actions

    def play_turn(self, agent_name, action):
        agent = self.get_agent(agent_name)
        print(self.get_legal_actions(self.current_player))

        if(not self.get_legal_actions(self.current_player)[action]):
            print("ILLEGAL MOVE, is", action)
            return

        actions = get_actions(self.players[self.current_player], self)
        actions[action].execute()

        # check whether the monument wall is filled and either:
        # 1: start a mini turn for players who have energy tiles on the wall or
        # 2: end the game if all the walls of all the monuments are filled
        # for monument in self.monuments: #TODO: Later convert to this condition
        self.num_of_built_monuments = 0

        for i in range(0, 6):
            monument = self.monuments[i]
            if monument.is_top_wall_completed():
                filled_wall = monument.get_top_wall()
                # if the current top wall is completed, change the top wall to next wall
                monument.change_top_wall()
                # TODO: start mini turn here, use filled_wall to get the energy and the owner's of the energy to know which players will be part of the mini turn
            if monument.is_completed() and self.monument_index < 5:
                self.monument_index += 1
                self.num_of_built_monuments += 1

        print('Current wall is:',
              self.monuments[self.monument_index].name, 'index is:', self.monument_index)
        monument = self.monuments[self.monument_index]
        if monument.is_top_wall_completed():
            filled_wall = monument.get_top_wall()
            # if the current top wall is completed, change the top wall to next wall
            monument.change_top_wall()
            # TODO: start mini turn here, use filled_wall to get the energy and the owner's of the energy to know which players will be part of the mini turn
        self.action_counter += 1

    def get_current_agents_turn(self):
        return self.get_agents()[self.current_player]

    def get_current_characters_turn(self):
        return constants.CHARACTER_NAMES[self.current_player]

    def get_game_state(self):
        index_of_agent = self.current_player
        all_character_states = []
        for i in range(len(self.players)):
            index = ((i+index_of_agent) % len(self.players))
            player = (self.players[index])
            all_character_states.extend(States.get_character_states(
                self, player))
        return all_character_states

    def get_reward(self, agent_name):
        return self.get_agent(agent_name).get_transmuter().get_total_empty_cells() * 10

    def get_winner(self):
        max = 0
        winner = ""
        for agent in constants.AGENT_NAMES:
            if self.get_agent(agent).get_transmuter().get_total_empty_cells() > max:
                winner = agent
        return winner

    def render(self, agent_name):
        agent = self.get_agent(agent_name)
        print(agent.character)
        agent.get_transmuter().print_transmuter()
        # print(self.monuments[0].get_top_wall().print_wall())
        self.turn.print_turn_state()

    def _check_if_last_wall_filled(self):
        if self.monument_index == 5:
            if self.monuments[self.monument_index].is_completed():
                return True
        return False

    def _check_if_current_wall_filled(self):
        if self.monuments[self.monument_index].is_completed():
            return True
        return False
