python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pip install pettingzoo==1.22.1
pip install packaging==21.3
pip install git+https://github.com/WillDudley/tianshou.git

Run with:
python main.py --agent-id 1 --resume-path log/AnAgeContrived/dqn/policy.pth --opponent-path log/AnAgeContrived/dqn/policy.pth --seed 3435
