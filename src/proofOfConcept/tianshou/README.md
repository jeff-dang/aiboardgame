python -m venv venv
source venv/bin/activate

pip install pettingzoo==1.22.1
pip install packaging==21.3
pip install git+https://github.com/WillDudley/tianshou.git

run it once with python main.py --agent-id 1
will run it with training user with X

afterwards can run, will run both agents with training data
python main.py --agent-id 1 --resume-path log/tic_tac_toe/dqn/policy.pth --opponent-path log/tic_tac_toe/dqn/policy.pth

play around with params to get diff outputs
