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

position = ['Button Left', 'Button Mid', 'Button Right']
winRate = []
winRate.append(BLCounter)
winRate.append(BMCounter)
winRate.append(BRCounter)
print(winRate)

plt.barh(position, winRate)

plt.title("tictactoe Win games of x in different position")
plt.ylabel("Position")
plt.xlabel("Number of Win Game")

plt.tight_layout()
plt.savefig('tic-tac-toe-barh.png')
plt.show()



