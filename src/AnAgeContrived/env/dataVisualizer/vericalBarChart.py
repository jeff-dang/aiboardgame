from matplotlib import pyplot as plt
import json

from jsonParser import JSONParser

class VerticalBarChart:
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

    def get_VerticalBarChart(self):
        games = self.jsonInput
        print("games")
        print(games)
        counterList = []
        for game in games:
            counter=0
            win = False
            
            for pos in game.values():
                if pos =="x":
                    counter = counter +1
                    #print(counter)
                if pos == True:
                    win = True
            if(win==True):
                counterList.append(counter)
        print(counterList)
        c3= 0
        c4 = 0
        c5 = 0
        c6 = 0
        for i in counterList:
            if(i==3):
                c3= c3+1
            elif(i==4):
                c4= c4+1
            elif(i==5):
                c5= c5+1
            elif(i==6):
                c6= c6+1

        index = ["3 steps","4 steps","5 steps","6 steps"]
        winList = [c3, c4, c5, c6]
        chartTitle = self.chartTitle
        plt.bar(index, winList)

        plt.title(chartTitle)
        plt.xlabel("steps")
        plt.ylabel("Number of Win Game")

        plt.tight_layout()
        plt.savefig('tic-tac-toe-barh-StepWin.png')
        plt.show()

p1 = JSONParser("tic-tac-toe_json.json")

pc1 = VerticalBarChart(p1.get_jsonOutput(),"tictactoe Winrate PieChart")
pc1.get_VerticalBarChart()