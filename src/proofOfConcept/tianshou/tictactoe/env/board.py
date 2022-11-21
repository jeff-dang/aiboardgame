# Add player turn to game engine and remove from environment

class Board:
    def __init__(self):
        # internally self.board.squares holds a flat representation of tic tac toe board
        # where an empty board is [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # where indexes are column wise order
        # 0 3 6
        # 1 4 7
        # 2 5 8

        # empty -- 0
        # player 0 -- 1
        # player 1 -- 2

        self.squares = [0] * 16

        # index 0 = player 1's moves left, index 1 = player 2's moves left
        # special move lets a player remove the other players space, but they skip a turn
        self.specialMovesLeft = [4, 6]
        # precommute possible winning combinations
        self.calculate_winners()

    def setup(self):
        self.specialMovesLeft = [2, 2]
        self.calculate_winners()

    def play_turn(self, agent, action):
        # if spot is empty
        if action <= 15:
            if self.squares[action] != 0:
                return
            if agent == 0:
                self.squares[action] = 1
            elif agent == 1:
                self.squares[action] = 2
        else:
            if self.specialMovesLeft[agent] > 0 and (self.squares[action-16] != (agent+1) or self.squares[action-16] != 0):
                self.squares[action-16] = agent+1
                print(action-16)
                self.specialMovesLeft[agent] = self.specialMovesLeft[agent] - 1
        return

    def calculate_winners(self):
        winning_combinations = []
        vert = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15)]
        horiz = [(0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15)]
        corner = [(0, 3, 12, 15)]
        diags = [(0, 5, 10, 15), (3, 6, 9, 12)]

        square1 = [(0, 1, 4, 5), (4, 5, 8, 9), (8, 9, 12, 13)]
        square2 = [(1, 2, 5, 6), (5, 6, 9, 10), (9, 10, 13, 14)]
        square3 = [(2, 3, 6, 7), (6, 7, 10, 11), (10, 11, 14, 15)]

        winning_combinations = (
            vert + horiz + corner + diags + square1 + square2 + square3)
        self.winning_combinations = winning_combinations

    # returns:
    # -1 for no winner
    # 0 -- agent 0 wins
    # 1 -- agent 1 wins
    def check_for_winner(self):
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

    def check_game_over(self):
        winner = self.check_for_winner()

        if winner == -1 and all(square in [1, 2] for square in self.squares):
            # tie
            return True
        elif winner in [1, 2]:
            return True
        else:
            return False

    def __str__(self):
        return str(self.squares)


if __name__ == "__main__":
    # train the agent and watch its performance in a match!
    b = Board()
    b.check_for_winner()

    def getSymbol(input):
        if input == 0:
            return "-"
        elif input == 1:
            return "X"
        else:
            return "O"

    board = list(map(getSymbol, b.squares))
    print("#" * 22)
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {board[0]}  " + "|" + f"  {board[4]}  " +
          "|" + f"  {board[8]} " + " |" + f"  {board[12]} ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)

    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {board[1]}  " + "|" + f"  {board[5]}  " +
          "|" + f"  {board[9]} " + " |" + f"  {board[13]} ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)

    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {board[2]}  " + "|" + f"  {board[6]}  " +
          "|" + f"  {board[10]} " + " |" + f"  {board[14]} ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)

    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {board[3]}  " + "|" + f"  {board[7]}  " +
          "|" + f"  {board[11]} " + " |" + f"  {board[15]} ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5 + "|" + " " * 5)
