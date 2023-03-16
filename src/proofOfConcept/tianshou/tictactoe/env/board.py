# Add player turn to game engine and remove from environment
import random


class Board:
    def __init__(self):
        self.squares = [0] * 16
        # index 0 = player 1's moves left, index 1 = player 2's moves left
        # special move lets a player remove the other players space, but they skip a turn
        self.specialMovesLeft = [2, 6]
        self.currentPlayer = 0
        # precommute possible winning combinations
        self.calculate_winners()

    def getPlayer(self):
        return self.currentPlayer

    def setup(self):
        self.specialMovesLeft = [2, 6]
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

            #self.currentPlayer = (self.currentPlayer + 1) % 2
        else:
            if self.specialMovesLeft[agent] > 0 and (self.squares[action-16] != (agent+1) or self.squares[action-16] != 0):
                self.squares[action-16] = 0
                self.specialMovesLeft[agent] = self.specialMovesLeft[agent] - 1

        self.currentPlayer = random.randint(0, 1)

        return

    def calculate_winners(self):
        winning_combinations = []
        # 0 1 2
        # 3 4 5
        # 6 7 8
        vert = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        horiz = [(0, 3, 6), (1,4,7), (2,5,8)]
        diags = [(0, 4, 8), (2,4,6)]

        winning_combinations = (vert + horiz + diags)
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
