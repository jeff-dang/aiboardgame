from env.action_initiater import get_actions

class Engine:
    def __init__(self):
        self.turn_counter: int = 0
        self.current_player: int = 0
        self.players: list[str] = ['player_0', 'player_1']
        self.winning_combinations = self.calculate_winners()
        self.board = [0,0,0,0,0,0,0,0,0]
    def get_agents(self):
        return self.players
    
    def calculate_winners(self):
        winning_combinations = []
        vert = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        horiz = [(0, 3, 6), (1,4,7), (2,5,8)]
        diags = [(0, 4, 8), (2,4,6)]
        winning_combinations = (vert + horiz + diags)
        return winning_combinations

    def check_over(self):
        winner = -1
        for combination in self.winning_combinations:
            states = []
            for index in combination:
                states.append(self.squares[index])
            if all(x == 1 for x in states):
                winner = 1
            if all(x == 2 for x in states):
                winner = 2
        return winner

    def reset(self):
        self.__init__()

    def get_action_names(self) -> list[dict[str, str]]:
        actions = get_actions(self.players[self.current_player], self)
        action_names: list[dict[str, str]] = []
        for i, a in enumerate(actions):
            action_names.append(
                {"index": i, "action": a.action, "action_details": a.action_details}
            )
        return action_names

    def get_action_index(self, name):
        list = self.get_action_names()
        index = -1
        for action in list:
            if name in action["action_details"]:
                index = action["index"]
                break
        return index

    def get_legal_action_names(self, agent_name: str) -> list[str]:
        actions = get_actions((agent_name), self)
        legal_actions: list[str] = []
        for i, action in enumerate(actions):
            if action.check():
                legal_actions.append(
                    str(i) + ": " + action.action + " " + action.action_details
                )
        return legal_actions

    def get_action_space(self) -> int:
        return 9

    def get_legal_actions(self, agent_name: str):
        actions = get_actions((agent_name), self)
        legal_actions = []
        for action in actions:
            is_legal = action.check()
            legal_actions.append(is_legal)
        return legal_actions

    def play_turn(self, agent_name: str, action):

               # checks whether the action is legal or not
        if not self.get_legal_actions(self.get_agents()[self.current_player])[action]:
            return False

        actions = get_actions(self.players[self.current_player], self)
        actions[action].execute()

  
        self.turn_counter += 1
        return True

    def get_current_agents_turn(self) -> str:
        return self.get_agents()[self.current_player]

    def get_game_state(self):
        
        return []

    def get_reward(self, agent_name):
        
        return 0

  
    def render(self):
        def getSymbol(input):
            if input == 0:
                return "-"
            elif input == 1:
                return "X"
            else:
                return "O"

        board = list(map(getSymbol, self.board.squares))

        print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
        print(f"  {board[0]}  " + "|" + f"  {board[3]}  " + "|" + f"  {board[6]}  ")
        print("_" * 5 + "|" + "_" * 5 + "|" + "_" * 5)

        print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
        print(f"  {board[1]}  " + "|" + f"  {board[4]}  " + "|" + f"  {board[7]}  ")
        print("_" * 5 + "|" + "_" * 5 + "|" + "_" * 5)

        print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
        print(f"  {board[2]}  " + "|" + f"  {board[5]}  " + "|" + f"  {board[8]}  ")
        print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)

    
    


    

 