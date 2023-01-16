from matplotlib import pyplot as plt
import json
import pandas as pd
import numpy as np
# read JSON output file
tictactoeJSON = open('scoresState.json','r')
gameJsonData=tictactoeJSON.read()

# parse JSON data to python, use load function
games = json.loads(gameJsonData)
# print(games)
GDB = pd.read_json('scoresState.json')
print(GDB)


State1 = [i["State"] for i in GDB["Player1"]]
Score1 = [i["Scores"] for i in GDB["Player1"]]

State2 = [i["State"] for i in GDB["Player2"]]
Score2 = [i["Scores"] for i in GDB["Player2"]]

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


