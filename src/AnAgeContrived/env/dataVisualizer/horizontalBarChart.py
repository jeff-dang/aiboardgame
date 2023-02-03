from matplotlib import pyplot as plt
import json

from jsonParser import JSONParser

class HorizontalBarChart:
    def __init__(self, jsonInput, chartTitle):
        self.jsonInput = jsonInput
        self.chartTitle = chartTitle
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

    def get_HorizontalBarChart(self):
        games = self.jsonInput
        print("games")
        print(games)
        BLCounter = 0
        BMCounter = 0
        BRCounter = 0
        for game in games:
            # if games["BL"] == "x" and games["class"] == True:
            #     counter = counter +1
            if 'x' in game['BL'] and game['class']==True:
                BLCounter = BLCounter +1
            if 'x' in game['BM'] and game['class']==True:
                BMCounter = BMCounter +1
            if 'x' in game['BR'] and game['class']==True:
                BRCounter = BRCounter +1
        print("BLCounter: "+ str(BLCounter)+ " "+ "BMCounter: "+ str(BMCounter) + " "+ "BRCounter: "+ str(BRCounter))
        position = ['ButtonLeft', 'ButtonMid', 'ButtonRight']
        winRate = []
        winRate.append(BLCounter)
        winRate.append(BMCounter)
        winRate.append(BRCounter)
        print("Output is below")
        print(position)
        print(winRate)
        #explode = [0, 0.3, 0]
        chartTitle = self.chartTitle
        plt.barh(position, winRate)

        plt.title(chartTitle)
        plt.tight_layout()
        plt.savefig('tic-tac-toe-barh.png')
        plt.show()

p1 = JSONParser("tic-tac-toe_json.json")

pc1 = HorizontalBarChart(p1.get_jsonOutput(),"tictactoe Winrate PieChart")
pc1.get_HorizontalBarChart()