from matplotlib import pyplot as plt
import json

# read JSON output file
tictactoeJSON = open('tic-tac-toe_json.json','r')
gameJsonData=tictactoeJSON.read()

# parse JSON data to python, use load function
games = json.loads(gameJsonData)

#print(obj)
print(len(games))
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
explode = [0, 0.3, 0]
plt.pie(winRate, labels=position, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title("tictactoe Winrate PieChart")
plt.tight_layout()
plt.savefig('tic-tac-toe-PieChart.png')
plt.show()