import csv
import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
from matplotlib import pyplot as plt

data = pd.read_csv('tic-tac-toe.csv')

#print(data.describe())
TL = data['TL']
TM = data['TM']
TR = data['TR']
ML = data['ML']
MM = data['MM']
MR = data['MR']
BL = data['BL']
BM = data['BM']
BR = data['BR']
result = data['result']
input = str(input("Please a Position in tic-tac-toe game: "))
winMM = data.groupby(input)["result"].mean()
print(winMM)
sns.barplot(data = data, y="result", x=input, ci = None)

plt.title("Win rate based on "+input)

plt.show()










