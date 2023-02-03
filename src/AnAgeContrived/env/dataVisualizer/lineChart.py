from matplotlib import pyplot as plt
import json
import pandas as pd
import numpy as np
from jsonParser import JSONParser

class LineChart:
    def __init__(self, jsonInput, chartTitle, rounds, targetDataType):
        self.jsonInput = jsonInput
        self.chartTitle = chartTitle
        #self.rounds = rounds
        self.targetDataType = targetDataType

        #object
        #percentage
    def get_jsonInput(self):
        return self.jsonInput

    def set_jsonInput(self, jsonInput):
        self.jsonInput = jsonInput
    
    def get_chartTitle(self):
        return self.chartTitle
        
    def set_chartTitle(self, chartTitle):
        self.chartTitle = chartTitle

    def get_rounds(self):
        return self.rounds

    def set_rounds(self, rounds):
        self.rounds = rounds

    def get_targetDataType(self):
        return self.targetDataType

    def set_targetDataType(self, targetDataType):
        self.targetDataType = targetDataType

    def get_LineChart(self):
        games = self.jsonInput
        print("games")
        print(games)
        GDB = pd.read_json('scoresState.json')
        print(GDB)
        
        st = self.rounds
        sc = self.targetDataType

        State1 = [i[st] for i in GDB["Player1"]]
        Score1 = [i[sc] for i in GDB["Player1"]]

        State2 = [i[st] for i in GDB["Player2"]]
        Score2 = [i[sc] for i in GDB["Player2"]]

        Score1 =  np.array(Score1)
        Score2 =  np.array(Score2)
        print(State1)
        print(Score1)
        print(Score2)

        plt.plot(State1, Score1, label='Player1')
        plt.plot(State1, Score2, label='Player2', linewidth = 3)

        plt.fill_between(State1, Score1, Score2,
                        where=(Score1>Score2),
                        interpolate=True, alpha=0.25, label='p1Scores > p2Scores')

        plt.fill_between(State1, Score1, Score2,
                        where=(Score1 <= Score2),
                        interpolate=True, color='red', alpha=0.25, label='p1Scores <= p2Scores')

        plt.xlabel('Game States')
        plt.ylabel('Game Scores')
        plt.title('States VS Scores Change')

        plt.legend()
        #To get some padding for the Line
        plt.tight_layout()

        #Adding grid
        plt.grid(True)

        #Save the output graph in the same directory
        plt.savefig('plot.png')

        plt.show()

p1 = JSONParser("scoresState.json")

pc1 = LineChart(p1.get_jsonOutput(),"tictactoe Winrate PieChart", "State", "Scores")
pc1.get_LineChart()