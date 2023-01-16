from matplotlib import pyplot as plt
import json

# read JSON output file
tictactoeJSON = open('tic-tac-toe_json.json','r')
gameJsonData=tictactoeJSON.read()

# parse JSON data to python, use load function
games = json.loads(gameJsonData)

#print(obj)
#print(len(games))
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
plt.bar(index, winList)

plt.title("tictactoe Steps to win for player x")
plt.xlabel("steps")
plt.ylabel("Number of Win Game")

plt.tight_layout()
plt.savefig('tic-tac-toe-barh-StepWin.png')
plt.show()