# Author: Jonah Ada
# Date: January 27th, 2023
# Description: 
# Starting point for the custom environment

from env.env import env, raw_env

# main loop
if __name__ == "__main__":
    from pettingzoo.test import api_test  # noqa: E402
    api_test(env(render_mode="human"), num_cycles=1_000_000)
