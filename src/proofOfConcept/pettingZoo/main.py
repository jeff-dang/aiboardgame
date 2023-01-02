import tictactoe_env
from pettingzoo.test import api_test
from pettingzoo.classic import tictactoe_v3
env = tictactoe_env.env()
env.reset()
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()
    action = None if termination or truncation else env.action_space(agent).sample()
    env.step(action)