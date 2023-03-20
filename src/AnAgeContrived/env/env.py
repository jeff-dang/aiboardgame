import gymnasium
import numpy as np
from gymnasium import spaces
from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers
from .engine import Engine
import history_writer
from env.action_initiater import get_actions
from env.helpers.logger import Logger
from env.entities.energy import Energy


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
        self.action_spaces = {
            i: spaces.Discrete(self.engine.get_action_space()) for i in self.agents
        }

        game_state_shape = np.shape(np.array(self.engine.get_game_state()))
        self.observation_spaces = {
            i: spaces.Dict(
                {
                    "observation": spaces.Box(
                        low=0, high=1, shape=game_state_shape, dtype=np.bool8
                    ),
                    "action_mask": spaces.Box(
                        low=0,
                        high=1,
                        shape=(self.engine.get_action_space(),),
                        dtype=np.bool8,
                    ),
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
        self.json_name = history_writer.jsonNamer("ai_history")
        folder_path = history_writer.jsonDirectory("ai_history")
        history_writer.jsonWriter(folder_path, self.json_name)

    def observe(self, agent):
        # Get Action Space Vector and check legal moves
        action_mask = np.array(self.engine.get_legal_actions(agent), dtype="int8")

        observation = np.array(self.engine.get_game_state())
        observation = np.stack(observation, axis=1).astype(np.int8)
        return {"observation": observation, "action_mask": action_mask}

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]

    def _legal_moves(self, agent):
        return self.engine.get_legal_actions(agent)

    def step(self, action):
        Logger.log(
            "env.py - @@@@@@@@@@@@@@@@@@@@ START STEP FUNCTION @@@@@@@@@@@@@@@@@@@@@@@@@",
            "INITIALIZATION_LOGS",
        )

        # Check if terminations or truncations for current agent
        if (
            self.terminations[self.agent_selection]
            or self.truncations[self.agent_selection]
        ):
            return self._was_dead_step(action)

        turn_entry = {}

        if self.output_json:
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
                action_s = (
                    "is_legal: "
                    + str(action_mask[j])
                    + " "
                    + str(i["index"])
                    + " "
                    + i["action"]
                    + " "
                    + i["action_details"]
                )
                action_details.append(action_s)
                j += 1

            legal_actions = self.engine.get_legal_action_names(self.agent_selection)
            current_monument = self.engine.monuments[self.engine.monument_index]
            cur_monument_sections = []
            cur_monument_remaining_sections = []
            cur_monument_filled_sections = []
            for i in current_monument.walls:
                cur_monument_sections.append(i.sections)
                cur_monument_remaining_sections.append(i.remaining_sections)
                cur_monument_filled_sections.append(i.filled_sections)
            energies_on_poc = []
            te_in_poc = 0
            for i in self.engine.pillars_of_civilization:
                poc = str(i.name) + ": " + str(i.binded_energies)
                energies_on_poc.append(poc)
                te_in_poc += len(i.binded_energies) - i.binded_energies.count(None)
            energies_on_monuments = []
            te_in_monuments = 0
            for i in self.engine.monuments:
                binded = str(i.name) + ": " + str(i.binded_energies)
                energies_on_monuments.append(binded)
                te_in_monuments += len(i.binded_energies)
            te_total = te_in_poc
            te_total += te_in_monuments
            te_exhaust = len(self.engine.players[self.engine.current_player].exhausted_energies[Energy.SINGLE])
            te_released = len(self.engine.players[self.engine.current_player].energies_released[Energy.SINGLE])
            te_remaining = len(self.engine.players[self.engine.current_player].remaining_energies[Energy.SINGLE])
            te_transmuter = 0
            for tile in self.engine.players[self.engine.current_player].transmuter.active_tiles:
                te_transmuter += (tile.top_size - tile.top.count(0))
                te_transmuter += (tile.bottom_size - tile.bottom.count(0))
            te_total += te_exhaust
            te_total += te_released
            te_total += te_remaining
            te_total += te_transmuter
            total_energy_number = ["te_in_poc: " + str(te_in_poc), "te_in_monuments: " + str(te_in_monuments), "te_exhaust: " + str(te_exhaust), "te_released: " + str(te_released), "te_remaining: " + str(te_remaining), "te_transmuter: " + str(te_transmuter), "te_total: " + str(te_total)]

            turn_entry = {
                "player": self.engine.current_player,
                "turn_num": self.engine.turn_counter,
                "turn_type": str(self.engine.turn.turn_type),
                "action": actions[action.item(0)].action,
                "action_details": actions[action.item(0)].action_details,
                "current_score": self.rewards[self.agent_selection],
                "legal_actions": legal_actions,
                "player_transmuter_energies": str(
                    self.engine.players[
                        self.engine.current_player
                    ].transmuter.print_energies()
                ),
                "player_exhausted_energies": str(
                    self.engine.players[self.engine.current_player].exhausted_energies
                ),
                "player_released_energies": str(
                    self.engine.players[self.engine.current_player].energies_released
                ),
                "player_remaining_energies": str(
                    self.engine.players[self.engine.current_player].remaining_energies
                ),
                "energies_on_poc": str(energies_on_poc),
                "energies_on_monuments": str(energies_on_monuments),
                "total_energy_number": str(total_energy_number),
                "player_sentient_track": str(self.engine.players[self.engine.current_player].sentient_track.track),
                "player_transformative_track": str(self.engine.players[self.engine.current_player].transformative_track.track),
                # "monuments": str(self.engine.monuments),
                "current_wall_name": current_monument.name,
                # "c_w_accepted_energies": str(
                #     cur_monument_sections
                # ),  # str(current_monument.get_top_wall().sections),
                "c_w_remaining_sections": str(
                    cur_monument_remaining_sections
                ),  # str(current_monument.get_top_wall().remaining_sections),
                "c_w_remaining_section_num": str(
                    current_monument.get_top_wall().empty_sections
                ),
                "c_w_filled_sections": str(
                    cur_monument_filled_sections
                ),  # str(current_monument.get_top_wall().filled_sections),
                # "all_actions": action_details
                # "action_mask": action_mask
            }
        
        self.engine.play_turn(self.agent_selection, action)

        # Assign rewards for players, updates only not incremental
        temp_reward = self.engine.assign_temp_rewards(action)
        Logger.log("TEMP REWARDS" + str(temp_reward), "GAME_ENGINE_LOGS")
        self.rewards[self.agent_selection] += temp_reward
        turn_entry["current_score"] = self.rewards[self.agent_selection]
        self.simulation_history[str(self.engine.action_counter)] = turn_entry

        if self.engine.check_over():
            for agent in self.agents:
                Logger.log(
                    "FINAL REWARDS" + str(self.engine.get_reward(agent)),
                    "GAME_ENGINE_LOGS",
                )
                self.rewards[agent] += self.engine.get_reward(agent)
                self._cumulative_rewards[agent] = self.rewards[agent]

            # If game is over assign termination for all agents
            Logger.log(str(self.rewards), "INITIALIZATION_LOGS")
            self.simulation_history["meta_data"] = self.rewards
            actionList = self.engine.get_action_names()
            history_writer.jsonActionConverter("ai_history", actionList)
            self.terminations = {i: True for i in self.agents}
            self._accumulate_rewards()

        # Assign current players turn
        self.agent_selection = self.engine.get_current_agents_turn()

        # Don't know what this does

        if self.render_mode == "human":
            self.render()

        Logger.log(
            "env.py - @@@@@@@@@@@@@@@@@@@@ END STEP FUNCTION @@@@@@@@@@@@@@@@@@@@@@@@@",
            "INITIALIZATION_LOGS",
        )

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
                "You are calling render method without specifying any render mode."
            )
            return
        self.engine.render(self.agent_selection)

    def close(self):
        pass


if __name__ == "__main__":
    from pettingzoo.test import api_test  # noqa: E402

    api_test(env(), num_cycles=1_000_000)
