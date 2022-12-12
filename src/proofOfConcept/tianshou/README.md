python -m venv venv
source venv/bin/activate

pip install pettingzoo==1.22.1
pip install packaging==21.3
pip install git+https://github.com/WillDudley/tianshou.git

run it once with python main.py --agent-id 1
will run it with training user with X

afterwards can run, will run both agents with training data
python main.py --agent-id 1 --resume-path log/tic_tac_toe/dqn/policy.pth --opponent-path log/tic_tac_toe/dqn/policy.pth --seed 123
python main.py --agent-id 2 --resume-path log/tic_tac_toe/dqn/policy.pth --opponent-path log/tic_tac_toe/dqn/policy.pth --seed 123

play around with params to get diff outputs

add whos turn it is in game engine and action mask and legal moves in engine
small - reward, big for winning, doesnt matter at the end
discrete action space and translator to translate move index to move
use json library to write json file
explain that libaray ai was apart of exploratory stage and caused risks cause badly documented
