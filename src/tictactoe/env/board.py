# Add player turn to game engine and remove from environment
import random


class Board:
    def __init__(self):
        self.squares = [0] * 9
        # index 0 = player 1's moves left, index 1 = player 2's moves left
        # special move lets a player remove the other players space, but they skip a turn
        self.specialMovesLeft = [0, 0]
        self.currentPlayer = 0
        # precommute possible winning combinations
        self.calculate_winners()
        self.turn_num = 0

    def getPlayer(self):
        return self.currentPlayer

    def setup(self):
        self.specialMovesLeft = [0, 0]
        self.calculate_winners()
        self.turn_num = 0

    def play_turn(self, agent, action):
        # if spot is empty
       
        if agent == 0:
            self.squares[action] = 1
        elif agent == 1:
            self.squares[action] = 2

        if(action != 0):
            self.currentPlayer = (self.currentPlayer + 1) % 2
        
        self.turn_num +=1
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


