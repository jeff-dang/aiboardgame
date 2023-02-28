import gymnasium
import numpy as np
from gymnasium import spaces
from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers
from .engine import Engine
import history_writer
from env.action_initiater import get_actions


def env(render_mode=None):
    internal_render_mode = render_mode if render_mode != "ansi" else "human"
    env = raw_env(render_mode=internal_render_mode)
    if render_mode == "ansi":
        env = wrappers.CaptureStdoutWrapper(env)
    env = wrappers.TerminateIllegalWrapper(env, illegal_reward=-1)
    env = wrappers.AssertOutOfBoundsWrapper(env)
    env = wrappers.OrderEnforcingWrapper(env)
    return env


class raw_env(AECEnv):
    metadata = {
        "render_modes": ["human"],
        "name": "an_age_contrived_v0",
        "is_parallelizable": False,
        "render_fps": 1,
    }

    def __init__(self, render_mode=None):
        super().__init__()
        self.output_json = True
        self.engine = Engine()
        self.agents = self.engine.get_agents()
        self.possible_agents = self.agents[:]
        self.action_spaces = {i: spaces.Discrete(self.engine.get_action_space())
                              for i in self.agents}

        game_state_shape = np.shape(np.array(self.engine.get_game_state()))
        self.observation_spaces = {
            i: spaces.Dict(
                {
                    "observation": spaces.Box(
                        low=0, high=1, shape=game_state_shape, dtype=np.bool8
                    ),
                    "action_mask": spaces.Box(low=0, high=1, shape=(self.engine.get_action_space(),), dtype=np.bool8),
                }
            )
            for i in self.agents
        }
        self.rewards = {i: 0 for i in self.agents}
        self._cumulative_rewards = {i: 0 for i in self.agents}
        self.terminations = {i: False for i in self.agents}
        self.truncations = {i: False for i in self.agents}
        self.infos = {i: {} for i in self.agents}
        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.reset()
        self.render_mode = render_mode

        self.simulation_history = {}
        self.json_name = history_writer.jsonNamer('ai_history')
        folder_path = history_writer.jsonDirectory('ai_history')
        history_writer.jsonWriter(folder_path, self.json_name)

    def observe(self, agent):

        # Get Action Space Vector and check legal moves
        action_mask = np.array(
            self.engine.get_legal_actions(agent), dtype="int8")

        observation = np.array(self.engine.get_game_state())

        observation = np.stack(
            observation, axis=1).astype(np.int8)
        return {"observation": observation, "action_mask": action_mask}

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]

    def _legal_moves(self, agent):
        return self.engine.get_legal_actions(agent)

    def step(self, action):

        print('env.py - @@@@@@@@@@@@@@@@@@@@ START STEP FUNCTION @@@@@@@@@@@@@@@@@@@@@@@@@')

        # Check if terminations or truncations for current agent
        if (
            self.terminations[self.agent_selection]
            or self.truncations[self.agent_selection]
        ):
            return self._was_dead_step(action)

        # Check if action is a legal move
        # Get index of current agent self.agents.index(self.agent_selection)
        # Get name of current agent self.agent_selection

        # Play turn, pass in agent name, add some extra details
        actions = get_actions(self.engine.current_player, self.engine)

        action_mask = self.engine.get_legal_actions(self.agent_selection)

        action_details = []
        a_list = self.engine.get_action_names()
        j = 0
        for i in a_list:
            action_s = 'is_legal: ' + str(action_mask[j]) + ' ' + str(i['index']) + ' ' + i['action'] + ' ' + i['action_details']
            action_details.append(action_s)
            j += 1

        legal_actions = self.engine.get_legal_action_names(
            self.agent_selection)
        # print('DATA BEOFRE JSON starts')
        # print("player", self.engine.current_player)
        # print("turn_num", self.engine.turn_counter)       
        current_monument = self.engine.monuments[self.engine.monument_index]
        # print('remaining sections:', current_monument.get_top_wall().remaining_sections, 'filled energies:', current_monument.get_top_wall().filled_sections, 'num of empty spaces:', current_monument.get_top_wall().empty_sections)
        # print('current monument is:', current_monument.name, 'monument wall starting accepted:', current_monument.get_top_wall().sections)    
        # print('LEGAL ACTIONS ARE:', legal_actions)
        # print('ACTION MASK is:', action_mask)
        # print('DATA BEOFRE JSON ends')

        turn_entry = {
            "player": self.engine.current_player,
            "turn_num": self.engine.turn_counter,
            "turn_type": str(self.engine.turn.turn_type),
            "action": actions[action.item(0)].action,
            "action_details": actions[action.item(0)].action_details,
            "current_score": self.rewards[self.agent_selection],
            "legal_actions": legal_actions,
            "player_transmuter_energies": str(self.engine.players[self.engine.current_player].transmuter.print_energies()),
            "player_exhausted_energies": str(self.engine.players[self.engine.current_player].exhausted_energies),
            "player_released_energies": str(self.engine.players[self.engine.current_player].energies_released),
            "monuments": str(self.engine.monuments),
            "current_wall_name": current_monument.name,
            "c_w_accepted_energies": str(current_monument.get_top_wall().sections),
            "c_w_remaining_sections": str(current_monument.get_top_wall().remaining_sections),
            "c_w_remaining_section_num": str(current_monument.get_top_wall().empty_sections),
            "c_w_filled_sections": str(current_monument.get_top_wall().filled_sections),
            # "all_actions": action_details
            "action_mask": action_mask
        }

        self.simulation_history[str(self.engine.action_counter
                                    )] = turn_entry
        
        # print('DATA AFTER JSON starts')
        # print("player", self.engine.current_player)
        # print("turn_num", self.engine.turn_counter)       
        # current_monument = self.engine.monuments[self.engine.monument_index]
        # print('remaining sections:', current_monument.get_top_wall().remaining_sections, 'filled energies:', current_monument.get_top_wall().filled_sections, 'num of empty spaces:', current_monument.get_top_wall().empty_sections)
        # print('current monument is:', current_monument.name, 'monument wall starting accepted:', current_monument.get_top_wall().sections)    
        # print('DATA AFTER JSON ends')

        self.engine.play_turn(self.agent_selection, action)

        # Assign rewards for players, updates only not incremental
        self.rewards[self.agent_selection] += -1
        if(self.engine.check_over()):
            for agent in self.agents:
                self.rewards[agent] += (self.engine.get_reward(agent))
            # If game is over assign termination for all agents
            print(self.rewards)
            self.simulation_history['meta_data'] = self.rewards
            actionList = self.engine.get_action_names()
            history_writer.jsonActionConverter('ai_history',actionList)
            self.terminations = {i: True for i in self.agents}

        # Assign current players turn
        self.agent_selection = self.engine.get_current_agents_turn()

        # Don't know what this does
        self._cumulative_rewards[self.agent_selection] = 0
        self._accumulate_rewards()

        if self.render_mode == "human":
            self.render()

        print('env.py - @@@@@@@@@@@@@@@@@@@@ END STEP FUNCTION @@@@@@@@@@@@@@@@@@@@@@@@@')
        # print()
        # print()

    def reset(self, seed=None, return_info=False, options=None):
        # reset environment
        self.engine.reset()

        self.agents = self.possible_agents[:]
        self.rewards = {i: 0 for i in self.agents}
        self._cumulative_rewards = {i: 0 for i in self.agents}
        self.terminations = {i: False for i in self.agents}
        self.truncations = {i: False for i in self.agents}
        self.infos = {i: {} for i in self.agents}
        # selects the first agent
        self._agent_selector.reinit(self.agents)
        self._agent_selector.reset()
        self.agent_selection = self._agent_selector.reset()

        # Dump into json list
        if self.output_json and self.simulation_history != {}:
            history_writer.jsonDump(self.simulation_history, self.json_name)
        self.simulation_history = {}

    def render(self):
        if self.render_mode is None:
            gymnasium.logger.warn(
                "You are calling render method without specifying any render mode.")
            return
        self.engine.render(self.agent_selection)

    def close(self):
        pass


if __name__ == "__main__":
    from pettingzoo.test import api_test  # noqa: E402
    api_test(env(), num_cycles=1_000_000)
