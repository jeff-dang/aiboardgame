import gymnasium
import numpy as np
from gymnasium import spaces
from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers
from engine import Engine


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
        self.engine = Engine()

        self.agents = self.engine.get_agents()
        self.possible_agents = self.agents[:]
        self.action_spaces = {i: spaces.Discrete(self.engine.get_action_space())
                              for i in self.agents}
        self.observation_spaces = {
            i: spaces.Dict(
                {
                    "observation": spaces.Box(
                        low=0, high=1, shape=(self.engine.get_observation_space_shape()), dtype=np.int8
                    ),
                    "action_mask": spaces.Box(low=0, high=1, shape=(self.engine.get_action_space(),), dtype=np.int8),
                }
            )
            for i in self.agents
        }
        self.rewards = {i: 0 for i in self.agents}
        self.terminations = {i: False for i in self.agents}
        self.truncations = {i: False for i in self.agents}
        self.infos = {i: {} for i in self.agents}
        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.reset()
        self.render_mode = render_mode

    def observe(self, agent):

        # Get Action Space Vector and check legal moves
        action_mask = np.array(
            self.engine.get_legal_actions(agent), dtype="int8")

        observation = self.engine.get_game_state(agent)
        return {"observation": observation, "action_mask": action_mask}

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]

    def _legal_moves(self, agent):
        return self.engine.get_legal_actions(agent)

    def step(self, action):

        # Check if terminations or truncations for current agent
        if (
            self.terminations[self.agent_selection]
            or self.truncations[self.agent_selection]
        ):
            return self._was_dead_step(action)

        # Check if action is a legal move
        # Get index of current agent self.agents.index(self.agent_selection)
        # Get name of current agent self.agent_selection

        # Play turn, pass in agent name
        self.engine.play_turn(self.agent_selection, action)

        # Assign rewards for players

        # If game is over assign termination for all agents
        # self.terminations = {i: True for i in self.agents}

        # Assign current players turn
        self.agent_selection = self.engine.get_current_agents_turn()

        # Don't know what this does
        self._cumulative_rewards[self.agent_selection] = 0
        self._accumulate_rewards()

        if self.render_mode == "human":
            self.render()

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

    def render(self):
        if self.render_mode is None:
            gymnasium.logger.warn(
                "You are calling render method without specifying any render mode.")
            return
        self.engine.render()

    def close(self):
        pass


if __name__ == "__main__":
    from pettingzoo.test import api_test  # noqa: E402
    api_test(env(), num_cycles=1_000_000)
